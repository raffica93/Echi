#!/usr/bin/env python3
"""Tests for scripts/run_verification.py."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
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


def expected_path_filtered_output() -> str:
    proc = subprocess.run(
        ["git", "log", "--oneline", "--", "data/100cose.json", ".walden/constitution.md", "-1"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    return proc.stdout.strip()


class RunVerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_run_and_capture_writes_cmd_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            outfile = Path(tmp) / "sample.log"
            self.mod.run_and_capture(["git", "log", "--oneline", "-1"], outfile)
            content = outfile.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("# cmd: git log --oneline -1\n"))

    def test_bootstrap_commit_includes_required_files(self):
        bootstrap_hash, _ = self.mod.find_bootstrap_commit()
        files = self.mod.run_git("show", "--name-only", "--pretty=format:", bootstrap_hash)
        for required in self.mod.BOOTSTRAP_PATHS:
            self.assertIn(required, files)

    def test_git_log_literal_path_filtered_capture(self):
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp)
            self.mod.capture_git_log(scratch)

            log_text = (scratch / "git-log.log").read_text(encoding="utf-8")
            self.assertNotIn("latest:", log_text)
            self.assertNotIn("bootstrap:", log_text)

            blocks = self.mod.parse_cmd_blocks(log_text)
            path_cmd = " ".join(self.mod.PATH_FILTERED_LOG_CMD)
            path_outputs = self.mod.blocks_for_command(blocks, path_cmd)
            self.assertEqual(len(path_outputs), 1)
            self.assertEqual(path_outputs[0], expected_path_filtered_output())

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
            blocks = self.mod.parse_cmd_blocks(walden_log)
            version = json.loads(self.mod.blocks_for_command(blocks, "walden version --json")[0])
            self.assertTrue(version.get("ok"))


if __name__ == "__main__":
    unittest.main()