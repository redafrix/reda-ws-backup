#!/usr/bin/env python3
"""
evaluate_action_heavy_ood_object.py - Standalone script to evaluate fixed action-heavy RND
on the OOD-object (unseen tasks in seen suites) split, as well as the ID, OOD-task, and OOD-suite splits.

It also extracts and evaluates a leakage-free subset of the OOD-object split by cross-referencing
the training set sample IDs.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np
import torch
import torch.nn as nn

# ---- CONFIG ----
CAMPAIGN_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/success_only_fiper_20260521_102354")
DATASETS_DIR = CAMPAIGN_DIR / "datasets"
ENRICHED_DIR = CAMPAIGN_DIR / "rnd_observation_only_fix_20260521_112832"
FIXED_RND_DIR = CAMPAIGN_DIR / "fiper" / "rnd_success_only_fixed"

TRAIN_SPLIT_ORIG = DATASETS_DIR / "train_success_id.jsonl"
MODEL_PATH = FIXED_RND_DIR / "rnd_oe_fixed.pt"
THRESHOLDS_PATH = FIXED_RND_DIR / "rnd_conformal_thresholds.json"

SPLITS_TO_EVAL = {
    "test_success_id": ENRICHED_DIR / "test_success_id_enriched.jsonl",
    "test_success_ood_task": ENRICHED_DIR / "test_success_ood_task_enriched.jsonl",
    "test_success_ood_suite": ENRICHED_DIR / "test_success_ood_suite_enriched.jsonl",
    "test_success_ood_object": ENRICHED_DIR / "test_success_ood_object_enriched.jsonl",
}

# --- Action-Heavy Feature Extractor (81 dims) ---
def extract_numeric_features(sample: dict) -> list[float]:
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

    return feats

def build_feature_matrix(samples: list[dict]) -> np.ndarray:
    feats = [extract_numeric_features(s) for s in samples]
    return np.array(feats, dtype=np.float32)

def score_samples_fixed(model_path: Path, samples: list[dict], clip_val: float = 10.0) -> tuple[list[dict], float]:
    X_raw = build_feature_matrix(samples)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(str(model_path), map_location=device, weights_only=False)
    
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

def load_jsonl(path: Path) -> list[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    print("=" * 80)
    print("FIXED ACTION-HEAVY RND - OOD-OBJECT & SPATIAL GENERALIZATION EVALUATION")
    print("=" * 80)
    
    if not MODEL_PATH.exists():
        print(f"ERROR: Model checkpoint not found at {MODEL_PATH}")
        sys.exit(1)
    if not THRESHOLDS_PATH.exists():
        print(f"ERROR: Thresholds file not found at {THRESHOLDS_PATH}")
        sys.exit(1)
        
    # Load thresholds
    with THRESHOLDS_PATH.open() as f:
        thresholds = json.load(f)
    q90, q95, q99 = thresholds["q90"], thresholds["q95"], thresholds["q99"]
    print(f"Loaded conformal thresholds (calibrated on calib_success_id):")
    print(f"  q90 = {q90:.8f}")
    print(f"  q95 = {q95:.8f}")
    print(f"  q99 = {q99:.8f}\n")
    
    # Load training set sample IDs to check for leakage
    print(f"Loading original training split to audit leakage: {TRAIN_SPLIT_ORIG}")
    train_samples = load_jsonl(TRAIN_SPLIT_ORIG)
    train_ids = {s["sample_id"] for s in train_samples}
    print(f"Loaded {len(train_ids)} unique training sample IDs.\n")
    
    eval_results = {}
    
    # Evaluate standard splits
    for name, path in SPLITS_TO_EVAL.items():
        if not path.exists():
            print(f"WARNING: Split file {path.name} not found, skipping.")
            continue
            
        print(f"Evaluating {name} from {path.name}...")
        samples = load_jsonl(path)
        scored, max_abs = score_samples_fixed(MODEL_PATH, samples)
        scores = np.array([s["rnd_score"] for s in scored])
        
        fa_90 = float((scores > q90).mean())
        fa_95 = float((scores > q95).mean())
        fa_99 = float((scores > q99).mean())
        
        eval_results[name] = {
            "count": len(samples),
            "mean_rnd": float(scores.mean()),
            "std_rnd": float(scores.std()),
            "fa_90": fa_90,
            "fa_95": fa_95,
            "fa_99": fa_99,
            "max_abs_norm": max_abs,
            "all_finite": bool(np.all(np.isfinite(scores))),
        }
        print(f"  Count: {len(samples)}")
        print(f"  Mean RND: {scores.mean():.6f} (std={scores.std():.6f})")
        print(f"  False Alarm @ q90: {fa_90*100:.2f}%")
        print(f"  False Alarm @ q95: {fa_95*100:.2f}%")
        print(f"  False Alarm @ q99: {fa_99*100:.2f}%")
        print("-" * 50)
        
        # If this is the OOD-object split, also perform the leakage-free subset analysis
        if name == "test_success_ood_object":
            print("\nEvaluating LEAKAGE-FREE SUBSET of test_success_ood_object...")
            # Filter out any samples whose IDs exist in the train split
            leak_free_samples = [s for s in samples if s["sample_id"] not in train_ids]
            leaked_count = len(samples) - len(leak_free_samples)
            
            print(f"  Leaked samples (present in training set): {leaked_count}")
            print(f"  Leakage-free samples (moved from test/calib sets): {len(leak_free_samples)}")
            
            if len(leak_free_samples) > 0:
                scored_lf, max_abs_lf = score_samples_fixed(MODEL_PATH, leak_free_samples)
                scores_lf = np.array([s["rnd_score"] for s in scored_lf])
                
                fa_90_lf = float((scores_lf > q90).mean())
                fa_95_lf = float((scores_lf > q95).mean())
                fa_99_lf = float((scores_lf > q99).mean())
                
                eval_results["test_success_ood_object_leakage_free"] = {
                    "count": len(leak_free_samples),
                    "mean_rnd": float(scores_lf.mean()),
                    "std_rnd": float(scores_lf.std()),
                    "fa_90": fa_90_lf,
                    "fa_95": fa_95_lf,
                    "fa_99": fa_99_lf,
                    "max_abs_norm": max_abs_lf,
                    "all_finite": bool(np.all(np.isfinite(scores_lf))),
                }
                print(f"  Mean RND (LF): {scores_lf.mean():.6f} (std={scores_lf.std():.6f})")
                print(f"  False Alarm @ q90 (LF): {fa_90_lf*100:.2f}%")
                print(f"  False Alarm @ q95 (LF): {fa_95_lf*100:.2f}%")
                print(f"  False Alarm @ q99 (LF): {fa_99_lf*100:.2f}%")
            else:
                print("  ERROR: No leakage-free samples found in OOD-object split!")
            print("=" * 80)
            
    # Save output summary
    out_summary_path = FIXED_RND_DIR / "action_heavy_ood_object_eval.json"
    out_summary_path.write_text(json.dumps(eval_results, indent=2) + "\n")
    print(f"Saved evaluation results to {out_summary_path}")

if __name__ == "__main__":
    main()
