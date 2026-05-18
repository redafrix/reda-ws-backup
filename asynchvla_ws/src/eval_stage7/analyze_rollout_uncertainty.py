import json
import numpy as np
import sys
from pathlib import Path

def analyze_json(path):
    with open(path) as f:
        data = json.load(f)
    
    eps = data.get("episodes", [])
    num_eps = len(eps)
    successes = [e for e in eps if e.get("success")]
    num_success = len(successes)
    
    success_rate = (num_success / num_eps * 100) if num_eps > 0 else 0
    
    all_steps = [e.get("steps", 0) for e in eps]
    success_steps = [e.get("steps", 0) for e in successes]
    
    avg_steps = np.mean(all_steps) if all_steps else 0
    avg_success_steps = np.mean(success_steps) if success_steps else 0
    
    all_rewards = []
    for e in eps:
        trace = e.get("trace", [])
        rewards = [t.get("reward", 0.0) for t in trace if "reward" in t]
        all_rewards.append(sum(rewards))
    
    avg_total_reward = np.mean(all_rewards) if all_rewards else 0
    
    # Uncertainty analysis
    all_unc = []
    chosen_seeds = []
    seed0_unc = []
    
    for e in eps:
        trace = e.get("trace", [])
        for t in trace:
            if t.get("kind") == "replan":
                scores = t.get("scores", [])
                if scores:
                    all_unc.extend(scores)
                    seed0_unc.append(scores[0])
                chosen_seeds.append(t.get("chosen_seed"))

    unc_metrics = {
        "mean": float(np.mean(all_unc)) if all_unc else 0,
        "min": float(np.min(all_unc)) if all_unc else 0,
        "max": float(np.max(all_unc)) if all_unc else 0,
        "std": float(np.std(all_unc)) if all_unc else 0,
    }
    
    seed_dist = {}
    if chosen_seeds:
        for s in set(chosen_seeds):
            if s is not None:
                seed_dist[int(s)] = chosen_seeds.count(s)

    return {
        "task": data.get("task_language"),
        "num_episodes": num_eps,
        "success_rate": success_rate,
        "avg_steps": float(avg_steps),
        "avg_success_steps": float(avg_success_steps),
        "avg_total_reward": float(avg_total_reward),
        "unc_metrics": unc_metrics,
        "seed_distribution": seed_dist,
        "seed0_unc_avg": float(np.mean(seed0_unc)) if seed0_unc else 0
    }

if __name__ == "__main__":
    paths = sys.argv[1:]
    results = {}
    for p in paths:
        name = Path(p).stem
        results[name] = analyze_json(p)
    
    print(json.dumps(results, indent=2))
