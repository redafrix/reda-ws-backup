"""Corrected trajectory + threshold plot. Uses p_fail[t] at exactly step t."""
import sys, torch, numpy as np, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader
from scipy.stats import gaussian_kde

sys.path.insert(0, "tests_trains/combined_idea134_v7/code")
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features

CKPT_PATH = "tests_trains/combined_idea134_v7/runs/combined_idea134_v7/best.pt"
TEST_PATH  = "data/v7_11d_test.pt"
OUT_PATH   = "tests_trains/combined_idea134_v7/plots/trajectory_and_threshold.png"

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

print("Running inference...")
trajs = []
with torch.no_grad():
    for batch in test_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])
        for b in range(q.shape[0]):
            L   = int(batch["lengths"][b].item())
            lbl = int(batch["failure"][b].item())
            trajs.append((lbl, q[b, :L].cpu().numpy()))

fail_trajs    = [t for lbl, t in trajs if lbl == 1]
success_trajs = [t for lbl, t in trajs if lbl == 0]
print(f"  failures={len(fail_trajs)}  successes={len(success_trajs)}")

MAX_T = 300

def step_mean_std(traj_list, max_t):
    means, stds = [], []
    for t in range(max_t):
        vals = [tr[t] for tr in traj_list if len(tr) > t]
        if vals:
            means.append(np.mean(vals))
            stds.append(np.std(vals))
        else:
            means.append(np.nan)
            stds.append(np.nan)
    return np.array(means), np.array(stds)

fail_mean,    fail_std    = step_mean_std(fail_trajs,    MAX_T)
success_mean, success_std = step_mean_std(success_trajs, MAX_T)
t_axis = np.arange(MAX_T)

# ── Figure ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle("TDQC v7 — Failure Probability Trajectories  (test set, best checkpoint epoch 61)",
             fontsize=13, fontweight="bold")

# ── Left: episode trajectories + mean/std ────────────────────────────────────
ax = axes[0]
random.seed(42)
MAX_EP = 1200
fail_sample    = random.sample(fail_trajs,    min(MAX_EP, len(fail_trajs)))
success_sample = random.sample(success_trajs, min(MAX_EP, len(success_trajs)))

for tr in success_sample:
    ax.plot(np.arange(len(tr)), tr, color="#3a86ff", alpha=0.018, linewidth=0.4)
for tr in fail_sample:
    ax.plot(np.arange(len(tr)), tr, color="#e63946", alpha=0.018, linewidth=0.4)

vf = ~np.isnan(fail_mean)
vs = ~np.isnan(success_mean)
ax.fill_between(t_axis[vs],
    np.clip(success_mean[vs]-success_std[vs], 0, 1),
    np.clip(success_mean[vs]+success_std[vs], 0, 1),
    color="#3a86ff", alpha=0.12)
ax.fill_between(t_axis[vf],
    np.clip(fail_mean[vf]-fail_std[vf], 0, 1),
    np.clip(fail_mean[vf]+fail_std[vf], 0, 1),
    color="#e63946", alpha=0.12)
ax.plot(t_axis[vs], success_mean[vs], color="#3a86ff", linewidth=2.5,
        label=f"Success mean  (n={len(success_trajs)})")
ax.plot(t_axis[vf], fail_mean[vf],    color="#e63946", linewidth=2.5,
        label=f"Failure mean  (n={len(fail_trajs)})")

# threshold lines — only 0.5 (the best one per our analysis)
ax.axhline(0.5, color="#2dc653", linewidth=2.0, linestyle="--", label="τ = 0.5  (best threshold)")
ax.axhline(0.3, color="#ffd166", linewidth=1.2, linestyle=":",  label="τ = 0.3")
ax.axhline(0.7, color="#ef476f", linewidth=1.2, linestyle=":",  label="τ = 0.7")

ax.set_xlim(0, MAX_T)
ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("Step", fontsize=11)
ax.set_ylabel("p_fail", fontsize=11)
ax.set_title("Individual trajectories + mean ± 1σ\n(subsampled for visibility)", fontsize=11)
ax.legend(fontsize=9, loc="upper left")
ax.grid(True, alpha=0.18)

# ── Right: p_fail[t] distribution AT exactly step t ──────────────────────────
ax2 = axes[1]
KEY_STEPS   = [10, 20, 50, 100, 200]
FAIL_COLORS = ["#d00000", "#e85d04", "#dc2f02", "#9d0208", "#6a040f"]
SUCC_COLORS = ["#0077b6", "#00b4d8", "#0096c7", "#023e8a", "#48cae4"]
x_grid = np.linspace(0, 1, 400)

for i, N in enumerate(KEY_STEPS):
    idx = N - 1
    f_vals = np.array([tr[idx] for tr in fail_trajs    if len(tr) > idx])
    s_vals = np.array([tr[idx] for tr in success_trajs if len(tr) > idx])

    if f_vals.std() > 1e-4:
        kde_f = gaussian_kde(f_vals, bw_method=0.12)
        y = kde_f(x_grid)
        y = y / y.max() * 0.9   # normalise height
        ax2.fill_between(x_grid, y, alpha=0.25, color=FAIL_COLORS[i])
        ax2.plot(x_grid, y, color=FAIL_COLORS[i], linewidth=1.6,
                 label=f"Failure  step={N}  (n={len(f_vals)})")

    if s_vals.std() > 1e-4:
        kde_s = gaussian_kde(s_vals, bw_method=0.12)
        y = kde_s(x_grid)
        y = y / y.max() * 0.9
        ax2.fill_between(x_grid, y, alpha=0.18, color=SUCC_COLORS[i])
        ax2.plot(x_grid, y, color=SUCC_COLORS[i], linewidth=1.6, linestyle="--",
                 label=f"Success  step={N}  (n={len(s_vals)})")

ax2.axvline(0.5, color="#2dc653", linewidth=2.5, linestyle="--", label="τ = 0.5")
ax2.axvline(0.3, color="#ffd166", linewidth=1.2, linestyle=":",  label="τ = 0.3")
ax2.axvline(0.7, color="#ef476f", linewidth=1.2, linestyle=":",  label="τ = 0.7")

ax2.set_xlim(0, 1)
ax2.set_xlabel("p_fail value at exactly step t", fontsize=11)
ax2.set_ylabel("Normalised KDE density", fontsize=11)
ax2.set_title("p_fail[t] distribution at fixed steps\n(solid=failure, dashed=success)", fontsize=11)
ax2.legend(fontsize=8, ncol=2, loc="upper center")
ax2.grid(True, alpha=0.18)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=160, bbox_inches="tight")
print(f"Saved → {OUT_PATH}")
