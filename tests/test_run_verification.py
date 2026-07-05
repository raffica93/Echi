#!/usr/bin/env python3
"""Tests for scripts/run_verification.py."""

from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_module():
    spec = importlib.util.spec_from_file_location(
        "run_verification",
        ROOT / "scripts" / "run_verification.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["run_verification"] = module
    spec.loader.exec_module(module)
    return module


class RunVerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_extract_matching_lines_constitution(self):
        lines = self.mod.extract_matching_lines(
            ROOT / ".walden" / "constitution.md",
            self.mod.CONSTITUTION_PATTERNS,
        )
        joined = "\n".join(lines)
        self.assertIn("100Cose", joined)
        self.assertIn("100cose.json", joined)
        self.assertNotIn("[What this project does", joined)

    def test_extract_matching_lines_readme(self):
        lines = self.mod.extract_matching_lines(
            ROOT / "README.md",
            self.mod.README_PATTERNS,
        )
        joined = "\n".join(lines)
        self.assertIn("Walden", joined)
        self.assertIn("walden feature init", joined)
        self.assertIn("github.com/raffica93/walden", joined)

    def test_bootstrap_commit_includes_required_files(self):
        bootstrap_hash, _ = self.mod.find_bootstrap_commit()
        files = self.mod.run_git("show", "--name-only", "--pretty=format:", bootstrap_hash)
        for required in self.mod.BOOTSTRAP_PATHS:
            self.assertIn(required, files)

    @unittest.skipIf(shutil.which("walden") is None, "walden CLI not in PATH")
    def test_full_verification_runner(self):
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp)
            for step in (
                self.mod.capture_git_remote,
                self.mod.capture_git_log,
                self.mod.capture_constitution_check,
                self.mod.capture_walden_launch,
                self.mod.capture_readme_check,
                self.mod.capture_data_presence,
                self.mod.capture_git_status,
            ):
                step(scratch)

            errors = self.mod.validate_observations(scratch)
            self.assertEqual(errors, [])

            walden_log = (scratch / "walden-launch.log").read_text(encoding="utf-8")
            self.assertIn('"ok": true', walden_log)

            version_json = walden_log.split("=== walden version --json ===", 1)[1].split("===", 1)[0].strip()
            version = json.loads(version_json)
            self.assertTrue(version.get("ok"))


if __name__ == "__main__":
    unittest.main()