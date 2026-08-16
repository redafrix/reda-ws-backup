#!/usr/bin/env python3
"""Run one bounded health check after the first production episode commits."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--collector-log", type=Path, required=True)
    parser.add_argument("--report-json", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    args = parser.parse_args()
    root = args.output_dir.resolve()
    deadline = time.monotonic() + args.timeout_seconds
    episode_dirs: list[Path] = []
    while time.monotonic() < deadline:
        episode_dirs = sorted(
            path
            for path in (root / "episodes").glob("*")
            if path.is_dir() and (path / "COMMITTED").is_file()
        )
        if episode_dirs:
            break
        process = subprocess.run(
            ["pgrep", "-af", "[c]ollect_isaac_risk.py"],
            capture_output=True,
            text=True,
        )
        if process.returncode != 0:
            raise RuntimeError("collector exited before its first committed episode")
        time.sleep(10)
    if not episode_dirs:
        raise TimeoutError("first episode did not commit before health-check timeout")

    first = episode_dirs[0]
    manifest = json.loads((root / "run_manifest.json").read_text())
    status = json.loads((root / "live_status.json").read_text())
    summary = json.loads((first / "summary.json").read_text())
    validation = json.loads((first / "validation.json").read_text())
    rows_payload = (first / "risk_rows.jsonl").read_bytes()
    log_text = args.collector_log.read_text(errors="replace")
    if "Traceback (most recent call last)" in log_text:
        raise RuntimeError("collector log contains a traceback")
    if hashlib.sha256(rows_payload).hexdigest() != validation["rows_sha256"]:
        raise RuntimeError("first committed episode hash mismatch")
    if manifest["timing"]["max_sim_steps"] != 2400:
        raise RuntimeError("run manifest does not use 2400 simulator steps")
    if manifest["timing"]["max_control_ticks"] != 600:
        raise RuntimeError("run manifest does not use 600 control ticks")
    if manifest["timing"]["max_decision_rows"] != 60:
        raise RuntimeError("run manifest does not use 60 H10 replans")
    if manifest["execution_mode"] != "chunk_h10":
        raise RuntimeError("run manifest does not use chunk_h10")
    if not manifest["round"]["enabled"] or manifest["round"]["round_id"] != 0:
        raise RuntimeError("run manifest does not identify Round 0")
    if summary.get("synthetic_smoke") or not summary.get("training_eligible"):
        raise RuntimeError("first production episode has invalid eligibility markers")

    gpu = subprocess.run(
        [
            "nvidia-smi",
            "--query-compute-apps=pid,process_name,used_memory",
            "--format=csv,noheader,nounits",
        ],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()
    process = subprocess.run(
        ["pgrep", "-af", "[c]ollect_isaac_risk.py"],
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        raise RuntimeError("collector is no longer alive after first commit")
    report = {
        "pass": True,
        "collector_process": process.stdout.strip(),
        "gpu_compute_processes": gpu,
        "output_dir": str(root),
        "first_committed_episode": first.name,
        "first_episode_source_id": summary["source_episode_id"],
        "first_episode_outcome": summary["outcome"],
        "first_episode_decision_rows": summary["decision_rows"],
        "live_status": status,
        "round_id": manifest["round"]["round_id"],
        "round_schedule_sha256": manifest["round"]["schedule"][
            "benchmark_episode_ids_sha256"
        ],
        "max_sim_steps": 2400,
        "max_control_ticks": 600,
        "max_decision_rows": 60,
        "execution_mode": "chunk_h10",
        "checkpoint_sha256": manifest["checkpoint"]["model_sha256"],
        "traceback_present": False,
    }
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
