#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
SCRIPT = Path("/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/src/run_policy_matrix_selected_cap.py")
PYTHON = "/home/redafrix/miniconda3/envs/simvla/bin/python"

configs = [ROOT / "configs" / f"task{i}_risk_topk8_selected_cap_m10.json" for i in range(18)]

for cfg in configs:
    print(f"[run_all_m10] START {cfg.name}", flush=True)
    rc = subprocess.call([PYTHON, str(SCRIPT), "--config", str(cfg), "--policy", "risk_topk8"])
    print(f"[run_all_m10] END {cfg.name} rc={rc}", flush=True)
    if rc != 0:
        sys.exit(rc)
    time.sleep(1)

print("[run_all_m10] COMPLETE", flush=True)
