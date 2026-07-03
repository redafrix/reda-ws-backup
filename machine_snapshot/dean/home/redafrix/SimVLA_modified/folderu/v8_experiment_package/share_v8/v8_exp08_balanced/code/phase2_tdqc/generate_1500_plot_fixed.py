
import json
import matplotlib.pyplot as plt
from pathlib import Path

def merge_and_plot_1500_fixed():
    base_path = Path('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/results/checkpoints')
    h1_path = base_path / 'lstm_v6_500epochs/history.json'
    h2_path = base_path / 'lstm_v6_1000epochs_fine_tuned/history.json'
    h3_path = base_path / 'lstm_v6_1500epochs_fine_tuned/history.json'
    
    with open(h1_path, 'r') as f: h1 = json.load(f)
    with open(h2_path, 'r') as f: h2 = json.load(f)
    with open(h3_path, 'r') as f: h3 = json.load(f)
    
    # FILTER AND MERGE LOGIC
    # h1 is 0-499
    # h2 is 498-999 (Resume logic overlap)
    # h3 is 999-1499 (Resume logic overlap)
    
    h2_filtered = [entry for entry in h2 if entry['epoch'] >= 500]
    h3_filtered = [entry for entry in h3 if entry['epoch'] >= 1000]
    
    full_history = h1 + h2_filtered + h3_filtered
    
    epochs = [h['epoch'] for h in full_history]
    train_loss = [h['train_loss'] for h in full_history]
    val_brier = [h['val_seq_brier'] for h in full_history]
    
    # Check for gaps or overlaps in merged epochs
    for i in range(1, len(epochs)):
        if epochs[i] != epochs[i-1] + 1:
            print(f"WARNING: Epoch continuity broken at index {i}: {epochs[i-1]} -> {epochs[i]}")

    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    # 1. TRAIN LOSS
    color = 'tab:blue'
    ax1.set_xlabel('Epoch', fontsize=12)
    ax1.set_ylabel('Train Loss (TD-Brier)', color=color, fontsize=12)
    ax1.plot(epochs, train_loss, color=color, alpha=0.2, label='Raw Loss')
    
    window = 30
    if len(train_loss) > window:
        smoothed = [sum(train_loss[i:i+window])/window for i in range(len(train_loss)-window)]
        ax1.plot(epochs[window:], smoothed, color='blue', linewidth=2, label=f'Loss (SMA-{window})')
    
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.4)
    
    # 2. VALIDATION BRIER
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Val Sequential Brier Score', color=color, fontsize=12)
    ax2.plot(epochs, val_brier, color=color, linewidth=2.5, label='Val Brier')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # 3. BASELINES (for context)
    RANDOM_BASELINE = 0.250
    DATASET_MEAN = 0.207
    ax2.axhline(y=RANDOM_BASELINE, color='red', linestyle='--', alpha=0.6, label='Random (0.25)')
    ax2.axhline(y=DATASET_MEAN, color='green', linestyle='--', alpha=0.6, label='Mean Baseline (0.207)')
    
    # 4. ANNOTATIONS
    plt.axvline(x=500, color='black', linestyle='-', alpha=0.5)
    plt.axvline(x=1000, color='black', linestyle='-', alpha=0.5)
    
    y_max = max(val_brier) * 1.05
    ax2.text(250, y_max*0.95, 'PHASE 1\nLR: 1e-4', ha='center', fontweight='bold')
    ax2.text(750, y_max*0.95, 'PHASE 2 (Fine-Tune)\nLR: 2e-5', ha='center', fontweight='bold')
    ax2.text(1250, y_max*0.95, 'PHASE 3 (Deep Polish)\nLR: 2e-5', ha='center', fontweight='bold')
    
    # Final Metric Box
    final_val = val_brier[-1]
    best_val = min(val_brier)
    stats_text = f"Final Val Brier: {final_val:.4f}\nBest Val Brier: {best_val:.4f}\nTotal Epochs: {len(epochs)}"
    props = dict(boxstyle='round', facecolor='white', alpha=0.8)
    ax2.text(0.02, 0.05, stats_text, transform=ax2.transAxes, verticalalignment='bottom', bbox=props, fontsize=11)

    plt.title('TDQC v6 Comprehensive Convergence (0 - 1500 Epochs)\nImpact of Multi-Phase Fine-Tuning', fontsize=14)
    fig.tight_layout()
    
    output_dir = Path('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/results/plots')
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_path = output_dir / 'v6_final_1500_fixed.png'
    plt.savefig(plot_path)
    
    # Update the merged JSON with fixed continuity
    merged_history_path = output_dir / 'v6_merged_history_1500_fixed.json'
    with open(merged_history_path, 'w') as f:
        json.dump(full_history, f, indent=2)
        
    print(f"Fixed plot saved to {plot_path}")
    print(f"Fixed history JSON saved to {merged_history_path}")

if __name__ == "__main__":
    merge_and_plot_1500_fixed()
