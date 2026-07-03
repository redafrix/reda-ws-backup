#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path


ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608")
ACTIVATE = Path("/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh")
RUNNER = ROOT / "src/run_policy_matrix.py"


def shell_cmd(job: dict, smoke: bool) -> str:
    args = [
        "/usr/bin/python3",
        str(RUNNER),
        "--config",
        job["config"],
        "--policy",
        job["policy"],
    ]
    if smoke:
        args.append("--smoke")
    command = " ".join(shlex.quote(x) for x in args)
    return (
        f"source {shlex.quote(str(ACTIVATE))} >/dev/null; "
        "export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 "
        "TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8; "
        f"{command}"
    )


def run_one(job: dict, smoke: bool, log_path: Path) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"[start] {time.strftime('%Y-%m-%dT%H:%M:%S%z')} smoke={smoke} job={job}\n")
        log.flush()
        proc = subprocess.Popen(["bash", "-lc", shell_cmd(job, smoke)], stdout=log, stderr=subprocess.STDOUT)
        code = proc.wait()
        log.write(f"[end] {time.strftime('%Y-%m-%dT%H:%M:%S%z')} code={code}\n")
        return int(code)


def run_group(jobs: list[dict], log_dir: Path) -> None:
    procs = []
    for job in sorted(jobs, key=lambda x: int(x["shard"])):
        log_path = log_dir / f"prod_task{job['task_id']}_{job['label']}_s{job['shard']}.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log = log_path.open("w", encoding="utf-8")
        log.write(f"[start] {time.strftime('%Y-%m-%dT%H:%M:%S%z')} job={job}\n")
        log.flush()
        proc = subprocess.Popen(["bash", "-lc", shell_cmd(job, False)], stdout=log, stderr=subprocess.STDOUT)
        procs.append((job, proc, log, log_path))
    failures = []
    for job, proc, log, log_path in procs:
        code = proc.wait()
        log.write(f"[end] {time.strftime('%Y-%m-%dT%H:%M:%S%z')} code={code}\n")
        log.close()
        if code != 0:
            failures.append((job, code, str(log_path)))
    if failures:
        raise RuntimeError(f"production group failed: {failures}")


def main() -> None:
    jobs_path = ROOT / "configs/online_jobs.json"
    jobs = json.loads(jobs_path.read_text())["jobs"]
    log_dir = ROOT / "logs/online"
    status_path = ROOT / "logs/online_status.json"

    groups: dict[tuple[int, str], list[dict]] = defaultdict(list)
    for job in jobs:
        groups[(int(job["task_id"]), str(job["label"]))].append(job)

    smoke_failures = []
    for job in jobs:
        log_path = log_dir / f"smoke_task{job['task_id']}_{job['label']}_s{job['shard']}.log"
        code = run_one(job, True, log_path)
        if code != 0:
            smoke_failures.append((job, code, str(log_path)))
    if smoke_failures:
        raise RuntimeError(f"smoke failures: {smoke_failures}")

    order = ["original_simvla", "original_h10_risk_base", "modified_simvla", "modified_h10_risk_topk8"]
    completed = []
    for task_id in [3, 6, 8]:
        for label in order:
            key = (task_id, label)
            if key not in groups:
                continue
            status_path.write_text(json.dumps({"running": {"task_id": task_id, "label": label}, "completed": completed}, indent=2) + "\n")
            run_group(groups[key], log_dir)
            completed.append({"task_id": task_id, "label": label, "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z")})
            status_path.write_text(json.dumps({"running": None, "completed": completed}, indent=2) + "\n")
    print(json.dumps({"completed_groups": completed}, indent=2), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
