"""Full analysis: per-step Brier/AUC table + trajectory + threshold plots."""
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

# ── Collect all episode trajectories ─────────────────────────────────────────
print("Running inference on test set...")
trajs   = []   # list of (label, np.array[T]) per episode
all_q_list, all_f_list, all_m_list = [], [], []

with torch.no_grad():
    for batch in test_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])
        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            traj_np = q[b, :L].cpu().numpy()
            lbl     = int(batch["failure"][b].item())
            trajs.append((lbl, traj_np))
            all_q_list.append(traj_np)
            all_f_list.append(lbl)

# Build episode-level arrays (variable length — use lists)
ep_trajs  = all_q_list   # list of np arrays, each shape [T_i]
ep_labels = np.array(all_f_list, dtype=int)

failures  = [(p, t) for t, p in [(lbl, traj) for lbl, traj in trajs] if t == 1]
successes = [(p, t) for t, p in [(lbl, traj) for lbl, traj in trajs] if t == 0]
# actually unpack properly:
fail_trajs    = [traj for lbl, traj in trajs if lbl == 1]
success_trajs = [traj for lbl, traj in trajs if lbl == 0]
print(f"  failures={len(fail_trajs)}  successes={len(success_trajs)}")

# ── 1. Per-step Brier & AUC-ROC table ────────────────────────────────────────
from sklearn.metrics import roc_auc_score
STEPS = [1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 75, 100, 150, 200, 300, 500]
labels_arr = ep_labels

print(f"\n{'Steps':>6}  {'AUC-ROC':>8}  {'Brier':>8}  {'Acc@0.3':>8}  {'Acc@0.4':>8}  {'Acc@0.5':>8}")
print("─" * 62)
table_rows = []
for N in STEPS:
    sliced = []
    brier_vals = []
    for b, traj in enumerate(ep_trajs):
        L = len(traj)
        if L == 0: continue
        cutoff = min(N, L)
        p_max = traj[:cutoff].max()
        sliced.append(p_max)
        brier_vals.append((p_max - labels_arr[b])**2)

    sliced = np.array(sliced)
    brier  = np.mean(brier_vals)
    auc    = roc_auc_score(labels_arr, sliced) if len(set(labels_arr)) > 1 else float("nan")

    acc_03 = np.mean((sliced >= 0.3).astype(int) == labels_arr)
    acc_04 = np.mean((sliced >= 0.4).astype(int) == labels_arr)
    acc_05 = np.mean((sliced >= 0.5).astype(int) == labels_arr)

    print(f"{N:>6}  {auc:>8.4f}  {brier:>8.4f}  {acc_03:>8.3f}  {acc_04:>8.3f}  {acc_05:>8.3f}")
    table_rows.append({"steps": N, "auc_roc": auc, "brier": brier,
                        "acc_03": acc_03, "acc_04": acc_04, "acc_05": acc_05})

with open(OUT_DIR / "step_metrics.json", "w") as f:
    json.dump(table_rows, f, indent=2)

# ── 2. Main trajectory plot ───────────────────────────────────────────────────
print("\nGenerating trajectory plot...")
MAX_STEPS_PLOT = 300

def pad_mean_std(traj_list, max_t):
    """For each step t, collect all episodes that have >= t+1 steps, compute mean/std."""
    means, stds, counts = [], [], []
    for t in range(max_t):
        vals = [tr[t] for tr in traj_list if len(tr) > t]
        if not vals:
            means.append(float("nan")); stds.append(0.0); counts.append(0)
        else:
            means.append(np.mean(vals)); stds.append(np.std(vals)); counts.append(len(vals))
    return np.array(means), np.array(stds), np.array(counts)

fail_mean,    fail_std,    _ = pad_mean_std(fail_trajs,    MAX_STEPS_PLOT)
success_mean, success_std, _ = pad_mean_std(success_trajs, MAX_STEPS_PLOT)
t_axis = np.arange(MAX_STEPS_PLOT)

fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle("TDQC v7 — Failure Probability Trajectories (test set, epoch 61 best)", fontsize=14)

# ── Left panel: individual trajectories + mean/std ───────────────────────────
ax = axes[0]
ALPHA_IND = 0.012
MAX_EP_PLOT = 1500  # subsample to avoid SVG bloat

import random
random.seed(42)
fail_sample    = random.sample(fail_trajs,    min(MAX_EP_PLOT, len(fail_trajs)))
success_sample = random.sample(success_trajs, min(MAX_EP_PLOT, len(success_trajs)))

for traj in success_sample:
    t = np.arange(len(traj))
    ax.plot(t, traj, color="steelblue", alpha=ALPHA_IND, linewidth=0.4)
for traj in fail_sample:
    t = np.arange(len(traj))
    ax.plot(t, traj, color="tomato", alpha=ALPHA_IND, linewidth=0.4)

# means + bands
valid_f = ~np.isnan(fail_mean)
valid_s = ~np.isnan(success_mean)
ax.plot(t_axis[valid_s], success_mean[valid_s], color="steelblue", linewidth=2.2, label=f"Success mean (n={len(success_trajs)})")
ax.fill_between(t_axis[valid_s],
                np.clip(success_mean[valid_s] - success_std[valid_s], 0, 1),
                np.clip(success_mean[valid_s] + success_std[valid_s], 0, 1),
                color="steelblue", alpha=0.15)
ax.plot(t_axis[valid_f], fail_mean[valid_f], color="tomato", linewidth=2.2, label=f"Failure mean (n={len(fail_trajs)})")
ax.fill_between(t_axis[valid_f],
                np.clip(fail_mean[valid_f] - fail_std[valid_f], 0, 1),
                np.clip(fail_mean[valid_f] + fail_std[valid_f], 0, 1),
                color="tomato", alpha=0.15)

# threshold lines
for thresh, ls, col in [(0.3, "--", "gold"), (0.4, "-.", "orange"), (0.5, ":", "red")]:
    ax.axhline(thresh, color=col, linewidth=1.5, linestyle=ls, label=f"τ={thresh}")

ax.set_xlim(0, MAX_STEPS_PLOT)
ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("Step", fontsize=11)
ax.set_ylabel("p_fail", fontsize=11)
ax.set_title("Episode trajectories (subsampled) + mean ± std", fontsize=11)
ax.legend(fontsize=9, loc="upper left")
ax.grid(True, alpha=0.2)

# ── Right panel: p_fail distribution at key steps ────────────────────────────
ax2 = axes[1]
KEY_STEPS = [5, 20, 50, 200]
colors_fail    = ["#d62728", "#ff7f0e", "#e377c2", "#7f7f7f"]
colors_success = ["#1f77b4", "#17becf", "#2ca02c", "#bcbd22"]
offsets = [-0.018, -0.006, 0.006, 0.018]

from scipy.stats import gaussian_kde

for i, (N, of, cf, cs) in enumerate(zip(KEY_STEPS, offsets, colors_fail, colors_success)):
    f_vals = np.array([tr[min(N-1, len(tr)-1)] for tr in fail_trajs])
    s_vals = np.array([tr[min(N-1, len(tr)-1)] for tr in success_trajs])

    x_grid = np.linspace(0, 1, 300)
    if f_vals.std() > 1e-4:
        kde_f = gaussian_kde(f_vals, bw_method=0.15)
        ax2.plot(x_grid, kde_f(x_grid) * 0.09 + of + 0.5, color=cf, linewidth=1.5,
                 label=f"Fail  step={N}")
    if s_vals.std() > 1e-4:
        kde_s = gaussian_kde(s_vals, bw_method=0.15)
        ax2.plot(x_grid, kde_s(x_grid) * 0.09 + of + 0.0, color=cs, linewidth=1.5,
                 linestyle="--", label=f"Succ  step={N}")

ax2.axvline(0.3, color="gold",   linewidth=1.5, linestyle="--", label="τ=0.3")
ax2.axvline(0.4, color="orange", linewidth=1.5, linestyle="-.", label="τ=0.4")
ax2.axvline(0.5, color="red",    linewidth=1.5, linestyle=":",  label="τ=0.5")
ax2.axhline(0.5, color="gray", linewidth=0.8, linestyle=":", alpha=0.5)
ax2.text(0.01, 0.52, "← Failure distribution (upper)", fontsize=8, color="gray")
ax2.text(0.01, 0.02, "← Success distribution (lower)", fontsize=8, color="gray")
ax2.set_xlim(0, 1)
ax2.set_xlabel("p_fail value", fontsize=11)
ax2.set_ylabel("KDE density (scaled, offset by step)", fontsize=11)
ax2.set_title("p_fail distribution at fixed steps\n(upper=failure, lower=success)", fontsize=11)
ax2.legend(fontsize=8, ncol=2, loc="upper right")
ax2.grid(True, alpha=0.2)

plt.tight_layout()
out_path = OUT_DIR / "trajectory_and_threshold.png"
plt.savefig(out_path, dpi=160, bbox_inches="tight")
print(f"Saved → {out_path}")

# ── 3. Youden J optimal threshold at each step ───────────────────────────────
print(f"\n{'Steps':>6}  {'Best τ':>7}  {'TPR':>7}  {'TNR':>7}  {'Youden J':>9}  {'Acc@τ':>7}")
print("─" * 52)
from sklearn.metrics import roc_curve
for N in [1, 5, 10, 20, 50, 100, 200]:
    sliced = []
    for b, traj in enumerate(ep_trajs):
        L = len(traj)
        if L == 0: continue
        cutoff = min(N, L)
        sliced.append(traj[:cutoff].max())
    sliced = np.array(sliced)
    labs   = labels_arr
    fpr, tpr, thresholds = roc_curve(labs, sliced)
    j = tpr - fpr
    best_idx = np.argmax(j)
    best_tau = thresholds[best_idx]
    tpr_at   = tpr[best_idx]
    tnr_at   = 1 - fpr[best_idx]
    acc_at   = np.mean((sliced >= best_tau).astype(int) == labs)
    print(f"{N:>6}  {best_tau:>7.3f}  {tpr_at:>7.3f}  {tnr_at:>7.3f}  {j[best_idx]:>9.4f}  {acc_at:>7.3f}")

print("\nAll done.")
