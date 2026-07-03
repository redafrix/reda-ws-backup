#!/usr/bin/env python3
import argparse
import json
import hashlib
import random
import sys
from pathlib import Path
from collections import Counter, defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description="Create group-safe splits and hard evaluation sets")
    parser.add_argument("--campaign-dir", required=True, help="Path to campaign root directory")
    parser.add_argument("--failure-jsonl", required=True, help="Path to raw failure mined jsonl")
    parser.add_argument("--safe-jsonl", required=True, help="Path to raw safe mass jsonl")
    parser.add_argument("--expert-jsonl", required=True, help="Path to raw expert anchor jsonl")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser.parse_args()

def get_state_group_id(sample):
    meta = sample.get("metadata", {})
    state_id = meta.get("state_id")
    if state_id:
        return f"state_{state_id}"
    
    cr = sample.get("continuous_risk", {})
    if isinstance(cr, dict):
        ssg = cr.get("same_state_group_summary_v2", {})
        if isinstance(ssg, dict) and ssg.get("state_id"):
            return f"state_{ssg.get('state_id')}"
            
    demo_name = meta.get("demo_name")
    task = meta.get("task_language") or meta.get("task_name") or "unk"
    if demo_name:
        return f"demo_{task}_{demo_name}"
        
    env_seed = meta.get("env_seed", meta.get("seed", "unk"))
    chunk_start = meta.get("chunk_start", meta.get("step_start", "unk"))
    return f"fallback_{task}_eseed{env_seed}_cs{chunk_start}"

def assign_split(group_id, seed):
    h = hashlib.md5(f"{group_id}_{seed}".encode()).hexdigest()
    val = int(h[:8], 16) / 0xFFFFFFFF
    if val < 0.70:
        return "train"
    elif val < 0.80:
        return "calib"
    elif val < 0.90:
        return "test_seen_task"
    else:
        return "test_unseen_group"

def load_jsonl(path_str, source_tag):
    path = Path(path_str)
    if not path.exists():
        print(f"WARN: {path} not found")
        return []
    rows = []
    with path.open() as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                row["_source_tag"] = source_tag
                row["_source_jsonl"] = str(path.absolute())
                rows.append(row)
    print(f"Loaded {len(rows)} from {path} (source={source_tag})")
    return rows


def get_risk_fields(sample):
    cr = sample.get("continuous_risk", {})
    if not isinstance(cr, dict):
        cr = {}
    lbl = sample.get("label", {})
    if not isinstance(lbl, dict):
        lbl_str = str(lbl) if lbl else "GOOD_STRONG"
        lbl = {}
    else:
        lbl_str = cr.get("legacy_label_suggestion", lbl.get("legacy_label_suggestion", "GOOD_STRONG"))

    return {
        "risk_score": float(cr.get("risk_score", lbl.get("risk_score", 0.0))),
        "risk_confidence": float(cr.get("risk_confidence", lbl.get("risk_confidence", 1.0))),
        "risk_bin": str(cr.get("risk_bin", lbl.get("risk_bin", "SAFE_STRONG"))),
        "legacy_label": str(cr.get("legacy_label_suggestion", lbl_str)),
        "bad_subtype": str(cr.get("bad_subtype", lbl.get("bad_subtype", "unknown"))),
    }

def main():
    args = parse_args()
    random.seed(args.seed)
    
    campaign_dir = Path(args.campaign_dir)
    corrected_dir = campaign_dir / "datasets" / "corrected_splits_v2"
    hard_eval_dir = campaign_dir / "datasets" / "hard_eval_v2"
    
    corrected_dir.mkdir(parents=True, exist_ok=True)
    hard_eval_dir.mkdir(parents=True, exist_ok=True)
    
    print("Loading raw files...")
    failure_rows = load_jsonl(args.failure_jsonl, "failure_mined")
    safe_rows = load_jsonl(args.safe_jsonl, "safe_mass")
    expert_rows = load_jsonl(args.expert_jsonl, "expert_anchor")
    
    all_rows = failure_rows + safe_rows + expert_rows
    print(f"Total samples loaded: {len(all_rows)}")
    
    # 1. Group by state / demo
    groups = defaultdict(list)
    for row in all_rows:
        gid = get_state_group_id(row)
        groups[gid].append(row)
    
    print(f"Total unique groups: {len(groups)}")
    
    # 2. Assign splits
    # Task 1 is held out as OOD Task
    splits = defaultdict(list)
    ood_task_groups = set()
    
    for gid, members in groups.items():
        # Check if this group belongs to task1
        is_task1 = False
        for m in members:
            meta = m.get("metadata", {})
            if meta.get("task_name") == "libero_spatial_with_mug_task1":
                is_task1 = True
                break
                
        if is_task1:
            split = "ood_task"
            ood_task_groups.add(gid)
        else:
            split = assign_split(gid, args.seed)
            
        for row in members:
            rf = get_risk_fields(row)
            manifest_row = {
                "sample_id": row.get("sample_id", ""),
                "split": split,
                "group_id": gid,
                "source_tag": row.get("_source_tag", ""),
                "label": rf["legacy_label"],
                "bad_subtype": rf["bad_subtype"],
                "risk_score": rf["risk_score"],
                "risk_confidence": rf["risk_confidence"],
                "risk_bin": rf["risk_bin"],
                "source_jsonl": row.get("_source_jsonl", ""),
            }
            splits[split].append(manifest_row)
            
    # Write corrected splits
    for split_name in ["train", "calib", "test_seen_task", "test_unseen_group"]:
        rows = splits.get(split_name, [])
        path = corrected_dir / f"{split_name}.jsonl"
        with path.open("w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
        print(f"Written {len(rows)} samples to corrected {path}")
        
    # Write combined manifest
    all_manifest = []
    for split_name in ["train", "calib", "test_seen_task", "test_unseen_group", "ood_task"]:
        all_manifest.extend(splits.get(split_name, []))
    with (corrected_dir / "all_manifest.jsonl").open("w") as f:
        for r in all_manifest:
            f.write(json.dumps(r) + "\n")
            
    # Write summary stats
    summary = {
        "total_samples": len(all_rows),
        "total_groups": len(groups),
        "ood_task_groups_count": len(ood_task_groups),
        "splits": {}
    }
    for split_name, rows in splits.items():
        risk_scores = [r["risk_score"] for r in rows]
        summary["splits"][split_name] = {
            "count": len(rows),
            "label_counts": dict(Counter(r["label"] for r in rows)),
            "risk_bin_counts": dict(Counter(r["risk_bin"] for r in rows)),
            "bad_subtype_counts": dict(Counter(r["bad_subtype"] for r in rows)),
            "source_counts": dict(Counter(r["source_tag"] for r in rows)),
            "risk_score_mean": float(sum(risk_scores)/len(risk_scores)) if risk_scores else 0.0,
            "high_risk_count": sum(1 for r in risk_scores if r >= 0.75),
            "low_risk_count": sum(1 for r in risk_scores if r <= 0.20),
        }
    with (corrected_dir / "split_summary.json").open("w") as f:
        json.dump(summary, f, indent=2, sort_keys=True, default=str)
    print("Corrected splits summary statistics saved.")
    
    # -------------------------------------------------------------
    # BUILD HARD EVALUATION SETS
    # -------------------------------------------------------------
    
    test_rows_seen = splits.get("test_seen_task", [])
    test_rows_unseen = splits.get("test_unseen_group", [])
    test_rows_all = test_rows_seen + test_rows_unseen
    
    # 1. hard_balanced_test.jsonl
    # Balanced low-risk and high-risk from test splits.
    # Include safe mass + expert anchors as low-risk.
    # Include failure-mined RISKY_STRONG as high-risk.
    low_risk_candidates = [r for r in test_rows_all if r["risk_score"] <= 0.20 and r["source_tag"] in {"safe_mass", "expert_anchor"}]
    high_risk_candidates = [r for r in test_rows_all if r["risk_score"] >= 0.75 and r["source_tag"] == "failure_mined" and r["risk_bin"] == "RISKY_STRONG"]
    
    num_samples = min(len(low_risk_candidates), len(high_risk_candidates))
    balanced_low = random.sample(low_risk_candidates, num_samples)
    balanced_high = random.sample(high_risk_candidates, num_samples)
    balanced_test = balanced_low + balanced_high
    random.shuffle(balanced_test)
    
    with (hard_eval_dir / "hard_balanced_test.jsonl").open("w") as f:
        for r in balanced_test:
            f.write(json.dumps(r) + "\n")
    print(f"1. Created hard_balanced_test.jsonl with {len(balanced_test)} samples ({num_samples} low, {num_samples} high)")
    
    # 2. state_context_test.jsonl
    # All available state_context high-risk samples. Matched low-risk samples if possible.
    # We load them from ALL splits (or just test? The prompt says 'all available state_context high-risk samples').
    # Let's search all manifest for state_context with high risk.
    state_ctx_high = [r for r in all_manifest if r["bad_subtype"] == "state_context" and r["risk_score"] >= 0.75]
    # Matched low-risk samples from expert/safe mass.
    matched_low = random.sample(low_risk_candidates + [r for r in all_manifest if r["split"] in {"test_seen_task", "test_unseen_group"} and r["risk_score"] <= 0.20], min(len(state_ctx_high), len(low_risk_candidates)))
    state_ctx_test = state_ctx_high + matched_low
    random.shuffle(state_ctx_test)
    
    with (hard_eval_dir / "state_context_test.jsonl").open("w") as f:
        for r in state_ctx_test:
            f.write(json.dumps(r) + "\n")
    print(f"2. Created state_context_test.jsonl with {len(state_ctx_test)} samples ({len(state_ctx_high)} high, {len(matched_low)} matched low)")
    
    # 3. action_specific_test.jsonl
    # All action_specific samples if any exist. Include matched same-state or same-task low-risk samples.
    act_spec_all = [r for r in all_manifest if r["bad_subtype"] == "action_specific"]
    # Matched low-risk samples
    matched_low_act = random.sample(low_risk_candidates, min(len(act_spec_all), len(low_risk_candidates)))
    act_spec_test = act_spec_all + matched_low_act
    random.shuffle(act_spec_test)
    
    with (hard_eval_dir / "action_specific_test.jsonl").open("w") as f:
        for r in act_spec_test:
            f.write(json.dumps(r) + "\n")
    print(f"3. Created action_specific_test.jsonl with {len(act_spec_test)} samples ({len(act_spec_all)} action-specific, {len(matched_low_act)} matched low)")
    
    # 4. ood_task_test.jsonl
    # Hold out task1. Must contain both low-risk and high-risk.
    ood_task_all = splits.get("ood_task", [])
    # Task1 has RISKY_STRONG (high risk) and SAFE_WEAK (lower risk).
    with (hard_eval_dir / "ood_task_test.jsonl").open("w") as f:
        for r in ood_task_all:
            f.write(json.dumps(r) + "\n")
    print(f"4. Created ood_task_test.jsonl with {len(ood_task_all)} samples (held-out task1)")
    
    # 5. ood_source_test.jsonl
    # Test separately on failure-mined source and safe-mass source.
    # We will put all test-split samples of safe_mass and failure_mined here.
    ood_src_rows = [r for r in test_rows_all if r["source_tag"] in {"safe_mass", "failure_mined"}]
    with (hard_eval_dir / "ood_source_test.jsonl").open("w") as f:
        for r in ood_src_rows:
            f.write(json.dumps(r) + "\n")
    print(f"5. Created ood_source_test.jsonl with {len(ood_src_rows)} samples")
    
    # 6. expert_false_alarm_test.jsonl
    # Expert anchors only from test splits.
    expert_test_rows = [r for r in test_rows_all if r["source_tag"] == "expert_anchor"]
    with (hard_eval_dir / "expert_false_alarm_test.jsonl").open("w") as f:
        for r in expert_test_rows:
            f.write(json.dumps(r) + "\n")
    print(f"6. Created expert_false_alarm_test.jsonl with {len(expert_test_rows)} samples")
    
    # 7. same_state_group_test.jsonl
    # Preserve all 64 seeds per state group in test splits.
    # Find all groups assigned to test splits.
    test_groups = set(r["group_id"] for r in test_rows_all if r["source_tag"] in {"safe_mass", "failure_mined"})
    same_state_rows = [r for r in test_rows_all if r["group_id"] in test_groups]
    with (hard_eval_dir / "same_state_group_test.jsonl").open("w") as f:
        for r in same_state_rows:
            f.write(json.dumps(r) + "\n")
    print(f"7. Created same_state_group_test.jsonl with {len(same_state_rows)} samples across {len(test_groups)} state groups")

if __name__ == "__main__":
    main()
