import json
import os
import glob
from collections import defaultdict

def analyze_jsonl(file_path):
    episodes = 0
    successes = 0
    failures = 0
    total_steps = 0
    total_mods = 0
    mod_episodes = 0
    errors = 0
    seeds = []
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                episodes += 1
                
                # Success/Failure
                if data.get('success') is True or data.get('outcome') == 'success':
                    successes += 1
                else:
                    failures += 1
                
                # Steps
                total_steps += data.get('num_steps', data.get('steps', 0))
                
                # Mods
                mods = data.get('action_modifications_count', data.get('mods', 0))
                total_mods += mods
                if mods > 0:
                    mod_episodes += 1
                
                # Error
                if data.get('error_message') or data.get('error'):
                    errors += 1
                
                # Seeds
                seed = data.get('reset_seed', data.get('seed'))
                seeds.append(seed)
    except Exception as e:
        return {"error": str(e)}

    unique_seeds = len(set(seeds))
    duplicate_seeds = episodes - unique_seeds
    
    return {
        "episodes": episodes,
        "successes": successes,
        "failures": failures,
        "success_rate": successes / episodes if episodes > 0 else 0,
        "mean_steps": total_steps / episodes if episodes > 0 else 0,
        "mod_episodes": mod_episodes,
        "total_mods": total_mods,
        "errors": errors,
        "duplicate_seeds": duplicate_seeds,
        "unique_seeds": unique_seeds,
        "path": file_path
    }

def main():
    roots = [
        "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608",
        "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608",
        "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608",
        "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608"
    ]
    
    all_results = []
    for root in roots:
        files = glob.glob(os.path.join(root, "**/episode_summaries.jsonl"), recursive=True)
        for f in files:
            # Skip input datasets
            if "inputs/datasets" in f:
                continue
            res = analyze_jsonl(f)
            if "error" not in res:
                all_results.append(res)
    
    print(json.dumps(all_results, indent=2))

if __name__ == "__main__":
    main()
