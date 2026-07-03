#!/usr/bin/env python3
import json
import torch
import torch.nn as nn
import numpy as np
from pathlib import Path

EXP_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546")
SPLIT_PATH = EXP_DIR / "splits" / "success_test.jsonl"
RND_MODEL_PATH = EXP_DIR / "rnd" / "rnd_model.pt"
RND_THRESH_PATH = EXP_DIR / "rnd" / "rnd_thresholds.json"
OUT_DIR = EXP_DIR / "corrupted"
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

def apply_corruption(chunk, corr_type):
    # chunk shape is (10, 7)
    corr_chunk = chunk.copy()
    if corr_type == "zero":
        corr_chunk = np.zeros_like(corr_chunk)
    elif corr_type == "random":
        corr_chunk = np.random.uniform(-1.0, 1.0, size=corr_chunk.shape).astype(np.float32)
    elif corr_type == "shuffled":
        idx = np.arange(10)
        np.random.shuffle(idx)
        corr_chunk = corr_chunk[idx]
    elif corr_type == "reversed":
        corr_chunk = corr_chunk[::-1]
    elif corr_type == "scaled":
        corr_chunk = corr_chunk * 2.0
        # Clip to typical normalized action bounds
        corr_chunk = np.clip(corr_chunk, -1.0, 1.0)
    elif corr_type == "gripper_flipped":
        corr_chunk[:, 6] = -corr_chunk[:, 6]
    elif corr_type == "repeated_first":
        corr_chunk = np.tile(corr_chunk[0], (10, 1)).reshape(10, 7)
    elif corr_type == "noise_low":
        corr_chunk = corr_chunk + np.random.normal(0.0, 0.05, size=corr_chunk.shape).astype(np.float32)
    elif corr_type == "noise_medium":
        corr_chunk = corr_chunk + np.random.normal(0.0, 0.15, size=corr_chunk.shape).astype(np.float32)
    elif corr_type == "noise_high":
        corr_chunk = corr_chunk + np.random.normal(0.0, 0.30, size=corr_chunk.shape).astype(np.float32)
    return corr_chunk

def main():
    # Load model and thresholds
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint = torch.load(str(RND_MODEL_PATH), map_location=device)
    
    with RND_THRESH_PATH.open() as f:
        thresholds = json.load(f)
    q95 = thresholds["q95"]
    print(f"Loaded q95 threshold: {q95:.6f}")

    active_indices = checkpoint["active_indices"]
    mean_active = checkpoint["mean_active"]
    std_active = checkpoint["std_active"]
    input_dim = len(active_indices)

    target_net = RNDMLP(input_dim).to(device)
    target_net.load_state_dict(checkpoint["target_net"])
    target_net.eval()

    predictor_net = RNDMLP(input_dim).to(device)
    predictor_net.load_state_dict(checkpoint["predictor_net"])
    predictor_net.eval()

    # Load success test rows
    rows = []
    with SPLIT_PATH.open() as f:
        for line in f:
            if not line.strip():
                continue
            rows.append(json.loads(line))

    print(f"Loaded {len(rows)} test samples.")

    corruptions = [
        "clean", "zero", "random", "shuffled", "reversed", 
        "scaled", "gripper_flipped", "repeated_first", 
        "noise_low", "noise_medium", "noise_high"
    ]

    all_corr_results = []
    alarm_rates = {}

    np.random.seed(42)

    for corr in corruptions:
        corr_features = []
        for row in rows:
            chunk = np.array(row["main_candidate_action_chunk_normalized"], dtype=np.float32)
            corr_chunk = apply_corruption(chunk, corr)
            corr_features.append(corr_chunk.flatten())

        corr_features = np.array(corr_features, dtype=np.float32)
        # Normalize
        X_act = corr_features[:, active_indices]
        X_norm = (X_act - mean_active) / std_active
        X_norm = np.clip(X_norm, -10.0, 10.0)

        t_split = torch.tensor(X_norm, dtype=torch.float32).to(device)
        with torch.no_grad():
            target_out = target_net(t_split)
            pred_out = predictor_net(t_split)
            scores = torch.mean((pred_out - target_out) ** 2, dim=-1).cpu().numpy()

        alarms = scores > q95
        alarm_rate = float(np.mean(alarms))
        alarm_rates[corr] = alarm_rate
        print(f"Corruption: {corr:20s} | Mean Score: {np.mean(scores):.6f} | Alarm Rate @ q95: {alarm_rate*100:.2f}%")

        for idx, row in enumerate(rows):
            all_corr_results.append({
                "episode_id": row.get("episode_id"),
                "timestep": row.get("timestep"),
                "suite": row.get("suite"),
                "task_id": row.get("task_id"),
                "corruption_type": corr,
                "rnd_score": float(scores[idx]),
                "alarm": bool(alarms[idx])
            })

    # Save scores
    out_jsonl = OUT_DIR / "corrupted_scores.jsonl"
    with out_jsonl.open("w") as f:
        for r in all_corr_results:
            f.write(json.dumps(r) + "\n")
    print(f"Wrote corrupted scores to {out_jsonl}")

    # Generate MD Report
    report_dir = EXP_DIR / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    md_lines = [
        "# Corrupted-Action Sanity Test Report",
        "",
        "This report evaluates the sensitivity of the trained RND safety monitor to various types of action chunk corruptions.",
        "We apply corruptions to the `success_test` action chunks and measure the alarm rate against the conformal `q95` threshold.",
        "",
        "## Alarm Rates on Corrupted Actions",
        "| Corruption Type | Mean RND Score | Alarm Rate @ q95 (%) | Sensitivity Status |",
        "|---|---|---|---|",
    ]

    for corr in corruptions:
        rate = alarm_rates[corr]
        mean_score = np.mean([r["rnd_score"] for r in all_corr_results if r["corruption_type"] == corr])
        # Status check
        if corr == "clean":
            status = "Nominal (False Alarm)"
        else:
            status = "SENSITIVE (Success)" if rate > 0.50 else "WEAK (Low sensitivity)"
        md_lines.append(f"| `{corr}` | {mean_score:.6f} | {rate*100:.2f}% | {status} |")

    md_lines.extend([
        "",
        "## Analysis of Results",
        "- **Clean Success Chunks**: Alarms at approximately the false alarm rate target (~5%).",
        "- **Severe Corruptions (Zero/Random)**: These represent completely out-of-distribution behaviors and should trigger near 100% alarms.",
        "- **Structural Corruptions (Shuffled/Reversed/Repeated)**: These evaluate whether the model is sensitive to temporal ordering and structure, which is crucial for action-heavy risk detectors.",
        "- **Noise Sensitivity**: Low noise should trigger fewer alarms, while high noise should trigger significant alarms, showing graceful scaling."
    ])

    with (report_dir / "corrupted_action_sanity_report.md").open("w") as f:
        f.write("\n".join(md_lines))

    print("Corrupted action sanity test complete.")

if __name__ == "__main__":
    main()
