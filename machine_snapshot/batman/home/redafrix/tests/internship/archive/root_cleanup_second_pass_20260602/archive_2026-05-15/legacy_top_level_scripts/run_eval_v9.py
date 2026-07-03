import argparse
import torch
import numpy as np
from pathlib import Path
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score

import sys
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp01/code")
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

def evaluate_detailed(model, loader, mean, std, device, steps_to_check=[10, 12, 15, 50, 100, 150, 200, 300]):
    model.eval()
    
    # We need to collect step-wise max-pooled probabilities and ground truths
    # step -> {"probs": [], "targets": []}
    step_data = {s: {"probs": [], "targets": []} for s in steps_to_check}
    
    total_brier = 0.0
    total_count = 0.0
    
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            
            # Predict
            q = model(x, batch["lengths"]) # [B, T]
            
            targets = batch["failure"].cpu().numpy() # [B]
            masks = batch["mask"].cpu().numpy() # [B, T]
            q_np = q.cpu().numpy() # [B, T]
            
            # Overall Brier Score
            for b in range(len(targets)):
                target_b = targets[b]
                mask_b = masks[b]
                q_b = q_np[b]
                total_brier += np.sum(np.square(q_b - target_b) * mask_b)
                total_count += np.sum(mask_b)
            
            # Step-wise Horizon Max-Pooling
            for b in range(len(targets)):
                target_b = targets[b]
                L = int(batch["lengths"][b].item())
                
                for s in steps_to_check:
                    if L >= s: # Only evaluate episodes that reach this step
                        max_q = np.max(q_np[b, :s])
                        step_data[s]["probs"].append(max_q)
                        step_data[s]["targets"].append(target_b)

    print(f"Overall Sequential Brier Score: {total_brier / max(total_count, 1.0):.6f}")
    
    print("\nStep |  Acc (t=0.5)  |  Brier Score  |    AUC-ROC    |   N   ")
    print("-" * 65)
    
    for s in steps_to_check:
        probs = np.array(step_data[s]["probs"])
        targets = np.array(step_data[s]["targets"])
        
        if len(probs) == 0:
            print(f"{s:>4} | {'N/A':>13} | {'N/A':>13} | {'N/A':>13} | {0:>5}")
            continue
            
        acc = np.mean((probs > 0.5) == targets)
        brier = np.mean(np.square(probs - targets))
        
        try:
            auc = roc_auc_score(targets, probs)
        except ValueError:
            auc = float('nan') # E.g., only one class present
            
        if np.isnan(auc):
            auc_str = "N/A"
        else:
            auc_str = f"{auc:.6f}"
            
        print(f"{s:>4} | {acc:>12.2%} | {brier:>13.6f} | {auc_str:>13} | {len(probs):>5}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_path", required=True)
    parser.add_argument("--ckpt", required=True)
    parser.add_argument("--batch_size", type=int, default=64)
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print(f"Loading dataset from {args.test_path}...")
    dataset = TDQCDataset(args.test_path)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)

    print(f"Loading checkpoint from {args.ckpt}...")
    ckpt = torch.load(args.ckpt, map_location=device)
    cfg = ckpt["config"]
    
    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"],
        hidden_dim=cfg["hidden_dim"],
        num_layers=cfg["num_layers"],
        dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)

    print("Running evaluation...")
    evaluate_detailed(model, loader, mean, std, device)

if __name__ == "__main__":
    main()
