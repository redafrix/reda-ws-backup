#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(
    "/home/dean/fiper_uncertainty_collection/realtime_deployment/"
    "ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611"
)


def main() -> None:
    (ROOT / "configs").mkdir(parents=True, exist_ok=True)
    (ROOT / "runs").mkdir(parents=True, exist_ok=True)

    seeds = list(range(400, 500))
    base = {
        "suite": "libero_goal_object_ood",
        "reset_seeds": seeds,
        "checkpoint": "/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000",
        "expected_checkpoint_sha256": "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71",
        "simvla_root": "/home/redafrix/SimVLA_modified",
        "libero_pro_root": "/home/redafrix/LIBERO-PRO",
        "smolvlm_path": "/home/redafrix/.cache/huggingface/hub/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47",
        "norm_stats": "/home/redafrix/SimVLA_modified/norm_stats/libero_norm.json",
        "risk_model_unc_topk8_dir": "/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/unc_topk8",
        "expected_topk8_dims": [6, 21, 25, 27, 23, 2, 26, 24],
        "history_steps": 16,
        "ace_candidate_count": 8,
        "execution_horizon": 10,
        "max_steps": 300,
        "model_denoise_steps": 10,
        "model_load_seed": 906101111,
        "global_action_seed": 906101120,
        "resolution": 128,
        "image_size": 384,
        "warmup": 10,
        "device": "cuda",
    }

    for tid in range(18):
        baseline = dict(base)
        baseline.update(
            {
                "task_id": tid,
                "experiment_id": f"task{tid}_modified_simvla",
                "output_dir": str(ROOT / "runs" / f"task{tid}" / "modified_simvla"),
            }
        )
        (ROOT / "configs" / f"task{tid}_modified_simvla.json").write_text(
            json.dumps(baseline, indent=2, sort_keys=True) + "\n"
        )

        risk = dict(base)
        risk.update(
            {
                "task_id": tid,
                "experiment_id": f"task{tid}_risk_topk8_selected_cap_delay30",
                "output_dir": str(ROOT / "runs" / f"task{tid}" / "risk_topk8_selected_cap_delay30"),
                "selection_main_threshold": 0.3,
                "selection_streak_threshold": 0.3,
                "selection_min_margin": 0.02,
                "selection_strong_margin": 0.05,
                "selection_max_selected_score": 0.4,
                "selection_min_high_risk_streak": 1,
                "selection_cooldown_steps": 0,
                "selection_min_timestep": 30,
            }
        )
        (ROOT / "configs" / f"task{tid}_risk_topk8_selected_cap_delay30.json").write_text(
            json.dumps(risk, indent=2, sort_keys=True) + "\n"
        )

    (ROOT / "configs" / "seed_plan.json").write_text(
        json.dumps(
            {
                "reset_seeds": seeds,
                "seed_policy": "Dean paired 100ep delay30 replication seeds, disjoint from 0..399 prior OOD sweeps",
                "global_action_seed": 906101120,
                "model_load_seed": 906101111,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    run_all = """#!/usr/bin/env python3
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
"""
    (ROOT / "run_all.py").write_text(run_all)
    os.chmod(ROOT / "run_all.py", 0o755)

    print(ROOT)
    print("configs", len(list((ROOT / "configs").glob("*.json"))))
    print("seeds", seeds[0], seeds[-1], len(seeds))


if __name__ == "__main__":
    main()
