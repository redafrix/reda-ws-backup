import matplotlib.pyplot as plt
import re
import os
import numpy as np
from pathlib import Path
from scipy.signal import savgol_filter

# Dynamic paths
WS_ROOT = Path(__file__).parents[2]
log_paths = [
    WS_ROOT / 'outputs/runs/tdqc_calibrator/training.log',
    WS_ROOT / 'outputs/runs/tdqc_calibrator/fine_tuning.log',
    WS_ROOT / 'outputs/runs/tdqc_calibrator/final_stretch.log',
    WS_ROOT / 'outputs/runs/tdqc_calibrator/lstm_td0_final_polish/polish_pass.log'
]
output_dir = WS_ROOT / 'outputs/plots/tdqc_calibrator/lstm_td0_final_polish'
output_dir.mkdir(parents=True, exist_ok=True)
output_plot = output_dir / 'final_training_curve.png'

epochs = []
train_losses = []
val_briers = []

pattern = re.compile(r'epoch=(\d+) train_loss=([\d.]+) val_seq_brier=([\d.]+) best=')

def parse_log(path):
    if not os.path.exists(path):
        print(f"Warning: {path} not found.")
        return
    with open(path, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ep = int(match.group(1))
                if epochs and ep <= epochs[-1]:
                    continue
                epochs.append(ep)
                train_losses.append(float(match.group(2)))
                val_briers.append(float(match.group(3)))

for path in log_paths:
    parse_log(path)

if not epochs:
    print("No data found in log files.")
    exit(1)

RANDOM_BASELINE = 0.250
DATASET_MEAN_BASELINE = 0.207 
FINAL_TEST_BRIER = 0.084363

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot Training Loss
ax1.plot(epochs, train_losses, label='Train TD-Loss', color='tab:blue', alpha=0.3)
if len(train_losses) > 51:
    smoothed_loss = savgol_filter(train_losses, 51, 3)
    ax1.plot(epochs, smoothed_loss, color='blue', linewidth=2, label='Smoothed Loss')

ax1.set_ylabel('Loss (Brier-TD)')
ax1.set_title(f'Comprehensive TDQC Calibration Training (1,300 Epochs)')
ax1.axvline(x=200, color='gray', linestyle='--', alpha=0.5)
ax1.axvline(x=700, color='gray', linestyle='--', alpha=0.5)
ax1.axvline(x=1000, color='gray', linestyle='--', alpha=0.5)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()

# Plot Validation Brier Score
ax2.plot(epochs, val_briers, label='Val Sequential Brier', color='tab:orange', linewidth=2)
ax2.axhline(y=RANDOM_BASELINE, color='red', linestyle='--', label='Baseline: Random (0.250)')
ax2.axhline(y=DATASET_MEAN_BASELINE, color='green', linestyle='--', label='Baseline: Dataset Mean (0.207)')
ax2.axhline(y=FINAL_TEST_BRIER, color='purple', linestyle=':', label=f'Final Test Brier: {FINAL_TEST_BRIER:.4f}')

ax2.set_xlabel('Epoch')
ax2.set_ylabel('Brier Score')
ax2.set_ylim(0.07, 0.26)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper right')

# Annotate milestones
ax2.text(50, 0.23, 'Stage 1: Initial', rotation=0, fontweight='bold')
ax2.text(350, 0.16, 'Stage 2: Fine-Tune', rotation=0, fontweight='bold')
ax2.text(750, 0.11, 'Stage 3: Stretch', rotation=0, fontweight='bold')
ax2.text(1050, 0.09, 'Stage 4: Polish', rotation=0, fontweight='bold')

textstr = '\n'.join((
    f'Final Epoch: {epochs[-1]}',
    f'Final Test Brier: {FINAL_TEST_BRIER:.4f}',
    f'Step 100 Brier: 0.1063',
    f'Step 50 Accuracy: 80.7%',
    f'Improvement vs Mean: {((DATASET_MEAN_BASELINE - FINAL_TEST_BRIER) / DATASET_MEAN_BASELINE * 100):.1f}%'
))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax2.text(0.02, 0.25, textstr, transform=ax2.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig(output_plot)
print(f"Plot saved to {output_plot}")
