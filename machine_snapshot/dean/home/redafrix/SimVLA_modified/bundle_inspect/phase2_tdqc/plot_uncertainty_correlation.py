import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score

# Configuration
DATASET_PATH = "/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_denoise_clean_splits_20260504/combined_clean.jsonl"
OUTPUT_DIR = "/home/redafrix/SimVLA_modified/phase2_tdqc/plots_uncertainty_correlation"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
data = []
with open(DATASET_PATH, 'r') as f:
    for line in f:
        item = json.loads(line)
        # Flatten basic metrics
        row = {
            'success': item.get('success', 0),
            'mean_path_uncertainty': item.get('mean_path_uncertainty', 0),
            'max_path_uncertainty': item.get('max_path_uncertainty', 0),
            'mean_last_step_uncertainty': item.get('mean_last_step_uncertainty', 0),
            'max_last_step_uncertainty': item.get('max_last_step_uncertainty', 0),
            'steps': item.get('steps', 0)
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

# 1. Boxplots: Distribution of uncertainty for Success vs Failure
for metric in uncertainty_metrics:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='status', y=metric, data=df, palette={'Success': 'green', 'Failure': 'red'})
    plt.title(f'{metric} Distribution: Success vs Failure')
    plt.ylabel(metric)
    plt.xlabel('Episode Outcome')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'boxplot_{metric}.png'))
    plt.close()

# 2. KDE Plots (Density): Compare distributions
for metric in uncertainty_metrics:
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data=df, x=metric, hue='status', fill=True, palette={'Success': 'green', 'Failure': 'red'}, common_norm=False)
    plt.title(f'{metric} Density: Success vs Failure')
    plt.xlabel(metric)
    plt.ylabel('Density')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'kde_{metric}.png'))
    plt.close()

# 3. Reliability Diagram / Binned Failure Rates
# Divide uncertainty into bins and calculate failure rate in each bin
for metric in uncertainty_metrics:
    plt.figure(figsize=(8, 6))
    # Use quantiles for binning to ensure equal sized bins if possible, or regular bins
    num_bins = 10
    df[f'{metric}_bin'] = pd.qcut(df[metric], q=num_bins, duplicates='drop')
    
    # Calculate mean failure rate and mean uncertainty per bin
    bin_stats = df.groupby(f'{metric}_bin', observed=False).agg(
        failure_rate=('failure', 'mean'),
        mean_uncertainty=(metric, 'mean'),
        count=('failure', 'count')
    ).reset_index()
    
    # Plot
    sns.scatterplot(x='mean_uncertainty', y='failure_rate', size='count', sizes=(50, 400), data=bin_stats, color='blue', alpha=0.7)
    sns.lineplot(x='mean_uncertainty', y='failure_rate', data=bin_stats, color='blue', alpha=0.5)
    
    plt.ylim(0, 1.1)
    plt.title(f'Failure Rate vs {metric} (Binned)')
    plt.xlabel(f'Mean {metric} in Bin')
    plt.ylabel('Failure Rate')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'binned_failure_rate_{metric}.png'))
    plt.close()

# 4. ROC Curves: Uncertainty as a predictor of Failure
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
plt.title('ROC Curve: Predicting Failure using Uncertainty')
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'roc_curve_all_metrics.png'))
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
plt.title('Precision-Recall Curve: Predicting Failure using Uncertainty')
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'pr_curve_all_metrics.png'))
plt.close()

print(f"Successfully generated {len(uncertainty_metrics) * 3 + 2} plots in {OUTPUT_DIR}")
