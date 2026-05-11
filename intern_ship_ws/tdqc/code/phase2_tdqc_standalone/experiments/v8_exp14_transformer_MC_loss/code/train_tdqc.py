from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from phase2_tdqc.tdqc_losses import tdqc_brier_td_loss, sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator, hard_update


class EarlyStopping:
    def __init__(self, patience=20, min_delta=1e-4):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = None
        self.early_stop = False

    def __call__(self, val_loss):
        if self.best_loss is None:
            self.best_loss = val_loss
        elif val_loss > self.best_loss - self.min_delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_loss = val_loss
            self.counter = 0


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", type=str, required=True)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--hidden_dim", type=int, default=256)
    p.add_argument("--num_layers", type=int, default=4)
    p.add_argument("--n_heads", type=int, default=8)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--epochs", type=int, default=200)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--warmup_epochs", type=int, default=5)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--target_update_freq", type=int, default=100)
    p.add_argument("--train_ratio", type=float, default=0.7)
    p.add_argument("--val_ratio", type=float, default=0.15)
    p.add_argument("--test_ratio", type=float, default=0.15)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument("--resume_path", type=str, default=None, help="Path to checkpoint to resume from")
    p.add_argument("--patience", type=int, default=20)
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
        q = model(x, mask=batch["mask"])
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
    print(f"Using device: {device}", flush=True)
    out_dir = Path(args.output_dir)
    
    if out_dir.exists() and not args.resume_path:
        # Check if it contains any significant files
        if (out_dir / "best.pt").exists() or (out_dir / "history.json").exists():
            print(f"FATAL ERROR: Output directory {args.output_dir} already exists and contains model artifacts (best.pt or history.json).", flush=True)
            print("Aborting to prevent catastrophic overwrite. Please use a different --output_dir.", flush=True)
            return

    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading dataset from {args.dataset_path}...", flush=True)
    dataset = TDQCDataset(args.dataset_path)
    n_total = len(dataset)
    print(f"Loaded {n_total} episodes.", flush=True)
    
    # Split sizes
    n_train = int(args.train_ratio * n_total)
    n_val = int(args.val_ratio * n_total)
    n_test = n_total - n_train - n_val
    print(f"Split sizes: {n_train} train, {n_val} val, {n_test} test.", flush=True)

    print("DEBUG: Splitting dataset...", flush=True)
    train_set, val_set, test_set = random_split(
        dataset,
        [n_train, n_val, n_test],
        generator=torch.Generator().manual_seed(args.seed),
    )

    print("DEBUG: Creating DataLoaders...", flush=True)
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
    print("DEBUG: Computing class weights...", flush=True)
    successes = sum(int(dataset[i].success) for i in range(len(dataset)))
    failures = len(dataset) - successes
    print(f"DEBUG: total successes={successes}, failures={failures}", flush=True)
    success_rate = successes / max(len(dataset), 1)
    failure_rate = failures / max(len(dataset), 1)
    success_weight = 0.5 / max(success_rate, 1e-6)
    fail_weight = 0.5 / max(failure_rate, 1e-6)

    print("DEBUG: Initializing model...", flush=True)
    model = TDQCTransformerCalibrator(
        input_dim=dataset.input_dim,
        hidden_dim=args.hidden_dim,
        n_heads=args.n_heads,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)

    # Fixed: Revert to standard AdamW
    optim = torch.optim.AdamW(
        model.parameters(), 
        lr=args.lr, 
        weight_decay=args.weight_decay
    )
    
    # Linear Warmup + Plateau
    def lr_lambda(epoch):
        if epoch < args.warmup_epochs:
            return (epoch + 1) / args.warmup_epochs
        return 1.0
    
    warmup_scheduler = torch.optim.lr_scheduler.LambdaLR(optim, lr_lambda)
    plateau_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optim, mode="min", factor=0.5, patience=15, verbose=False
    )
    early_stopping = EarlyStopping(patience=args.patience, min_delta=1e-4)

    global_step = 0
    best_val = float("inf")
    start_epoch = 0

    if args.resume_path:
        print(f"Resuming from {args.resume_path}...", flush=True)
        ckpt = torch.load(args.resume_path, map_location=device)
        model.load_state_dict(ckpt["model"])
        # Removed target_model reference for MC loss
        mean = ckpt["mean"].to(device)
        std = ckpt["std"].to(device)
        start_epoch = ckpt["epoch"] + 1
        best_val = ckpt.get("val_seq_brier", float("inf"))
        print(f"Resuming at epoch {start_epoch} with best_val={best_val:.6f}", flush=True)
    else:
        print("DEBUG: Collecting training statistics for normalization...", flush=True)
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
        print("DEBUG: Statistics collected.", flush=True)

    config = vars(args) | {
        "input_dim": dataset.input_dim,
        "n_total": n_total,
        "n_train": n_train,
        "n_val": n_val,
        "n_test": n_test,
        "successes": successes,
        "failures": failures,
        "success_weight": success_weight,
        "fail_weight": fail_weight,
    }
    (out_dir / "config.json").write_text(json.dumps(config, indent=2))

    history = []
    print("DEBUG: Starting training loop...", flush=True)
    for epoch in range(start_epoch, args.epochs):
        model.train()
        running = 0.0
        denom = 0

        for batch in train_loader:
            batch = move_batch(batch, device)
            x = normalize_features(batch["features"], mean, std)

            # --- RANDOM TRUNCATION HACK ---
            # Randomly chop off the end of the sequence 50% of the time to force early prediction
            B, T, F = x.shape
            if T > 50 and random.random() < 0.5:
                # Pick a random cut point between 30% and 90% of the sequence
                cut_point = random.randint(int(T * 0.3), int(T * 0.9))
                
                # Truncate the inputs and masks
                x = x[:, :cut_point, :]
                batch["mask"] = batch["mask"][:, :cut_point]
                
                # Update lengths (cap them at the cut point)
                batch["lengths"] = torch.clamp(batch["lengths"], max=cut_point)
            # ------------------------------

            q_online = model(x, mask=batch["mask"])

            from phase2_tdqc.tdqc_losses import tdqc_mc_brier_loss
            loss = tdqc_mc_brier_loss(
                q_online=q_online,
                failure=batch["failure"],
                mask=batch["mask"],
                fail_weight=fail_weight,
                success_weight=success_weight,
            )

            optim.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optim.step()

            global_step += 1
            running += loss.item()
            denom += 1

        train_loss = running / max(denom, 1)
        val_metrics = evaluate(model, val_loader, mean, std, device)
        val_brier = val_metrics["seq_brier"]
        
        if epoch < args.warmup_epochs:
            warmup_scheduler.step()
        else:
            plateau_scheduler.step(val_brier)

        print(
            f"epoch={epoch:04d} lr={optim.param_groups[0]['lr']:.2e} "
            f"train_loss={train_loss:.6f} val_seq_brier={val_brier:.6f} "
            f"best={best_val:.6f} patience={early_stopping.counter}/{early_stopping.patience}",
            flush=True
        )

        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "val_seq_brier": val_brier,
        })
        (out_dir / "history.json").write_text(json.dumps(history, indent=2))

        ckpt = {
            "model": model.state_dict(),
            "mean": mean.detach().cpu(),
            "std": std.detach().cpu(),
            "config": config,
            "epoch": epoch,
            "val_seq_brier": val_brier,
        }
        torch.save(ckpt, out_dir / "last.pt")

        if val_brier < best_val:
            best_val = val_brier
            torch.save(ckpt, out_dir / "best.pt")
        
        early_stopping(val_brier)
        if early_stopping.early_stop:
            print(f"Early stopping at epoch {epoch}", flush=True)
            break

    print(f"Training Done. Best val sequential Brier: {best_val:.6f}", flush=True)
    
    # Final Evaluation on Test Set
    print("\n--- Final Test Evaluation ---", flush=True)
    best_ckpt = torch.load(out_dir / "best.pt")
    model.load_state_dict(best_ckpt["model"])
    test_metrics = evaluate(model, test_loader, mean, std, device)
    print(f"Final Test Sequential Brier: {test_metrics['seq_brier']:.6f}", flush=True)


if __name__ == "__main__":
    main()
