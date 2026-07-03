#!/usr/bin/env python3
"""
run_observation_rnd_campaign.py – Full campaign for observation-only RND-OE.

Implements three feature modes:
  A. observation_context_only: proprio(8) + joint_states(7) + ee_states(6) = 21 dims
  B. proprio_only: proprio(8) = 8 dims  
  C. action_free_with_vlm: pooled_vlm_features if available (will be skipped if absent)

Steps:
  1. Train + calibrate for each feature mode
  2. Evaluate false alarm rates on all success splits (ID, OOD-task, OOD-object, OOD-suite)
  3. Score rollout datasets
  4. Reuse ACE, classify FIPER quadrants
  5. Generate mining queue
  6. Save execution summary

Usage:
    python3 run_observation_rnd_campaign.py --enriched-dir <path>
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

try:
    import torch
    import torch.nn as nn
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("ERROR: torch required")
    sys.exit(1)


# ========================================================================
# FEATURE NAMES AND EXTRACTORS
# ========================================================================

FEATURE_MODES = {
    "observation_context_only": {
        "description": "proprio(8) + joint_states(7) + ee_states(6) = 21 dims",
        "names": (
            [f"ee_pos_{i}" for i in range(3)] +
            [f"ee_ori_{i}" for i in range(3)] +
            [f"gripper_{i}" for i in range(2)] +
            [f"joint_{i}" for i in range(7)] +
            [f"ee_state_{i}" for i in range(6)]
        ),
        "target_dim": 21,
    },
    "proprio_only": {
        "description": "proprio(8) = ee_pos(3) + ee_ori(3) + gripper(2)",
        "names": (
            [f"ee_pos_{i}" for i in range(3)] +
            [f"ee_ori_{i}" for i in range(3)] +
            [f"gripper_{i}" for i in range(2)]
        ),
        "target_dim": 8,
    },
}


def extract_features(sample: dict, mode: str) -> list[float]:
    """Extract features for a given mode."""
    cur = sample.get("current", {})
    
    if mode == "observation_context_only":
        proprio = cur.get("proprio", [0.0] * 8)
        joint = cur.get("joint_states", [0.0] * 7)
        ee_states = cur.get("ee_states", [0.0] * 6)
        return list(proprio)[:8] + list(joint)[:7] + list(ee_states)[:6]
    
    elif mode == "proprio_only":
        proprio = cur.get("proprio", [0.0] * 8)
        return list(proprio)[:8]
    
    elif mode == "action_free_with_vlm":
        vlm = sample.get("pooled_vlm_features") or cur.get("pooled_vlm_features")
        if vlm is not None:
            return list(vlm)
        return None  # signal unavailable
    
    raise ValueError(f"Unknown mode: {mode}")


def build_feature_matrix(samples: list[dict], mode: str) -> np.ndarray | None:
    """Build feature matrix for a mode. Returns None if mode unavailable."""
    feats = []
    for s in samples:
        f = extract_features(s, mode)
        if f is None:
            return None  # mode unavailable
        feats.append(f)
    return np.array(feats, dtype=np.float32)


def compute_feature_mask(X: np.ndarray, feature_names: list[str],
                          min_std: float = 1e-4) -> dict:
    """Compute feature statistics and drop near-constant features."""
    raw_mean = X.mean(axis=0)
    raw_std = X.std(axis=0)
    mask = raw_std >= min_std
    
    kept_names = [feature_names[i] for i in range(len(feature_names)) if mask[i]]
    dropped_names = [feature_names[i] for i in range(len(feature_names)) if not mask[i]]
    kept_idx = [i for i in range(len(feature_names)) if mask[i]]
    dropped_idx = [i for i in range(len(feature_names)) if not mask[i]]
    
    print(f"  Total: {len(feature_names)}, Kept: {len(kept_names)}, Dropped: {len(dropped_names)}")
    if dropped_names:
        for i in dropped_idx:
            print(f"    DROPPED [{i}] {feature_names[i]}: mean={raw_mean[i]:.6f}, std={raw_std[i]:.2e}")
    
    return {
        "mask": mask,
        "kept_names": kept_names,
        "dropped_names": dropped_names,
        "kept_indices": kept_idx,
        "dropped_indices": dropped_idx,
        "raw_mean": raw_mean,
        "raw_std": raw_std,
    }


def train_rnd_fixed(X_raw: np.ndarray, mask_info: dict, hidden_dim: int,
                     output_dim: int, epochs: int, batch_size: int, lr: float,
                     save_path: Path, clip_val: float = 10.0,
                     mode_name: str = "", all_feature_names: list[str] = None) -> dict:
    """Train RND-OE with feature masking and clipping."""
    mask = mask_info["mask"]
    X = X_raw[:, mask]
    input_dim = X.shape[1]
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"  Training RND-OE [{mode_name}] on {X.shape[0]}x{input_dim} features (device={device})")
    
    X_t = torch.from_numpy(X).to(device)
    X_mean = X_t.mean(dim=0, keepdim=True)
    X_std = X_t.std(dim=0, keepdim=True).clamp(min=1e-6)
    X_norm = (X_t - X_mean) / X_std
    max_abs_pre = float(X_norm.abs().max().item())
    X_norm = X_norm.clamp(-clip_val, clip_val)
    max_abs_post = float(X_norm.abs().max().item())
    print(f"  Max |norm| before clip: {max_abs_pre:.4f}, after: {max_abs_post:.4f}")
    
    target_net = nn.Sequential(
        nn.Linear(input_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    ).to(device)
    for p in target_net.parameters():
        p.requires_grad = False
    
    predictor_net = nn.Sequential(
        nn.Linear(input_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    ).to(device)
    
    optimizer = torch.optim.Adam(predictor_net.parameters(), lr=lr)
    best_loss = float("inf")
    history = []
    
    for epoch in range(epochs):
        idx = torch.randperm(len(X_norm))
        eloss = 0.0
        nb = 0
        for i in range(0, len(X_norm), batch_size):
            batch = X_norm[idx[i:i+batch_size]]
            with torch.no_grad():
                t_out = target_net(batch)
            p_out = predictor_net(batch)
            loss = ((p_out - t_out) ** 2).mean()
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            eloss += loss.item()
            nb += 1
        avg = eloss / max(1, nb)
        history.append(avg)
        if avg < best_loss:
            best_loss = avg
        if (epoch+1) % 5 == 0 or epoch == 0:
            print(f"    epoch {epoch+1}/{epochs}: loss={avg:.6f}")
    
    save_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({
        "target_net": target_net.state_dict(),
        "predictor_net": predictor_net.state_dict(),
        "X_mean": X_mean.cpu(),
        "X_std": X_std.cpu(),
        "feature_mask": mask.tolist(),
        "kept_feature_names": mask_info["kept_names"],
        "dropped_feature_names": mask_info["dropped_names"],
        "all_feature_names": all_feature_names or [],
        "clip_val": clip_val,
        "input_dim": input_dim,
        "original_dim": len(mask),
        "hidden_dim": hidden_dim,
        "output_dim": output_dim,
        "training_samples": X.shape[0],
        "best_loss": best_loss,
        "mode_name": mode_name,
    }, str(save_path))
    print(f"  Saved: {save_path}")
    
    return {
        "best_loss": best_loss, "epochs": epochs, "samples": X.shape[0],
        "input_dim": input_dim, "dropped_count": len(mask_info["dropped_names"]),
        "max_abs_pre_clip": max_abs_pre, "max_abs_post_clip": max_abs_post,
        "history_last5": history[-5:],
    }


def score_split_fixed(model_path: Path, samples: list[dict], mode: str,
                       clip_val: float = 10.0) -> tuple[list[dict], float]:
    """Score samples with fixed RND model."""
    X_raw = build_feature_matrix(samples, mode)
    if X_raw is None:
        return [], 0.0
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(str(model_path), map_location=device, weights_only=False)
    
    mask = np.array(ckpt["feature_mask"])
    X = X_raw[:, mask]
    input_dim = ckpt["input_dim"]
    hidden_dim = ckpt["hidden_dim"]
    output_dim = ckpt["output_dim"]
    clip_val = ckpt.get("clip_val", clip_val)
    
    assert X.shape[1] == input_dim, f"Dim mismatch: {X.shape[1]} vs {input_dim}"
    
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
    X_t = torch.from_numpy(X).to(device)
    X_norm = (X_t - X_mean) / X_std
    max_abs = float(X_norm.abs().max().item())
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
    return results, max_abs


def load_jsonl(path: Path) -> list[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--enriched-dir", required=True, help="Path to enriched splits")
    args = parser.parse_args()
    
    ENRICHED_DIR = Path(args.enriched_dir)
    CAMPAIGN_DIR = ENRICHED_DIR.parent
    
    # Paths
    SAFE_MASS = Path("/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/sam_20260520_140528/counterfactual_samples.jsonl")
    FAILURE_MINED = Path("/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/sam_20260520_144408/replay_counterfactual_samples.jsonl")
    ACE_SAFE_DIR = CAMPAIGN_DIR / "fiper" / "ace_safe_mass_sam"
    ACE_FAIL_DIR = CAMPAIGN_DIR / "fiper" / "ace_failure_mined_sam"
    
    # Split files
    TRAIN = ENRICHED_DIR / "train_success_id_enriched.jsonl"
    CALIB = ENRICHED_DIR / "calib_success_id_enriched.jsonl"
    TEST_ID = ENRICHED_DIR / "test_success_id_enriched.jsonl"
    TEST_OOD_TASK = ENRICHED_DIR / "test_success_ood_task_enriched.jsonl"
    TEST_OOD_OBJ = ENRICHED_DIR / "test_success_ood_object_enriched.jsonl"
    TEST_OOD_SUITE = ENRICHED_DIR / "test_success_ood_suite_enriched.jsonl"
    
    print("=" * 70)
    print("OBSERVATION-ONLY RND CAMPAIGN")
    print("=" * 70)
    
    # Load training data once
    train_samples = load_jsonl(TRAIN)
    calib_samples = load_jsonl(CALIB)
    print(f"Train: {len(train_samples)}, Calib: {len(calib_samples)}")
    
    # Check which modes are available
    available_modes = []
    for mode_name, mode_info in FEATURE_MODES.items():
        X = build_feature_matrix(train_samples[:10], mode_name)
        if X is not None:
            available_modes.append(mode_name)
            print(f"  Mode '{mode_name}': AVAILABLE ({mode_info['description']})")
        else:
            print(f"  Mode '{mode_name}': UNAVAILABLE")
    
    # Check VLM mode
    X_vlm = build_feature_matrix(train_samples[:10], "action_free_with_vlm")
    if X_vlm is not None:
        available_modes.append("action_free_with_vlm")
        print(f"  Mode 'action_free_with_vlm': AVAILABLE (dim={X_vlm.shape[1]})")
    else:
        print(f"  Mode 'action_free_with_vlm': UNAVAILABLE (no pooled_vlm_features in data)")
    
    all_results = {}
    
    for mode_name in available_modes:
        print(f"\n{'='*70}")
        print(f"PROCESSING MODE: {mode_name}")
        print(f"{'='*70}")
        
        mode_dir = ENRICHED_DIR / f"rnd_{mode_name}"
        mode_dir.mkdir(parents=True, exist_ok=True)
        
        # Build feature matrix
        X_train = build_feature_matrix(train_samples, mode_name)
        if X_train is None:
            print(f"  SKIP: cannot build features for {mode_name}")
            continue
        
        feature_names = FEATURE_MODES.get(mode_name, {}).get("names", [f"f{i}" for i in range(X_train.shape[1])])
        if len(feature_names) != X_train.shape[1]:
            feature_names = [f"f{i}" for i in range(X_train.shape[1])]
        
        print(f"\n--- Feature Mask ---")
        mask_info = compute_feature_mask(X_train, feature_names)
        
        mask_report = {
            "mode": mode_name,
            "total": len(feature_names),
            "kept": len(mask_info["kept_names"]),
            "dropped": len(mask_info["dropped_names"]),
            "kept_names": mask_info["kept_names"],
            "dropped_names": mask_info["dropped_names"],
        }
        (mode_dir / "feature_mask_report.json").write_text(json.dumps(mask_report, indent=2) + "\n")
        
        # Train
        print(f"\n--- Training ---")
        model_path = mode_dir / f"rnd_oe_{mode_name}.pt"
        train_result = train_rnd_fixed(
            X_train, mask_info, hidden_dim=256, output_dim=128,
            epochs=30, batch_size=512, lr=1e-3,
            save_path=model_path, clip_val=10.0,
            mode_name=mode_name, all_feature_names=feature_names,
        )
        (mode_dir / "rnd_training_summary.json").write_text(json.dumps(train_result, indent=2, default=str) + "\n")
        
        # Calibrate on calib split
        print(f"\n--- Calibrating ---")
        calib_scored, calib_max_abs = score_split_fixed(model_path, calib_samples, mode_name)
        calib_vals = np.array([s["rnd_score"] for s in calib_scored])
        
        thresholds = {
            "q90": float(np.quantile(calib_vals, 0.90)),
            "q95": float(np.quantile(calib_vals, 0.95)),
            "q99": float(np.quantile(calib_vals, 0.99)),
            "mean": float(calib_vals.mean()),
            "std": float(calib_vals.std()),
        }
        (mode_dir / "rnd_conformal_thresholds.json").write_text(json.dumps(thresholds, indent=2) + "\n")
        print(f"  q90={thresholds['q90']:.8f}, q95={thresholds['q95']:.8f}, q99={thresholds['q99']:.8f}")
        
        q90, q95, q99 = thresholds["q90"], thresholds["q95"], thresholds["q99"]
        
        # Evaluate false alarm rates
        print(f"\n--- False Alarm Evaluation ---")
        fa_rates = {}
        eval_splits = [
            ("train_success_id", TRAIN),
            ("test_success_id", TEST_ID),
            ("test_success_ood_task", TEST_OOD_TASK),
            ("test_success_ood_object", TEST_OOD_OBJ),
            ("test_success_ood_suite", TEST_OOD_SUITE),
        ]
        
        for label, split_path in eval_splits:
            if not split_path.exists():
                print(f"  SKIP: {split_path.name} not found")
                continue
            samples = load_jsonl(split_path)
            scored, max_abs = score_split_fixed(model_path, samples, mode_name)
            
            if not scored:
                continue
            
            rnd_vals = np.array([s["rnd_score"] for s in scored])
            fa_90 = float((rnd_vals > q90).mean())
            fa_95 = float((rnd_vals > q95).mean())
            fa_99 = float((rnd_vals > q99).mean())
            
            fa_rates[label] = {
                "count": len(scored),
                "mean_rnd": float(rnd_vals.mean()),
                "std_rnd": float(rnd_vals.std()),
                "fa_90": fa_90, "fa_95": fa_95, "fa_99": fa_99,
                "max_abs_norm": max_abs,
                "all_finite": bool(np.all(np.isfinite(rnd_vals))),
            }
            print(f"  {label}: n={len(scored)}, FA@q90={fa_90:.4f}, FA@q95={fa_95:.4f}, FA@q99={fa_99:.4f}")
            
            # Save scores
            scores_path = mode_dir / f"rnd_scores_{label}.jsonl"
            with scores_path.open("w") as f:
                for s in scored:
                    f.write(json.dumps(s) + "\n")
        
        # Score rollout datasets
        print(f"\n--- Rollout Sanity Check ---")
        rollout_stats = {}
        for label, rpath in [("safe_mass", SAFE_MASS), ("failure_mined", FAILURE_MINED)]:
            if not rpath.exists():
                print(f"  SKIP: {rpath} not found")
                continue
            r_samples = load_jsonl(rpath)
            scored, max_abs = score_split_fixed(model_path, r_samples, mode_name)
            if not scored:
                print(f"  {label}: scoring failed (mode incompatible)")
                continue
            rnd_vals = np.array([s["rnd_score"] for s in scored])
            rollout_stats[label] = {
                "count": len(scored),
                "mean": float(rnd_vals.mean()),
                "std": float(rnd_vals.std()),
                "min": float(rnd_vals.min()),
                "max": float(rnd_vals.max()),
                "max_abs_norm": max_abs,
                "all_finite": bool(np.all(np.isfinite(rnd_vals))),
            }
            print(f"  {label}: n={len(scored)}, mean={rnd_vals.mean():.6f}, "
                  f"max={rnd_vals.max():.6f}, finite={np.all(np.isfinite(rnd_vals))}")
            
            scores_path = mode_dir / f"rnd_scores_{label}.jsonl"
            with scores_path.open("w") as f:
                for s in scored:
                    f.write(json.dumps(s) + "\n")
        
        # FIPER quadrants (reuse ACE)
        print(f"\n--- FIPER Quadrants ---")
        
        def load_ace(path):
            r = {}
            if not path.exists():
                return r
            with path.open() as f:
                for line in f:
                    if not line.strip(): continue
                    g = json.loads(line)
                    r[g["state_id"]] = g
            return r
        
        ace_safe = load_ace(ACE_SAFE_DIR / "ace_group_summaries.jsonl")
        ace_fail = load_ace(ACE_FAIL_DIR / "ace_group_summaries.jsonl")
        
        if ace_safe:
            safe_ace_vals = np.array([g["ace_score"] for g in ace_safe.values()])
            q95_ace = float(np.quantile(safe_ace_vals, 0.95))
        else:
            q95_ace = 0.0
        
        def map_rnd_to_state(scored_path):
            if not scored_path.exists():
                return {}
            scored = load_jsonl(scored_path)
            by_state = defaultdict(list)
            for s in scored:
                sid = s["sample_id"]
                if "_seed" in sid:
                    sid = sid.split("_seed")[0]
                by_state[sid].append(s["rnd_score"])
            return {sid: float(np.mean(v)) for sid, v in by_state.items()}
        
        rnd_safe = map_rnd_to_state(mode_dir / "rnd_scores_safe_mass.jsonl")
        rnd_fail = map_rnd_to_state(mode_dir / "rnd_scores_failure_mined.jsonl")
        
        def classify(ace_dict, rnd_dict, thresh_rnd, thresh_ace):
            quads = {"OOD_confident": [], "action_uncertain": [], "FIPER_alarm": [], "normal_confident": []}
            all_st = []
            for sid, g in ace_dict.items():
                ace = g["ace_score"]
                rnd = rnd_dict.get(sid, 0.0)
                rh = rnd > thresh_rnd
                ah = ace > thresh_ace
                if rh and not ah: q = "OOD_confident"
                elif not rh and ah: q = "action_uncertain"
                elif rh and ah: q = "FIPER_alarm"
                else: q = "normal_confident"
                sd = {"state_id": sid, "ace_score": ace, "rnd_score": rnd, "quadrant": q,
                      "group_type": g.get("group_type", ""), "action_std_mean": g.get("action_std_mean", 0)}
                quads[q].append(sd)
                all_st.append(sd)
            return quads, all_st
        
        sq, sa = classify(ace_safe, rnd_safe, q95, q95_ace)
        fq, fa_st = classify(ace_fail, rnd_fail, q95, q95_ace)
        
        print(f"  Safe Mass: " + ", ".join(f"{k}={len(v)}" for k, v in sq.items()))
        print(f"  Fail Mined: " + ", ".join(f"{k}={len(v)}" for k, v in fq.items()))
        
        # Mining queue
        all_combined = sa + fa_st
        seen = set()
        unique_states = []
        for s in all_combined:
            if s["state_id"] not in seen:
                seen.add(s["state_id"])
                rnd_f = s["rnd_score"] / max(q95, 1e-10)
                ace_f = (s["ace_score"] - (-200)) / 100.0
                pri = rnd_f + ace_f
                if s["quadrant"] == "FIPER_alarm": pri += 5.0
                elif s["quadrant"] == "action_uncertain": pri += 2.0
                s["priority_score"] = float(pri)
                unique_states.append(s)
        unique_states.sort(key=lambda x: x["priority_score"], reverse=True)
        
        mining_path = mode_dir / f"fiper_candidate_states_{mode_name}.jsonl"
        with mining_path.open("w") as f:
            for s in unique_states:
                f.write(json.dumps(s) + "\n")
        print(f"  Mining queue: {len(unique_states)} states -> {mining_path.name}")
        
        # Save mode results
        mode_result = {
            "mode": mode_name,
            "feature_mask": mask_report,
            "training": train_result,
            "thresholds": thresholds,
            "false_alarm_rates": fa_rates,
            "rollout_stats": rollout_stats,
            "ace_threshold_q95": q95_ace,
            "safe_mass_quadrants": {k: len(v) for k, v in sq.items()},
            "failure_mined_quadrants": {k: len(v) for k, v in fq.items()},
            "mining_queue_count": len(unique_states),
        }
        (mode_dir / f"exec_summary_{mode_name}.json").write_text(
            json.dumps(mode_result, indent=2, default=str) + "\n"
        )
        all_results[mode_name] = mode_result
    
    # Save combined results
    (ENRICHED_DIR / "all_modes_summary.json").write_text(
        json.dumps(all_results, indent=2, default=str) + "\n"
    )
    
    print(f"\n{'='*70}")
    print("OBSERVATION-ONLY RND CAMPAIGN COMPLETE")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
