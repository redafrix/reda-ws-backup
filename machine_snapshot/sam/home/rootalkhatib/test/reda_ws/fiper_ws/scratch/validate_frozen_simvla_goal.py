import json
import os
import sys
import numpy as np
from collections import Counter

DATASET_DIR = "/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622"

def main():
    print("Starting validation of frozen dataset...")
    summaries_path = os.path.join(DATASET_DIR, "episode_summaries.jsonl")
    samples_path = os.path.join(DATASET_DIR, "fiper_receding_samples.jsonl")

    # 1. Parse summaries
    print("Checking episode_summaries.jsonl...")
    if not os.path.exists(summaries_path):
        print(f"ERROR: {summaries_path} does not exist!")
        sys.exit(1)

    episodes = []
    with open(summaries_path, "r") as f:
        for idx, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                episodes.append(json.loads(line))
            except Exception as e:
                print(f"ERROR: Failed to parse summary line {idx}: {e}")
                sys.exit(1)

    print(f"Parsed {len(episodes)} episodes.")
    
    # Check exact episode count
    if len(episodes) != 5410:
        print(f"ERROR: Expected 5410 episodes, got {len(episodes)}")
        sys.exit(1)
        
    # Check duplicate episode_id
    episode_ids = [ep["episode_id"] for ep in episodes]
    unique_episode_ids = set(episode_ids)
    if len(episode_ids) != len(unique_episode_ids):
        print(f"ERROR: Found duplicate episode IDs! Total: {len(episode_ids)}, Unique: {len(unique_episode_ids)}")
        sys.exit(1)
    else:
        print("Success: No duplicate episode IDs found.")

    # Check per-task counts
    task_counts = Counter()
    for ep in episodes:
        task_id = ep.get("task_id")
        if task_id is None:
            parts = ep["episode_id"].split("_")
            task_part = [p for p in parts if p.startswith("t") and p[1:].isdigit()]
            if task_part:
                task_id = int(task_part[0][1:])
        task_counts[task_id] += 1

    print("Per-task counts:")
    for t in sorted(task_counts.keys()):
        print(f"  Task {t}: {task_counts[t]}")

    for t in range(10):
        if task_counts[t] != 541:
            print(f"ERROR: Task {t} count is {task_counts[t]}, expected 541")
            sys.exit(1)
    print("Success: Exact 541 episodes for each task (0..9) - complete rounds verified.")

    # Success/failure counts
    num_success = sum(1 for ep in episodes if ep.get("success", ep.get("outcome") == "success"))
    num_failure = len(episodes) - num_success
    print(f"Success/failure counts: Successes: {num_success}, Failures: {num_failure}")

    # Check max steps includes 800-step failures
    failure_steps = [ep["num_steps"] for ep in episodes if not ep.get("success", ep.get("outcome") == "success")]
    if not failure_steps:
        print("WARNING: No failures found in summaries!")
    else:
        max_failed_steps = max(failure_steps)
        print(f"Max steps in failed episodes: {max_failed_steps}")
        if max_failed_steps < 800:
            print(f"WARNING: Max failed steps is {max_failed_steps}, less than 800-step timeout limit!")
        else:
            print("Success: Max steps in failed episodes reaches 800.")

    # 2. Parse samples
    print("Checking fiper_receding_samples.jsonl...")
    if not os.path.exists(samples_path):
        print(f"ERROR: {samples_path} does not exist!")
        sys.exit(1)

    sample_count = 0
    sample_episodes = set()
    nan_inf_found = False

    # Check first few samples for schema completeness and check all for NaNs/infs
    with open(samples_path, "r") as f:
        for idx, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except Exception as e:
                print(f"ERROR: Failed to parse sample line {idx}: {e}")
                sys.exit(1)

            sample_count += 1
            ep_id = row.get("episode_id")
            if not ep_id:
                print(f"ERROR: Sample line {idx} is missing 'episode_id'")
                sys.exit(1)
            sample_episodes.add(ep_id)

            if ep_id not in unique_episode_ids:
                print(f"ERROR: Sample line {idx} has episode_id {ep_id} which is not in the frozen summaries!")
                sys.exit(1)

            # Perform detailed schema checks on first line
            if idx == 1:
                required_fields = [
                    'task_id', 'suite', 'episode_id', 'episode_outcome', 'timestep',
                    'current', 'main_candidate_action_chunk_normalized', 'ace_candidate_chunks_normalized',
                    'simvla_uncertainty_49d', 'simvla_uncertainty_raw', 'history'
                ]
                for field in required_fields:
                    if field not in row:
                        print(f"ERROR: Required field '{field}' is missing from sample row!")
                        sys.exit(1)
                
                if 'proprio' not in row['current']:
                    print("ERROR: 'proprio' is missing from 'current' field in sample row!")
                    sys.exit(1)
                print("Success: Required fields verified on the first sample.")

            # Validate feature arrays for NaN or inf
            action = np.array(row["main_candidate_action_chunk_normalized"])
            proprio = np.array(row["current"]["proprio"])
            ace = np.array(row["ace_candidate_chunks_normalized"])
            uncertainty = np.array(row["simvla_uncertainty_49d"])
            
            if np.isnan(action).any() or np.isinf(action).any():
                nan_inf_found = True
                print(f"ERROR: NaN/inf found in main_candidate_action_chunk_normalized at line {idx}")
                sys.exit(1)
            if np.isnan(proprio).any() or np.isinf(proprio).any():
                nan_inf_found = True
                print(f"ERROR: NaN/inf found in proprio at line {idx}")
                sys.exit(1)
            if np.isnan(ace).any() or np.isinf(ace).any():
                nan_inf_found = True
                print(f"ERROR: NaN/inf found in ace_candidate_chunks_normalized at line {idx}")
                sys.exit(1)
            if np.isnan(uncertainty).any() or np.isinf(uncertainty).any():
                nan_inf_found = True
                print(f"ERROR: NaN/inf found in simvla_uncertainty_49d at line {idx}")
                sys.exit(1)

    print(f"Successfully processed {sample_count} sample rows.")
    print(f"Unique episodes referenced in samples: {len(sample_episodes)}")
    
    # every sample row belongs to a frozen episode id, no extra sample rows from non-frozen episodes
    if len(sample_episodes) != len(unique_episode_ids):
        missing_eps = unique_episode_ids - sample_episodes
        if missing_eps:
            print(f"WARNING: Some frozen episodes have no samples in the samples file! Count missing: {len(missing_eps)}")
        extra_eps = sample_episodes - unique_episode_ids
        if extra_eps:
            print(f"ERROR: Samples file contains extra episode IDs not in summaries! Count: {len(extra_eps)}")
            sys.exit(1)
    else:
        print("Success: All sample rows map perfectly 1:1 to frozen episode IDs.")

    if not nan_inf_found:
        print("Success: Checked all feature arrays for NaN or inf, none found.")
        
    print("\nALL AUDIT CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
