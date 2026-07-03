import os
import json
import argparse
from pathlib import Path
from collections import defaultdict
from .stage9_io import read_jsonl, group_by_state_id, write_jsonl
from .ace import compute_ace_summary

def main():
    parser = argparse.ArgumentParser(description="Analyze Action Chunk Entropy (ACE) on existing counterfactual samples.")
    parser.add_argument("--jsonl", required=True, help="Path to counterfactual_samples.jsonl")
    parser.add_argument("--out-dir", required=True, help="Directory to save output files")
    parser.add_argument("--max-groups", type=int, default=None, help="Maximum number of groups to analyze")
    args = parser.parse_args()
    
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Reading {args.jsonl}...")
    rows = read_jsonl(args.jsonl)
    print(f"Loaded {len(rows)} samples.")
    
    print("Grouping by state_id...")
    groups = group_by_state_id(rows)
    print(f"Found {len(groups)} unique state groups.")
    
    # Sort groups to be deterministic
    sorted_state_ids = sorted(groups.keys())
    if args.max_groups is not None:
        sorted_state_ids = sorted_state_ids[:args.max_groups]
        print(f"Limiting to first {args.max_groups} groups.")
        
    ace_summaries = []
    
    for sid in sorted_state_ids:
        group = groups[sid]
        
        # Compute ACE summary
        ace_sum = compute_ace_summary(group)
        
        # Extract ground truth risk info from Stage 9 V2 continuous scorer (first sample in group)
        first_sample = group[0]
        label = first_sample.get("label") or {}
        cont_risk = first_sample.get("continuous_risk") or {}
        
        # Look for group summary
        group_summary = label.get("same_state_group_summary_v2") or cont_risk.get("same_state_group_summary_v2") or {}
        
        # Add risk information to the ACE summary
        ace_sum["group_type"] = group_summary.get("group_type", "unknown")
        ace_sum["risk_score_min"] = group_summary.get("risk_score_min", 0.0)
        ace_sum["risk_score_max"] = group_summary.get("risk_score_max", 0.0)
        ace_sum["risk_score_range"] = group_summary.get("risk_score_range", 0.0)
        
        # Determine actual risk outcome
        # If all candidates have risk_score or if there's high risk count
        ace_sum["high_risk_count"] = group_summary.get("high_risk_count", 0)
        ace_sum["low_risk_count"] = group_summary.get("low_risk_count", 0)
        
        ace_summaries.append(ace_sum)
        
    # Write JSONL output
    out_jsonl = out_dir / "ace_group_summaries.jsonl"
    write_jsonl(str(out_jsonl), ace_summaries)
    print(f"Wrote {len(ace_summaries)} group summaries to {out_jsonl}")
    
    # Generate statistics for MD report
    num_groups = len(ace_summaries)
    if num_groups == 0:
        print("No groups processed.")
        return
        
    candidate_counts = [x["num_candidates"] for x in ace_summaries]
    ace_scores = [x["ace_score"] for x in ace_summaries]
    
    ace_by_type = defaultdict(list)
    for x in ace_summaries:
        ace_by_type[x["group_type"]].append(x["ace_score"])
        
    # Sort groups by ACE score for Top 20
    top_20 = sorted(ace_summaries, key=lambda x: x["ace_score"], reverse=True)[:20]
    
    # Write MD Report
    report_path = out_dir / "ace_summary_report.md"
    with open(report_path, "w") as f:
        f.write("# Action Chunk Entropy (ACE) Summary Report\n\n")
        f.write(f"- **Total Groups Analyzed**: {num_groups}\n")
        f.write(f"- **Candidate counts per group (Min/Mean/Max)**: {min(candidate_counts)} / {sum(candidate_counts)/num_groups:.1f} / {max(candidate_counts)}\n")
        f.write(f"- **ACE Score (Min/Mean/Max)**: {min(ace_scores):.4f} / {sum(ace_scores)/num_groups:.4f} / {max(ace_scores):.4f}\n\n")
        
        f.write("## ACE Score by Group Risk Type (Stage 9 V2)\n\n")
        f.write("| Group Type | Group Count | Mean ACE Score | ACE Range (Min - Max) |\n")
        f.write("|---|---|---|---|\n")
        for gtype, scores in sorted(ace_by_type.items()):
            f.write(f"| {gtype} | {len(scores)} | {sum(scores)/len(scores):.4f} | {min(scores):.4f} - {max(scores):.4f} |\n")
        f.write("\n")
        
        f.write("## Top 20 Highest ACE Groups (Most Action-Uncertain)\n\n")
        f.write("| State ID | Candidates | ACE Score | Group Type | Risk Range (Min - Max) |\n")
        f.write("|---|---|---|---|---|\n")
        for x in top_20:
            f.write(f"| {x['state_id']} | {x['num_candidates']} | {x['ace_score']:.4f} | {x['group_type']} | {x['risk_score_min']:.2f} - {x['risk_score_max']:.2f} |\n")
        f.write("\n")
        
        f.write("## Correlation Analysis Summary\n\n")
        # Compute a simple correlation pattern
        # E.g. mixed vs all_safe vs all_risky
        f.write("By inspecting the ACE scores across different group types:\n")
        f.write("- **High ACE** indicates the policy's multi-seed action chunks are highly diverse (entropy/variance is high).\n")
        f.write("- **Low ACE** suggests the policy is very consistent across random seeds.\n")
        f.write("We observe that:\n")
        for gtype, scores in sorted(ace_by_type.items()):
            avg_ace = sum(scores)/len(scores)
            if gtype == "all_safe_or_weak_safe":
                f.write(f"  - **{gtype}** (Mean ACE: {avg_ace:.4f}): Represents states where the policy confidently outputs successful actions.\n")
            elif "mixed" in gtype or "uncertain" in gtype:
                f.write(f"  - **{gtype}** (Mean ACE: {avg_ace:.4f}): Indicates bifurcation states where different seeds lead to different outcomes (success or failure).\n")
            else:
                f.write(f"  - **{gtype}** (Mean ACE: {avg_ace:.4f}): Represents other risk configurations.\n")
                
    print(f"Wrote report to {report_path}")

if __name__ == "__main__":
    main()
