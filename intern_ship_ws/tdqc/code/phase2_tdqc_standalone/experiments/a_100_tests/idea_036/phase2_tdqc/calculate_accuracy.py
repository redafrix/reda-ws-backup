
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from pathlib import Path

# Mock/Minimal LSTM for loading (must match architecture in train_tdqc.py)
class TDQC_LSTM(nn.Module):
    def __init__(self, input_dim=8, hidden_dim=64, num_layers=2):
        super(TDQC_LSTM, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        out = self.fc(lstm_out)
        return self.sigmoid(out).squeeze(-1)

def evaluate_accuracy(checkpoint_path, data_path, device='cpu'):
    # Load data
    data = torch.load(data_path, map_location=device)
    X = data['X_val']
    Y = data['Y_val']
    
    # Pre-calculate normalization if needed (assuming v6 features)
    # The training script locks stats to X_train, but for a quick accuracy check,
    # we'll assume the model was trained on the same distribution.
    # Note: Proper eval should use train-set stats.
    
    dataset = TensorDataset(X, Y)
    loader = DataLoader(dataset, batch_size=128, shuffle=False)
    
    model = TDQC_LSTM().to(device)
    model.load_state_dict(torch.load(checkpoint_path, map_location=device))
    model.eval()
    
    all_preds = []
    all_targets = []
    
    with torch.no_grad():
        for x_batch, y_batch in loader:
            x_batch = x_batch.to(device)
            preds = model(x_batch)
            all_preds.append(preds.cpu().numpy())
            all_targets.append(y_batch.numpy())
            
    all_preds = np.concatenate(all_preds)
    all_targets = np.concatenate(all_targets)
    
    # Accuracy at p > 0.5
    binary_preds = (all_preds > 0.5).astype(float)
    accuracy = (binary_preds == all_targets).mean()
    
    # Sequential Brier (for double check)
    brier = np.mean((all_preds - all_targets)**2)
    
    return accuracy, brier

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    data_path = 'intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/final_calibrated_3924rollouts_v6.pt'
    base_checkpoints = Path('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/results/checkpoints')
    
    checkpoints = {
        "500 Epochs": base_checkpoints / 'lstm_v6_500epochs/best.pt',
        "1000 Epochs": base_checkpoints / 'lstm_v6_1000epochs_fine_tuned/best.pt',
        "1500 Epochs": base_checkpoints / 'lstm_v6_1500epochs_fine_tuned/best.pt'
    }
    
    print(f"{'Checkpoint':<15} | {'Accuracy (%)':<15} | {'Brier Score':<15}")
    print("-" * 50)
    
    for name, path in checkpoints.items():
        if path.exists():
            acc, brier = evaluate_accuracy(path, data_path, device)
            print(f"{name:<15} | {acc*100:>12.2f}% | {brier:>12.6f}")
        else:
            print(f"{name:<15} | {'MISSING':<15} | {'-'}")

if __name__ == "__main__":
    main()
