from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import torch
from torch.utils.data import DataLoader, random_split

# Import from local capsule library
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from phase2_tdqc.tdqc_losses import tdqc_brier_mc_loss, sequential_brier_score
from tdqc_model import TDQCMambaCalibrator, hard_update


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", type=str, required=True)
    p.add_argument("--val_path", type=str, default=None)
    p.add_argument("--test_path", type=str, default=None)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--hidden_dim", type=int, default=128)
    p.add_argument("--num_layers", type=int, default=2)
    p.add_argument("--dropout", type=float, default=0.05)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--epochs", type=int, default=200)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--train_ratio", type=float, default=0.8)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument("--resume_path", type=str, default=None, help="Path to checkpoint to resume from")
    
    # Mamba specific
    p.add_argument("--d_state", type=int, default=16)
    p.add_argument("--d_conv", type=int, default=4)
    p.add_argument("--expand", type=int, default=2)
    p.add_argument("--early_stopping_patience", type=int, default=30)
    
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
        # For now, we don't pass suite_embed separately in the dataset collate, 
        # it's usually concatenated or handled inside features. 
        # If the dataset has 'suite_id', we might need to fetch it.
        q = model(x)
        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count

    return {"seq_brier": total_brier / max(total_count, 1.0)}


def main():
    import os
    print(f"LD_LIBRARY_PATH: {os.environ.get('LD_LIBRARY_PATH', 'Not Set')}", flush=True)
    args = parse_args()
    random.seed(args.seed)
    torch.manual_seed(args.seed)

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}", flush=True)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading train dataset from {args.dataset_path}...", flush=True)
    train_dataset = TDQCDataset(args.dataset_path)
    
    if args.val_path and args.test_path:
        print(f"Loading val dataset from {args.val_path}...", flush=True)
        val_set = TDQCDataset(args.val_path)
        print(f"Loading test dataset from {args.test_path}...", flush=True)
        test_set = TDQCDataset(args.test_path)
        train_set = train_dataset
    else:
        n_total = len(train_dataset)
        n_train = int(args.train_ratio * n_total)
        n_val = (n_total - n_train) // 2
        n_test = n_total - n_train - n_val
        print(f"Splitting dataset: {n_train} train, {n_val} val, {n_test} test.", flush=True)
        train_set, val_set, test_set = random_split(
            train_dataset,
            [n_train, n_val, n_test],
            generator=torch.Generator().manual_seed(args.seed),
        )

    print("DEBUG: Creating DataLoaders...", flush=True)
    train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, collate_fn=tdqc_collate)
    val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)
    test_loader = DataLoader(test_set, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)

    # Class weights.
    print("DEBUG: Computing class weights...", flush=True)
    successes = sum(int(train_dataset[i].success) for i in range(len(train_dataset)))
    failures = len(train_dataset) - successes
    print(f"DEBUG: total successes={successes}, failures={failures}", flush=True)
    success_rate = successes / max(len(train_dataset), 1)
    failure_rate = failures / max(len(train_dataset), 1)
    success_weight = 0.5 / max(success_rate, 1e-6)
    fail_weight = 0.5 / max(failure_rate, 1e-6)

    print("DEBUG: Initializing Mamba model...", flush=True)
    model = TDQCMambaCalibrator(
        input_dim=train_dataset.input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
        d_state=args.d_state,
        d_conv=args.d_conv,
        expand=args.expand,
    ).to(device)
    
    optim = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optim, mode="min", factor=0.5, patience=15)

    global_step = 0
    best_val = float("inf")
    start_epoch = 0
    early_stop_counter = 0

    if args.resume_path:
        print(f"Resuming from {args.resume_path}...", flush=True)
        ckpt = torch.load(args.resume_path, map_location=device)
        model.load_state_dict(ckpt["model"])
        mean = ckpt["mean"].to(device)
        std = ckpt["std"].to(device)
        start_epoch = ckpt["epoch"] + 1
        best_val = ckpt.get("val_seq_brier", float("inf"))
        print(f"Resuming at epoch {start_epoch} with best_val={best_val:.6f}", flush=True)
    else:
        print("DEBUG: Collecting training statistics for normalization...", flush=True)
        stats_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)
        stats = collect_train_stats(stats_loader, device)
        mean = stats["mean"].to(device)
        std = stats["std"].to(device)
        print("DEBUG: Statistics collected.", flush=True)

    config = vars(args) | {
        "input_dim": train_dataset.input_dim,
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

            q = model(x)
            loss = tdqc_brier_mc_loss(
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

            global_step += 1
            running += loss.item()
            denom += 1
            
            if args.epochs == 1 and denom >= 1: break

        train_loss = running / max(denom, 1)
        val_metrics = evaluate(model, val_loader, mean, std, device)
        val_brier = val_metrics["seq_brier"]
        scheduler.step(val_brier)

        status_msg = ""
        if val_brier < best_val:
            best_val = val_brier
            early_stop_counter = 0
            status_msg = f" | [NEW BEST]"
            ckpt = {
                "model": model.state_dict(),
                "mean": mean.detach().cpu(),
                "std": std.detach().cpu(),
                "config": config,
                "epoch": epoch,
                "val_seq_brier": val_brier,
            }
            torch.save(ckpt, out_dir / "best.pt")
        else:
            early_stop_counter += 1
            status_msg = f" | patience: {early_stop_counter}/{args.early_stopping_patience}"

        print(f"epoch={epoch:04d} train_loss={train_loss:.6f} val_seq_brier={val_brier:.6f} best={best_val:.6f}{status_msg}", flush=True)

        history.append({"epoch": epoch, "train_loss": train_loss, "val_seq_brier": val_brier})
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

        if early_stop_counter >= args.early_stopping_patience:
            print(f"Early stopping triggered after {args.early_stopping_patience} epochs.", flush=True)
            break
        if args.epochs == 1: break
            
        # Dry run check
        if args.epochs == 1:
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
