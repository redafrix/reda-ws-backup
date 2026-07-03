import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.metrics import roc_curve, auc

DATASET_PATH = "/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_pro_state_mahal_k8_6000_20260507_145523/combined_all_suites_all_seeds.jsonl"
BASE_OUTPUT_DIR = "/home/redafrix/SimVLA_modified/phase2_tdqc/plots_sample_actions"

def print_action_chunk_differences():
    print("=== Differences between Action Chunks (Noise Sensitivity) per Task Suite ===")
    suites_seen = set()
    with open(DATASET_PATH, 'r') as f:
        for line in f:
            data = json.loads(line)
            suite = data.get('task_suite')
            if suite not in suites_seen:
                suites_seen.add(suite)
                trace = data.get('uncertainty_trace', [])
                if trace:
                    first_step = trace[0]
                    sample_var = first_step.get('sample_action_variance', [])
                    print(f"Task Suite: {suite}")
                    print(f"  Task ID: {data.get('task_id')} | Success: {data.get('success')} | Env Step: {first_step.get('env_step')}")
                    if sample_var:
                        # Print the first action's variance across its dimensions to show the differences
                        print(f"  Sample Action Variance (1st action chunk dims): {sample_var[0] if len(sample_var)>0 else 'N/A'}")
                    print(f"  Sample Action Var Max: {first_step.get('sample_action_var_max', 0):.6f} | Mean: {first_step.get('sample_action_var_mean', 0):.6f}")
                    print(f"  Sample Action L2 Max: {first_step.get('sample_action_l2_max', 0):.6f} | Mean: {first_step.get('sample_action_l2_mean', 0):.6f}")
                    print("-" * 60)
            if len(suites_seen) >= 11:
                break
    print("==============================================================================\n")

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
            sns.lineplot(data=df_all_steps, x='step_idx', y=metric, hue='status', palette={'Success': 'green', 'Failure': 'red'})
            plt.title(f'{metric} over Time (Steps): Success vs Failure')
            plt.xlabel('Step Index')
            plt.ylabel(metric)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'time_series_{metric}.png'))
            plt.close()

def generate_plots_for_limit(limit, dataset_lines):
    output_dir = os.path.join(BASE_OUTPUT_DIR, f"first_{limit}_steps")
    os.makedirs(output_dir, exist_ok=True)
    
    data = []
    
    for item in dataset_lines:
        trace = item.get('uncertainty_trace', [])
        if not trace:
            continue
        
        trace_limited = trace[:limit]
        
        # We aggregate the maximum over the first N steps as a predictor for failure
        step_metrics = {
            'sample_action_var_mean': [step.get('sample_action_var_mean', 0) for step in trace_limited],
            'sample_action_var_max': [step.get('sample_action_var_max', 0) for step in trace_limited],
            'sample_action_l2_mean': [step.get('sample_action_l2_mean', 0) for step in trace_limited],
            'sample_action_l2_max': [step.get('sample_action_l2_max', 0) for step in trace_limited],
            'sample_action_translation_var': [step.get('sample_action_translation_var', 0) for step in trace_limited],
            'sample_action_rotation_var': [step.get('sample_action_rotation_var', 0) for step in trace_limited],
            'sample_action_gripper_var': [step.get('sample_action_gripper_var', 0) for step in trace_limited],
        }

        if not step_metrics['sample_action_var_mean']:
            continue

        row = {
            'success': item.get('success', 0),
            'steps': item.get('steps', 0),
            'max_sample_action_var_mean': np.max(step_metrics['sample_action_var_mean']),
            'max_sample_action_var_max': np.max(step_metrics['sample_action_var_max']),
            'max_sample_action_l2_mean': np.max(step_metrics['sample_action_l2_mean']),
            'max_sample_action_l2_max': np.max(step_metrics['sample_action_l2_max']),
            'max_sample_action_translation_var': np.max(step_metrics['sample_action_translation_var']),
            'max_sample_action_rotation_var': np.max(step_metrics['sample_action_rotation_var']),
            'max_sample_action_gripper_var': np.max(step_metrics['sample_action_gripper_var']),
        }
        data.append(row)

    df = pd.DataFrame(data)
    if df.empty:
        print(f"No data for limit {limit}")
        return
        
    df['failure'] = 1 - df['success']
    df['status'] = df['success'].apply(lambda x: 'Success' if x == 1 else 'Failure')

    uncertainty_metrics = [
        'max_sample_action_var_mean', 'max_sample_action_var_max',
        'max_sample_action_l2_mean', 'max_sample_action_l2_max',
        'max_sample_action_translation_var', 'max_sample_action_rotation_var', 'max_sample_action_gripper_var'
    ]

    sns.set_theme(style="whitegrid")

    # 1. Boxplots
    for metric in uncertainty_metrics:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='status', y=metric, data=df, hue='status', palette={'Success': 'green', 'Failure': 'red'}, legend=False)
        plt.title(f'{metric} (First {limit} Steps)')
        plt.ylabel(metric)
        plt.xlabel('Episode Outcome')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'boxplot_{metric}.png'))
        plt.close()

    # 2. KDE Plots
    for metric in uncertainty_metrics:
        plt.figure(figsize=(8, 6))
        sns.kdeplot(data=df, x=metric, hue='status', fill=True, palette={'Success': 'green', 'Failure': 'red'}, common_norm=False)
        plt.title(f'{metric} Density (First {limit} Steps)')
        plt.xlabel(metric)
        plt.ylabel('Density')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'kde_{metric}.png'))
        plt.close()

    # 3. ROC Curves
    plt.figure(figsize=(10, 8))
    for metric in uncertainty_metrics:
        metric_vals = df[metric]
        fpr, tpr, _ = roc_curve(df['failure'], metric_vals)
        roc_auc = auc(fpr, tpr)
        
        if roc_auc < 0.5:
            fpr, tpr, _ = roc_curve(df['failure'], -metric_vals)
            roc_auc = auc(fpr, tpr)
            label_suffix = " (inverted)"
        else:
            label_suffix = ""
            
        plt.plot(fpr, tpr, lw=2, label=f'{metric}{label_suffix} (AUC = {roc_auc:.2f})')

    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve (First {limit} Steps)')
    plt.legend(loc="lower right", fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'roc_curve_all_metrics.png'))
    plt.close()

    print(f"Generated plots for first {limit} steps in {output_dir}")

def main():
    print_action_chunk_differences()
    
    print("Loading dataset into memory...")
    dataset_lines = []
    time_series_data = []
    
    with open(DATASET_PATH, 'r') as f:
        for line in f:
            item = json.loads(line)
            dataset_lines.append(item)
            
            # Subsample for time series to avoid massive memory usage
            if np.random.rand() < 0.2:
                status = 'Success' if item.get('success', 0) == 1 else 'Failure'
                for i, step in enumerate(item.get('uncertainty_trace', [])):
                    if i > 200:
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
                    
    df_time_series = pd.DataFrame(time_series_data)
    
    print("Generating time series plots...")
    time_series_dir = os.path.join(BASE_OUTPUT_DIR, "time_series")
    plot_metrics_over_time(df_time_series, time_series_dir)
    print(f"Time series plots saved to {time_series_dir}")

    limits = [50, 70, 90, 120]
    for limit in limits:
        print(f"Processing limit: {limit} steps...")
        generate_plots_for_limit(limit, dataset_lines)
        
    print("All done!")

if __name__ == "__main__":
    main()
