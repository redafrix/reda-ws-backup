"""OOD evaluation on goal_object_ood dataset using exp01 best checkpoint."""
import sys, torch, numpy as np, json, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader
from scipy.stats import gaussian_kde
from sklearn.metrics import roc_auc_score, roc_curve

ROOT = Path(".")
sys.path.insert(0, str(ROOT / "experiments/v7_exp01_combined134/code"))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model    import TDQCLSTMCalibrator
from phase2_tdqc.tdqc_losses   import sequential_brier_score

CKPT     = ROOT / "experiments/v7_exp01_combined134/runs/combined_idea134_v7/best.pt"
OOD_PT   = ROOT / "data/ood/goal_object_ood.pt"
PLOT_DIR = ROOT / "experiments/v7_exp01_combined134/plots"
ANA_DIR  = ROOT / "experiments/v7_exp01_combined134/analysis"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ckpt   = torch.load(CKPT, map_location=device)
mean   = ckpt["mean"].to(device)
std    = ckpt["std"].to(device)
cfg    = ckpt["config"]
print(f"Model: epoch={ckpt['epoch']}  val_brier={ckpt['val_seq_brier']:.6f}")

model = TDQCLSTMCalibrator(
    input_dim=cfg["input_dim"], hidden_dim=cfg["hidden_dim"],
    num_layers=cfg["num_layers"], dropout=cfg["dropout"],
).to(device)
model.load_state_dict(ckpt["model"])
model.eval()

ood_set    = TDQCDataset(str(OOD_PT))
ood_loader = DataLoader(ood_set, batch_size=64, shuffle=False,
                        collate_fn=tdqc_collate, num_workers=2)

print(f"OOD dataset: {len(ood_set)} episodes  input_dim={ood_set.input_dim}")

# ── Inference ─────────────────────────────────────────────────────────────────
print("Running inference...")
trajs = []
with torch.no_grad():
    for batch in ood_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])
        for b in range(q.shape[0]):
            L   = int(batch["lengths"][b].item())
            lbl = int(batch["failure"][b].item())
            trajs.append((lbl, q[b, :L].cpu().numpy()))

fail_trajs    = [t for lbl, t in trajs if lbl == 1]
success_trajs = [t for lbl, t in trajs if lbl == 0]
labels        = np.array([lbl for lbl, _ in trajs])
print(f"  failures={len(fail_trajs)}  successes={len(success_trajs)}")

# ── Sequential Brier ──────────────────────────────────────────────────────────
all_sq = []
for lbl, traj in trajs:
    all_sq.extend(((traj - lbl)**2).tolist())
seq_brier = np.mean(all_sq)

# ── Episode AUC-ROC ───────────────────────────────────────────────────────────
ep_max = np.array([t.max() for _, t in trajs])
auc_ep = roc_auc_score(labels, ep_max) if len(set(labels)) > 1 else float("nan")

print(f"\n{'='*52}")
print(f"OOD TEST RESULTS  (libero_goal_object, 450 ep)")
print(f"{'='*52}")
print(f"  Sequential Brier   : {seq_brier:.6f}")
print(f"  Episode AUC-ROC    : {auc_ep:.4f}")
print(f"  Failure rate       : {len(fail_trajs)/len(trajs)*100:.1f}%  ({len(fail_trajs)}/{len(trajs)})")
print()

# ── Per-step AUC-ROC + accuracy table ────────────────────────────────────────
STEPS      = list(range(10, 201, 10))
THRESHOLDS = [0.3, 0.4, 0.5, 0.6, 0.7]

print(f"{'Step':>5}", end="")
for tau in THRESHOLDS:
    print(f"  τ={tau:.1f}", end="")
print(f"  {'AUC-ROC':>8}  {'n_ep':>5}")
print("─" * (5 + len(THRESHOLDS)*7 + 18))

step_results = []
for t in STEPS:
    idx    = t - 1
    preds  = {tau: [] for tau in THRESHOLDS}
    sliced, labs_t = [], []
    for lbl, traj in trajs:
        if len(traj) <= idx: continue
        p = float(traj[idx])
        sliced.append(p); labs_t.append(lbl)
        for tau in THRESHOLDS:
            preds[tau].append(int((p >= tau) == lbl))
    auc_t = roc_auc_score(labs_t, sliced) if len(set(labs_t)) > 1 else float("nan")
    print(f"{t:>5}", end="")
    row = {"step": t, "auc": auc_t, "n": len(sliced)}
    for tau in THRESHOLDS:
        acc = np.mean(preds[tau]) if preds[tau] else float("nan")
        row[f"acc_{tau}"] = acc
        print(f"  {acc:.3f}", end="")
    print(f"  {auc_t:>8.4f}  {len(sliced):>5}")
    step_results.append(row)

(ANA_DIR / "ood_step_metrics.json").write_text(json.dumps(step_results, indent=2))

# ── Youden optimal threshold ──────────────────────────────────────────────────
print(f"\n{'Step':>5}  {'Best τ':>7}  {'TPR':>6}  {'TNR':>6}  {'J':>6}  {'Acc':>6}")
print("─" * 45)
for t in [5, 10, 20, 50, 100, 200]:
    idx = t - 1
    sliced, labs_t = [], []
    for lbl, traj in trajs:
        if len(traj) <= idx: continue
        sliced.append(float(traj[idx])); labs_t.append(lbl)
    if len(set(labs_t)) < 2: continue
    fpr, tpr, thresholds = roc_curve(labs_t, sliced)
    j = tpr - fpr
    bi = np.argmax(j)
    acc = np.mean((np.array(sliced) >= thresholds[bi]).astype(int) == np.array(labs_t))
    print(f"{t:>5}  {thresholds[bi]:>7.3f}  {tpr[bi]:>6.3f}  {1-fpr[bi]:>6.3f}  {j[bi]:>6.4f}  {acc:>6.3f}")

# ── Plot 1: Trajectory + threshold ────────────────────────────────────────────
print("\nGenerating plots...")
MAX_T = 200

def step_mean_std(tl, mt):
    ms, ss = [], []
    for t in range(mt):
        v = [tr[t] for tr in tl if len(tr) > t]
        ms.append(np.mean(v) if v else np.nan)
        ss.append(np.std(v)  if v else np.nan)
    return np.array(ms), np.array(ss)

fm, fs  = step_mean_std(fail_trajs,    MAX_T)
sm, ss_ = step_mean_std(success_trajs, MAX_T)
tx = np.arange(MAX_T)

fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle(
    "TDQC v7 Exp01 — OOD Evaluation  (libero_goal_object, 450 episodes)\n"
    f"Seq Brier={seq_brier:.4f}  AUC-ROC={auc_ep:.4f}  "
    f"failures={len(fail_trajs)}/450 ({len(fail_trajs)/len(trajs)*100:.0f}%)",
    fontsize=12, fontweight="bold")

ax = axes[0]
random.seed(42)
for tr in random.sample(success_trajs, min(400, len(success_trajs))):
    ax.plot(np.arange(len(tr)), tr, color="#3a86ff", alpha=0.04, linewidth=0.5)
for tr in fail_trajs:
    ax.plot(np.arange(len(tr)), tr, color="#e63946", alpha=0.10, linewidth=0.6)
vf = ~np.isnan(fm); vs = ~np.isnan(sm)
ax.fill_between(tx[vs], np.clip(sm[vs]-ss_[vs],0,1), np.clip(sm[vs]+ss_[vs],0,1), color="#3a86ff", alpha=0.15)
ax.fill_between(tx[vf], np.clip(fm[vf]-fs[vf],0,1), np.clip(fm[vf]+fs[vf],0,1), color="#e63946", alpha=0.15)
ax.plot(tx[vs], sm[vs], color="#3a86ff", linewidth=2.5, label=f"Success mean (n={len(success_trajs)})")
ax.plot(tx[vf], fm[vf], color="#e63946", linewidth=2.5, label=f"Failure mean (n={len(fail_trajs)})")
ax.axhline(0.5, color="#2dc653", linewidth=2.0, linestyle="--", label="τ=0.5")
ax.axhline(0.3, color="#ffd166", linewidth=1.2, linestyle=":",  label="τ=0.3")
ax.axhline(0.7, color="#ef476f", linewidth=1.2, linestyle=":",  label="τ=0.7")
ax.set_xlim(0, MAX_T); ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("Step"); ax.set_ylabel("p_fail")
ax.set_title("OOD episode trajectories + mean ± 1σ")
ax.legend(fontsize=9); ax.grid(True, alpha=0.18)

ax2 = axes[1]
x_grid = np.linspace(0, 1, 400)
FCOLS = ["#d00000","#e85d04","#9d0208","#6a040f"]
SCOLS = ["#0077b6","#00b4d8","#023e8a","#48cae4"]
for i, N in enumerate([10, 20, 50, 100]):
    idx = N - 1
    fv = np.array([tr[idx] for tr in fail_trajs    if len(tr) > idx])
    sv = np.array([tr[idx] for tr in success_trajs if len(tr) > idx])
    for vals, col, ls, lbl in [(fv, FCOLS[i], "-", f"Fail step={N}"), (sv, SCOLS[i], "--", f"Succ step={N}")]:
        if len(vals) > 1 and vals.std() > 1e-4:
            y = gaussian_kde(vals, bw_method=0.15)(x_grid)
            y = y / y.max() * 0.9
            ax2.fill_between(x_grid, y, alpha=0.18, color=col)
            ax2.plot(x_grid, y, color=col, linewidth=1.6, linestyle=ls, label=lbl)
ax2.axvline(0.5, color="#2dc653", linewidth=2.0, linestyle="--", label="τ=0.5")
ax2.set_xlim(0, 1); ax2.set_xlabel("p_fail[t] at exactly step t")
ax2.set_ylabel("Normalised KDE")
ax2.set_title("p_fail[t] distribution (OOD)\n(solid=failure, dashed=success)")
ax2.legend(fontsize=8, ncol=2); ax2.grid(True, alpha=0.18)

plt.tight_layout()
plt.savefig(str(PLOT_DIR / "ood_trajectory_and_threshold.png"), dpi=160, bbox_inches="tight")
print("  Saved ood_trajectory_and_threshold.png")

# ── Plot 2: Stepwise accuracy ──────────────────────────────────────────────────
COLORS = {0.3:"#ff7f00", 0.4:"#f0c000", 0.5:"#4daf4a", 0.6:"#377eb8", 0.7:"#984ea3"}
fig2, axes2 = plt.subplots(1, 2, figsize=(16, 6))
fig2.suptitle("TDQC v7 Exp01 — OOD Per-step accuracy  (libero_goal_object)", fontsize=13)

ax3 = axes2[0]
for tau in THRESHOLDS:
    ax3.plot(STEPS, [r[f"acc_{tau}"] for r in step_results],
             color=COLORS[tau], linewidth=2, marker="o", markersize=4, label=f"τ={tau}")
ax3.axhline(len(success_trajs)/len(trajs), color="black", linewidth=1.2,
            linestyle="--", label=f"Naive baseline ({len(success_trajs)/len(trajs):.3f})")
ax3.set_xlabel("Step"); ax3.set_ylabel("Accuracy")
ax3.set_title("Accuracy at p_fail[t] for each threshold")
ax3.legend(fontsize=9); ax3.grid(True, alpha=0.25)
ax3.set_xlim(5, 205); ax3.set_ylim(0.5, 1.01)

ax4 = axes2[1]
ax4.plot(STEPS, [r["auc"] for r in step_results],
         color="#e63946", linewidth=2.5, marker="o", markersize=5, label="OOD AUC-ROC")
ax4.axhline(0.5, color="gray", linewidth=0.8, linestyle=":")
ax4.set_xlabel("Step"); ax4.set_ylabel("AUC-ROC")
ax4.set_title("AUC-ROC at exactly step t  (OOD)")
ax4.legend(); ax4.grid(True, alpha=0.25)
ax4.set_xlim(5, 205); ax4.set_ylim(0.4, 1.01)

plt.tight_layout()
plt.savefig(str(PLOT_DIR / "ood_stepwise_accuracy.png"), dpi=160, bbox_inches="tight")
print("  Saved ood_stepwise_accuracy.png")

print("\nAll done.")
