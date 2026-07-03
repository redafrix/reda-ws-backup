import os
import json

c1_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608"
c2_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608"
c3_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608"

def load_seed_to_success(jsonl_paths):
    seed_map = {}
    for p in jsonl_paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r') as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    seed = r.get("reset_seed")
                    success = r.get("success", False)
                    if seed is not None:
                        seed_map[seed] = success
    return seed_map

# Find Campaign 1 Task 3 modified_simvla paths
t3_c1_simvla_paths = [
    f"{c1_root}/runs/online/task3/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task3/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
]
# Campaign 2 Task 3 modified_h10_risk_topk8 paths
t3_c2_risk_paths = [
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]

# Find Campaign 1 Task 6 modified_simvla paths
t6_c1_simvla_paths = [
    f"{c1_root}/runs/online/task6/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task6/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
]
# Campaign 2 Task 6 modified_h10_risk_topk8 paths
t6_c2_risk_paths = [
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]
# Campaign 3 Task 6 modified_h10_risk_topk8 paths
t6_c3_risk_paths = [
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]

# Task 3
t3_simvla = load_seed_to_success(t3_c1_simvla_paths)
t3_c2_risk = load_seed_to_success(t3_c2_risk_paths)

# Task 6
t6_simvla = load_seed_to_success(t6_c1_simvla_paths)
t6_c2_risk = load_seed_to_success(t6_c2_risk_paths)
t6_c3_risk = load_seed_to_success(t6_c3_risk_paths)

def compute_metrics(base_map, eval_map, label):
    rescues = 0
    regressions = 0
    both_success = 0
    both_failure = 0
    
    all_seeds = set(base_map.keys()).intersection(set(eval_map.keys()))
    for s in all_seeds:
        b = base_map[s]
        e = eval_map[s]
        if not b and e:
            rescues += 1
        elif b and not e:
            regressions += 1
        elif b and e:
            both_success += 1
        else:
            both_failure += 1
            
    print(f"--- Paired Analysis for {label} (total overlapping seeds: {len(all_seeds)}) ---")
    print(f"  Rescues (Base=Fail, Risk=Success): {rescues}")
    print(f"  Regressions (Base=Success, Risk=Fail): {regressions}")
    print(f"  Both Success: {both_success}")
    print(f"  Both Failure: {both_failure}")
    print(f"  Net change: {rescues - regressions}")

compute_metrics(t3_simvla, t3_c2_risk, "Task 3 (C1 modified_simvla vs C2 modified_h10_risk_topk8)")
compute_metrics(t6_simvla, t6_c2_risk, "Task 6 (C1 modified_simvla vs C2 modified_h10_risk_topk8)")
compute_metrics(t6_simvla, t6_c3_risk, "Task 6 (C1 modified_simvla vs C3 modified_h10_risk_topk8 - Old Detector)")
