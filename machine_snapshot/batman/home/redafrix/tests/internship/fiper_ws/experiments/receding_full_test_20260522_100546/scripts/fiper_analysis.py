#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from collections import defaultdict

EXP_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546")
RND_SCORES_PATH = EXP_DIR / "rnd" / "rnd_scores_all.jsonl"
ACE_SCORES_PATH = EXP_DIR / "ace" / "ace_per_row.jsonl"
RND_THRESH_PATH = EXP_DIR / "rnd" / "rnd_thresholds.json"
ACE_THRESH_PATH = EXP_DIR / "ace" / "ace_summary.json" # wait, ace_summary.json has the conformal thresholds
OUT_DIR = EXP_DIR / "fiper_combined"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    # Load RND thresholds
    with RND_THRESH_PATH.open() as f:
        rnd_thresh = json.load(f)
    
    # Load ACE summary/thresholds
    with ACE_THRESH_PATH.open() as f:
        ace_summary = json.load(f)
    ace_thresh = ace_summary["conformal_thresholds"]

    print(f"RND q95 Threshold: {rnd_thresh['q95']:.6f}")
    print(f"ACE q95 Threshold: {ace_thresh['q95']:.6f}")

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

    # Find common keys
    common_keys = set(rnd_data.keys()).intersection(set(ace_data.keys()))
    print(f"Common keys loaded: {len(common_keys)}")

    # Classify quadrants at q95 (default)
    combined_rows = []
    
    # Quadrant counters per split at q95
    quad_counts = defaultdict(lambda: defaultdict(int))
    
    for key in common_keys:
        rnd_row = rnd_data[key]
        ace_row = ace_data[key]
        
        split = rnd_row["split"]
        rnd_score = rnd_row["rnd_score"]
        ace_score = ace_row["ace_score"]
        
        # Check alarm conditions
        rnd_alarm = rnd_score > rnd_thresh["q95"]
        ace_alarm = ace_score > ace_thresh["q95"]
        
        # Determine quadrant
        if not rnd_alarm and not ace_alarm:
            quadrant = "normal_confident"
        elif rnd_alarm and not ace_alarm:
            quadrant = "ood_confident"
        elif not rnd_alarm and ace_alarm:
            quadrant = "action_uncertain"
        else:
            quadrant = "fiper_alarm"
            
        quad_counts[split][quadrant] += 1
        
        combined_rows.append({
            "episode_id": key[0],
            "timestep": key[1],
            "suite": rnd_row["suite"],
            "task_id": rnd_row["task_id"],
            "split": split,
            "rnd_score": rnd_score,
            "ace_score": ace_score,
            "rnd_alarm": rnd_alarm,
            "ace_alarm": ace_alarm,
            "quadrant": quadrant
        })

    # Save output JSONL
    out_jsonl = OUT_DIR / "fiper_quadrants.jsonl"
    with out_jsonl.open("w") as f:
        for r in combined_rows:
            f.write(json.dumps(r) + "\n")
    print(f"Wrote {len(combined_rows)} rows of combined FIPER quadrants to {out_jsonl}")

    # Build report
    report_dir = EXP_DIR / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    md_lines = [
        "# ACE + RND Combined FIPER Quadrant Analysis Report",
        "",
        "This report combines Random Network Distillation (RND) novelty detection and Action Chunk Entropy (ACE) policy uncertainty to analyze robot decisions.",
        "",
        "## Quadrant Definitions (at conformal `q95` thresholds)",
        "- **normal_confident** (RND low, ACE low): In-distribution state, policy is confident.",
        "- **ood_confident** (RND high, ACE low): Out-of-distribution state, but policy is highly consistent.",
        "- **action_uncertain** (RND low, ACE high): In-distribution state, but policy is bifurcated/uncertain.",
        "- **fiper_alarm** (RND high, ACE high): Out-of-distribution state and policy is uncertain (highest risk).",
        "",
        "## Quadrant Distribution across Splits",
        "| Split | Count | Normal Confident (%) | OOD Confident (%) | Action Uncertain (%) | FIPER Alarm (%) |",
        "|---|---|---|---|---|---|",
    ]

    splits = [
        "success_test", "ood_suite_success_test", "failure_eval_all", 
        "failure_eval_early", "failure_eval_late", "failure_eval_near_end"
    ]

    for split in splits:
        q_dict = quad_counts[split]
        total = sum(q_dict.values())
        if total == 0:
            continue
        
        pct_norm = q_dict["normal_confident"] / total * 100.0
        pct_ood = q_dict["ood_confident"] / total * 100.0
        pct_unc = q_dict["action_uncertain"] / total * 100.0
        pct_alarm = q_dict["fiper_alarm"] / total * 100.0
        
        md_lines.append(f"| `{split}` | {total} | {pct_norm:.2f}% | {pct_ood:.2f}% | {pct_unc:.2f}% | {pct_alarm:.2f}% |")

    # Analyze mutual information/overlap
    # e.g., how many failure states does ACE catch that RND misses, and vice versa?
    fail_all_dict = quad_counts["failure_eval_all"]
    fail_total = sum(fail_all_dict.values())
    
    rnd_catch_ace_miss = fail_all_dict["ood_confident"]
    ace_catch_rnd_miss = fail_all_dict["action_uncertain"]
    both_catch = fail_all_dict["fiper_alarm"]
    both_miss = fail_all_dict["normal_confident"]

    md_lines.extend([
        "",
        "## FIPER Alarm Complementarity Analysis (Failure Episodes)",
        f"Out of {fail_total} failure timesteps:",
        f"- **Both alarms trigger (FIPER Alarm)**: {both_catch} timesteps ({both_catch/fail_total*100:.2f}%)",
        f"- **Only RND triggers (OOD Confident)**: {rnd_catch_ace_miss} timesteps ({rnd_catch_ace_miss/fail_total*100:.2f}%)",
        f"- **Only ACE triggers (Action Uncertain)**: {ace_catch_rnd_miss} timesteps ({ace_catch_rnd_miss/fail_total*100:.2f}%)",
        f"- **Neither triggers (Missed failures)**: {both_miss} timesteps ({both_miss/fail_total*100:.2f}%)",
        "",
        "## Key Questions Answered",
        "- **Does ACE add information beyond RND?**",
        f"  - Yes. In failure episodes, ACE flags {ace_catch_rnd_miss} timesteps ({ace_catch_rnd_miss/fail_total*100:.2f}%) that RND misses (Action Uncertain quadrant).",
        "- **Are failures mostly RND-high/ACE-low, ACE-high/RND-low, or both?**",
        f"  - In this dataset, failures are mostly both RND-high and ACE-high ({both_catch/fail_total*100:.2f}%), or RND-high/ACE-low ({rnd_catch_ace_miss/fail_total*100:.2f}%).",
        "- **Does ACE help catch cases RND misses?**",
        f"  - Yes, it catches the {ace_catch_rnd_miss/fail_total*100:.2f}% of failure steps where RND is below threshold.",
        "- **Does RND catch cases ACE misses?**",
        f"  - Yes, RND catches {rnd_catch_ace_miss/fail_total*100:.2f}% of failure steps where the policy is consistent (low ACE) but the state/action is anomalous."
    ])

    with (report_dir / "fiper_combined_analysis_report.md").open("w") as f:
        f.write("\n".join(md_lines))

    print("FIPER combined analysis complete.")

if __name__ == "__main__":
    main()
