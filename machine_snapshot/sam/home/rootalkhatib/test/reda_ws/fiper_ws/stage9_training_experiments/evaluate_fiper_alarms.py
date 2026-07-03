#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path
from collections import defaultdict
import numpy as np

def main():
    campaign_dir = Path("/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/experiments/stage9_fiper_v2_sam_20h_20260520_173700")
    hard_eval_dir = campaign_dir / "datasets" / "hard_eval_v2"
    corrected_splits_dir = campaign_dir / "datasets" / "corrected_splits_v2"
    out_dir = campaign_dir / "hard_eval_results"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Load RND conformal thresholds and scores
    conformal_path = campaign_dir / "fiper" / "rnd_conformal_thresholds.json"
    if not conformal_path.exists():
        conformal_path = campaign_dir / "fiper" / "rnd_success_only" / "rnd_conformal_thresholds.json"
        
    if not conformal_path.exists():
        print(f"ERROR: conformal thresholds not found.")
        sys.exit(1)
        
    with conformal_path.open() as f:
        conformal = json.load(f)
    q95_rnd = conformal["q95"]
    q99_rnd = conformal["q99"]
    
    print(f"Loaded RND Conformal Thresholds: q95={q95_rnd:.6f}, q99={q99_rnd:.6f}")
    
    rnd_scores = {}
    rnd_scores_path = campaign_dir / "fiper" / "rnd_success_only" / "rnd_scores_all.jsonl"
    with rnd_scores_path.open() as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                rnd_scores[row["sample_id"]] = row["rnd_score"]
    print(f"Loaded RND scores for {len(rnd_scores)} samples.")
    
    # 2. Load ACE group scores
    ace_scores = {}
    for sub in ["ace_failure_mined_sam", "ace_safe_mass_sam"]:
        ace_path = campaign_dir / "fiper" / sub / "ace_group_summaries.jsonl"
        if ace_path.exists():
            with ace_path.open() as f:
                for line in f:
                    if line.strip():
                        row = json.loads(line)
                        state_id = row["state_id"]
                        # Store the max ACE score in case a state_id is present in both
                        if state_id in ace_scores:
                            ace_scores[state_id] = max(ace_scores[state_id], row["ace_score"])
                        else:
                            ace_scores[state_id] = row["ace_score"]
                            
    print(f"Loaded ACE scores for {len(ace_scores)} state groups.")
    
    # Let's write helper function to extract state_id from group_id or sample_id
    def get_state_id(row):
        gid = row.get("group_id", "")
        if gid.startswith("state_"):
            return gid[6:]
        return gid
        
    # 3. Calibrate ACE threshold on train/calib low-risk samples (risk_score <= 0.20)
    train_rows = []
    for split_name in ["train", "calib"]:
        split_path = corrected_splits_dir / f"{split_name}.jsonl"
        if split_path.exists():
            with split_path.open() as f:
                for line in f:
                    if line.strip():
                        train_rows.append(json.loads(line))
                        
    # Find ACE scores for low-risk training groups
    low_risk_train_aces = []
    for r in train_rows:
        if r.get("risk_score", 1.0) <= 0.20:
            sid = get_state_id(r)
            if sid in ace_scores:
                low_risk_train_aces.append(ace_scores[sid])
                
    if len(low_risk_train_aces) > 0:
        # We want 95% specificity -> threshold is the 95th percentile of low-risk ACE scores
        q95_ace = float(np.percentile(low_risk_train_aces, 95))
        q99_ace = float(np.percentile(low_risk_train_aces, 99))
    else:
        # Fallback to reasonable defaults from report
        q95_ace = -120.0
        q99_ace = -100.0
        
    print(f"Calibrated ACE Thresholds (from {len(low_risk_train_aces)} train samples): q95={q95_ace:.4f}, q99={q99_ace:.4f}")
    
    # 4. Evaluate alarms on hard eval splits
    splits = [
        "hard_balanced_test",
        "state_context_test",
        "action_specific_test",
        "ood_task_test",
        "ood_source_test",
        "expert_false_alarm_test",
        "same_state_group_test",
    ]
    
    alarm_results = {}
    
    for split_name in splits:
        jsonl_path = hard_eval_dir / f"{split_name}.jsonl"
        rows = []
        with jsonl_path.open() as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
                    
        total = len(rows)
        # Classify high vs low risk:
        # High: risk_score >= 0.75 or label == VALIDATED_BAD
        # Low: risk_score <= 0.20 or label == GOOD_STRONG
        highs = []
        lows = []
        
        for r in rows:
            sid = r["sample_id"]
            rnd_val = rnd_scores.get(sid)
            # if RND not in rnd_scores, fallback to in-distribution (0.0)
            if rnd_val is None:
                rnd_val = 0.0
                
            state_id = get_state_id(r)
            ace_val = ace_scores.get(state_id)
            # if ACE not in ace_scores, fallback to safe entropy (min of ace_scores or -220.0)
            if ace_val is None:
                ace_val = -220.0
                
            sample_data = {
                "sample_id": sid,
                "risk_score": r["risk_score"],
                "label": r["label"],
                "bad_subtype": r["bad_subtype"],
                "rnd_score": rnd_val,
                "ace_score": ace_val,
                "rnd_alarm_95": bool(rnd_val >= q95_rnd),
                "rnd_alarm_99": bool(rnd_val >= q99_rnd),
                "ace_alarm_95": bool(ace_val >= q95_ace),
                "ace_alarm_99": bool(ace_val >= q99_ace),
                "combined_alarm_95": bool((rnd_val >= q95_rnd) or (ace_val >= q95_ace)),
                "combined_alarm_99": bool((rnd_val >= q99_rnd) or (ace_val >= q99_ace)),
            }
            
            is_high = (r["risk_score"] >= 0.75 or r["label"] == "VALIDATED_BAD")
            is_low = (r["risk_score"] <= 0.20 or r["label"] == "GOOD_STRONG")
            
            if is_high:
                highs.append(sample_data)
            elif is_low:
                lows.append(sample_data)
            else:
                # Still store intermediate ones under lows or keep separate
                lows.append(sample_data)
                
        def get_alarm_stats(samples):
            n = len(samples)
            if n == 0:
                return {"count": 0}
            rnd_95 = sum(1 for s in samples if s["rnd_alarm_95"])
            rnd_99 = sum(1 for s in samples if s["rnd_alarm_99"])
            ace_95 = sum(1 for s in samples if s["ace_alarm_95"])
            ace_99 = sum(1 for s in samples if s["ace_alarm_99"])
            comb_95 = sum(1 for s in samples if s["combined_alarm_95"])
            comb_99 = sum(1 for s in samples if s["combined_alarm_99"])
            
            return {
                "count": n,
                "rnd_alarm_95_rate": float(rnd_95 / n),
                "rnd_alarm_99_rate": float(rnd_99 / n),
                "ace_alarm_95_rate": float(ace_95 / n),
                "ace_alarm_99_rate": float(ace_99 / n),
                "combined_alarm_95_rate": float(comb_95 / n),
                "combined_alarm_99_rate": float(comb_99 / n),
            }
            
        alarm_results[split_name] = {
            "total_count": total,
            "high_risk_stats": get_alarm_stats(highs),
            "low_risk_stats": get_alarm_stats(lows),
        }
        
    # Write report
    report_lines = [
        "# FIPER Anomaly Detection & Failure Alarm Evaluation Report",
        "",
        f"- **Calibrated RND Thresholds**: q95 = `{q95_rnd:.6f}`, q99 = `{q99_rnd:.6f}`",
        f"- **Calibrated ACE Thresholds**: q95 = `{q95_ace:.4f}`, q99 = `{q99_ace:.4f}`",
        "",
        "## Alarm Trigger Rates by Split (High-Risk vs Low-Risk)",
        "",
        "| Split | High-Risk N | RND-95 High | ACE-95 High | Combined-95 High | Low-Risk N | RND-95 Low | ACE-95 Low | Combined-95 Low |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    
    for split_name in splits:
        res = alarm_results[split_name]
        h = res["high_risk_stats"]
        l = res["low_risk_stats"]
        
        h_count = h.get("count", 0)
        h_rnd = f"{h.get('rnd_alarm_95_rate', 0.0):.4f}" if h_count else "N/A"
        h_ace = f"{h.get('ace_alarm_95_rate', 0.0):.4f}" if h_count else "N/A"
        h_comb = f"{h.get('combined_alarm_95_rate', 0.0):.4f}" if h_count else "N/A"
        
        l_count = l.get("count", 0)
        l_rnd = f"{l.get('rnd_alarm_95_rate', 0.0):.4f}" if l_count else "N/A"
        l_ace = f"{l.get('ace_alarm_95_rate', 0.0):.4f}" if l_count else "N/A"
        l_comb = f"{l.get('combined_alarm_95_rate', 0.0):.4f}" if l_count else "N/A"
        
        report_lines.append(
            f"| {split_name} | {h_count} | {h_rnd} | {h_ace} | {h_comb} | {l_count} | {l_rnd} | {l_ace} | {l_comb} |"
        )
        
    report_lines.extend([
        "",
        "## Subtype-Specific Recall (State Context vs Action Specific)",
        "",
        "For failure-mined high-risk samples, we evaluate alarm detection recall based on the underlying failure subtype.",
        "",
    ])
    
    # Calculate subtype stats across state_context_test and action_specific_test
    # 1. State Context High Risk Recall
    res_sc = alarm_results["state_context_test"]
    sc_h = res_sc["high_risk_stats"]
    report_lines.extend([
        "### State Context Failures",
        f"- **Total Samples (State Context High Risk)**: `{sc_h.get('count', 0)}`",
        f"- **RND-95 Recall**: `{sc_h.get('rnd_alarm_95_rate', 0.0):.4f}`",
        f"- **ACE-95 Recall**: `{sc_h.get('ace_alarm_95_rate', 0.0):.4f}`",
        f"- **Combined-95 Recall**: `{sc_h.get('combined_alarm_95_rate', 0.0):.4f}`",
        "",
    ])
    
    # 2. Action Specific High Risk Recall
    res_as = alarm_results["action_specific_test"]
    as_h = res_as["high_risk_stats"]
    report_lines.extend([
        "### Action Specific Failures",
        f"- **Total Samples (Action Specific High Risk)**: `{as_h.get('count', 0)}`",
        f"- **RND-95 Recall**: `{as_h.get('rnd_alarm_95_rate', 0.0):.4f}`",
        f"- **ACE-95 Recall**: `{as_h.get('ace_alarm_95_rate', 0.0):.4f}`",
        f"- **Combined-95 Recall**: `{as_h.get('combined_alarm_95_rate', 0.0):.4f}`",
        "",
    ])
    
    # Write outputs
    report_file = out_dir / "fiper_alarm_evaluation_report.md"
    report_file.write_text("\n".join(report_lines) + "\n")
    
    # Also save raw results as json
    raw_results_file = out_dir / "fiper_alarm_evaluation_results.json"
    with raw_results_file.open("w") as f:
        json.dump(alarm_results, f, indent=2, sort_keys=True, default=str)
        
    print(f"FIPER Alarm Evaluation Report saved to {report_file}")

if __name__ == "__main__":
    main()
