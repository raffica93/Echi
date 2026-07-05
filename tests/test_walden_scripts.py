#!/usr/bin/env python3
"""Tests for Walden helper scripts."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class WaldenRepoInitSafeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if shutil.which("walden") is None:
            raise unittest.SkipTest("walden CLI not in PATH")
        cls.mod = load_module(
            "walden_repo_init_safe",
            ROOT / "scripts" / "walden_repo_init_safe.py",
        )
        cls._managed_backups = {
            ROOT / ".walden" / "constitution.md": (
                ROOT / ".walden" / "constitution.md"
            ).read_text(encoding="utf-8"),
            ROOT / ".github" / "pull_request_template.md": (
                ROOT / ".github" / "pull_request_template.md"
            ).read_text(encoding="utf-8"),
        }

    @classmethod
    def tearDownClass(cls):
        for path, content in cls._managed_backups.items():
            path.write_text(content, encoding="utf-8", newline="\n")

    def test_preserves_populated_constitution(self):
        constitution = ROOT / ".walden" / "constitution.md"
        before = constitution.read_text(encoding="utf-8")
        self.assertNotIn(self.mod.TEMPLATE_MARKER, before)
        self.assertNotIn(self.mod.PR_TEMPLATE_MARKER, (ROOT / ".github" / "pull_request_template.md").read_text(encoding="utf-8"))

        self.assertEqual(self.mod.main(), 0)

        after = constitution.read_text(encoding="utf-8")
        self.assertEqual(before, after)

    def test_second_init_is_idempotent(self):
        first, _, code = self.mod.run_walden_json("repo", "init", "--json")
        self.assertEqual(code, 0)
        self.assertTrue(first and first.get("ok"))

        second, _, code = self.mod.run_walden_json("repo", "init", "--json")
        self.assertEqual(code, 0)
        self.assertEqual(self.mod.check_repo_init_idempotent(second), [])


class CheckWaldenCliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if shutil.which("walden") is None:
            raise unittest.SkipTest("walden CLI not in PATH")
        cls.mod = load_module("check_walden_cli", ROOT / "scripts" / "check_walden_cli.py")

    def test_version_ok(self):
        envelope, errors = self.mod.run_walden_version()
        self.assertEqual(errors, [])
        self.assertTrue(envelope and envelope.get("ok"))

    def test_main_returns_zero(self):
        self.assertEqual(self.mod.main(), 0)


class ValidateWaldenSpecTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module(
            "validate_walden_spec",
            ROOT / "scripts" / "validate_walden_spec.py",
        )

    def test_missing_feature_fails(self):
        errors = self.mod.structural_validate("nonexistent-feature-xyz")
        self.assertTrue(errors)

    def test_script_exits_nonzero_for_missing_feature(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_walden_spec.py"), "missing-feature"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("INVALID", proc.stdout)


if __name__ == "__main__":
    unittest.main()