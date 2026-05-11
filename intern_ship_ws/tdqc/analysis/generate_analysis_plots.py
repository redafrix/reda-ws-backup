import matplotlib.pyplot as plt
import re
import os
from pathlib import Path

# Dynamic paths
WS_ROOT = Path(__file__).parents[2]
log_path = WS_ROOT / 'outputs/runs/tdqc_calibrator/training.log'
output_dir = WS_ROOT / 'outputs/plots/tdqc_calibrator'
output_dir.mkdir(parents=True, exist_ok=True)
output_plot = output_dir / 'training_analysis.png'

epochs = []
train_losses = []
val_briers = []

# Regex to match: epoch=0000 train_loss=0.000928 val_seq_brier=0.245806 best=inf
pattern = re.compile(r'epoch=(\d+) train_loss=([\d.]+) val_seq_brier=([\d.]+) best=')

with open(log_path, 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            epochs.append(int(match.group(1)))
            train_losses.append(float(match.group(2)))
            val_briers.append(float(match.group(3)))

if not epochs:
    print("No data found in log file.")
    exit(1)

# Baselines
RANDOM_BASELINE = 0.250
DATASET_MEAN_BASELINE = 0.207 # Based on 29.3% failure rate
FINAL_TEST_BRIER = 0.1666

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Plot Training Loss
ax1.plot(epochs, train_losses, label='Train TD-Loss (Brier-TD)', color='tab:blue', alpha=0.8)
ax1.set_ylabel('Loss (TD-Bootstrapped Brier)')
ax1.set_title('TDQC Calibrator Training Analysis (LSTM-128)')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()

# Plot Validation Brier Score
ax2.plot(epochs, val_briers, label='Val Sequential Brier', color='tab:orange', linewidth=2)
ax2.axhline(y=RANDOM_BASELINE, color='red', linestyle='--', label='Baseline: Random (0.250)')
ax2.axhline(y=DATASET_MEAN_BASELINE, color='green', linestyle='--', label='Baseline: Dataset Mean (0.207)')
ax2.axhline(y=FINAL_TEST_BRIER, color='purple', linestyle=':', label=f'Final Test Brier: {FINAL_TEST_BRIER:.4f}')

ax2.set_xlabel('Epoch')
ax2.set_ylabel('Brier Score (Lower is better)')
ax2.set_ylim(0.15, 0.26)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper right')

# Text box for final summary
textstr = '\n'.join((
    f'Episodes: 3,751',
    f'Split: 70/15/15',
    f'Final Test Score: {FINAL_TEST_BRIER:.4f}',
    f'Improvement over Mean: {((DATASET_MEAN_BASELINE - FINAL_TEST_BRIER) / DATASET_MEAN_BASELINE * 100):.1f}%'
))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax2.text(0.05, 0.25, textstr, transform=ax2.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig(output_plot)
print(f"Plot saved to {output_plot}")
