#!/usr/bin/env python3
"""Verify walden CLI health without breaking project bootstrap files."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_walden_version() -> tuple[dict | None, list[str]]:
    proc = subprocess.run(
        ["walden", "version", "--json"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    if proc.returncode != 0:
        return None, [f"walden version failed (exit {proc.returncode}): {proc.stderr.strip()}"]

    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None, ["walden version returned invalid JSON"]

    if not envelope.get("ok"):
        return envelope, ["walden version returned ok:false"]

    return envelope, []


def run_safe_repo_init() -> list[str]:
    script = ROOT / "scripts" / "walden_repo_init_safe.py"
    spec = importlib.util.spec_from_file_location("walden_repo_init_safe", script)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.main() != 0:
        return ["walden repo init safe check failed"]
    return []


def main() -> int:
    errors: list[str] = []

    _, version_errors = run_walden_version()
    errors.extend(version_errors)
    errors.extend(run_safe_repo_init())

    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("OK: walden CLI checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())