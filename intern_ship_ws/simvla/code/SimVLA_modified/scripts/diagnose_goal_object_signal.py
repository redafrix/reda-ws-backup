#!/usr/bin/env python3
import argparse
import json
import gzip
from pathlib import Path
import numpy as np
from sklearn.metrics import roc_auc_score, brier_score_loss, accuracy_score, balanced_accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


FEATURE_KEYS = [
    "path_step_mean",
    "last_step_mean",
    "mean_path_var",
    "mean_last_var",
    "max_path_var",
    "max_last_var",
    "denoise_initial_mean",
    "denoise_final_mean",
    "denoise_delta",
    "denoise_slope",
    "denoise_final_max",
    "denoise_spike",
    "denoise_final_gripper",
    "denoise_final_rotation_mean",
]


def open_jsonl(path):
    path = Path(path)
    if str(path).endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, "r", encoding="utf-8")


def load_prefix(path, prefix_step):
    X = []
    y = []

    with open_jsonl(path) as f:
        for line in f:
            if not line.strip():
                continue

            rec = json.loads(line)
            trace = rec.get("uncertainty_trace") or []

            if len(trace) < prefix_step:
                continue

            row = trace[prefix_step - 1]

            feats = []
            ok = True
            for k in FEATURE_KEYS:
                v = row.get(k)
                if v is None:
                    ok = False
                    break
                feats.append(float(v))

            if not ok:
                continue

            X.append(feats)
            y.append(0 if rec.get("success") else 1)  # 1 = failure risk

    return np.asarray(X, dtype=np.float32), np.asarray(y, dtype=np.int64)


def report(name, y, p):
    pred = (p >= 0.5).astype(int)

    out = {
        "name": name,
        "n": int(len(y)),
        "failures": int(y.sum()),
        "failure_rate": float(y.mean()),
        "brier": float(brier_score_loss(y, p)),
        "acc": float(accuracy_score(y, pred)),
        "bal_acc": float(balanced_accuracy_score(y, pred)),
        "mean_pred_success": float(p[y == 0].mean()) if np.any(y == 0) else None,
        "mean_pred_failure": float(p[y == 1].mean()) if np.any(y == 1) else None,
    }

    if len(set(y.tolist())) == 2:
        out["auroc"] = float(roc_auc_score(y, p))
    else:
        out["auroc"] = None

    print(json.dumps(out, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--train_jsonl", required=True)
    ap.add_argument("--val_jsonl", required=True)
    ap.add_argument("--prefix_steps", nargs="+", type=int, default=[50, 75, 100, 120])
    args = ap.parse_args()

    for step in args.prefix_steps:
        print("\n============================================================")
        print(f"PREFIX STEP {step}")
        print("============================================================")

        Xtr, ytr = load_prefix(args.train_jsonl, step)
        Xva, yva = load_prefix(args.val_jsonl, step)

        print(f"train: X={Xtr.shape}, failures={int(ytr.sum())}/{len(ytr)}")
        print(f"val:   X={Xva.shape}, failures={int(yva.sum())}/{len(yva)}")

        # constant train-rate baseline
        p_train = np.full_like(yva, ytr.mean(), dtype=np.float32)
        report("constant_train_failure_rate", yva, p_train)

        # constant val-rate oracle baseline, not deployable, just sanity check
        p_val = np.full_like(yva, yva.mean(), dtype=np.float32)
        report("constant_val_failure_rate_oracle", yva, p_val)

        # logistic regression
        logreg = make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=2000, class_weight=None),
        )
        logreg.fit(Xtr, ytr)
        p = logreg.predict_proba(Xva)[:, 1]
        report("logistic_regression", yva, p)

        # balanced logistic regression
        logreg_bal = make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=2000, class_weight="balanced"),
        )
        logreg_bal.fit(Xtr, ytr)
        p = logreg_bal.predict_proba(Xva)[:, 1]
        report("logistic_regression_balanced", yva, p)

        # random forest
        rf = RandomForestClassifier(
            n_estimators=300,
            max_depth=3,
            min_samples_leaf=10,
            random_state=0,
            class_weight=None,
        )
        rf.fit(Xtr, ytr)
        p = rf.predict_proba(Xva)[:, 1]
        report("random_forest_depth3", yva, p)


if __name__ == "__main__":
    main()
