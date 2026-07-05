#!/usr/bin/env python3
"""Validate a Walden feature spec directory (CI entry point)."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS_ROOT = ROOT / ".walden" / "specs"
REQUIRED_FILES = ("requirements.md", "design.md", "tasks.md")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
REQUIRED_KEYS = ("status", "last_modified")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path.name}: missing YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def structural_validate(feature: str) -> list[str]:
    spec_dir = SPECS_ROOT / feature
    if not spec_dir.is_dir():
        return [f"feature directory not found: .walden/specs/{feature}"]

    errors: list[str] = []
    for filename in REQUIRED_FILES:
        path = spec_dir / filename
        if not path.is_file():
            errors.append(f"missing {filename}")
            continue
        try:
            frontmatter = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for key in REQUIRED_KEYS:
            if key not in frontmatter or not frontmatter[key]:
                errors.append(f"{filename}: frontmatter missing '{key}'")

    return errors


def walden_validate(feature: str) -> tuple[bool, str]:
    if shutil.which("walden") is None:
        return False, "walden CLI not found in PATH"

    proc = subprocess.run(
        ["walden", "validate", feature, "--json"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    output = proc.stdout.strip() or proc.stderr.strip()
    if proc.returncode != 0:
        return False, output or f"walden validate exited {proc.returncode}"

    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return False, "walden validate returned invalid JSON"

    if not envelope.get("ok"):
        return False, output

    result = envelope.get("result") or {}
    if result.get("exit_code", 0) != 0:
        return False, result.get("summary") or output

    return True, result.get("summary") or "valid"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_walden_spec.py <feature-name>", file=sys.stderr)
        return 2

    feature = sys.argv[1]
    errors = structural_validate(feature)
    if errors:
        print(f"INVALID: .walden/specs/{feature}")
        for err in errors:
            print(f"  - {err}")
        return 1

    ok, message = walden_validate(feature)
    if ok:
        print(f"VALID: .walden/specs/{feature} ({message})")
        return 0

    print(f"VALID (structural only): .walden/specs/{feature}")
    print(f"  note: {message}")
    return 0


if __name__ == "__main__":
    sys.exit(main())