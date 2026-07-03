import os
import json
import pickle
import sys
import shutil
from pathlib import Path
import numpy as np
import torch

BASE_DIR = Path("/home/dean/fiper_uncertainty_collection")
EXP_DIR = BASE_DIR / "experiments" / "official_fiper_goal_object_ood_ablation_20260625"
CACHE_DIR = EXP_DIR / "cache"
DATA_ROOT = EXP_DIR / "official_fiper_data"

IN_DOMAIN_ROOT = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/worker_0")
IN_DOMAIN_QUERY_SAMPLES = IN_DOMAIN_ROOT / "stratified_query_samples_50train_15calib_per_task.jsonl"
OOD_ROOT = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622")

SPLITS = [
    "success_train_seen",
    "success_calib_seen",
    "success_test_seen",
    "success_test_ood",
    "failure_test_seen",
    "failure_eval_ood",
]

def main():
    in_domain_rows_by_ep = {}
    with open(IN_DOMAIN_QUERY_SAMPLES) as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            ep_id = row["episode_id"]
            in_domain_rows_by_ep.setdefault(ep_id, []).append(row)

    in_domain_summaries = {}
    with open(IN_DOMAIN_ROOT / "episode_summaries.jsonl") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                in_domain_summaries[row["episode_id"]] = row

    eps_by_task = {}
    for ep_id in sorted(in_domain_rows_by_ep):
        summary = in_domain_summaries[ep_id]
        if not bool(summary.get("success", False)):
            continue
        task_id = int(summary["task_id"])
        eps_by_task.setdefault(task_id, []).append(ep_id)

    expected_tasks = list(range(10))
    train_eps = []
    calib_eps = []
    for task_id in expected_tasks:
        eps = sorted(eps_by_task[task_id])
        train_eps.extend(eps[:50])
        calib_eps.extend(eps[50:65])

    train_eps_set = set(train_eps)
    calib_eps_set = set(calib_eps)
    assert len(train_eps) == 500
    assert len(calib_eps) == 150
    assert not train_eps_set.intersection(calib_eps_set)

    ood_rows_by_ep = {}
    with open(OOD_ROOT / "fiper_receding_samples.jsonl") as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            ep_id = row["episode_id"]
            ood_rows_by_ep.setdefault(ep_id, []).append(row)

    ood_outcomes = {}
    with open(OOD_ROOT / "episode_summaries.jsonl") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                ood_outcomes[row["episode_id"]] = row["success"]

    split_episodes = {
        "success_train_seen": train_eps,
        "success_calib_seen": calib_eps,
        "success_test_seen": [],
        "success_test_ood": [ep_id for ep_id, succ in ood_outcomes.items() if succ],
        "failure_test_seen": [],
        "failure_eval_ood": [ep_id for ep_id, succ in ood_outcomes.items() if not succ],
    }

    def get_ep_task_key(ep, split_name):
        if "seen" in split_name:
            summary = in_domain_summaries[ep]
            return (summary["suite"], int(summary["task_id"]))
        else:
            rows = ood_rows_by_ep[ep]
            return (rows[0]["suite"], int(rows[0]["task_id"]))

    all_obs_list = []
    all_act_list = []
    starts = []
    ends = []
    calibration = []
    test = []
    success = []
    failed = []
    id_labels = []
    ood_labels = []
    offset = 0
    rollout_idx = 0
    episode_keys = []

    for split in SPLITS:
        ep_ids = split_episodes[split]
        ep_ids = sorted(ep_ids, key=lambda ep: get_ep_task_key(ep, split))
        print(f"Merging split {split} ({len(ep_ids)} episodes)...", flush=True)

        for ep_id in ep_ids:
            cache_file = CACHE_DIR / f"{split}_{ep_id}.pkl"
            if not cache_file.exists():
                raise FileNotFoundError(f"Missing cache file {cache_file}")

            with open(cache_file, "rb") as f:
                cache_data = pickle.load(f)

            episode_obs = cache_data["obs"]
            episode_actions = cache_data["actions"]

            starts.append(offset)
            episode_keys.append(ep_id)

            obs_array = np.array(episode_obs, dtype=np.float32)
            act_array = np.array(episode_actions, dtype=np.float32)

            all_obs_list.append(obs_array)
            all_act_list.append(act_array)

            offset += len(episode_obs)
            ends.append(offset)

            is_success = "success" in split
            is_ood = "ood" in split
            success.append(is_success)
            failed.append(not is_success)
            id_labels.append(not is_ood)
            ood_labels.append(is_ood)
            calibration.append(split == "success_calib_seen")
            test.append(is_ood)
            rollout_idx += 1

    out_dir = DATA_ROOT / "libero_fold00" / "processed_rollouts"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Concatenating obs and action predictions...", flush=True)
    final_obs = np.concatenate(all_obs_list, axis=0)
    final_act = np.concatenate(all_act_list, axis=0)

    stacked_obs = torch.from_numpy(final_obs)
    stacked_actions = torch.from_numpy(final_act)

    metadata = {
        "episode_start_indices": np.asarray(starts, dtype=np.int64),
        "episode_end_indices": np.asarray(ends, dtype=np.int64),
        "calibration_rollout_labels": np.asarray(calibration, dtype=bool),
        "test_rollout_labels": np.asarray(test, dtype=bool),
        "successful_rollout_labels": np.asarray(success, dtype=bool),
        "failed_rollout_labels": np.asarray(failed, dtype=bool),
        "id_rollout_labels": np.asarray(id_labels, dtype=bool),
        "ood_rollout_labels": np.asarray(ood_labels, dtype=bool),
        "num_steps": int(offset),
        "num_rollouts": int(rollout_idx),
        "episode_lengths": np.asarray(ends, dtype=np.int64) - np.asarray(starts, dtype=np.int64),
        "num_robots": 1,
        "actions": {
            "action_dim": 7,
            "action_mapping": {"position": [0, 1, 2], "rotation": [3, 4, 5], "gripper": [6]},
        },
        "available_tensors": ["action_preds", "obs_embeddings"],
        "episode_keys": episode_keys,
    }

    torch.save(stacked_obs, out_dir / "obs_embeddings.pt")
    torch.save(stacked_actions, out_dir / "action_preds.pt")
    with (out_dir / "metadata.pkl").open("wb") as f:
        pickle.dump(metadata, f)

    print("\nDataset Merge Completed Successfully!", flush=True)
    print(f"Saved to {out_dir}", flush=True)
    print(f"Tensors shape: obs={stacked_obs.shape}, actions={stacked_actions.shape}", flush=True)
    print(f"Num rollouts: {metadata['num_rollouts']}, Num steps: {metadata['num_steps']}", flush=True)

if __name__ == "__main__":
    main()
