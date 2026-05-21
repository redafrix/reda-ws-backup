"""
train_rnd_oe.py – Train an RND (Random Network Distillation) model on success-only data.
Part of the FIPER bridge for Stage 9.

Usage:
    python3 -m stage9_fiper_bridge.train_rnd_oe \
        --jsonl safe.jsonl expert.jsonl \
        --out-dir /path/to/output \
        --hidden-dim 256 --output-dim 128 --epochs 30 --batch-size 512

Only samples with risk_score <= 0.20 and risk_confidence >= 0.80 are used.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

try:
    import torch
    import torch.nn as nn
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False


def extract_numeric_features(sample: dict) -> list[float]:
    """Extract a fixed-size numeric feature vector from a sample."""
    feats: list[float] = []
    # candidate action (normalized, 7-dim per step, 10 steps = 70)
    ca = sample.get("candidate_action", {})
    action_norm = ca.get("candidate_action_normalized") or ca.get("candidate_action_env") or []
    flat_action = []
    for step in action_norm:
        if isinstance(step, list):
            flat_action.extend(step)
        else:
            flat_action.append(float(step))
    # Pad/truncate to 70
    flat_action = flat_action[:70]
    flat_action += [0.0] * (70 - len(flat_action))
    feats.extend(flat_action)

    # flowtrace features if available
    ft = ca.get("flowtrace_features", {})
    for key in ["action_norm_mean", "action_norm_std", "action_norm_max",
                 "gripper_change_count", "gripper_open_fraction",
                 "direction_change_count", "smoothness_score"]:
        val = ft.get(key)
        feats.append(float(val) if val is not None else 0.0)

    # outcome features
    outcome = sample.get("outcome", {})
    for key in ["reward_sum_H", "steps_executed", "H_used"]:
        val = outcome.get(key)
        feats.append(float(val) if val is not None else 0.0)

    # history length
    hist = sample.get("history", [])
    feats.append(float(len(hist)))

    return feats  # 70 + 7 + 3 + 1 = 81 dims


def load_success_only_samples(jsonl_paths: list[str], max_risk: float = 0.20, min_conf: float = 0.80) -> list[dict]:
    """Load samples, keep only success/low-risk ones for RND training."""
    samples = []
    stats = Counter()
    for path_str in jsonl_paths:
        path = Path(path_str)
        if not path.exists():
            print(f"WARN: {path} not found, skipping")
            continue
        with path.open() as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                stats["total"] += 1
                cr = row.get("continuous_risk", {})
                if not isinstance(cr, dict):
                    cr = row.get("label", {})
                    if not isinstance(cr, dict):
                        cr = {}
                risk_score = cr.get("risk_score")
                risk_conf = cr.get("risk_confidence")
                risk_bin = cr.get("risk_bin", "")
                if risk_score is None:
                    stats["no_risk_score"] += 1
                    continue
                risk_score = float(risk_score)
                risk_conf = float(risk_conf) if risk_conf is not None else 1.0
                if risk_score <= max_risk and risk_conf >= min_conf:
                    samples.append(row)
                    stats["accepted"] += 1
                elif risk_bin in ("SAFE_STRONG", "SAFE_WEAK"):
                    samples.append(row)
                    stats["accepted_by_bin"] += 1
                else:
                    stats["rejected"] += 1
    print(f"RND training data: {json.dumps(dict(stats), indent=2)}")
    return samples


def build_feature_matrix(samples: list[dict]) -> np.ndarray:
    """Convert samples to a numeric feature matrix."""
    feats = [extract_numeric_features(s) for s in samples]
    return np.array(feats, dtype=np.float32)


def train_rnd_torch(X: np.ndarray, hidden_dim: int, output_dim: int,
                    epochs: int, batch_size: int, lr: float,
                    save_path: Path) -> dict:
    """Train RND using PyTorch."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_dim = X.shape[1]

    # Target network (frozen random)
    target_net = nn.Sequential(
        nn.Linear(input_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    ).to(device)
    for p in target_net.parameters():
        p.requires_grad = False

    # Predictor network (trained)
    predictor_net = nn.Sequential(
        nn.Linear(input_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    ).to(device)

    optimizer = torch.optim.Adam(predictor_net.parameters(), lr=lr)
    X_tensor = torch.from_numpy(X).to(device)

    # Normalize
    X_mean = X_tensor.mean(dim=0, keepdim=True)
    X_std = X_tensor.std(dim=0, keepdim=True).clamp(min=1e-6)
    X_norm = (X_tensor - X_mean) / X_std

    best_loss = float("inf")
    history = []

    for epoch in range(epochs):
        indices = torch.randperm(len(X_norm))
        epoch_loss = 0.0
        n_batches = 0
        for i in range(0, len(X_norm), batch_size):
            batch = X_norm[indices[i:i + batch_size]]
            with torch.no_grad():
                target_out = target_net(batch)
            pred_out = predictor_net(batch)
            loss = ((pred_out - target_out) ** 2).mean()
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1
        avg_loss = epoch_loss / max(1, n_batches)
        history.append(avg_loss)
        if avg_loss < best_loss:
            best_loss = avg_loss
        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  RND epoch {epoch+1}/{epochs}: loss={avg_loss:.6f} best={best_loss:.6f}")

    # Save
    save_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({
        "target_net": target_net.state_dict(),
        "predictor_net": predictor_net.state_dict(),
        "X_mean": X_mean.cpu(),
        "X_std": X_std.cpu(),
        "input_dim": input_dim,
        "hidden_dim": hidden_dim,
        "output_dim": output_dim,
        "training_samples": len(X),
        "best_loss": best_loss,
    }, str(save_path))
    print(f"  RND model saved to {save_path}")
    return {"best_loss": best_loss, "epochs": epochs, "samples": len(X), "history": history[-5:]}


def train_rnd_numpy(X: np.ndarray, hidden_dim: int, output_dim: int,
                    epochs: int, save_path: Path) -> dict:
    """Fallback numpy-only RND using random projections."""
    input_dim = X.shape[1]
    rng = np.random.RandomState(42)

    # Normalize
    X_mean = X.mean(axis=0, keepdims=True)
    X_std = X.std(axis=0, keepdims=True).clip(min=1e-6)
    X_norm = (X - X_mean) / X_std

    # Random projection target
    W1 = rng.randn(input_dim, hidden_dim).astype(np.float32) * 0.1
    W2 = rng.randn(hidden_dim, output_dim).astype(np.float32) * 0.1

    target_out = np.maximum(0, X_norm @ W1) @ W2  # simple 1-layer ReLU + linear

    # Store mean/std of target outputs for scoring
    target_mean = target_out.mean(axis=0, keepdims=True)
    target_std = target_out.std(axis=0, keepdims=True).clip(min=1e-6)

    save_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez(str(save_path),
             W1=W1, W2=W2,
             X_mean=X_mean, X_std=X_std,
             target_mean=target_mean, target_std=target_std,
             training_samples=len(X))
    print(f"  RND (numpy fallback) saved to {save_path}")
    return {"method": "numpy_random_projection", "samples": len(X)}


def score_samples(model_path: Path, samples: list[dict]) -> list[dict]:
    """Score samples with trained RND model. Returns list of {sample_id, rnd_score}."""
    X = build_feature_matrix(samples)

    if TORCH_AVAILABLE and model_path.suffix == ".pt":
        import torch
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        ckpt = torch.load(str(model_path), map_location=device)
        input_dim = ckpt["input_dim"]
        hidden_dim = ckpt["hidden_dim"]
        output_dim = ckpt["output_dim"]

        target_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        ).to(device)
        target_net.load_state_dict(ckpt["target_net"])

        predictor_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        ).to(device)
        predictor_net.load_state_dict(ckpt["predictor_net"])

        X_mean = ckpt["X_mean"].to(device)
        X_std = ckpt["X_std"].to(device)
        X_tensor = torch.from_numpy(X).to(device)
        X_norm = (X_tensor - X_mean) / X_std

        with torch.no_grad():
            t_out = target_net(X_norm)
            p_out = predictor_net(X_norm)
            scores = ((t_out - p_out) ** 2).mean(dim=1).cpu().numpy()
    else:
        # numpy fallback
        data = np.load(str(model_path))
        X_mean = data["X_mean"]
        X_std = data["X_std"]
        W1 = data["W1"]
        W2 = data["W2"]
        target_mean = data["target_mean"]
        target_std = data["target_std"]
        X_norm = (X - X_mean) / X_std
        target_out = np.maximum(0, X_norm @ W1) @ W2
        scores = np.mean(((target_out - target_mean) / target_std) ** 2, axis=1)

    results = []
    for i, s in enumerate(samples):
        results.append({
            "sample_id": s.get("sample_id", f"idx_{i}"),
            "rnd_score": float(scores[i]),
            "risk_score": float(s.get("continuous_risk", s.get("label", {})).get("risk_score", -1)),
            "risk_bin": str(s.get("continuous_risk", s.get("label", {})).get("risk_bin", "unknown")),
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="Train RND-OE on success-only data")
    parser.add_argument("--jsonl", nargs="+", required=True, help="JSONL files to load")
    parser.add_argument("--out-dir", required=True, help="Output directory")
    parser.add_argument("--hidden-dim", type=int, default=256)
    parser.add_argument("--output-dim", type=int, default=128)
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--max-risk", type=float, default=0.20)
    parser.add_argument("--min-conf", type=float, default=0.80)
    parser.add_argument("--score-jsonl", nargs="*", help="Additional JSONL files to score after training")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load success-only
    samples = load_success_only_samples(args.jsonl, args.max_risk, args.min_conf)
    if len(samples) < 10:
        print(f"ERROR: Only {len(samples)} success samples found, need at least 10")
        summary = {"error": "not_enough_samples", "count": len(samples)}
        (out_dir / "rnd_training_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
        return

    X = build_feature_matrix(samples)
    print(f"Feature matrix: {X.shape}")

    model_path = out_dir / "rnd_oe_success_only.pt"
    if TORCH_AVAILABLE:
        result = train_rnd_torch(X, args.hidden_dim, args.output_dim,
                                 args.epochs, args.batch_size, args.lr, model_path)
    else:
        model_path = out_dir / "rnd_oe_success_only.npz"
        result = train_rnd_numpy(X, args.hidden_dim, args.output_dim, args.epochs, model_path)

    # Score all input data
    all_score_paths = list(args.jsonl)
    if args.score_jsonl:
        all_score_paths.extend(args.score_jsonl)

    all_scores = []
    for path_str in all_score_paths:
        path = Path(path_str)
        if not path.exists():
            continue
        with path.open() as f:
            file_samples = [json.loads(line) for line in f if line.strip()]
        scored = score_samples(model_path, file_samples)
        for s in scored:
            s["source_file"] = str(path)
        all_scores.extend(scored)

    scores_path = out_dir / "rnd_scores_all.jsonl"
    with scores_path.open("w") as f:
        for s in all_scores:
            f.write(json.dumps(s, default=str) + "\n")
    print(f"Scored {len(all_scores)} samples -> {scores_path}")

    # Compute thresholds
    rnd_vals = np.array([s["rnd_score"] for s in all_scores])
    thresholds = {}
    for q_name, q_val in [("q95", 0.95), ("q99", 0.99), ("q90", 0.90), ("q75", 0.75)]:
        thresholds[q_name] = float(np.quantile(rnd_vals, q_val))
    thresholds["mean"] = float(rnd_vals.mean())
    thresholds["std"] = float(rnd_vals.std())
    thresholds["min"] = float(rnd_vals.min())
    thresholds["max"] = float(rnd_vals.max())

    thresh_path = out_dir / "rnd_conformal_thresholds.json"
    thresh_path.write_text(json.dumps(thresholds, indent=2) + "\n")
    print(f"Thresholds: {json.dumps(thresholds, indent=2)}")

    result["thresholds"] = thresholds
    result["scored_samples"] = len(all_scores)
    result["model_path"] = str(model_path)
    (out_dir / "rnd_training_summary.json").write_text(json.dumps(result, indent=2, default=str) + "\n")
    print("RND-OE training complete.")


if __name__ == "__main__":
    main()
