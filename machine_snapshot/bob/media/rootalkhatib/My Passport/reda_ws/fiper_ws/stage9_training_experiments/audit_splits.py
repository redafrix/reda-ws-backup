#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description="Audit campaign splits for legitimate evaluation")
    parser.add_argument("--campaign-dir", required=True, help="Path to campaign root directory")
    parser.add_argument("--failure-jsonl", required=True, help="Path to raw failure mined jsonl")
    parser.add_argument("--safe-jsonl", required=True, help="Path to raw safe mass jsonl")
    parser.add_argument("--expert-jsonl", required=True, help="Path to raw expert anchor jsonl")
    parser.add_argument("--out-file", default="split_audit.md", help="Output audit filename inside campaign dir")
    return parser.parse_args()

def load_raw_dataset(path_str):
    path = Path(path_str)
    if not path.exists():
        print(f"WARN: Raw dataset {path} does not exist!")
        return {}
    
    data_map = {}
    print(f"Loading {path}...")
    with path.open() as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                sid = row.get("sample_id")
                if sid:
                    data_map[sid] = row
    print(f"Loaded {len(data_map)} samples from {path}")
    return data_map

def main():
    args = parse_args()
    campaign_dir = Path(args.campaign_dir)
    
    # Load all raw samples for enrichment
    raw_samples = {}
    raw_samples.update(load_raw_dataset(args.failure_jsonl))
    raw_samples.update(load_raw_dataset(args.safe_jsonl))
    raw_samples.update(load_raw_dataset(args.expert_jsonl))
    
    split_dir = campaign_dir / "datasets" / "continuous_v2_trainset"
    if not split_dir.exists():
        print(f"ERROR: Split directory does not exist at {split_dir}")
        sys.exit(1)
        
    splits = ["train", "calib", "test_seen_task", "test_unseen_group"]
    split_data = {}
    
    # Audit each split
    for split in splits:
        split_file = split_dir / f"{split}.jsonl"
        if not split_file.exists():
            print(f"WARN: Split file {split_file} not found, skipping.")
            continue
            
        rows = []
        with split_file.open() as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
        split_data[split] = rows
        
    print("Auditing split statistics...")
    
    audit_lines = [
        "# STAGE 9 SPLIT AUDIT REPORT",
        "",
        f"Campaign Directory: `{campaign_dir}`",
        ""
    ]
    
    # Split Summary Table
    audit_lines.extend([
        "## 1. Split Distribution Overview",
        "",
        "| Split | Sample Count | Unique States | Unique Tasks | Unique Suites | Min Risk | Mean Risk | Max Risk | Valid? |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
    ])
    
    split_group_types = {}
    split_subtypes = {}
    split_sources = {}
    split_state_ids = {}
    split_demo_names = {}
    split_sample_ids = {}
    
    for split, rows in split_data.items():
        sample_ids = set()
        state_ids = set()
        tasks = set()
        suites = set()
        demo_names = set()
        
        risk_scores = []
        high_risk_count = 0
        low_risk_count = 0
        
        subtypes = Counter()
        group_types = Counter()
        sources = Counter()
        
        has_pos = False
        has_neg = False
        
        for r in rows:
            sid = r["sample_id"]
            sample_ids.add(sid)
            
            # Risk info from manifest
            risk = float(r.get("risk_score", 0.0))
            risk_scores.append(risk)
            if risk >= 0.75 or r.get("risk_bin") == "RISKY_STRONG" or r.get("label") == "VALIDATED_BAD":
                high_risk_count += 1
                has_pos = True
            if risk <= 0.20 or r.get("risk_bin") == "SAFE_STRONG" or r.get("label") == "GOOD_STRONG":
                low_risk_count += 1
                has_neg = True
                
            subtypes[r.get("bad_subtype", "unknown")] += 1
            sources[r.get("source_tag", "")] += 1
            
            # Enrich from raw dataset if available
            raw = raw_samples.get(sid, {})
            meta = raw.get("metadata", {})
            cr = raw.get("continuous_risk", {})
            ssg = cr.get("same_state_group_summary_v2", {}) if isinstance(cr, dict) else {}
            
            state_id = meta.get("state_id")
            if state_id:
                state_ids.add(state_id)
                
            task_name = meta.get("task_name") or meta.get("task_language")
            if task_name:
                tasks.add(task_name)
                
            suite = meta.get("libero_pro_suite_or_task")
            if suite:
                suites.add(suite)
                
            demo_name = meta.get("demo_name")
            if demo_name:
                demo_names.add(demo_name)
                
            if isinstance(ssg, dict):
                group_type = ssg.get("group_type", "unknown")
                group_types[group_type] += 1
            else:
                group_types["unknown"] += 1
                
        # Determine validity: must have both high-risk and low-risk samples
        is_valid = "VALID" if (has_pos and has_neg) else "INVALID (Single Class)"
        
        # Save split maps for leakage check
        split_sample_ids[split] = sample_ids
        split_state_ids[split] = state_ids
        split_demo_names[split] = demo_names
        split_group_types[split] = group_types
        split_subtypes[split] = subtypes
        split_sources[split] = sources
        
        min_risk = min(risk_scores) if risk_scores else 0.0
        mean_risk = sum(risk_scores)/len(risk_scores) if risk_scores else 0.0
        max_risk = max(risk_scores) if risk_scores else 0.0
        
        audit_lines.append(
            f"| **`{split}`** | {len(rows)} | {len(state_ids)} | {len(tasks)} | {len(suites)} | {min_risk:.4f} | {mean_risk:.4f} | {max_risk:.4f} | **{is_valid}** |"
        )
        
    audit_lines.append("")
    
    # Sources distribution
    audit_lines.extend([
        "## 2. Data Source Breakdown",
        "",
        "| Split | Expert Anchors | Safe Mass | Failure Mined |",
        "| :--- | :---: | :---: | :---: |"
    ])
    for split in splits:
        src = split_sources.get(split, Counter())
        audit_lines.append(f"| `{split}` | {src.get('expert_anchor', 0)} | {src.get('safe_mass', 0)} | {src.get('failure_mined', 0)} |")
    audit_lines.append("")
    
    # Subtypes distribution
    audit_lines.extend([
        "## 3. Risk Subtype Breakdown",
        "",
        "| Split | unknown | state_context | action_specific |",
        "| :--- | :---: | :---: | :---: |"
    ])
    for split in splits:
        sub = split_subtypes.get(split, Counter())
        audit_lines.append(f"| `{split}` | {sub.get('unknown', 0)} | {sub.get('state_context', 0)} | {sub.get('action_specific', 0)} |")
    audit_lines.append("")
    
    # Same state group summary distribution
    audit_lines.extend([
        "## 4. Same-State Group Types Distribution",
        "",
        "| Split | all_safe_or_weak_safe | all_risky_state_context_candidate | action_specific_mixed | mixed_needs_review | uncertain |",
        "| :--- | :---: | :---: | :---: | :---: | :---: |"
    ])
    for split in splits:
        gt = split_group_types.get(split, Counter())
        audit_lines.append(f"| `{split}` | {gt.get('all_safe_or_weak_safe', 0)} | {gt.get('all_risky_state_context_candidate', 0)} | {gt.get('action_specific_mixed', 0)} | {gt.get('mixed_needs_review', 0)} | {gt.get('uncertain_or_low_confidence', 0)} |")
    audit_lines.append("")
    
    # Leakage Analysis
    audit_lines.extend([
        "## 5. Leakage Analysis",
        "",
        "Leakage check based on sample IDs, unique environmental state IDs, and demonstration names.",
        ""
    ])
    
    # Sample ID leakage
    audit_lines.append("### A. Sample ID Leakage (Duplicates)")
    has_leak = False
    for i, s1 in enumerate(splits):
        for s2 in splits[i+1:]:
            intersection = split_sample_ids.get(s1, set()) & split_sample_ids.get(s2, set())
            if len(intersection) > 0:
                audit_lines.append(f"- **WARNING**: `{s1}` vs `{s2}` shares {len(intersection)} identical `sample_id`s!")
                has_leak = True
    if not has_leak:
        audit_lines.append("- No sample ID leaks detected between splits.")
    audit_lines.append("")
    
    # State ID leakage
    audit_lines.append("### B. State ID Leakage (Mass/Failure Perturbations)")
    has_state_leak = False
    for i, s1 in enumerate(splits):
        for s2 in splits[i+1:]:
            intersection = split_state_ids.get(s1, set()) & split_state_ids.get(s2, set())
            if len(intersection) > 0:
                audit_lines.append(f"- **WARNING**: `{s1}` vs `{s2}` shares {len(intersection)} unique `state_id`s!")
                has_state_leak = True
    if not has_state_leak:
        audit_lines.append("- No state ID leaks detected between splits.")
    audit_lines.append("")
    
    # Demo Name leakage
    audit_lines.append("### C. Demo Name Leakage (Expert Demonstration Chunks)")
    has_demo_leak = False
    for i, s1 in enumerate(splits):
        for s2 in splits[i+1:]:
            intersection = split_demo_names.get(s1, set()) & split_demo_names.get(s2, set())
            if len(intersection) > 0:
                audit_lines.append(f"- **WARNING**: `{s1}` vs `{s2}` shares {len(intersection)} unique `demo_name`s!")
                has_demo_leak = True
    if not has_demo_leak:
        audit_lines.append("- No demo name leaks detected between splits.")
    audit_lines.append("")
    
    # Write out the file
    out_path = campaign_dir / args.out_file
    out_path.write_text("\n".join(audit_lines) + "\n")
    print(f"Audit report written to {out_path}")
    
    # Print summary to stdout
    print("\n".join(audit_lines))

if __name__ == "__main__":
    main()
