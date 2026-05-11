import argparse
import torch
import random
import numpy as np
from torch.utils.data import DataLoader
from pathlib import Path
from tqdm import tqdm

# Local imports
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score
from tdqc_model import TDQCMambaCalibrator

def move_batch(batch, device):
    return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}

@torch.no_grad()
def evaluate(model, loader, mean, std, device, shuffle_time=False):
    model.eval()
    total_count = 0.0
    total_brier = 0.0

    for batch in loader:
        batch = move_batch(batch, device)
        features = batch["features"]
        mask = batch["mask"]
        
        if shuffle_time:
            # Shuffle along T dimension for each batch item independently
            for b in range(features.shape[0]):
                T = int(batch["lengths"][b].item())
                idx = torch.randperm(T)
                features[b, :T] = features[b, idx]
        
        x = normalize_features(features, mean, std)
        q = model(x)
        brier = sequential_brier_score(q, batch["failure"], mask)
        count = mask.sum().item()
        total_brier += brier.item() * count
        total_count += count

    return total_brier / max(total_count, 1.0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"Loading checkpoint from {args.ckpt}...")
    ckpt = torch.load(args.ckpt, map_location=device)
    
    config = ckpt["config"]
    model = TDQCMambaCalibrator(
        input_dim=config["input_dim"],
        hidden_dim=config["hidden_dim"],
        num_layers=config["num_layers"],
        d_state=config.get("d_state", 16),
        d_conv=config.get("d_conv", 4),
        expand=config.get("expand", 2),
    ).to(device)
    model.load_state_dict(ckpt["model"])
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)

    # All 22D OOD candidates
    ood_datasets = [
        "../../data/v7_22d/v7_22d_ood.pt",
        "../../data/v8_balanced/v8_unseen_obj_ood.pt",
        "../../data/goal_object_ood/v7_22d_ood.pt",
        "../../data/libero_object_object_new/v7_22d_ood.pt",
    ]

    print("\n" + "="*50)
    print("      COMPREHENSIVE OOD & CAUSALITY AUDIT")
    print("="*50)
    
    for ds_path in ood_datasets:
        if not Path(ds_path).exists():
            continue
            
        print(f"\nEvaluating: {ds_path}")
        dataset = TDQCDataset(ds_path)
        loader = DataLoader(dataset, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
        
        # Standard Eval
        brier_std = evaluate(model, loader, mean, std, device, shuffle_time=False)
        print(f"  [Standard] Sequential Brier: {brier_std:.6f}")
        
        # Causal Integrity (Shuffle) Eval
        brier_shuf = evaluate(model, loader, mean, std, device, shuffle_time=True)
        print(f"  [Shuffled] Sequential Brier: {brier_shuf:.6f}")
        
        # Analysis
        delta = brier_shuf - brier_std
        if abs(delta) < 1e-4:
            print("  RESULT: No temporal dependence detected. Model is likely using instantaneous features.")
        else:
            print(f"  RESULT: Temporal dependence confirmed. Delta: {delta:+.6f}")

    print("\n" + "="*50)

if __name__ == "__main__":
    main()
