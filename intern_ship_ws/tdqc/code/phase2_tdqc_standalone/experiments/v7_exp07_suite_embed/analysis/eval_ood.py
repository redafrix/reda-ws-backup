"""Full eval for v7_exp07_suite_embed."""
import sys, torch, numpy as np, json, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader
from scipy.stats import gaussian_kde
from sklearn.metrics import roc_auc_score, roc_curve

ROOT     = Path(".")
EXP      = ROOT / "experiments/v7_exp07_suite_embed"
sys.path.insert(0, str(EXP / "code"))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model    import TDQCLSTMCalibrator
from phase2_tdqc.tdqc_losses   import sequential_brier_score

CKPT  = EXP / "runs/best.pt"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_eval():
    if not CKPT.exists():
        print(f"Error: {CKPT} not found. Training might still be in progress.")
        return

    ckpt  = torch.load(CKPT, map_location=device)
    mean  = ckpt["mean"].to(device)
    std   = ckpt["std"].to(device)
    cfg   = ckpt["config"]
    print(f"Best checkpoint: epoch={ckpt['epoch']}  val_brier={ckpt['val_seq_brier']:.6f}")

    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"], hidden_dim=cfg["hidden_dim"],
        num_layers=cfg["num_layers"], dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()

    test_set    = TDQCDataset(str(ROOT / "data/v7_22d/v7_22d_ood.pt"))
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False,
                             collate_fn=tdqc_collate, num_workers=2)

    print("Running inference...")
    trajs = []
    with torch.no_grad():
        for batch in test_loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            
            # WORKAROUND: Map unknown suites (negative ids) to index 0 to avoid CUDA crash
            s_ids = batch["suite_id"].clone()
            s_ids[s_ids < 0] = 0
            
            q = model(x, batch["lengths"], suite_ids=s_ids)
            for b in range(q.shape[0]):
                L   = int(batch["lengths"][b].item())
                lbl = int(batch["failure"][b].item())
                trajs.append((lbl, q[b, :L].cpu().numpy()))

    fail_trajs    = [t for lbl, t in trajs if lbl == 1]
    success_trajs = [t for lbl, t in trajs if lbl == 0]
    labels = np.array([lbl for lbl, _ in trajs])
    print(f"  failures={len(fail_trajs)}  successes={len(success_trajs)}")

    # ── Sequential Brier (per-step, all episodes) ─────────────────────────────────
    # Compute manually from trajs
    all_sq_err = []
    for lbl, traj in trajs:
        all_sq_err.extend(((traj - lbl)**2).tolist())
    seq_brier = np.mean(all_sq_err)
    print(f"\nTest Sequential Brier : {seq_brier:.6f}")

    # ── Episode-level AUC-ROC (max p_fail per episode) ────────────────────────────
    ep_max = np.array([t.max() for _, t in trajs])
    auc_ep = roc_auc_score(labels, ep_max)
    print(f"Test Episode AUC-ROC  : {auc_ep:.4f}")

    # ── Stepwise accuracy (p_fail[t] at exactly step t) ──────────────────────────
    STEPS      = list(range(10, 201, 10))
    THRESHOLDS = [0.3, 0.4, 0.5, 0.6, 0.7]

    print(f"\n{'Step':>5}", end="")
    for tau in THRESHOLDS:
        print(f"  τ={tau:.1f}", end="")
    print(f"  {'AUC':>6}  {'n':>5}")
    print("─" * (5 + len(THRESHOLDS)*7 + 16))

    step_results = []
    for t in STEPS:
        idx    = t - 1
        preds  = {tau: [] for tau in THRESHOLDS}
        sliced = []
        labs_t = []
        for lbl, traj in trajs:
            if len(traj) <= idx:
                continue
            p = float(traj[idx])
            sliced.append(p)
            labs_t.append(lbl)
            for tau in THRESHOLDS:
                preds[tau].append(int((p >= tau) == lbl))
        auc_t = roc_auc_score(labs_t, sliced) if len(set(labs_t)) > 1 else float("nan")
        print(f"{t:>5}", end="")
        row = {"step": t, "auc": auc_t, "n": len(sliced)}
        for tau in THRESHOLDS:
            acc = np.mean(preds[tau]) if preds[tau] else float("nan")
            row[f"acc_{tau}"] = acc
            print(f"  {acc:.3f}", end="")
        print(f"  {auc_t:.4f}  {len(sliced):>5}")
        step_results.append(row)

    # Save results
    (EXP / "analysis/step_metrics_ood.json").write_text(json.dumps(step_results, indent=2))

    # ── Plot 1: Trajectory + threshold ────────────────────────────────────────────
    MAX_T = 300
    def step_mean_std(tl, max_t):
        ms, ss = [], []
        for t in range(max_t):
            v = [tr[t] for tr in tl if len(tr) > t]
            ms.append(np.mean(v) if v else np.nan)
            ss.append(np.std(v)  if v else np.nan)
        return np.array(ms), np.array(ss)

    fm, fs = step_mean_std(fail_trajs,    MAX_T)
    sm, ss_ = step_mean_std(success_trajs, MAX_T)
    tx = np.arange(MAX_T)

    fig, axes = plt.subplots(1, 2, figsize=(18, 7))
    fig.suptitle("TDQC v7 Exp07 — Delta + Task Embed (Large)  (OOD test set)", fontsize=13, fontweight="bold")

    ax = axes[0]
    random.seed(42)
    for tr in random.sample(success_trajs, min(1200, len(success_trajs))):
        ax.plot(np.arange(len(tr)), tr, color="#3a86ff", alpha=0.018, linewidth=0.4)
    for tr in random.sample(fail_trajs, min(1200, len(fail_trajs))):
        ax.plot(np.arange(len(tr)), tr, color="#e63946", alpha=0.018, linewidth=0.4)
    vf = ~np.isnan(fm);  vs = ~np.isnan(sm)
    ax.fill_between(tx[vs], np.clip(sm[vs]-ss_[vs],0,1), np.clip(sm[vs]+ss_[vs],0,1), color="#3a86ff", alpha=0.12)
    ax.fill_between(tx[vf], np.clip(fm[vf]-fs[vf],0,1), np.clip(fm[vf]+fs[vf],0,1), color="#e63946", alpha=0.12)
    ax.plot(tx[vs], sm[vs], color="#3a86ff", linewidth=2.5, label=f"Success mean (n={len(success_trajs)})")
    ax.plot(tx[vf], fm[vf], color="#e63946", linewidth=2.5, label=f"Failure mean (n={len(fail_trajs)})")
    ax.axhline(0.5, color="#2dc653", linewidth=2.0, linestyle="--", label="τ=0.5")
    ax.axhline(0.3, color="#ffd166", linewidth=1.2, linestyle=":",  label="τ=0.3")
    ax.axhline(0.7, color="#ef476f", linewidth=1.2, linestyle=":",  label="τ=0.7")
    ax.set_xlim(0, MAX_T); ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel("Step"); ax.set_ylabel("p_fail")
    ax.set_title("Trajectories + mean ± 1σ"); ax.legend(fontsize=9); ax.grid(True, alpha=0.18)

    ax2 = axes[1]
    x_grid = np.linspace(0, 1, 400)
    FCOLS = ["#d00000","#e85d04","#9d0208","#6a040f","#370617"]
    SCOLS = ["#0077b6","#00b4d8","#023e8a","#48cae4","#0096c7"]
    for i, N in enumerate([10, 20, 50, 100, 200]):
        idx = N - 1
        fv = np.array([tr[idx] for tr in fail_trajs    if len(tr) > idx])
        sv = np.array([tr[idx] for tr in success_trajs if len(tr) > idx])
        for vals, col, ls, lbl in [(fv, FCOLS[i], "-", f"Fail step={N}"), (sv, SCOLS[i], "--", f"Succ step={N}")]:
            if vals.std() > 1e-4:
                y = gaussian_kde(vals, bw_method=0.12)(x_grid)
                y = y / y.max() * 0.9
                ax2.fill_between(x_grid, y, alpha=0.18, color=col)
                ax2.plot(x_grid, y, color=col, linewidth=1.6, linestyle=ls, label=lbl)
    ax2.axvline(0.5, color="#2dc653", linewidth=2.5, linestyle="--", label="τ=0.5")
    ax2.set_xlim(0, 1); ax2.set_xlabel("p_fail[t] at exactly step t")
    ax2.set_ylabel("Normalised KDE"); ax2.set_title("Distribution at fixed steps\n(solid=failure, dashed=success)")
    ax2.legend(fontsize=8, ncol=2); ax2.grid(True, alpha=0.18)

    plt.tight_layout()
    plt.savefig(str(EXP / "plots/trajectory_and_threshold_ood.png"), dpi=160, bbox_inches="tight")
    print("Saved trajectory plot.")

    # ── Plot 2: Stepwise accuracy ─────────────────────────────────────────────────
    COLORS = {0.3:"#ff7f00", 0.4:"#f0c000", 0.5:"#4daf4a", 0.6:"#377eb8", 0.7:"#984ea3"}
    fig2, axes2 = plt.subplots(1, 2, figsize=(16, 6))
    fig2.suptitle("TDQC v7 Exp07 — Per-step accuracy at fixed thresholds", fontsize=13)
    ax3 = axes2[0]
    for tau in THRESHOLDS:
        accs = [r[f"acc_{tau}"] for r in step_results]
        ax3.plot(STEPS, accs, color=COLORS[tau], linewidth=2, marker="o", markersize=4, label=f"τ={tau}")
    ax3.axhline(len(success_trajs)/len(trajs), color="black", linewidth=1.2, linestyle="--", label="Naive baseline")
    ax3.set_xlabel("Step"); ax3.set_ylabel("Accuracy"); ax3.legend(fontsize=9)
    ax3.set_title("Accuracy at step t (p_fail[t] exactly)"); ax3.grid(True, alpha=0.25)
    ax3.set_xlim(5, 205); ax3.set_ylim(0.5, 1.01)

    ax4 = axes2[1]
    aucs = [r["auc"] for r in step_results]
    ax4.plot(STEPS, aucs, color="#e63946", linewidth=2.5, marker="o", markersize=5, label="AUC-ROC at step t")
    ax4.axhline(0.5, color="gray", linewidth=0.8, linestyle=":")
    ax4.set_xlabel("Step"); ax4.set_ylabel("AUC-ROC")
    ax4.set_title("AUC-ROC at exactly step t"); ax4.legend(); ax4.grid(True, alpha=0.25)
    ax4.set_xlim(5, 205); ax4.set_ylim(0.4, 1.01)

    plt.tight_layout()
    plt.savefig(str(EXP / "plots/stepwise_accuracy_ood.png"), dpi=160, bbox_inches="tight")
    print("Saved stepwise accuracy plot.")

    # ── Plot 3: Training curve ─────────────────────────────────────────────────────
    history_file = EXP / "runs/history.json"
    if history_file.exists():
        history = json.loads(history_file.read_text())
        epochs   = [h["epoch"]        for h in history]
        tr_loss  = [h["train_loss"]   for h in history]
        vl_brier = [h["val_seq_brier"] for h in history]
        best_ep  = min(range(len(vl_brier)), key=lambda i: vl_brier[i])

        fig3, ax5 = plt.subplots(figsize=(12, 5))
        ax5.plot(epochs, tr_loss,  color="steelblue", linewidth=1.4, label="Train loss")
        ax5.plot(epochs, vl_brier, color="tomato",    linewidth=1.4, label="Val seq Brier")
        ax5.axvline(epochs[best_ep], color="green", linestyle="--", linewidth=1.2,
                    label=f"Best: epoch {epochs[best_ep]}, val={vl_brier[best_ep]:.4f}")
        ax5.fill_between(epochs, tr_loss, vl_brier,
                         where=[v > t for v, t in zip(vl_brier, tr_loss)],
                         alpha=0.12, color="red", label="Overfit gap")
        ax5.set_xlabel("Epoch"); ax5.set_ylabel("Loss / Brier")
        ax5.set_title("v7 Exp07 — Training curve (Delta + Task Embed (Large))")
        ax5.legend(); ax5.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(str(EXP / "plots/training_curve.png"), dpi=150, bbox_inches="tight")
        print("Saved training curve.")

    # ── Summary ───────────────────────────────────────────────────────────────────
    print(f"\n{'='*55}")
    print(f"SUMMARY — v7_exp07_suite_embed (OOD)")
    print(f"{'='*55}")
    print(f"Best epoch        : {ckpt['epoch']}")
    print(f"Val Brier (best)  : {ckpt['val_seq_brier']:.6f}")
    print(f"Test seq Brier    : {seq_brier:.6f}")
    print(f"Test AUC-ROC      : {auc_ep:.4f}")
    print(f"Acc @ step10, τ=0.5 : {step_results[0]['acc_0.5']:.3f}")
    print(f"Acc @ step20, τ=0.5 : {step_results[1]['acc_0.5']:.3f}")
    print(f"Acc @ step50, τ=0.5 : {step_results[4]['acc_0.5']:.3f}")
    print(f"{'='*55}")
    print("\nAll plots saved to experiments/v7_exp07_suite_embed/plots/")

if __name__ == "__main__":
    run_eval()
