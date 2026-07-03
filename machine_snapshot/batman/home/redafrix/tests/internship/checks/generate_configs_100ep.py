import json
from pathlib import Path

NEW_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609")
TASKS = range(18)
MODELS = [
    {"label": "original_simvla", "checkpoint": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO", "policy": "simvla_only"},
    {"label": "modified_simvla", "checkpoint": "/tmp/ood_ckpt60000", "policy": "simvla_only"},
    {"label": "modified_h10_risk_topk8", "checkpoint": "/tmp/ood_ckpt60000", "policy": "risk_topk8"}
]

# We will use seeds 10 to 109 (100 unique seeds, disjoint from smoke/10ep seeds 0-9)
RESET_SEEDS = list(range(10, 110))

def run():
    NEW_ROOT.joinpath("configs").mkdir(parents=True, exist_ok=True)
    
    # Save seed_plan.json
    seed_plan = {"reset_seeds": RESET_SEEDS}
    seed_plan_path = NEW_ROOT / "configs/seed_plan.json"
    seed_plan_path.write_text(json.dumps(seed_plan, indent=2))
    print(f"Saved seed plan to {seed_plan_path}")
    
    for task_id in TASKS:
        for model in MODELS:
            label = model["label"]
            config_path = NEW_ROOT / f"configs/task{task_id}_{label}.json"
            
            cfg = {
                "ace_candidate_count": 8,
                "checkpoint": model["checkpoint"],
                "execution_horizon": 10,
                "experiment_id": f"task{task_id}_{label}",
                "global_action_seed": 206080920,
                "history_steps": 16,
                "image_size": 384,
                "libero_pro_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO",
                "max_steps": 300,
                "model_denoise_steps": 10,
                "model_load_seed": 206080911,
                "norm_stats": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json",
                "output_dir": str(NEW_ROOT / f"runs/task{task_id}/{label}"),
                "reset_seeds": RESET_SEEDS,
                "resolution": 128,
                "simvla_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified",
                "smolvlm_path": "/tmp/ood_smolvlm_cache",
                "suite": "libero_goal_object_ood",
                "task_id": task_id,
                "warmup": 10
            }
            
            if model["policy"] == "risk_topk8":
                cfg["risk_model_unc_topk8_dir"] = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8"
                # Flattened keys matching src/run_policy_matrix.py parser requirements
                cfg["selection_main_threshold"] = 0.3
                cfg["selection_streak_threshold"] = 0.3
                cfg["selection_min_margin"] = 0.02
                cfg["selection_strong_margin"] = 0.05
                
            config_path.write_text(json.dumps(cfg, indent=2))
            print(f"Generated {config_path.name}")

if __name__ == "__main__":
    run()
