#!/usr/bin/env python3
import json
import random
import numpy as np
from pathlib import Path
from collections import defaultdict

PATHS = {
    "sam_instance_A": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_A/fiper_receding_samples.jsonl",
    "sam_instance_B": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_B/fiper_receding_samples.jsonl",
    "bob_instance_A": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data/instance_A/fiper_receding_samples.jsonl",
    "bob_instance_B": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data/instance_B/fiper_receding_samples.jsonl"
}

def main():
    # Load all rows grouped by episode_id
    episodes = defaultdict(list)
    
    for name, path_str in PATHS.items():
        path = Path(path_str)
        if not path.exists():
            print(f"Skipping non-existent path: {path_str}")
            continue
        with path.open() as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                ep_id = row.get("episode_id")
                # prepend dataset name to ensure unique episode_ids across different instances
                unique_ep_id = f"{name}_{ep_id}"
                row["unique_episode_id"] = unique_ep_id
                episodes[unique_ep_id].append(row)

    print(f"Total episodes loaded: {len(episodes)}")

    # Sort episodes by suite and outcome
    success_suite_A = []  # libero_spatial_with_mug (from instance_A)
    success_suite_B = []  # libero_goal_with_mug (from instance_B)
    failure_episodes = []

    for ep_id, rows in episodes.items():
        # Sort rows by timestep to be absolutely sure
        rows.sort(key=lambda x: x["timestep"])
        outcome = rows[-1].get("episode_outcome")
        suite = rows[0].get("suite")

        if outcome == "success":
            if "instance_B" in ep_id:
                success_suite_B.append((ep_id, rows))
            else:
                success_suite_A.append((ep_id, rows))
        else:
            failure_episodes.append((ep_id, rows))

    print(f"Success libero_spatial_with_mug: {len(success_suite_A)}")
    print(f"Success libero_goal_with_mug: {len(success_suite_B)}")
    print(f"Failure episodes: {len(failure_episodes)}")

    # We will train the main RND safety monitor on libero_goal_with_mug (suite B)
    # and use libero_spatial_with_mug (suite A) as the OOD test suite.
    # Split success_suite_B into Train (60%), Calib (20%), Test (20%)
    random.seed(42)
    random.shuffle(success_suite_B)

    n_total = len(success_suite_B)
    n_train = int(n_total * 0.6)
    n_calib = int(n_total * 0.2)
    
    train_eps = success_suite_B[:n_train]
    calib_eps = success_suite_B[n_train:n_train+n_calib]
    test_eps = success_suite_B[n_train+n_calib:]

    print(f"Split libero_goal_with_mug success episodes:")
    print(f"  Train: {len(train_eps)}")
    print(f"  Calib: {len(calib_eps)}")
    print(f"  Test: {len(test_eps)}")

    # Directory for splits
    split_dir = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/splits")
    split_dir.mkdir(parents=True, exist_ok=True)

    def write_rows(filename, eps_list):
        out_path = split_dir / filename
        row_count = 0
        with out_path.open("w") as f:
            for ep_id, rows in eps_list:
                for row in rows:
                    f.write(json.dumps(row) + "\n")
                    row_count += 1
        print(f"Wrote {row_count} rows across {len(eps_list)} episodes to {out_path.name}")
        return row_count

    # Write splits
    row_counts = {}
    row_counts["success_train"] = write_rows("success_train.jsonl", train_eps)
    row_counts["success_calib"] = write_rows("success_calib.jsonl", calib_eps)
    row_counts["success_test"] = write_rows("success_test.jsonl", test_eps)
    row_counts["ood_suite_success_test"] = write_rows("ood_suite_success_test.jsonl", success_suite_A)
    
    # Write failure splits
    row_counts["failure_eval_all"] = write_rows("failure_eval_all.jsonl", failure_episodes)

    # early, late, and near_end failure splits
    early_rows = []
    late_rows = []
    near_end_rows = []

    for ep_id, rows in failure_episodes:
        L = len(rows)
        # early: first 25%
        early_cutoff = max(1, int(np.floor(0.25 * L)))
        early_rows.extend(rows[:early_cutoff])

        # late: last 25%
        late_cutoff = int(np.ceil(0.75 * L))
        # Ensure at least 1 step is in late
        if late_cutoff >= L:
            late_cutoff = max(0, L - 1)
        late_rows.extend(rows[late_cutoff:])

        # near_end: last 50 timesteps
        near_end_start = max(0, L - 50)
        near_end_rows.extend(rows[near_end_start:])

    def write_raw_rows(filename, rows_list):
        out_path = split_dir / filename
        with out_path.open("w") as f:
            for row in rows_list:
                f.write(json.dumps(row) + "\n")
        print(f"Wrote {len(rows_list)} rows to {out_path.name}")
        return len(rows_list)

    row_counts["failure_eval_early"] = write_raw_rows("failure_eval_early.jsonl", early_rows)
    row_counts["failure_eval_late"] = write_raw_rows("failure_eval_late.jsonl", late_rows)
    row_counts["failure_eval_near_end"] = write_raw_rows("failure_eval_near_end.jsonl", near_end_rows)

    # Audit Leakage
    train_ep_ids = set(ep_id for ep_id, _ in train_eps)
    calib_ep_ids = set(ep_id for ep_id, _ in calib_eps)
    test_ep_ids = set(ep_id for ep_id, _ in test_eps)
    ood_ep_ids = set(ep_id for ep_id, _ in success_suite_A)
    fail_ep_ids = set(ep_id for ep_id, _ in failure_episodes)

    leakage_detected = (
        len(train_ep_ids.intersection(calib_ep_ids)) > 0 or
        len(train_ep_ids.intersection(test_ep_ids)) > 0 or
        len(train_ep_ids.intersection(ood_ep_ids)) > 0 or
        len(train_ep_ids.intersection(fail_ep_ids)) > 0 or
        len(calib_ep_ids.intersection(test_ep_ids)) > 0 or
        len(calib_ep_ids.intersection(ood_ep_ids)) > 0 or
        len(calib_ep_ids.intersection(fail_ep_ids)) > 0 or
        len(test_ep_ids.intersection(ood_ep_ids)) > 0 or
        len(test_ep_ids.intersection(fail_ep_ids)) > 0 or
        len(ood_ep_ids.intersection(fail_ep_ids)) > 0
    )

    print(f"Leakage check: {'LEAKAGE DETECTED!' if leakage_detected else 'PASS'}")

    summary = {
        "success_train_episodes": len(train_eps),
        "success_train_rows": row_counts["success_train"],
        "success_calib_episodes": len(calib_eps),
        "success_calib_rows": row_counts["success_calib"],
        "success_test_episodes": len(test_eps),
        "success_test_rows": row_counts["success_test"],
        "ood_suite_success_test_episodes": len(success_suite_A),
        "ood_suite_success_test_rows": row_counts["ood_suite_success_test"],
        "failure_eval_all_episodes": len(failure_episodes),
        "failure_eval_all_rows": row_counts["failure_eval_all"],
        "failure_eval_early_rows": row_counts["failure_eval_early"],
        "failure_eval_late_rows": row_counts["failure_eval_late"],
        "failure_eval_near_end_rows": row_counts["failure_eval_near_end"],
        "leakage_audit_pass": not leakage_detected
    }

    # Write summary
    summary_path = split_dir / "split_summary.json"
    with summary_path.open("w") as f:
        json.dump(summary, f, indent=2)

    # Generate MD report
    report_dir = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    
    md_lines = [
        "# Split Construction & Leakage Audit Report",
        "",
        "This report summarizes the datasets splits generated for RND training, conformal threshold calibration, and challenge evaluations.",
        "",
        "## Dataset Splits Overview",
        "| Split File | Episodes | Rows | Purpose |",
        "|---|---|---|---|",
        f"| `success_train.jsonl` | {summary['success_train_episodes']} | {summary['success_train_rows']} | RND training |",
        f"| `success_calib.jsonl` | {summary['success_calib_episodes']} | {summary['success_calib_rows']} | Threshold calibration |",
        f"| `success_test.jsonl` | {summary['success_test_episodes']} | {summary['success_test_rows']} | False alarm testing |",
        f"| `ood_suite_success_test.jsonl` | {summary['ood_suite_success_test_episodes']} | {summary['ood_suite_success_test_rows']} | Held-out suite false alarm testing |",
        f"| `failure_eval_all.jsonl` | {summary['failure_eval_all_episodes']} | {summary['failure_eval_all_rows']} | Full failure evaluations |",
        f"| `failure_eval_early.jsonl` | N/A | {summary['failure_eval_early_rows']} | Early-episode failure evaluation (first 25%) |",
        f"| `failure_eval_late.jsonl` | N/A | {summary['failure_eval_late_rows']} | Late-episode failure evaluation (last 25%) |",
        f"| `failure_eval_near_end.jsonl` | N/A | {summary['failure_eval_near_end_rows']} | Near-end failure evaluation (last 50 steps) |",
        "",
        "## Leakage Audit Details",
        f"- **Episode-level partition check:** `{'FAILED' if leakage_detected else 'PASSED'}`",
        f"- **No overlap between train, calib, test, OOD, and failure episodes.**",
    ]

    with (report_dir / "split_summary.md").open("w") as f:
        f.write("\n".join(md_lines))

    print("Splitting complete.")

if __name__ == "__main__":
    main()
