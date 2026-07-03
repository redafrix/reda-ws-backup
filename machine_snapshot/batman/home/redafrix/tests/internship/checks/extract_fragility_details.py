import os
import json
from collections import defaultdict

c1_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608"
c2_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608"
c3_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608"

def load_episodes(jsonl_paths):
    episodes = {}
    for p in jsonl_paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r') as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    seed = r.get("reset_seed")
                    if seed is not None:
                        episodes[seed] = r
    return episodes

def load_step_scores(jsonl_paths):
    scores_by_seed = defaultdict(list)
    for p in jsonl_paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r') as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    seed = r.get("reset_seed")
                    if seed is not None:
                        scores_by_seed[seed].append(r)
    for s in scores_by_seed:
        scores_by_seed[s].sort(key=lambda x: x["query_index"])
    return scores_by_seed

# Task 3
t3_simvla_eps = load_episodes([
    f"{c1_root}/runs/online/task3/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task3/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
])
t3_c2_risk_eps = load_episodes([
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])
t3_c2_steps = load_step_scores([
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/step_scores_risk_topk8.jsonl",
    f"{c2_root}/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/step_scores_risk_topk8.jsonl"
])

# Task 6
t6_simvla_eps = load_episodes([
    f"{c1_root}/runs/online/task6/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl",
    f"{c1_root}/runs/online/task6/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl"
])
t6_c2_risk_eps = load_episodes([
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])
t6_c2_steps = load_step_scores([
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/step_scores_risk_topk8.jsonl",
    f"{c2_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/step_scores_risk_topk8.jsonl"
])

t6_c3_risk_eps = load_episodes([
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl",
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl"
])
t6_c3_steps = load_step_scores([
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/step_scores_risk_topk8.jsonl",
    f"{c3_root}/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/step_scores_risk_topk8.jsonl"
])

def analyze_fragility(base_eps, eval_eps, eval_steps, label):
    rescues = []
    regressions = []
    
    all_seeds = set(base_eps.keys()).intersection(set(eval_eps.keys()))
    for s in sorted(all_seeds):
        b = base_eps[s]["success"]
        e = eval_eps[s]["success"]
        
        steps = eval_steps.get(s, [])
        mods_info = []
        for q in steps:
            sel_idx = q.get("selected_candidate_index", 0)
            if sel_idx != 0:
                mods_info.append({
                    "query_index": q["query_index"],
                    "main_score": q["main_score"],
                    "selected_score": q["selected_score"],
                    "reason": q.get("selection_reason", "")
                })
        
        info = {
            "seed": s,
            "base_success": b,
            "base_steps": base_eps[s]["num_steps"],
            "risk_success": e,
            "risk_steps": eval_eps[s]["num_steps"],
            "modifications_count": eval_eps[s]["action_modifications_count"],
            "modifications": mods_info
        }
        
        if not b and e:
            rescues.append(info)
        elif b and not e:
            regressions.append(info)
            
    print(f"=== {label} ===")
    print(f"Rescues Count: {len(rescues)}")
    for r in rescues:
        mods_str = ", ".join([f"Q{m['query_index']}(M={m['main_score']:.3f}->S={m['selected_score']:.3f}, {m['reason']})" for m in r["modifications"]])
        print(f"  Rescue Seed {r['seed']}: Base={r['base_steps']} steps -> Risk={r['risk_steps']} steps. Mods={r['modifications_count']} [{mods_str}]")
        
    print(f"Regressions Count: {len(regressions)}")
    for r in regressions:
        mods_str = ", ".join([f"Q{m['query_index']}(M={m['main_score']:.3f}->S={m['selected_score']:.3f}, {m['reason']})" for m in r["modifications"]])
        print(f"  Regression Seed {r['seed']}: Base={r['base_steps']} steps -> Risk={r['risk_steps']} steps. Mods={r['modifications_count']} [{mods_str}]")
    print()

analyze_fragility(t3_simvla_eps, t3_c2_risk_eps, t3_c2_steps, "Task 3 (Aggressive TopK8 vs Baseline)")
analyze_fragility(t6_simvla_eps, t6_c2_risk_eps, t6_c2_steps, "Task 6 (Aggressive TopK8 vs Baseline)")
analyze_fragility(t6_simvla_eps, t6_c3_risk_eps, t6_c3_steps, "Task 6 (Old Detector Aggressive vs Baseline)")
