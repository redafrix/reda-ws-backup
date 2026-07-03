#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import subprocess
import time
from collections import Counter
from pathlib import Path
from typing import Any


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")
    tmp.replace(path)


def jsonl_rows(path: Path) -> tuple[int, int]:
    rows = 0
    errors = 0
    if not path.exists():
        return rows, errors
    with path.open() as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            rows += 1
            if row.get("outcome") == "error" or row.get("error_message"):
                errors += 1
    return rows, errors


def check_job(job: dict[str, Any]) -> tuple[bool, list[str]]:
    messages: list[str] = []
    ok = True
    for check in job.get("checks", []):
        kind = check["type"]
        path = Path(check["path"])
        if kind == "file":
            passed = path.is_file() and path.stat().st_size >= int(check.get("min_bytes", 1))
            messages.append(f"file {path}: {passed}")
        elif kind == "jsonl":
            rows, errors = jsonl_rows(path)
            passed = rows >= int(check.get("min_rows", 1)) and (not check.get("require_no_errors", True) or errors == 0)
            messages.append(f"jsonl {path}: rows={rows} errors={errors} pass={passed}")
        elif kind == "detector":
            required = ["model.pt", "normalization.json", "thresholds.json", "metrics.json"]
            missing = [name for name in required if not (path / name).is_file()]
            passed = not missing
            messages.append(f"detector {path}: missing={missing} pass={passed}")
        else:
            passed = False
            messages.append(f"unknown check type {kind}")
        ok = ok and passed
    return ok, messages


def load_state(path: Path, jobs: list[dict[str, Any]]) -> dict[str, Any]:
    if path.exists():
        state = json.loads(path.read_text())
    else:
        state = {"created_at": now_iso(), "jobs": {}}
    for job in jobs:
        state["jobs"].setdefault(
            job["id"],
            {"status": "pending", "attempts": 0, "updated_at": now_iso(), "history": []},
        )
    return state


def run_job(job: dict[str, Any], state: dict[str, Any], state_path: Path, heartbeat_path: Path) -> bool:
    record = state["jobs"][job["id"]]
    record["status"] = "running"
    record["attempts"] += 1
    record["started_at"] = now_iso()
    record["updated_at"] = now_iso()
    write_json(state_path, state)

    log_path = Path(job["log"])
    log_path.parent.mkdir(parents=True, exist_ok=True)
    command = [str(x) for x in job["command"]]
    timeout = int(job.get("timeout_seconds", 172800))
    started = time.time()
    with log_path.open("ab") as log:
        log.write((f"\n[{now_iso()}] START attempt={record['attempts']} command={json.dumps(command)}\n").encode())
        log.flush()
        proc = subprocess.Popen(
            command,
            cwd=job.get("cwd"),
            env={**os.environ, **{str(k): str(v) for k, v in job.get("env", {}).items()}},
            stdout=log,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
        )
        record["pid"] = proc.pid
        write_json(state_path, state)
        timed_out = False
        while proc.poll() is None:
            elapsed = time.time() - started
            write_json(
                heartbeat_path,
                {
                    "updated_at": now_iso(),
                    "job_id": job["id"],
                    "pid": proc.pid,
                    "elapsed_seconds": elapsed,
                    "attempt": record["attempts"],
                },
            )
            if elapsed > timeout:
                timed_out = True
                os.killpg(proc.pid, signal.SIGTERM)
                time.sleep(10)
                if proc.poll() is None:
                    os.killpg(proc.pid, signal.SIGKILL)
                break
            time.sleep(30)
        code = proc.wait()
        log.write((f"[{now_iso()}] END code={code} timed_out={timed_out}\n").encode())

    checks_ok, check_messages = check_job(job)
    success = code == 0 and not timed_out and checks_ok
    record["status"] = "completed" if success else "failed_attempt"
    record["returncode"] = code
    record["timed_out"] = timed_out
    record["check_messages"] = check_messages
    record["elapsed_seconds"] = time.time() - started
    record["updated_at"] = now_iso()
    record["history"].append(
        {
            "attempt": record["attempts"],
            "returncode": code,
            "timed_out": timed_out,
            "checks_ok": checks_ok,
            "finished_at": now_iso(),
        }
    )
    write_json(state_path, state)
    return success


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text())
    jobs = list(manifest["jobs"])
    campaign_root = Path(manifest["campaign_root"])
    state_path = campaign_root / "state" / "scheduler_state.json"
    heartbeat_path = campaign_root / "state" / "heartbeat.json"
    state = load_state(state_path, jobs)
    min_free_gb = float(manifest.get("min_free_disk_gb", 40.0))

    while True:
        status = {job_id: rec["status"] for job_id, rec in state["jobs"].items()}
        if all(value in {"completed", "failed", "blocked"} for value in status.values()):
            break

        progress = False
        for job in jobs:
            record = state["jobs"][job["id"]]
            if record["status"] == "completed":
                continue
            deps = list(job.get("depends_on", []))
            dep_states = [state["jobs"][dep]["status"] for dep in deps]
            allow_failed_dependencies = bool(job.get("allow_failed_dependencies", False))
            if not allow_failed_dependencies and any(value in {"failed", "blocked"} for value in dep_states):
                record["status"] = "blocked"
                record["updated_at"] = now_iso()
                record["reason"] = "dependency_failed"
                write_json(state_path, state)
                progress = True
                continue
            allowed_terminal = {"completed", "failed", "blocked"} if allow_failed_dependencies else {"completed"}
            if not all(value in allowed_terminal for value in dep_states):
                continue
            if record["status"] == "running":
                pid = int(record.get("pid") or 0)
                try:
                    os.kill(pid, 0)
                    time.sleep(30)
                    progress = True
                    break
                except OSError:
                    record["status"] = "failed_attempt"
            max_attempts = int(job.get("max_attempts", 2))
            if record["attempts"] >= max_attempts and record["status"] != "pending":
                record["status"] = "failed"
                record["updated_at"] = now_iso()
                write_json(state_path, state)
                progress = True
                continue
            free_gb = shutil.disk_usage(campaign_root).free / (1024**3)
            if free_gb < min_free_gb:
                write_json(
                    heartbeat_path,
                    {"updated_at": now_iso(), "status": "waiting_for_disk", "free_gb": free_gb, "required_gb": min_free_gb},
                )
                time.sleep(300)
                progress = True
                break
            run_job(job, state, state_path, heartbeat_path)
            progress = True
            break
        if not progress:
            time.sleep(60)

    counts = Counter(record["status"] for record in state["jobs"].values())
    write_json(
        campaign_root / "state" / "campaign_complete.json",
        {"finished_at": now_iso(), "status_counts": dict(counts), "manifest": str(manifest_path)},
    )
    if counts.get("failed") or counts.get("blocked"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
