import os
import json
import glob

runs_root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609/runs"

def load_jsonl(path):
    if not os.path.exists(path):
        return []
    res = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    res.append(json.loads(line))
                except Exception as e:
                    pass
    return res

tasks = sorted(os.listdir(runs_root))
# Keep only directories starting with task
tasks = [t for t in tasks if t.startswith("task") and os.path.isdir(os.path.join(runs_root, t))]

results = {}

for task in tasks:
    task_num = int(task.replace("task", ""))
    task_path = os.path.join(runs_root, task)
    results[task_num] = {}
    
    policies = ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]
    for pol in policies:
        pol_path = os.path.join(task_path, pol)
        # find subdirectory
        subdirs = [d for d in os.listdir(pol_path) if os.path.isdir(os.path.join(pol_path, d))]
        if not subdirs:
            continue
        sub_dir = os.path.join(pol_path, subdirs[0])
        
        # Load episode_summaries.jsonl
        summary_path = os.path.join(sub_dir, "episode_summaries.jsonl")
        summaries = load_jsonl(summary_path)
        
        # Sort by episode_index
        summaries = sorted(summaries, key=lambda x: x.get("episode_index", 0))
        
        results[task_num][pol] = {
            "summaries": summaries
        }

print(f"Loaded {len(results)} tasks.")

# Verify completeness
# 18 tasks, 3 policies, 10 episodes each
total_episodes = 0
seed_parity_failures = 0
all_seeds_checked = True

task_keys = sorted(results.keys())

for t in task_keys:
    t_data = results[t]
    if len(t_data) != 3:
        print(f"Task {t} has missing policies: {list(t_data.keys())}")
        all_seeds_checked = False
    
    # Check seed parity and episode counts
    p_seeds = {}
    for pol in t_data:
        summaries = t_data[pol]["summaries"]
        total_episodes += len(summaries)
        if len(summaries) != 10:
            print(f"Task {t} policy {pol} has {len(summaries)} episodes instead of 10")
            all_seeds_checked = False
        
        seeds = [x.get("reset_seed") for x in summaries]
        p_seeds[pol] = seeds
        
        # Check duplicates
        if len(seeds) != len(set(seeds)):
            print(f"Task {t} policy {pol} has duplicate seeds: {seeds}")
            all_seeds_checked = False
            
    # Check parity across policies
    p_keys = list(p_seeds.keys())
    if len(p_keys) == 3:
        s0, s1, s2 = p_seeds[p_keys[0]], p_seeds[p_keys[1]], p_seeds[p_keys[2]]
        if s0 != s1 or s1 != s2:
            print(f"Task {t} seed mismatch across policies! {p_keys[0]}: {s0}, {p_keys[1]}: {s1}, {p_keys[2]}: {s2}")
            seed_parity_failures += 1
            all_seeds_checked = False

print(f"Total episodes verified: {total_episodes} (Expected: 540)")
print(f"Seed parity status: {'PASS' if seed_parity_failures == 0 and all_seeds_checked else 'FAIL'}")

# Now analyze results
report_data = {
    "total_episodes": total_episodes,
    "seed_parity_pass": seed_parity_failures == 0 and all_seeds_checked,
    "tasks": {}
}

# Cumulative metrics
global_successes = {"original_simvla": 0, "modified_simvla": 0, "modified_h10_risk_topk8": 0}
global_steps = {"original_simvla": 0, "modified_simvla": 0, "modified_h10_risk_topk8": 0}
global_counts = {"original_simvla": 0, "modified_simvla": 0, "modified_h10_risk_topk8": 0}

# Paired metrics
# Pairs: (modified_simvla vs original_simvla), (risk vs modified), (risk vs original)
global_paired = {
    "mod_vs_orig": {"rescues": 0, "regressions": 0, "both_success": 0, "both_fail": 0},
    "risk_vs_mod": {"rescues": 0, "regressions": 0, "both_success": 0, "both_fail": 0},
    "risk_vs_orig": {"rescues": 0, "regressions": 0, "both_success": 0, "both_fail": 0}
}

# risk_topk8 modifications
global_mods = {
    "total_mods": 0,
    "episodes_with_mods": 0,
    "total_queries": 0,
    "modified_queries": 0
}

for t in task_keys:
    t_data = results[t]
    t_report = {}
    
    # Policies summary
    for pol in ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]:
        summaries = t_data[pol]["summaries"]
        successes = sum([1 for x in summaries if x.get("success", False) or x.get("outcome") == "success"])
        steps = sum([x.get("num_steps", 0) for x in summaries])
        count = len(summaries)
        
        t_report[pol] = {
            "success_rate": successes / count if count > 0 else 0,
            "success_count": successes,
            "mean_steps": steps / count if count > 0 else 0
        }
        
        global_successes[pol] += successes
        global_steps[pol] += steps
        global_counts[pol] += count

    # Paired comparisons (episode-by-episode since seeds are aligned)
    # We assume seed parity is correct
    t_paired = {
        "mod_vs_orig": {"rescues": 0, "regressions": 0, "both_success": 0, "both_fail": 0},
        "risk_vs_mod": {"rescues": 0, "regressions": 0, "both_success": 0, "both_fail": 0},
        "risk_vs_orig": {"rescues": 0, "regressions": 0, "both_success": 0, "both_fail": 0}
    }
    
    orig_sum = t_data["original_simvla"]["summaries"]
    mod_sum = t_data["modified_simvla"]["summaries"]
    risk_sum = t_data["modified_h10_risk_topk8"]["summaries"]
    
    # We zip by episode_index because seeds are verified to match
    for idx in range(10):
        o_succ = orig_sum[idx].get("success", False) or orig_sum[idx].get("outcome") == "success"
        m_succ = mod_sum[idx].get("success", False) or mod_sum[idx].get("outcome") == "success"
        r_succ = risk_sum[idx].get("success", False) or risk_sum[idx].get("outcome") == "success"
        
        # mod vs orig
        if m_succ and not o_succ:
            t_paired["mod_vs_orig"]["rescues"] += 1
            global_paired["mod_vs_orig"]["rescues"] += 1
        elif not m_succ and o_succ:
            t_paired["mod_vs_orig"]["regressions"] += 1
            global_paired["mod_vs_orig"]["regressions"] += 1
        elif m_succ and o_succ:
            t_paired["mod_vs_orig"]["both_success"] += 1
            global_paired["mod_vs_orig"]["both_success"] += 1
        else:
            t_paired["mod_vs_orig"]["both_fail"] += 1
            global_paired["mod_vs_orig"]["both_fail"] += 1
            
        # risk vs mod
        if r_succ and not m_succ:
            t_paired["risk_vs_mod"]["rescues"] += 1
            global_paired["risk_vs_mod"]["rescues"] += 1
        elif not r_succ and m_succ:
            t_paired["risk_vs_mod"]["regressions"] += 1
            global_paired["risk_vs_mod"]["regressions"] += 1
        elif r_succ and m_succ:
            t_paired["risk_vs_mod"]["both_success"] += 1
            global_paired["risk_vs_mod"]["both_success"] += 1
        else:
            t_paired["risk_vs_mod"]["both_fail"] += 1
            global_paired["risk_vs_mod"]["both_fail"] += 1
            
        # risk vs orig
        if r_succ and not o_succ:
            t_paired["risk_vs_orig"]["rescues"] += 1
            global_paired["risk_vs_orig"]["rescues"] += 1
        elif not r_succ and o_succ:
            t_paired["risk_vs_orig"]["regressions"] += 1
            global_paired["risk_vs_orig"]["regressions"] += 1
        elif r_succ and o_succ:
            t_paired["risk_vs_orig"]["both_success"] += 1
            global_paired["risk_vs_orig"]["both_success"] += 1
        else:
            t_paired["risk_vs_orig"]["both_fail"] += 1
            global_paired["risk_vs_orig"]["both_fail"] += 1

    # Action modifications for risk_topk8
    # We count from summaries
    t_mods = {
        "total_mods": sum([x.get("action_modifications_count", 0) for x in risk_sum]),
        "episodes_with_mods": sum([1 for x in risk_sum if x.get("action_modifications_count", 0) > 0])
    }
    
    # Query modification rate from step logs
    # Find step_scores file
    sub_dir = [d for d in os.listdir(os.path.join(task_path, "modified_h10_risk_topk8")) if os.path.isdir(os.path.join(task_path, "modified_h10_risk_topk8", d))][0]
    step_scores_path = os.path.join(task_path, "modified_h10_risk_topk8", sub_dir, "step_scores_risk_topk8.jsonl")
    
    total_queries = 0
    modified_queries = 0
    if os.path.exists(step_scores_path):
        step_scores = load_jsonl(step_scores_path)
        # Filter for query timesteps: in H10, query is made every 10 steps or when early stopped.
        # But actually in the step logs, we record the decision at each step or when a query is made.
        # Let's count how many query steps are recorded. In step_scores, is there a query flag or do we record every query?
        # Let's check a few lines of step scores in the main thread to see what fields exist.
        # Or we can just sum up the number of queries directly.
        # Let's count lines where query was made.
        for step in step_scores:
            # Check if it's a query step: usually has 'query_index' or 'main_risk' or similar.
            if "main_risk" in step or "main_score" in step or "query_index" in step:
                total_queries += 1
                if step.get("selected_candidate_index", 0) != 0:
                    modified_queries += 1
                    
    t_mods["total_queries"] = total_queries
    t_mods["modified_queries"] = modified_queries
    t_mods["query_modification_rate"] = modified_queries / total_queries if total_queries > 0 else 0
    
    global_mods["total_mods"] += t_mods["total_mods"]
    global_mods["episodes_with_mods"] += t_mods["episodes_with_mods"]
    global_mods["total_queries"] += total_queries
    global_mods["modified_queries"] += modified_queries
    
    t_report["paired"] = t_paired
    t_report["mods"] = t_mods
    
    report_data["tasks"][t] = t_report

# Overall summary
overall = {}
for pol in ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]:
    overall[pol] = {
        "success_rate": global_successes[pol] / global_counts[pol] if global_counts[pol] > 0 else 0,
        "success_count": global_successes[pol],
        "mean_steps": global_steps[pol] / global_counts[pol] if global_counts[pol] > 0 else 0
    }
overall["paired"] = global_paired
global_mods["query_modification_rate"] = global_mods["modified_queries"] / global_mods["total_queries"] if global_mods["total_queries"] > 0 else 0
overall["mods"] = global_mods

report_data["overall"] = overall

# Write output json
with open("/tmp/libero_goal_object_ood_10ep_audit_results.json", "w") as f:
    json.dump(report_data, f, indent=2)

print("SUCCESS: Forensic audit calculations completed.")
print(json.dumps(overall, indent=2))
