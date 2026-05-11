import matplotlib.pyplot as plt
import re
import os
from pathlib import Path

# Dynamic paths
WS_ROOT = Path(__file__).parents[2]
log_path_1 = WS_ROOT / 'outputs/runs/tdqc_calibrator/training.log'
log_path_2 = WS_ROOT / 'outputs/runs/tdqc_calibrator/fine_tuning.log'
output_dir = WS_ROOT / 'outputs/plots/tdqc_calibrator'
output_dir.mkdir(parents=True, exist_ok=True)
output_plot = output_dir / 'full_training_700_analysis.png'

epochs = []
train_losses = []
val_briers = []

# Regex to match: epoch=0000 train_loss=0.000928 val_seq_brier=0.245806 best=inf
pattern = re.compile(r'epoch=(\d+) train_loss=([\d.]+) val_seq_brier=([\d.]+) best=')

def parse_log(path):
    with open(path, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ep = int(match.group(1))
                # Avoid duplicates if resuming at the same epoch
                if epochs and ep <= epochs[-1]:
                    continue
                epochs.append(ep)
                train_losses.append(float(match.group(2)))
                val_briers.append(float(match.group(3)))

parse_log(log_path_1)
parse_log(log_path_2)

if not epochs:
    print("No data found in log files.")
    exit(1)

# Baselines
RANDOM_BASELINE = 0.250
DATASET_MEAN_BASELINE = 0.207 
FINAL_TEST_BRIER = 0.09955

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot Training Loss
ax1.plot(epochs, train_losses, label='Train TD-Loss', color='tab:blue', alpha=0.6)
# Smoothing for better visualization
from scipy.signal import savgol_filter
if len(train_losses) > 31:
    smoothed_loss = savgol_filter(train_losses, 31, 3)
    ax1.plot(epochs, smoothed_loss, color='blue', linewidth=2, label='Smoothed Loss')

ax1.set_ylabel('Loss (Brier-TD)')
ax1.set_title(f'Full 700-Epoch TDQC Calibration Analysis')
ax1.axvline(x=200, color='gray', linestyle='--', alpha=0.5, label='Fine-tuning Resume (LR 1e-4 -> 5e-5)')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()

# Plot Validation Brier Score
ax2.plot(epochs, val_briers, label='Val Sequential Brier', color='tab:orange', linewidth=2)
ax2.axhline(y=RANDOM_BASELINE, color='red', linestyle='--', label='Baseline: Random (0.250)')
ax2.axhline(y=DATASET_MEAN_BASELINE, color='green', linestyle='--', label='Baseline: Dataset Mean (0.207)')
ax2.axhline(y=FINAL_TEST_BRIER, color='purple', linestyle=':', label=f'Final Test Brier: {FINAL_TEST_BRIER:.4f}')

ax2.set_xlabel('Epoch')
ax2.set_ylabel('Brier Score')
ax2.set_ylim(0.08, 0.26)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper right')

# Highlight the fine-tuning improvement
ax2.annotate('Fine-tuning Phase', xy=(450, 0.13), xytext=(500, 0.18),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, fontweight='bold')

# Text box for final summary
textstr = '\n'.join((
    f'Final Epoch: {epochs[-1]}',
    f'Total Episodes: 3,751',
    f'Final Test Brier: {FINAL_TEST_BRIER:.4f}',
    f'Rel. Improvement: {((DATASET_MEAN_BASELINE - FINAL_TEST_BRIER) / DATASET_MEAN_BASELINE * 100):.1f}%'
))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax2.text(0.02, 0.15, textstr, transform=ax2.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig(output_plot)
print(f"Plot saved to {output_plot}")
