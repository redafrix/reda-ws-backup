import json
import os
import numpy as np
import pandas as pd
from collections import defaultdict

def load_episodes(path):
    episodes = {}
    with open(path, 'r') as f:
        for line in f:
            data = json.loads(line)
            episodes[data['reset_seed']] = data
    return episodes

def analyze_task(task_name, root, policies):
    policy_data = {}
    for pol_key, pol_path in policies.items():
        full_path = os.path.join(root, task_name, pol_path, 'episode_summaries.jsonl')
        policy_data[pol_key] = load_episodes(full_path)
    
    # Check if all policies have 100 episodes
    for pol_key, data in policy_data.items():
        if len(data) != 100:
            print(f"WARNING: {task_name} {pol_key} has {len(data)} episodes instead of 100")

    seeds = sorted(list(policy_data['original_simvla'].keys()))
    
    # Paired comparisons
    results = []
    for seed in seeds:
        orig = policy_data['original_simvla'][seed]
        mod = policy_data['modified_simvla'][seed]
        risk = policy_data['risk_topk8'][seed]
        
        results.append({
            'seed': seed,
            'orig_success': orig.get('success', False),
            'mod_success': mod.get('success', False),
            'risk_success': risk.get('success', False),
            'orig_steps': orig.get('num_steps', 0),
            'mod_steps': mod.get('num_steps', 0),
            'risk_steps': risk.get('num_steps', 0),
            'risk_mods': risk.get('action_modifications_count', 0)
        })
    
    df = pd.DataFrame(results)
    
    analysis = {
        'task': task_name,
        'episodes': len(df),
        'metrics': {},
        'paired': {},
        'risk_stats': {}
    }
    
    for pol in ['orig', 'mod', 'risk']:
        success = df[f'{pol}_success']
        analysis['metrics'][pol] = {
            'success_rate': float(success.mean()),
            'mean_steps': float(df[f'{pol}_steps'].mean()),
            'success_mean_steps': float(df[df[f'{pol}_success']][f'{pol}_steps'].mean()) if success.any() else 0.0,
            'failure_mean_steps': float(df[~df[f'{pol}_success']][f'{pol}_steps'].mean()) if (~success).any() else 0.0,
        }
        
    # Paired logic
    def compare(p1_success, p2_success):
        res = {
            'shared_success': int(((p1_success == True) & (p2_success == True)).sum()),
            'shared_failure': int(((p1_success == False) & (p2_success == False)).sum()),
            'p2_rescue_p1': int(((p1_success == False) & (p2_success == True)).sum()),
            'p2_regress_p1': int(((p1_success == True) & (p2_success == False)).sum())
        }
        return res

    analysis['paired']['mod_vs_orig'] = compare(df['orig_success'], df['mod_success'])
    analysis['paired']['risk_vs_mod'] = compare(df['mod_success'], df['risk_success'])
    analysis['paired']['risk_vs_orig'] = compare(df['orig_success'], df['risk_success'])
    
    # Risk mods stats
    risk_df = df[df['risk_mods'] > 0]
    # Convert mod_dist keys to string for JSON serialization
    mod_dist_raw = df['risk_mods'].value_counts().to_dict()
    mod_dist = {str(k): int(v) for k, v in mod_dist_raw.items()}
    
    analysis['risk_stats'] = {
        'mod_episodes': int(len(risk_df)),
        'total_mods': int(df['risk_mods'].sum()),
        'mean_mods_per_ep': float(df['risk_mods'].mean()),
        'mod_dist': mod_dist,
        'rescue_in_mod_ep': int(((df['risk_mods'] > 0) & (df['mod_success'] == False) & (df['risk_success'] == True)).sum()),
        'regress_in_mod_ep': int(((df['risk_mods'] > 0) & (df['mod_success'] == True) & (df['risk_success'] == False)).sum()),
        'neutral_in_mod_ep': int(((df['risk_mods'] > 0) & (df['mod_success'] == df['risk_success'])).sum())
    }
    
    return analysis

def main():
    root = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608/runs/production_goal_swap_100ep_20260608"
    tasks = {
        'top_drawer_bowl': 'top_drawer_bowl',
        'cream_cheese_bowl': 'cream_cheese_bowl',
        'bowl_on_plate': 'bowl_on_plate'
    }
    policies = {
        'original_simvla': 'original_simvla/simvla_only',
        'modified_simvla': 'modified_simvla/simvla_only',
        'risk_topk8': 'risk_topk8/risk_topk8'
    }
    
    full_analysis = []
    
    for task_name in tasks:
        task_res = analyze_task(task_name, root, policies)
        full_analysis.append(task_res)

    print(json.dumps(full_analysis, indent=2))

if __name__ == "__main__":
    main()
