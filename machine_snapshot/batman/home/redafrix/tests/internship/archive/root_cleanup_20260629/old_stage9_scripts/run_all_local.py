import subprocess
import time
from pathlib import Path
import shlex

NEW_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609")
TASKS = range(18)
MODELS = [
    {"label": "original_simvla", "policy": "simvla_only"},
    {"label": "modified_simvla", "policy": "simvla_only"},
    {"label": "modified_h10_risk_topk8", "policy": "risk_topk8"}
]

def run():
    print("Starting full production sweep...")
    activate_script = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
    runner_script = str(NEW_ROOT / "src/run_policy_matrix.py")

    for task_id in TASKS:
        for model in MODELS:
            label = model["label"]
            policy = model["policy"]
            config_path = NEW_ROOT / f"configs/task{task_id}_{label}.json"
            
            inner_script = (
                f"source {shlex.quote(activate_script)} >/dev/null; "
                f"export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8; "
                f"python3 {shlex.quote(runner_script)} --config {shlex.quote(str(config_path))} --policy {shlex.quote(policy)}"
            )
            
            now_str = time.strftime("%Y-%m-%dT%H:%M:%S")
            print(f"Launching Task {task_id} Label {label} at {now_str}", flush=True)
            res = subprocess.run(["bash", "-lc", inner_script])
            if res.returncode != 0:
                print(f"Warning: Task {task_id} {label} finished with code {res.returncode}", flush=True)

if __name__ == "__main__":
    run()