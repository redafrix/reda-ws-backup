from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import torch
from torch.utils.data import DataLoader

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from phase2_tdqc.tdqc_losses import tdqc_brier_mc_loss, sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator


def parse_args():
    p = argparse.ArgumentParser()
    # Pre-split dataset paths (replaces the old --dataset_path + random_split approach)
    p.add_argument("--train_path", type=str, required=True)
    p.add_argument("--val_path",   type=str, required=True)
    p.add_argument("--test_path",  type=str, required=True)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--hidden_dim", type=int,   default=256)
    p.add_argument("--num_layers", type=int,   default=2)
    p.add_argument("--dropout",    type=float, default=0.05)
    p.add_argument("--batch_size", type=int,   default=64)
    p.add_argument("--epochs",     type=int,   default=500)
    p.add_argument("--lr",         type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--seed",       type=int,   default=0)
    p.add_argument("--device",     type=str,   default="cuda")
    p.add_argument("--resume_path", type=str,  default=None)
    p.add_argument("--early_stop_patience", type=int, default=40)
    return p.parse_args()


def move_batch(batch, device):
    return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}


@torch.no_grad()
def collect_train_stats(loader, device):
    all_valid_feats = []
    for batch in loader:
        feats = batch["features"]   # [B, T, F]
        mask  = batch["mask"]       # [B, T]
        all_valid_feats.append(feats[mask == 1.0])
    features = torch.cat(all_valid_feats, dim=0).to(device)
    dummy_mask = torch.ones(features.shape[0], device=device)
    return compute_feature_stats(features, dummy_mask)


@torch.no_grad()
def evaluate(model, loader, mean, std, device):
    model.eval()
    total_count = 0.0
    total_brier = 0.0
    for batch in loader:
        batch = move_batch(batch, device)
        x     = normalize_features(batch["features"], mean, std)
        q     = model(x, batch["lengths"], suite_ids=batch["suite_id"])
        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count
    return {"seq_brier": total_brier / max(total_count, 1.0)}


def main():
    args = parse_args()
    random.seed(args.seed)
    torch.manual_seed(args.seed)

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load the three pre-split datasets
    print("Loading datasets...")
    train_set = TDQCDataset(args.train_path)
    val_set   = TDQCDataset(args.val_path)
    test_set  = TDQCDataset(args.test_path)
    print(f"  train={len(train_set)}  val={len(val_set)}  test={len(test_set)}")
    print(f"  input_dim={train_set.input_dim}")

    train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True,
                              collate_fn=tdqc_collate, num_workers=4)
    val_loader   = DataLoader(val_set,   batch_size=args.batch_size, shuffle=False,
                              collate_fn=tdqc_collate, num_workers=2)
    test_loader  = DataLoader(test_set,  batch_size=args.batch_size, shuffle=False,
                              collate_fn=tdqc_collate, num_workers=2)

    # Class weights computed from training set only
    successes = sum(1 for ep in train_set.episodes if ep.success)
    failures  = len(train_set) - successes
    print(f"  train: successes={successes}  failures={failures}")
    success_rate   = successes / max(len(train_set), 1)
    failure_rate   = failures  / max(len(train_set), 1)
    success_weight = 0.5 / max(success_rate, 1e-6)
    fail_weight    = 0.5 / max(failure_rate, 1e-6)

    model = TDQCLSTMCalibrator(
        input_dim=train_set.input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)

    optim = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optim, mode="min", factor=0.5, patience=15
    )

    best_val    = float("inf")
    start_epoch = 0
    patience_counter = 0

    if args.resume_path:
        print(f"Resuming from {args.resume_path}...")
        ckpt = torch.load(args.resume_path, map_location=device)
        model.load_state_dict(ckpt["model"])
        mean = ckpt["mean"].to(device)
        std  = ckpt["std"].to(device)
        start_epoch = ckpt["epoch"] + 1
        best_val    = ckpt.get("val_seq_brier", float("inf"))
        print(f"  Resumed at epoch {start_epoch}, best_val={best_val:.6f}")
    else:
        print("Computing normalization stats from training set...")
        stats_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=False,
                                  collate_fn=tdqc_collate, num_workers=2)
        stats = collect_train_stats(stats_loader, device)
        mean  = stats["mean"].to(device)
        std   = stats["std"].to(device)
        print(f"  mean={mean.tolist()}")
        print(f"  std ={std.tolist()}")

    config = vars(args) | {
        "input_dim":      train_set.input_dim,
        "n_train":        len(train_set),
        "n_val":          len(val_set),
        "n_test":         len(test_set),
        "successes":      successes,
        "failures":       failures,
        "success_weight": success_weight,
        "fail_weight":    fail_weight,
    }
    (out_dir / "config.json").write_text(json.dumps(config, indent=2))

    history = []
    print("Starting training loop...")
    for epoch in range(start_epoch, args.epochs):
        model.train()
        running = 0.0
        denom   = 0

        for batch in train_loader:
            batch = move_batch(batch, device)
            x     = normalize_features(batch["features"], mean, std)
            q     = model(x, batch["lengths"], suite_ids=batch["suite_id"])
            loss  = tdqc_brier_mc_loss(
                q_online=q,
                failure=batch["failure"],
                mask=batch["mask"],
                fail_weight=fail_weight,
                success_weight=success_weight,
            )
            optim.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optim.step()
            running += loss.item()
            denom   += 1

        train_loss  = running / max(denom, 1)
        val_metrics = evaluate(model, val_loader, mean, std, device)
        val_brier   = val_metrics["seq_brier"]
        scheduler.step(val_brier)

        print(
            f"epoch={epoch:04d}  train_loss={train_loss:.6f}  "
            f"val_seq_brier={val_brier:.6f}  best={best_val:.6f}  "
            f"patience={patience_counter}/{args.early_stop_patience}"
        )

        history.append({"epoch": epoch, "train_loss": train_loss, "val_seq_brier": val_brier})
        (out_dir / "history.json").write_text(json.dumps(history, indent=2))

        ckpt = {
            "model":        model.state_dict(),
            "mean":         mean.detach().cpu(),
            "std":          std.detach().cpu(),
            "config":       config,
            "epoch":        epoch,
            "val_seq_brier": val_brier,
        }
        torch.save(ckpt, out_dir / "last.pt")
        
        if val_brier < best_val:
            best_val = val_brier
            patience_counter = 0
            torch.save(ckpt, out_dir / "best.pt")
        else:
            patience_counter += 1
            if patience_counter >= args.early_stop_patience:
                print(f"Early stopping at epoch {epoch}")
                break

    print(f"\nTraining Done. Best val sequential Brier: {best_val:.6f}")

    print("\n--- Final Test Evaluation ---")
    best_ckpt = torch.load(out_dir / "best.pt")
    model.load_state_dict(best_ckpt["model"])
    test_metrics = evaluate(model, test_loader, mean, std, device)
    print(f"Final Test Sequential Brier: {test_metrics['seq_brier']:.6f}")


if __name__ == "__main__":
    main()
