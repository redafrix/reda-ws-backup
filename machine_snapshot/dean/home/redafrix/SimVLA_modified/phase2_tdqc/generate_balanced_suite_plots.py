import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

DATASET_PATH = "/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_pro_state_mahal_k8_6000_20260507_145523/combined_all_suites_all_seeds.jsonl"
TARGET_SUITE = "libero_10_object"
BASE_OUTPUT_DIR = f"/home/redafrix/SimVLA_modified/phase2_tdqc/plots_sample_actions_balanced_{TARGET_SUITE}"

def plot_metrics_over_time(df_all_steps, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid")
    
    metrics = [
        'sample_action_var_mean', 'sample_action_var_max',
        'sample_action_l2_mean', 'sample_action_l2_max',
        'sample_action_translation_var', 'sample_action_rotation_var', 'sample_action_gripper_var'
    ]
    
    for metric in metrics:
        if metric in df_all_steps.columns:
            plt.figure(figsize=(10, 6))
            # Use error bars (ci='sd' or 'boot') to show variance across episodes
            sns.lineplot(data=df_all_steps, x='step_idx', y=metric, hue='status', palette={'Success': 'green', 'Failure': 'red'})
            plt.title(f'{metric} over Time ({TARGET_SUITE}): Success vs Failure')
            plt.xlabel('Step Index')
            plt.ylabel(metric)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'time_series_{metric}.png'))
            plt.close()

def main():
    print(f"Loading dataset and filtering for {TARGET_SUITE}...")
    time_series_data = []
    
    success_count = 0
    failure_count = 0
    
    with open(DATASET_PATH, 'r') as f:
        for line in f:
            item = json.loads(line)
            if item.get('task_suite') != TARGET_SUITE:
                continue
                
            status = 'Success' if item.get('success', 0) == 1 else 'Failure'
            if status == 'Success':
                success_count += 1
            else:
                failure_count += 1
                
            # We collect all episodes for this specific suite to get a good average
            for i, step in enumerate(item.get('uncertainty_trace', [])):
                if i > 250: # Limit to 250 steps
                    break
                row = {
                    'step_idx': i,
                    'status': status,
                    'sample_action_var_mean': step.get('sample_action_var_mean', 0),
                    'sample_action_var_max': step.get('sample_action_var_max', 0),
                    'sample_action_l2_mean': step.get('sample_action_l2_mean', 0),
                    'sample_action_l2_max': step.get('sample_action_l2_max', 0),
                    'sample_action_translation_var': step.get('sample_action_translation_var', 0),
                    'sample_action_rotation_var': step.get('sample_action_rotation_var', 0),
                    'sample_action_gripper_var': step.get('sample_action_gripper_var', 0),
                }
                time_series_data.append(row)
                    
    print(f"Found {success_count} Successes and {failure_count} Failures.")
    df_time_series = pd.DataFrame(time_series_data)
    
    print("Generating time series plots...")
    time_series_dir = os.path.join(BASE_OUTPUT_DIR, "time_series")
    plot_metrics_over_time(df_time_series, time_series_dir)
    print(f"Time series plots saved to {time_series_dir}")

if __name__ == "__main__":
    main()
