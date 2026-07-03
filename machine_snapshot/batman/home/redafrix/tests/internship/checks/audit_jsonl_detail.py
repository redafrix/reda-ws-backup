import json
import os
from collections import Counter, defaultdict

# Define remote paths
c1_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608"
c2_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608"
c3_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608"

files_to_audit = {
    "t3_simvla_s0": f"{c1_root}/runs/online/task3/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    "t3_simvla_s1": f"{c1_root}/runs/online/task3/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl",
    "t3_risk_s0": f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    "t3_risk_s1": f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl",
    "t6_simvla_s0": f"{c1_root}/runs/online/task6/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    "t6_simvla_s1": f"{c1_root}/runs/online/task6/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl",
    "t6_risk_s0": f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    "t6_risk_s1": f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl",
    "t6_old_s0": f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    "t6_old_s1": f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl",
}

def load_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows

def audit_file(name, path):
    rows = load_jsonl(path)
    if rows is None:
        return {"exists": False}
    
    row_count = len(rows)
    keys = list(rows[0].keys()) if row_count > 0 else []
    
    seeds = [r.get("reset_seed") for r in rows if r.get("reset_seed") is not None]
    seed_counts = Counter(seeds)
    unique_seeds = len(seed_counts)
    duplicate_seeds = {s: count for s, count in seed_counts.items() if count > 1}
    
    ep_indices = [r.get("episode_index") for r in rows if r.get("episode_index") is not None]
    ep_counts = Counter(ep_indices)
    unique_ep_indices = len(ep_counts)
    duplicate_ep_indices = {e: count for e, count in ep_counts.items() if count > 1}
    
    duplicate_seed_details = []
    for s, c in duplicate_seeds.items():
        occ = [i for i, r in enumerate(rows) if r.get("reset_seed") == s]
        duplicate_seed_details.append({
            "seed": s,
            "occurrences": occ,
            "successes": [rows[i].get("success") for i in occ],
            "num_steps": [rows[i].get("num_steps") for i in occ],
        })

    return {
        "exists": True,
        "row_count": row_count,
        "keys": keys,
        "unique_seeds": unique_seeds,
        "duplicate_seeds_count": len(duplicate_seeds),
        "duplicate_seeds": duplicate_seeds,
        "unique_ep_indices": unique_ep_indices,
        "duplicate_ep_indices_count": len(duplicate_ep_indices),
        "duplicate_ep_indices": duplicate_ep_indices,
        "duplicate_seed_details": duplicate_seed_details,
    }

# Run audit of all files
report = {}
for name, path in files_to_audit.items():
    report[name] = audit_file(name, path)

# Check shard overlap in reset_seeds
def check_shard_overlap(s0_name, s1_name):
    s0_info = report[s0_name]
    s1_info = report[s1_name]
    if not s0_info.get("exists") or not s1_info.get("exists"):
        return None
    
    s0_rows = load_jsonl(files_to_audit[s0_name])
    s1_rows = load_jsonl(files_to_audit[s1_name])
    
    s0_seeds = set(r.get("reset_seed") for r in s0_rows if r.get("reset_seed") is not None)
    s1_seeds = set(r.get("reset_seed") for r in s1_rows if r.get("reset_seed") is not None)
    
    overlap = s0_seeds.intersection(s1_seeds)
    return {
        "s0_seed_count": len(s0_seeds),
        "s1_seed_count": len(s1_seeds),
        "overlap_count": len(overlap),
        "overlap_seeds": list(overlap)
    }

overlaps = {
    "t3_simvla": check_shard_overlap("t3_simvla_s0", "t3_simvla_s1"),
    "t3_risk": check_shard_overlap("t3_risk_s0", "t3_risk_s1"),
    "t6_simvla": check_shard_overlap("t6_simvla_s0", "t6_simvla_s1"),
    "t6_risk": check_shard_overlap("t6_risk_s0", "t6_risk_s1"),
    "t6_old": check_shard_overlap("t6_old_s0", "t6_old_s1"),
}

print(json.dumps({"audit": report, "overlaps": overlaps}, indent=2))
