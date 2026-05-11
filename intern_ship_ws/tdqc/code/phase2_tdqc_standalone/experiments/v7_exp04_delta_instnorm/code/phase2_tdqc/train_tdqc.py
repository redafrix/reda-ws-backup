from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import torch
from torch.utils.data import DataLoader, random_split

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from phase2_tdqc.tdqc_losses import tdqc_brier_td_loss, sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator, hard_update


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", type=str, default="data/v7_22d/v7_22d_train.pt")
    p.add_argument("--val_path", type=str, default="data/v7_22d/v7_22d_val.pt")
    p.add_argument("--test_path", type=str, default="data/v7_22d/v7_22d_test.pt")
    p.add_argument("--output_dir", type=str, default="experiments/v7_exp04_delta_instnorm/outputs")
    p.add_argument("--input_dim", type=int, default=22)
    p.add_argument("--hidden_dim", type=int, default=128)
    p.add_argument("--num_layers", type=int, default=1)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--epochs", type=int, default=500)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--target_update_freq", type=int, default=100)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument("--resume_path", type=str, default=None, help="Path to checkpoint to resume from")
    p.add_argument("--early_stop_patience", type=int, default=40)
    return p.parse_args()


def move_batch(batch, device):
    return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}


@torch.no_grad()
def collect_train_stats(loader, device):
    all_valid_feats = []
    for batch in loader:
        feats = batch["features"]  # [B, T, F]
        mask = batch["mask"]      # [B, T]
        
        # Only keep steps where mask == 1
        valid_feats = feats[mask == 1.0] # [N_valid_steps, F]
        all_valid_feats.append(valid_feats)
        
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
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"])
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

    print(f"Loading datasets...")
    train_set = TDQCDataset(args.dataset_path)
    val_set = TDQCDataset(args.val_path)
    test_set = TDQCDataset(args.test_path)
    print(f"Loaded {len(train_set)} train, {len(val_set)} val, {len(test_set)} test episodes.")
    
    print("DEBUG: Creating DataLoaders...")
    train_loader = DataLoader(
        train_set,
        batch_size=args.batch_size,
        shuffle=True,
        collate_fn=tdqc_collate,
        num_workers=0,
    )
    val_loader = DataLoader(
        val_set,
        batch_size=args.batch_size,
        shuffle=False,
        collate_fn=tdqc_collate,
        num_workers=0,
    )
    test_loader = DataLoader(
        test_set,
        batch_size=args.batch_size,
        shuffle=False,
        collate_fn=tdqc_collate,
        num_workers=0,
    )

    # Class weights.
    print("DEBUG: Computing class weights...")
    # Use train_set for weights
    successes = sum(int(ep.success) for ep in train_set.episodes)
    failures = len(train_set) - successes
    print(f"DEBUG: total successes={successes}, failures={failures}")
    success_rate = successes / max(len(train_set), 1)
    failure_rate = failures / max(len(train_set), 1)
    success_weight = 0.5 / max(success_rate, 1e-6)
    fail_weight = 0.5 / max(failure_rate, 1e-6)

    print("DEBUG: Initializing model...")
    model = TDQCLSTMCalibrator(
        input_dim=args.input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)
    target_model = TDQCLSTMCalibrator(
        input_dim=args.input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)
    hard_update(target_model, model)
    target_model.eval()

    optim = torch.optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=args.weight_decay,
    )
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optim, mode="min", factor=0.5, patience=15
    )

    global_step = 0
    best_val = float("inf")
    start_epoch = 0
    patience_counter = 0

    if args.resume_path:
        print(f"Resuming from {args.resume_path}...")
        ckpt = torch.load(args.resume_path, map_location=device)
        model.load_state_dict(ckpt["model"])
        target_model.load_state_dict(ckpt["target_model"])
        mean = ckpt["mean"].to(device)
        std = ckpt["std"].to(device)
        start_epoch = ckpt["epoch"] + 1
        best_val = ckpt.get("val_seq_brier", float("inf"))
        print(f"Resuming at epoch {start_epoch} with best_val={best_val:.6f}")
    else:
        print("DEBUG: Collecting training statistics for normalization...")
        mean_std_loader = DataLoader(
            train_set,
            batch_size=args.batch_size,
            shuffle=False,
            collate_fn=tdqc_collate,
            num_workers=0,
        )
        stats = collect_train_stats(mean_std_loader, device)
        mean = stats["mean"].to(device)
        std = stats["std"].to(device)
        print("DEBUG: Statistics collected.")

    config = vars(args) | {
        "input_dim": args.input_dim,
        "n_train": len(train_set),
        "n_val": len(val_set),
        "n_test": len(test_set),
        "successes": successes,
        "failures": failures,
        "success_weight": success_weight,
        "fail_weight": fail_weight,
    }
    (out_dir / "config.json").write_text(json.dumps(config, indent=2))

    history = []
    print("DEBUG: Starting training loop...")
    for epoch in range(start_epoch, args.epochs):
        model.train()
        running = 0.0
        denom = 0

        for batch in train_loader:
            batch = move_batch(batch, device)
            x = normalize_features(batch["features"], mean, std)

            q_online = model(x, batch["lengths"])
            with torch.no_grad():
                q_target = target_model(x, batch["lengths"])

            loss = tdqc_brier_td_loss(
                q_online=q_online,
                q_target=q_target,
                failure=batch["failure"],
                lengths=batch["lengths"],
                mask=batch["mask"],
                fail_weight=fail_weight,
                success_weight=success_weight,
            )

            optim.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optim.step()

            global_step += 1
            if global_step % args.target_update_freq == 0:
                hard_update(target_model, model)
                target_model.eval()

            running += loss.item()
            denom += 1

        train_loss = running / max(denom, 1)
        val_metrics = evaluate(model, val_loader, mean, std, device)
        val_brier = val_metrics["seq_brier"]
        scheduler.step(val_brier)

        print(
            f"epoch={epoch:04d} train_loss={train_loss:.6f} "
            f"val_seq_brier={val_brier:.6f} best={best_val:.6f} patience={patience_counter}/{args.early_stop_patience}"
        )

        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "val_seq_brier": val_brier,
        })
        (out_dir / "history.json").write_text(json.dumps(history, indent=2))

        ckpt = {
            "model": model.state_dict(),
            "target_model": target_model.state_dict(),
            "mean": mean.detach().cpu(),
            "std": std.detach().cpu(),
            "config": config,
            "epoch": epoch,
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

    print(f"Training Done. Best val sequential Brier: {best_val:.6f}")
    
    # Final Evaluation on Test Set
    print("\n--- Final Test Evaluation ---")
    best_ckpt = torch.load(out_dir / "best.pt")
    model.load_state_dict(best_ckpt["model"])
    test_metrics = evaluate(model, test_loader, mean, std, device)
    print(f"Final Test Sequential Brier: {test_metrics['seq_brier']:.6f}")


if __name__ == "__main__":
    main()
