"""Consulta y validación local de Agent Engineering Hub."""
import argparse
import json
import re
import sys
from datetime import date
from graphlib import CycleError, TopologicalSorter
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ("codex", "antigravity")
LEVELS = {"essential": "esencial", "recommended": "recomendada",
          "optional": "opcional", "not-applicable": "no aplicable"}


class Invalid(ValueError):
    """Dato o combinación que no cumple el contrato."""


def unique_mapping(pairs):
    result = {}
    for key, value in pairs:
        if not isinstance(key, str) or key in result:
            raise Invalid(f"Clave repetida o no textual: {key!r}")
        result[key] = value
    return result


class DataLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        return unique_mapping(self.construct_pairs(node, deep=deep))

    def compose_node(self, parent, index):
        if self.check_event(yaml.AliasEvent):
            raise Invalid("Los alias YAML quedan fuera del formato de datos del Hub")
        return super().compose_node(parent, index)


def local(root, path):
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise Invalid(f"Referencia fuera del Hub: {path}")
    return resolved


def read(path):
    if path.stat().st_size > 1_000_000:
        raise Invalid(f"{path}: archivo demasiado grande para una ficha o documento")
    return path.read_text(encoding="utf-8-sig")


def parse(path, source=None):
    try:
        raw = read(path) if source is None else source
        if path.suffix == ".json":
            return json.loads(raw, object_pairs_hook=unique_mapping)
        return yaml.load(raw, Loader=DataLoader)
    except (ValueError, yaml.YAMLError, RecursionError) as exc:
        raise Invalid(f"{path}: {exc}") from exc


def contract(name, root=ROOT):
    path = local(root, root / "schemas" / f"{name}.schema.json")
    schema = parse(path)
    if not isinstance(schema, dict) or schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise Invalid(f"{path}: se requiere JSON Schema 2020-12")
    # Los contratos se distribuyen completos y no necesitan resolución por red.
    nodes = [schema]
    while nodes:
        node = nodes.pop()
        if isinstance(node, dict):
            for field in ("$ref", "$dynamicRef"):
                if field in node and not str(node[field]).startswith("#"):
                    raise Invalid(f"{path}: referencia de esquema externa: {node[field]}")
            nodes.extend(node.values())
        elif isinstance(node, list):
            nodes.extend(node)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise Invalid(f"{path}: {exc.message}") from exc
    return Draft202012Validator(schema, format_checker=FormatChecker())


def check(validator, data, path):
    error = next(validator.iter_errors(data), None)
    if error:
        raise Invalid(f"{path} {error.json_path}: {error.message}")


def records(root, folder, kind):
    validator = contract(kind)
    result = {}
    directory = local(root, root / folder)
    for path in sorted(directory.iterdir()):
        if path.suffix not in {".json", ".yaml", ".yml"}:
            raise Invalid(f"Archivo no reconocido en {folder}: {path.name}")
        data = parse(local(root, path))
        check(validator, data, path)
        key = data["id"]
        if key in result or key != path.stem:
            raise Invalid(f"{path}: ID duplicado o distinto del nombre de archivo: {key}")
        result[key] = data
    if not result:
        raise Invalid(f"{folder} vacío")
    return result


def graph(caps):
    for key, cap in caps.items():
        for other in cap["depends_on"] + cap["conflicts_with"]:
            if other not in caps or other == key:
                raise Invalid(f"{key}: referencia inválida a {other}")
    sorter = TopologicalSorter({key: cap["depends_on"] for key, cap in caps.items()})
    try:
        return tuple(sorter.static_order())
    except CycleError as exc:
        raise Invalid(f"Ciclo de dependencias: {' -> '.join(exc.args[1])}") from exc


def choices_for(profile, caps):
    choices = {}
    for row in profile["choices"]:
        key = row["id"]
        if key not in caps or key in choices:
            raise Invalid(f"{profile['id']}: capacidad desconocida o repetida: {key}")
        if set(row["when"]) - profile["conditions"].keys():
            raise Invalid(f"{profile['id']}: condición no definida para {key}")
        if row["level"] != "not-applicable" and set(caps[key]["requires_stack"]) - set(profile["stack"]):
            raise Invalid(f"{profile['id']}: stack incompatible con {key}")
        choices[key] = row
    return choices


def select(profile, caps, agent, contexts=(), include=()):
    order = graph(caps)
    choices = choices_for(profile, caps)
    enabled, requested = set(contexts), set(include)
    if enabled - profile["conditions"].keys():
        raise Invalid("Condiciones desconocidas: " + ", ".join(sorted(enabled - profile["conditions"].keys())))
    if requested - choices.keys():
        raise Invalid("Se solicitaron capacidades fuera del perfil: " + ", ".join(sorted(requested - choices.keys())))
    selected, skipped = {}, {}
    for key, row in choices.items():
        missing = set(row["when"]) - enabled
        if row["level"] == "not-applicable":
            skipped[key] = "no aplicable"
        elif missing:
            skipped[key] = "requiere condición " + ", ".join(sorted(missing))
        elif agent not in caps[key]["agents"]:
            skipped[key] = f"agente incompatible: {agent}"
            if row["level"] == "essential":
                raise Invalid(f"{key}: {skipped[key]}")
        elif row["level"] != "optional" or key in requested:
            selected[key] = row["reason"]
        else:
            skipped[key] = "opcional; requiere --include"
        if key in requested and key in skipped:
            raise Invalid(f"{key}: {skipped[key]}")
    for key in reversed(order):
        if key not in selected:
            continue
        for dep in caps[key]["depends_on"]:
            if dep not in choices:
                raise Invalid(f"{key}: dependencia no disponible: {dep}")
            row = choices[dep]
            if agent not in caps[dep]["agents"] or set(row["when"]) - enabled or row["level"] == "not-applicable":
                raise Invalid(f"{key}: dependencia incompatible: {dep}")
            skipped.pop(dep, None)
            selected.setdefault(dep, f"dependencia de {key}")
    for key in selected:
        conflicts = set(caps[key]["conflicts_with"]) & selected.keys()
        if conflicts:
            raise Invalid(f"{key}: conflicto con {', '.join(sorted(conflicts))}")
    return {key: selected[key] for key in order if key in selected}, skipped


def check_profile(profile, caps):
    choices = choices_for(profile, caps)
    # Las condiciones son conjunciones positivas: las de la raíz deben bastar
    # también para sus dependencias. Los conflictos entre opcionales se comprueban
    # al pedir la combinación; dos alternativas pueden coexistir en un perfil.
    for key, row in choices.items():
        if row["level"] == "not-applicable":
            continue
        for dep in caps[key]["depends_on"]:
            needed = choices.get(dep)
            if (not needed or needed["level"] == "not-applicable"
                    or set(needed["when"]) - set(row["when"])
                    or set(caps[key]["agents"]) - set(caps[dep]["agents"])):
                raise Invalid(f"{profile['id']}: {key} tiene dependencia incompatible: {dep}")
    for agent in AGENTS:
        select(profile, caps, agent, profile["conditions"])
        for key, row in choices.items():
            if row["level"] == "optional" and agent in caps[key]["agents"]:
                select(profile, caps, agent, profile["conditions"], [key])


def check_skills(root, caps):
    validator = contract("skill")
    actual = set()
    for base in ("skills", ".agents/skills"):
        for folder in local(root, root / base).iterdir():
            path = local(root, folder / "SKILL.md")
            parts = re.split(r"^---[ \t]*$", read(path), flags=re.M)
            if len(parts) < 3 or parts[0].strip() or not "".join(parts[2:]).strip():
                raise Invalid(f"{path}: se requiere frontmatter y cuerpo")
            data = parse(path, parts[1])
            check(validator, data, path)
            if data["name"] != folder.name or folder.name in actual:
                raise Invalid(f"{path}: nombre duplicado o distinto de la carpeta")
            cap = caps.get(folder.name, {})
            if cap.get("type") != "skill" or cap.get("entry") != path.relative_to(root).as_posix():
                raise Invalid(f"{path}: falta ficha correspondiente")
            actual.add(folder.name)
    expected = {key for key, cap in caps.items() if cap["origin"] == "hub" and cap["type"] == "skill"}
    if expected != actual:
        raise Invalid(f"Skills sin correspondencia: {sorted(expected ^ actual)}")
    return len(actual)


def check_links(root):
    directories = ["docs", "examples", "templates", "workflows", "mcp", "skills", ".agents", ".github"]
    documents = list(root.glob("*.md"))
    for name in directories:
        documents.extend(local(root, root / name).rglob("*.md"))
    for doc in documents:
        body = re.sub(r"^\x60{3}.*?^\x60{3}[^\n]*", "", read(local(root, doc)), flags=re.M | re.S)
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", body):
            uri = urlsplit(target.strip("<>"))
            if uri.scheme in {"https", "http", "mailto"} or not uri.path:
                continue
            if not local(root, doc.parent / unquote(uri.path)).exists():
                raise Invalid(f"{doc}: enlace local inexistente: {target}")


def validate(root, caps, profiles):
    if root != ROOT:
        # Examinar los esquemas candidatos como datos; para las fichas se usan
        # siempre los contratos que acompañan al ejecutable de confianza.
        for name in ("capability", "profile", "skill"):
            contract(name, root)
    graph(caps)
    if caps.keys() & profiles.keys():
        raise Invalid("Un perfil y una capacidad comparten ID")
    for key, cap in caps.items():
        date.fromisoformat(cap["review"]["date"])
        if "entry" in cap and not local(root, root / cap["entry"]).is_file():
            raise Invalid(f"{key}: falta {cap['entry']}")
    count = check_skills(root, caps)
    for profile in profiles.values():
        check_profile(profile, caps)
    check_links(root)
    return f"OK: {len(caps)} capacidades, {len(profiles)} perfiles, {count} skills propias."


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="árbol de datos a inspeccionar")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    listing = sub.add_parser("list")
    listing.add_argument("--type", choices=["skill", "mcp", "workflow", "tool", "plugin", "rule"])
    listing.add_argument("--tech")
    sub.add_parser("profiles")
    show = sub.add_parser("show")
    show.add_argument("id")
    rec = sub.add_parser("recommend")
    rec.add_argument("profile")
    rec.add_argument("--agent", choices=AGENTS, default="codex")
    rec.add_argument("--context", action="append", default=[])
    rec.add_argument("--include", action="append", default=[])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        caps = records(root, "catalog", "capability")
        if args.command == "list":
            for cap in caps.values():
                if (not args.type or cap["type"] == args.type) and (not args.tech or args.tech in cap["technologies"]):
                    print(f"{cap['id']:24} {cap['type']:9} {cap['name']}")
            return 0
        profiles = records(root, "profiles", "profile")
        if args.command == "validate":
            print(validate(root, caps, profiles))
        elif args.command == "profiles":
            for profile in profiles.values():
                print(f"{profile['id']:28} {profile['activate_when']}")
        elif args.command == "show":
            item = caps.get(args.id) or profiles.get(args.id)
            if not item:
                raise Invalid(f"ID desconocido: {args.id}")
            print(json.dumps(item, indent=2, ensure_ascii=False))
        else:
            if args.profile not in profiles:
                raise Invalid(f"Perfil desconocido: {args.profile}")
            profile = profiles[args.profile]
            selected, skipped = select(profile, caps, args.agent, args.context, args.include)
            rows = {row["id"]: row for row in profile["choices"]}
            print(f"Propuesta local | {args.profile} | {args.agent}")
            for key, reason in selected.items():
                print(f"  + {key} [{LEVELS[rows[key]['level']]}] {reason}")
                if caps[key]["requirements"]:
                    print("    Requiere: " + " ".join(caps[key]["requirements"]))
            for key, reason in skipped.items():
                print(f"  - {key} [{reason}] {rows[key]['reason']}")
    except (ValueError, OSError, RecursionError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
