#!/usr/bin/env python3
from __future__ import annotations

import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_10ep_comparison_20260611")
ACTIVATE = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
RUNNER = ROOT / "src" / "run_policy_matrix_selected_cap.py"

VARIANTS = [
    "risk_topk8_selected_cap",
    "risk_topk8_selected_cap_delay30",
]


def completed_rows(task_id: int, variant: str) -> int:
    path = ROOT / "runs" / f"task{task_id}" / variant / "risk_topk8" / "episode_summaries.jsonl"
    if not path.exists():
        return 0
    with path.open() as f:
        return sum(1 for line in f if line.strip())


def main() -> int:
    print("[resume] selected-cap-only Bob 10ep queue", flush=True)
    print(f"[resume] root={ROOT}", flush=True)
    for task_id in range(18):
        for variant in VARIANTS:
            rows = completed_rows(task_id, variant)
            if rows >= 10:
                print(f"[resume] SKIP complete task={task_id} variant={variant} rows={rows}", flush=True)
                continue

            cfg = ROOT / "configs" / f"task{task_id}_{variant}.json"
            inner = (
                f"source {shlex.quote(ACTIVATE)} >/dev/null; "
                "export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 "
                "USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "
                "CUBLAS_WORKSPACE_CONFIG=:4096:8; "
                f"python3 {shlex.quote(str(RUNNER))} --config {shlex.quote(str(cfg))} --policy risk_topk8"
            )
            print(f"[resume] RUN task={task_id} variant={variant} existing_rows={rows}", flush=True)
            print("[resume]", inner, flush=True)
            rc = subprocess.call(["bash", "-lc", inner])
            if rc != 0:
                print(f"[resume] FAILED task={task_id} variant={variant} rc={rc}", flush=True)
                return rc

    print("[resume] COMPLETE selected-cap-only queue", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
