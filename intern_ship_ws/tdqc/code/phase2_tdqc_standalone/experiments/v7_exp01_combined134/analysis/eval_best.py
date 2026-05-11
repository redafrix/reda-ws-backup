"""Evaluate best.pt from combined_idea134_v7 on the v7 test set — Fixed for variable lengths and score function."""
import sys, torch, numpy as np
from pathlib import Path
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence

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
ep_preds  = []   # list of [T] tensors
ep_labels = []   # list of failure scalars
ep_masks  = []   # list of [T] masks

with torch.no_grad():
    for batch in test_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])  # [B, T]

        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            ep_preds.append(q[b, :L].cpu())
            ep_labels.append(batch["failure"][b].item())
            ep_masks.append(batch["mask"][b, :L].cpu())

# Pad for unified Brier calculation
Q = pad_sequence(ep_preds, batch_first=True, padding_value=0.0)
F = torch.tensor(ep_labels) # [N]
M = pad_sequence(ep_masks, batch_first=True, padding_value=0.0)

# ── Sequential Brier ──────────────────────────────────────────────────────────
# sequential_brier_score expects failure to be [B]
seq_brier = sequential_brier_score(Q, F, M).item()
print(f"\nTest Sequential Brier: {seq_brier:.6f}")

# ── Episode-level AUC-ROC ─────────────────────────────────────────────────────
from sklearn.metrics import roc_auc_score
ep_max_pfail = np.array([p.max().item() for p in ep_preds])
ep_labels_arr = np.array(ep_labels)
auc = roc_auc_score(ep_labels_arr, ep_max_pfail)
print(f"Test Episode AUC-ROC:  {auc:.4f}")

# ── Early-slice AUC-ROC ───────────────────────────────────────────────────────
print("\nEarly-slice AUC-ROC (using first N steps only):")
print(f"{'Steps':>8}  {'AUC-ROC':>8}  {'Episodes covered':>18}")
for N in [1, 2, 5, 10, 20, 50, 100, 200]:
    sliced, labels = [], []
    for i in range(len(ep_preds)):
        p = ep_preds[i]
        L = len(p)
        cutoff = min(N, L)
        sliced.append(p[:cutoff].max().item())
        labels.append(ep_labels[i])
    if len(set(labels)) < 2:
        print(f"{N:>8}  {'N/A':>8}")
        continue
    a = roc_auc_score(labels, sliced)
    print(f"{N:>8}  {a:>8.4f}  {len(sliced):>18}")

# ── Accuracy at threshold=0.5 by step bucket ─────────────────────────────────
print("\nAccuracy at threshold=0.5 by first-N-steps max:")
for N in [1, 2, 5, 10, 20, 50, 100, 200]:
    preds, labels = [], []
    for i in range(len(ep_preds)):
        p = ep_preds[i]
        L = len(p)
        cutoff = min(N, L)
        preds.append(1 if p[:cutoff].max().item() >= 0.5 else 0)
        labels.append(ep_labels[i])
    acc = np.mean(np.array(preds) == np.array(labels))
    print(f"  steps <= {N:>3}: acc={acc:.3f}  ({sum(labels)}/{len(labels)} failures)")

print("\nDone.")
