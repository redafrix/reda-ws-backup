
import argparse
import random
from pathlib import Path
import torch
import numpy as np
from torch.utils.data import DataLoader, random_split

# Import existing TDQC modules
import sys
# Dynamic root discovery
WS_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(WS_ROOT / 'code'))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

@torch.no_grad()
def calculate_metrics(model, loader, mean, std, device, fixed_horizons=[50, 100]):
    model.eval()
    
    total_correct = 0
    total_steps = 0
    total_brier_seq = 0.0
    
    horizon_brier = {h: 0.0 for h in fixed_horizons}
    horizon_counts = {h: 0 for h in fixed_horizons}

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"]) # [B, T]
        
        target = batch["failure"] # [B]
        mask = batch["mask"] # [B, T]
        
        target_expanded = target.unsqueeze(1) # [B, 1]
        
        # Binary prediction (Accuracy)
        preds_binary = (q > 0.5).float()
        correct = (preds_binary == target_expanded) * mask
        total_correct += correct.sum().item()
        total_steps += mask.sum().item()
        
        # Brier score (sequential)
        total_brier_seq += (torch.square(q - target_expanded) * mask).sum().item()
        
        # Fixed Horizons
        for h in fixed_horizons:
            # We check if the rollout has at least h steps
            # lengths is [B]
            h_mask = (batch["lengths"] >= h)
            if h_mask.any():
                # Get the prediction at step h-1 (0-indexed)
                q_h = q[h_mask, h-1]
                t_h = target[h_mask]
                horizon_brier[h] += torch.square(q_h - t_h).sum().item()
                horizon_counts[h] += h_mask.sum().item()

    accuracy = total_correct / max(total_steps, 1)
    brier_seq = total_brier_seq / max(total_steps, 1)
    
    results = {
        "accuracy": accuracy,
        "brier_seq": brier_seq
    }
    
    for h in fixed_horizons:
        results[f"brier_{h}"] = horizon_brier[h] / max(horizon_counts[h], 1)
        
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument("--checkpoint_path", type=str, required=True)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device if torch.cuda.is_available() else 'cpu')
    
    # Reproduce the split used during training
    dataset = TDQCDataset(args.dataset_path)
    n_total = len(dataset)
    n_train = int(0.7 * n_total)
    n_val = int(0.15 * n_total)
    n_test = n_total - n_train - n_val
    
    train_set, val_set, test_set = random_split(
        dataset,
        [n_train, n_val, n_test],
        generator=torch.Generator().manual_seed(args.seed),
    )
    
    # Get normalization stats from train set
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
    
    ckpt_path = Path(args.checkpoint_path)
    if not ckpt_path.exists():
        print(f"Error: Checkpoint {ckpt_path} not found.")
        return

    # Load model
    model = TDQCLSTMCalibrator(input_dim=dataset.input_dim, hidden_dim=128, num_layers=1).to(device)
    ckpt = torch.load(ckpt_path, map_location=device)
    
    # Handle both wrapped and unwrapped state dicts
    if 'model' in ckpt:
        model.load_state_dict(ckpt['model'])
    else:
        model.load_state_dict(ckpt)
    
    metrics = calculate_metrics(model, val_loader, mean, std, device)
    
    print(f"Results for {ckpt_path.parent.name}:")
    print(f"  Accuracy:  {metrics['accuracy']*100:.2f}%")
    print(f"  Brier Seq: {metrics['brier_seq']:.6f}")
    print(f"  Brier 50:  {metrics['brier_50']:.6f}")
    print(f"  Brier 100: {metrics['brier_100']:.6f}")

if __name__ == "__main__":
    main()
