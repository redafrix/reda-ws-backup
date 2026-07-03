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

def analyze_task_step_scores(step_paths, groups, label):
    step_rows = load_jsonl(step_paths)
    
    # Group step scores by seed
    steps_by_seed = defaultdict(list)
    for r in step_rows:
        seed = r.get("reset_seed")
        if seed is not None:
            steps_by_seed[seed].append(r)
            
    print(f"\n==================== {label} ====================")
    for gname, seeds in groups.items():
        print(f"\n--- Group: {gname} (Count: {len(seeds)}) ---")
        if not seeds:
            print("  No episodes in this group.")
            continue
            
        group_main_scores = []
        group_selected_scores = []
        group_reductions = []
        episode_max_main_scores = []
        
        intervention_counts = []
        first_intervention_indices = []
        selected_ranks = []
        
        selected_lower_count = 0
        total_intervention_count = 0
        
        for seed in seeds:
            eps_steps = steps_by_seed.get(seed, [])
            if not eps_steps:
                continue
            
            # Sort by query_index
            eps_steps = sorted(eps_steps, key=lambda x: x["query_index"])
            
            main_scores = [r["main_score"] for r in eps_steps]
            selected_scores = [r["selected_score"] for r in eps_steps]
            
            episode_max_main_scores.append(max(main_scores) if main_scores else 0)
            
            # Interventions in this episode
            interventions = [r for r in eps_steps if r.get("selected_candidate_index", 0) != 0]
            intervention_counts.append(len(interventions))
            
            if interventions:
                first_intervention_indices.append(interventions[0]["query_index"])
                for r in interventions:
                    group_reductions.append(r["main_score"] - r["selected_score"])
                    
                    # Compute rank of selected candidate score among candidate_scores[1:] (the 8 candidates)
                    cand_scores = r["candidate_scores"][1:]
                    sorted_cands = sorted(cand_scores)
                    rank = sorted_cands.index(r["selected_score"]) + 1 # 1-indexed (1 = lowest risk)
                    selected_ranks.append(rank)
                    
                    total_intervention_count += 1
                    if r["selected_score"] < r["main_score"]:
                        selected_lower_count += 1
                        
            group_main_scores.extend(main_scores)
            group_selected_scores.extend(selected_scores)
            
        mean_main = np.mean(group_main_scores) if group_main_scores else 0.0
        max_main = np.mean(episode_max_main_scores) if episode_max_main_scores else 0.0
        mean_selected = np.mean(group_selected_scores) if group_selected_scores else 0.0
        mean_reduction_all = np.mean([m - s for m, s in zip(group_main_scores, group_selected_scores)]) if group_main_scores else 0.0
        mean_reduction_interventions = np.mean(group_reductions) if group_reductions else 0.0
        
        total_interventions = sum(intervention_counts)
        mean_interventions = np.mean(intervention_counts) if intervention_counts else 0.0
        mean_first_int = np.mean(first_intervention_indices) if first_intervention_indices else 0.0
        mean_rank = np.mean(selected_ranks) if selected_ranks else 0.0
        pct_lower = (selected_lower_count / total_intervention_count * 100) if total_intervention_count > 0 else 0.0
        
        print(f"  Mean main risk score: {mean_main:.4f}")
        print(f"  Mean max main risk score per episode: {max_main:.4f}")
        print(f"  Mean selected risk score: {mean_selected:.4f}")
        print(f"  Mean risk reduction (all steps): {mean_reduction_all:.4f}")
        print(f"  Mean risk reduction (only intervened steps): {mean_reduction_interventions:.4f}")
        print(f"  Total interventions: {total_interventions}")
        print(f"  Interventions per episode: {mean_interventions:.2f}")
        print(f"  Mean first intervention query index: {mean_first_int:.2f}")
        print(f"  Mean selected candidate rank (1-8, 1=best): {mean_rank:.2f}")
        print(f"  % of interventions where selected risk < main risk: {pct_lower:.1f}%")

print("Loading summaries...")
t3_base = load_jsonl(t3_simvla_paths)
t3_risk = load_jsonl(t3_risk_paths)
t6_base = load_jsonl(t6_simvla_paths)
t6_risk = load_jsonl(t6_risk_paths)

print("Grouping episodes...")
t3_groups = group_episodes(t3_base, t3_risk)
t6_groups = group_episodes(t6_base, t6_risk)

analyze_task_step_scores(t3_step_paths, t3_groups, "Task 3 Aggressive TopK8 Analysis")
analyze_task_step_scores(t6_step_paths, t6_groups, "Task 6 Aggressive TopK8 Analysis")
