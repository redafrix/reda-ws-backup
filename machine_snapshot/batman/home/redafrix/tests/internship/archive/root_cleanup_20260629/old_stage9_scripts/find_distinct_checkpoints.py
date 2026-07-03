import os
import json
import glob
from collections import defaultdict

roots = [
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608"
]

inventory = []

for root in roots:
    # Find all config json files under root/configs
    config_pattern = os.path.join(root, "configs/**/*.json")
    config_files = glob.glob(config_pattern, recursive=True)
    for cf in config_files:
        if os.path.basename(cf) in ["online_seed_plan.json", "online_jobs.json", "seed_plan.json"]:
            continue
        try:
            with open(cf, 'r') as f:
                cfg = json.load(f)
            
            # Skip if it is not a runner config (must have policy or checkpoint)
            if not isinstance(cfg, dict) or ("checkpoint" not in cfg and "policy" not in cfg):
                continue
                
            checkpoint = cfg.get("checkpoint", "")
            policy = cfg.get("policy", "")
            risk_model_dir = cfg.get("risk_model_dir", "")
            selected_uncertainty_dims = cfg.get("selected_uncertainty_dims", [])
            execution_horizon = cfg.get("execution_horizon", "")
            controls = cfg.get("selection_controls", {})
            threshold = controls.get("selection_main_threshold", "")
            task_id = cfg.get("task_id", "")
            suite = cfg.get("suite", "")
            
            inventory.append({
                "root": root,
                "config_file": os.path.relpath(cf, root),
                "suite": suite,
                "task_id": task_id,
                "policy": policy,
                "checkpoint": checkpoint,
                "risk_model_dir": risk_model_dir,
                "selected_uncertainty_dims": selected_uncertainty_dims,
                "execution_horizon": execution_horizon,
                "threshold": threshold
            })
        except Exception as e:
            print(f"Error reading {cf}: {e}")

# Group the inventory by distinct properties to see what combinations exist
distinct_combos = defaultdict(list)
for item in inventory:
    key = (item["suite"], item["task_id"], item["policy"], item["checkpoint"], item["risk_model_dir"], tuple(item["selected_uncertainty_dims"]), item["execution_horizon"], item["threshold"])
    distinct_combos[key].append(item["config_file"])

print(f"Found {len(inventory)} configs in total.")
print(f"Distinct combinations: {len(distinct_combos)}")
for key, files in distinct_combos.items():
    suite, task_id, policy, checkpoint, risk_model_dir, dims, horizon, thresh = key
    print(f"\nCombo:")
    print(f"  Files: {files[:3]} (count={len(files)})")
    print(f"  Suite/Task: {suite} / {task_id}")
    print(f"  Policy: {policy}")
    print(f"  Checkpoint: {checkpoint}")
    print(f"  Risk Model Dir: {risk_model_dir}")
    print(f"  Dims: {dims}")
    print(f"  Horizon: {horizon}")
    print(f"  Threshold: {thresh}")
