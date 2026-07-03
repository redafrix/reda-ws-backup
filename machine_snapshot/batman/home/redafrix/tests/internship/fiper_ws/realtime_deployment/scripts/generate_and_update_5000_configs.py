import json
import numpy as np
import hashlib
from pathlib import Path

# Setup directories
seeds_dir = Path("fiper_ws/realtime_deployment/configs/seed_plans")
seeds_dir.mkdir(parents=True, exist_ok=True)
configs_dir = Path("fiper_ws/realtime_deployment/configs")
configs_dir.mkdir(parents=True, exist_ok=True)

workers_info = {
    "worker_sam_0": {"base_seed": 202605290, "name": "worker_sam_0_seeds_5000.json"},
    "worker_sam_1": {"base_seed": 202605291, "name": "worker_sam_1_seeds_5000.json"},
    "worker_bob_0": {"base_seed": 202605292, "name": "worker_bob_0_seeds_5000.json"},
    "worker_bob_1": {"base_seed": 202605293, "name": "worker_bob_1_seeds_5000.json"}
}

# Generate 5000 seeds per worker
seeds_dict = {}
for worker_id, info in workers_info.items():
    rng = np.random.default_rng(info["base_seed"])
    seeds = []
    seen = set()
    while len(seeds) < 5000:
        val = int(rng.integers(1, 2**31 - 1))
        if val not in seen:
            seeds.append(val)
            seen.add(val)
    
    # Save seed plan file
    plan_path = seeds_dir / info["name"]
    plan_path.write_text(json.dumps(seeds, indent=2) + "\n")
    seeds_dict[worker_id] = seeds
    print(f"Generated {len(seeds)} seeds for {worker_id} at {plan_path}. SHA256: {hashlib.sha256(plan_path.read_bytes()).hexdigest()}")

# Check overlaps
all_seeds_flat = []
for k, v in seeds_dict.items():
    all_seeds_flat.extend(v)
assert len(all_seeds_flat) == len(set(all_seeds_flat)), "Duplicate seeds found across workers!"
print("Overlap check passed: All 20,000 seeds are unique across workers.")

# Policy parameters
policy_fields = {
    "mode": "riskaware_simvla_full_v2_strict",
    "num_episodes_target": 5000,
    "max_steps": 300,
    "execute_policy": "receding_horizon_execute_first_action_only",
    "risk_model_name": "v2_018_transformer_k16",
    "global_action_seed": 424242,
    "enforce_unique_action_seeds_per_timestep": True,
    "ace_candidate_count": 8,
    "ace_sampling": "standard_every_timestep",
    "action_selection_policy": "risk_filtered_lowest_score_candidate_v2_strict_margin",
    "modify_actions": True,
    "action_mod_min_improvement": 0.10,
    "action_mod_q99_min_improvement": 0.15,
    "action_mod_require_main_above": "q95",
    "action_mod_prefer_candidate_below": "q95",
    "save_full_rows": False,
    "save_video": False,
    "save_lightweight_step_scores": True
}

# 1. Sam seen task 7 config
sam_seen_config = {
    "suite": "libero_10_with_milk",
    "task_id": 7,
    "risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16",
    "fallback_risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16",
    "output_dir": "realtime_deployment/runs/riskaware_4worker_20260529/sam_w0_seen_task7",
    "seeds": seeds_dict["worker_sam_0"],
    **policy_fields
}

# 2. Sam OOD task 8 config
sam_ood_config = {
    "suite": "libero_10_with_milk",
    "task_id": 8,
    "risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16",
    "fallback_risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16",
    "output_dir": "realtime_deployment/runs/riskaware_4worker_20260529/sam_w1_ood_task8",
    "seeds": seeds_dict["worker_sam_1"],
    **policy_fields
}

# 3. Bob fold_00 seen task 2 config
bob_seen_config = {
    "suite": "libero_object_with_mug",
    "task_id": 2,
    "risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16",
    "fallback_risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16",
    "output_dir": "realtime_deployment/runs/riskaware_4worker_20260529/bob_w0_fold00_seen_butter_t2",
    "seeds": seeds_dict["worker_bob_0"],
    **policy_fields
}

# 4. Bob fold_00 unseen task 0 config
bob_unseen_config = {
    "suite": "libero_object_with_mug",
    "task_id": 0,
    "risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16",
    "fallback_risk_model_job_dir": "experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16",
    "output_dir": "realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0",
    "seeds": seeds_dict["worker_bob_1"],
    **policy_fields
}

configs = {
    "riskaware_actionmod_v2_strict_sam_seen_task7_20260529.json": sam_seen_config,
    "riskaware_actionmod_v2_strict_sam_ood_task8_20260529.json": sam_ood_config,
    "riskaware_actionmod_v2_strict_bob_fold00_seen_butter_task2_20260529.json": bob_seen_config,
    "riskaware_actionmod_v2_strict_bob_fold00_unseen_alphabet_soup_task0_20260529.json": bob_unseen_config
}

for name, cfg in configs.items():
    p = configs_dir / name
    p.write_text(json.dumps(cfg, indent=2) + "\n")
    print(f"Updated config {p}. SHA256: {hashlib.sha256(p.read_bytes()).hexdigest()}")
