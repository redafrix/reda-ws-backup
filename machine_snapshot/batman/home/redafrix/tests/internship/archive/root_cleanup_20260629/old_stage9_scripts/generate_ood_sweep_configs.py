import json
import os
from pathlib import Path

# Paths on Bob (External SSD)
BASE_DIR = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_full_sweep_20260609"
CKPT_VANILLA = "/tmp/vanilla-simvla" 
CKPT_MODIFIED = "/tmp/ckpt-60000-tmp"
RISK_MODEL_DIR = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8"
SMOLVLM_CACHE = "/tmp/smolvlm_cache" 

TASKS = [
    "open_the_middle_drawer_of_the_cabinet(yellow_cabinet)",
    "open_the_top_drawer_and_put_the_bowl_inside(yellow_bowl)",
    "open_the_top_drawer_and_put_the_bowl_inside(yellow_cabinet)",
    "push_the_plate_to_the_front_of_the_stove(yellow_plate)",
    "push_the_plate_to_the_front_of_the_stove(yellow_stove)",
    "put_the_bowl_on_the_plate(yellow_bowl)",
    "put_the_bowl_on_the_plate(yellow_plate)",
    "put_the_bowl_on_the_stove(yellow_bowl)",
    "put_the_bowl_on_the_stove(yellow_stove)",
    "put_the_bowl_on_top_of_the_cabinet(yellow_bowl)",
    "put_the_bowl_on_top_of_the_cabinet(yellow_cabinet)",
    "put_the_cream_cheese_in_the_bowl(red_cream_cheese)",
    "put_the_cream_cheese_in_the_bowl(yellow_bowl)",
    "put_the_wine_bottle_on_the_rack(brown_rack)",
    "put_the_wine_bottle_on_the_rack(green_bottle)",
    "put_the_wine_bottle_on_top_of_the_cabinet(green_bottle)",
    "put_the_wine_bottle_on_top_of_the_cabinet(yellow_cabinet)",
    "turn_on_the_stove(yellow_stove)"
]

MODELS = [
    {"label": "original_simvla", "checkpoint": CKPT_VANILLA, "policy": "simvla_only"},
    {"label": "modified_simvla", "checkpoint": CKPT_MODIFIED, "policy": "simvla_only"},
    {"label": "modified_h10_risk_topk8", "checkpoint": CKPT_MODIFIED, "policy": "risk_topk8"}
]

# Seeds: 30 episodes (3 sets of 10 as requested: "ten episodes... three times")
SEEDS = list(range(30))

def generate():
    jobs = []
    config_dir = Path("configs/online")
    os.makedirs(config_dir, exist_ok=True)
    
    for task_id, task_name in enumerate(TASKS):
        for model in MODELS:
            label = model["label"]
            policy = model["policy"]
            
            job_id = f"task{task_id}_{label}"
            config_file = config_dir / f"{job_id}.json"
            
            cfg = {
                "ace_candidate_count": 8,
                "checkpoint": model["checkpoint"],
                "execution_horizon": 10,
                "expected_checkpoint_sha256": "", # Skipping hash check for speed
                "expected_topk8_dims": [6, 21, 25, 27, 23, 2, 26, 24],
                "experiment_id": job_id,
                "global_action_seed": 206080920,
                "history_steps": 16,
                "image_size": 384,
                "libero_pro_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO",
                "max_steps": 300,
                "model_denoise_steps": 10,
                "model_load_seed": 206080911,
                "norm_stats": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json",
                "output_dir": f"{BASE_DIR}/runs/online/task{task_id}/{label}",
                "reset_seeds": SEEDS,
                "resolution": 128,
                "risk_model_base_dir": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/base",
                "risk_model_unc_topk8_dir": RISK_MODEL_DIR,
                "selection_cooldown_steps": 0,
                "selection_main_threshold": "q95",
                "selection_max_modifications_per_episode": 0,
                "selection_min_high_risk_streak": 1,
                "selection_min_margin": 0.1,
                "selection_min_timestep": 0,
                "selection_require_candidate_below_q95": False,
                "selection_streak_threshold": "q95",
                "selection_strong_margin": 0.15,
                "simvla_root": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified",
                "smolvlm_path": SMOLVLM_CACHE,
                "suite": "libero_goal_object_ood",
                "task_id": task_id,
                "warmup": 10
            }
            
            with open(config_file, "w") as f:
                json.dump(cfg, f, indent=2)
            
            jobs.append({
                "config": str(config_file),
                "episodes": len(SEEDS),
                "label": label,
                "output_dir": cfg["output_dir"],
                "policy": policy,
                "shard": 0,
                "task_id": task_id
            })
            
    with open("configs/online_jobs.json", "w") as f:
        json.dump({"jobs": jobs}, f, indent=2)

if __name__ == "__main__":
    generate()
