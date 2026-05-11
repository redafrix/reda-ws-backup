"""Eval for new Goal Object OOD dataset using v8_exp08_balanced."""
import sys, torch, numpy as np, json, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader
from scipy.stats import gaussian_kde
from sklearn.metrics import roc_auc_score, roc_curve

# Setup paths relative to the experiment capsule
ROOT     = Path(".")
EXP      = ROOT / "experiments/v8_exp08_balanced"
# Add experiment code to path to use the modified tdqc_dataset.py
sys.path.insert(0, str(EXP / "code"))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model    import TDQCLSTMCalibrator

# Use the best checkpoint from Exp 08
CKPT  = EXP / "runs/best.pt"
# Point to our NEWLY converted dataset
DATASET_PATH = ROOT / "data/goal_object_ood/v7_22d_ood.pt"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_eval():
    if not CKPT.exists():
        print(f"Error: {CKPT} not found.")
        return
    if not DATASET_PATH.exists():
        print(f"Error: {DATASET_PATH} not found. Did you run the conversion?")
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

    test_set    = TDQCDataset(str(DATASET_PATH))
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False,
                             collate_fn=tdqc_collate, num_workers=2)

    print("Running inference...")
    trajs = []
    with torch.no_grad():
        for batch in test_loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            
            # Use suite_ids from batch (mapped in tdqc_dataset.py)
            q = model(x, batch["lengths"], suite_ids=batch["suite_id"])
            
            for b in range(q.shape[0]):
                L   = int(batch["lengths"][b].item())
                lbl = int(batch["failure"][b].item())
                trajs.append((lbl, q[b, :L].cpu().numpy()))

    fail_trajs    = [t for lbl, t in trajs if lbl == 1]
    success_trajs = [t for lbl, t in trajs if lbl == 0]
    labels = np.array([lbl for lbl, _ in trajs])
    print(f"  failures={len(fail_trajs)}  successes={len(success_trajs)}")

    # ── Sequential Brier (per-step, all episodes) ─────────────────────────────────
    all_sq_err = []
    for lbl, traj in trajs:
        all_sq_err.extend(((traj - lbl)**2).tolist())
    seq_brier = np.mean(all_sq_err)
    print(f"\nTest Sequential Brier : {seq_brier:.6f}")

    # ── Episode-level AUC-ROC (max p_fail per episode) ────────────────────────────
    ep_max = np.array([t.max() for _, t in trajs])
    auc_ep = roc_auc_score(labels, ep_max) if len(set(labels)) > 1 else float("nan")
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

    # ── Summary ───────────────────────────────────────────────────────────────────
    print(f"\n{'='*55}")
    print(f"SUMMARY — Goal Object OOD (v8_exp08_balanced)")
    print(f"{'='*55}")
    print(f"Test seq Brier    : {seq_brier:.6f}")
    print(f"Test AUC-ROC      : {auc_ep:.4f}")
    if step_results:
        print(f"Acc @ step10, τ=0.5 : {step_results[0]['acc_0.5']:.3f}")
        print(f"Acc @ step50, τ=0.5 : {step_results[4]['acc_0.5']:.3f}")
    print(f"{'='*55}")

if __name__ == "__main__":
    run_eval()
