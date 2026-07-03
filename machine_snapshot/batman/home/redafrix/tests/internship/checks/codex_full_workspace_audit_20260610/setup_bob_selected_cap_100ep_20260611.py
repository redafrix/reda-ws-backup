#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

OLD_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609")
SRC_10EP_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_10ep_comparison_20260611")
ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_100ep_comparison_20260611")
ACTIVATE = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"

VARIANTS = {
    "risk_topk8_selected_cap": {
        "selection_main_threshold": 0.3,
        "selection_streak_threshold": 0.3,
        "selection_min_high_risk_streak": 1,
        "selection_min_margin": 0.02,
        "selection_strong_margin": 0.05,
        "selection_max_selected_score": 0.4,
        "selection_cooldown_steps": 0,
        "selection_min_timestep": 0,
    },
    "risk_topk8_selected_cap_delay30": {
        "selection_main_threshold": 0.3,
        "selection_streak_threshold": 0.3,
        "selection_min_high_risk_streak": 1,
        "selection_min_margin": 0.02,
        "selection_strong_margin": 0.05,
        "selection_max_selected_score": 0.4,
        "selection_cooldown_steps": 0,
        "selection_min_timestep": 30,
    },
}


def main() -> None:
    for d in [ROOT, ROOT / "configs", ROOT / "runs", ROOT / "src", ROOT / "logs"]:
        d.mkdir(parents=True, exist_ok=True)

    shutil.copy2(SRC_10EP_ROOT / "src" / "run_policy_matrix_selected_cap.py", ROOT / "src" / "run_policy_matrix_selected_cap.py")
    shutil.copy2(SRC_10EP_ROOT / "src" / "collect_fiper_uncertainty_receding_dean_v1.py", ROOT / "src" / "collect_fiper_uncertainty_receding_dean_v1.py")

    for tid in range(18):
        template_path = OLD_ROOT / "configs" / f"task{tid}_modified_h10_risk_topk8.json"
        cfg0 = json.loads(template_path.read_text())
        for variant, controls in VARIANTS.items():
            cfg = dict(cfg0)
            cfg.update(controls)
            cfg["output_dir"] = str(ROOT / "runs" / f"task{tid}" / variant)
            cfg["experiment_root"] = str(ROOT)
            cfg["policy_label"] = variant
            cfg["comparison_source_root"] = str(OLD_ROOT)
            cfg["comparison_seed_policy"] = "match Bob 100ep OOD aggressive-fixed seeds 10..109 for paired comparison against original_simvla, modified_simvla, and topk8_t03"
            out = ROOT / "configs" / f"task{tid}_{variant}.json"
            out.write_text(json.dumps(cfg, indent=2, sort_keys=True))

    run_all = f'''#!/usr/bin/env python3
from __future__ import annotations

import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path({str(ROOT)!r})
ACTIVATE = {ACTIVATE!r}
RUNNER = ROOT / "src" / "run_policy_matrix_selected_cap.py"
VARIANTS = {list(VARIANTS.keys())!r}


def completed_rows(task_id: int, variant: str) -> int:
    p = ROOT / "runs" / f"task{{task_id}}" / variant / "risk_topk8" / "episode_summaries.jsonl"
    if not p.exists():
        return 0
    return sum(1 for line in p.open() if line.strip())


for task_id in range(18):
    for variant in VARIANTS:
        rows = completed_rows(task_id, variant)
        if rows >= 100:
            print(f"[run_all_100] SKIP complete task={{task_id}} variant={{variant}} rows={{rows}}", flush=True)
            continue
        cfg = ROOT / "configs" / f"task{{task_id}}_{{variant}}.json"
        inner = (
            f"source {{shlex.quote(ACTIVATE)}} >/dev/null; "
            "export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 "
            "USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "
            "CUBLAS_WORKSPACE_CONFIG=:4096:8; "
            f"python3 {{shlex.quote(str(RUNNER))}} --config {{shlex.quote(str(cfg))}} --policy risk_topk8"
        )
        print(f"[run_all_100] RUN task={{task_id}} variant={{variant}} existing_rows={{rows}}", flush=True)
        print("[run_all_100] " + inner, flush=True)
        rc = subprocess.call(["bash", "-lc", inner])
        if rc != 0:
            print(f"[run_all_100] FAILED task={{task_id}} variant={{variant}} rc={{rc}}", flush=True)
            sys.exit(rc)
print("[run_all_100] COMPLETE", flush=True)
'''
    (ROOT / "run_all.py").write_text(run_all)
    os.chmod(ROOT / "run_all.py", 0o755)

    manifest = {
        "root": str(ROOT),
        "source_100ep_root": str(OLD_ROOT),
        "source_10ep_selected_cap_root": str(SRC_10EP_ROOT),
        "variants": VARIANTS,
        "tasks": list(range(18)),
        "seeds": list(range(10, 110)),
        "expected_episodes": 18 * len(VARIANTS) * 100,
        "execution": "sequential single GPU queue",
    }
    (ROOT / "launch_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    print(ROOT)
    print("configs", len(list((ROOT / "configs").glob("task*.json"))))


if __name__ == "__main__":
    main()
