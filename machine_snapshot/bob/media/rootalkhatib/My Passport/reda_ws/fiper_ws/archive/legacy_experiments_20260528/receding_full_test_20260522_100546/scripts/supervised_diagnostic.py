#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, confusion_matrix, brier_score_loss
from sklearn.preprocessing import StandardScaler

EXP_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546")
RND_SCORES_PATH = EXP_DIR / "rnd" / "rnd_scores_all.jsonl"
ACE_SCORES_PATH = EXP_DIR / "ace" / "ace_per_row.jsonl"
SPLITS_DIR = EXP_DIR / "splits"
OUT_DIR = EXP_DIR / "supervised_diagnostic"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    # Load RND scores
    rnd_data = {}
    with RND_SCORES_PATH.open() as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            key = (row["episode_id"], row["timestep"])
            rnd_data[key] = row

    # Load ACE scores
    ace_data = {}
    with ACE_SCORES_PATH.open() as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            key = (row["episode_id"], row["timestep"])
            ace_data[key] = row

    # Load original raw splits to get action chunks
    def load_rows_from_file(filename):
        rows = []
        path = SPLITS_DIR / filename
        with path.open() as f:
            for line in f:
                if not line.strip():
                    continue
                rows.append(json.loads(line))
        return rows

    print("Loading raw splits...")
    train_success_rows = load_rows_from_file("success_train.jsonl")
    test_success_rows = load_rows_from_file("success_test.jsonl")
    failure_all_rows = load_rows_from_file("failure_eval_all.jsonl")

    # Group failure rows by episode
    failure_episodes_dict = {}
    for r in failure_all_rows:
        ep_id = r["episode_id"]
        if ep_id not in failure_episodes_dict:
            failure_episodes_dict[ep_id] = []
        failure_episodes_dict[ep_id].append(r)

    fail_ep_ids = sorted(failure_episodes_dict.keys())
    # Split failures: first 16 for train, remaining 8 for test
    train_fail_eps = fail_ep_ids[:16]
    test_fail_eps = fail_ep_ids[16:]

    train_failure_rows = []
    for ep in train_fail_eps:
        train_failure_rows.extend(failure_episodes_dict[ep])

    test_failure_rows = []
    for ep in test_fail_eps:
        test_failure_rows.extend(failure_episodes_dict[ep])

    print(f"Train failures: {len(train_fail_eps)} eps ({len(train_failure_rows)} rows)")
    print(f"Test failures: {len(test_fail_eps)} eps ({len(test_failure_rows)} rows)")

    # Prepare features and labels
    # Label: 0 for success, 1 for failure/timeout
    def prepare_dataset(success_rows, failure_rows):
        X_action = []
        X_ace = []
        X_rnd = []
        y = []
        
        for r in success_rows:
            key = (r["episode_id"], r["timestep"])
            if key not in rnd_data or key not in ace_data:
                continue
            
            flat_action = np.array(r["main_candidate_action_chunk_normalized"], dtype=np.float32).flatten()
            
            ace_r = ace_data[key]
            # ACE features: entropy, pairwise_distance, stds, etc.
            ace_feats = [
                ace_r["ace_score"],
                ace_r["action_std_mean"],
                ace_r["action_pairwise_distance_mean"],
                ace_r["gripper_std"],
                ace_r["translation_std"],
                ace_r["rotation_std"],
                ace_r["effective_diversity_score"],
                ace_r["near_duplicate_pairs"]
            ]
            
            rnd_feats = [rnd_data[key]["rnd_score"]]
            
            X_action.append(flat_action)
            X_ace.append(ace_feats)
            X_rnd.append(rnd_feats)
            y.append(0)

        for r in failure_rows:
            key = (r["episode_id"], r["timestep"])
            if key not in rnd_data or key not in ace_data:
                continue
            
            flat_action = np.array(r["main_candidate_action_chunk_normalized"], dtype=np.float32).flatten()
            
            ace_r = ace_data[key]
            ace_feats = [
                ace_r["ace_score"],
                ace_r["action_std_mean"],
                ace_r["action_pairwise_distance_mean"],
                ace_r["gripper_std"],
                ace_r["translation_std"],
                ace_r["rotation_std"],
                ace_r["effective_diversity_score"],
                ace_r["near_duplicate_pairs"]
            ]
            
            rnd_feats = [rnd_data[key]["rnd_score"]]
            
            X_action.append(flat_action)
            X_ace.append(ace_feats)
            X_rnd.append(rnd_feats)
            y.append(1)

        return (np.array(X_action, dtype=np.float32), 
                np.array(X_ace, dtype=np.float32), 
                np.array(X_rnd, dtype=np.float32), 
                np.array(y, dtype=np.int32))

    X_train_action, X_train_ace, X_train_rnd, y_train = prepare_dataset(train_success_rows, train_failure_rows)
    X_test_action, X_test_ace, X_test_rnd, y_test = prepare_dataset(test_success_rows, test_failure_rows)

    print(f"Train dataset size: {len(y_train)}")
    print(f"Test dataset size: {len(y_test)}")

    # Feature groups
    feature_groups = {
        "action_only": (X_train_action, X_test_action, "Action Chunk Only"),
        "ace_only": (X_train_ace, X_test_ace, "ACE Metrics Only"),
        "rnd_only": (X_train_rnd, X_test_rnd, "RND Score Only"),
        "ace_rnd": (np.hstack([X_train_ace, X_train_rnd]), np.hstack([X_test_ace, X_test_rnd]), "ACE + RND Combined")
    }

    results = {}

    for name, (X_tr, X_te, label) in feature_groups.items():
        print(f"Training Logistic Regression for {label}...")
        
        # Scale features
        scaler = StandardScaler()
        X_tr_scaled = scaler.fit_transform(X_tr)
        X_te_scaled = scaler.transform(X_te)
        
        clf = LogisticRegression(max_iter=1000, random_state=42)
        clf.fit(X_tr_scaled, y_train)
        
        probs = clf.predict_proba(X_te_scaled)[:, 1]
        preds = clf.predict(X_te_scaled)
        
        auroc = roc_auc_score(y_test, probs)
        auprc = average_precision_score(y_test, probs)
        brier = brier_score_loss(y_test, probs)
        cm = confusion_matrix(y_test, preds)
        
        # If Logistic regression and ace/rnd features, record coefficients
        coefs = None
        if name in ("ace_only", "rnd_only", "ace_rnd"):
            coefs = clf.coef_[0].tolist()

        # Also train a small MLP to see if non-linear works better
        print(f"Training MLP Classifier for {label}...")
        mlp = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=200, random_state=42)
        mlp.fit(X_tr_scaled, y_train)
        mlp_probs = mlp.predict_proba(X_te_scaled)[:, 1]
        mlp_auroc = roc_auc_score(y_test, mlp_probs)
        mlp_auprc = average_precision_score(y_test, mlp_probs)

        results[name] = {
            "label": label,
            "lr_auroc": float(auroc),
            "lr_auprc": float(auprc),
            "lr_brier": float(brier),
            "lr_confusion_matrix": cm.tolist(),
            "lr_coefs": coefs,
            "mlp_auroc": float(mlp_auroc),
            "mlp_auprc": float(mlp_auprc)
        }

    # Save to JSON
    with (OUT_DIR / "supervised_diagnostic_results.json").open("w") as f:
        json.dump(results, f, indent=2)

    # Generate MD Report
    report_dir = EXP_DIR / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    md_lines = [
        "# Episode Outcome Separability Diagnostic Report",
        "",
        "This diagnostic experiment evaluates how well we can distinguish success vs failure steps using various action features via supervised classifiers.",
        "Note: This is an offline diagnostic only, not a runtime safety monitor.",
        "",
        "## Classification Performance Summary",
        "| Feature Set | LR AUROC | LR AUPRC | MLP AUROC | MLP AUPRC | LR Brier Score |",
        "|---|---|---|---|---|---|",
    ]

    for name, res in results.items():
        md_lines.append(f"| {res['label']} | {res['lr_auroc']:.4f} | {res['lr_auprc']:.4f} | {res['mlp_auroc']:.4f} | {res['mlp_auprc']:.4f} | {res['lr_brier']:.4f} |")

    # Add ACE Feature Coefficients (to show feature importance)
    ace_res = results["ace_only"]
    ace_feature_names = [
        "ACE score (Gaussian Entropy)",
        "Action std mean",
        "Action pairwise distance mean",
        "Gripper std",
        "Translation std",
        "Rotation std",
        "Effective diversity score",
        "Near-duplicate pairs"
    ]
    
    md_lines.extend([
        "",
        "## Logistic Regression Coefficient Analysis (ACE Features)",
        "Positive coefficients mean higher values correlate with failure; negative coefficients correlate with success.",
        "",
        "| Feature | Coefficient | Coefficient Magnitude |",
        "|---|---|---|",
    ])

    for fname, coef in zip(ace_feature_names, ace_res["lr_coefs"]):
        md_lines.append(f"| {fname} | {coef:.4f} | {abs(coef):.4f} |")

    with (report_dir / "supervised_episode_outcome_diagnostic_report.md").open("w") as f:
        f.write("\n".join(md_lines))

    print("Supervised diagnostic analysis complete.")

if __name__ == "__main__":
    main()
