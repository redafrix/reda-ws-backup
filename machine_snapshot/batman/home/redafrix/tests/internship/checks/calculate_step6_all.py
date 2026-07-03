import json
import os
import numpy as np
from collections import defaultdict, Counter

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

# 1. Exact Intervention Rates Recomputation
def recompute_rates(step_paths, summaries_paths, label):
    step_rows = load_jsonl(step_paths)
    sums = load_jsonl(summaries_paths)
    
    total_episodes = len(sums)
    total_queries = len(step_rows)
    total_actual_mods = sum(1 for r in step_rows if r.get("selected_candidate_index", 0) != 0)
    mods_per_ep = total_actual_mods / total_episodes if total_episodes else 0.0
    modified_query_rate = total_actual_mods / total_queries if total_queries else 0.0
    
    # Episodes with at least one mod
    mod_episodes_set = set(r["reset_seed"] for r in step_rows if r.get("selected_candidate_index", 0) != 0)
    eps_with_mods = len(mod_episodes_set)
    
    print(f"\n=== Rates for {label} ===")
    print(f"  Total episodes: {total_episodes}")
    print(f"  Total queries: {total_queries}")
    print(f"  Total actual modifications (interventions): {total_actual_mods}")
    print(f"  Modifications per episode: {mods_per_ep:.4f}")
    print(f"  Modified query rate: {modified_query_rate:.4f} ({modified_query_rate*100:.2f}%)")
    print(f"  Episodes with at least one modification: {eps_with_mods} / {total_episodes} ({eps_with_mods/total_episodes*100:.1f}%)")

# Loading data
t3_base = load_jsonl(t3_simvla_paths)
t3_risk = load_jsonl(t3_risk_paths)
t6_base = load_jsonl(t6_simvla_paths)
t6_risk = load_jsonl(t6_risk_paths)

t3_groups = group_episodes(t3_base, t3_risk)
t6_groups = group_episodes(t6_base, t6_risk)

recompute_rates(t3_step_paths, t3_risk_paths, "Task 3 Aggressive TopK8")
recompute_rates(t6_step_paths, t6_risk_paths, "Task 6 Aggressive TopK8")

# 2. Threshold Grid Search
def threshold_grid(step_paths, groups, label):
    step_rows = load_jsonl(step_paths)
    steps_by_seed = defaultdict(list)
    for r in step_rows:
        seed = r.get("reset_seed")
        if seed is not None:
            steps_by_seed[seed].append(r)
            
    thresholds = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.6155, 0.65, 0.7, 0.8, 0.9]
    
    print(f"\n==================== Threshold Grid: {label} ====================")
    print("| T | Allowed Interventions | Preserved Int % (Rescues) | Preserved Int % (Regressions) | Rescue Eps Touched | Regress Eps Fully Untouched | Rescue/Regress Sep Quality |")
    print("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    for T in thresholds:
        allowed_count = sum(1 for r in step_rows if r["main_score"] >= T and r.get("selected_candidate_index", 0) != 0)
        
        # Rescues
        rescue_int_total = sum(1 for s in groups["rescues"] for r in steps_by_seed[s] if r.get("selected_candidate_index", 0) != 0)
        rescue_int_allowed = sum(1 for s in groups["rescues"] for r in steps_by_seed[s] if r["main_score"] >= T and r.get("selected_candidate_index", 0) != 0)
        rescue_pct = rescue_int_allowed / rescue_int_total if rescue_int_total else 0.0
        
        # Regressions
        reg_int_total = sum(1 for s in groups["regressions"] for r in steps_by_seed[s] if r.get("selected_candidate_index", 0) != 0)
        reg_int_allowed = sum(1 for s in groups["regressions"] for r in steps_by_seed[s] if r["main_score"] >= T and r.get("selected_candidate_index", 0) != 0)
        reg_pct = reg_int_allowed / reg_int_total if reg_int_total else 0.0
        
        # Rescue episodes still touched (at least one allowed intervention)
        rescue_eps_touched = sum(1 for s in groups["rescues"] if any(r["main_score"] >= T and r.get("selected_candidate_index", 0) != 0 for r in steps_by_seed[s]))
        # Regression episodes fully untouched (0 allowed interventions)
        reg_eps_untouched = sum(1 for s in groups["regressions"] if not any(r["main_score"] >= T and r.get("selected_candidate_index", 0) != 0 for r in steps_by_seed[s]))
        
        # Separation Quality: Preserved Rescues - Remaining Regressions
        remaining_regressions = len(groups["regressions"]) - reg_eps_untouched
        sep_quality = rescue_eps_touched - remaining_regressions
        
        print(f"| {T:.4f} | {allowed_count} | {rescue_pct*100:.1f}% | {reg_pct*100:.1f}% | {rescue_eps_touched} / {len(groups['rescues'])} | {reg_eps_untouched} / {len(groups['regressions'])} | {sep_quality} |")

threshold_grid(t3_step_paths, t3_groups, "Task 3")
threshold_grid(t6_step_paths, t6_groups, "Task 6")

# 3. Test Smarter Gates (Task 6)
def evaluate_gates(step_paths, groups):
    step_rows = load_jsonl(step_paths)
    steps_by_seed = defaultdict(list)
    for r in step_rows:
        seed = r.get("reset_seed")
        if seed is not None:
            steps_by_seed[seed].append(r)
            
    # We only evaluate on actual modified queries (i.e. those with selected_candidate_index != 0 in the logs)
    # Let's define the gates:
    gates = {}
    
    # selected_risk <= cap
    for cap in [0.4, 0.5, 0.6, 0.7, 0.8]:
        gates[f"selected_risk <= {cap}"] = lambda r, c=cap: r["selected_score"] <= c
        
    # risk_reduction >= delta
    for delta in [0.02, 0.05, 0.08, 0.10, 0.15]:
        gates[f"risk_reduction >= {delta}"] = lambda r, d=delta: (r["main_score"] - r["selected_score"]) >= d
        
    # main_risk in bands
    gates["main_risk in 0.3-0.8"] = lambda r: 0.3 <= r["main_score"] <= 0.8
    gates["main_risk in 0.4-0.8"] = lambda r: 0.4 <= r["main_score"] <= 0.8
    gates["main_risk in 0.5-0.8"] = lambda r: 0.5 <= r["main_score"] <= 0.8
    gates["main_risk in 0.3-0.9"] = lambda r: 0.3 <= r["main_score"] <= 0.9
    gates["main_risk in 0.4-0.9"] = lambda r: 0.4 <= r["main_score"] <= 0.9
    gates["main_risk < 0.95"] = lambda r: r["main_score"] < 0.95
    
    # delayed intervention
    for d in [1, 2, 3]:
        gates[f"query_index >= {d}"] = lambda r, delay=d: r["query_index"] >= delay
        
    # max interventions per episode
    # Since max interventions is stateful per episode, we need custom check.
    
    # Compound gates
    # selected_risk < main_risk AND selected_risk <= cap AND risk_reduction >= delta
    for cap in [0.6, 0.7]:
        for delta in [0.05, 0.08]:
            gates[f"risk_lower AND sel <= {cap} AND red >= {delta}"] = (
                lambda r, c=cap, d=delta: r["selected_score"] < r["main_score"] and r["selected_score"] <= c and (r["main_score"] - r["selected_score"]) >= d
            )
            
    print("\n==================== Smarter Gates Evaluation (Task 6) ====================")
    print("| Gate | Rescue Queries Preserved | Regress Queries Blocked | Rescue Eps Touched | Regress Eps Untouched | Shared-Succ Preserved/Blocked | Shared-Fail Preserved/Blocked |")
    print("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    for gname, fn in gates.items():
        # Evaluate query counts
        # Rescue queries
        res_total = 0
        res_pres = 0
        for s in groups["rescues"]:
            for r in steps_by_seed[s]:
                if r.get("selected_candidate_index", 0) != 0:
                    res_total += 1
                    if fn(r):
                        res_pres += 1
                        
        # Regress queries
        reg_total = 0
        reg_blocked = 0
        for s in groups["regressions"]:
            for r in steps_by_seed[s]:
                if r.get("selected_candidate_index", 0) != 0:
                    reg_total += 1
                    if not fn(r):
                        reg_blocked += 1
                        
        # Episode counts
        rescue_touched = sum(1 for s in groups["rescues"] if any(r.get("selected_candidate_index", 0) != 0 and fn(r) for r in steps_by_seed[s]))
        regress_untouched = sum(1 for s in groups["regressions"] if not any(r.get("selected_candidate_index", 0) != 0 and fn(r) for r in steps_by_seed[s]))
        
        # Shared success queries
        ss_pres = 0
        ss_blocked = 0
        for s in groups["shared_success"]:
            for r in steps_by_seed[s]:
                if r.get("selected_candidate_index", 0) != 0:
                    if fn(r): ss_pres += 1
                    else: ss_blocked += 1
                    
        # Shared failure queries
        sf_pres = 0
        sf_blocked = 0
        for s in groups["shared_failure"]:
            for r in steps_by_seed[s]:
                if r.get("selected_candidate_index", 0) != 0:
                    if fn(r): sf_pres += 1
                    else: sf_blocked += 1
                    
        print(f"| {gname} | {res_pres} / {res_total} ({res_pres/res_total*100:.1f}%) | {reg_blocked} / {reg_total} ({reg_blocked/reg_total*100:.1f}%) | {rescue_touched} / {len(groups['rescues'])} | {regress_untouched} / {len(groups['regressions'])} | {ss_pres} / {ss_blocked} | {sf_pres} / {sf_blocked} |")

    # Evaluate Max Interventions (Stateful Gate)
    for max_mods in [1, 2, 3, 5]:
        gname = f"first {max_mods} mods only"
        
        # Helper to simulate stateful masking
        def get_stateful_mask(seed):
            mask = []
            count = 0
            # Sort steps by query_index
            sorted_steps = sorted(steps_by_seed[seed], key=lambda x: x["query_index"])
            for r in sorted_steps:
                if r.get("selected_candidate_index", 0) != 0:
                    count += 1
                    mask.append(count <= max_mods)
            return mask
            
        res_total = 0
        res_pres = 0
        rescue_touched = 0
        for s in groups["rescues"]:
            mask = get_stateful_mask(s)
            res_total += len(mask)
            res_pres += sum(1 for m in mask if m)
            if any(mask):
                rescue_touched += 1
                
        reg_total = 0
        reg_blocked = 0
        regress_untouched = 0
        for s in groups["regressions"]:
            mask = get_stateful_mask(s)
            reg_total += len(mask)
            reg_blocked += sum(1 for m in mask if not m)
            # Regress episode is fully untouched if NO mods are allowed (which means mask is empty or all False)
            if not any(mask):
                regress_untouched += 1
                
        # Shared success and failure
        ss_pres = 0
        ss_blocked = 0
        for s in groups["shared_success"]:
            mask = get_stateful_mask(s)
            ss_pres += sum(1 for m in mask if m)
            ss_blocked += sum(1 for m in mask if not m)
            
        sf_pres = 0
        sf_blocked = 0
        for s in groups["shared_failure"]:
            mask = get_stateful_mask(s)
            sf_pres += sum(1 for m in mask if m)
            sf_blocked += sum(1 for m in mask if not m)
            
        print(f"| {gname} | {res_pres} / {res_total} ({res_pres/res_total*100:.1f}%) | {reg_blocked} / {reg_total} ({reg_blocked/reg_total*100:.1f}%) | {rescue_touched} / {len(groups['rescues'])} | {regress_untouched} / {len(groups['regressions'])} | {ss_pres} / {ss_blocked} | {sf_pres} / {sf_blocked} |")

evaluate_gates(t6_step_paths, t6_groups)

# 4. Critical Intervention Timing (Task 6 Rescues vs Regressions)
def timing_analysis(step_paths, groups):
    step_rows = load_jsonl(step_paths)
    steps_by_seed = defaultdict(list)
    for r in step_rows:
        seed = r.get("reset_seed")
        if seed is not None:
            steps_by_seed[seed].append(r)
            
    print("\n==================== Critical Intervention Timing (Task 6) ====================")
    
    def analyze_episodes(seeds, label):
        print(f"\n--- {label} ---")
        for s in seeds:
            eps_steps = sorted(steps_by_seed[s], key=lambda x: x["query_index"])
            mods = [r for r in eps_steps if r.get("selected_candidate_index", 0) != 0]
            if not mods:
                continue
            first = mods[0]
            main_r = first["main_score"]
            sel_r = first["selected_score"]
            red = main_r - sel_r
            q_idx = first["query_index"]
            total_mods = len(mods)
            
            # Checks
            cond_T3 = main_r >= 0.3
            cond_sel7 = sel_r <= 0.7
            cond_sel6 = sel_r <= 0.6
            cond_red05 = red >= 0.05
            cond_q2 = q_idx >= 2
            
            print(f"  Seed {s}: FirstMod Q{q_idx} | main_r={main_r:.4f}, sel_r={sel_r:.4f}, red={red:.4f} | TotalMods={total_mods} | Allowed: T=0.3:{cond_T3}, sel<=0.7:{cond_sel7}, sel<=0.6:{cond_sel6}, red>=0.05:{cond_red05}, q>=2:{cond_q2}")

    analyze_episodes(groups["rescues"], "Rescues")
    analyze_episodes(groups["regressions"], "Regressions")

timing_analysis(t6_step_paths, t6_groups)

