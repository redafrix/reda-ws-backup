#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = "/home/redafrix/miniconda3/envs/simvla/bin/python"
RUNNER = ROOT.parent / "src" / "run_policy_matrix_selected_cap.py"
ENV = os.environ.copy()
ENV.update(
    {
        "USE_TF": "0",
        "TRANSFORMERS_NO_TF": "1",
        "USE_FLAX": "0",
        "PYTHONPATH": "/home/redafrix/LIBERO-PRO:/home/redafrix/SimVLA_modified",
    }
)

for tid in range(18):
    jobs = [
        (f"task{tid}_modified_simvla.json", "simvla_only"),
        (f"task{tid}_risk_topk8_selected_cap_delay30.json", "risk_topk8"),
    ]
    for cfg, policy in jobs:
        cmd = [PY, str(RUNNER), "--config", str(ROOT / "configs" / cfg), "--policy", policy]
        print("[run_all]", " ".join(cmd), flush=True)
        rc = subprocess.call(cmd, env=ENV)
        if rc != 0:
            print(f"[run_all] FAILED tid={tid} policy={policy} rc={rc}", flush=True)
            sys.exit(rc)

print("[run_all] COMPLETE", flush=True)
