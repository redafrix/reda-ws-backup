import json
from pathlib import Path
import numpy as np

v2b_root = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610")
v2c_root = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610")

tasks = range(18)

modified_success_total = 0
v2b_success_total = 0
v2c_success_total = 0
total_episodes = 0

v2c_rescues_vs_modified = 0
v2c_regressions_vs_modified = 0
v2c_shared_success_vs_modified = 0
v2c_shared_failure_vs_modified = 0

modified_steps_list = []
v2b_steps_list = []
v2c_steps_list = []

v2c_h5_total = 0
v2c_h10_total = 0
v2c_all_risk_scores = []

# Task-wise stats
task_stats = []

for task_id in tasks:
    mod_path = v2b_root / f"runs/task{task_id}/modified_simvla/simvla_only/episode_summaries.jsonl"
    v2b_path = v2b_root / f"runs/task{task_id}/topk8_v2b_adaptive_horizon/topk8_v2b_adaptive_horizon/episode_summaries.jsonl"
    v2c_path = v2c_root / f"runs/task{task_id}/topk8_v2c_h5_adaptive_horizon/topk8_v2c_h5_adaptive_horizon/episode_summaries.jsonl"
    v2c_steps_path = v2c_root / f"runs/task{task_id}/topk8_v2c_h5_adaptive_horizon/topk8_v2c_h5_adaptive_horizon/step_scores_topk8_v2c.jsonl"
    
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
    
    # Load v2c
    v2c_episodes = []
    with open(v2c_path) as f:
        for line in f:
            if line.strip():
                v2c_episodes.append(json.loads(line))
    v2c_episodes.sort(key=lambda x: x["episode_index"])
    
    assert len(mod_episodes) == 10, f"Task {task_id} modified has {len(mod_episodes)} eps"
    assert len(v2b_episodes) == 10, f"Task {task_id} v2b has {len(v2b_episodes)} eps"
    assert len(v2c_episodes) == 10, f"Task {task_id} v2c has {len(v2c_episodes)} eps"
    
    mod_success_count = 0
    v2b_success_count = 0
    v2c_success_count = 0
    mod_steps = []
    v2b_steps = []
    v2c_steps = []
    
    task_rescues = 0
    task_regressions = 0
    task_shared_success = 0
    task_shared_failure = 0
    
    for i in range(10):
        m_ep = mod_episodes[i]
        v2b_ep = v2b_episodes[i]
        v2c_ep = v2c_episodes[i]
        
        # Verify seed parity
        assert m_ep["reset_seed"] == v2c_ep["reset_seed"], f"Seed mismatch at Task {task_id} index {i}: {m_ep['reset_seed']} vs {v2c_ep['reset_seed']}"
        assert v2b_ep["reset_seed"] == v2c_ep["reset_seed"], f"Seed mismatch at Task {task_id} index {i}: {v2b_ep['reset_seed']} vs {v2c_ep['reset_seed']}"
        
        m_succ = m_ep["success"]
        v2b_succ = v2b_ep["success"]
        v2c_succ = v2c_ep["success"]
        
        if m_succ:
            mod_success_count += 1
            modified_success_total += 1
        if v2b_succ:
            v2b_success_count += 1
            v2b_success_total += 1
        if v2c_succ:
            v2c_success_count += 1
            v2c_success_total += 1
            
        if not m_succ and v2c_succ:
            v2c_rescues_vs_modified += 1
            task_rescues += 1
        elif m_succ and not v2c_succ:
            v2c_regressions_vs_modified += 1
            task_regressions += 1
        elif m_succ and v2c_succ:
            v2c_shared_success_vs_modified += 1
            task_shared_success += 1
        else:
            v2c_shared_failure_vs_modified += 1
            task_shared_failure += 1
            
        mod_steps.append(m_ep["num_steps"])
        v2b_steps.append(v2b_ep["num_steps"])
        v2c_steps.append(v2c_ep["num_steps"])
        modified_steps_list.append(m_ep["num_steps"])
        v2b_steps_list.append(v2b_ep["num_steps"])
        v2c_steps_list.append(v2c_ep["num_steps"])
        total_episodes += 1
        
    # Load step-level horizons and risks for v2c
    task_h5 = 0
    task_h10 = 0
    task_risks = []
    if v2c_steps_path.exists():
        with open(v2c_steps_path) as f:
            for line in f:
                if line.strip():
                    step = json.loads(line)
                    horizon = step["chosen_execution_horizon"]
                    risk = step["main_risk"]
                    if horizon == 5:
                        task_h5 += 1
                        v2c_h5_total += 1
                    elif horizon == 10:
                        task_h10 += 1
                        v2c_h10_total += 1
                    task_risks.append(risk)
                    v2c_all_risk_scores.append(risk)
                    
    task_stats.append({
        "task_id": task_id,
        "mod_success": mod_success_count,
        "v2b_success": v2b_success_count,
        "v2c_success": v2c_success_count,
        "mod_mean_steps": np.mean(mod_steps),
        "v2b_mean_steps": np.mean(v2b_steps),
        "v2c_mean_steps": np.mean(v2c_steps),
        "rescues": task_rescues,
        "regressions": task_regressions,
        "shared_success": task_shared_success,
        "shared_failure": task_shared_failure,
        "h5": task_h5,
        "h10": task_h10,
        "risk_mean": np.mean(task_risks) if task_risks else 0.0,
        "risk_max": np.max(task_risks) if task_risks else 0.0,
    })

print("# Analysis Results")
print(f"Total episodes compared: {total_episodes}")
print(f"Modified Success Total: {modified_success_total}/180 ({modified_success_total/180:.2%})")
print(f"V2B H1 Success Total: {v2b_success_total}/180 ({v2b_success_total/180:.2%})")
print(f"V2C H5 Success Total: {v2c_success_total}/180 ({v2c_success_total/180:.2%})")
print(f"V2C Rescues vs Modified: {v2c_rescues_vs_modified}")
print(f"V2C Regressions vs Modified: {v2c_regressions_vs_modified}")
print(f"V2C Net Gain vs Modified: {v2c_rescues_vs_modified - v2c_regressions_vs_modified}")
print(f"Modified Mean Steps: {np.mean(modified_steps_list):.2f}")
print(f"V2B Mean Steps: {np.mean(v2b_steps_list):.2f}")
print(f"V2C Mean Steps: {np.mean(v2c_steps_list):.2f}")
print(f"V2C Horizon 5 Total: {v2c_h5_total}")
print(f"V2C Horizon 10 Total: {v2c_h10_total}")
v2c_total_queries = v2c_h5_total + v2c_h10_total
print(f"V2C Total Queries: {v2c_total_queries}")
print(f"Percentage using H5: {v2c_h5_total/v2c_total_queries:.2%}" if v2c_total_queries else "0%")
print(f"V2C Risk Mean: {np.mean(v2c_all_risk_scores):.4f}" if v2c_all_risk_scores else "0")
print(f"V2C Risk Max: {np.max(v2c_all_risk_scores):.4f}" if v2c_all_risk_scores else "0")
print()
print("| Task | Mod Success | V2B Success | V2C Success | Mod Steps | V2B Steps | V2C Steps | V2C Rescues | V2C Regress | H5 | H10 | Risk Mean | Risk Max |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for s in task_stats:
    print(f"| Task {s['task_id']:02d} | {s['mod_success']}/10 | {s['v2b_success']}/10 | {s['v2c_success']}/10 | {s['mod_mean_steps']:.1f} | {s['v2b_mean_steps']:.1f} | {s['v2c_mean_steps']:.1f} | {s['rescues']} | {s['regressions']} | {s['h5']} | {s['h10']} | {s['risk_mean']:.4f} | {s['risk_max']:.4f} |")
