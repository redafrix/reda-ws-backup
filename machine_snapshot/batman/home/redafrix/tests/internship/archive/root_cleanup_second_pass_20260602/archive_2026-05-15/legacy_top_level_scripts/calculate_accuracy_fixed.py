
import argparse
import random
from pathlib import Path

import torch
import numpy as np
from torch.utils.data import DataLoader, random_split

# Import existing TDQC modules (assuming they are in the PYTHONPATH or current dir)
import sys
sys.path.append('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/code')

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

@torch.no_grad()
def calculate_metrics(model, loader, mean, std, device):
    model.eval()
    all_preds = []
    all_targets = []
    all_masks = []

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"]) # [B, T]
        
        all_preds.append(q.cpu().numpy())
        all_targets.append(batch["failure"].cpu().numpy())
        all_masks.append(batch["mask"].cpu().numpy())

    # Calculate Accuracy at p > 0.5 for all valid steps
    total_correct = 0
    total_steps = 0
    total_brier = 0.0

    for q, target, mask in zip(all_preds, all_targets, all_masks):
        # target is [B], q is [B, T], mask is [B, T]
        # We need to broadcast target to [B, T]
        target_expanded = np.expand_dims(target, axis=1) # [B, 1]
        
        # Binary prediction
        preds_binary = (q > 0.5).astype(float)
        
        # Masked comparison
        correct = (preds_binary == target_expanded) * mask
        total_correct += correct.sum()
        total_steps += mask.sum()
        
        # Brier score (sequential)
        total_brier += (np.square(q - target_expanded) * mask).sum()

    accuracy = total_correct / max(total_steps, 1)
    brier = total_brier / max(total_steps, 1)
    
    return accuracy, brier

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    dataset_path = 'intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/final_calibrated_3924rollouts_v6.pt'
    seed = 0
    
    # Reproduce the split used during training
    dataset = TDQCDataset(dataset_path)
    n_total = len(dataset)
    n_train = int(0.7 * n_total)
    n_val = int(0.15 * n_total)
    n_test = n_total - n_train - n_val
    
    train_set, val_set, test_set = random_split(
        dataset,
        [n_train, n_val, n_test],
        generator=torch.Generator().manual_seed(seed),
    )
    
    # Get normalization stats from train set (crucial for consistency)
    # We need to compute stats just like train_tdqc.py does
    train_loader = DataLoader(train_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    all_valid_feats = []
    for batch in train_loader:
        feats = batch["features"]
        mask = batch["mask"]
        all_valid_feats.append(feats[mask == 1.0])
    features = torch.cat(all_valid_feats, dim=0).to(device)
    mean = features.mean(dim=0)
    std = features.std(dim=0) + 1e-6
    
    val_loader = DataLoader(val_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    base_checkpoints = Path('intern_ship_ws/tdqc/code/phase2_tdqc_standalone/results/checkpoints')
    checkpoints = {
        "500 Epochs": base_checkpoints / 'lstm_v6_500epochs/best.pt',
        "1000 Epochs": base_checkpoints / 'lstm_v6_1000epochs_fine_tuned/best.pt',
        "1500 Epochs": base_checkpoints / 'lstm_v6_1500epochs_fine_tuned/best.pt'
    }
    
    print(f"{'Checkpoint':<15} | {'Val Accuracy (%)':<18} | {'Val Brier Score':<15}")
    print("-" * 55)
    
    for name, path in checkpoints.items():
        if path.exists():
            # Load model
            model = TDQCLSTMCalibrator(input_dim=dataset.input_dim, hidden_dim=128, num_layers=1).to(device)
            ckpt = torch.load(path, map_location=device)
            model.load_state_dict(ckpt['model'])
            
            acc, brier = calculate_metrics(model, val_loader, mean, std, device)
            print(f"{name:<15} | {acc*100:>15.2f}% | {brier:>15.6f}")
        else:
            print(f"{name:<15} | {'MISSING':>15} | {'-'}")

if __name__ == "__main__":
    main()
