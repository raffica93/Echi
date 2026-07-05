#!/usr/bin/env python3
"""Run the goal verification plan and write verbatim command evidence logs."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCRATCH = Path(
    r"C:\Users\raffa\AppData\Local\Temp\grok-goal-49701ab177b0\implementer"
)

BOOTSTRAP_PATHS = ("data/100cose.json", ".walden/constitution.md")
PATH_FILTERED_LOG_CMD = [
    "git",
    "log",
    "--oneline",
    "--",
    "data/100cose.json",
    ".walden/constitution.md",
    "-1",
]


def load_safe_module():
    script = ROOT / "scripts" / "walden_repo_init_safe.py"
    spec = importlib.util.spec_from_file_location("walden_repo_init_safe", script)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def format_cmd(argv: list[str]) -> str:
    return " ".join(argv)


def run_and_capture(
    argv: list[str],
    outfile: Path | None = None,
    *,
    append: bool = False,
    cwd: Path = ROOT,
) -> str:
    proc = subprocess.run(argv, capture_output=True, text=True, cwd=cwd, check=False)
    stdout = proc.stdout
    if proc.stderr:
        stdout = f"{stdout}{proc.stderr}" if stdout else proc.stderr

    block = f"# cmd: {format_cmd(argv)}\n{stdout}"
    if stdout and not stdout.endswith("\n"):
        block += "\n"

    if outfile is not None:
        if append and outfile.exists():
            existing = outfile.read_text(encoding="utf-8")
            if existing and not existing.endswith("\n"):
                existing += "\n"
            outfile.write_text(existing + block, encoding="utf-8")
        else:
            outfile.write_text(block, encoding="utf-8")

    if proc.returncode != 0:
        raise RuntimeError(
            f"command failed (exit {proc.returncode}): {format_cmd(argv)}\n{proc.stderr.strip()}"
        )

    return stdout.strip()


def run_git(*args: str) -> str:
    return run_and_capture(["git", *args])


def find_bootstrap_commit() -> tuple[str, str]:
    for line in run_git("log", "--oneline", "--reverse").splitlines():
        commit_hash = line.split()[0]
        files = run_git("show", "--name-only", "--pretty=format:", commit_hash)
        if all(required in files for required in BOOTSTRAP_PATHS):
            return commit_hash, line
    raise RuntimeError("no bootstrap commit contains required data and constitution files")


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


def capture_git_remote(scratch: Path) -> None:
    run_and_capture(["git", "remote", "-v"], scratch / "git-remote.log")


def capture_git_log(scratch: Path) -> None:
    outfile = scratch / "git-log.log"
    if outfile.exists():
        outfile.unlink()

    run_and_capture(["git", "log", "--oneline", "-1"], outfile, append=True)
    run_and_capture(PATH_FILTERED_LOG_CMD, outfile, append=True)

    bootstrap_hash, _ = find_bootstrap_commit()
    run_and_capture(["git", "show", "-s", "--oneline", bootstrap_hash], outfile, append=True)

    run_and_capture(
        ["git", "show", "--name-only", "--pretty=format:", bootstrap_hash],
        scratch / "git-log-files.log",
    )


def capture_constitution_check(scratch: Path) -> None:
    run_and_capture(
        [
            "git",
            "grep",
            "-n",
            "-E",
            "100Cose|100 cose|100cose.json|github.com/raffica93/walden",
            "--",
            ".walden/constitution.md",
        ],
        scratch / "constitution-check.log",
    )


def capture_readme_check(scratch: Path) -> None:
    run_and_capture(
        [
            "git",
            "grep",
            "-n",
            "-E",
            r"Walden|walden feature init|github.com/raffica93/walden",
            "--",
            "README.md",
        ],
        scratch / "readme-check.log",
    )


def capture_walden_launch(scratch: Path) -> None:
    safe = load_safe_module()
    outfile = scratch / "walden-launch.log"
    if outfile.exists():
        outfile.unlink()

    run_and_capture(["walden", "version", "--json"], outfile, append=True)

    backups = safe.backup_managed_files()
    try:
        run_and_capture(["walden", "repo", "init", "--json"], outfile, append=True)
        run_and_capture(["walden", "repo", "init", "--json"], outfile, append=True)
    finally:
        errors = safe.restore_managed_files(backups)
        if errors:
            raise RuntimeError("; ".join(errors))


def capture_data_presence(scratch: Path) -> None:
    run_and_capture(
        [sys.executable, "scripts/verify_dev_env.py"],
        scratch / "data-presence.log",
    )


def capture_git_status(scratch: Path) -> None:
    run_and_capture(["git", "status"], scratch / "git-status-post-verify.log")


def validate_observations(scratch: Path) -> list[str]:
    errors: list[str] = []

    remote = (scratch / "git-remote.log").read_text(encoding="utf-8")
    if "https://github.com/raffica93/100Cose" not in remote:
        errors.append("origin remote missing")

    git_log = (scratch / "git-log.log").read_text(encoding="utf-8")
    git_blocks = parse_cmd_blocks(git_log)

    latest_cmd = "git log --oneline -1"
    if not blocks_for_command(git_blocks, latest_cmd):
        errors.append("git-log.log missing latest commit output")

    path_cmd = format_cmd(PATH_FILTERED_LOG_CMD)
    if not blocks_for_command(git_blocks, path_cmd):
        errors.append("git-log.log missing path-filtered log output")

    bootstrap_hash, bootstrap_line = find_bootstrap_commit()
    show_cmd = f"git show -s --oneline {bootstrap_hash}"
    show_blocks = blocks_for_command(git_blocks, show_cmd)
    if not show_blocks:
        errors.append("git-log.log missing bootstrap show output")
    elif bootstrap_hash not in show_blocks[0]:
        errors.append("git-log.log bootstrap show missing hash")

    git_files = (scratch / "git-log-files.log").read_text(encoding="utf-8")
    show_files_cmd = f"git show --name-only --pretty=format: {bootstrap_hash}"
    if not blocks_for_command(parse_cmd_blocks(git_files), show_files_cmd):
        errors.append("git-log-files.log missing expected cmd header")

    for required in BOOTSTRAP_PATHS:
        if required not in git_files:
            errors.append(f"bootstrap commit missing {required}")

    if bootstrap_hash not in bootstrap_line:
        errors.append("bootstrap hash mismatch")

    constitution = (scratch / "constitution-check.log").read_text(encoding="utf-8")
    if "[What this project does" in constitution:
        errors.append("constitution still template")
    for marker in ("100Cose", "100cose.json", "github.com/raffica93/walden"):
        if marker not in constitution:
            errors.append(f"constitution-check missing {marker}")

    walden_log = (scratch / "walden-launch.log").read_text(encoding="utf-8")
    walden_blocks = parse_cmd_blocks(walden_log)

    version_cmd = "walden version --json"
    init_cmd = "walden repo init --json"
    version_outputs = blocks_for_command(walden_blocks, version_cmd)
    init_outputs = blocks_for_command(walden_blocks, init_cmd)
    if not version_outputs:
        errors.append("walden-launch.log missing version cmd")
    if len(init_outputs) < 2:
        errors.append("walden-launch.log missing two repo init cmd blocks")

    try:
        version = json.loads(version_outputs[0])
        run1 = json.loads(init_outputs[0])
        run2 = json.loads(init_outputs[1])
    except (json.JSONDecodeError, IndexError):
        errors.append("walden-launch.log JSON parse failed")
        return errors

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