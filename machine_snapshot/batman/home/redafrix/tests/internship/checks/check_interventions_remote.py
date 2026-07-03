import os
import json

c1_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608"
c2_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608"

def load_mod_stats(jsonl_paths):
    total_episodes = 0
    episodes_with_mods = 0
    total_mods = 0
    for p in jsonl_paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r') as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    mods = r.get("action_modifications_count", 0)
                    total_episodes += 1
                    total_mods += mods
                    if mods > 0:
                        episodes_with_mods += 1
    return {
        "total_episodes": total_episodes,
        "episodes_with_mods": episodes_with_mods,
        "total_mods": total_mods,
        "mod_rate": episodes_with_mods / total_episodes if total_episodes else 0.0,
        "avg_mods": total_mods / total_episodes if total_episodes else 0.0
    }

# Task 3 Campaign 1 (conservative topk8)
t3_c1_risk = load_mod_stats([
    f"{c1_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])

# Task 3 Campaign 2 (aggressive topk8)
t3_c2_risk = load_mod_stats([
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])

# Task 6 Campaign 1 (conservative topk8)
t6_c1_risk = load_mod_stats([
    f"{c1_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])

# Task 6 Campaign 2 (aggressive topk8)
t6_c2_risk = load_mod_stats([
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])

print("Task 3 Campaign 1 (Conservative q95):", t3_c1_risk)
print("Task 3 Campaign 2 (Aggressive 0.3):", t3_c2_risk)
print("Task 6 Campaign 1 (Conservative q95):", t6_c1_risk)
print("Task 6 Campaign 2 (Aggressive 0.3):", t6_c2_risk)
