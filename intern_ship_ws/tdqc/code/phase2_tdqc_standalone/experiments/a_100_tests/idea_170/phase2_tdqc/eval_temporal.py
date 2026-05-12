from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import torch
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", required=True)
    p.add_argument("--ckpt", required=True)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--device", default="cuda")
    p.add_argument("--interval", type=int, default=20)
    return p.parse_args()


@torch.no_grad()
def main():
    args = parse_args()
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")

    dataset = TDQCDataset(args.dataset_path)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)

    ckpt = torch.load(args.ckpt, map_location="cpu")
    cfg = ckpt["config"]
    model = TDQCTransformerCalibrator(
        input_dim=cfg["input_dim"],
        hidden_dim=cfg["hidden_dim"],
        n_heads=cfg.get("n_heads", 8),
        num_layers=cfg["num_layers"],
        dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()

    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)

    # Storage for temporal analysis
    all_episode_data = []

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])
        
        q_cpu = q.cpu().numpy()
        f_cpu = batch["failure"].cpu().numpy()
        l_cpu = batch["lengths"].cpu().numpy()
        
        for b in range(q_cpu.shape[0]):
            L = int(l_cpu[b])
            all_episode_data.append({
                "q": q_cpu[b, :L],
                "failure": int(f_cpu[b])
            })

    if args.interval > 0:
        max_len = max(len(d["q"]) for d in all_episode_data)
        intervals = list(range(args.interval, max_len + args.interval, args.interval))
    else:
        # Custom steps for ultra-early analysis
        intervals = [1, 3, 5, 7, 10, 13, 16, 20]

    print(f"\nTemporal Analysis for: {Path(args.dataset_path).name}")
    print(f"{'Step':<6} | {'Acc (0.5)':<10} | {'AUC':<10} | {'n_episodes':<10}")
    print("-" * 45)

    for step in intervals:
        step_scores = []
        step_labels = []
        
        for d in all_episode_data:
            L = len(d["q"])
            # Use min(step, L) to allow evaluation even if episode is shorter than step
            # but for this specific request, we only care about episodes that reach the step
            if L < step:
                continue 
            
            # Max Q observed up to this step
            current_max_q = d["q"][:step].max()
            step_scores.append(current_max_q)
            step_labels.append(d["failure"])
            
        if len(step_scores) < 2:
            continue
            
        step_scores = np.array(step_scores)
        step_labels = np.array(step_labels)
        
        # Calculate Accuracy at 0.5 threshold
        preds = (step_scores >= 0.5).astype(int)
        acc = (preds == step_labels).mean()
        
        # Calculate AUC
        try:
            if len(np.unique(step_labels)) > 1:
                auc = roc_auc_score(step_labels, step_scores)
            else:
                auc = 1.0 if step_labels[0] == 1 and all(step_scores >= 0.5) else 0.0
                # If only one class, AUC is not well-defined, but we show status
        except:
            auc = np.nan
            
        print(f"{step:<6} | {acc:<10.4f} | {auc:<10.4f} | {len(step_scores):<10}")

if __name__ == "__main__":
    main()
