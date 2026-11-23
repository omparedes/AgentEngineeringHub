"""Regresiones del contrato, del grafo y de los comandos públicos."""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

from scripts import hub


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caps = hub.records(hub.ROOT, "catalog", "capability")
        cls.profiles = hub.records(hub.ROOT, "profiles", "profile")

    def test_release_validates(self):
        result = hub.validate(hub.ROOT, self.caps, self.profiles)
        self.assertTrue(result.startswith("OK:"))

    def test_all_profiles_for_both_agents(self):
        for profile in self.profiles.values():
            for agent in hub.AGENTS:
                with self.subTest(profile=profile["id"], agent=agent):
                    chosen, _ = hub.select(profile, self.caps, agent)
                    self.assertTrue(chosen)
                    self.assertTrue(all(agent in self.caps[key]["agents"] for key in chosen))

    def test_minimum_and_condition(self):
        p = self.profiles["angular-supabase-cloudflare"]
        chosen, _ = hub.select(p, self.caps, "codex", ["cambio-sql"])
        self.assertIn("supabase-skills", chosen)
        self.assertNotIn("supabase-mcp", chosen)
        chosen, _ = hub.select(p, self.caps, "codex", ["inspeccion-remota"], ["supabase-mcp"])
        self.assertIn("supabase-mcp", chosen)

    def test_modern_web_guidance_requires_frontend_work(self):
        capability = "modern-web-guidance"
        frontend_profiles = ("generic-web", "angular-frontend", "angular-supabase-cloudflare")
        for agent in hub.AGENTS:
            for profile_id, profile in self.profiles.items():
                with self.subTest(profile=profile_id, agent=agent):
                    default, _ = hub.select(profile, self.caps, agent)
                    self.assertNotIn(capability, default)
                    if profile_id in frontend_profiles:
                        selected, _ = hub.select(profile, self.caps, agent, ["trabajo-frontend"])
                        self.assertIn(capability, selected)
                    else:
                        self.assertNotIn(capability, {choice["id"] for choice in profile["choices"]})

    def test_engineering_capabilities_follow_confirmed_context(self):
        web_profiles = {"generic-web", "angular-frontend", "angular-supabase-cloudflare"}
        app_profiles = web_profiles - {"angular-frontend"}
        criteria = {
            "nextjs-16-dev": ("next-devtools-mcp", {"generic-web"}),
            "auditoria-accesibilidad": ("axe-core-playwright", web_profiles),
            "presupuesto-lighthouse": ("lighthouse-ci", web_profiles),
            "seguridad-aplicacion": ("owasp-asvs", app_profiles),
            "sentry-en-alcance": ("sentry-mcp", app_profiles | {"python-ai"}),
            "diseno-figma": ("figma-mcp", web_profiles),
        }
        additions = {capability for capability, _ in criteria.values()} | {"filesystem-mcp"}
        for profile_id, profile in self.profiles.items():
            for agent in hub.AGENTS:
                with self.subTest(profile=profile_id, agent=agent):
                    default, _ = hub.select(profile, self.caps, agent)
                    self.assertFalse(additions & default.keys())
                    for context, (capability, eligible) in criteria.items():
                        if profile_id in eligible:
                            selected, _ = hub.select(profile, self.caps, agent, [context])
                            self.assertEqual(set(selected) - default.keys(), {capability})
                        else:
                            with self.assertRaises(hub.Invalid):
                                hub.select(profile, self.caps, agent, [context])
                    profile_options = {choice["id"] for choice in profile["choices"]}
                    self.assertNotIn("filesystem-mcp", profile_options)
                    if profile_id != "generic-web":
                        self.assertNotIn("next-devtools-mcp", profile_options)

    def test_axe_and_lighthouse_can_run_without_browser_mcp(self):
        for capability in ("axe-core-playwright", "lighthouse-ci"):
            with self.subTest(capability=capability):
                self.assertEqual(self.caps[capability]["type"], "tool")
                self.assertEqual(self.caps[capability]["depends_on"], [])
        asvs = self.caps["owasp-asvs"]
        self.assertEqual((asvs["type"], asvs["setup"]["scope"]), ("rule", "none"))

    def test_playwright_mcp_requires_explicit_selection(self):
        for profile_id in ("angular-frontend", "angular-supabase-cloudflare", "generic-web"):
            with self.subTest(profile=profile_id):
                profile = self.profiles[profile_id]
                selected, _ = hub.select(profile, self.caps, "codex", ["prueba-navegacion"])
                self.assertNotIn("playwright-mcp", selected)
                with self.assertRaises(hub.Invalid):
                    hub.select(profile, self.caps, "codex", include=["playwright-mcp"])
                selected, _ = hub.select(profile, self.caps, "codex", ["prueba-navegacion"],
                                         ["playwright-mcp"])
                self.assertIn("playwright-mcp", selected)

    def test_invalid_selections(self):
        p = self.profiles["angular-frontend"]
        for conditions, ids in [([], ["supabase-mcp"]), ([], ["angular-cli-mcp"]),
                                (["inventada"], []), ([], ["context7"])]:
            with self.subTest(ids=ids), self.assertRaises(hub.Invalid):
                hub.select(p, self.caps, "codex", conditions, ids)

    def test_transitive_optional_dependencies_and_order(self):
        caps = copy.deepcopy(self.caps)
        p = copy.deepcopy(self.profiles["business-discovery"])
        caps["domain-discovery"]["depends_on"] = ["project-bootstrap"]
        next(row for row in p["choices"] if row["id"] == "domain-discovery")["level"] = "optional"
        chosen, _ = hub.select(p, caps, "antigravity")
        self.assertEqual(list(chosen), ["project-bootstrap", "domain-discovery", "descubrimiento"])

    def test_conflict_from_dependency(self):
        caps = copy.deepcopy(self.caps)
        caps["domain-discovery"]["conflicts_with"] = ["project-bootstrap"]
        with self.assertRaisesRegex(hub.Invalid, "conflicto"):
            hub.select(self.profiles["business-discovery"], caps, "codex", include=["project-bootstrap"])

    def test_cycle_and_missing_edge(self):
        caps = copy.deepcopy(self.caps)
        for dep, error in [("descubrimiento", "Ciclo"), ("missing", "referencia")]:
            caps["domain-discovery"]["depends_on"] = [dep]
            with self.subTest(dep=dep), self.assertRaisesRegex(hub.Invalid, error):
                hub.graph(caps)

    def test_profile_edges(self):
        p = copy.deepcopy(self.profiles["business-discovery"])
        p["conditions"]["extra"] = "condición de prueba"
        next(row for row in p["choices"] if row["id"] == "domain-discovery")["when"] = ["extra"]
        with self.assertRaisesRegex(hub.Invalid, "dependencia incompatible"):
            hub.check_profile(p, self.caps)
        with self.assertRaisesRegex(hub.Invalid, "dependencia"):
            hub.select(p, self.caps, "codex")

    def test_profile_duplicate_unknown_stack(self):
        p = self.profiles["business-discovery"]
        for key, error in [("descubrimiento", "repetida"), ("ausente", "desconocida"),
                           ("angular-skills", "stack")]:
            changed = copy.deepcopy(p)
            changed["choices"].append(dict(changed["choices"][0], id=key))
            with self.subTest(key=key), self.assertRaisesRegex(hub.Invalid, error):
                hub.choices_for(changed, self.caps)

    def test_incompatible_agent(self):
        caps = copy.deepcopy(self.caps)
        caps["domain-discovery"]["agents"] = ["codex"]
        with self.assertRaisesRegex(hub.Invalid, "agente incompatible"):
            hub.select(self.profiles["business-discovery"], caps, "antigravity")

    def test_data_only(self):
        for suffix, content in [(".json", '{"id":1,"id":2}'), (".yaml", "id: a\nid: b"),
                                (".yaml", "x: &x []\ny: *x"), (".yaml", "x: !unknown value")]:
            with self.subTest(content=content), self.assertRaises(hub.Invalid):
                hub.parse(Path("example" + suffix), content)

    def test_required_and_extra_fields(self):
        cap = dict(self.caps["context7"])
        for key in ("review", "docs", "repository"):
            bad = cap.copy()
            del bad[key]
            with self.subTest(key=key), self.assertRaises(hub.Invalid):
                hub.check(hub.contract("capability"), bad, "context7")
        with self.assertRaises(hub.Invalid):
            hub.check(hub.contract("capability"), dict(cap, typo=True), "context7")

    def test_candidate_schema_is_local_and_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            directory = root / "schemas"
            directory.mkdir()
            path = directory / "skill.schema.json"
            for fields, expected in [({"type": "inventado"}, "inventado"),
                                     ({"$ref": "https://example.invalid/schema"}, "externa")]:
                path.write_text(json.dumps({"$schema": "https://json-schema.org/draft/2020-12/schema",
                                            **fields}), encoding="utf-8")
                with self.subTest(fields=fields), self.assertRaisesRegex(hub.Invalid, expected):
                    hub.contract("skill", root)

    def test_readonly_connection_examples(self):
        from urllib.parse import parse_qs, urlsplit

        with (hub.ROOT / "mcp/supabase.codex.example.toml").open("rb") as stream:
            url = tomllib.load(stream)["mcp_servers"]["supabase_dev_readonly"]["url"]
        self.assertEqual(urlsplit(url).hostname, "mcp.supabase.com")
        self.assertEqual(parse_qs(urlsplit(url).query), {"project_ref": ["PROJECT_REF"],
                                                        "read_only": ["true"], "features": ["database"]})
        with (hub.ROOT / "mcp/angular.codex.example.toml").open("rb") as stream:
            server = tomllib.load(stream)["mcp_servers"]["angular_workspace"]
        self.assertTrue({"--read-only", "--local-only"}.issubset(server["args"]))

    def test_rpc_with_existing_hosting(self):
        chosen, _ = hub.select(self.profiles["angular-supabase-cloudflare"], self.caps, "codex",
                               ["cambio-existente", "cambio-sql"])
        self.assertEqual(set(chosen), {"project-bootstrap", "angular-skills", "change-impact-analysis",
                                       "supabase-skills", "cambio-controlado"})

    def test_date_validation(self):
        cap = copy.deepcopy(self.caps["context7"])
        cap["review"]["date"] = "2026-02-30"
        with self.assertRaises(ValueError):
            hub.validate(hub.ROOT, {**self.caps, "context7": cap}, self.profiles)

    def test_yaml_json_equivalence_and_duplicate_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            folder = root / "catalog"
            folder.mkdir()
            path = folder / "context7.json"
            path.write_text(json.dumps(self.caps["context7"]), encoding="utf-8")
            self.assertEqual(hub.records(root, "catalog", "capability")["context7"], self.caps["context7"])
            shutil.copy(hub.ROOT / "catalog/context7.yaml", folder)
            with self.assertRaisesRegex(hub.Invalid, "duplicado"):
                hub.records(root, "catalog", "capability")

    def test_skill_metadata_and_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            folder = root / "skills/prueba"
            folder.mkdir(parents=True)
            entry = folder / "SKILL.md"
            entry.write_text("---\nname: prueba\n---\nCuerpo", encoding="utf-8")
            with self.assertRaisesRegex(hub.Invalid, "description"):
                hub.check_skills(root, self.caps)
            entry.write_text("---\nname: otro\ndescription: Ejemplo\n---\nCuerpo", encoding="utf-8")
            with self.assertRaisesRegex(hub.Invalid, "nombre"):
                hub.check_skills(root, self.caps)

    def test_local_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            for value in ("ausente.md", "../fuera.md"):
                (root / "README.md").write_text(f"[archivo]({value})", encoding="utf-8")
                with self.subTest(value=value), self.assertRaises(hub.Invalid):
                    hub.check_links(root)
        caps = copy.deepcopy(self.caps)
        caps["domain-discovery"]["entry"] = "skills/no-existe/SKILL.md"
        with self.assertRaisesRegex(hub.Invalid, "falta"):
            hub.validate(hub.ROOT, caps, self.profiles)

    def test_cli_from_other_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            for args, code, token in [
                (["list", "--tech", "angular", "--type", "mcp"], 0, "angular-cli-mcp"),
                (["profiles"], 0, "python-ai"),
                (["show", "codex-skill-evals"], 0, "cli-help-checked"),
                (["recommend", "generic-web", "--agent", "antigravity", "--context", "trabajo-frontend"],
                 0, "  + modern-web-guidance"),
                (["recommend", "angular-supabase-cloudflare", "--context", "cambio-sql",
                  "--context", "cambio-existente"], 0, "Condiciones activas: cambio-existente, cambio-sql"),
                (["recommend", "ausente"], 1, "desconocido"),
            ]:
                with self.subTest(args=args):
                    run = subprocess.run([sys.executable, "-X", "utf8", str(hub.ROOT / "scripts/hub.py"), *args],
                                         cwd=tmp, capture_output=True, encoding="utf-8")
                    self.assertEqual(run.returncode, code, run.stderr)
                    self.assertIn(token, run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
