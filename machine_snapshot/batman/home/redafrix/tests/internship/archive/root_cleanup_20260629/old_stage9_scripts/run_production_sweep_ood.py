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

# Paths on Bob (External SSD)
ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_full_sweep_20260609")
ACTIVATE = Path("/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh")
RUNNER = ROOT / "src/run_policy_matrix.py"

def shell_cmd(job: dict, smoke: bool) -> str:
    args = [
        "/usr/bin/python3",
        str(RUNNER),
        "--config",
        str(ROOT / job["config"]),
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
        # Use -l to ensure shell activation
        proc = subprocess.Popen(["bash", "-lc", shell_cmd(job, smoke)], stdout=log, stderr=subprocess.STDOUT)
        code = proc.wait()
        log.write(f"[end] {time.strftime('%Y-%m-%dT%H:%M:%S%z')} code={code}\n")
        return int(code)

def main() -> None:
    jobs_path = ROOT / "configs/online_jobs.json"
    if not jobs_path.exists():
        print(f"ERROR: online_jobs.json not found at {jobs_path}")
        sys.exit(1)
        
    jobs_data = json.loads(jobs_path.read_text())
    jobs = jobs_data["jobs"]
    log_dir = ROOT / "logs/online"
    status_path = ROOT / "logs/online_status.json"
    
    # Smoke Test all jobs first to ensure model/env loading works for all pairs
    print("Starting smoke tests for all 54 jobs...")
    smoke_failures = []
    for job in jobs:
        log_path = log_dir / f"smoke_task{job['task_id']}_{job['label']}.log"
        code = run_one(job, True, log_path)
        if code != 0:
            print(f"Smoke failure for task {job['task_id']} label {job['label']}")
            smoke_failures.append((job, code, str(log_path)))
            
    if smoke_failures:
        print(f"WARNING: {len(smoke_failures)} jobs failed smoke test.")
        # We continue anyway for the successful ones
    
    # Group jobs by task
    groups: dict[int, list[dict]] = defaultdict(list)
    for job in jobs:
        groups[int(job["task_id"])].append(job)
        
    order = ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]
    completed = []
    
    print("Starting production sweep...")
    for task_id in sorted(groups.keys()):
        task_jobs = groups[task_id]
        # Sort task_jobs by the preferred label order
        task_jobs.sort(key=lambda x: order.index(x["label"]) if x["label"] in order else 99)
        
        for job in task_jobs:
            label = job["label"]
            print(f"Running Task {task_id} Label {label}...")
            
            status_path.parent.mkdir(parents=True, exist_ok=True)
            status_path.write_text(json.dumps({
                "running": {"task_id": task_id, "label": label}, 
                "completed": completed,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z")
            }, indent=2) + "\n")
            
            log_path = log_dir / f"prod_task{task_id}_{label}.log"
            code = run_one(job, False, log_path)
            
            completed.append({
                "task_id": task_id, 
                "label": label, 
                "exit_code": code,
                "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z")
            })
            
            status_path.write_text(json.dumps({
                "running": None, 
                "completed": completed,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z")
            }, indent=2) + "\n")

if __name__ == "__main__":
    main()
