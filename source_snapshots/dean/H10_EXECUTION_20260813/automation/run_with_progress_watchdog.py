#!/usr/bin/env python3
"""Run a resumable collector and restart it if episode progress stops."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from typing import Any


VALID_COLLECTOR_FINAL_STATES = {
    "complete",
    "paused_before_episode",
    "paused_after_episode",
    "paused_after_current_episode",
}


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    temp.replace(path)


def append_jsonl_fsync(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def read_status(path: Path) -> tuple[dict[str, Any], int]:
    try:
        return json.loads(path.read_text()), path.stat().st_mtime_ns
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}, 0


def effective_collector_return_code(
    process_return_code: int, final_status: dict[str, Any]
) -> tuple[int, str | None]:
    if process_return_code != 0:
        return process_return_code, None
    final_state = final_status.get("state")
    if final_state not in VALID_COLLECTOR_FINAL_STATES:
        return 125, (
            "collector exited zero without a durable terminal status; "
            f"final_state={final_state!r}"
        )
    return 0, None


def terminate_process_group(
    process: subprocess.Popen[bytes], *, interrupt_grace_s: float, term_grace_s: float
) -> tuple[int, bool]:
    if process.poll() is not None:
        return int(process.returncode), False
    os.killpg(process.pid, signal.SIGINT)
    try:
        return int(process.wait(timeout=interrupt_grace_s)), False
    except subprocess.TimeoutExpired:
        pass
    os.killpg(process.pid, signal.SIGTERM)
    try:
        return int(process.wait(timeout=term_grace_s)), False
    except subprocess.TimeoutExpired:
        # Native CUDA/Isaac calls can remain uninterruptible to Python signal
        # handling. Episode commits are atomic, so killing the wedged process
        # cannot make a partial episode authoritative; resume quarantines any
        # staging directory before continuing.
        os.killpg(process.pid, signal.SIGKILL)
        return int(process.wait(timeout=30.0)), True


def run(args: argparse.Namespace) -> int:
    if not args.command:
        raise ValueError("a collector command is required after --")
    if args.stall_seconds <= 0 or args.poll_seconds <= 0:
        raise ValueError("watchdog durations must be positive")
    if args.max_stall_restarts < 0:
        raise ValueError("max-stall-restarts must be nonnegative")

    status_path = args.status.resolve()
    events_path = args.events.resolve()
    watchdog_status = args.watchdog_status.resolve()
    stall_restarts = 0

    while True:
        observed_status, observed_mtime = read_status(status_path)
        last_progress = time.monotonic()
        process = subprocess.Popen(args.command, start_new_session=True)
        atomic_json(
            watchdog_status,
            {
                "schema_version": "simvla_collector_progress_watchdog_v1",
                "state": "running",
                "collector_pid": process.pid,
                "stall_restarts": stall_restarts,
                "stall_seconds": args.stall_seconds,
                "status_path": str(status_path),
                "command": args.command,
                "updated_at_utc": datetime.now(timezone.utc).isoformat(),
            },
        )
        stalled = False
        while process.poll() is None:
            time.sleep(args.poll_seconds)
            current_status, current_mtime = read_status(status_path)
            if current_mtime != observed_mtime or current_status != observed_status:
                observed_status = current_status
                observed_mtime = current_mtime
                last_progress = time.monotonic()
            quiet_s = time.monotonic() - last_progress
            atomic_json(
                watchdog_status,
                {
                    "schema_version": "simvla_collector_progress_watchdog_v1",
                    "state": "running",
                    "collector_pid": process.pid,
                    "stall_restarts": stall_restarts,
                    "seconds_since_status_progress": quiet_s,
                    "collector_status": current_status,
                    "updated_at_utc": datetime.now(timezone.utc).isoformat(),
                },
            )
            if quiet_s < args.stall_seconds:
                continue

            stalled = True
            stall_restarts += 1
            event = {
                "schema_version": "simvla_collector_stall_event_v1",
                "event": "collector_stall_detected",
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "collector_pid": process.pid,
                "seconds_without_status_progress": quiet_s,
                "stall_restart_number": stall_restarts,
                "source_episode_id": current_status.get("current_source_episode_id"),
                "global_episode_id": current_status.get("current_global_episode_id"),
                "completed_episodes": current_status.get("completed_episodes"),
                "training_rows_written": False,
                "risk_label_written": False,
            }
            append_jsonl_fsync(events_path, event)
            print(
                "COLLECTOR_STALL_DETECTED "
                f"source_episode_id={event['source_episode_id']} "
                f"quiet_seconds={quiet_s:.1f} restart={stall_restarts}",
                flush=True,
            )
            return_code, forced_kill = terminate_process_group(
                process,
                interrupt_grace_s=args.interrupt_grace_seconds,
                term_grace_s=args.term_grace_seconds,
            )
            append_jsonl_fsync(
                events_path,
                {
                    "schema_version": "simvla_collector_stall_event_v1",
                    "event": "collector_stall_process_stopped",
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                    "collector_pid": process.pid,
                    "collector_exit_code": return_code,
                    "forced_sigkill_after_graceful_signals": forced_kill,
                    "stall_restart_number": stall_restarts,
                    "training_rows_written": False,
                    "risk_label_written": False,
                },
            )
            print(
                "COLLECTOR_STALL_PROCESS_STOPPED "
                f"rc={return_code} pid={process.pid} forced_kill={forced_kill}",
                flush=True,
            )
            break

        if not stalled:
            process_return_code = int(process.wait())
            final_status, _ = read_status(status_path)
            return_code, status_error = effective_collector_return_code(
                process_return_code, final_status
            )
            if status_error is not None:
                append_jsonl_fsync(
                    events_path,
                    {
                        "schema_version": "simvla_collector_terminal_status_error_v1",
                        "event": "collector_missing_terminal_status",
                        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                        "collector_process_exit_code": process_return_code,
                        "effective_exit_code": return_code,
                        "collector_status": final_status,
                        "error": status_error,
                    },
                )
                print(f"COLLECTOR_TERMINAL_STATUS_ERROR {status_error}", flush=True)
            atomic_json(
                watchdog_status,
                {
                    "schema_version": "simvla_collector_progress_watchdog_v1",
                    "state": "complete" if return_code == 0 else "collector_failed",
                    "collector_exit_code": return_code,
                    "collector_process_exit_code": process_return_code,
                    "collector_status": final_status,
                    "terminal_status_error": status_error,
                    "stall_restarts": stall_restarts,
                    "updated_at_utc": datetime.now(timezone.utc).isoformat(),
                },
            )
            return return_code

        if stall_restarts > args.max_stall_restarts:
            atomic_json(
                watchdog_status,
                {
                    "schema_version": "simvla_collector_progress_watchdog_v1",
                    "state": "stall_restart_limit_exceeded",
                    "stall_restarts": stall_restarts,
                    "collector_status": observed_status,
                    "updated_at_utc": datetime.now(timezone.utc).isoformat(),
                },
            )
            return 124
        print("COLLECTOR_RESTARTING_FROM_ATOMIC_COMMIT_STATE", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--status", type=Path, required=True)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--watchdog-status", type=Path, required=True)
    parser.add_argument("--stall-seconds", type=float, default=1800.0)
    parser.add_argument("--poll-seconds", type=float, default=15.0)
    parser.add_argument("--interrupt-grace-seconds", type=float, default=60.0)
    parser.add_argument("--term-grace-seconds", type=float, default=120.0)
    parser.add_argument("--max-stall-restarts", type=int, default=5)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command and args.command[0] == "--":
        args.command = args.command[1:]
    return args


if __name__ == "__main__":
    raise SystemExit(run(parse_args()))
