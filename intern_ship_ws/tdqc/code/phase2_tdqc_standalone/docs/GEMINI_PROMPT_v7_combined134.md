# TDQC Experiment: combined_idea134_v7 — Combined Ideas 1+3+4 on v7 11D Dataset

## Context

You previously trained `combined_idea134`, which combined three improvements over the baseline TDQC calibrator:
- **Idea 1**: Monte Carlo targets — every step in an episode is trained directly against the terminal failure label (1 = failed, 0 = succeeded), instead of TD(0) bootstrapping. No target network needed.
- **Idea 3**: Task ID embedding — an `nn.Embedding(20, hidden_dim)` is trained alongside the LSTM. The embedding for the episode's `task_id` is broadcast-added to all time steps before the LSTM, giving the model a per-task prior.
- **Idea 4**: Larger LSTM — 256 hidden units, 2 layers (vs. 128/1 in the baseline).

That experiment achieved: **val_seq_brier = 0.0899** (best at epoch 120), **test_seq_brier = 0.0932**, **AUC-ROC = 0.9805**.

---

## What's New

We now have a **10x larger dataset** with **11D features** (instead of 8D). The 3 new features come from the denoising chain inside the diffusion policy and carry important pre-action uncertainty signals:

| idx | name | description |
|-----|------|-------------|
| [8] | `dn_init` | `log1p(denoise_initial_mean)` — uncertainty before denoising starts |
| [9] | `dn_delta` | `sign(Δ)·log1p(\|Δ\|)` where Δ = initial − final — denoising resolution (signed; always ~negative) |
| [10] | `dn_rot` | `log1p(denoise_final_rotation_mean)` — residual rotation-dim variance after denoising |

Dataset split (pre-stratified 80/10/10 by task_suite × success/failure):
- **train**: 31,537 episodes, 7,324,244 steps
- **val**:   3,942 episodes, 914,402 steps
- **test**:  3,942 episodes, 917,462 steps

---

## Your Task

Run the **exact same combined 1+3+4 architecture** on the v7 11D dataset for **500 epochs**.

The only code change needed is that the old training script did a random 70/15/15 split of a single `.pt` file. The new dataset comes pre-split as three separate files, so you need to modify the training script to accept `--train_path`, `--val_path`, `--test_path` instead of `--dataset_path`.

---

## File Paths

All paths below are inside the standalone project root. Run every command from:
```
/home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/
```

- **Reference code (combined_idea134):** `tests_trains/combined_idea134/code/phase2_tdqc/`
- **v7 dataset (already built and verified):**
  - `data/v7_11d_train.pt`
  - `data/v7_11d_val.pt`
  - `data/v7_11d_test.pt`
- **New experiment output:** `tests_trains/combined_idea134_v7/runs/combined_idea134_v7/`

---

## Step-by-Step Instructions

### Step 0 — Verify CUDA PyTorch

```bash
python3 -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

If it prints `False`, install CUDA-enabled PyTorch first:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
python3 -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

---

### Step 1 — Create experiment directory and copy code

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

mkdir -p tests_trains/combined_idea134_v7/code
cp -r tests_trains/combined_idea134/code/phase2_tdqc \
      tests_trains/combined_idea134_v7/code/

mkdir -p tests_trains/combined_idea134_v7/runs/combined_idea134_v7
```

---

### Step 2 — Replace train_tdqc.py with the pre-split version

Write the following **complete file** to
`tests_trains/combined_idea134_v7/code/phase2_tdqc/train_tdqc.py`
(overwrite the existing one):

```python
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
        q     = model(x, batch["lengths"], task_ids=batch["task_ids"])
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
            q     = model(x, batch["lengths"], task_ids=batch["task_ids"])
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
            f"val_seq_brier={val_brier:.6f}  best={best_val:.6f}"
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
            torch.save(ckpt, out_dir / "best.pt")

    print(f"\nTraining Done. Best val sequential Brier: {best_val:.6f}")

    print("\n--- Final Test Evaluation ---")
    best_ckpt = torch.load(out_dir / "best.pt")
    model.load_state_dict(best_ckpt["model"])
    test_metrics = evaluate(model, test_loader, mean, std, device)
    print(f"Final Test Sequential Brier: {test_metrics['seq_brier']:.6f}")


if __name__ == "__main__":
    main()
```

---

### Step 3 — Launch training (screen/tmux recommended)

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

PYTHONPATH=tests_trains/combined_idea134_v7/code \
python3 tests_trains/combined_idea134_v7/code/phase2_tdqc/train_tdqc.py \
    --train_path  data/v7_11d_train.pt \
    --val_path    data/v7_11d_val.pt   \
    --test_path   data/v7_11d_test.pt  \
    --output_dir  tests_trains/combined_idea134_v7/runs/combined_idea134_v7 \
    --hidden_dim  256 \
    --num_layers  2   \
    --dropout     0.05 \
    --batch_size  64  \
    --epochs      500 \
    --lr          1e-4 \
    --weight_decay 1e-2 \
    --device      cuda \
    2>&1 | tee tests_trains/combined_idea134_v7/training_log.txt
```

To run in a persistent screen session:
```bash
screen -S tdqc_v7
# (paste the command above)
# Ctrl+A, D to detach
# screen -r tdqc_v7 to re-attach
```

---

## What to Expect

- **Input dim**: 11 (auto-detected from the .pt file)
- **Model params**: 256 hidden, 2 layers, task_embed(20, 256) — same as combined_idea134
- **Loss**: MC Brier (terminal label broadcast to all steps)
- **Training set**: 31,537 episodes (vs 2,747 in previous experiment — ~11x more)
- **Each epoch**: ~493 batches of 64 → more gradient signal per epoch
- **Expected convergence**: Potentially faster (more data) and to a lower Brier score than 0.0899

Monitor progress:
```bash
tail -f tests_trains/combined_idea134_v7/training_log.txt
```

Check best so far:
```bash
python3 -c "
import torch, json
ckpt = torch.load('tests_trains/combined_idea134_v7/runs/combined_idea134_v7/best.pt', map_location='cpu')
print(f'best epoch={ckpt[\"epoch\"]}  val_brier={ckpt[\"val_seq_brier\"]:.6f}')
"
```

---

## Reference: Previous Results

| Experiment | Val Brier | Test Brier | AUC-ROC | Best Epoch |
|---|---|---|---|---|
| Baseline (v6, 8D) | 0.1232 | 0.1497 | — | — |
| combined_idea134 (v6, 8D) | 0.0899 | 0.0932 | 0.9805 | 120/2000 |
| **combined_idea134_v7 (v7, 11D)** | ??? | ??? | ??? | ??? |

Target: beat val_brier = 0.0899 and test_brier = 0.0932.
