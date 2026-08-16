#!/usr/bin/env python3
"""Verify that the dean account can read and execute non-secret audit inputs."""

from __future__ import annotations

import grp
import json
import os
from pathlib import Path
import pwd
import subprocess

WORKSPACE = Path(__file__).resolve().parents[1]
PINNED_PYTHON = Path(
    "/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python"
)


def account_groups(user: pwd.struct_passwd) -> set[int]:
    groups = {user.pw_gid}
    for entry in grp.getgrall():
        if user.pw_name in entry.gr_mem:
            groups.add(entry.gr_gid)
    return groups


def permitted(path: Path, uid: int, gids: set[int], mask: int) -> bool:
    stat = path.stat()
    if stat.st_uid == uid:
        bits = (stat.st_mode >> 6) & 0o7
    elif stat.st_gid in gids:
        bits = (stat.st_mode >> 3) & 0o7
    else:
        bits = stat.st_mode & 0o7
    return bits & mask == mask


def require_path_access(
    path: Path,
    *,
    uid: int,
    gids: set[int],
    read: bool,
    execute: bool,
    failures: list[str],
) -> None:
    resolved = path.resolve()
    for parent in [resolved, *resolved.parents]:
        if parent == resolved and not parent.is_dir():
            continue
        if not permitted(parent, uid, gids, 0o1):
            failures.append(f"missing traverse permission: {parent}")
    if read and not permitted(resolved, uid, gids, 0o4):
        failures.append(f"missing read permission: {resolved}")
    if execute and not permitted(resolved, uid, gids, 0o1):
        failures.append(f"missing execute permission: {resolved}")


def main() -> int:
    user = pwd.getpwnam("dean")
    gids = account_groups(user)
    failures: list[str] = []
    checked_files = 0

    readable_roots = (
        "src",
        "tests",
        "configs",
        "schemas",
        "manifests",
        "reports",
        "logs",
        "smokes_timeout2400",
    )
    for relative in readable_roots:
        root = WORKSPACE / relative
        if not root.exists():
            continue
        require_path_access(
            root,
            uid=user.pw_uid,
            gids=gids,
            read=True,
            execute=True,
            failures=failures,
        )
        for path in root.rglob("*"):
            if "__pycache__" in path.parts or path.is_symlink():
                continue
            require_path_access(
                path,
                uid=user.pw_uid,
                gids=gids,
                read=True,
                execute=path.is_dir(),
                failures=failures,
            )
            if path.is_file():
                checked_files += 1

    for script in (WORKSPACE / "scripts").glob("*"):
        if not script.is_file():
            continue
        require_path_access(
            script,
            uid=user.pw_uid,
            gids=gids,
            read=True,
            execute=script.suffix in {".py", ".sh"},
            failures=failures,
        )
        checked_files += 1

    require_path_access(
        PINNED_PYTHON,
        uid=user.pw_uid,
        gids=gids,
        read=True,
        execute=True,
        failures=failures,
    )
    module_paths = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-c",
            "import numpy, pytest; print(numpy.__file__); print(pytest.__file__)",
        ],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    for text in module_paths:
        require_path_access(
            Path(text),
            uid=user.pw_uid,
            gids=gids,
            read=True,
            execute=False,
            failures=failures,
        )

    payload = {
        "audit_account": user.pw_name,
        "audit_uid": user.pw_uid,
        "audit_gids": sorted(gids),
        "checked_nonsecret_files": checked_files,
        "pinned_python": str(PINNED_PYTHON),
        "test_command": (
            "PYTHONDONTWRITEBYTECODE=1 "
            f"PYTHONPATH={WORKSPACE / 'src'} "
            f"{PINNED_PYTHON} -m pytest -p no:cacheprovider -q "
            f"{WORKSPACE / 'tests'}"
        ),
        "credentialless_impersonation_available": False,
        "permission_failures": sorted(set(failures)),
        "dean_nonsecret_test_access": not failures,
    }
    destination = WORKSPACE / "reports" / "DEAN_NONSECRET_ACCESS_AUDIT_20260731.json"
    destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    destination.chmod(0o644)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
