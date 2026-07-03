import subprocess
import time
from pathlib import Path
import shlex
import sys

NEW_ROOT = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615")
TASKS = [0, 17]
MODELS = [
    {"label": "original_simvla", "policy": "simvla_only"},
    {"label": "modified_simvla", "policy": "simvla_only"},
    {"label": "risk_topk8_selected_cap", "policy": "risk_topk8"}
]

def run():
    print("Starting smoke test...", flush=True)
    activate_script = "/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh"
    runner_script = str(NEW_ROOT / "src/run_policy_matrix.py")

    for task_id in TASKS:
        for model in MODELS:
            label = model["label"]
            policy = model["policy"]
            config_path = NEW_ROOT / f"configs/task{task_id}_{label}.json"
            
            import json
            with open(config_path, "r") as f:
                cfg = json.load(f)
            cfg["reset_seeds"] = [10]
            smoke_config_path = NEW_ROOT / f"configs/task{task_id}_{label}_smoke.json"
            with open(smoke_config_path, "w") as f:
                json.dump(cfg, f, indent=2)

            inner_script = (
                f"source {shlex.quote(activate_script)} >/dev/null; "
                f"export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8; "
                f"python3 {shlex.quote(runner_script)} --config {shlex.quote(str(smoke_config_path))} --policy {shlex.quote(policy)}"
            )
            
            now_str = time.strftime("%Y-%m-%dT%H:%M:%S")
            print(f"Launching Smoke Task {task_id} Label {label} at {now_str}", flush=True)
            res = subprocess.run(["bash", "-lc", inner_script])
            if res.returncode != 0:
                print(f"Error: Smoke test failed for Task {task_id} {label} with code {res.returncode}", flush=True)
                sys.exit(1)

if __name__ == "__main__":
    run()