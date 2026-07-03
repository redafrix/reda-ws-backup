import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score

DATASET_PATH = "/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_denoise_clean_splits_20260504/combined_clean.jsonl"
BASE_OUTPUT_DIR = "/home/redafrix/SimVLA_modified/phase2_tdqc/plots_uncertainty_correlation_comprehensive"

def print_action_chunk_variances():
    print("=== Action Chunk Variances (Noise Sensitivity) per Task Suite ===")
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
                    path_var = first_step.get('path_variance', [])
                    print(f"Task Suite: {suite}")
                    print(f"  Task ID: {data.get('task_id')} | Success: {data.get('success')} | Env Step: {first_step.get('env_step')}")
                    if len(path_var) > 5:
                        print(f"  Sample Path Variance (first 5 dims): {path_var[:5]} ... (len={len(path_var)})")
                    else:
                        print(f"  Sample Path Variance: {path_var}")
                    print(f"  Max Path Var: {first_step.get('max_path_var'):.4f} | Denoise Delta: {first_step.get('denoise_delta', 0):.4f}")
                    print("-" * 40)
            if len(suites_seen) >= 11: # We know there are 11 suites
                break
    print("===============================================================\n")

def plot_metrics_over_time(df_all_steps, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid")
    
    metrics = ['path_step_mean', 'denoise_final_mean', 'denoise_delta', 'denoise_spike', 'max_path_var', 'denoise_final_rotation_mean']
    
    for metric in metrics:
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
        
        step_metrics = {
            'path_step_mean': [step.get('path_step_mean', 0) for step in trace_limited],
            'last_step_mean': [step.get('last_step_mean', 0) for step in trace_limited],
            'max_path_var': [step.get('max_path_var', 0) for step in trace_limited],
            'denoise_final_mean': [step.get('denoise_final_mean', 0) for step in trace_limited],
            'denoise_delta': [step.get('denoise_delta', 0) for step in trace_limited],
            'denoise_spike': [step.get('denoise_spike', 0) for step in trace_limited],
            'denoise_final_rotation_mean': [step.get('denoise_final_rotation_mean', 0) for step in trace_limited]
        }

        if not step_metrics['path_step_mean']:
            continue

        row = {
            'success': item.get('success', 0),
            'steps': item.get('steps', 0),
            'max_path_step_mean': np.max(step_metrics['path_step_mean']),
            'mean_path_step_mean': np.mean(step_metrics['path_step_mean']),
            'max_last_step_mean': np.max(step_metrics['last_step_mean']),
            'max_max_path_var': np.max(step_metrics['max_path_var']),
            'max_denoise_final_mean': np.max(step_metrics['denoise_final_mean']),
            'max_denoise_delta': np.max(step_metrics['denoise_delta']),
            'mean_denoise_delta': np.mean(step_metrics['denoise_delta']),
            'max_denoise_spike': np.max(step_metrics['denoise_spike']),
            'max_denoise_final_rotation': np.max(step_metrics['denoise_final_rotation_mean']),
        }
        data.append(row)

    df = pd.DataFrame(data)
    if df.empty:
        print(f"No data for limit {limit}")
        return
        
    df['failure'] = 1 - df['success']
    df['status'] = df['success'].apply(lambda x: 'Success' if x == 1 else 'Failure')

    uncertainty_metrics = [
        'max_path_step_mean', 'mean_path_step_mean', 'max_last_step_mean', 
        'max_max_path_var', 'max_denoise_final_mean', 'max_denoise_delta', 
        'mean_denoise_delta', 'max_denoise_spike', 'max_denoise_final_rotation'
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
        # For delta, lower might mean higher uncertainty in some contexts, but usually higher is worse, 
        # let's assume higher value -> higher chance of failure. If some need negation, we'd adjust, 
        # but for max variance, max mean, higher is worse.
        # Actually denoise_delta is often negative. Let's use abs or assume higher is worse if it goes positive.
        # Let's just use raw values to see correlation.
        metric_vals = df[metric]
        fpr, tpr, _ = roc_curve(df['failure'], metric_vals)
        roc_auc = auc(fpr, tpr)
        
        # If AUC < 0.5, it means inverse correlation. Flip it for the plot to show predictive power.
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
    print_action_chunk_variances()
    
    print("Loading dataset into memory...")
    dataset_lines = []
    time_series_data = []
    
    with open(DATASET_PATH, 'r') as f:
        for line in f:
            item = json.loads(line)
            dataset_lines.append(item)
            
            # Prepare time series data (subsample for memory efficiency)
            if np.random.rand() < 0.1: # Use 10% of episodes for time series to avoid massive memory usage
                status = 'Success' if item.get('success', 0) == 1 else 'Failure'
                for i, step in enumerate(item.get('uncertainty_trace', [])):
                    if i > 200: # Limit to first 200 steps for time series
                        break
                    row = {
                        'step_idx': i,
                        'status': status,
                        'path_step_mean': step.get('path_step_mean', 0),
                        'denoise_final_mean': step.get('denoise_final_mean', 0),
                        'denoise_delta': step.get('denoise_delta', 0),
                        'denoise_spike': step.get('denoise_spike', 0),
                        'max_path_var': step.get('max_path_var', 0),
                        'denoise_final_rotation_mean': step.get('denoise_final_rotation_mean', 0)
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
