import json
from pathlib import Path
import numpy as np

v2b_root = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610")
v2c_root = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610")
v2d_root = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2d_commit_gate_20260610")

tasks = range(18)

modified_success_total = 0
v2b_success_total = 0
v2c_success_total = 0
v2d_success_total = 0

modified_steps_list = []
v2b_steps_list = []
v2c_steps_list = []
v2d_steps_list = []

# V2D metrics
v2d_rescues_vs_modified = 0
v2d_regressions_vs_modified = 0
v2d_shared_success_vs_modified = 0
v2d_shared_failure_vs_modified = 0

total_v2d_commits = 0
total_v2d_replans = 0
total_v2d_tails_committed = 0
total_v2d_tails_discarded = 0

task_stats = []

for task_id in tasks:
    mod_path = v2b_root / f"runs/task{task_id}/modified_simvla/simvla_only/episode_summaries.jsonl"
    v2b_path = v2b_root / f"runs/task{task_id}/topk8_v2b_adaptive_horizon/topk8_v2b_adaptive_horizon/episode_summaries.jsonl"
    v2c_path = v2c_root / f"runs/task{task_id}/topk8_v2c_h5_adaptive_horizon/topk8_v2c_h5_adaptive_horizon/episode_summaries.jsonl"
    v2d_path = v2d_root / f"runs/task{task_id}/topk8_v2d_commit_gate/topk8_v2d_commit_gate/episode_summaries.jsonl"
    
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
    
    # Load v2d
    v2d_episodes = []
    with open(v2d_path) as f:
        for line in f:
            if line.strip():
                v2d_episodes.append(json.loads(line))
    v2d_episodes.sort(key=lambda x: x["episode_index"])
    
    assert len(mod_episodes) == 10, f"Task {task_id} modified has {len(mod_episodes)} eps"
    assert len(v2b_episodes) == 10, f"Task {task_id} v2b has {len(v2b_episodes)} eps"
    assert len(v2c_episodes) == 10, f"Task {task_id} v2c has {len(v2c_episodes)} eps"
    assert len(v2d_episodes) == 10, f"Task {task_id} v2d has {len(v2d_episodes)} eps"
    
    mod_succ_count = 0
    v2d_succ_count = 0
    mod_steps = []
    v2d_steps = []
    
    task_rescues = 0
    task_regressions = 0
    
    for i in range(10):
        m_ep = mod_episodes[i]
        v2b_ep = v2b_episodes[i]
        v2c_ep = v2c_episodes[i]
        v2d_ep = v2d_episodes[i]
        
        # Verify seed parity
        assert m_ep["reset_seed"] == v2d_ep["reset_seed"], f"Seed mismatch: {m_ep['reset_seed']} vs {v2d_ep['reset_seed']}"
        assert v2b_ep["reset_seed"] == v2d_ep["reset_seed"], f"Seed mismatch: {v2b_ep['reset_seed']} vs {v2d_ep['reset_seed']}"
        assert v2c_ep["reset_seed"] == v2d_ep["reset_seed"], f"Seed mismatch: {v2c_ep['reset_seed']} vs {v2d_ep['reset_seed']}"
        
        m_succ = m_ep["success"]
        v2b_succ = v2b_ep["success"]
        v2c_succ = v2c_ep["success"]
        v2d_succ = v2d_ep["success"]
        
        if m_succ:
            mod_succ_count += 1
            modified_success_total += 1
        if v2b_succ:
            v2b_success_total += 1
        if v2c_succ:
            v2c_success_total += 1
        if v2d_succ:
            v2d_succ_count += 1
            v2d_success_total += 1
            
        if not m_succ and v2d_succ:
            v2d_rescues_vs_modified += 1
            task_rescues += 1
        elif m_succ and not v2d_succ:
            v2d_regressions_vs_modified += 1
            task_regressions += 1
        elif m_succ and v2d_succ:
            v2d_shared_success_vs_modified += 1
        else:
            v2d_shared_failure_vs_modified += 1
            
        mod_steps.append(m_ep["num_steps"])
        v2d_steps.append(v2d_ep["num_steps"])
        modified_steps_list.append(m_ep["num_steps"])
        v2b_steps_list.append(v2b_ep["num_steps"])
        v2c_steps_list.append(v2c_ep["num_steps"])
        v2d_steps_list.append(v2d_ep["num_steps"])
        
        total_v2d_commits += v2d_ep.get("v2d_commit_count", 0)
        total_v2d_replans += v2d_ep.get("v2d_replan_count", 0)
        total_v2d_tails_committed += v2d_ep.get("v2d_tails_committed", 0)
        total_v2d_tails_discarded += v2d_ep.get("v2d_tails_discarded", 0)
        
    task_stats.append({
        "task_id": task_id,
        "mod_success": mod_succ_count,
        "v2d_success": v2d_succ_count,
        "mod_mean_steps": np.mean(mod_steps),
        "v2d_mean_steps": np.mean(v2d_steps),
        "rescues": task_rescues,
        "regressions": task_regressions
    })

print("==================================================")
print("GLOBAL SWEEP RESULTS SUMMARY")
print("==================================================")
print(f"Total Episodes Analyzed: {len(tasks) * 10}")
print(f"Modified SimVLA Success: {modified_success_total}/180 ({modified_success_total/180*100:.2f}%)")
print(f"V2B (H1) Success:       {v2b_success_total}/180 ({v2b_success_total/180*100:.2f}%)")
print(f"V2C (H5) Success:       {v2c_success_total}/180 ({v2c_success_total/180*100:.2f}%)")
print(f"V2D (Commit-Gate) Succ: {v2d_success_total}/180 ({v2d_success_total/180*100:.2f}%)")
print("--------------------------------------------------")
print(f"V2D Rescues:            {v2d_rescues_vs_modified}")
print(f"V2D Regressions:        {v2d_regressions_vs_modified}")
print(f"V2D Net Gain:           {v2d_rescues_vs_modified - v2d_regressions_vs_modified}")
print("--------------------------------------------------")
print(f"Modified Mean Steps:    {np.mean(modified_steps_list):.2f}")
print(f"V2D Mean Steps:         {np.mean(v2d_steps_list):.2f}")
print("--------------------------------------------------")
print(f"Total V2D Commit Decisions: {total_v2d_commits}")
print(f"Total V2D Replan Decisions: {total_v2d_replans}")
total_decisions = total_v2d_tails_committed + total_v2d_tails_discarded
if total_decisions > 0:
    pct_committed = (total_v2d_tails_committed / total_decisions) * 100
    pct_discarded = (total_v2d_tails_discarded / total_decisions) * 100
else:
    pct_committed = 0.0
    pct_discarded = 0.0
print(f"Tails Committed:        {total_v2d_tails_committed} ({pct_committed:.2f}%)")
print(f"Tails Discarded:        {total_v2d_tails_discarded} ({pct_discarded:.2f}%)")
print("==================================================")
print("PER-TASK SUCCESS RATES (V2D vs Modified)")
print("==================================================")
print("TaskID | Mod_Succ | V2D_Succ | Mod_Steps | V2D_Steps | Rescues | Regressions")
for s in task_stats:
    print(f"Task {s['task_id']:02d} |    {s['mod_success']}/10   |    {s['v2d_success']}/10   |   {s['mod_mean_steps']:.1f}   |   {s['v2d_mean_steps']:.1f}   |    {s['rescues']}    |      {s['regressions']}")
print("==================================================")
