# TDQC: Stop v7 training, evaluate best checkpoint, launch v2 with better regularization

## Situation

The `combined_idea134_v7` training is **overfitting**. Best val was at epoch 61 (val=0.037176), but val has since risen to ~0.050 at epoch 152 while train_loss keeps dropping to ~0.010. The model is memorizing the training set.

**The best checkpoint is already saved** at:
`tests_trains/combined_idea134_v7/runs/combined_idea134_v7/best.pt`

Root cause: dropout=0.05 is nearly zero and weight_decay=1e-2 is insufficient for this dataset size.

---

## Step 0 — Kill the running training

```bash
pkill -f "combined_idea134_v7/code/phase2_tdqc/train_tdqc.py"
```

Verify it stopped:
```bash
ps aux | grep train_tdqc
```

---

## Step 1 — Evaluate best.pt on the test set

All paths are relative to the standalone project root:
```
/home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/
```

Run from that directory. Write the following script to `tests_trains/combined_idea134_v7/eval_best.py` and execute it:

```python
"""Evaluate best.pt from combined_idea134_v7 on the v7 test set."""
import sys, torch, numpy as np
from pathlib import Path
from torch.utils.data import DataLoader

sys.path.insert(0, "tests_trains/combined_idea134_v7/code")
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score

CKPT_PATH = "tests_trains/combined_idea134_v7/runs/combined_idea134_v7/best.pt"
TEST_PATH  = "data/v7_11d_test.pt"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

ckpt  = torch.load(CKPT_PATH, map_location=device)
mean  = ckpt["mean"].to(device)
std   = ckpt["std"].to(device)
cfg   = ckpt["config"]
print(f"Best checkpoint: epoch={ckpt['epoch']}  val_brier={ckpt['val_seq_brier']:.6f}")

from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator
model = TDQCLSTMCalibrator(
    input_dim=cfg["input_dim"],
    hidden_dim=cfg["hidden_dim"],
    num_layers=cfg["num_layers"],
    dropout=cfg["dropout"],
).to(device)
model.load_state_dict(ckpt["model"])
model.eval()

test_set    = TDQCDataset(TEST_PATH)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False,
                         collate_fn=tdqc_collate, num_workers=2)

# ── collect per-episode predictions ──────────────────────────────────────────
ep_max_pfail = []   # max p_fail over episode (for AUC-ROC)
ep_labels    = []   # 1=failure
all_q, all_f, all_m = [], [], []

with torch.no_grad():
    for batch in test_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])  # [B, T]

        all_q.append(q.cpu())
        all_f.append(batch["failure"].cpu())
        all_m.append(batch["mask"].cpu())

        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            ep_max_pfail.append(q[b, :L].max().item())
            ep_labels.append(int(batch["failure"][b].item()))

Q = torch.cat(all_q)
F = torch.cat(all_f)
M = torch.cat(all_m)

# ── Sequential Brier ──────────────────────────────────────────────────────────
seq_brier = sequential_brier_score(Q, F, M).item()
print(f"\nTest Sequential Brier: {seq_brier:.6f}")

# ── Episode-level AUC-ROC ─────────────────────────────────────────────────────
from sklearn.metrics import roc_auc_score
ep_max_pfail = np.array(ep_max_pfail)
ep_labels    = np.array(ep_labels)
auc = roc_auc_score(ep_labels, ep_max_pfail)
print(f"Test Episode AUC-ROC:  {auc:.4f}")

# ── Early-slice AUC-ROC ───────────────────────────────────────────────────────
print("\nEarly-slice AUC-ROC (using first N steps only):")
print(f"{'Steps':>8}  {'AUC-ROC':>8}  {'Episodes covered':>18}")
for N in [1, 2, 5, 10, 20, 50, 100, 200]:
    sliced, labels = [], []
    for b in range(Q.shape[0]):
        L = int(M[b].sum().item())
        if L == 0:
            continue
        cutoff = min(N, L)
        sliced.append(Q[b, :cutoff].max().item())
        labels.append(int(F[b].item()))
    if len(set(labels)) < 2:
        print(f"{N:>8}  {'N/A':>8}")
        continue
    a = roc_auc_score(labels, sliced)
    print(f"{N:>8}  {a:>8.4f}  {len(sliced):>18}")

# ── Accuracy at threshold=0.5 by step bucket ─────────────────────────────────
print("\nAccuracy at threshold=0.5 by first-N-steps max:")
for N in [1, 2, 5, 10, 20, 50, 100, 200]:
    preds, labels = [], []
    for b in range(Q.shape[0]):
        L = int(M[b].sum().item())
        if L == 0:
            continue
        cutoff = min(N, L)
        preds.append(1 if Q[b, :cutoff].max().item() >= 0.5 else 0)
        labels.append(int(F[b].item()))
    acc = np.mean(np.array(preds) == np.array(labels))
    print(f"  steps <= {N:>3}: acc={acc:.3f}  ({sum(labels)}/{len(labels)} failures)")

print("\nDone.")
```

Run it:
```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone
python3 tests_trains/combined_idea134_v7/eval_best.py
```

---

## Step 2 — Plot the training curve (shows overfitting clearly)

Write the following to `tests_trains/combined_idea134_v7/plot_training.py` and run it:

```python
"""Plot training history for combined_idea134_v7 — shows overfitting."""
import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HISTORY_PATH = "tests_trains/combined_idea134_v7/runs/combined_idea134_v7/history.json"
OUT_PATH     = "tests_trains/combined_idea134_v7/training_curve.png"

history = json.load(open(HISTORY_PATH))
epochs     = [h["epoch"] for h in history]
train_loss = [h["train_loss"] for h in history]
val_brier  = [h["val_seq_brier"] for h in history]

best_epoch = min(range(len(val_brier)), key=lambda i: val_brier[i])
best_val   = val_brier[best_epoch]

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(epochs, train_loss, label="Train loss", color="steelblue", linewidth=1.2)
ax.plot(epochs, val_brier,  label="Val seq Brier", color="tomato", linewidth=1.2)
ax.axvline(epochs[best_epoch], color="green", linestyle="--", linewidth=1,
           label=f"Best: epoch {epochs[best_epoch]}, val={best_val:.4f}")
ax.fill_between(epochs, train_loss, val_brier,
                where=[v > t for v, t in zip(val_brier, train_loss)],
                alpha=0.15, color="red", label="Overfit gap")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss / Brier")
ax.set_title("combined_idea134_v7 — Overfitting (dropout=0.05, wd=0.01)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT_PATH, dpi=150)
print(f"Saved → {OUT_PATH}")
```

Run it:
```bash
python3 tests_trains/combined_idea134_v7/plot_training.py
```

---

## Step 3 — Launch v2 with proper regularization

### What changed and why

| Parameter | v1 (overfits) | v2 (fixed) | Why |
|---|---|---|---|
| dropout | 0.05 | **0.30** | Near-zero dropout = no regularization |
| weight_decay | 0.01 | **0.05** | 5x stronger L2 penalty |
| LR scheduler patience | 15 | **20** | Give more time before reducing LR |
| Early stopping patience | none | **40** | Stop automatically when val stops improving |
| epochs | 500 | 500 | (early stopping will trigger sooner) |

Everything else is identical: 256/2L LSTM, MC loss, task embedding, batch_size=64.

### Create the v2 experiment directory

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

mkdir -p tests_trains/combined_idea134_v7_v2/code
cp -r tests_trains/combined_idea134_v7/code/phase2_tdqc \
      tests_trains/combined_idea134_v7_v2/code/
mkdir -p tests_trains/combined_idea134_v7_v2/runs/combined_idea134_v7_v2
```

### Write the new train_tdqc.py with early stopping

Write the following to `tests_trains/combined_idea134_v7_v2/code/phase2_tdqc/train_tdqc.py`:

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
    p.add_argument("--train_path", type=str, required=True)
    p.add_argument("--val_path",   type=str, required=True)
    p.add_argument("--test_path",  type=str, required=True)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--hidden_dim", type=int,   default=256)
    p.add_argument("--num_layers", type=int,   default=2)
    p.add_argument("--dropout",    type=float, default=0.30)
    p.add_argument("--batch_size", type=int,   default=64)
    p.add_argument("--epochs",     type=int,   default=500)
    p.add_argument("--lr",         type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=5e-2)
    p.add_argument("--lr_patience",  type=int,   default=20)
    p.add_argument("--early_stop_patience", type=int, default=40)
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
        feats = batch["features"]
        mask  = batch["mask"]
        all_valid_feats.append(feats[mask == 1.0])
    features   = torch.cat(all_valid_feats, dim=0).to(device)
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

    device  = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

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

    successes      = sum(1 for ep in train_set.episodes if ep.success)
    failures       = len(train_set) - successes
    success_rate   = successes / max(len(train_set), 1)
    failure_rate   = failures  / max(len(train_set), 1)
    success_weight = 0.5 / max(success_rate, 1e-6)
    fail_weight    = 0.5 / max(failure_rate, 1e-6)
    print(f"  successes={successes}  failures={failures}")

    model = TDQCLSTMCalibrator(
        input_dim=train_set.input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)

    optim     = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optim, mode="min", factor=0.5, patience=args.lr_patience
    )

    best_val          = float("inf")
    start_epoch       = 0
    epochs_no_improve = 0

    if args.resume_path:
        print(f"Resuming from {args.resume_path}...")
        ckpt        = torch.load(args.resume_path, map_location=device)
        model.load_state_dict(ckpt["model"])
        mean        = ckpt["mean"].to(device)
        std         = ckpt["std"].to(device)
        start_epoch = ckpt["epoch"] + 1
        best_val    = ckpt.get("val_seq_brier", float("inf"))
        print(f"  Resumed at epoch {start_epoch}, best_val={best_val:.6f}")
    else:
        print("Computing normalization stats...")
        stats_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=False,
                                  collate_fn=tdqc_collate, num_workers=2)
        stats = collect_train_stats(stats_loader, device)
        mean  = stats["mean"].to(device)
        std   = stats["std"].to(device)

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
                q_online=q, failure=batch["failure"], mask=batch["mask"],
                fail_weight=fail_weight, success_weight=success_weight,
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

        improved = val_brier < best_val
        if improved:
            best_val          = val_brier
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        print(
            f"epoch={epoch:04d}  train={train_loss:.6f}  val={val_brier:.6f}  "
            f"best={best_val:.6f}  no_improve={epochs_no_improve}/{args.early_stop_patience}"
            + ("  ← NEW BEST" if improved else "")
        )

        history.append({"epoch": epoch, "train_loss": train_loss, "val_seq_brier": val_brier})
        (out_dir / "history.json").write_text(json.dumps(history, indent=2))

        ckpt = {
            "model":         model.state_dict(),
            "mean":          mean.detach().cpu(),
            "std":           std.detach().cpu(),
            "config":        config,
            "epoch":         epoch,
            "val_seq_brier": val_brier,
        }
        torch.save(ckpt, out_dir / "last.pt")
        if improved:
            torch.save(ckpt, out_dir / "best.pt")

        # Early stopping
        if epochs_no_improve >= args.early_stop_patience:
            print(f"\nEarly stopping triggered at epoch {epoch} "
                  f"(no improvement for {args.early_stop_patience} epochs).")
            break

    print(f"\nTraining Done. Best val sequential Brier: {best_val:.6f}")

    print("\n--- Final Test Evaluation ---")
    best_ckpt = torch.load(out_dir / "best.pt")
    model.load_state_dict(best_ckpt["model"])
    test_metrics = evaluate(model, test_loader, mean, std, device)
    print(f"Final Test Sequential Brier: {test_metrics['seq_brier']:.6f}")


if __name__ == "__main__":
    main()
```

### Launch v2 training (screen/tmux recommended)

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

screen -S tdqc_v7_v2

PYTHONPATH=tests_trains/combined_idea134_v7_v2/code \
python3 tests_trains/combined_idea134_v7_v2/code/phase2_tdqc/train_tdqc.py \
    --train_path   data/v7_11d_train.pt \
    --val_path     data/v7_11d_val.pt   \
    --test_path    data/v7_11d_test.pt  \
    --output_dir   tests_trains/combined_idea134_v7_v2/runs/combined_idea134_v7_v2 \
    --hidden_dim   256  \
    --num_layers   2    \
    --dropout      0.30 \
    --batch_size   64   \
    --epochs       500  \
    --lr           1e-4 \
    --weight_decay 5e-2 \
    --lr_patience  20   \
    --early_stop_patience 40 \
    --device       cuda \
    2>&1 | tee tests_trains/combined_idea134_v7_v2/training_log.txt
```

Detach with Ctrl+A, D. Monitor with:
```bash
tail -f tests_trains/combined_idea134_v7_v2/training_log.txt
```

---

## Summary of what you're doing

1. **Kill** the overfitting v1 run (best already saved at epoch 61)
2. **Eval** v1 best.pt on test set → get final Brier, AUC-ROC, early-slice AUC-ROC
3. **Plot** the training curve showing the overfit gap
4. **Launch v2** with dropout=0.30 and weight_decay=0.05 + early stopping (patience=40)

Expected: v2 should converge more smoothly, best epoch somewhere around 100-200, and the val/train gap should be much smaller.
