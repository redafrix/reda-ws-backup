#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import numpy as np
from pathlib import Path
from collections import defaultdict

def run_cmd(cmd, env=None):
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
        raise RuntimeError(f"Command failed: {res.stderr}")
    return res.stdout

def main():
    parser = argparse.ArgumentParser(description="Evaluate success-only FIPER safety monitor")
    parser.add_argument("--campaign-dir", required=True, help="Campaign root directory")
    args = parser.parse_args()

    campaign_dir = Path(args.campaign_dir)
    datasets_dir = campaign_dir / "datasets"
    fiper_dir = campaign_dir / "fiper"
    
    rnd_model_dir = fiper_dir / "rnd_success_only"
    rnd_model_path = rnd_model_dir / "rnd_oe_success_only.pt"
    thresholds_path = rnd_model_dir / "rnd_conformal_thresholds.json"
    
    # Load calibrated conformal thresholds
    with thresholds_path.open() as f:
        rnd_thresholds = json.load(f)
    q90 = rnd_thresholds["q90"]
    q95 = rnd_thresholds["q95"]
    q99 = rnd_thresholds["q99"]

    print(f"Loaded conformal RND thresholds (calibrated strictly on calib_success_id):")
    print(f"  q90 = {q90:.6f}")
    print(f"  q95 = {q95:.6f}")
    print(f"  q99 = {q99:.6f}\n")

    # Setup environment for running fiper bridge scripts
    env = os.environ.copy()
    env["PYTHONPATH"] = f"/home/rootalkhatib/test/reda_ws/fiper_ws:/home/rootalkhatib/test/reda_ws/asynchvla_ws/src:{env.get('PYTHONPATH', '')}"

    from stage9_fiper_bridge.train_rnd_oe import score_samples

    # Step 1: Evaluate false alarm rates on success splits
    splits = ["train_success_id", "test_success_id", "test_success_ood_task", "test_success_ood_suite"]
    fa_rates = {}

    print("=== Evaluating False Alarm Rates on Success Splits ===")
    for split in splits:
        split_path = datasets_dir / f"{split}.jsonl"
        if not split_path.exists():
            print(f"Warning: {split_path} not found. Skipping.")
            continue
        
        with split_path.open() as f:
            samples = [json.loads(line) for line in f if line.strip()]
            
        print(f"Scoring {len(samples)} samples from {split}...")
        scored = score_samples(rnd_model_path, samples)
        
        # Save scored output for audit
        out_score_path = rnd_model_dir / f"rnd_scores_{split}.jsonl"
        with out_score_path.open("w") as out_f:
            for s in scored:
                out_f.write(json.dumps(s) + "\n")
                
        scores = np.array([s["rnd_score"] for s in scored])
        
        fa_90 = np.mean(scores > q90)
        fa_95 = np.mean(scores > q95)
        fa_99 = np.mean(scores > q99)
        
        fa_rates[split] = {
            "count": len(samples),
            "mean_rnd": float(scores.mean()),
            "std_rnd": float(scores.std()),
            "fa_90": float(fa_90),
            "fa_95": float(fa_95),
            "fa_99": float(fa_99)
        }
        
        print(f"  {split} ({len(samples)} samples):")
        print(f"    Mean RND: {scores.mean():.6f}")
        print(f"    False Alarm @ q90 (th={q90:.6f}): {fa_90 * 100:.2f}%")
        print(f"    False Alarm @ q95 (th={q95:.6f}): {fa_95 * 100:.2f}%")
        print(f"    False Alarm @ q99 (th={q99:.6f}): {fa_99 * 100:.2f}%\n")

    # Step 2: Run ACE analysis on 64-seed Sam datasets
    safe_mass_jsonl = "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/sam_20260520_140528/counterfactual_samples.jsonl"
    failure_mined_jsonl = "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/sam_20260520_144408/replay_counterfactual_samples.jsonl"

    print("=== Running ACE analysis on Sam datasets ===")
    
    ace_safe_dir = fiper_dir / "ace_safe_mass_sam"
    cmd_safe = [
        "python3", "-u", "-m", "stage9_fiper_bridge.analyze_existing_ace",
        "--jsonl", safe_mass_jsonl,
        "--out-dir", str(ace_safe_dir)
    ]
    run_cmd(cmd_safe, env=env)
    
    ace_failure_dir = fiper_dir / "ace_failure_mined_sam"
    cmd_failure = [
        "python3", "-u", "-m", "stage9_fiper_bridge.analyze_existing_ace",
        "--jsonl", failure_mined_jsonl,
        "--out-dir", str(ace_failure_dir)
    ]
    run_cmd(cmd_failure, env=env)

    # Step 3: Run RND scoring on the counterfactual datasets
    print("\n=== Scoring 64-seed counterfactual datasets with RND ===")
    
    # Load and score safe mass
    print(f"Loading safe mass samples from {safe_mass_jsonl}...")
    with open(safe_mass_jsonl) as f:
        safe_samples = [json.loads(line) for line in f if line.strip()]
    print(f"Scoring {len(safe_samples)} safe mass samples...")
    scored_safe = score_samples(rnd_model_path, safe_samples)
    
    rnd_scores_safe_path = rnd_model_dir / "rnd_scores_safe_mass.jsonl"
    with rnd_scores_safe_path.open("w") as f:
        for s in scored_safe:
            f.write(json.dumps(s) + "\n")
            
    # Load and score failure mined
    print(f"Loading failure mined samples from {failure_mined_jsonl}...")
    with open(failure_mined_jsonl) as f:
        fail_samples = [json.loads(line) for line in f if line.strip()]
    print(f"Scoring {len(fail_samples)} failure mined samples...")
    scored_fail = score_samples(rnd_model_path, fail_samples)
    
    rnd_scores_fail_path = rnd_model_dir / "rnd_scores_failure_mined.jsonl"
    with rnd_scores_fail_path.open("w") as f:
        for s in scored_fail:
            f.write(json.dumps(s) + "\n")

    # Step 4: Map RND scores to state_id
    # We group by state_id (removing _seedX suffix)
    def map_rnd_to_state(scored_list):
        rnd_by_state = defaultdict(list)
        for s in scored_list:
            sid = s["sample_id"]
            if "_seed" in sid:
                sid = sid.split("_seed")[0]
            rnd_by_state[sid].append(s["rnd_score"])
        return {sid: float(np.mean(vals)) for sid, vals in rnd_by_state.items()}

    rnd_safe_by_state = map_rnd_to_state(scored_safe)
    rnd_fail_by_state = map_rnd_to_state(scored_fail)

    # Step 5: Read ACE scores
    def load_ace_summaries(summary_jsonl):
        ace_by_state = {}
        with summary_jsonl.open() as f:
            for line in f:
                if not line.strip():
                    continue
                g = json.loads(line)
                ace_by_state[g["state_id"]] = g
        return ace_by_state

    ace_safe = load_ace_summaries(ace_safe_dir / "ace_group_summaries.jsonl")
    ace_fail = load_ace_summaries(ace_failure_dir / "ace_group_summaries.jsonl")

    # Step 6: Unsupervised Calibrate ACE threshold
    # We will use the 95th percentile of the safe mass ACE scores as the "high ACE" threshold
    safe_ace_vals = np.array([g["ace_score"] for g in ace_safe.values()])
    q95_ace = float(np.quantile(safe_ace_vals, 0.95))
    print(f"\nCalibrated ACE threshold (q95 of safe mass): {q95_ace:.4f}")

    # Combine RND + ACE into FIPER-style quadrant classification
    def classify_quadrants(ace_dict, rnd_dict, threshold_rnd, threshold_ace):
        quadrants = {
            "OOD_confident": [],       # RND high, ACE low
            "action_uncertain": [],    # RND low, ACE high
            "FIPER_alarm": [],         # RND high, ACE high
            "normal_confident": []     # RND low, ACE low
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
                "rnd_score": rnd,
                "quadrant": quad,
                "group_type": g.get("group_type", "unknown"),
                "risk_score_range": g.get("risk_score_range", 0.0),
                "num_candidates": g.get("num_candidates", 0),
                "action_std_mean": g.get("action_std_mean", 0.0)
            }
            quadrants[quad].append(state_data)
            all_states.append(state_data)
            
        return quadrants, all_states

    # We use q95 for both RND and ACE
    safe_quads, safe_all_states = classify_quadrants(ace_safe, rnd_safe_by_state, q95, q95_ace)
    fail_quads, fail_all_states = classify_quadrants(ace_fail, rnd_fail_by_state, q95, q95_ace)

    print("\n=== Safe Mass Quadrant Distribution ===")
    for q, states in safe_quads.items():
        print(f"  {q}: {len(states)} states ({len(states)/len(safe_all_states)*100:.2f}%)")

    print("\n=== Failure Mined Quadrant Distribution ===")
    for q, states in fail_quads.items():
        print(f"  {q}: {len(states)} states ({len(states)/len(fail_all_states)*100:.2f}%)")

    # Step 7: Create a future mining queue
    # The mining priority score will rank states. High priority is given to:
    # 1. FIPER_alarm (both OOD and policy uncertain)
    # 2. action_uncertain (in-distribution but policy struggles/bifurcates)
    # 3. OOD_confident (policy is confident, but observations are strange/unseen)
    # We rank states based on a combined score:
    # priority_score = (rnd_score / q95) + (ace_score / abs(q95_ace) if q95_ace != 0 else ace_score)
    # Plus a bonus for FIPER_alarm quadrant.
    
    all_combined_states = safe_all_states + fail_all_states
    
    # Remove duplicates if any (states that might appear in both, though they should be distinct due to counterfactual setups)
    seen_sids = set()
    unique_combined_states = []
    for s in all_combined_states:
        if s["state_id"] not in seen_sids:
            seen_sids.add(s["state_id"])
            
            # Compute priority score
            rnd_factor = s["rnd_score"] / q95
            
            # ACE score is negative differential entropy. Larger (closer to 0) means more uncertain.
            # Standardize ACE by shift/scaling
            ace_factor = (s["ace_score"] - (-200)) / 100.0  # approximate scale
            
            priority = rnd_factor + ace_factor
            if s["quadrant"] == "FIPER_alarm":
                priority += 5.0  # Large bonus for joint alarms
            elif s["quadrant"] == "action_uncertain":
                priority += 2.0  # Medium bonus for policy uncertainty
                
            s["priority_score"] = float(priority)
            unique_combined_states.append(s)

    unique_combined_states.sort(key=lambda x: x["priority_score"], reverse=True)

    mining_queue_path = fiper_dir / "fiper_candidate_states.jsonl"
    with mining_queue_path.open("w") as f:
        for s in unique_combined_states:
            f.write(json.dumps(s) + "\n")
    print(f"\nWrote {len(unique_combined_states)} unique candidate states to {mining_queue_path}")

    # Step 8: Save execution results to JSON summary
    exec_summary = {
        "conformal_rnd_thresholds": {
            "q90": q90,
            "q95": q95,
            "q99": q99
        },
        "ace_threshold_q95": q95_ace,
        "false_alarm_rates": fa_rates,
        "safe_mass_quadrants": {q: len(states) for q, states in safe_quads.items()},
        "failure_mined_quadrants": {q: len(states) for q, states in fail_quads.items()},
        "total_mining_queue": len(unique_combined_states)
    }
    
    summary_path = fiper_dir / "fiper_exec_summary.json"
    with summary_path.open("w") as f:
        json.dump(exec_summary, f, indent=2)
    print(f"Saved evaluation execution summary to {summary_path}")

if __name__ == "__main__":
    main()
