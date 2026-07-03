import json
from pathlib import Path
import numpy as np

root = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610")

tasks = range(18)
modified_success_total = 0
v2b_success_total = 0
total_episodes = 0

rescues = 0
regressions = 0
shared_success = 0
shared_failure = 0

modified_steps_list = []
v2b_steps_list = []

h1_total = 0
h10_total = 0
all_risk_scores = []

# Task-wise stats
task_stats = []

for task_id in tasks:
    mod_path = root / f"runs/task{task_id}/modified_simvla/simvla_only/episode_summaries.jsonl"
    v2b_path = root / f"runs/task{task_id}/topk8_v2b_adaptive_horizon/topk8_v2b_adaptive_horizon/episode_summaries.jsonl"
    v2b_steps_path = root / f"runs/task{task_id}/topk8_v2b_adaptive_horizon/topk8_v2b_adaptive_horizon/step_scores_topk8_v2.jsonl"
    
    # Load modified
    mod_episodes = []
    with open(mod_path) as f:
        for line in f:
            if line.strip():
                mod_episodes.append(json.loads(line))
    mod_episodes.sort(key=lambda x: x["episode_index"])
    
    # Load v2b
    v2b_episodes = []
    with open(v2b_path) as f:
        for line in f:
            if line.strip():
                v2b_episodes.append(json.loads(line))
    v2b_episodes.sort(key=lambda x: x["episode_index"])
    
    assert len(mod_episodes) == 10, f"Task {task_id} modified has {len(mod_episodes)} eps"
    assert len(v2b_episodes) == 10, f"Task {task_id} v2b has {len(v2b_episodes)} eps"
    
    mod_success_count = 0
    v2b_success_count = 0
    mod_steps = []
    v2b_steps = []
    
    task_rescues = 0
    task_regressions = 0
    task_shared_success = 0
    task_shared_failure = 0
    
    for i in range(10):
        m_ep = mod_episodes[i]
        v_ep = v2b_episodes[i]
        
        # Verify seed parity
        assert m_ep["reset_seed"] == v_ep["reset_seed"], f"Seed mismatch at Task {task_id} index {i}: {m_ep['reset_seed']} vs {v_ep['reset_seed']}"
        
        m_succ = m_ep["success"]
        v_succ = v_ep["success"]
        
        if m_succ:
            mod_success_count += 1
            modified_success_total += 1
        if v_succ:
            v2b_success_count += 1
            v2b_success_total += 1
            
        if not m_succ and v_succ:
            rescues += 1
            task_rescues += 1
        elif m_succ and not v_succ:
            regressions += 1
            task_regressions += 1
        elif m_succ and v_succ:
            shared_success += 1
            task_shared_success += 1
        else:
            shared_failure += 1
            task_shared_failure += 1
            
        mod_steps.append(m_ep["num_steps"])
        v2b_steps.append(v_ep["num_steps"])
        modified_steps_list.append(m_ep["num_steps"])
        v2b_steps_list.append(v_ep["num_steps"])
        total_episodes += 1
        
    # Load step-level horizons and risks for v2b
    task_h1 = 0
    task_h10 = 0
    task_risks = []
    if v2b_steps_path.exists():
        with open(v2b_steps_path) as f:
            for line in f:
                if line.strip():
                    step = json.loads(line)
                    horizon = step["chosen_execution_horizon"]
                    risk = step["main_risk"]
                    if horizon == 1:
                        task_h1 += 1
                        h1_total += 1
                    elif horizon == 10:
                        task_h10 += 1
                        h10_total += 1
                    task_risks.append(risk)
                    all_risk_scores.append(risk)
                    
    task_stats.append({
        "task_id": task_id,
        "mod_success": mod_success_count,
        "v2b_success": v2b_success_count,
        "mod_mean_steps": np.mean(mod_steps),
        "v2b_mean_steps": np.mean(v2b_steps),
        "rescues": task_rescues,
        "regressions": task_regressions,
        "shared_success": task_shared_success,
        "shared_failure": task_shared_failure,
        "h1": task_h1,
        "h10": task_h10,
        "risk_mean": np.mean(task_risks) if task_risks else 0.0,
        "risk_max": np.max(task_risks) if task_risks else 0.0,
    })

print("# Analysis Results")
print(f"Total episodes compared: {total_episodes}")
print(f"Modified Success Total: {modified_success_total}/180 ({modified_success_total/180:.2%})")
print(f"V2B Success Total: {v2b_success_total}/180 ({v2b_success_total/180:.2%})")
print(f"Rescues: {rescues}")
print(f"Regressions: {regressions}")
print(f"Net Gain: {rescues - regressions}")
print(f"Shared Success: {shared_success}")
print(f"Shared Failure: {shared_failure}")
print(f"Modified Mean Steps: {np.mean(modified_steps_list):.2f}")
print(f"V2B Mean Steps: {np.mean(v2b_steps_list):.2f}")
print(f"V2B Horizon 1 Total: {h1_total}")
print(f"V2B Horizon 10 Total: {h10_total}")
total_queries = h1_total + h10_total
print(f"V2B Total Queries: {total_queries}")
print(f"Percentage using H1: {h1_total/total_queries:.2%}" if total_queries else "0%")
print(f"V2B Risk Mean: {np.mean(all_risk_scores):.4f}" if all_risk_scores else "0")
print(f"V2B Risk Max: {np.max(all_risk_scores):.4f}" if all_risk_scores else "0")
print()
print("| Task | Mod Success | V2B Success | Mod Steps | V2B Steps | Rescues | Regressions | H1 | H10 | Risk Mean | Risk Max |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
for s in task_stats:
    print(f"| Task {s['task_id']:02d} | {s['mod_success']}/10 | {s['v2b_success']}/10 | {s['mod_mean_steps']:.1f} | {s['v2b_mean_steps']:.1f} | {s['rescues']} | {s['regressions']} | {s['h1']} | {s['h10']} | {s['risk_mean']:.4f} | {s['risk_max']:.4f} |")
