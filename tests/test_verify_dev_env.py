#!/usr/bin/env python3
"""Unit tests for scripts/verify_dev_env.py shipped checks."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "verify_dev_env.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verify_dev_env", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["verify_dev_env"] = module
    spec.loader.exec_module(module)
    return module


class VerifyDevEnvTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_data_files_present(self):
        self.assertEqual(self.mod.check_data_files(), [])

    def test_json_has_100_items(self):
        self.assertEqual(self.mod.check_json_count(), [])

    def test_constitution_populated(self):
        self.assertEqual(self.mod.check_constitution(), [])

    def test_main_returns_zero(self):
        self.assertEqual(self.mod.main(), 0)


if __name__ == "__main__":
    unittest.main()