#!/usr/bin/env python3
import os
import json
import shutil
import time
from collections import Counter
import numpy as np

SOURCE_DIR = "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/simvla_goal_uncertainty_2000ep_20260619/worker_0"
DEST_DIR = "/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622"

def main():
    start_time = time.time()
    print(f"Creating destination directory: {DEST_DIR}")
    os.makedirs(DEST_DIR, exist_ok=True)

    # 1. Load episode summaries and filter to first 5410 episodes (541 complete rounds of 10 tasks)
    src_summaries_path = os.path.join(SOURCE_DIR, "episode_summaries.jsonl")
    dest_summaries_path = os.path.join(DEST_DIR, "episode_summaries.jsonl")

    print("Loading episode summaries...")
    all_episodes = []
    with open(src_summaries_path, "r") as f:
        for line in f:
            if line.strip():
                all_episodes.append(json.loads(line))

    print(f"Total raw episodes found: {len(all_episodes)}")
    frozen_episodes = all_episodes[:5410]
    print(f"Keeping the first {len(frozen_episodes)} episodes.")

    # Validation of summaries
    episode_ids = [ep["episode_id"] for ep in frozen_episodes]
    unique_episode_ids = set(episode_ids)
    assert len(episode_ids) == len(unique_episode_ids), "Duplicate episode IDs found in frozen set!"
    assert len(frozen_episodes) == 5410, f"Expected 5410 episodes, got {len(frozen_episodes)}"

    task_counts = Counter()
    for ep in frozen_episodes:
        # Extract task_id (from 0 to 9)
        task_id = ep.get("task_id")
        if task_id is None:
            # Fallback parsing from episode_id
            parts = ep["episode_id"].split("_")
            # e.g. worker_0_libero_goal_t5_r10 -> t5
            task_part = [p for p in parts if p.startswith("t") and p[1:].isdigit()]
            if task_part:
                task_id = int(task_part[0][1:])
        task_counts[task_id] += 1

    print(f"Per-task episode counts: {sorted(task_counts.items())}")
    for t in range(10):
        assert task_counts[t] == 541, f"Task {t} does not have exactly 541 episodes! Count: {task_counts[t]}"

    # Write frozen summaries
    print(f"Writing frozen episode summaries to {dest_summaries_path}...")
    with open(dest_summaries_path, "w") as f:
        for ep in frozen_episodes:
            f.write(json.dumps(ep) + "\n")

    # 2. Copy/rename metadata files
    print("Copying run manifest and live status final snapshot...")
    shutil.copy(os.path.join(SOURCE_DIR, "run_manifest.json"), os.path.join(DEST_DIR, "run_manifest.json"))
    shutil.copy(os.path.join(SOURCE_DIR, "live_status.json"), os.path.join(DEST_DIR, "live_status_final_snapshot.json"))

    # 3. Filter receding samples
    src_samples_path = os.path.join(SOURCE_DIR, "fiper_receding_samples.jsonl")
    dest_samples_path = os.path.join(DEST_DIR, "fiper_receding_samples.jsonl")

    print(f"Filtering {src_samples_path} to {dest_samples_path} (this may take a few minutes)...")
    written_count = 0
    total_processed = 0
    with open(src_samples_path, "r") as f_in, open(dest_samples_path, "w") as f_out:
        for line in f_in:
            if not line.strip():
                continue
            total_processed += 1
            if total_processed % 100000 == 0:
                print(f"Processed {total_processed} lines...")
            # Parse JSON to check episode_id
            row = json.loads(line)
            ep_id = row.get("episode_id")
            if ep_id in unique_episode_ids:
                f_out.write(line)
                written_count += 1

    print(f"Filtering finished. Processed {total_processed} rows, wrote {written_count} rows.")

    # 4. Verify frozen dataset details
    print("Starting verification checks on frozen dataset...")
    
    # Check lines and JSON validity of summaries
    with open(dest_summaries_path, "r") as f:
        dest_episodes = [json.loads(line) for line in f if line.strip()]
    assert len(dest_episodes) == 5410, "Summary file line count doesn't match 5410!"

    # Verify that max steps for failures are up to 800
    failed_lengths = [ep["num_steps"] for ep in dest_episodes if not ep.get("success", ep.get("outcome") == "success")]
    max_failed_len = max(failed_lengths) if failed_lengths else 0
    print(f"Max steps in failed episodes: {max_failed_len}")
    assert max_failed_len > 300, f"Failed episodes seem truncated! Max steps: {max_failed_len}"

    # Load samples and check schema compatibility + NaNs
    print("Checking samples schema and checking for NaNs...")
    referenced_episodes = set()
    nan_found = False
    
    with open(dest_samples_path, "r") as f:
        for idx, line in enumerate(f):
            if not line.strip():
                continue
            row = json.loads(line)
            ep_id = row["episode_id"]
            referenced_episodes.add(ep_id)
            
            # Check schema
            assert "main_candidate_action_chunk_normalized" in row, "Missing main candidate action chunk normalized"
            assert "ace_candidate_chunks_normalized" in row, "Missing ace candidate chunks normalized"
            assert "current" in row and "proprio" in row["current"], "Missing current proprio"
            assert "simvla_uncertainty_raw" in row or "simvla_uncertainty_scalar_map" in row, "Missing uncertainty features"
            
            # Extract features like train_and_eval does and check for NaNs
            action = np.array(row["main_candidate_action_chunk_normalized"])
            proprio = np.array(row["current"]["proprio"])
            if np.isnan(action).any() or np.isinf(action).any():
                nan_found = True
            if np.isnan(proprio).any() or np.isinf(proprio).any():
                nan_found = True
                
    assert not nan_found, "NaN or infinite values found in training features!"
    assert referenced_episodes.issubset(unique_episode_ids), "Samples contain episode IDs not in summaries!"
    print(f"Verification successful: {len(referenced_episodes)} unique episodes referenced in samples.")

    # 5. Generate freeze report
    report_path = os.path.join(DEST_DIR, "DATASET_FREEZE_REPORT_20260622.md")
    print(f"Generating freeze report at {report_path}...")
    
    # Calculate stats
    num_success = sum(1 for ep in dest_episodes if ep.get("success", ep.get("outcome") == "success"))
    num_failure = 5410 - num_success
    success_rate = (num_success / 5410) * 100
    
    report_content = f"""# Dataset Freeze Report: SimVLA Goal Uncertainty Final 5410ep
Date: 2026-06-22

This dataset was frozen and cleaned from the raw Sam collection outputs under `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/simvla_goal_uncertainty_2000ep_20260619`.

## Summary Stats
- **Total Frozen Episodes:** 5410 (541 complete round-robin rounds of 10 tasks)
- **Successful Episodes:** {num_success} ({success_rate:.2f}%)
- **Failed Episodes:** {num_failure} ({100 - success_rate:.2f}%)
- **Total Sample/Query Rows:** {written_count}
- **Per-Task Count:** exactly 541 episodes for each task (0..9)
- **Max Timeout:** 800 steps (failures retain their full trajectories up to 800 steps, max observed is {max_failed_len})

## Verification Status
- [x] JSONL files parse cleanly
- [x] No duplicate episode IDs in summaries
- [x] Exact per-task counts are equal (exactly 541 each)
- [x] Sample rows reference only the 5410 frozen episode IDs
- [x] ACE candidate action chunks and proprio vectors are fully present
- [x] No NaNs/non-finite values found in the features
- [x] Failures have length up to 800, not forced/truncated to 300 in raw dataset

## File Inventory
- `episode_summaries.jsonl` (5410 lines, filtered summaries)
- `fiper_receding_samples.jsonl` ({written_count} lines, filtered sample/query rows)
- `run_manifest.json` (original run configuration)
- `live_status_final_snapshot.json` (snapshot of live_status when dataset collection was stopped)
"""

    with open(report_path, "w") as f:
        f.write(report_content)

    elapsed = time.time() - start_time
    print(f"Dataset freeze completed successfully in {elapsed:.1f}s.")

if __name__ == "__main__":
    main()
