import json
import os
import numpy as np
from collections import defaultdict

c1_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608"
c2_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608"

# Shards definitions
t3_simvla_paths = [
    f"{c1_root}/runs/online/task3/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task3/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
]
t3_risk_paths = [
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]
t3_step_paths = [
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/step_scores_risk_topk8.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/step_scores_risk_topk8.jsonl"
]

t6_simvla_paths = [
    f"{c1_root}/runs/online/task6/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task6/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
]
t6_risk_paths = [
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]
t6_step_paths = [
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/step_scores_risk_topk8.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/step_scores_risk_topk8.jsonl"
]

def load_jsonl(paths):
    rows = []
    for p in paths:
        if os.path.exists(p):
            with open(p, 'r') as f:
                for line in f:
                    if line.strip():
                        rows.append(json.loads(line))
    return rows

def group_episodes(base_summaries, risk_summaries):
    base_eps = {r["reset_seed"]: r for r in base_summaries if r.get("reset_seed") is not None}
    risk_eps = {r["reset_seed"]: r for r in risk_summaries if r.get("reset_seed") is not None}
    
    groups = {
        "rescues": [],
        "regressions": [],
        "shared_success": [],
        "shared_failure": []
    }
    
    for seed in sorted(base_eps.keys()):
        if seed in risk_eps:
            b_succ = base_eps[seed].get("success", False)
            r_succ = risk_eps[seed].get("success", False)
            if not b_succ and r_succ:
                groups["rescues"].append(seed)
            elif b_succ and not r_succ:
                groups["regressions"].append(seed)
            elif b_succ and r_succ:
                groups["shared_success"].append(seed)
            else:
                groups["shared_failure"].append(seed)
    return groups

def run_threshold_analysis(step_paths, groups, label):
    step_rows = load_jsonl(step_paths)
    steps_by_seed = defaultdict(list)
    for r in step_rows:
        seed = r.get("reset_seed")
        if seed is not None:
            steps_by_seed[seed].append(r)
            
    thresholds = [0.3, 0.4, 0.5, 0.6155]
    
    print(f"\n==================== {label} ====================")
    for T in thresholds:
        print(f"\n--- Threshold T = {T} ---")
        
        # 1. Count interventions that would be allowed (main_score >= T)
        allowed_interventions = 0
        total_queries = 0
        for r in step_rows:
            total_queries += 1
            if r["main_score"] >= T:
                allowed_interventions += 1
                
        print(f"  Allowed interventions: {allowed_interventions} / {total_queries} queries ({allowed_interventions/total_queries*100:.1f}%)")
        
        # 2. Rescue episodes analysis
        rescues_with_risk_above_T = []
        for seed in groups["rescues"]:
            eps_steps = steps_by_seed.get(seed, [])
            max_main = max([r["main_score"] for r in eps_steps]) if eps_steps else 0.0
            if max_main >= T:
                rescues_with_risk_above_T.append((seed, max_main))
        print(f"  Rescues with max main risk >= T: {len(rescues_with_risk_above_T)} / {len(groups['rescues'])}")
        
        # 3. Regression episodes analysis
        regressions_with_risk_above_T = []
        for seed in groups["regressions"]:
            eps_steps = steps_by_seed.get(seed, [])
            max_main = max([r["main_score"] for r in eps_steps]) if eps_steps else 0.0
            if max_main >= T:
                regressions_with_risk_above_T.append((seed, max_main))
        print(f"  Regressions with max main risk >= T: {len(regressions_with_risk_above_T)} / {len(groups['regressions'])}")
        
        # Estimated Net Gain
        # If T increases, some regressions are prevented (good!) but some rescues are lost (bad!).
        # A rescue is preserved only if max_main >= T.
        # A regression is prevented only if max_main < T (it reverts to baseline = success).
        # So:
        # Preserved Rescues = count of rescues with max_main >= T
        # Prevented Regressions = count of regressions with max_main < T
        # Regressions that still happen = count of regressions with max_main >= T
        # Estimated Net Gain = Preserved Rescues - Regressions that still happen
        preserved_rescues = len(rescues_with_risk_above_T)
        remaining_regressions = len(regressions_with_risk_above_T)
        prevented_regressions = len(groups['regressions']) - remaining_regressions
        est_net_gain = preserved_rescues - remaining_regressions
        
        print(f"  Estimated Preserved Rescues: {preserved_rescues}")
        print(f"  Estimated Prevented Regressions: {prevented_regressions}")
        print(f"  Estimated Remaining Regressions: {remaining_regressions}")
        print(f"  Estimated Net Gain: {est_net_gain}")

t3_base = load_jsonl(t3_simvla_paths)
t3_risk = load_jsonl(t3_risk_paths)
t6_base = load_jsonl(t6_simvla_paths)
t6_risk = load_jsonl(t6_risk_paths)

t3_groups = group_episodes(t3_base, t3_risk)
t6_groups = group_episodes(t6_base, t6_risk)

run_threshold_analysis(t3_step_paths, t3_groups, "Task 3 Threshold Analysis")
run_threshold_analysis(t6_step_paths, t6_groups, "Task 6 Threshold Analysis")
