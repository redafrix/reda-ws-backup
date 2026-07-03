
import json
import matplotlib.pyplot as plt
import sys
from pathlib import Path

def plot_history(history_path, output_dir):
    with open(history_path, 'r') as f:
        history = json.load(f)
    
    epochs = [h['epoch'] for h in history]
    train_loss = [h['train_loss'] for h in history]
    val_brier = [h['val_seq_brier'] for h in history]
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = 'tab:blue'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Train Loss (TD Brier)', color=color)
    ax1.plot(epochs, train_loss, color=color, label='Train Loss')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Val Sequential Brier', color=color)
    ax2.plot(epochs, val_brier, color=color, label='Val Brier')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('TDQC Training Curves (500 Epochs, v5 Dataset)')
    fig.tight_layout()
    
    plot_path = Path(output_dir) / 'training_curves.png'
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python plot_history.py <history_json> <output_dir>")
        sys.exit(1)
    plot_history(sys.argv[1], sys.argv[2])
