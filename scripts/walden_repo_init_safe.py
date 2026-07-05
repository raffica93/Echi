#!/usr/bin/env python3
"""Run walden repo init twice without losing a populated constitution.md."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANAGED_FILES = (
    ROOT / ".walden" / "constitution.md",
    ROOT / ".github" / "pull_request_template.md",
)
CONSTITUTION = ROOT / ".walden" / "constitution.md"
TEMPLATE_MARKER = "[What this project does"
PR_TEMPLATE_MARKER = "go test ./..."


def is_populated_constitution(text: str) -> bool:
    return TEMPLATE_MARKER not in text


def is_custom_pr_template(text: str) -> bool:
    return PR_TEMPLATE_MARKER not in text


def should_preserve(path: Path, content: str) -> bool:
    if path == CONSTITUTION:
        return is_populated_constitution(content)
    if path.name == "pull_request_template.md":
        return is_custom_pr_template(content)
    return False


def run_walden_json(*args: str) -> tuple[dict | None, str, int]:
    cmd = ["walden", *args]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    stdout = proc.stdout.strip()
    if not stdout:
        return None, proc.stderr.strip(), proc.returncode

    try:
        return json.loads(stdout), proc.stderr.strip(), proc.returncode
    except json.JSONDecodeError:
        return None, stdout or proc.stderr.strip(), proc.returncode


def backup_managed_files() -> dict[Path, bytes]:
    backups: dict[Path, bytes] = {}
    for path in MANAGED_FILES:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if should_preserve(path, content):
            backups[path] = path.read_bytes()
    return backups


def restore_managed_files(backups: dict[Path, bytes]) -> list[str]:
    errors: list[str] = []
    for path, content in backups.items():
        path.write_bytes(content)
        restored = path.read_text(encoding="utf-8")
        if path == CONSTITUTION and not is_populated_constitution(restored):
            errors.append("failed to restore populated constitution.md")
        if path.name == "pull_request_template.md" and not is_custom_pr_template(restored):
            errors.append("failed to restore customized pull_request_template.md")
    return errors


def check_repo_init_idempotent(envelope: dict | None) -> list[str]:
    if envelope is None:
        return ["repo init returned no JSON envelope"]

    if not envelope.get("ok"):
        return ["repo init returned ok:false"]

    result = envelope.get("result") or {}
    created = result.get("created_files") or result.get("changed_files")
    if created:
        return [f"repo init unexpectedly created/changed files: {created}"]

    skipped = result.get("skipped_files") or []
    expected = {
        ".walden/constitution.md",
        ".walden/lessons.md",
        ".github/pull_request_template.md",
        ".github/workflows/validate-walden.yml",
    }
    missing = expected - set(skipped)
    if missing:
        return [f"repo init did not skip expected bootstrap files: {sorted(missing)}"]

    return []


def main() -> int:
    backups = backup_managed_files()
    errors: list[str] = []
    try:
        first, first_err, first_code = run_walden_json("repo", "init", "--json")
        if first_code != 0:
            errors.append(f"repo init run 1 failed (exit {first_code}): {first_err}")
        elif first is None or not first.get("ok"):
            errors.append("repo init run 1 returned ok:false")

        second, second_err, second_code = run_walden_json("repo", "init", "--json")
        if second_code != 0:
            errors.append(f"repo init run 2 failed (exit {second_code}): {second_err}")
        else:
            errors.extend(check_repo_init_idempotent(second))
    finally:
        errors.extend(restore_managed_files(backups))

    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("OK: walden repo init is idempotent and constitution preserved")
    return 0


if __name__ == "__main__":
    sys.exit(main())