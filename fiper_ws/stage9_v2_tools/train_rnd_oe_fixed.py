"""
train_rnd_oe_fixed.py – Fixed RND-OE training with feature masking and clipping.
Fixes the feature explosion bug from the original train_rnd_oe.py.

Key changes vs original:
1. Assigns names to all 81 features
2. Computes std on training data and drops features with std < 1e-4
3. Saves feature_mask, feature_names (kept & dropped) in checkpoint
4. Clips normalized values to [-10, 10] at train and eval time
5. Reports max absolute normalized value before/after clipping

Usage:
    python3 train_rnd_oe_fixed.py \
        --train-jsonl train_success_id.jsonl \
        --out-dir /path/to/output \
        --hidden-dim 256 --output-dim 128 --epochs 30 --batch-size 512 --lr 0.001
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

try:
    import torch
    import torch.nn as nn
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("WARNING: torch not available, will use numpy fallback")

# --- Feature names for all 81 dimensions ---
FEATURE_NAMES = []
for step_i in range(10):
    for dim_j in range(7):
        FEATURE_NAMES.append(f"action_step{step_i}_dim{dim_j}")
# flowtrace (7)
for key in ["action_norm_mean", "action_norm_std", "action_norm_max",
            "gripper_change_count", "gripper_open_fraction",
            "direction_change_count", "smoothness_score"]:
    FEATURE_NAMES.append(f"flowtrace_{key}")
# outcome (3)
for key in ["reward_sum_H", "steps_executed", "H_used"]:
    FEATURE_NAMES.append(f"outcome_{key}")
# history (1)
FEATURE_NAMES.append("history_length")
assert len(FEATURE_NAMES) == 81, f"Expected 81 feature names, got {len(FEATURE_NAMES)}"


def extract_numeric_features(sample: dict) -> list[float]:
    """Extract a fixed-size 81-dim numeric feature vector from a sample."""
    feats: list[float] = []
    ca = sample.get("candidate_action", {})
    action_norm = ca.get("candidate_action_normalized") or ca.get("candidate_action_env") or []
    flat_action = []
    for step in action_norm:
        if isinstance(step, list):
            flat_action.extend(step)
        else:
            flat_action.append(float(step))
    flat_action = flat_action[:70]
    flat_action += [0.0] * (70 - len(flat_action))
    feats.extend(flat_action)

    ft = ca.get("flowtrace_features", {})
    for key in ["action_norm_mean", "action_norm_std", "action_norm_max",
                 "gripper_change_count", "gripper_open_fraction",
                 "direction_change_count", "smoothness_score"]:
        val = ft.get(key)
        feats.append(float(val) if val is not None else 0.0)

    outcome = sample.get("outcome", {})
    for key in ["reward_sum_H", "steps_executed", "H_used"]:
        val = outcome.get(key)
        feats.append(float(val) if val is not None else 0.0)

    hist = sample.get("history", [])
    feats.append(float(len(hist)))

    return feats  # 81 dims


def build_feature_matrix(samples: list[dict]) -> np.ndarray:
    """Convert samples to a numeric feature matrix."""
    feats = [extract_numeric_features(s) for s in samples]
    return np.array(feats, dtype=np.float32)


def load_success_only_samples(jsonl_paths: list[str], max_risk: float = 0.20,
                               min_conf: float = 0.80) -> list[dict]:
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


def compute_feature_mask(X: np.ndarray, min_std: float = 1e-4) -> dict:
    """Compute feature statistics and identify stable (non-constant) features.
    
    Returns dict with:
        feature_mask: boolean array (True = keep)
        kept_names: list of kept feature names
        dropped_names: list of dropped feature names
        kept_indices: list of kept feature indices
        dropped_indices: list of dropped feature indices
        raw_mean: mean of all 81 features
        raw_std: std of all 81 features
    """
    raw_mean = X.mean(axis=0)
    raw_std = X.std(axis=0)
    
    feature_mask = raw_std >= min_std
    
    kept_names = [FEATURE_NAMES[i] for i in range(len(FEATURE_NAMES)) if feature_mask[i]]
    dropped_names = [FEATURE_NAMES[i] for i in range(len(FEATURE_NAMES)) if not feature_mask[i]]
    kept_indices = [i for i in range(len(FEATURE_NAMES)) if feature_mask[i]]
    dropped_indices = [i for i in range(len(FEATURE_NAMES)) if not feature_mask[i]]
    
    print(f"\n=== Feature Mask Analysis ===")
    print(f"Total features: {len(FEATURE_NAMES)}")
    print(f"Kept features: {len(kept_names)} (std >= {min_std})")
    print(f"Dropped features: {len(dropped_names)} (std < {min_std})")
    print(f"\nDropped features:")
    for i in dropped_indices:
        print(f"  [{i}] {FEATURE_NAMES[i]}: mean={raw_mean[i]:.6f}, std={raw_std[i]:.2e}")
    print(f"\nKept feature std range: [{raw_std[feature_mask].min():.6f}, {raw_std[feature_mask].max():.6f}]")
    
    return {
        "feature_mask": feature_mask,
        "kept_names": kept_names,
        "dropped_names": dropped_names,
        "kept_indices": kept_indices,
        "dropped_indices": dropped_indices,
        "raw_mean": raw_mean,
        "raw_std": raw_std,
    }


def train_rnd_torch_fixed(X_raw: np.ndarray, mask_info: dict,
                           hidden_dim: int, output_dim: int,
                           epochs: int, batch_size: int, lr: float,
                           save_path: Path, clip_val: float = 10.0) -> dict:
    """Train RND using PyTorch with feature masking and clipping."""
    import torch
    import torch.nn as nn
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Apply feature mask
    mask = mask_info["feature_mask"]
    X = X_raw[:, mask]
    input_dim = X.shape[1]
    
    print(f"\nTraining RND-OE on {X.shape[0]} samples x {input_dim} features (device={device})")
    
    # Compute mean/std on masked features only
    X_tensor = torch.from_numpy(X).to(device)
    X_mean = X_tensor.mean(dim=0, keepdim=True)
    X_std = X_tensor.std(dim=0, keepdim=True).clamp(min=1e-6)
    
    # Normalize and clip
    X_norm = (X_tensor - X_mean) / X_std
    max_abs_before_clip = float(X_norm.abs().max().item())
    X_norm = X_norm.clamp(-clip_val, clip_val)
    max_abs_after_clip = float(X_norm.abs().max().item())
    
    print(f"Max |normalized| before clip: {max_abs_before_clip:.4f}")
    print(f"Max |normalized| after clip:  {max_abs_after_clip:.4f}")
    
    # Target network (frozen random)
    target_net = nn.Sequential(
        nn.Linear(input_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    ).to(device)
    for p in target_net.parameters():
        p.requires_grad = False
    
    # Predictor network (trained)
    predictor_net = nn.Sequential(
        nn.Linear(input_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    ).to(device)
    
    optimizer = torch.optim.Adam(predictor_net.parameters(), lr=lr)
    
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
    
    # Save checkpoint with all metadata
    save_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({
        "target_net": target_net.state_dict(),
        "predictor_net": predictor_net.state_dict(),
        "X_mean": X_mean.cpu(),
        "X_std": X_std.cpu(),
        "feature_mask": mask.tolist(),           # boolean list, len=81
        "kept_feature_names": mask_info["kept_names"],
        "dropped_feature_names": mask_info["dropped_names"],
        "kept_indices": mask_info["kept_indices"],
        "dropped_indices": mask_info["dropped_indices"],
        "all_feature_names": FEATURE_NAMES,
        "clip_val": clip_val,
        "input_dim": input_dim,                  # after masking
        "original_dim": len(FEATURE_NAMES),      # before masking (81)
        "hidden_dim": hidden_dim,
        "output_dim": output_dim,
        "training_samples": len(X),
        "best_loss": best_loss,
        "max_abs_before_clip": max_abs_before_clip,
        "max_abs_after_clip": max_abs_after_clip,
    }, str(save_path))
    print(f"  RND model saved to {save_path}")
    
    return {
        "best_loss": best_loss,
        "epochs": epochs,
        "samples": len(X),
        "input_dim": input_dim,
        "dropped_count": len(mask_info["dropped_names"]),
        "max_abs_before_clip": max_abs_before_clip,
        "max_abs_after_clip": max_abs_after_clip,
        "history": history[-5:],
    }


def score_samples_fixed(model_path: Path, samples: list[dict],
                         clip_val: float = 10.0) -> list[dict]:
    """Score samples with the fixed RND model (with feature masking and clipping)."""
    X_raw = build_feature_matrix(samples)
    
    if not TORCH_AVAILABLE or model_path.suffix != ".pt":
        raise RuntimeError("Fixed scoring requires PyTorch and .pt checkpoint")
    
    import torch
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(str(model_path), map_location=device, weights_only=False)
    
    # Apply feature mask
    feature_mask = np.array(ckpt["feature_mask"])
    X = X_raw[:, feature_mask]
    
    input_dim = ckpt["input_dim"]
    hidden_dim = ckpt["hidden_dim"]
    output_dim = ckpt["output_dim"]
    clip_val = ckpt.get("clip_val", clip_val)
    
    assert X.shape[1] == input_dim, f"Feature dim mismatch: {X.shape[1]} vs checkpoint {input_dim}"
    
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
    
    # Normalize and clip
    X_norm = (X_tensor - X_mean) / X_std
    max_abs_raw = float(X_norm.abs().max().item())
    X_norm = X_norm.clamp(-clip_val, clip_val)
    
    with torch.no_grad():
        t_out = target_net(X_norm)
        p_out = predictor_net(X_norm)
        scores = ((t_out - p_out) ** 2).mean(dim=1).cpu().numpy()
    
    results = []
    for i, s in enumerate(samples):
        results.append({
            "sample_id": s.get("sample_id", f"idx_{i}"),
            "rnd_score": float(scores[i]),
        })
    return results, max_abs_raw


def main():
    parser = argparse.ArgumentParser(description="Train fixed RND-OE with feature masking")
    parser.add_argument("--train-jsonl", required=True, help="Training JSONL (success-only)")
    parser.add_argument("--out-dir", required=True, help="Output directory")
    parser.add_argument("--hidden-dim", type=int, default=256)
    parser.add_argument("--output-dim", type=int, default=128)
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--max-risk", type=float, default=0.20)
    parser.add_argument("--min-conf", type=float, default=0.80)
    parser.add_argument("--min-std", type=float, default=1e-4,
                        help="Minimum std to keep a feature (default 1e-4)")
    parser.add_argument("--clip-val", type=float, default=10.0,
                        help="Clip normalized values to [-clip_val, clip_val]")
    args = parser.parse_args()
    
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Load training data
    samples = load_success_only_samples([args.train_jsonl], args.max_risk, args.min_conf)
    if len(samples) < 10:
        print(f"ERROR: Only {len(samples)} success samples, need >= 10")
        return
    
    X = build_feature_matrix(samples)
    print(f"Raw feature matrix: {X.shape}")
    
    # Compute feature mask
    mask_info = compute_feature_mask(X, min_std=args.min_std)
    
    # Save mask info
    mask_report = {
        "total_features": len(FEATURE_NAMES),
        "kept_count": len(mask_info["kept_names"]),
        "dropped_count": len(mask_info["dropped_names"]),
        "kept_names": mask_info["kept_names"],
        "dropped_names": mask_info["dropped_names"],
        "dropped_indices": mask_info["dropped_indices"],
        "min_std_threshold": args.min_std,
    }
    (out_dir / "feature_mask_report.json").write_text(
        json.dumps(mask_report, indent=2) + "\n"
    )
    
    # Train
    model_path = out_dir / "rnd_oe_fixed.pt"
    result = train_rnd_torch_fixed(
        X, mask_info, args.hidden_dim, args.output_dim,
        args.epochs, args.batch_size, args.lr, model_path,
        clip_val=args.clip_val,
    )
    
    result["feature_mask_report"] = mask_report
    result["model_path"] = str(model_path)
    (out_dir / "rnd_training_summary.json").write_text(
        json.dumps(result, indent=2, default=str) + "\n"
    )
    print("\n=== Fixed RND-OE training complete ===")


if __name__ == "__main__":
    main()
