import json
import numpy as np
import os
import matplotlib.pyplot as plt
from glob import glob

def analyze_individual_rollouts(data_dir):
    success_files = glob(os.path.join(data_dir, "*_success_uncertainty.json"))
    failure_files = glob(os.path.join(data_dir, "*_failure_uncertainty.json"))
    
    def get_rollout_data(files):
        data_list = []
        for f in files:
            with open(f, 'r') as j:
                steps_data = json.load(j)
                # Mean variance per step
                vars = [np.mean(step['path_variance']) for step in steps_data]
                data_list.append({
                    "name": os.path.basename(f),
                    "trajectory": vars,
                    "mean": np.mean(vars),
                    "max": np.max(vars),
                    "std": np.std(vars)
                })
        return data_list

    successes = get_rollout_data(success_files)
    failures = get_rollout_data(failure_files)

    print("=== Deep Individual Comparison Report ===")
    
    print("\n[SUCCESS ROLLOUTS]")
    s_means = []
    for i, s in enumerate(successes):
        print(f"  Rollout {i}: Mean={s['mean']:.6f}, Max={s['max']:.6f}, Steps={len(s['trajectory'])}")
        s_means.append(s['mean'])
    if s_means:
        print(f"  >> Consistency (Std Dev between Successes): {np.std(s_means):.6f}")

    print("\n[FAILURE ROLLOUTS]")
    f_means = []
    for i, f in enumerate(failures):
        # Only show first few for brevity in print, but calculate for all
        if i < 3:
            print(f"  Rollout {i}: Mean={f['mean']:.6f}, Max={f['max']:.6f}, Steps={len(f['trajectory'])}")
        f_means.append(f['mean'])
    print(f"  (Total {len(failures)} failures analyzed)")
    if f_means:
        print(f"  >> Consistency (Std Dev between Failures): {np.std(f_means):.6f}")

    # Cross-comparison
    if s_means and f_means:
        gap = np.mean(f_means) - np.mean(s_means)
        print(f"\n[CROSS-GROUP ANALYSIS]")
        print(f"  Average Gap (Fail-Succ): {gap:.6f}")
        print(f"  Ratio (Failure/Success): {np.mean(f_means)/np.mean(s_means):.2f}x")

    # Plotting ALL individual trajectories to see the overlap
    plt.figure(figsize=(15, 8))
    for s in successes:
        plt.plot(s['trajectory'], color='green', alpha=0.6, linewidth=1, label='Success' if s == successes[0] else "")
    for f in failures:
        plt.plot(f['trajectory'], color='red', alpha=0.2, linewidth=0.5, label='Failure' if f == failures[0] else "")
    
    plt.title("Individual Uncertainty Fingerprints: Success vs Failure (Task 5)")
    plt.xlabel("Step")
    plt.ylabel("Uncertainty (Variance)")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.savefig("individual_uncertainty_comparison.png")
    print("\nGenerated: individual_uncertainty_comparison.png")

from pathlib import Path
ROOT = Path(__file__).parents[2]
data_dir = ROOT / "eval_outputs" / "task5_retest_800steps"
analyze_individual_rollouts(data_dir)
