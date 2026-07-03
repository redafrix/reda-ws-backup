import os
import json

# Paths
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
    if os.path.exists(sum_path):
        return sum_path
    return None

def process_results():
    stats = {}
    
    total_q_q95 = 0
    mod_q_q95 = 0
    
    for task_id in range(18):
        task_name = TASKS[task_id]
        
        p_orig = get_summaries_path(ROOT_03, task_id, "original_simvla")
        p_mod = get_summaries_path(ROOT_03, task_id, "modified_simvla")
        p_r3 = get_summaries_path(ROOT_03, task_id, "modified_h10_risk_topk8")
        p_r5 = get_summaries_path(ROOT_05, task_id, "modified_h10_risk_topk8")
        p_q95 = get_summaries_path(ROOT_Q95, task_id, "modified_h10_risk_topk8")
        
        sum_orig = load_jsonl(p_orig) if p_orig else []
        sum_mod = load_jsonl(p_mod) if p_mod else []
        sum_r3 = load_jsonl(p_r3) if p_r3 else []
        sum_r5 = load_jsonl(p_r5) if p_r5 else []
        sum_q95 = load_jsonl(p_q95) if p_q95 else []
        
        # Success maps
        map_orig = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_orig}
        map_mod = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_mod}
        map_r3 = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_r3}
        map_r5 = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_r5}
        map_q95 = {ep.get("reset_seed"): (ep.get("success", False) or ep.get("outcome") == "success") for ep in sum_q95}
        
        # Compute rates
        sr_orig = sum(1 for ep in sum_orig if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_orig) if sum_orig else 0.0
        sr_mod = sum(1 for ep in sum_mod if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_mod) if sum_mod else 0.0
        sr_r3 = sum(1 for ep in sum_r3 if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_r3) if sum_r3 else 0.0
        sr_r5 = sum(1 for ep in sum_r5 if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_r5) if sum_r5 else 0.0
        sr_q95 = sum(1 for ep in sum_q95 if ep.get("success", False) or ep.get("outcome") == "success") / len(sum_q95) if sum_q95 else 0.0
        
        # Query metrics for q95
        if p_q95:
            scores_path = os.path.dirname(p_q95) + "/step_scores_risk_topk8.jsonl"
            if os.path.exists(scores_path):
                steps_scores = load_jsonl(scores_path)
                for step in steps_scores:
                    if "main_risk" in step or "main_score" in step or "query_index" in step:
                        total_q_q95 += 1
                        if step.get("selected_candidate_index", 0) != 0:
                            mod_q_q95 += 1
                            
        # Paired comparisons relative to modified_simvla
        rescues_3, regressions_3 = 0, 0
        rescues_5, regressions_5 = 0, 0
        rescues_q, regressions_q = 0, 0
        
        common_seeds_3 = set(map_mod.keys()).intersection(map_r3.keys())
        for seed in common_seeds_3:
            m_ok = map_mod[seed]
            r3_ok = map_r3[seed]
            if r3_ok and not m_ok:
                rescues_3 += 1
            elif not r3_ok and m_ok:
                regressions_3 += 1
                
        common_seeds_5 = set(map_mod.keys()).intersection(map_r5.keys())
        for seed in common_seeds_5:
            m_ok = map_mod[seed]
            r5_ok = map_r5[seed]
            if r5_ok and not m_ok:
                rescues_5 += 1
            elif not r5_ok and m_ok:
                regressions_5 += 1
                
        common_seeds_q = set(map_mod.keys()).intersection(map_q95.keys())
        for seed in common_seeds_q:
            m_ok = map_mod[seed]
            rq_ok = map_q95[seed]
            if rq_ok and not m_ok:
                rescues_q += 1
            elif not rq_ok and m_ok:
                regressions_q += 1
                
        stats[task_id] = {
            "name": task_name,
            "sr_orig": sr_orig,
            "sr_mod": sr_mod,
            "sr_r3": sr_r3,
            "sr_r5": sr_r5,
            "sr_q95": sr_q95,
            "p3": {"rescues": rescues_3, "regressions": regressions_3, "net_gain": rescues_3 - regressions_3},
            "p5": {"rescues": rescues_5, "regressions": regressions_5, "net_gain": rescues_5 - regressions_5},
            "pq95": {"rescues": rescues_q, "regressions": regressions_q, "net_gain": rescues_q - regressions_q}
        }
        
    return stats, {"total_queries": total_q_q95, "modified_queries": mod_q_q95, "modification_rate": mod_q_q95 / total_q_q95 if total_q_q95 > 0 else 0}

if __name__ == "__main__":
    stats, q95_metrics = process_results()
    output = {
        "task_stats": stats,
        "q95_query_stats": q95_metrics
    }
    print(json.dumps(output, indent=2))
