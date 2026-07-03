#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path


ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_10ep_comparison_20260611")
OLD_10EP_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609")
RUNNER_SRC = Path("/tmp/run_policy_matrix_selected_cap.py")


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main() -> None:
    (ROOT / "configs").mkdir(parents=True, exist_ok=True)
    (ROOT / "runs").mkdir(parents=True, exist_ok=True)
    (ROOT / "src").mkdir(parents=True, exist_ok=True)

    shutil.copy2(RUNNER_SRC, ROOT / "src" / "run_policy_matrix_selected_cap.py")
    shutil.copy2(OLD_10EP_ROOT / "src" / "collect_fiper_uncertainty_receding_dean_v1.py", ROOT / "src" / "collect_fiper_uncertainty_receding_dean_v1.py")

    seeds = list(range(10))
    base = {
        "suite": "libero_goal_object_ood",
        "reset_seeds": seeds,
        "checkpoint": "/tmp/ood_ckpt60000",
        "expected_checkpoint_sha256": "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71",
        "simvla_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified",
        "libero_pro_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO",
        "smolvlm_path": "/tmp/ood_smolvlm_cache",
        "norm_stats": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json",
        "risk_model_unc_topk8_dir": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8",
        "expected_topk8_dims": [6, 21, 25, 27, 23, 2, 26, 24],
        "history_steps": 16,
        "ace_candidate_count": 8,
        "execution_horizon": 10,
        "max_steps": 300,
        "model_denoise_steps": 10,
        "model_load_seed": 206080911,
        "global_action_seed": 206080920,
        "resolution": 128,
        "image_size": 384,
        "warmup": 10,
        "device": "cuda",
    }

    variants = [
        (
            "risk_topk8_selected_cap",
            {
                "selection_main_threshold": 0.3,
                "selection_streak_threshold": 0.3,
                "selection_min_margin": 0.02,
                "selection_strong_margin": 0.05,
                "selection_max_selected_score": 0.4,
                "selection_min_high_risk_streak": 1,
                "selection_cooldown_steps": 0,
                "selection_min_timestep": 0,
            },
        ),
        (
            "risk_topk8_threshold_05",
            {
                "selection_main_threshold": 0.5,
                "selection_streak_threshold": 0.5,
                "selection_min_margin": 0.02,
                "selection_strong_margin": 0.05,
                "selection_min_high_risk_streak": 1,
                "selection_cooldown_steps": 0,
                "selection_min_timestep": 0,
            },
        ),
        (
            "risk_topk8_threshold_q95",
            {
                "selection_main_threshold": "q95",
                "selection_streak_threshold": "q95",
                "selection_min_margin": 0.02,
                "selection_strong_margin": 0.05,
                "selection_min_high_risk_streak": 1,
                "selection_cooldown_steps": 0,
                "selection_min_timestep": 0,
            },
        ),
        (
            "risk_topk8_selected_cap_delay30",
            {
                "selection_main_threshold": 0.3,
                "selection_streak_threshold": 0.3,
                "selection_min_margin": 0.02,
                "selection_strong_margin": 0.05,
                "selection_max_selected_score": 0.4,
                "selection_min_high_risk_streak": 1,
                "selection_cooldown_steps": 0,
                "selection_min_timestep": 30,
            },
        ),
    ]

    for tid in range(18):
        for variant, controls in variants:
            cfg = dict(base)
            cfg.update(
                {
                    "task_id": tid,
                    "experiment_id": f"task{tid}_{variant}",
                    "output_dir": str(ROOT / "runs" / f"task{tid}" / variant),
                    **controls,
                }
            )
            write_json(ROOT / "configs" / f"task{tid}_{variant}.json", cfg)

    write_json(
        ROOT / "configs" / "seed_plan.json",
        {
            "reset_seeds": seeds,
            "seed_policy": "match Bob corrected 10ep OOD aggressive-fixed run seeds 0..9 for paired comparison",
            "global_action_seed": 206080920,
            "model_load_seed": 206080911,
            "baseline_source_root": str(OLD_10EP_ROOT),
        },
    )

    run_all = """#!/usr/bin/env python3
from __future__ import annotations

import os
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ACTIVATE = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
RUNNER = ROOT / "src" / "run_policy_matrix_selected_cap.py"

variants = [
    "risk_topk8_selected_cap",
    "risk_topk8_threshold_05",
    "risk_topk8_threshold_q95",
    "risk_topk8_selected_cap_delay30",
]

for tid in range(18):
    for variant in variants:
        cfg = f"task{tid}_{variant}.json"
        inner = (
            f"source {shlex.quote(ACTIVATE)} >/dev/null; "
            "export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 "
            "USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "
            "CUBLAS_WORKSPACE_CONFIG=:4096:8; "
            f"python3 {shlex.quote(str(RUNNER))} --config {shlex.quote(str(ROOT / 'configs' / cfg))} --policy risk_topk8"
        )
        print("[run_all]", inner, flush=True)
        rc = subprocess.call(["bash", "-lc", inner])
        if rc != 0:
            print(f"[run_all] FAILED tid={tid} variant={variant} rc={rc}", flush=True)
            sys.exit(rc)

print("[run_all] COMPLETE", flush=True)
"""
    (ROOT / "run_all.py").write_text(run_all)
    os.chmod(ROOT / "run_all.py", 0o755)
    print(ROOT)
    print("configs", len(list((ROOT / "configs").glob("task*.json"))))


if __name__ == "__main__":
    main()
