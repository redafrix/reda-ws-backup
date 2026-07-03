#!/usr/bin/env python3
import json
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from pathlib import Path

SPLITS_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/splits")
OUT_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/rnd")
OUT_DIR.mkdir(parents=True, exist_ok=True)

class RNDMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim=256, output_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    def forward(self, x):
        return self.net(x)

def load_features(split_name):
    path = SPLITS_DIR / f"{split_name}.jsonl"
    if not path.exists():
        return None, []
    
    features = []
    rows = []
    with path.open() as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            # main_candidate_action_chunk_normalized is (10, 7)
            chunk = row.get("main_candidate_action_chunk_normalized")
            if not chunk or len(chunk) != 10:
                continue
            flat_chunk = np.array(chunk, dtype=np.float32).flatten() # 70-dim
            features.append(flat_chunk)
            rows.append(row)
    return np.array(features, dtype=np.float32), rows

def main():
    print("Loading success_train features...")
    X_train, train_rows = load_features("success_train")
    print(f"X_train shape: {X_train.shape}")

    print("Loading success_calib features...")
    X_calib, calib_rows = load_features("success_calib")
    print(f"X_calib shape: {X_calib.shape}")

    # Robust normalization parameters computed on success_train
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    
    # drop std < 1e-4
    mask = std >= 1e-4
    active_indices = np.where(mask)[0]
    
    print(f"Active features: {len(active_indices)} / {X_train.shape[1]}")
    
    mean_active = mean[active_indices]
    std_active = std[active_indices]

    def normalize(X):
        X_act = X[:, active_indices]
        X_norm = (X_act - mean_active) / std_active
        return np.clip(X_norm, -10.0, 10.0)

    # Normalize inputs
    X_train_norm = normalize(X_train)
    X_calib_norm = normalize(X_calib)

    input_dim = len(active_indices)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Initialize RND networks
    torch.manual_seed(42)
    target_net = RNDMLP(input_dim).to(device)
    # Predictor network
    predictor_net = RNDMLP(input_dim).to(device)
    
    # Freeze target network
    for p in target_net.parameters():
        p.requires_grad = False

    optimizer = optim.Adam(predictor_net.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    # Convert to PyTorch tensors
    t_train = torch.tensor(X_train_norm, dtype=torch.float32).to(device)
    t_calib = torch.tensor(X_calib_norm, dtype=torch.float32).to(device)

    # Training parameters
    epochs = 150
    batch_size = 256
    best_val_loss = float("inf")
    patience = 15
    patience_counter = 0
    best_weights = None

    # Early stopping loop
    for epoch in range(epochs):
        predictor_net.train()
        permutation = torch.randperm(t_train.size(0))
        epoch_loss = 0.0
        
        for i in range(0, t_train.size(0), batch_size):
            indices = permutation[i:i+batch_size]
            batch_x = t_train[indices]
            
            optimizer.zero_grad()
            with torch.no_grad():
                target_out = target_net(batch_x)
            pred_out = predictor_net(batch_x)
            
            loss = criterion(pred_out, target_out)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * len(indices)

        epoch_loss /= len(t_train)

        # Validation
        predictor_net.eval()
        with torch.no_grad():
            target_val = target_net(t_calib)
            pred_val = predictor_net(t_calib)
            val_loss = criterion(pred_val, target_val).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            best_weights = {k: v.cpu().clone() for k, v in predictor_net.state_dict().items()}
        else:
            patience_counter += 1

        if (epoch + 1) % 10 == 0 or epoch == 0:
            print(f"Epoch {epoch+1:03d} | Train Loss: {epoch_loss:.6f} | Val Loss: {val_loss:.6f}")

        if patience_counter >= patience:
            print(f"Early stopping at epoch {epoch+1}!")
            break

    # Restore best weights
    predictor_net.load_state_dict({k: v.to(device) for k, v in best_weights.items()})

    # Evaluate on all splits
    splits = [
        "success_train", "success_calib", "success_test", "ood_suite_success_test",
        "failure_eval_all", "failure_eval_early", "failure_eval_late", "failure_eval_near_end"
    ]

    all_scores = []
    
    predictor_net.eval()
    for split in splits:
        X_split, rows = load_features(split)
        if X_split is None or len(X_split) == 0:
            print(f"Split {split} is empty or missing, skipping evaluation.")
            continue
        
        X_split_norm = normalize(X_split)
        t_split = torch.tensor(X_split_norm, dtype=torch.float32).to(device)
        
        with torch.no_grad():
            target_out = target_net(t_split)
            pred_out = predictor_net(t_split)
            # RND score is the per-sample mean squared error
            losses = torch.mean((pred_out - target_out) ** 2, dim=-1).cpu().numpy()

        for idx, row in enumerate(rows):
            score_data = {
                "episode_id": row.get("episode_id"),
                "timestep": row.get("timestep"),
                "suite": row.get("suite"),
                "task_id": row.get("task_id"),
                "episode_outcome": row.get("episode_outcome"),
                "rnd_score": float(losses[idx]),
                "split": split
            }
            all_scores.append(score_data)

    # Save rnd_scores_all.jsonl
    scores_path = OUT_DIR / "rnd_scores_all.jsonl"
    with scores_path.open("w") as f:
        for s in all_scores:
            f.write(json.dumps(s) + "\n")
    print(f"Wrote scored samples to {scores_path}")

    # Compute thresholds on success_calib only
    calib_scores = [s["rnd_score"] for s in all_scores if s["split"] == "success_calib"]
    calib_scores = np.array(calib_scores)

    q90 = float(np.percentile(calib_scores, 90))
    q95 = float(np.percentile(calib_scores, 95))
    q99 = float(np.percentile(calib_scores, 99))

    thresholds = {
        "q90": q90,
        "q95": q95,
        "q99": q99
    }
    
    # Save thresholds
    thresh_path = OUT_DIR / "rnd_thresholds.json"
    with thresh_path.open("w") as f:
        json.dump(thresholds, f, indent=2)
    print(f"Wrote thresholds to {thresh_path}")

    # Compute alarm rates across all splits
    split_evals = {}
    for split in splits:
        split_s = [s["rnd_score"] for s in all_scores if s["split"] == split]
        if len(split_s) == 0:
            continue
        split_s = np.array(split_s)
        
        split_evals[split] = {
            "count": len(split_s),
            "mean_score": float(np.mean(split_s)),
            "std_score": float(np.std(split_s)),
            "alarm_q90": float(np.mean(split_s > q90)),
            "alarm_q95": float(np.mean(split_s > q95)),
            "alarm_q99": float(np.mean(split_s > q99))
        }

    # Save model and normalizer
    torch.save({
        "target_net": target_net.state_dict(),
        "predictor_net": predictor_net.state_dict(),
        "mean_active": mean_active,
        "std_active": std_active,
        "active_indices": active_indices,
    }, str(OUT_DIR / "rnd_model.pt"))

    # Generate MD Report
    report_dir = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    md_lines = [
        "# RND Success-Only vs Failure Report",
        "",
        "This report summarizes the training and evaluation of the Action-heavy Random Network Distillation (RND) safety monitor.",
        "",
        "## Conformal Thresholds (Calibrated on `success_calib`)",
        f"- **q90**: {q90:.6f}",
        f"- **q95**: {q95:.6f}",
        f"- **q99**: {q99:.6f}",
        "",
        "## Split Evaluation & Alarm Rates",
        "| Split | Count | Mean RND Score | Alarm @ q90 (%) | Alarm @ q95 (%) | Alarm @ q99 (%) |",
        "|---|---|---|---|---|---|",
    ]

    for split in splits:
        if split not in split_evals:
            continue
        ev = split_evals[split]
        md_lines.append(f"| `{split}` | {ev['count']} | {ev['mean_score']:.6f} | {ev['alarm_q90']*100:.2f}% | {ev['alarm_q95']*100:.2f}% | {ev['alarm_q99']*100:.2f}% |")

    # Assess if the model flags everything safe or not
    # Under normal operation: success_test should be close to 10% (q90), 5% (q95), 1% (q99)
    # Failure evaluations should be significantly higher.
    fail_q95_rate = split_evals.get("failure_eval_all", {}).get("alarm_q95", 0.0)
    test_q95_rate = split_evals.get("success_test", {}).get("alarm_q95", 0.0)

    flags_everything_safe = fail_q95_rate < 0.1
    flags_everything_risky = test_q95_rate > 0.4

    audit_status = "NORMAL (selective alarm)"
    if flags_everything_safe:
        audit_status = "FAILED (flags everything safe)"
    elif flags_everything_risky:
        audit_status = "FAILED (flags everything risky/high false alarm)"

    md_lines.extend([
        "",
        "## Model Diagnostic Audit",
        f"- **False Alarm Rate on success_test @ q95**: {test_q95_rate*100:.2f}% (Target: 5.00%)",
        f"- **Alarm Rate on failure_eval_all @ q95**: {fail_q95_rate*100:.2f}%",
        f"- **Alarm Rate on failure_eval_late @ q95**: {split_evals.get('failure_eval_late', {}).get('alarm_q95', 0.0)*100:.2f}%",
        f"- **Alarm Rate on failure_eval_near_end @ q95**: {split_evals.get('failure_eval_near_end', {}).get('alarm_q95', 0.0)*100:.2f}%",
        f"- **Audit Status**: `{audit_status}`",
    ])

    with (report_dir / "rnd_success_only_vs_failure_report.md").open("w") as f:
        f.write("\n".join(md_lines))

    print("RND training and evaluation complete.")

if __name__ == "__main__":
    main()
