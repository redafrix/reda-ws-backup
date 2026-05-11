import json
import numpy as np
import os
import matplotlib.pyplot as plt
from glob import glob

def analyze_uncertainty(data_dir):
    success_files = glob(os.path.join(data_dir, "*_success_uncertainty.json"))
    failure_files = glob(os.path.join(data_dir, "*_failure_uncertainty.json"))
    
    def get_stats(files):
        all_means = []
        all_trajectories = []
        for f in files:
            with open(f, 'r') as j:
                data = json.load(j)
                # path_variance is typically [horizon, action_dim]
                # We'll take the mean across action dimensions for each timestep
                vars = [np.mean(step['path_variance']) for step in data]
                all_means.append(np.mean(vars))
                all_trajectories.append(vars)
        return all_means, all_trajectories

    s_means, s_trajs = get_stats(success_files)
    f_means, f_trajs = get_stats(failure_files)

    print("=== Uncertainty Analysis Report ===")
    print(f"Successes Analyzed: {len(s_means)}")
    print(f"Failures Analyzed: {len(f_means)}")
    print(f"Average Variance (Success): {np.mean(s_means):.6f}")
    print(f"Average Variance (Failure): {np.mean(f_means):.6f}")
    
    # Check for "Self-Awareness": Is failure variance significantly higher?
    diff = (np.mean(f_means) - np.mean(s_means)) / np.mean(s_means) * 100
    print(f"Uncertainty is {diff:.2f}% higher in failures.")

    # Plotting representative trajectories
    plt.figure(figsize=(12, 6))
    if s_trajs:
        plt.plot(s_trajs[0], label="Success Example (Task 0)", color='green', alpha=0.7)
    if f_trajs:
        plt.plot(f_trajs[0], label="Failure Example (Task 4)", color='red', alpha=0.7)
    
    plt.title("Uncertainty over Time: Success vs Failure")
    plt.xlabel("Environment Step")
    plt.ylabel("Mean Path Variance")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("uncertainty_comparison.png")
    print("Generated comparison plot: uncertainty_comparison.png")

# Data directory from the last evaluation run
from pathlib import Path
ROOT = Path(__file__).parents[2]
data_dir = ROOT / "eval_outputs" / "sweep_2_final_uncertainty_v2"
analyze_uncertainty(data_dir)
