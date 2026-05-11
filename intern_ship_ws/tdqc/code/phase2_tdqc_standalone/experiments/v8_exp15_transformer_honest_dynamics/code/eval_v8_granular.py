from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import torch
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score, brier_score_loss

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", required=True)
    p.add_argument("--ckpt", required=True)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--device", default="cuda")
    p.add_argument("--task_id", type=int, default=None)
    return p.parse_args()


@torch.no_grad()
def main():
    args = parse_args()
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")

    dataset = TDQCDataset(args.dataset_path)
    
    # Filter by Task ID if requested
    if args.task_id is not None:
        filtered_episodes = [ep for ep in dataset.episodes if int(ep.task_id) == args.task_id]
        if not filtered_episodes:
            print(f"ERROR: No episodes found for Task ID {args.task_id}")
            return
        dataset.episodes = filtered_episodes
        print(f"Filtered to Task ID {args.task_id}: {len(dataset)} episodes.")

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

    # Steps to evaluate: Granular request
    eval_steps = [10, 12, 15, 50, 100, 150, 200, 300, "overall"]
    
    results = {}

    for step in eval_steps:
        step_scores = []
        step_labels = []
        
        for d in all_episode_data:
            L = len(d["q"])
            
            if step == "overall":
                # For overall, we take the max probability observed throughout the entire episode
                score = d["q"].max()
            else:
                # For specific steps, we only evaluate episodes that reach that step
                if L < int(step):
                    continue
                # Predict failure if ANY step up to the current horizon indicates failure (Max-pool proactivity)
                score = d["q"][:int(step)].max()
            
            step_scores.append(score)
            step_labels.append(d["failure"])
            
        if len(step_scores) < 2:
            results[step] = None
            continue
            
        scores = np.array(step_scores)
        labels = np.array(step_labels)
        
        # Accuracy at 0.5
        preds = (scores >= 0.5).astype(int)
        acc = (preds == labels).mean()
        
        # Brier Score
        brier = brier_score_loss(labels, scores)
        
        # AUC-ROC
        try:
            if len(np.unique(labels)) > 1:
                auc = roc_auc_score(labels, scores)
            else:
                auc = np.nan
        except:
            auc = np.nan
            
        results[step] = {
            "acc": acc,
            "brier": brier,
            "auc": auc,
            "n": len(scores)
        }

    # Print Table
    name = Path(args.dataset_path).name
    if args.task_id is not None:
        name += f" (Task {args.task_id})"
        
    print(f"\nResults for {name}")
    print(f"{'Step':<10} | {'Acc':<8} | {'Brier':<8} | {'AUC':<8} | {'N':<6}")
    print("-" * 50)
    for step in eval_steps:
        res = results[step]
        if res is None:
            print(f"{str(step):<10} | {'N/A':<8} | {'N/A':<8} | {'N/A':<8} | {'0':<6}")
        else:
            print(f"{str(step):<10} | {res['acc']:.4f} | {res['brier']:.4f} | {res['auc']:.4f} | {res['n']}")


if __name__ == "__main__":
    main()
