#!/usr/bin/env python3
"""Verify 100Cose development environment setup."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONSTITUTION = ROOT / ".walden" / "constitution.md"

DATA_FILES = [
    DATA / "100cose.json",
    DATA / "100 cose da fare  - Sheet1.csv",
    DATA / "100cose.txt",
]

CONSTITUTION_MARKERS = [
    "100Cose",
    "100 cose",
    "100cose.json",
    "github.com/raffica93/walden",
    "github.com/raffica93/Echi",
]


def check_data_files() -> list[str]:
    errors: list[str] = []
    for path in DATA_FILES:
        if not path.is_file():
            errors.append(f"missing data file: {path.relative_to(ROOT)}")
    return errors


def check_json_count() -> list[str]:
    json_path = DATA / "100cose.json"
    if not json_path.is_file():
        return ["cannot count items: 100cose.json missing"]

    with json_path.open(encoding="utf-8") as f:
        payload = json.load(f)

    items = payload.get("Fare")
    if not isinstance(items, list):
        return ["100cose.json: expected top-level 'Fare' array"]

    count = len(items)
    if count != 100:
        return [f"100cose.json: expected 100 items, got {count}"]

    ids = [item.get("id") for item in items if isinstance(item, dict)]
    if sorted(ids) != list(range(1, 101)):
        return ["100cose.json: ids must be 1..100"]

    return []


def check_constitution() -> list[str]:
    if not CONSTITUTION.is_file():
        return ["missing .walden/constitution.md"]

    text = CONSTITUTION.read_text(encoding="utf-8")
    if "[What this project does" in text:
        return ["constitution still contains template placeholders"]

    missing = [m for m in CONSTITUTION_MARKERS if m not in text]
    if missing:
        return [f"constitution missing markers: {', '.join(missing)}"]

    return []


def main() -> int:
    errors: list[str] = []
    errors.extend(check_data_files())
    errors.extend(check_json_count())
    errors.extend(check_constitution())

    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("OK: dev environment verified")
    print(f"  data files: {len(DATA_FILES)}")
    print("  json items: 100")
    print("  constitution: populated")
    return 0


if __name__ == "__main__":
    sys.exit(main())