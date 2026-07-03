import os
import json
import random
import numpy as np
import math

SOURCE_JSONL = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl"
DEST_DIR = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/seen_goal_object_fiper_subset"
BOB_STATES_DIR = os.path.join(DEST_DIR, "states")

# Target counts
TRAIN_SUCCESS_TARGET = 500
CALIB_SUCCESS_TARGET = 150
TEST_SUCCESS_TARGET = 150
TEST_FAILURE_TARGET = 100

SEED = 20260701

def main():
    print("Starting validation of JSONL source data...")
    
    # 1. First pass: scan file, extract metadata, validate fields and shapes
    episodes_meta = {} # episode_id -> {task_id, outcome, row_count, line_numbers}
    
    # Track statistics
    total_rows = 0
    corrupt_rows = 0
    nan_inf_found = 0
    
    # Set to check unique values
    all_task_ids = set()
    all_outcomes = set()
    
    # We will validate shapes:
    # main_candidate_action_chunk_env: [10, 7]
    # ace_candidate_chunks_env: [8, 10, 7]
    
    with open(SOURCE_JSONL, 'r') as f:
        for line_idx, line in enumerate(f):
            total_rows += 1
            if total_rows % 100000 == 0:
                print(f"Scanned {total_rows} rows...")
                
            try:
                row = json.loads(line)
            except Exception as e:
                print(f"Error parsing JSON at line {line_idx}: {e}")
                corrupt_rows += 1
                continue
                
            # Check presence of required fields
            required_keys = [
                'main_candidate_action_chunk_env',
                'ace_candidate_chunks_env',
                'current',
                'episode_id',
                'timestep',
                'episode_outcome',
                'task_id'
            ]
            missing_keys = [k for k in required_keys if k not in row]
            if 'current' in row and 'sim_state_path' not in row['current']:
                missing_keys.append('current.sim_state_path')
                
            if missing_keys:
                print(f"Row {line_idx} missing keys: {missing_keys}")
                corrupt_rows += 1
                continue
                
            episode_id = row['episode_id']
            task_id = row['task_id']
            outcome = row['episode_outcome']
            timestep = row['timestep']
            sim_state_path = row['current']['sim_state_path']
            
            all_task_ids.add(task_id)
            all_outcomes.add(outcome)
            
            # Check action chunk shapes
            main_chunk = row['main_candidate_action_chunk_env']
            ace_chunks = row['ace_candidate_chunks_env']
            
            try:
                main_arr = np.array(main_chunk, dtype=np.float32)
                ace_arr = np.array(ace_chunks, dtype=np.float32)
            except Exception as e:
                print(f"Row {line_idx} action chunks cannot be converted to numpy: {e}")
                corrupt_rows += 1
                continue
                
            if main_arr.shape != (10, 7):
                print(f"Row {line_idx} main chunk has wrong shape {main_arr.shape}")
                corrupt_rows += 1
                continue
                
            if ace_arr.shape != (8, 10, 7):
                print(f"Row {line_idx} ACE chunks have wrong shape {ace_arr.shape}")
                corrupt_rows += 1
                continue
                
            # Perform NaN/Inf check on a sample (every 50th row) to be efficient
            if line_idx % 50 == 0:
                if not np.isfinite(main_arr).all() or not np.isfinite(ace_arr).all():
                    print(f"Row {line_idx} contains NaN or Inf values!")
                    nan_inf_found += 1
            
            # Record episode metadata
            if episode_id not in episodes_meta:
                episodes_meta[episode_id] = {
                    'task_id': task_id,
                    'outcome': outcome,
                    'row_count': 0,
                    'line_numbers': []
                }
            
            # Consistency checks within episode
            meta = episodes_meta[episode_id]
            if meta['task_id'] != task_id:
                print(f"Consistency error: episode {episode_id} has conflicting task_id: {meta['task_id']} vs {task_id}")
            if meta['outcome'] != outcome:
                print(f"Consistency error: episode {episode_id} has conflicting outcome: {meta['outcome']} vs {outcome}")
                
            meta['row_count'] += 1
            meta['line_numbers'].append(line_idx)
            
    print("\nFirst pass complete!")
    print(f"Total rows scanned: {total_rows}")
    print(f"Corrupt or invalid rows: {corrupt_rows}")
    print(f"NaN/Inf checks in sample (every 50th row) completed. Bad rows in sample: {nan_inf_found}")
    print(f"Unique tasks found: {len(all_task_ids)}: {sorted(list(all_task_ids))}")
    print(f"Unique outcomes found: {all_outcomes}")
    print(f"Total unique episodes: {len(episodes_meta)}")
    
    if corrupt_rows > 0:
        print("WARNING: Found corrupt rows. Please inspect.")
        
    # Group episodes by task_id and success/failure
    success_episodes_by_task = {} # task_id -> list of episode_ids
    failure_episodes_by_task = {} # task_id -> list of episode_ids
    
    for tid in all_task_ids:
        success_episodes_by_task[tid] = []
        failure_episodes_by_task[tid] = []
        
    for ep_id, meta in episodes_meta.items():
        tid = meta['task_id']
        outcome = meta['outcome']
        if outcome == 'success':
            success_episodes_by_task[tid].append(ep_id)
        elif outcome == 'failure_or_timeout':
            failure_episodes_by_task[tid].append(ep_id)
        else:
            print(f"Unknown outcome '{outcome}' for episode {ep_id}")
            
    # Print counts per task
    print("\nOriginal episode count by task:")
    for tid in sorted(list(all_task_ids)):
        s_count = len(success_episodes_by_task[tid])
        f_count = len(failure_episodes_by_task[tid])
        print(f"  Task {tid}: Successes = {s_count}, Failures = {f_count}, Total = {s_count + f_count}")
        
    # 2. Selection algorithm
    # We want to select:
    # - train_success: 500 success episodes
    # - calib_success: 150 success episodes
    # - seen_test_success: 150 success episodes
    # - seen_test_failure: up to 100 failure episodes
    
    # Shuffle lists deterministically
    rng = random.Random(SEED)
    
    # To keep selection round-robin and balanced, sort tasks
    sorted_task_ids = sorted(list(all_task_ids))
    
    # For successes, shuffle each task's pool
    success_pools = {}
    for tid in sorted_task_ids:
        pool = sorted(success_episodes_by_task[tid]) # sort first for determinism
        rng.shuffle(pool)
        success_pools[tid] = pool
        
    # Pick success episodes using round-robin over tasks
    selected_train = []
    selected_calib = []
    selected_test_success = []
    
    # We will pick 500 for train, then 150 for calib, then 150 for test.
    # This prevents any overlap.
    
    # 1) Train success (500)
    task_idx = 0
    while len(selected_train) < TRAIN_SUCCESS_TARGET:
        # Check if all pools are empty
        if all(len(success_pools[t]) == 0 for t in sorted_task_ids):
            print("ERROR: Ran out of success episodes while picking train successes!")
            break
        tid = sorted_task_ids[task_idx % len(sorted_task_ids)]
        if len(success_pools[tid]) > 0:
            selected_train.append(success_pools[tid].pop(0))
        task_idx += 1
        
    # 2) Calib success (150)
    task_idx = 0
    while len(selected_calib) < CALIB_SUCCESS_TARGET:
        if all(len(success_pools[t]) == 0 for t in sorted_task_ids):
            print("ERROR: Ran out of success episodes while picking calib successes!")
            break
        tid = sorted_task_ids[task_idx % len(sorted_task_ids)]
        if len(success_pools[tid]) > 0:
            selected_calib.append(success_pools[tid].pop(0))
        task_idx += 1
        
    # 3) Test success (150)
    task_idx = 0
    while len(selected_test_success) < TEST_SUCCESS_TARGET:
        if all(len(success_pools[t]) == 0 for t in sorted_task_ids):
            print("ERROR: Ran out of success episodes while picking test successes!")
            break
        tid = sorted_task_ids[task_idx % len(sorted_task_ids)]
        if len(success_pools[tid]) > 0:
            selected_test_success.append(success_pools[tid].pop(0))
        task_idx += 1
        
    # For failures, shuffle each task's pool
    failure_pools = {}
    for tid in sorted_task_ids:
        pool = sorted(failure_episodes_by_task[tid]) # sort first for determinism
        rng.shuffle(pool)
        failure_pools[tid] = pool
        
    # 4) Test failure (up to 100)
    selected_test_failure = []
    task_idx = 0
    while len(selected_test_failure) < TEST_FAILURE_TARGET:
        if all(len(failure_pools[t]) == 0 for t in sorted_task_ids):
            print("Finished selecting all available failures.")
            break
        tid = sorted_task_ids[task_idx % len(sorted_task_ids)]
        if len(failure_pools[tid]) > 0:
            selected_test_failure.append(failure_pools[tid].pop(0))
        task_idx += 1
        
    print("\nSelection completed:")
    print(f"  train_success: {len(selected_train)}")
    print(f"  calib_success: {len(selected_calib)}")
    print(f"  seen_test_success: {len(selected_test_success)}")
    print(f"  seen_test_failure: {len(selected_test_failure)}")
    total_selected_episodes = len(selected_train) + len(selected_calib) + len(selected_test_success) + len(selected_test_failure)
    print(f"  Total selected: {total_selected_episodes} episodes")
    
    # Verify no overlap
    set_train = set(selected_train)
    set_calib = set(selected_calib)
    set_test_success = set(selected_test_success)
    set_test_failure = set(selected_test_failure)
    
    assert len(set_train) == len(selected_train)
    assert len(set_calib) == len(selected_calib)
    assert len(set_test_success) == len(selected_test_success)
    assert len(set_test_failure) == len(selected_test_failure)
    
    overlap = (set_train & set_calib) | (set_train & set_test_success) | (set_train & set_test_failure) | \
              (set_calib & set_test_success) | (set_calib & set_test_failure) | \
              (set_test_success & set_test_failure)
              
    assert len(overlap) == 0, f"Overlap detected between splits: {overlap}"
    print("Overlap check passed: Splits are mutually exclusive.")
    
    # Map episode_id -> split
    episode_to_split = {}
    for ep in selected_train: episode_to_split[ep] = 'train_success'
    for ep in selected_calib: episode_to_split[ep] = 'calib_success'
    for ep in selected_test_success: episode_to_split[ep] = 'seen_test_success'
    for ep in selected_test_failure: episode_to_split[ep] = 'seen_test_failure'
    
    # Count of selected episodes by task for each split
    split_task_counts = {
        'train_success': {tid: 0 for tid in sorted_task_ids},
        'calib_success': {tid: 0 for tid in sorted_task_ids},
        'seen_test_success': {tid: 0 for tid in sorted_task_ids},
        'seen_test_failure': {tid: 0 for tid in sorted_task_ids}
    }
    for ep, split in episode_to_split.items():
        tid = episodes_meta[ep]['task_id']
        split_task_counts[split][tid] += 1
        
    print("\nSelected episode count by task per split:")
    for split in ['train_success', 'calib_success', 'seen_test_success', 'seen_test_failure']:
        print(f"  Split: {split}")
        for tid in sorted_task_ids:
            print(f"    Task {tid}: {split_task_counts[split][tid]}")
            
    # 3. Create manifest and write outputs
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # 3a. Save selected_episodes.json
    selected_ep_data = {}
    for ep, split in episode_to_split.items():
        meta = episodes_meta[ep]
        selected_ep_data[ep] = {
            'split': split,
            'task_id': meta['task_id'],
            'outcome': meta['outcome'],
            'num_rows': meta['row_count']
        }
    with open(os.path.join(DEST_DIR, "selected_episodes.json"), 'w') as f_ep:
        json.dump(selected_ep_data, f_ep, indent=2)
        
    print("Saved selected_episodes.json")
    
    # 3b. Read source JSONL again and write selected_rows.jsonl, generating state transfer list
    state_transfer_manifest = [] # list of (sam_source, bob_dest)
    total_selected_rows = 0
    state_files_needed = set()
    
    output_rows_path = os.path.join(DEST_DIR, "selected_rows.jsonl")
    
    print("Writing selected_rows.jsonl and generating transfer manifest...")
    with open(SOURCE_JSONL, 'r') as f_src, open(output_rows_path, 'w') as f_dst:
        for line_idx, line in enumerate(f_src):
            # Parse line
            row = json.loads(line)
            episode_id = row['episode_id']
            if episode_id in episode_to_split:
                total_selected_rows += 1
                # Modify state path for Bob, saving the original Sam path
                original_state_path = row['current']['sim_state_path']
                filename = os.path.basename(original_state_path)
                bob_state_path = os.path.join(BOB_STATES_DIR, filename)
                
                row['current']['sim_state_path_sam_original'] = original_state_path
                row['current']['sim_state_path'] = bob_state_path
                
                # Write row
                f_dst.write(json.dumps(row) + "\n")
                
                # Add state file to manifest (if not already added)
                if original_state_path not in state_files_needed:
                    state_files_needed.add(original_state_path)
                    state_transfer_manifest.append((original_state_path, bob_state_path))
                    
    print(f"Saved {total_selected_rows} selected rows to selected_rows.jsonl")
    print(f"Unique state files needed: {len(state_files_needed)}")
    
    # 3c. Write state_transfer_manifest.txt
    manifest_path = os.path.join(DEST_DIR, "state_transfer_manifest.txt")
    with open(manifest_path, 'w') as f_man:
        for src, dst in sorted(state_transfer_manifest):
            f_man.write(f"{src}\t{dst}\n")
    print(f"Saved state_transfer_manifest.txt")
    
    # 3d. Generate SPLIT_SUMMARY.md
    summary_path = os.path.join(DEST_DIR, "SPLIT_SUMMARY.md")
    with open(summary_path, 'w') as f_sum:
        f_sum.write("# FIPER Dataset Split Summary\n\n")
        f_sum.write(f"Selection seed: `{SEED}`\n\n")
        f_sum.write("## Overview counts\n\n")
        f_sum.write("| Split | Episode Count | Row Count |\n")
        f_sum.write("|---|---|---|\n")
        for split in ['train_success', 'calib_success', 'seen_test_success', 'seen_test_failure']:
            eps_in_split = [ep for ep, s in episode_to_split.items() if s == split]
            rows_count = sum(episodes_meta[ep]['row_count'] for ep in eps_in_split)
            f_sum.write(f"| {split} | {len(eps_in_split)} | {rows_count} |\n")
        f_sum.write(f"| **Total** | **{total_selected_episodes}** | **{total_selected_rows}** |\n\n")
        
        f_sum.write("## Episode count per Task ID by Split\n\n")
        f_sum.write("| Task ID | train_success | calib_success | seen_test_success | seen_test_failure | Total |\n")
        f_sum.write("|---|---|---|---|---|---|\n")
        for tid in sorted_task_ids:
            t_train = split_task_counts['train_success'][tid]
            t_calib = split_task_counts['calib_success'][tid]
            t_test_s = split_task_counts['seen_test_success'][tid]
            t_test_f = split_task_counts['seen_test_failure'][tid]
            t_total = t_train + t_calib + t_test_s + t_test_f
            f_sum.write(f"| {tid} | {t_train} | {t_calib} | {t_test_s} | {t_test_f} | {t_total} |\n")
            
    print("Saved SPLIT_SUMMARY.md")
    
    # 3e. Generate PREP_REPORT.md
    report_path = os.path.join(DEST_DIR, "PREP_REPORT.md")
    with open(report_path, 'w') as f_rep:
        f_rep.write("# FIPER Dataset Preparation Report\n\n")
        f_rep.write("This report summarizes the data validation and selection results on Bob.\n\n")
        f_rep.write("## Source Information\n")
        f_rep.write(f"- **Source JSONL**: `{SOURCE_JSONL}`\n")
        f_rep.write(f"- **Total Source Rows**: {total_rows}\n")
        f_rep.write(f"- **Total Unique Source Episodes**: {len(episodes_meta)}\n")
        f_rep.write(f"- **Corrupt Rows**: {corrupt_rows}\n")
        f_rep.write(f"- **NaN/Inf Rows (in checked sample)**: {nan_inf_found}\n\n")
        
        f_rep.write("## Selection Parameters\n")
        f_rep.write(f"- **Seed**: `{SEED}`\n")
        f_rep.write(f"- **Total Target Episodes**: ~900 (successes: 800, failures: up to 100)\n\n")
        
        f_rep.write("## Selected Subset Statistics\n")
        f_rep.write(f"- **Total Selected Episodes**: {total_selected_episodes}\n")
        f_rep.write(f"- **Total Selected Rows**: {total_selected_rows}\n")
        f_rep.write(f"- **Unique State Files Required**: {len(state_files_needed)}\n\n")
        
        f_rep.write("## Destination Paths\n")
        f_rep.write(f"- **Workspace Destination**: `{DEST_DIR}`\n")
        f_rep.write("- **Generated Files**:\n")
        f_rep.write("  - `selected_episodes.json`\n")
        f_rep.write("  - `selected_rows.jsonl`\n")
        f_rep.write("  - `state_transfer_manifest.txt`\n")
        f_rep.write("  - `SPLIT_SUMMARY.md`\n")
        f_rep.write("  - `PREP_REPORT.md`\n")
        f_rep.write("  - `states/` (to be transferred from Sam)\n")
        
    print("Saved PREP_REPORT.md")
    
    print("\nDataset preparation script completed successfully!")

if __name__ == '__main__':
    main()
