import json

with open("checks/libero_goal_object_ood_step9_audit_results_thresh_0.5_20260610.json") as f:
    data_05 = json.load(f)

# Let us run the same logic directly from the data loaded via Python
# We already have all data in get_all_completed_stats_with_q95.py output
# Let's write the code to print the Markdown table
import subprocess

p = subprocess.run(["ssh", "pcrobot", "python3 -"], input="""
import os
import json

ROOT_03 = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609"
ROOT_05 = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610"
ROOT_Q95 = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610"

TASKS = [
    "open_the_middle_drawer_of_the_cabinet(yellow_cabinet)",
    "open_the_top_drawer_and_put_the_bowl_inside(yellow_bowl)",
    "open_the_top_drawer_and_put_the_bowl_inside(yellow_cabinet)",
    "push_the_plate_to_the_front_of_the_stove(yellow_plate)",
    "push_the_plate_to_the_front_of_the_stove(yellow_stove)",
    "put_the_bowl_on_the_plate(yellow_bowl)",
    "put_the_bowl_on_the_plate(yellow_plate)",
    "put_the_bowl_on_the_stove(yellow_bowl)",
    "put_the_bowl_on_the_stove(yellow_stove)",
    "put_the_bowl_on_top_of_the_cabinet(yellow_bowl)",
    "put_the_bowl_on_top_of_the_cabinet(yellow_cabinet)",
    "put_the_cream_cheese_in_the_bowl(red_cream_cheese)",
    "put_the_cream_cheese_in_the_bowl(yellow_bowl)",
    "put_the_wine_bottle_on_the_rack(brown_rack)",
    "put_the_wine_bottle_on_the_rack(green_bottle)",
    "put_the_wine_bottle_on_top_of_the_cabinet(green_bottle)",
    "put_the_wine_bottle_on_top_of_the_cabinet(yellow_cabinet)",
    "turn_on_the_stove(yellow_stove)"
]

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
                except Exception:
                    pass
    return res

def get_summaries_path(root_dir, task_id, policy):
    pol_path = os.path.join(root_dir, "runs", f"task{task_id}", policy)
    if not os.path.exists(pol_path):
        return None
    subdirs = [d for d in os.listdir(pol_path) if os.path.isdir(os.path.join(pol_path, d))]
    if not subdirs:
        return None
    sum_path = os.path.join(pol_path, subdirs[0], "episode_summaries.jsonl")
    return sum_path

stats = {}
for task_id in range(18):
    task_name = TASKS[task_id]
    
    p_orig = get_summaries_path(ROOT_03, task_id, "original_simvla")
    p_mod = get_summaries_path(ROOT_03, task_id, "modified_simvla")
    p_r3 = get_summaries_path(ROOT_03, task_id, "modified_h10_risk_topk8")
    p_r5 = get_summaries_path(ROOT_05, task_id, "modified_h10_risk_topk8")
    p_q95 = get_summaries_path(ROOT_Q95, task_id, "modified_h10_risk_topk8")
    
    sum_orig = load_jsonl(p_orig)
    sum_mod = load_jsonl(p_mod)
    sum_r3 = load_jsonl(p_r3)
    sum_r5 = load_jsonl(p_r5)
    sum_q95 = load_jsonl(p_q95)
    
    map_orig = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_orig}
    map_mod = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_mod}
    map_r3 = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_r3}
    map_r5 = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_r5}
    map_q95 = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_q95}
    
    sr_orig = sum(1 for ep in sum_orig if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_orig) if sum_orig else 0.0
    sr_mod = sum(1 for ep in sum_mod if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_mod) if sum_mod else 0.0
    sr_r3 = sum(1 for ep in sum_r3 if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_r3) if sum_r3 else 0.0
    sr_r5 = sum(1 for ep in sum_r5 if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_r5) if sum_r5 else 0.0
    sr_q95 = sum(1 for ep in sum_q95 if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_q95) if sum_q95 else 0.0
    
    rescues_3, regressions_3 = 0, 0
    rescues_5, regressions_5 = 0, 0
    rescues_q, regressions_q = 0, 0
    
    common_seeds = set(map_mod.keys()).intersection(map_r3.keys()).intersection(map_r5.keys()).intersection(map_q95.keys())
    for seed in common_seeds:
        m_ok = map_mod[seed]
        r3_ok = map_r3[seed]
        r5_ok = map_r5[seed]
        rq_ok = map_q95[seed]
        
        if r3_ok and not m_ok: rescues_3 += 1
        elif not r3_ok and m_ok: regressions_3 += 1
        
        if r5_ok and not m_ok: rescues_5 += 1
        elif not r5_ok and m_ok: regressions_5 += 1
        
        if rq_ok and not m_ok: rescues_q += 1
        elif not rq_ok and m_ok: regressions_q += 1
        
    stats[task_id] = {
        "name": task_name,
        "sr_orig": sr_orig, "sr_mod": sr_mod, "sr_r3": sr_r3, "sr_r5": sr_r5, "sr_q95": sr_q95,
        "p3": {"rescues": rescues_3, "regressions": regressions_3, "net_gain": rescues_3 - regressions_3},
        "p5": {"rescues": rescues_5, "regressions": regressions_5, "net_gain": rescues_5 - regressions_5},
        "pq95": {"rescues": rescues_q, "regressions": regressions_q, "net_gain": rescues_q - regressions_q}
    }

# 1. Generate Success Rate Markdown Table
print("### 1. Success Rate Comparison")
print("| Task ID | Task Name | Original SimVLA | Modified SimVLA (Baseline) | Risk TopK8 (Thresh 0.3) | Risk TopK8 (Thresh 0.5) | Risk TopK8 (Thresh q95) |")
print("| :---: | :--- | :---: | :---: | :---: | :---: | :---: |")
for tid in sorted(stats.keys()):
    s = stats[tid]
    print(f"| **{tid}** | {s['name']} | {s['sr_orig']*100:.1f}% | {s['sr_mod']*100:.1f}% | {s['sr_r3']*100:.1f}% | {s['sr_r5']*100:.1f}% | {s['sr_q95']*100:.1f}% |")

avg_orig = sum(stats[k]['sr_orig'] for k in stats)/18 * 100
avg_mod = sum(stats[k]['sr_mod'] for k in stats)/18 * 100
avg_r3 = sum(stats[k]['sr_r3'] for k in stats)/18 * 100
avg_r5 = sum(stats[k]['sr_r5'] for k in stats)/18 * 100
avg_q = sum(stats[k]['sr_q95'] for k in stats)/18 * 100
print(f"| **Avg** | **Overall Success Rate** | **{avg_orig:.2f}%** | **{avg_mod:.2f}%** | **{avg_r3:.2f}%** | **{avg_r5:.2f}%** | **{avg_q:.2f}%** |")
print()

# 2. Generate Paired Outcome Markdown Table
print("### 2. Paired Outcome Breakdown (Relative to Modified SimVLA Baseline)")
print("| Task ID | Task Name | Gating Threshold 0.3 | Gating Threshold 0.5 | Gating Threshold q95 (0.6155) |")
print("| :---: | :--- | :--- | :--- | :--- |")
for tid in sorted(stats.keys()):
    s = stats[tid]
    p3 = f"{s['p3']['rescues']} res, {s['p3']['regressions']} reg (Net: **{s['p3']['net_gain']:+d}**)"
    p5 = f"{s['p5']['rescues']} res, {s['p5']['regressions']} reg (Net: **{s['p5']['net_gain']:+d}**)"
    pq = f"{s['pq95']['rescues']} res, {s['pq95']['regressions']} reg (Net: **{s['pq95']['net_gain']:+d}**)"
    print(f"| **{tid}** | {s['name']} | {p3} | {p5} | {pq} |")

tot_res3 = sum(stats[k]['p3']['rescues'] for k in stats)
tot_reg3 = sum(stats[k]['p3']['regressions'] for k in stats)
tot_res5 = sum(stats[k]['p5']['rescues'] for k in stats)
tot_reg5 = sum(stats[k]['p5']['regressions'] for k in stats)
tot_resq = sum(stats[k]['pq95']['rescues'] for k in stats)
tot_regq = sum(stats[k]['pq95']['regressions'] for k in stats)
print(f"| **Total** | **All 18 Tasks Combined** | **{tot_res3} res, {tot_reg3} reg (Net: **{tot_res3-tot_reg3:+d}**)** | **{tot_res5} res, {tot_reg5} reg (Net: **{tot_res5-tot_reg5:+d}**)** | **{tot_resq} res, {tot_regq} reg (Net: **{tot_resq-tot_regq:+d}**)** |")
""", capture_output=True, text=True)

print(p.stdout)
