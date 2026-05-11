"""
Per-step accuracy at fixed thresholds.
At each step t: use p_fail[t] (current prediction, NOT max).
Only episodes with length >= t are included at that step.
"""
import sys, torch, numpy as np, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader

sys.path.insert(0, "tests_trains/combined_idea134_v7/code")
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features

CKPT_PATH = "tests_trains/combined_idea134_v7/runs/combined_idea134_v7/best.pt"
TEST_PATH  = "data/v7_11d_test.pt"
OUT_DIR    = Path("tests_trains/combined_idea134_v7/plots")
OUT_DIR.mkdir(exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ckpt   = torch.load(CKPT_PATH, map_location=device)
mean   = ckpt["mean"].to(device)
std    = ckpt["std"].to(device)
cfg    = ckpt["config"]

from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator
model = TDQCLSTMCalibrator(
    input_dim=cfg["input_dim"], hidden_dim=cfg["hidden_dim"],
    num_layers=cfg["num_layers"], dropout=cfg["dropout"],
).to(device)
model.load_state_dict(ckpt["model"])
model.eval()

test_set    = TDQCDataset(TEST_PATH)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False,
                         collate_fn=tdqc_collate, num_workers=2)

# ── Collect per-episode full trajectories ─────────────────────────────────────
print("Running inference...")
trajs  = []   # list of (label:int, p_fail_array:np.array[T])
with torch.no_grad():
    for batch in test_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])
        for b in range(q.shape[0]):
            L   = int(batch["lengths"][b].item())
            lbl = int(batch["failure"][b].item())
            trajs.append((lbl, q[b, :L].cpu().numpy()))

n_fail    = sum(1 for l, _ in trajs if l == 1)
n_success = sum(1 for l, _ in trajs if l == 0)
print(f"  total={len(trajs)}  failures={n_fail}  successes={n_success}")

# ── Stepwise accuracy at fixed thresholds ─────────────────────────────────────
STEPS      = list(range(10, 201, 10))   # 10, 20, ..., 200
THRESHOLDS = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

# results[tau][step] = (accuracy, n_episodes, tpr, tnr)
results = {tau: {} for tau in THRESHOLDS}

print(f"\nStep-wise accuracy (p_fail[t] at exactly step t, NOT max)")
print(f"{'Step':>5}", end="")
for tau in THRESHOLDS:
    print(f"  τ={tau:.1f}", end="")
print(f"  {'n_ep':>6}")
print("─" * (5 + len(THRESHOLDS)*8 + 8))

for t in STEPS:
    idx = t - 1  # zero-indexed
    correct_by_tau = {tau: [] for tau in THRESHOLDS}
    tpr_by_tau     = {tau: [] for tau in THRESHOLDS}
    tnr_by_tau     = {tau: [] for tau in THRESHOLDS}
    n_ep = 0

    for lbl, traj in trajs:
        if len(traj) <= idx:
            continue
        p = float(traj[idx])
        n_ep += 1
        for tau in THRESHOLDS:
            pred = 1 if p >= tau else 0
            correct_by_tau[tau].append(int(pred == lbl))
            if lbl == 1:
                tpr_by_tau[tau].append(int(pred == 1))
            else:
                tnr_by_tau[tau].append(int(pred == 0))

    print(f"{t:>5}", end="")
    for tau in THRESHOLDS:
        if correct_by_tau[tau]:
            acc = np.mean(correct_by_tau[tau])
            tpr = np.mean(tpr_by_tau[tau]) if tpr_by_tau[tau] else float("nan")
            tnr = np.mean(tnr_by_tau[tau]) if tnr_by_tau[tau] else float("nan")
        else:
            acc = tpr = tnr = float("nan")
        results[tau][t] = (acc, n_ep, tpr, tnr)
        print(f"  {acc:.3f}", end="")
    print(f"  {n_ep:>6}")

# ── Also print TPR / TNR breakdown for τ=0.5 ─────────────────────────────────
print(f"\nTPR / TNR breakdown at each step (τ=0.5):")
print(f"{'Step':>5}  {'Acc':>6}  {'TPR':>6}  {'TNR':>6}  {'n_ep':>6}")
print("─" * 36)
for t in STEPS:
    acc, n_ep, tpr, tnr = results[0.5][t]
    print(f"{t:>5}  {acc:.3f}  {tpr:.3f}  {tnr:.3f}  {n_ep:>6}")

# ── Plot ──────────────────────────────────────────────────────────────────────
print("\nGenerating accuracy plot...")

COLORS = {
    0.2: "#e41a1c",
    0.3: "#ff7f00",
    0.4: "#f0c000",
    0.5: "#4daf4a",
    0.6: "#377eb8",
    0.7: "#984ea3",
    0.8: "#a65628",
}

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("TDQC v7 — Per-step accuracy at fixed thresholds\n"
             "(p_fail[t] at exactly step t, all test episodes)", fontsize=13)

# ── Left: accuracy curves ─────────────────────────────────────────────────────
ax = axes[0]
for tau in THRESHOLDS:
    accs  = [results[tau][t][0] for t in STEPS]
    n_eps = [results[tau][t][1] for t in STEPS]
    ax.plot(STEPS, accs, color=COLORS[tau], linewidth=2,
            marker="o", markersize=4, label=f"τ={tau:.1f}")

# baseline (always predict success = majority class)
baseline = n_success / len(trajs)
ax.axhline(baseline, color="black", linewidth=1.2, linestyle="--",
           label=f"Naive baseline ({baseline:.3f})")

ax.set_xlabel("Step (t)", fontsize=11)
ax.set_ylabel("Accuracy", fontsize=11)
ax.set_title("Accuracy at step t for each fixed threshold", fontsize=11)
ax.set_xlim(5, 205)
ax.set_ylim(0.35, 1.01)
ax.legend(fontsize=9, loc="lower right")
ax.grid(True, alpha=0.25)
ax.set_xticks(STEPS[::2])

# ── Right: TPR and TNR for best thresholds ───────────────────────────────────
ax2 = axes[1]
for tau in [0.3, 0.4, 0.5, 0.6]:
    tprs = [results[tau][t][2] for t in STEPS]
    tnrs = [results[tau][t][3] for t in STEPS]
    ax2.plot(STEPS, tprs, color=COLORS[tau], linewidth=2,
             linestyle="-",  marker="o", markersize=3, label=f"TPR τ={tau:.1f}")
    ax2.plot(STEPS, tnrs, color=COLORS[tau], linewidth=2,
             linestyle="--", marker="s", markersize=3, label=f"TNR τ={tau:.1f}")

ax2.axhline(0.5, color="gray", linewidth=0.8, linestyle=":", alpha=0.7)
ax2.set_xlabel("Step (t)", fontsize=11)
ax2.set_ylabel("Rate", fontsize=11)
ax2.set_title("TPR (solid) vs TNR (dashed) by step\nfor thresholds 0.3–0.6", fontsize=11)
ax2.set_xlim(5, 205)
ax2.set_ylim(-0.02, 1.02)
ax2.legend(fontsize=8, ncol=2, loc="lower right")
ax2.grid(True, alpha=0.25)
ax2.set_xticks(STEPS[::2])

plt.tight_layout()
out = OUT_DIR / "stepwise_accuracy.png"
plt.savefig(out, dpi=160, bbox_inches="tight")
print(f"Saved → {out}")
