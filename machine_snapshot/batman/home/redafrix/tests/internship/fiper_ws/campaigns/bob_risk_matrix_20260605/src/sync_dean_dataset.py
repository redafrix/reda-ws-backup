#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from pathlib import Path


FILES = ["episode_summaries.jsonl", "fiper_receding_samples.jsonl", "query_samples.jsonl", "transitions.jsonl"]


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=check)


def remote_count(host: str, root: str) -> int:
    command = f"find {json.dumps(root)} -mindepth 2 -maxdepth 2 -name episode_summaries.jsonl -print0 | xargs -0 -r cat | wc -l"
    result = run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", host, command])
    return int(result.stdout.strip() or 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote-host", required=True)
    parser.add_argument("--remote-root", required=True)
    parser.add_argument("--dest", required=True)
    parser.add_argument("--min-episodes", type=int, required=True)
    parser.add_argument("--poll-seconds", type=int, default=600)
    parser.add_argument("--max-wait-hours", type=float, default=72.0)
    args = parser.parse_args()

    started = time.time()
    while True:
        count = remote_count(args.remote_host, args.remote_root)
        print(f"remote episodes={count} required={args.min_episodes}", flush=True)
        if count >= args.min_episodes:
            break
        if time.time() - started > args.max_wait_hours * 3600:
            raise TimeoutError(f"dataset did not reach {args.min_episodes} episodes")
        time.sleep(args.poll_seconds)

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    command = [
        "rsync",
        "-a",
        "--partial",
        "--append-verify",
        "--info=progress2",
        "--include=worker_*/",
    ]
    for filename in FILES:
        command.append(f"--include=worker_*/{filename}")
    command.extend(["--exclude=*", f"{args.remote_host}:{args.remote_root.rstrip('/')}/", str(dest) + "/"])
    subprocess.run(command, check=True)

    local_summaries = sorted(dest.glob("worker_*/episode_summaries.jsonl"))
    local_count = sum(sum(1 for line in path.open() if line.strip()) for path in local_summaries)
    if local_count < args.min_episodes:
        raise RuntimeError(f"copied dataset has only {local_count} summaries")
    files = []
    for path in sorted(dest.glob("worker_*/*.jsonl")):
        files.append({"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)})
    manifest = {
        "remote_host": args.remote_host,
        "remote_root": args.remote_root,
        "copied_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "episode_count": local_count,
        "files": files,
    }
    (dest / "SYNC_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"episode_count": local_count, "file_count": len(files), "dest": str(dest)}, sort_keys=True))


if __name__ == "__main__":
    main()
