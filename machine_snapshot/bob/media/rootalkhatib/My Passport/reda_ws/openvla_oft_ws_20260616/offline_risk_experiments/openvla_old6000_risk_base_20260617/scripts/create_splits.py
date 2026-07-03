#!/usr/bin/env python3
import os
import json
import random
from collections import defaultdict

def main():
    summaries_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded/episode_summaries.jsonl"
    splits_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_risk_base_20260617/splits"
    os.makedirs(splits_dir, exist_ok=True)

    # Set seed for reproducibility
    random.seed(42)

    # Read all episodes
    episodes = []
    task_groups = defaultdict(list)

    with open(summaries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            ep = json.loads(line)
            episodes.append(ep)
            # Group by task_id and success
            task_groups[(ep["task_id"], ep["success"])].append(ep["episode_index_global"])

    train_ids = []
    val_ids = []
    test_ids = []

    for (task_id, success), ids in sorted(task_groups.items()):
        # Shuffle ids deterministically
        random.shuffle(ids)
        n = len(ids)
        n_train = int(n * 0.7)
        n_val = int(n * 0.15)
        
        train_ids.extend(ids[:n_train])
        val_ids.extend(ids[n_train:n_train+n_val])
        test_ids.extend(ids[n_train+n_val:])

    # Sort ids for convenience
    train_ids.sort()
    val_ids.sort()
    test_ids.sort()

    # Save splits
    with open(os.path.join(splits_dir, "train_episode_ids.json"), "w") as f:
        json.dump(train_ids, f)
    with open(os.path.join(splits_dir, "val_episode_ids.json"), "w") as f:
        json.dump(val_ids, f)
    with open(os.path.join(splits_dir, "test_episode_ids.json"), "w") as f:
        json.dump(test_ids, f)

    # Calculate statistics
    id_to_outcome = {ep["episode_index_global"]: (ep["task_id"], ep["success"]) for ep in episodes}
    
    def get_split_stats(ids):
        stats = defaultdict(lambda: {"success": 0, "failure": 0})
        for idx in ids:
            task_id, success = id_to_outcome[idx]
            if success:
                stats[task_id]["success"] += 1
            else:
                stats[task_id]["failure"] += 1
        return stats

    summary = {
        "train": {
            "total": len(train_ids),
            "failures": sum(1 for idx in train_ids if not id_to_outcome[idx][1]),
            "successes": sum(1 for idx in train_ids if id_to_outcome[idx][1]),
            "per_task": {str(k): v for k, v in sorted(get_split_stats(train_ids).items())}
        },
        "val": {
            "total": len(val_ids),
            "failures": sum(1 for idx in val_ids if not id_to_outcome[idx][1]),
            "successes": sum(1 for idx in val_ids if id_to_outcome[idx][1]),
            "per_task": {str(k): v for k, v in sorted(get_split_stats(val_ids).items())}
        },
        "test": {
            "total": len(test_ids),
            "failures": sum(1 for idx in test_ids if not id_to_outcome[idx][1]),
            "successes": sum(1 for idx in test_ids if id_to_outcome[idx][1]),
            "per_task": {str(k): v for k, v in sorted(get_split_stats(test_ids).items())}
        }
    }

    with open(os.path.join(splits_dir, "split_summary.json"), "w") as f:
        json.dump(summary, f, indent=4)

    print("Created split files successfully!")
    print(f"Train: {len(train_ids)} episodes ({summary['train']['failures']} failures)")
    print(f"Val: {len(val_ids)} episodes ({summary['val']['failures']} failures)")
    print(f"Test: {len(test_ids)} episodes ({summary['test']['failures']} failures)")

if __name__ == "__main__":
    main()
