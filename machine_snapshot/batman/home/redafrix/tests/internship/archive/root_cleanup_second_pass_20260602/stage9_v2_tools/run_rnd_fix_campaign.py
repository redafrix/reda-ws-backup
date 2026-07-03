#!/usr/bin/env python3
"""
run_rnd_fix_campaign.py – Full campaign script for the RND feature fix.

Steps:
1. Train fixed RND-OE on train_success_id.jsonl
2. Calibrate conformal thresholds on calib_success_id.jsonl
3. Evaluate false alarm rates on all success splits
4. Score rollout datasets (safe_mass, failure_mined) as sanity check
5. Reuse existing ACE analysis
6. Classify FIPER quadrants using fixed RND scores
7. Generate fiper_candidate_states_fixed.jsonl
8. Save execution summary JSON

Usage:
    python3 run_rnd_fix_campaign.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

# ---- CONFIG ----
CAMPAIGN_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/success_only_fiper_20260521_102354")
FIPER_WS = Path("/home/rootalkhatib/test/reda_ws/fiper_ws")
DATA_ROOT = Path("/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data")

DATASETS_DIR = CAMPAIGN_DIR / "datasets"
FIXED_OUT_DIR = CAMPAIGN_DIR / "fiper" / "rnd_success_only_fixed"

# Rollout datasets (read-only, not used for training)
SAFE_MASS_JSONL = DATA_ROOT / "v2_mass" / "sam_20260520_140528" / "counterfactual_samples.jsonl"
FAILURE_MINED_JSONL = DATA_ROOT / "v2_mass_failure" / "sam_20260520_144408" / "replay_counterfactual_samples.jsonl"

# Existing ACE results (reuse)
ACE_SAFE_DIR = CAMPAIGN_DIR / "fiper" / "ace_safe_mass_sam"
ACE_FAIL_DIR = CAMPAIGN_DIR / "fiper" / "ace_failure_mined_sam"

TRAIN_SPLIT = DATASETS_DIR / "train_success_id.jsonl"
CALIB_SPLIT = DATASETS_DIR / "calib_success_id.jsonl"
TEST_ID_SPLIT = DATASETS_DIR / "test_success_id.jsonl"
TEST_OOD_TASK_SPLIT = DATASETS_DIR / "test_success_ood_task.jsonl"
TEST_OOD_SUITE_SPLIT = DATASETS_DIR / "test_success_ood_suite.jsonl"


# Import the fixed training/scoring module
sys.path.insert(0, str(Path(__file__).parent))
from train_rnd_oe_fixed import (
    load_success_only_samples,
    build_feature_matrix,
    compute_feature_mask,
    train_rnd_torch_fixed,
    score_samples_fixed,
    FEATURE_NAMES,
)


def load_jsonl(path: Path) -> list[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def score_split(model_path: Path, split_path: Path, out_path: Path, label: str) -> dict:
    """Score a split and return stats."""
    samples = load_jsonl(split_path)
    scored, max_abs_raw = score_samples_fixed(model_path, samples)
    
    with out_path.open("w") as f:
        for s in scored:
            f.write(json.dumps(s) + "\n")
    
    rnd_vals = np.array([s["rnd_score"] for s in scored])
    stats = {
        "label": label,
        "count": len(scored),
        "mean": float(rnd_vals.mean()),
        "std": float(rnd_vals.std()),
        "min": float(rnd_vals.min()),
        "max": float(rnd_vals.max()),
        "p50": float(np.percentile(rnd_vals, 50)),
        "p90": float(np.percentile(rnd_vals, 90)),
        "p95": float(np.percentile(rnd_vals, 95)),
        "p99": float(np.percentile(rnd_vals, 99)),
        "max_abs_normalized": max_abs_raw,
        "all_finite": bool(np.all(np.isfinite(rnd_vals))),
    }
    print(f"  {label}: n={stats['count']}, mean={stats['mean']:.6f}, "
          f"std={stats['std']:.6f}, max={stats['max']:.6f}, "
          f"max_abs_norm={max_abs_raw:.2f}, finite={stats['all_finite']}")
    return stats


def main():
    print("=" * 70)
    print("RND FEATURE FIX CAMPAIGN")
    print("=" * 70)
    
    FIXED_OUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # ============================================================
    # STEP 1: TRAIN FIXED RND-OE
    # ============================================================
    print("\n=== STEP 1: Training fixed RND-OE ===")
    
    samples = load_success_only_samples([str(TRAIN_SPLIT)], max_risk=0.20, min_conf=0.80)
    print(f"Loaded {len(samples)} training samples")
    
    X = build_feature_matrix(samples)
    print(f"Raw feature matrix: {X.shape}")
    
    mask_info = compute_feature_mask(X, min_std=1e-4)
    
    # Save mask report
    mask_report = {
        "total_features": len(FEATURE_NAMES),
        "kept_count": len(mask_info["kept_names"]),
        "dropped_count": len(mask_info["dropped_names"]),
        "kept_names": mask_info["kept_names"],
        "dropped_names": mask_info["dropped_names"],
        "dropped_indices": mask_info["dropped_indices"],
        "min_std_threshold": 1e-4,
    }
    (FIXED_OUT_DIR / "feature_mask_report.json").write_text(
        json.dumps(mask_report, indent=2) + "\n"
    )
    
    model_path = FIXED_OUT_DIR / "rnd_oe_fixed.pt"
    training_result = train_rnd_torch_fixed(
        X, mask_info, hidden_dim=256, output_dim=128,
        epochs=30, batch_size=512, lr=1e-3,
        save_path=model_path, clip_val=10.0,
    )
    training_result["feature_mask_report"] = mask_report
    (FIXED_OUT_DIR / "rnd_training_summary.json").write_text(
        json.dumps(training_result, indent=2, default=str) + "\n"
    )
    
    # ============================================================
    # STEP 2: CALIBRATE ON CALIB SPLIT
    # ============================================================
    print("\n=== STEP 2: Calibrating conformal thresholds on calib_success_id ===")
    
    calib_stats = score_split(
        model_path, CALIB_SPLIT,
        FIXED_OUT_DIR / "rnd_scores_calib.jsonl",
        "calib_success_id"
    )
    
    calib_scored = load_jsonl(FIXED_OUT_DIR / "rnd_scores_calib.jsonl")
    calib_vals = np.array([s["rnd_score"] for s in calib_scored])
    
    thresholds = {
        "q90": float(np.quantile(calib_vals, 0.90)),
        "q95": float(np.quantile(calib_vals, 0.95)),
        "q99": float(np.quantile(calib_vals, 0.99)),
        "mean": float(calib_vals.mean()),
        "std": float(calib_vals.std()),
        "min": float(calib_vals.min()),
        "max": float(calib_vals.max()),
    }
    (FIXED_OUT_DIR / "rnd_conformal_thresholds.json").write_text(
        json.dumps(thresholds, indent=2) + "\n"
    )
    print(f"  Conformal thresholds (from calib only):")
    for k, v in thresholds.items():
        print(f"    {k}: {v:.8f}")
    
    q90 = thresholds["q90"]
    q95 = thresholds["q95"]
    q99 = thresholds["q99"]
    
    # ============================================================
    # STEP 3: EVALUATE FALSE ALARM RATES ON SUCCESS SPLITS
    # ============================================================
    print("\n=== STEP 3: Evaluating false alarm rates ===")
    
    fa_rates = {}
    splits = [
        ("train_success_id", TRAIN_SPLIT),
        ("test_success_id", TEST_ID_SPLIT),
        ("test_success_ood_task", TEST_OOD_TASK_SPLIT),
        ("test_success_ood_suite", TEST_OOD_SUITE_SPLIT),
    ]
    
    for label, split_path in splits:
        stats = score_split(
            model_path, split_path,
            FIXED_OUT_DIR / f"rnd_scores_{label}.jsonl",
            label
        )
        
        # Compute false alarm rates
        scored = load_jsonl(FIXED_OUT_DIR / f"rnd_scores_{label}.jsonl")
        rnd_vals = np.array([s["rnd_score"] for s in scored])
        
        fa_90 = float((rnd_vals > q90).mean())
        fa_95 = float((rnd_vals > q95).mean())
        fa_99 = float((rnd_vals > q99).mean())
        
        fa_rates[label] = {
            "count": len(scored),
            "mean_rnd": float(rnd_vals.mean()),
            "std_rnd": float(rnd_vals.std()),
            "fa_90": fa_90,
            "fa_95": fa_95,
            "fa_99": fa_99,
            "max_abs_normalized": stats["max_abs_normalized"],
            "all_finite": stats["all_finite"],
        }
        print(f"  {label}: FA@q90={fa_90:.4f} FA@q95={fa_95:.4f} FA@q99={fa_99:.4f}")
    
    # ============================================================
    # STEP 4: SCORE ROLLOUT DATASETS (SANITY CHECK)
    # ============================================================
    print("\n=== STEP 4: Scoring rollout datasets (sanity check) ===")
    
    rollout_stats = {}
    for label, path in [("safe_mass", SAFE_MASS_JSONL), ("failure_mined", FAILURE_MINED_JSONL)]:
        if not path.exists():
            print(f"  WARN: {path} not found, skipping")
            continue
        stats = score_split(
            model_path, path,
            FIXED_OUT_DIR / f"rnd_scores_{label}.jsonl",
            label
        )
        rollout_stats[label] = stats
    
    # ============================================================
    # STEP 5: REUSE ACE ANALYSIS
    # ============================================================
    print("\n=== STEP 5: Reusing existing ACE analysis ===")
    
    def load_ace_summaries(summary_jsonl: Path) -> dict:
        ace_by_state = {}
        if not summary_jsonl.exists():
            print(f"  WARN: {summary_jsonl} not found")
            return ace_by_state
        with summary_jsonl.open() as f:
            for line in f:
                if not line.strip():
                    continue
                g = json.loads(line)
                ace_by_state[g["state_id"]] = g
        return ace_by_state
    
    ace_safe = load_ace_summaries(ACE_SAFE_DIR / "ace_group_summaries.jsonl")
    ace_fail = load_ace_summaries(ACE_FAIL_DIR / "ace_group_summaries.jsonl")
    
    print(f"  ACE safe states: {len(ace_safe)}")
    print(f"  ACE failure states: {len(ace_fail)}")
    
    # Calibrate ACE threshold (reuse q95 of safe mass)
    if ace_safe:
        safe_ace_vals = np.array([g["ace_score"] for g in ace_safe.values()])
        q95_ace = float(np.quantile(safe_ace_vals, 0.95))
    else:
        q95_ace = 0.0
    print(f"  ACE threshold (q95 of safe mass): {q95_ace:.4f}")
    
    # ============================================================
    # STEP 6: FIPER QUADRANT CLASSIFICATION
    # ============================================================
    print("\n=== STEP 6: FIPER quadrant classification ===")
    
    def map_rnd_to_state(scored_path: Path) -> dict:
        scored = load_jsonl(scored_path)
        rnd_by_state = defaultdict(list)
        for s in scored:
            sid = s["sample_id"]
            if "_seed" in sid:
                sid = sid.split("_seed")[0]
            rnd_by_state[sid].append(s["rnd_score"])
        return {sid: float(np.mean(vals)) for sid, vals in rnd_by_state.items()}
    
    def classify_quadrants(ace_dict, rnd_dict, threshold_rnd, threshold_ace):
        quadrants = {
            "OOD_confident": [], "action_uncertain": [],
            "FIPER_alarm": [], "normal_confident": [],
        }
        all_states = []
        for sid, g in ace_dict.items():
            ace = g["ace_score"]
            rnd = rnd_dict.get(sid, 0.0)
            rnd_high = rnd > threshold_rnd
            ace_high = ace > threshold_ace
            
            if rnd_high and not ace_high:
                quad = "OOD_confident"
            elif not rnd_high and ace_high:
                quad = "action_uncertain"
            elif rnd_high and ace_high:
                quad = "FIPER_alarm"
            else:
                quad = "normal_confident"
            
            state_data = {
                "state_id": sid,
                "ace_score": ace,
                "rnd_score_fixed": rnd,
                "quadrant": quad,
                "group_type": g.get("group_type", "unknown"),
                "risk_score_range": g.get("risk_score_range", 0.0),
                "num_candidates": g.get("num_candidates", 0),
                "action_std_mean": g.get("action_std_mean", 0.0),
            }
            quadrants[quad].append(state_data)
            all_states.append(state_data)
        return quadrants, all_states
    
    # Build state-level RND maps from scored rollouts
    rnd_safe_by_state = {}
    rnd_fail_by_state = {}
    
    safe_scores_path = FIXED_OUT_DIR / "rnd_scores_safe_mass.jsonl"
    fail_scores_path = FIXED_OUT_DIR / "rnd_scores_failure_mined.jsonl"
    
    if safe_scores_path.exists():
        rnd_safe_by_state = map_rnd_to_state(safe_scores_path)
    if fail_scores_path.exists():
        rnd_fail_by_state = map_rnd_to_state(fail_scores_path)
    
    safe_quads, safe_all_states = classify_quadrants(ace_safe, rnd_safe_by_state, q95, q95_ace)
    fail_quads, fail_all_states = classify_quadrants(ace_fail, rnd_fail_by_state, q95, q95_ace)
    
    print("\n  Safe Mass Quadrant Distribution:")
    for q, states in safe_quads.items():
        n = len(states)
        pct = n / max(1, len(safe_all_states)) * 100
        print(f"    {q}: {n} states ({pct:.1f}%)")
    
    print("\n  Failure Mined Quadrant Distribution:")
    for q, states in fail_quads.items():
        n = len(states)
        pct = n / max(1, len(fail_all_states)) * 100
        print(f"    {q}: {n} states ({pct:.1f}%)")
    
    # ============================================================
    # STEP 7: GENERATE MINING QUEUE
    # ============================================================
    print("\n=== STEP 7: Generating mining queue ===")
    
    all_combined = safe_all_states + fail_all_states
    seen = set()
    unique_states = []
    for s in all_combined:
        if s["state_id"] not in seen:
            seen.add(s["state_id"])
            rnd_factor = s["rnd_score_fixed"] / max(q95, 1e-10)
            ace_factor = (s["ace_score"] - (-200)) / 100.0
            priority = rnd_factor + ace_factor
            if s["quadrant"] == "FIPER_alarm":
                priority += 5.0
            elif s["quadrant"] == "action_uncertain":
                priority += 2.0
            s["priority_score"] = float(priority)
            unique_states.append(s)
    
    unique_states.sort(key=lambda x: x["priority_score"], reverse=True)
    
    mining_path = CAMPAIGN_DIR / "fiper" / "fiper_candidate_states_fixed.jsonl"
    with mining_path.open("w") as f:
        for s in unique_states:
            f.write(json.dumps(s) + "\n")
    print(f"  Wrote {len(unique_states)} candidate states to {mining_path}")
    
    # Print top 5
    print("\n  Top 5 mining candidates:")
    for i, s in enumerate(unique_states[:5]):
        print(f"    {i+1}. {s['state_id']} | quadrant={s['quadrant']} | "
              f"rnd={s['rnd_score_fixed']:.6f} | ace={s['ace_score']:.2f} | "
              f"priority={s['priority_score']:.4f}")
    
    # ============================================================
    # STEP 8: SAVE EXECUTION SUMMARY
    # ============================================================
    print("\n=== STEP 8: Saving execution summary ===")
    
    # Compare with old (broken) thresholds
    old_thresh_path = CAMPAIGN_DIR / "fiper" / "rnd_success_only" / "rnd_conformal_thresholds.json"
    old_thresholds = {}
    if old_thresh_path.exists():
        old_thresholds = json.loads(old_thresh_path.read_text())
    
    exec_summary = {
        "fix_description": "Dropped constant/near-constant features (std < 1e-4) and clipped normalized values to [-10, 10]",
        "feature_mask": mask_report,
        "training_result": training_result,
        "conformal_thresholds_fixed": thresholds,
        "conformal_thresholds_old": old_thresholds,
        "false_alarm_rates": fa_rates,
        "rollout_sanity_check": rollout_stats,
        "ace_threshold_q95": q95_ace,
        "safe_mass_quadrants": {q: len(s) for q, s in safe_quads.items()},
        "failure_mined_quadrants": {q: len(s) for q, s in fail_quads.items()},
        "total_mining_queue": len(unique_states),
    }
    
    summary_path = FIXED_OUT_DIR / "fiper_exec_summary_fixed.json"
    with summary_path.open("w") as f:
        json.dump(exec_summary, f, indent=2, default=str)
    print(f"  Saved execution summary to {summary_path}")
    
    print("\n" + "=" * 70)
    print("RND FEATURE FIX CAMPAIGN COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
