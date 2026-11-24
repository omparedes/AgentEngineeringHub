"""Ensayos en un repositorio y un directorio de usuario desechables."""

from contextlib import redirect_stderr, redirect_stdout
import hashlib
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts import install_hub_guide as setup


class HubGuideSetupTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        directory = Path(temp.name).resolve()
        self.checkout = directory / "hub"
        self.checkout.mkdir()
        self.home = directory / "usuario"
        self.home.mkdir()
        self.git("init", "-q")
        self.skill = self.checkout / setup.SKILL
        self.skill.parent.mkdir(parents=True)
        self.skill.write_bytes((setup.ROOT / setup.SKILL).read_bytes())
        self.git("add", setup.SKILL)
        self.git("-c", "user.name=Pruebas", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "-c", "core.hooksPath=.",
                 "commit", "-qm", "Skill sintética")
        self.git("-c", "user.name=Pruebas", "-c", "user.email=test@example.invalid",
                 "tag", "--no-sign", "-a", "v0.3.0", "-m", "Versión de prueba")

    def git(self, *arguments):
        return subprocess.check_output(["git", "-C", str(self.checkout), *arguments],
                                       stderr=subprocess.PIPE, text=True).strip()

    def execute(self, client, *arguments, apply=False):
        argv = ["--client", client, *arguments]
        if apply:
            argv.extend(["--apply", self.git("rev-parse", "HEAD")])
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = setup.main(argv, root=self.checkout, user_home=self.home)
        return code, out.getvalue(), err.getvalue()

    def test_preview_never_writes_for_either_client(self):
        for client in setup.DESTINATIONS:
            with self.subTest(client=client):
                code, out, _ = self.execute(client)
                self.assertEqual(code, 0)
                self.assertIn(str(self.home / setup.DESTINATIONS[client]), out)
                self.assertIn("v0.3.0", out)
                self.assertEqual(list(self.home.iterdir()), [])

    def test_apply_copies_only_the_committed_skill_and_receipt(self):
        saved = setup.git(self.checkout, "show", f"HEAD:{setup.SKILL}")
        self.skill.write_text("cambio sin confirmar", encoding="utf-8")
        for client, location in {
            "codex": ".agents/skills/hub-guide",
            "antigravity": ".gemini/config/skills/hub-guide",
        }.items():
            with self.subTest(client=client):
                code, _, err = self.execute(client, apply=True)
                self.assertEqual(code, 0, err)
                destination = self.home / location
                self.assertEqual({item.name for item in destination.iterdir()}, {"SKILL.md", "hub-source.json"})
                self.assertEqual((destination / "SKILL.md").read_bytes(), saved)
                receipt = json.loads((destination / "hub-source.json").read_text(encoding="utf-8"))
                self.assertEqual(receipt, {
                    "checkout": str(self.checkout),
                    "commit": self.git("rev-parse", "HEAD"),
                    "version": "v0.3.0",
                    "sha256": hashlib.sha256(saved).hexdigest(),
                })

    def test_existing_skill_is_reported_and_preserved(self):
        destination = self.home / ".agents/skills/hub-guide"
        destination.mkdir(parents=True)
        skill = destination / "SKILL.md"
        skill.write_text("contenido del usuario", encoding="utf-8")
        self.assertIn("Ya existe", self.execute("codex")[1])
        self.assertEqual(self.execute("codex", apply=True)[0], 1)
        self.assertEqual(skill.read_text(encoding="utf-8"), "contenido del usuario")
        self.assertEqual(list(destination.iterdir()), [skill])

    def test_release_candidate_requires_explicit_opt_in(self):
        self.git("tag", "-d", "v0.3.0")
        self.git("tag", "v0.3.0-rc.1", "--no-sign")
        code, _, err = self.execute("codex", apply=True)
        self.assertEqual(code, 1)
        self.assertIn("etiqueta estable", err)
        self.assertEqual(list(self.home.iterdir()), [])
        code, out, _ = self.execute("codex", "--allow-unreleased")
        self.assertEqual(code, 0)
        self.assertIn("revisión sin etiqueta estable", out)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_stable_source_without_the_skill_explains_next_step(self):
        self.git("rm", "-q", setup.SKILL)
        self.git("-c", "user.name=Pruebas", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "-c", "core.hooksPath=.",
                 "commit", "-qm", "Referencia sin la skill")
        self.git("tag", "v0.3.1", "--no-sign")
        code, _, err = self.execute("antigravity", apply=True)
        self.assertEqual(code, 1)
        self.assertIn("todavía no distribuye", err)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_missing_git_leaves_home_untouched(self):
        commit = self.git("rev-parse", "HEAD")
        with patch.object(setup.subprocess, "run", side_effect=FileNotFoundError):
            code, _, err = self.execute("codex", "--apply", commit)
        self.assertEqual(code, 1)
        self.assertIn("Git no está disponible", err)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_commit_must_match_preview(self):
        code, _, err = self.execute("codex", "--apply", "0" * 40)
        self.assertEqual(code, 1)
        self.assertIn("difiere de HEAD", err)
        self.assertEqual(list(self.home.iterdir()), [])
