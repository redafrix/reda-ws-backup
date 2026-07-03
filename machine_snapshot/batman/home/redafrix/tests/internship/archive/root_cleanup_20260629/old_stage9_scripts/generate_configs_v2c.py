import json
from pathlib import Path

NEW_ROOT = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610")
TASKS = range(18)
MODELS = [
    {"label": "topk8_v2c_h5_adaptive_horizon", "checkpoint": "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610/checkpoints/ckpt-60000", "policy": "topk8_v2c_h5_adaptive_horizon"}
]

def run():
    NEW_ROOT.joinpath("configs").mkdir(parents=True, exist_ok=True)
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
                "libero_pro_root": "/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO",
                "max_steps": 300,
                "model_denoise_steps": 10,
                "model_load_seed": 206080911,
                "norm_stats": "/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json",
                "output_dir": str(NEW_ROOT / f"runs/task{task_id}/{label}"),
                "reset_seeds": list(range(10)),
                "resolution": 128,
                "simvla_root": "/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified",
                "smolvlm_path": "/tmp/ood_smolvlm_cache",
                "suite": "libero_goal_object_ood",
                "task_id": task_id,
                "warmup": 10
            }
            
            if model["policy"] == "topk8_v2c_h5_adaptive_horizon":
                cfg["risk_model_unc_topk8_dir"] = "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8"
                cfg["expected_topk8_dims"] = [6, 21, 25, 27, 23, 2, 26, 24]
                
            config_path.write_text(json.dumps(cfg, indent=2))
            print(f"Generated {config_path.name}")

if __name__ == "__main__":
    run()
