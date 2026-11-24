"""Previsualiza o instala únicamente hub-guide desde una revisión local."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = "skills/hub-guide/SKILL.md"
DESTINATIONS = {
    "codex": Path(".agents/skills/hub-guide"),
    "antigravity": Path(".gemini/config/skills/hub-guide"),
}
STABLE = re.compile(r"v[0-9]+\.[0-9]+\.[0-9]+")


def git(root, *arguments):
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *arguments],
            stdin=subprocess.DEVNULL, capture_output=True, check=True,
        )
    except FileNotFoundError as exc:
        raise ValueError("Git no está disponible. Usa el procedimiento manual de la guía.") from exc
    except subprocess.CalledProcessError as exc:
        raise ValueError(f"Git no pudo consultar la revisión local ({arguments[0]}).") from exc
    return result.stdout


def reviewed_source(root, allow_unreleased):
    top = Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    if top != root:
        raise ValueError("Ejecuta la utilidad desde un checkout propio del Hub.")
    commit = git(root, "rev-parse", "HEAD").decode().strip()
    tags = git(root, "tag", "--points-at", commit).decode().splitlines()
    stable = [tag for tag in tags if STABLE.fullmatch(tag)]
    version = max(stable, key=lambda tag: tuple(map(int, tag[1:].split("."))), default=None)
    if version is None and not allow_unreleased:
        raise ValueError("HEAD no tiene una etiqueta estable. Revisa la edición estable publicada.")
    try:
        manifest = git(root, "show", f"{commit}:{SKILL}")
    except ValueError as exc:
        raise ValueError("La revisión elegida todavía no distribuye hub-guide.") from exc
    return manifest, {"checkout": str(root), "commit": commit, "version": version}


def install(destination, files):
    destination.mkdir(parents=True, exist_ok=False)
    created = []
    try:
        for name, contents in files.items():
            path = destination / name
            with path.open("xb") as stream:
                created.append(path)
                stream.write(contents)
    except OSError:
        for path in reversed(created):
            path.unlink()
        destination.rmdir()
        raise


def main(argv=None, *, root=ROOT, user_home=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client", choices=DESTINATIONS, required=True)
    parser.add_argument("--apply", metavar="COMMIT", help="copiar la revisión mostrada en la previsualización")
    parser.add_argument("--allow-unreleased", action="store_true", help="usar HEAD sin etiqueta estable para un ensayo")
    args = parser.parse_args(argv)
    apply = args.apply is not None
    home = (Path.home() if user_home is None else user_home).resolve()
    destination = home / DESTINATIONS[args.client]
    try:
        if not destination.parent.resolve().is_relative_to(home):
            raise ValueError("El destino resuelve fuera del directorio de usuario.")
        if destination.exists() or destination.is_symlink():
            print(f"Ya existe una entrada en {destination}. Revísala antes de actualizar.")
            return 1 if apply else 0

        manifest, receipt = reviewed_source(root.resolve(), args.allow_unreleased)
        if apply and args.apply != receipt["commit"]:
            raise ValueError("El commit indicado difiere de HEAD. Repite la previsualización.")
        receipt["sha256"] = hashlib.sha256(manifest).hexdigest()
        files = {
            "SKILL.md": manifest,
            "hub-source.json": (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        }
        version = receipt["version"] or "revisión sin etiqueta estable"
        print(f"{version} · {receipt['commit']}\nDestino: {destination}")
        print(f"Archivos: {', '.join(files)}\nSHA-256 de SKILL.md: {receipt['sha256']}")
        if apply:
            install(destination, files)
            print("Skill copiada.")
        else:
            print(f"Previsualización. Usa --apply {receipt['commit']} para efectuar la copia.")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
