from __future__ import annotations

import argparse
from pathlib import Path

import torch
from torch.utils.data import DataLoader

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator


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
    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"],
        hidden_dim=cfg["hidden_dim"],
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

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"])

        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count

        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            # Failure detection score: max predicted failure probability over the episode.
            all_episode_scores.append(float(q[b, :L].max().item()))
            all_episode_failures.append(int(batch["failure"][b].item()))

    print(f"sequential_brier={total_brier / max(total_count, 1.0):.6f}")

    try:
        from sklearn.metrics import roc_auc_score
        auc = roc_auc_score(all_episode_failures, all_episode_scores)
        print(f"episode_roc_auc={auc:.6f}")
    except Exception as e:
        print(f"Could not compute ROC-AUC: {e}")


if __name__ == "__main__":
    main()
