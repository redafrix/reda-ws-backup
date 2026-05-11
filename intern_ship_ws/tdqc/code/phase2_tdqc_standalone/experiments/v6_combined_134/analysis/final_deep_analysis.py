import json
import numpy as np
import os
import matplotlib.pyplot as plt
from glob import glob

def final_cross_task_deep_analysis(success_dir, failure_dir):
    s_files = glob(os.path.join(success_dir, "*_success_uncertainty.json"))
    f_files = glob(os.path.join(failure_dir, "*_failure_uncertainty.json"))
    
    def get_data(files):
        stats = []
        trajs = []
        for f in files:
            with open(f, 'r') as j:
                d = json.load(j)
                v = [np.mean(step['path_variance']) for step in d]
                stats.append({"mean": np.mean(v), "max": np.max(v), "steps": len(v)})
                trajs.append(v)
        return stats, trajs

    s_stats, s_trajs = get_data(s_files)
    f_stats, f_trajs = get_data(f_files)

    s_means = [x['mean'] for x in s_stats]
    f_means = [x['mean'] for x in f_stats]

    print("=== FINAL CROSS-TASK UNCERTAINTY ANALYSIS ===")
    print(f"Successes (Task 4): {len(s_means)}")
    print(f"Failures (Task 5): {len(f_means)}")
    
    overall_gap = np.mean(f_means) - np.mean(s_means)
    print(f"\n[SUMMARY]")
    print(f"  Systematic Uncertainty Gap: {overall_gap:.6f} (+{overall_gap/np.mean(s_means)*100:.2f}%)")

    # Plot
    plt.figure(figsize=(12, 6))
    for i, t in enumerate(s_trajs):
        plt.plot(t, color='green', alpha=0.3, label='Success' if i==0 else "")
    for i, t in enumerate(f_trajs):
        plt.plot(t, color='red', alpha=0.3, label='Failure' if i==0 else "")
    plt.title("Deep Comparison: Successes vs Failures (Cross-Task)")
    plt.xlabel("Step")
    plt.ylabel("Variance")
    plt.legend()
    plt.grid(True, alpha=0.2)
    output_path = "results/plots/final_deep_uncertainty_comparison.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"\nGenerated: {output_path}")

# Default paths
from pathlib import Path
ROOT = Path(__file__).parents[2]
s_dir = ROOT / "eval_outputs" / "task5_450limit_eval"
f_dir = ROOT / "eval_outputs" / "task5_450limit_eval"
final_cross_task_deep_analysis(s_dir, f_dir)
