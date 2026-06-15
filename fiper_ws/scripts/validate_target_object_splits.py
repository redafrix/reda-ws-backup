#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from collections import defaultdict

def validate_fold(fold_dir):
    fold_dir = Path(fold_dir)
    if not fold_dir.exists():
        return False, f"Fold directory {fold_dir} does not exist."

    # Load config
    config_path = fold_dir / "experiment_config.json"
    if not config_path.exists():
        return False, f"Config not found at {config_path}"
    with config_path.open() as f:
        config = json.load(f)
    
    heldout_objects = set(config["heldout_objects"])
    fold_name = config["name"]
    
    refs_dir = fold_dir / "datasets/refs"
    split_names = [
        "success_train_seen",
        "success_calib_seen",
        "success_test_seen",
        "success_test_ood",
        "failure_eval_seen",
        "failure_eval_ood",
        "failure_eval_ood_late",
        "failure_eval_ood_near_end",
    ]
    
    stats = {}
    episodes_by_split = {}
    rows_by_split = {}
    
    for split_name in split_names:
        ep_file = refs_dir / f"{split_name}.episodes.jsonl"
        rows_file = refs_dir / f"{split_name}.rows.jsonl"
        
        if not ep_file.exists() or not rows_file.exists():
            return False, f"Missing ref files for split {split_name} in {fold_name}"
            
        eps = []
        with ep_file.open() as f:
            for line in f:
                if line.strip():
                    eps.append(json.loads(line))
        episodes_by_split[split_name] = eps
        
        rows = []
        with rows_file.open() as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
        rows_by_split[split_name] = rows
        
        stats[split_name] = {
            "episodes": len(eps),
            "rows": len(rows),
            "targets": set(e["target_object_label"] for e in eps)
        }
        
    # 1. Leakage Checks
    # No held-out objects in seen splits
    seen_splits = ["success_train_seen", "success_calib_seen", "success_test_seen", "failure_eval_seen"]
    for split in seen_splits:
        overlap = stats[split]["targets"] & heldout_set
        if overlap:
            return False, f"LEAKAGE: Seen split {split} contains heldout objects: {overlap}"
            
    # OOD splits contain ONLY held-out objects
    ood_splits = ["success_test_ood", "failure_eval_ood", "failure_eval_ood_late", "failure_eval_ood_near_end"]
    for split in ood_splits:
        other_objects = stats[split]["targets"] - heldout_set
        if other_objects:
            return False, f"LEAKAGE: OOD split {split} contains non-heldout objects: {other_objects}"
            
    # 2. Success split episode disjointness
    seen_success_splits = ["success_train_seen", "success_calib_seen", "success_test_seen"]
    for i in range(len(seen_success_splits)):
        for j in range(i + 1, len(seen_success_splits)):
            s1 = seen_success_splits[i]
            s2 = seen_success_splits[j]
            keys1 = set(e["episode_key"] for e in episodes_by_split[s1])
            keys2 = set(e["episode_key"] for e in episodes_by_split[s2])
            overlap = keys1 & keys2
            if overlap:
                return False, f"DISJOINTNESS FAIL: Episodes overlap between {s1} and {s2}: {overlap}"
                
    # OOD success vs seen success disjointness
    ood_keys = set(e["episode_key"] for e in episodes_by_split["success_test_ood"])
    for s in seen_success_splits:
        seen_keys = set(e["episode_key"] for e in episodes_by_split[s])
        overlap = ood_keys & seen_keys
        if overlap:
            return False, f"DISJOINTNESS FAIL: OOD success episodes overlap with {s}: {overlap}"
            
    # Seen failure vs OOD failure disjointness
    seen_fail_keys = set(e["episode_key"] for e in episodes_by_split["failure_eval_seen"])
    ood_fail_keys = set(e["episode_key"] for e in episodes_by_split["failure_eval_ood"])
    overlap = seen_fail_keys & ood_fail_keys
    if overlap:
        return False, f"DISJOINTNESS FAIL: Failure episodes overlap between seen and OOD failures: {overlap}"

    # Verify rows vs episode row count consistency
    for split in split_names:
        sum_rows = sum(e["num_rows"] for e in episodes_by_split[split])
        if sum_rows != stats[split]["rows"]:
            return False, f"COUNT MISMATCH: Sum of episodes num_rows ({sum_rows}) != split rows file count ({stats[split]['rows']}) for split {split}"

    # Status confirmation
    fail_eval_ood_eps = stats["failure_eval_ood"]["episodes"]
    if fail_eval_ood_eps < 20:
        expected_status = "LOW_OOD_FAILURE_SUPPORT"
    else:
        expected_status = "READY_STRONG"
        
    actual_status = config["status"]
    if actual_status != expected_status:
        return False, f"STATUS MISMATCH: config status {actual_status} != expected status {expected_status} (failures: {fail_eval_ood_eps})"

    return True, stats

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_target_object_splits.py <benchmark_dir>")
        sys.exit(1)
        
    benchmark_dir = Path(sys.argv[1])
    if not benchmark_dir.exists():
        print(f"Benchmark directory {benchmark_dir} not found.")
        sys.exit(1)
        
    folds = sorted(list(benchmark_dir.glob("fold_*")))
    all_pass = True
    
    print(f"Validating benchmark at {benchmark_dir}...")
    for fold in folds:
        config_path = fold / "experiment_config.json"
        if not config_path.exists():
            continue
        with config_path.open() as f:
            config = json.load(f)
        heldout_set = set(config["heldout_objects"])
        
        ok, res = validate_fold(fold)
        if ok:
            print(f"  Fold {fold.name}: PASS")
            # print splits summary in a clean format
            for split_name, s_data in res.items():
                print(f"    {split_name}: {s_data['episodes']} ep / {s_data['rows']} rows, targets: {s_data['targets']}")
        else:
            print(f"  Fold {fold.name}: FAIL - {res}")
            all_pass = False
            
    if all_pass:
        print("ALL FOLDS VALIDATED SUCCESSFULLY!")
        sys.exit(0)
    else:
        print("SOME FOLDS FAILED VALIDATION!")
        sys.exit(1)
