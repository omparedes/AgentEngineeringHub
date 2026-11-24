"""Decisiones persistentes y evidencia sintética de un entorno consumidor."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts import hub


EXAMPLE = hub.ROOT / "templates/herramientas-proyecto.yaml"


class ProjectToolsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = hub.load_project_tools(EXAMPLE)
        cls.decisions = cls.manifest["decisiones"]
        cls.capabilities = hub.records(hub.ROOT, "catalog", "capability")
        cls.profile = hub.records(hub.ROOT, "profiles", "profile")[cls.manifest["perfil"]]

    def row(self, tool, signal=None, decisions=None):
        observations = {tool: signal} if signal is not None else {}
        return hub.tool_plan(self.decisions if decisions is None else decisions, [tool], observations)[0]

    def test_github_registration_is_kept_and_verified_connection_is_reused(self):
        registered = self.row("github-mcp", "configuracion-observada")
        self.assertEqual(registered["siguiente_paso"], "proponer-verificacion")
        confirmed = self.row("github-mcp", "uso-verificado")
        self.assertEqual(confirmed["estado"], "instalada-y-operativa")
        self.assertEqual(confirmed["siguiente_paso"], "reutilizar-en-el-alcance-aprobado")
        self.assertFalse(confirmed["requiere_autorizacion_especifica"])

    def test_supabase_registration_does_not_prove_operation(self):
        row = self.row("supabase-mcp", "configuracion-observada")
        self.assertEqual(row["estado"], "configurada-sin-verificar")
        self.assertEqual(row["siguiente_paso"], "proponer-verificacion")
        self.assertTrue(row["requiere_autorizacion_especifica"])

    def test_angular_skills_becomes_relevant_with_frontend_work(self):
        for agent in hub.AGENTS:
            with self.subTest(agent=agent):
                sql, _ = hub.select(self.profile, self.capabilities, agent, ["cambio-sql"])
                frontend, _ = hub.select(self.profile, self.capabilities, agent, ["trabajo-frontend"])
                self.assertNotIn("angular-skills", sql)
                self.assertIn("angular-skills", frontend)
        row = self.row("angular-skills", "ausencia-confirmada")
        self.assertEqual(row["estado"], "no-instalada")
        self.assertEqual(row["siguiente_paso"], "esperar-seleccion")

    def test_next_devtools_is_excluded_in_angular(self):
        for agent in hub.AGENTS:
            with self.subTest(agent=agent), self.assertRaisesRegex(hub.Invalid, "fuera del perfil"):
                hub.select(self.profile, self.capabilities, agent, ["trabajo-frontend"],
                           include=["next-devtools-mcp"])
        row = self.row("next-devtools-mcp", "incompatibilidad-confirmada")
        self.assertEqual(row["siguiente_paso"], "descartar-por-incompatibilidad")

    def test_fresh_design_phase_does_not_override_deferred_figma(self):
        selected, _ = hub.select(self.profile, self.capabilities, "antigravity", ["diseno-figma"])
        self.assertIn("figma-mcp", selected)
        row = self.row("figma-mcp", "falta-configuracion-confirmada")
        self.assertEqual(row["estado"], "instalada-sin-configurar")
        self.assertEqual(row["siguiente_paso"], "mantener-pospuesta")
        self.assertFalse(row["requiere_autorizacion_especifica"])

    def test_omitted_playwright_is_not_activated_even_if_available(self):
        row = self.row("playwright-mcp", "uso-verificado")
        self.assertEqual(row["siguiente_paso"], "mantener-omitida")
        self.assertFalse(row["requiere_autorizacion_especifica"])

    def test_new_machine_preserves_intent_and_forgets_historical_verification(self):
        self.assertEqual(self.manifest["ultima_observacion"]["herramientas"]["github-mcp"], "instalada-y-operativa")
        row = self.row("github-mcp")
        self.assertEqual(row["seleccion"], "utilizar")
        self.assertEqual(row["alcance_elegido"], "proyecto")
        self.assertEqual(row["ubicacion_elegida"], "mcp-del-proyecto")
        self.assertEqual(row["estado"], "desconocido")
        self.assertEqual(row["siguiente_paso"], "obtener-evidencia-antes-de-actuar")

    def test_missing_inspection_permissions_do_not_imply_absence(self):
        row = self.row("angular-skills", "sin-evidencia")
        self.assertEqual(row["estado"], "desconocido")
        self.assertEqual(row["siguiente_paso"], "esperar-seleccion")

    def test_approved_tool_yields_only_a_proposal_and_leaves_project_intact(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            manifest = folder / "tools.json"
            decisions = {**self.decisions, "angular-skills": {
                "seleccion": "utilizar", "alcance": "proyecto", "ubicacion": "skills-del-proyecto",
            }}
            manifest.write_text(json.dumps({**self.manifest, "decisiones": decisions}), encoding="utf-8")
            snapshot = manifest.read_bytes()
            result = self.run_plan(folder, manifest, "--tool", "angular-skills",
                                   "--observed", "angular-skills=ausencia-confirmada")
            self.assertEqual(result.returncode, 0, result.stderr)
            [row] = json.loads(result.stdout)
            self.assertEqual(row["siguiente_paso"], "proponer-instalacion")
            self.assertTrue(row["requiere_autorizacion_especifica"])
            self.assertEqual(list(folder.iterdir()), [manifest])
            self.assertEqual(manifest.read_bytes(), snapshot)

    def test_manifest_rejects_private_locations_and_extra_credentials_without_echo(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            manifest = folder / "tools.json"
            invalid_decisions = [
                {"ubicacion": "C:/privado-sintetico"},
                {"token": "TEST-VALOR-SINTETICO"},
                {"autorizacion": "true"},
            ]
            for fields in invalid_decisions:
                with self.subTest(fields=fields):
                    bad = {**self.decisions["github-mcp"], **fields}
                    manifest.write_text(json.dumps({**self.manifest, "decisiones": {"github-mcp": bad}}),
                                        encoding="utf-8")
                    result = self.run_plan(folder, manifest, "--tool", "github-mcp")
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("no cumple el contrato", result.stderr)
                    self.assertNotIn(next(iter(fields.values())), result.stderr)

    def run_plan(self, folder, manifest, *args):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(hub.ROOT / "scripts/hub.py"), "tools-plan",
             "--manifest", str(manifest), *args],
            cwd=folder, capture_output=True, encoding="utf-8",
        )
