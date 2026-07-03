import os
import json
import subprocess
from pathlib import Path

# Paths
SRC_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609")
NEW_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610")
RESET_SEEDS = list(range(10, 110))

setup_code = f"""
import os
import json
import shutil
from pathlib import Path

SRC_ROOT = Path("{SRC_ROOT}")
NEW_ROOT = Path("{NEW_ROOT}")
RESET_SEEDS = {RESET_SEEDS}

# 1. Create directory structure
NEW_ROOT.mkdir(parents=True, exist_ok=True)
NEW_ROOT.joinpath("configs").mkdir(parents=True, exist_ok=True)

# 2. Copy src folder
if os.path.exists(SRC_ROOT / "src"):
    shutil.copytree(SRC_ROOT / "src", NEW_ROOT / "src", dirs_exist_ok=True)
    print("Copied src folder successfully.")
else:
    print("Error: src folder not found at SRC_ROOT.")

# 3. Save seed plan
seed_plan = {{"reset_seeds": RESET_SEEDS}}
with open(NEW_ROOT / "configs/seed_plan.json", "w") as f:
    json.dump(seed_plan, f, indent=2)

# 4. Generate configs for modified_h10_risk_topk8 only
label = "modified_h10_risk_topk8"
for task_id in range(18):
    config_path = NEW_ROOT / f"configs/task{{task_id}}_{{label}}.json"
    cfg = {{
        "ace_candidate_count": 8,
        "checkpoint": "/tmp/ood_ckpt60000",
        "execution_horizon": 10,
        "experiment_id": f"task{{task_id}}_{{label}}",
        "global_action_seed": 206080920,
        "history_steps": 16,
        "image_size": 384,
        "libero_pro_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO",
        "max_steps": 300,
        "model_denoise_steps": 10,
        "model_load_seed": 206080911,
        "norm_stats": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json",
        "output_dir": str(NEW_ROOT / f"runs/task{{task_id}}/{{label}}"),
        "reset_seeds": RESET_SEEDS,
        "resolution": 128,
        "simvla_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified",
        "smolvlm_path": "/tmp/ood_smolvlm_cache",
        "suite": "libero_goal_object_ood",
        "task_id": task_id,
        "warmup": 10,
        "risk_model_unc_topk8_dir": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8",
        # Flattened threshold 0.5 settings
        "selection_main_threshold": 0.5,
        "selection_streak_threshold": 0.5,
        "selection_min_margin": 0.02,
        "selection_strong_margin": 0.05
    }}
    with open(config_path, "w") as f:
        json.dump(cfg, f, indent=2)

print("Generated 18 configs for modified_h10_risk_topk8 with threshold 0.5.")

# 5. Write run_all.py execution script
run_all_code = \"\"\"
import subprocess
import time
from pathlib import Path
import shlex

NEW_ROOT = Path("{NEW_ROOT}")
TASKS = range(18)
label = "modified_h10_risk_topk8"
policy = "risk_topk8"

def run():
    print("Starting threshold 0.5 sweep...", flush=True)
    activate_script = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
    runner_script = str(NEW_ROOT / "src/run_policy_matrix.py")

    for task_id in TASKS:
        config_path = NEW_ROOT / f"configs/task{{task_id}}_{{label}}.json"
        
        inner_script = (
            f"source {{shlex.quote(activate_script)}} >/dev/null; "
            f"export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8; "
            f"python3 {{shlex.quote(runner_script)}} --config {{shlex.quote(str(config_path))}} --policy {{shlex.quote(policy)}}"
        )
        
        now_str = time.strftime("%Y-%m-%dT%H:%M:%S")
        print(f"Launching Task {{task_id}} at {{now_str}}", flush=True)
        res = subprocess.run(["bash", "-lc", inner_script])
        if res.returncode != 0:
            print(f"Warning: Task {{task_id}} finished with code {{res.returncode}}", flush=True)

if __name__ == '__main__':
    run()
\"\"\".strip()

with open(NEW_ROOT / "run_all.py", "w") as f:
    f.write(run_all_code)
print("Wrote run_all.py successfully.")
"""

# Let's execute this setup python code on Bob using SSH
p = subprocess.run(["ssh", "pcrobot", "python3 -"], input=setup_code, text=True, capture_output=True)
if p.returncode != 0:
    print(f"Failed to execute setup on Bob: {p.stderr}")
else:
    print("Setup completed successfully on Bob:")
    print(p.stdout)
    
    # Now launch the tmux session
    tmux_cmd = f"tmux new-session -d -s ood_production_threshold_0.5_100ep_20260610 'cd {NEW_ROOT} && python3 run_all.py > sweep_supervisor.log 2>&1'"
    p_tmux = subprocess.run(["ssh", "pcrobot", tmux_cmd], text=True, capture_output=True)
    if p_tmux.returncode != 0:
        print(f"Failed to launch tmux session on Bob: {p_tmux.stderr}")
    else:
        print("TMUX session 'ood_production_threshold_0.5_100ep_20260610' launched successfully!")
