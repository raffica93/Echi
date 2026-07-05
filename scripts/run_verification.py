#!/usr/bin/env python3
"""Run the goal verification plan and write evidence logs."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCRATCH = Path(
    r"C:\Users\raffa\AppData\Local\Temp\grok-goal-49701ab177b0\implementer"
)

CONSTITUTION_PATTERNS = (
    re.compile(r"100Cose"),
    re.compile(r"100 cose"),
    re.compile(r"100cose\.json"),
    re.compile(r"github\.com/raffica93/walden"),
)
README_PATTERNS = (
    re.compile(r"Walden"),
    re.compile(r"walden feature init"),
    re.compile(r"github\.com/raffica93/walden"),
)
BOOTSTRAP_PATHS = ("data/100cose.json", ".walden/constitution.md")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def extract_matching_lines(path: Path, patterns: tuple[re.Pattern[str], ...]) -> list[str]:
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if any(pattern.search(line) for pattern in patterns):
            lines.append(line)
    return lines


def capture_git_remote(scratch: Path) -> None:
    (scratch / "git-remote.log").write_text(run_git("remote", "-v") + "\n", encoding="utf-8")


def find_bootstrap_commit() -> tuple[str, str]:
    for line in run_git("log", "--oneline", "--reverse").splitlines():
        commit_hash = line.split()[0]
        files = run_git("show", "--name-only", "--pretty=format:", commit_hash)
        if all(required in files for required in BOOTSTRAP_PATHS):
            return commit_hash, line
    raise RuntimeError("no bootstrap commit contains required data and constitution files")


def capture_git_log(scratch: Path) -> None:
    latest = run_git("log", "--oneline", "-1")
    bootstrap_hash, bootstrap_line = find_bootstrap_commit()

    log_body = "\n".join(
        [
            f"latest: {latest}",
            f"bootstrap: {bootstrap_line}",
            f"bootstrap_paths: {', '.join(BOOTSTRAP_PATHS)}",
        ]
    )
    (scratch / "git-log.log").write_text(log_body + "\n", encoding="utf-8")

    files = run_git("show", "--name-only", "--pretty=format:", bootstrap_hash)
    (scratch / "git-log-files.log").write_text(files + "\n", encoding="utf-8")


def capture_constitution_check(scratch: Path) -> None:
    lines = extract_matching_lines(ROOT / ".walden" / "constitution.md", CONSTITUTION_PATTERNS)
    (scratch / "constitution-check.log").write_text("\n".join(lines) + "\n", encoding="utf-8")


def capture_readme_check(scratch: Path) -> None:
    lines = extract_matching_lines(ROOT / "README.md", README_PATTERNS)
    (scratch / "readme-check.log").write_text("\n".join(lines) + "\n", encoding="utf-8")


def capture_walden_launch(scratch: Path) -> None:
    check_mod = load_module("check_walden_cli", ROOT / "scripts" / "check_walden_cli.py")
    version_envelope, init_envelopes, errors = check_mod.check_walden_cli()
    if errors:
        raise RuntimeError("; ".join(errors))

    content = check_mod.format_walden_launch_log(version_envelope, init_envelopes)
    (scratch / "walden-launch.log").write_text(content, encoding="utf-8")


def capture_data_presence(scratch: Path) -> None:
    verify_mod = load_module("verify_dev_env", ROOT / "scripts" / "verify_dev_env.py")
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_dev_env.py")],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    (scratch / "data-presence.log").write_text(proc.stdout + proc.stderr, encoding="utf-8")
    if proc.returncode != 0:
        raise RuntimeError("verify_dev_env.py failed")


def capture_git_status(scratch: Path) -> None:
    proc = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    (scratch / "git-status-post-verify.log").write_text(
        proc.stdout + proc.stderr,
        encoding="utf-8",
    )


def validate_observations(scratch: Path) -> list[str]:
    errors: list[str] = []

    remote = (scratch / "git-remote.log").read_text(encoding="utf-8")
    if "https://github.com/raffica93/100Cose" not in remote:
        errors.append("origin remote missing")

    git_log = (scratch / "git-log.log").read_text(encoding="utf-8")
    if "bootstrap:" not in git_log:
        errors.append("bootstrap commit not captured")

    git_files = (scratch / "git-log-files.log").read_text(encoding="utf-8")
    for required in BOOTSTRAP_PATHS:
        if required not in git_files:
            errors.append(f"bootstrap commit missing {required}")

    constitution = (scratch / "constitution-check.log").read_text(encoding="utf-8")
    if "[What this project does" in constitution:
        errors.append("constitution still template")
    for marker in ("100Cose", "100cose.json", "github.com/raffica93/walden"):
        if marker not in constitution:
            errors.append(f"constitution-check missing {marker}")

    walden_log = (scratch / "walden-launch.log").read_text(encoding="utf-8")
    for section in (
        "=== walden version --json ===",
        "=== walden repo init --json (run 1) ===",
        "=== walden repo init --json (run 2) ===",
    ):
        if section not in walden_log:
            errors.append(f"walden-launch.log missing {section}")

    # Parse envelopes from walden-launch.log
    version_json = walden_log.split("=== walden version --json ===", 1)[1].split("===", 1)[0].strip()
    run1_json = walden_log.split("=== walden repo init --json (run 1) ===", 1)[1].split("===", 1)[0].strip()
    run2_json = walden_log.split("=== walden repo init --json (run 2) ===", 1)[1].strip()

    version = json.loads(version_json)
    run1 = json.loads(run1_json)
    run2 = json.loads(run2_json)

    if not version.get("ok"):
        errors.append("walden version ok:false")
    if not run1.get("ok") or not run2.get("ok"):
        errors.append("walden repo init ok:false")

    skipped = (run2.get("result") or {}).get("skipped_files") or []
    if ".walden/constitution.md" not in skipped:
        errors.append("repo init run 2 did not skip constitution")

    readme = (scratch / "readme-check.log").read_text(encoding="utf-8")
    for marker in ("Walden", "walden feature init", "github.com/raffica93/walden"):
        if marker not in readme:
            errors.append(f"readme-check missing {marker}")

    data_presence = (scratch / "data-presence.log").read_text(encoding="utf-8")
    if "OK: dev environment verified" not in data_presence:
        errors.append("data-presence check failed")

    git_status = (scratch / "git-status-post-verify.log").read_text(encoding="utf-8")
    if "nothing to commit, working tree clean" not in git_status:
        errors.append("git working tree not clean after verification")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Run verification plan evidence capture")
    parser.add_argument("--scratch-dir", type=Path, default=DEFAULT_SCRATCH)
    args = parser.parse_args()

    scratch = args.scratch_dir
    scratch.mkdir(parents=True, exist_ok=True)

    steps = (
        capture_git_remote,
        capture_git_log,
        capture_constitution_check,
        capture_walden_launch,
        capture_readme_check,
        capture_data_presence,
        capture_git_status,
    )

    try:
        for step in steps:
            step(scratch)
        errors = validate_observations(scratch)
    except Exception as exc:  # noqa: BLE001 - verification runner reports all failures
        print(f"FAIL: {exc}")
        return 1

    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"OK: verification evidence written to {scratch}")
    return 0


if __name__ == "__main__":
    sys.exit(main())