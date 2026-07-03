import json
import numpy as np
import os
import matplotlib.pyplot as plt
from glob import glob
from pathlib import Path

def analyze_fair_comparison(eval_root, task_identifier, window_size=300):
    # Find all uncertainty files for this task across all subfolders
    pattern = os.path.join(eval_root, "**", f"*{task_identifier}*_uncertainty.json")
    files = glob(pattern, recursive=True)
    
    success_means = []
    failure_means = []
    
    # Track unique trials by folder and filename to avoid double-counting
    processed = set()

    for f in files:
        if f in processed: continue
        processed.add(f)
        
        is_success = "success" in f.lower()
        
        with open(f, 'r') as j:
            try:
                data = json.load(j)
                # Take only the first window_size steps
                # Many rollouts are longer, but we crop them for fairness
                window_data = data[:window_size]
                
                if len(window_data) < window_size and not is_success:
                    # Skip failures that didn't even reach 130 steps (rare)
                    continue
                
                # Mean variance per rollout for this window
                rollout_mean = np.mean([np.mean(step['path_variance']) for step in window_data])
                
                if is_success:
                    success_means.append(rollout_mean)
                else:
                    failure_means.append(rollout_mean)
            except Exception as e:
                print(f"Error processing {f}: {e}")

    print(f"=== Fair Uncertainty Comparison (First {window_size} Steps) ===")
    print(f"Total Unique Task 5 Trials: {len(processed)}")
    print(f"Successes Found: {len(success_means)}")
    print(f"Failures Found: {len(failure_means)}")
    
    if success_means and failure_means:
        s_avg = np.mean(success_means)
        f_avg = np.mean(failure_means)
        gap = (f_avg - s_avg) / s_avg * 100
        print(f"\n[STATISTICS]")
        print(f"  Average Uncertainty (Success): {s_avg:.6f}")
        print(f"  Average Uncertainty (Failure): {f_avg:.6f}")
        print(f"  Systematic Gap: +{gap:.2f}% higher in failures")
        
        # Check overlap
        print(f"\n[DISTRIBUTION]")
        print(f"  Success Range: {np.min(success_means):.6f} - {np.max(success_means):.6f}")
        print(f"  Failure Range: {np.min(failure_means):.6f} - {np.max(failure_means):.6f}")
        
        # Visual check
        plt.figure(figsize=(10, 6))
        plt.boxplot([success_means, failure_means], labels=["Success", "Failure"])
        plt.title(f"Uncertainty Distribution (Steps 0-{window_size}) - Task 5")
        plt.ylabel("Mean Variance")
        plt.grid(True, alpha=0.2)
        # Save to local results/plots folder for standalone portability
        output_plot = Path(__file__).parents[1] / "results/plots/fair_uncertainty_comparison_300steps.png"
        os.makedirs(output_plot.parent, exist_ok=True)
        plt.savefig(output_plot)
        print(f"\nGenerated boxplot: {output_plot}")
    else:
        print("\nInsufficient data for comparison.")

# Path relative to workspace root
WS_ROOT = Path(__file__).parents[4]
eval_root = WS_ROOT / "outputs/eval"
task_id = "on_the_ramekin"
analyze_fair_comparison(eval_root, task_id, window_size=300)
