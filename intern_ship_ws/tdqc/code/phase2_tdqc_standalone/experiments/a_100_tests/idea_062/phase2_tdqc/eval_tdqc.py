from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np

import torch
from torch.utils.data import DataLoader

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", required=True)
    p.add_argument("--ckpt", required=True)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--device", default="cuda")
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

    total_brier = 0.0
    total_count = 0.0
    all_episode_scores = []
    all_episode_failures = []
    
    all_step_q_success = []
    all_step_q_failure = []

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])

        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count

        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            max_q = float(q[b, :L].max().item())
            all_episode_scores.append(max_q)
            is_fail = int(batch["failure"][b].item())
            all_episode_failures.append(is_fail)
            
            if is_fail:
                all_step_q_failure.extend(q[b, :L].cpu().numpy().tolist())
            else:
                all_step_q_success.extend(q[b, :L].cpu().numpy().tolist())

    all_episode_scores = np.array(all_episode_scores)
    all_episode_failures = np.array(all_episode_failures)

    print(f"sequential_brier={total_brier / max(total_count, 1.0):.6f}")

    success_scores = all_episode_scores[all_episode_failures == 0]
    failure_scores = all_episode_scores[all_episode_failures == 1]

    print(f"Episode Stats:")
    print(f"  Success: count={len(success_scores)}, mean_max_q={success_scores.mean():.4f}, std_max_q={success_scores.std():.4f}")
    print(f"  Failure: count={len(failure_scores)}, mean_max_q={failure_scores.mean():.4f}, std_max_q={failure_scores.std():.4f}")

    print(f"Step Stats:")
    print(f"  Success steps: mean_q={np.mean(all_step_q_success):.4f}, std_q={np.std(all_step_q_success):.4f}")
    print(f"  Failure steps: mean_q={np.mean(all_step_q_failure):.4f}, std_q={np.std(all_step_q_failure):.4f}")

    # Threshold analysis
    print("\nThreshold Analysis (Episode-level Accuracy):")
    print(f"{'Threshold':<10} | {'Accuracy':<10} | {'Precision':<10} | {'Recall':<10} | {'F1':<10}")
    print("-" * 60)
    for tau in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        preds = (all_episode_scores >= tau).astype(int)
        
        tp = ((preds == 1) & (all_episode_failures == 1)).sum()
        tn = ((preds == 0) & (all_episode_failures == 0)).sum()
        fp = ((preds == 1) & (all_episode_failures == 0)).sum()
        fn = ((preds == 0) & (all_episode_failures == 1)).sum()
        
        acc = (tp + tn) / len(all_episode_failures)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        
        print(f"{tau:<10.1f} | {acc:<10.4f} | {prec:<10.4f} | {rec:<10.4f} | {f1:<10.4f}")

    try:
        from sklearn.metrics import roc_auc_score
        auc = roc_auc_score(all_episode_failures, all_episode_scores)
        print(f"\nepisode_roc_auc={auc:.6f}")
    except Exception as e:
        print(f"Could not compute ROC-AUC: {e}")


if __name__ == "__main__":
    main()
