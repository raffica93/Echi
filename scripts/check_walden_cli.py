#!/usr/bin/env python3
"""Verify walden CLI health without breaking project bootstrap files."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_safe_module():
    script = ROOT / "scripts" / "walden_repo_init_safe.py"
    spec = importlib.util.spec_from_file_location("walden_repo_init_safe", script)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def run_safe_repo_init() -> tuple[list[dict | None], list[str]]:
    module = load_safe_module()
    return module.run_repo_init_twice()


def check_walden_cli() -> tuple[dict | None, list[dict | None], list[str]]:
    version_envelope, version_errors = run_walden_version()
    init_envelopes, init_errors = run_safe_repo_init()
    return version_envelope, init_envelopes, version_errors + init_errors


def format_walden_launch_log(
    version_envelope: dict | None,
    init_envelopes: list[dict | None],
) -> str:
    sections: list[str] = []

    sections.append("=== walden version --json ===")
    sections.append(json.dumps(version_envelope, indent=2) if version_envelope else "null")

    for index, envelope in enumerate(init_envelopes, start=1):
        sections.append(f"=== walden repo init --json (run {index}) ===")
        sections.append(json.dumps(envelope, indent=2) if envelope else "null")

    return "\n".join(sections) + "\n"


def main() -> int:
    version_envelope, init_envelopes, errors = check_walden_cli()

    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("OK: walden CLI checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())