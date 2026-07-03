#!/usr/bin/env python3
import os
import json
import numpy as np
from pathlib import Path
from collections import defaultdict

PATHS = {
    "sam_instance_A": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_A/fiper_receding_samples.jsonl",
    "sam_instance_B": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_B/fiper_receding_samples.jsonl",
    "bob_instance_A": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data/instance_A/fiper_receding_samples.jsonl",
    "bob_instance_B": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data/instance_B/fiper_receding_samples.jsonl"
}

REQUIRED_FIELDS = [
    "episode_id", "timestep", "suite", "task_id", "task_instruction",
    "main_seed", "main_candidate_action_chunk_normalized", "main_candidate_action_chunk_env",
    "executed_action", "ace_candidate_seeds", "ace_candidate_chunks_normalized",
    "ace_candidate_chunks_env", "episode_outcome", "allowed_use"
]

def analyze_jsonl(name, path_str):
    path = Path(path_str)
    if not path.exists():
        print(f"Path does not exist: {path_str}")
        return None

    print(f"Analyzing {name}: {path_str}")
    row_count = 0
    corrupt_rows = 0
    episodes = defaultdict(list)
    rows_per_suite_task = defaultdict(int)
    ace_counts = defaultdict(int)
    
    confirm_ace_replay_used_false = True
    confirm_64_ace_candidates = True
    confirm_first_action_executed = True
    missing_fields_set = set()
    all_main_seeds = set()
    all_ace_seeds = set()

    with path.open("r") as f:
        for line_idx, line in enumerate(f):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                row_count += 1
            except Exception as e:
                corrupt_rows += 1
                continue

            # check required fields
            for rf in REQUIRED_FIELDS:
                if rf not in row:
                    # special case: if ace_candidate_seeds exists, map it to the check
                    if rf == "ace_candidate_seeds_64" and "ace_candidate_seeds" in row:
                        continue
                    if rf == "ace_candidate_chunks_normalized_64" and "ace_candidate_chunks_normalized" in row:
                        continue
                    if rf == "ace_candidate_chunks_env_64" and "ace_candidate_chunks_env" in row:
                        continue
                    missing_fields_set.add(rf)

            ep_id = row.get("episode_id")
            if ep_id:
                episodes[ep_id].append(row)

            suite = row.get("suite")
            task_id = row.get("task_id")
            if suite is not None and task_id is not None:
                rows_per_suite_task[f"{suite}:task_{task_id}"] += 1

            # ace candidates count
            ace_seeds = row.get("ace_candidate_seeds") or []
            ace_counts[len(ace_seeds)] += 1
            if len(ace_seeds) != 64:
                confirm_64_ace_candidates = False

            # check ace_replay_used
            metadata = row.get("metadata") or {}
            if metadata.get("ace_replay_used") is not False:
                confirm_ace_replay_used_false = False

            # check executed action vs first action of main chunk env
            exec_act = row.get("executed_action")
            main_chunk_env = row.get("main_candidate_action_chunk_env")
            if exec_act and main_chunk_env and len(main_chunk_env) > 0:
                first_env_act = main_chunk_env[0]
                # compare with small tolerance
                if not np.allclose(exec_act, first_env_act, atol=1e-5):
                    confirm_first_action_executed = False

            main_seed = row.get("main_seed")
            if main_seed is not None:
                all_main_seeds.add(main_seed)

            for s in ace_seeds:
                all_ace_seeds.add(s)

    # Episode stats
    ep_lengths = []
    success_ep_count = 0
    failure_ep_count = 0
    success_row_count = 0
    failure_row_count = 0

    for ep_id, ep_rows in episodes.items():
        ep_lengths.append(len(ep_rows))
        # check last row outcome
        outcome = ep_rows[-1].get("episode_outcome")
        if outcome == "success":
            success_ep_count += 1
            success_row_count += len(ep_rows)
        else:
            failure_ep_count += 1
            failure_row_count += len(ep_rows)

    if len(ep_lengths) > 0:
        min_len = int(np.min(ep_lengths))
        mean_len = float(np.mean(ep_lengths))
        max_len = int(np.max(ep_lengths))
    else:
        min_len, mean_len, max_len = 0, 0.0, 0

    result = {
        "name": name,
        "path": path_str,
        "row_count": row_count,
        "corrupt_rows": corrupt_rows,
        "episode_count": len(episodes),
        "success_episodes": success_ep_count,
        "failure_episodes": failure_ep_count,
        "success_rows": success_row_count,
        "failure_rows": failure_row_count,
        "episode_length_min": min_len,
        "episode_length_mean": mean_len,
        "episode_length_max": max_len,
        "confirm_ace_replay_used_false": confirm_ace_replay_used_false,
        "confirm_64_ace_candidates": confirm_64_ace_candidates,
        "confirm_first_action_executed": confirm_first_action_executed,
        "missing_required_fields": list(missing_fields_set),
        "ace_candidates_count_distribution": dict(ace_counts),
        "rows_per_suite_task": dict(rows_per_suite_task),
        "unique_main_seeds": len(all_main_seeds),
        "unique_ace_seeds": len(all_ace_seeds),
    }
    return result

def main():
    results = {}
    for name, path in PATHS.items():
        res = analyze_jsonl(name, path)
        if res:
            results[name] = res

    # Write summary files
    out_dir = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/data")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    with (out_dir / "receding_dataset_inventory.json").open("w") as f:
        json.dump(results, f, indent=2)

    # Generate MD report
    report_dir = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/receding_full_test_20260522_100546/reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    md_lines = [
        "# Receding Dataset Inventory & Validation Report",
        "",
        "This report contains validation metrics for all Sam receding-horizon and consolidated Bob datasets.",
        ""
    ]

    for name, res in results.items():
        md_lines.extend([
            f"## Dataset: {name}",
            f"- **Path:** `{res['path']}`",
            f"- **Row Count:** {res['row_count']}",
            f"- **Episode Count:** {res['episode_count']}",
            f"- **Success Episodes / Rows:** {res['success_episodes']} / {res['success_rows']}",
            f"- **Failure/Timeout Episodes / Rows:** {res['failure_episodes']} / {res['failure_rows']}",
            f"- **Episode Lengths (Min/Mean/Max):** {res['episode_length_min']} / {res['episode_length_mean']:.1f} / {res['episode_length_max']}",
            f"- **Confirm `ace_replay_used == false`:** `{res['confirm_ace_replay_used_false']}`",
            f"- **Confirm 64 ACE Candidate Chunks:** `{res['confirm_64_ace_candidates']}`",
            f"- **Confirm First Action Executed:** `{res['confirm_first_action_executed']}`",
            f"- **Corrupt Rows:** {res['corrupt_rows']}",
            f"- **Unique Main Seeds:** {res['unique_main_seeds']}",
            f"- **Unique ACE Seeds:** {res['unique_ace_seeds']}",
            f"- **Missing Fields:** {res['missing_required_fields'] if res['missing_required_fields'] else 'None'}",
            "",
            "### Rows per Suite/Task",
            "| Suite:Task | Rows |",
            "|---|---|",
        ])
        for st, count in sorted(res['rows_per_suite_task'].items()):
            md_lines.append(f"| {st} | {count} |")
        md_lines.append("")

        md_lines.extend([
            "### ACE Candidate Count Distribution",
            "| Candidates | Rows |",
            "|---|---|",
        ])
        for c, count in sorted(res['ace_candidates_count_distribution'].items()):
            md_lines.append(f"| {c} | {count} |")
        md_lines.append("\n" + "="*40 + "\n")

    with (report_dir / "receding_dataset_inventory.md").open("w") as f:
        f.write("\n".join(md_lines))

    print("Inventory complete.")

if __name__ == "__main__":
    main()
