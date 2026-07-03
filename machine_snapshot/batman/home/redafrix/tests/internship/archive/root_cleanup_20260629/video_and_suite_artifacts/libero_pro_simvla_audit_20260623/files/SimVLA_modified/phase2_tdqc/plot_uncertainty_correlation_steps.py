import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score

DATASET_PATH = "/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_denoise_clean_splits_20260504/combined_clean.jsonl"
BASE_OUTPUT_DIR = "/home/redafrix/SimVLA_modified/phase2_tdqc/plots_uncertainty_correlation"

def generate_plots_for_limit(limit):
    output_dir = os.path.join(BASE_OUTPUT_DIR, f"first_{limit}_steps")
    os.makedirs(output_dir, exist_ok=True)
    
    data = []
    with open(DATASET_PATH, 'r') as f:
        for line in f:
            item = json.loads(line)
            trace = item.get('uncertainty_trace', [])
            if not trace:
                continue
            
            trace_limited = trace[:limit]
            
            path_means = [step['path_step_mean'] for step in trace_limited if 'path_step_mean' in step]
            last_means = [step['last_step_mean'] for step in trace_limited if 'last_step_mean' in step]

            if not path_means or not last_means:
                continue

            row = {
                'success': item.get('success', 0),
                'steps': item.get('steps', 0),
                'mean_path_uncertainty': np.mean(path_means),
                'max_path_uncertainty': np.max(path_means),
                'mean_last_step_uncertainty': np.mean(last_means),
                'max_last_step_uncertainty': np.max(last_means)
            }
            data.append(row)

    df = pd.DataFrame(data)
    df['failure'] = 1 - df['success']
    df['status'] = df['success'].apply(lambda x: 'Success' if x == 1 else 'Failure')

    uncertainty_metrics = [
        'mean_path_uncertainty',
        'max_path_uncertainty',
        'mean_last_step_uncertainty',
        'max_last_step_uncertainty'
    ]

    sns.set_theme(style="whitegrid")

    # 1. Boxplots
    for metric in uncertainty_metrics:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='status', y=metric, data=df, hue='status', palette={'Success': 'green', 'Failure': 'red'}, legend=False)
        plt.title(f'{metric} Distribution (First {limit} Steps): Success vs Failure')
        plt.ylabel(metric)
        plt.xlabel('Episode Outcome')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'boxplot_{metric}.png'))
        plt.close()

    # 2. KDE Plots
    for metric in uncertainty_metrics:
        plt.figure(figsize=(8, 6))
        sns.kdeplot(data=df, x=metric, hue='status', fill=True, palette={'Success': 'green', 'Failure': 'red'}, common_norm=False)
        plt.title(f'{metric} Density (First {limit} Steps): Success vs Failure')
        plt.xlabel(metric)
        plt.ylabel('Density')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'kde_{metric}.png'))
        plt.close()

    # 3. Binned Failure Rates
    for metric in uncertainty_metrics:
        plt.figure(figsize=(8, 6))
        num_bins = 10
        df[f'{metric}_bin'] = pd.qcut(df[metric], q=num_bins, duplicates='drop')
        
        bin_stats = df.groupby(f'{metric}_bin', observed=False).agg(
            failure_rate=('failure', 'mean'),
            mean_uncertainty=(metric, 'mean'),
            count=('failure', 'count')
        ).reset_index()
        
        sns.scatterplot(x='mean_uncertainty', y='failure_rate', size='count', sizes=(50, 400), data=bin_stats, color='blue', alpha=0.7)
        sns.lineplot(x='mean_uncertainty', y='failure_rate', data=bin_stats, color='blue', alpha=0.5)
        
        plt.ylim(0, 1.1)
        plt.title(f'Failure Rate vs {metric} (Binned, First {limit} Steps)')
        plt.xlabel(f'Mean {metric} in Bin')
        plt.ylabel('Failure Rate')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'binned_failure_rate_{metric}.png'))
        plt.close()

    # 4. ROC Curves
    plt.figure(figsize=(10, 8))
    for metric in uncertainty_metrics:
        fpr, tpr, _ = roc_curve(df['failure'], df[metric])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, lw=2, label=f'{metric} (AUC = {roc_auc:.2f})')

    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve (First {limit} Steps): Predicting Failure')
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'roc_curve_all_metrics.png'))
    plt.close()

    # 5. Precision-Recall Curves
    plt.figure(figsize=(10, 8))
    for metric in uncertainty_metrics:
        precision, recall, _ = precision_recall_curve(df['failure'], df[metric])
        ap = average_precision_score(df['failure'], df[metric])
        plt.plot(recall, precision, lw=2, label=f'{metric} (AP = {ap:.2f})')

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Recall (Failure)')
    plt.ylabel('Precision (Failure)')
    plt.title(f'Precision-Recall Curve (First {limit} Steps): Predicting Failure')
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pr_curve_all_metrics.png'))
    plt.close()

    print(f"Successfully generated plots for first {limit} steps in {output_dir}")

for limit in [75, 100]:
    generate_plots_for_limit(limit)
