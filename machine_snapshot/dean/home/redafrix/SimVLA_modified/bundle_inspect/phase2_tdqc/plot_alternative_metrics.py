import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
from scipy.stats import linregress

DATASET_PATH = "/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_denoise_clean_splits_20260504/combined_clean.jsonl"
OUTPUT_DIR = "/home/redafrix/SimVLA_modified/phase2_tdqc/plots_alternative_metrics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

LIMIT = 100

data = []
traces_success = []
traces_failure = []

with open(DATASET_PATH, 'r') as f:
    for line in f:
        item = json.loads(line)
        trace = item.get('uncertainty_trace', [])
        if not trace:
            continue
        
        trace_limited = trace[:LIMIT]
        success = item.get('success', 0)
        
        # Extract individual metrics for the trace plot
        step_metrics = {
            'path_step_mean': [step.get('path_step_mean', 0) for step in trace_limited],
            'denoise_final_mean': [step.get('denoise_final_mean', 0) for step in trace_limited],
            'denoise_delta': [step.get('denoise_delta', 0) for step in trace_limited],
            'denoise_spike': [step.get('denoise_spike', 0) for step in trace_limited],
            'max_path_var': [step.get('max_path_var', 0) for step in trace_limited],
            'denoise_final_rotation_mean': [step.get('denoise_final_rotation_mean', 0) for step in trace_limited]
        }
        
        if success == 1:
            traces_success.append(step_metrics)
        else:
            traces_failure.append(step_metrics)

        # Skip if trace is too short for basic aggregation
        if len(step_metrics['path_step_mean']) == 0:
            continue
            
        # Calculate trend of path_step_mean
        y = step_metrics['path_step_mean']
        x = np.arange(len(y))
        if len(y) > 1:
            slope, _, _, _, _ = linregress(x, y)
        else:
            slope = 0

        row = {
            'success': success,
            'failure': 1 - success,
            'max_denoise_delta': np.max(step_metrics['denoise_delta']),
            'mean_denoise_delta': np.mean(step_metrics['denoise_delta']),
            'max_denoise_spike': np.max(step_metrics['denoise_spike']),
            'max_max_path_var': np.max(step_metrics['max_path_var']),
            'max_denoise_final_rot': np.max(step_metrics['denoise_final_rotation_mean']),
            'max_denoise_final_mean': np.max(step_metrics['denoise_final_mean']),
            'path_mean_trend': slope
        }
        data.append(row)

df = pd.DataFrame(data)
df['status'] = df['success'].apply(lambda x: 'Success' if x == 1 else 'Failure')

sns.set_theme(style="whitegrid")

# 1. Time-series plots for key metrics
metrics_to_plot = ['path_step_mean', 'denoise_final_mean', 'denoise_delta', 'denoise_spike', 'max_path_var', 'denoise_final_rotation_mean']

for metric in metrics_to_plot:
    plt.figure(figsize=(10, 6))
    
    # Process Success Traces
    success_matrix = [t[metric] for t in traces_success if len(t[metric]) == LIMIT]
    if success_matrix:
        success_matrix = np.array(success_matrix)
        mean_succ = np.mean(success_matrix, axis=0)
        std_succ = np.std(success_matrix, axis=0) / np.sqrt(len(success_matrix)) # Standard Error
        x_axis = np.arange(LIMIT)
        plt.plot(x_axis, mean_succ, color='green', label=f'Success (n={len(success_matrix)})')
        plt.fill_between(x_axis, mean_succ - std_succ, mean_succ + std_succ, color='green', alpha=0.2)

    # Process Failure Traces
    failure_matrix = [t[metric] for t in traces_failure if len(t[metric]) == LIMIT]
    if failure_matrix:
        failure_matrix = np.array(failure_matrix)
        mean_fail = np.mean(failure_matrix, axis=0)
        std_fail = np.std(failure_matrix, axis=0) / np.sqrt(len(failure_matrix))
        x_axis = np.arange(LIMIT)
        plt.plot(x_axis, mean_fail, color='red', label=f'Failure (n={len(failure_matrix)})')
        plt.fill_between(x_axis, mean_fail - std_fail, mean_fail + std_fail, color='red', alpha=0.2)

    plt.title(f'Average {metric} Trajectory (First {LIMIT} Steps)')
    plt.xlabel('Step')
    plt.ylabel(metric)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'timeseries_{metric}.png'))
    plt.close()

# 2. Aggregated Alternative Metrics Analysis
alt_metrics = [
    'max_denoise_delta', 'mean_denoise_delta', 'max_denoise_spike',
    'max_max_path_var', 'max_denoise_final_rot', 'max_denoise_final_mean', 'path_mean_trend'
]

# ROC Curves
plt.figure(figsize=(12, 10))
for metric in alt_metrics:
    # Some metrics might be negatively correlated with failure (e.g. delta might be more negative?), 
    # we take absolute value or just test both directions for ROC to find the best predictor.
    # For ROC AUC > 0.5, we use the raw metric. If AUC < 0.5, it means negative correlation, so we invert it for display.
    fpr, tpr, _ = roc_curve(df['failure'], df[metric])
    roc_auc = auc(fpr, tpr)
    
    if roc_auc < 0.5:
        fpr, tpr, _ = roc_curve(df['failure'], -df[metric])
        roc_auc = auc(fpr, tpr)
        label = f'-{metric} (AUC = {roc_auc:.2f})'
    else:
        label = f'{metric} (AUC = {roc_auc:.2f})'
        
    plt.plot(fpr, tpr, lw=2, label=label)

plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title(f'ROC Curve: Predicting Failure using Alternative Features (First {LIMIT} Steps)')
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'roc_curve_alternative_metrics.png'))
plt.close()

# KDE Density plots for new metrics
for metric in alt_metrics:
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data=df, x=metric, hue='status', fill=True, palette={'Success': 'green', 'Failure': 'red'}, common_norm=False)
    plt.title(f'{metric} Density (First {LIMIT} Steps): Success vs Failure')
    plt.xlabel(metric)
    plt.ylabel('Density')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'kde_{metric}.png'))
    plt.close()

print(f"Successfully generated alternative metric plots in {OUTPUT_DIR}")
