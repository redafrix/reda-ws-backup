import json
import os
from collections import defaultdict

c1_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608"
c2_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608"
c3_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608"

# Shard paths
t3_simvla_paths = [
    f"{c1_root}/runs/online/task3/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task3/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
]
t3_risk_paths = [
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]

t6_simvla_paths = [
    f"{c1_root}/runs/online/task6/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task6/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
]
t6_risk_paths = [
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]

t6_old_paths = [
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
]

def load_episodes(paths):
    episodes = {}
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r') as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    seed = r.get("reset_seed")
                    if seed is not None:
                        if seed in episodes:
                            print(f"WARNING: Duplicate seed {seed} in {p}")
                        episodes[seed] = r
    return episodes

def compare(base_paths, risk_paths, label):
    base_eps = load_episodes(base_paths)
    risk_eps = load_episodes(risk_paths)
    
    base_seeds = set(base_eps.keys())
    risk_seeds = set(risk_eps.keys())
    
    shared_seeds = base_seeds.intersection(risk_seeds)
    base_only = base_seeds - risk_seeds
    risk_only = risk_seeds - base_seeds
    
    shared_success = 0
    shared_failure = 0
    rescues = []
    regressions = []
    
    base_success_count = 0
    risk_success_count = 0
    
    for s in sorted(shared_seeds):
        b_succ = base_eps[s].get("success", False)
        r_succ = risk_eps[s].get("success", False)
        
        b_steps = base_eps[s].get("num_steps", 0)
        r_steps = risk_eps[s].get("num_steps", 0)
        r_mods = risk_eps[s].get("action_modifications_count", 0)
        
        # We need to check if there are step scores / modification chunks info
        # But for the lists we can just construct a simple representation
        info = {
            "reset_seed": s,
            "base_success": b_succ,
            "risk_success": r_succ,
            "base_steps": b_steps,
            "risk_steps": r_steps,
            "risk_num_modifications": r_mods,
        }
        
        if b_succ:
            base_success_count += 1
        if r_succ:
            risk_success_count += 1
            
        if b_succ and r_succ:
            shared_success += 1
        elif not b_succ and not r_succ:
            shared_failure += 1
        elif not b_succ and r_succ:
            rescues.append(info)
        elif b_succ and not r_succ:
            regressions.append(info)
            
    print(f"=== Comparison: {label} ===")
    print(f"  Shared keys count: {len(shared_seeds)}")
    print(f"  Baseline-only keys count: {len(base_only)}")
    print(f"  Risk-only keys count: {len(risk_only)}")
    print(f"  Shared success count: {shared_success}")
    print(f"  Shared failure count: {shared_failure}")
    print(f"  Rescues count: {len(rescues)}")
    print(f"  Regressions count: {len(regressions)}")
    print(f"  Net gain: {len(rescues) - len(regressions)}")
    print(f"  Final baseline success count: {base_success_count}")
    print(f"  Final risk success count: {risk_success_count}")
    
    # Check intersection of rescue and regression seed sets
    rescue_seeds = set(r["reset_seed"] for r in rescues)
    regression_seeds = set(r["reset_seed"] for r in regressions)
    intersection = rescue_seeds.intersection(regression_seeds)
    print(f"  Rescue intersect Regression empty: {len(intersection) == 0}")
    if len(intersection) > 0:
        print(f"  WARNING: Intersection is not empty! Seeds: {intersection}")
        
    print("  Rescues list:")
    for r in rescues:
        print(f"    Seed {r['reset_seed']}: Base={r['base_steps']} steps (Success={r['base_success']}) -> Risk={r['risk_steps']} steps (Success={r['risk_success']}), Mods={r['risk_num_modifications']}")
    print("  Regressions list:")
    for r in regressions:
        print(f"    Seed {r['reset_seed']}: Base={r['base_steps']} steps (Success={r['base_success']}) -> Risk={r['risk_steps']} steps (Success={r['risk_success']}), Mods={r['risk_num_modifications']}")
    print()

compare(t3_simvla_paths, t3_risk_paths, "Task 3 Aggressive new TopK8 vs Baseline")
compare(t6_simvla_paths, t6_risk_paths, "Task 6 Aggressive new TopK8 vs Baseline")
compare(t6_simvla_paths, t6_old_paths, "Task 6 Aggressive old detector vs Baseline")
