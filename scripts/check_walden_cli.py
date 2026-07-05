#!/usr/bin/env python3
"""Walden CLI checks: validate envelopes and capture verbatim evidence."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CaptureFn = Callable[..., str]


def load_safe_module():
    script = ROOT / "scripts" / "walden_repo_init_safe.py"
    spec = importlib.util.spec_from_file_location("walden_repo_init_safe", script)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_cmd_blocks(log_text: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    for chunk in log_text.split("# cmd: "):
        if not chunk.strip():
            continue
        cmd_line, _, body = chunk.partition("\n")
        blocks.append((cmd_line.strip(), body.strip()))
    return blocks


def blocks_for_command(blocks: list[tuple[str, str]], command: str) -> list[str]:
    return [body for cmd, body in blocks if cmd == command]


def validate_envelopes(version: dict | None, init_envelopes: list[dict | None]) -> list[str]:
    errors: list[str] = []

    if version is None or not version.get("ok"):
        errors.append("walden version returned ok:false")

    if len(init_envelopes) < 2:
        errors.append("walden repo init: expected two envelopes")
        return errors

    if not init_envelopes[0] or not init_envelopes[0].get("ok"):
        errors.append("walden repo init run 1 returned ok:false")
    if not init_envelopes[1] or not init_envelopes[1].get("ok"):
        errors.append("walden repo init run 2 returned ok:false")
    else:
        skipped = (init_envelopes[1].get("result") or {}).get("skipped_files") or []
        if ".walden/constitution.md" not in skipped:
            errors.append("repo init run 2 did not skip constitution")

    return errors


def envelopes_from_launch_log(log_path: Path) -> tuple[dict | None, list[dict | None], list[str]]:
    if not log_path.is_file():
        return None, [], ["walden-launch.log missing"]

    blocks = parse_cmd_blocks(log_path.read_text(encoding="utf-8"))
    version_outputs = blocks_for_command(blocks, "walden version --json")
    init_outputs = blocks_for_command(blocks, "walden repo init --json")

    errors: list[str] = []
    version: dict | None = None
    inits: list[dict | None] = []

    try:
        if not version_outputs:
            errors.append("walden-launch.log missing version cmd")
        else:
            version = json.loads(version_outputs[0])

        if len(init_outputs) < 2:
            errors.append("walden-launch.log missing two repo init cmd blocks")
        else:
            inits = [json.loads(init_outputs[0]), json.loads(init_outputs[1])]
    except json.JSONDecodeError:
        errors.append("walden-launch.log JSON parse failed")
        return None, [], errors

    errors.extend(validate_envelopes(version, inits))
    return version, inits, errors


def capture_walden_launch(scratch: Path, capture_fn: CaptureFn) -> list[str]:
    """Capture walden version + repo init x2 with managed-file restore."""
    outfile = scratch / "walden-launch.log"
    if outfile.exists():
        outfile.unlink()

    safe = load_safe_module()
    backups = safe.backup_managed_files()
    errors: list[str] = []

    try:
        capture_fn(["walden", "version", "--json"], outfile, append=True)
        capture_fn(["walden", "repo", "init", "--json"], outfile, append=True)
        capture_fn(["walden", "repo", "init", "--json"], outfile, append=True)
    finally:
        errors.extend(safe.restore_managed_files(backups))

    _, _, check_errors = envelopes_from_launch_log(outfile)
    errors.extend(check_errors)
    return errors


def check_walden_cli(scratch: Path | None = None, capture_fn: CaptureFn | None = None) -> list[str]:
    if scratch is not None and capture_fn is not None:
        return capture_walden_launch(scratch, capture_fn)

    proc_version = subprocess.run(
        ["walden", "version", "--json"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    if proc_version.returncode != 0:
        return [f"walden version failed (exit {proc_version.returncode})"]

    try:
        version = json.loads(proc_version.stdout)
    except json.JSONDecodeError:
        return ["walden version returned invalid JSON"]

    safe = load_safe_module()
    init_envelopes, init_errors = safe.run_repo_init_twice()
    return validate_envelopes(version, init_envelopes) + init_errors


def main() -> int:
    errors = check_walden_cli()
    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("OK: walden CLI checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())