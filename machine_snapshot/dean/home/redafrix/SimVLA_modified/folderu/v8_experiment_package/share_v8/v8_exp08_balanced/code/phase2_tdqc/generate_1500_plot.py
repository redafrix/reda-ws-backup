
import json
import matplotlib.pyplot as plt
from pathlib import Path

def merge_and_plot_1500():
    base_path = Path('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/results/checkpoints')
    h1_path = base_path / 'lstm_v6_500epochs/history.json'
    h2_path = base_path / 'lstm_v6_1000epochs_fine_tuned/history.json'
    h3_path = base_path / 'lstm_v6_1500epochs_fine_tuned/history.json'
    
    with open(h1_path, 'r') as f: h1 = json.load(f)
    with open(h2_path, 'r') as f: h2 = json.load(f)
    with open(h3_path, 'r') as f: h3 = json.load(f)
    
    # Combined history
    full_history = h1 + h2 + h3
    
    epochs = [h['epoch'] for h in full_history]
    train_loss = [h['train_loss'] for h in full_history]
    val_brier = [h['val_seq_brier'] for h in full_history]
    
    fig, ax1 = plt.subplots(figsize=(12, 7))
    
    color = 'tab:blue'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Train Loss (TD Brier)', color=color)
    ax1.plot(epochs, train_loss, color=color, alpha=0.4, label='Raw Train Loss')
    
    # Simple moving average for loss
    window = 20
    if len(train_loss) > window:
        smoothed = [sum(train_loss[i:i+window])/window for i in range(len(train_loss)-window)]
        ax1.plot(epochs[window:], smoothed, color='blue', linewidth=2, label='Smoothed Loss')
    
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Val Sequential Brier', color=color)
    ax2.plot(epochs, val_brier, color=color, linewidth=2.5, label='Val Brier')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Markers for fine-tuning stages
    plt.axvline(x=500, color='gray', linestyle='--', alpha=0.7)
    plt.axvline(x=1000, color='gray', linestyle='--', alpha=0.7)
    
    plt.text(100, plt.ylim()[1]*0.9, 'Initial (LR 1e-4)', fontsize=10, fontweight='bold')
    plt.text(600, plt.ylim()[1]*0.9, 'Fine-Tune 1 (LR 2e-5)', fontsize=10, fontweight='bold')
    plt.text(1100, plt.ylim()[1]*0.9, 'Fine-Tune 2 (LR 2e-5)', fontsize=10, fontweight='bold')
    
    plt.title('TDQC v6 Full Training Trajectory (0 - 1500 Epochs)')
    fig.tight_layout()
    
    output_dir = Path('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/results/plots')
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_path = output_dir / 'v6_full_1500epochs_analysis.png'
    plt.savefig(plot_path)
    
    # Save merged history for future use
    merged_history_path = output_dir / 'v6_merged_history_1500.json'
    with open(merged_history_path, 'w') as f:
        json.dump(full_history, f, indent=2)
        
    print(f"Merged plot saved to {plot_path}")
    print(f"Merged history JSON saved to {merged_history_path}")

if __name__ == "__main__":
    merge_and_plot_1500()
