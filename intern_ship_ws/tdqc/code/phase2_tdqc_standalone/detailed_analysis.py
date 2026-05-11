"""Detailed Analysis for Libero Object Object dataset using v8_exp08_balanced."""
import sys, torch, numpy as np, json, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# import seaborn as sns
from pathlib import Path
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, average_precision_score

# Setup paths
ROOT     = Path(".")
EXP      = ROOT / "experiments/v8_exp08_balanced"
sys.path.insert(0, str(EXP / "code"))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model    import TDQCLSTMCalibrator

CKPT  = EXP / "runs/best.pt"
DATASET_PATH = ROOT / "data/libero_object_object_new/v7_22d_ood.pt"
OUT_DIR = ROOT / "outputs/analysis/libero_object_object_new"
OUT_DIR.mkdir(parents=True, exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_detailed_analysis():
    ckpt  = torch.load(CKPT, map_location=device)
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)
    cfg   = ckpt["config"]
    
    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"], hidden_dim=cfg["hidden_dim"],
        num_layers=cfg["num_layers"], dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()

    test_set    = TDQCDataset(str(DATASET_PATH))
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)

    trajs = []
    with torch.no_grad():
        for batch in test_loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            q = model(x, batch["lengths"], suite_ids=batch["suite_id"])
            for b in range(q.shape[0]):
                L = int(batch["lengths"][b].item())
                trajs.append({"label": int(batch["failure"][b].item()), "preds": q[b, :L].cpu().numpy()})

    labels = np.array([t["label"] for t in trajs])
    ep_max = np.array([t["preds"].max() for t in trajs])

    # 1. AUC Plot
    plt.figure(figsize=(8, 6))
    fpr, tpr, _ = roc_curve(labels, ep_max)
    auc_val = roc_auc_score(labels, ep_max)
    plt.plot(fpr, tpr, label=f"ROC (AUC={auc_val:.4f})", color="blue", lw=2)
    plt.plot([0, 1], [0, 1], "k--", alpha=0.5)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Episode-Level ROC Curve: Libero Object Object (New)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(OUT_DIR / "roc_curve.png", dpi=150)
    plt.close()

    # 2. Probability Distributions
    plt.figure(figsize=(10, 6))
    from scipy.stats import gaussian_kde
    x_grid = np.linspace(0, 1, 100)
    if len(ep_max[labels == 0]) > 1:
        kde_s = gaussian_kde(ep_max[labels == 0])
        plt.fill_between(x_grid, kde_s(x_grid), color="green", alpha=0.3, label="Successes")
    if len(ep_max[labels == 1]) > 1:
        kde_f = gaussian_kde(ep_max[labels == 1])
        plt.fill_between(x_grid, kde_f(x_grid), color="red", alpha=0.3, label="Failures")
    plt.axvline(0.5, color="black", linestyle="--", label="Threshold=0.5")
    plt.xlabel("Max Failure Probability")
    plt.ylabel("Density")
    plt.title("Distribution of Predicted Failure Probabilities")
    plt.legend()
    plt.savefig(OUT_DIR / "prob_dist.png", dpi=150)
    plt.close()

    # 3. Temporal Trajectories (Random Samples)
    plt.figure(figsize=(12, 8))
    for i in range(5):
        s_idx = random.choice([j for j, l in enumerate(labels) if l == 0])
        f_idx = random.choice([j for j, l in enumerate(labels) if l == 1])
        plt.plot(trajs[s_idx]["preds"], color="green", alpha=0.4, label="Success" if i==0 else "")
        plt.plot(trajs[f_idx]["preds"], color="red", alpha=0.6, label="Failure" if i==0 else "")
    plt.axhline(0.5, color="black", linestyle="--")
    plt.xlabel("Steps")
    plt.ylabel("P(Failure)")
    plt.title("Sample Temporal Predictions")
    plt.legend()
    plt.savefig(OUT_DIR / "trajectories.png", dpi=150)
    plt.close()

    # 4. Stepwise Metrics Table (Save to CSV)
    import csv
    STEPS = list(range(10, 201, 10))
    table_data = []
    with open(OUT_DIR / "stepwise_metrics.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["step", "auc", "acc_0.5", "n"])
        writer.writeheader()
        for t in STEPS:
            idx = t - 1
            labs_t, preds_t = [], []
            for traj in trajs:
                if len(traj["preds"]) > idx:
                    labs_t.append(traj["label"])
                    preds_t.append(traj["preds"][idx])
            if len(set(labs_t)) > 1:
                auc = roc_auc_score(labs_t, preds_t)
                acc = np.mean([(p > 0.5) == l for p, l in zip(preds_t, labs_t)])
                row = {"step": t, "auc": auc, "acc_0.5": acc, "n": len(labs_t)}
                writer.writerow(row)
                table_data.append(row)

    print(f"Detailed analysis complete. Files saved to {OUT_DIR}")
    print("\n--- Stepwise Metrics Table ---")
    print(f"{'Step':>5} | {'AUC':>7} | {'Acc@0.5':>7} | {'N':>5}")
    print("-" * 35)
    for row in table_data:
        print(f"{row['step']:>5} | {row['auc']:>7.4f} | {row['acc_0.5']:>7.4f} | {row['n']:>5}")

if __name__ == "__main__":
    run_detailed_analysis()
