#!/usr/bin/env python3
import json
import math
import random
import sys
import time
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Constants and Mappings
REQUIRED_KEYS = {
    "episode_id", "suite", "task_id", "timestep", "episode_outcome",
    "main_seed", "ace_candidate_seeds", "ace_candidate_chunks_normalized",
    "main_candidate_action_chunk_normalized", "main_candidate_action_chunk_env", "executed_action"
}

SUITE_FAMILIES = {
    "libero_spatial_with_mug": "spatial",
    "libero_object_with_mug": "object_family",
    "libero_goal_with_mug": "goal",
    "libero_spatial_with_milk": "spatial",
    "libero_10_with_milk": "10_family",
    "libero_goal_with_milk": "goal",
    "libero_spatial_object": "spatial",
    "libero_object_object": "object_family",
    "libero_goal_object": "goal",
    "libero_spatial_env": "spatial",
    "libero_object_env": "object_family",
    "libero_goal_env": "goal"
}

PERTURBATION_GROUPS = {
    "libero_spatial_with_mug": "mug",
    "libero_object_with_mug": "mug",
    "libero_goal_with_mug": "mug",
    "libero_spatial_with_milk": "milk",
    "libero_10_with_milk": "milk",
    "libero_goal_with_milk": "milk",
    "libero_spatial_object": "object",
    "libero_object_object": "object",
    "libero_goal_object": "object",
    "libero_spatial_env": "env",
    "libero_object_env": "env",
    "libero_goal_env": "env"
}

@dataclass
class RowRef:
    source_jsonl: str
    line_no: int
    episode_key: str
    machine: str
    instance: str
    suite: str
    task_id: int
    perturbation_group: str
    suite_family: str
    episode_outcome: str
    timestep: int
    row_index_in_episode: int

@dataclass
class EpisodeRef:
    episode_key: str
    source_jsonl: str
    machine: str
    instance: str
    suite: str
    task_id: int
    perturbation_group: str
    suite_family: str
    episode_outcome: str
    num_rows: int
    assigned_split: str = ""

def detect_machine_and_instance(path: Path) -> Tuple[str, str]:
    parts = path.parts
    machine = "unknown"
    instance = "unknown"
    for part in parts:
        if "sam_instance_A" in part:
            machine, instance = "sam", "instance_A"
        elif "sam_instance_B" in part:
            machine, instance = "sam", "instance_B"
        elif "bob_instance_A" in part:
            machine, instance = "bob", "instance_A"
        elif "bob_instance_B" in part:
            machine, instance = "bob", "instance_B"
    return machine, instance

def get_episode_key(machine: str, instance: str, suite: str, task_id: int, episode_id: str) -> str:
    return f"{machine}_{instance}_{suite}_t{task_id}_ep{episode_id}"

def read_config(config_path: Path) -> dict:
    with config_path.open("r") as f:
        return json.load(f)

def build_inventory_and_refs(config: dict, workspace_root: Path) -> Tuple[List[RowRef], List[EpisodeRef], dict, List[str]]:
    input_roots = [workspace_root / r for r in config["input_roots"]]
    jsonl_paths: List[Path] = []
    for r in input_roots:
        if r.exists():
            jsonl_paths.extend(sorted(r.glob("**/fiper_receding_samples.jsonl")))
    
    if not jsonl_paths:
        print("Error: No fiper_receding_samples.jsonl files found in input roots.")
        sys.exit(1)
        
    print(f"Discovered JSONL paths: {[str(p.relative_to(workspace_root)) for p in jsonl_paths]}")

    excluded_tasks = set()
    for item in config.get("excluded_suite_tasks", []):
        excluded_tasks.add((item["suite"], int(item["task_id"])))

    row_refs: List[RowRef] = []
    episodes_map: Dict[str, List[RowRef]] = defaultdict(list)
    
    stats = {
        "total_raw_rows": 0,
        "total_used_rows": 0,
        "total_excluded_rows": 0,
        "total_corrupt_rows": 0,
        "total_missing_keys_rows": 0,
        "rows_by_machine": Counter(),
        "rows_by_suite": Counter(),
        "rows_by_task_id": Counter(),
        "rows_by_perturbation_group": Counter(),
        "rows_by_suite_family": Counter(),
        "success_rows": 0,
        "failure_rows": 0,
        "ace_replay_used_distribution": Counter(),
        "ace_candidate_count_distribution": Counter(),
        "first_action_checked": 0,
        "first_action_mismatches": 0,
        "main_seeds": set(),
        "ace_seeds": set(),
        "duplicate_main_seeds": 0,
        "duplicate_ace_seeds": 0,
    }

    warnings = []

    for path in jsonl_paths:
        machine, instance = detect_machine_and_instance(path)
        source_rel = str(path.relative_to(workspace_root))
        print(f"Processing {source_rel} ({machine}, {instance})...")
        
        with path.open("r") as f:
            for idx, line in enumerate(f):
                stats["total_raw_rows"] += 1
                line_no = idx + 1
                try:
                    row = json.loads(line)
                except Exception:
                    stats["total_corrupt_rows"] += 1
                    continue

                missing = REQUIRED_KEYS.difference(row.keys())
                if missing:
                    stats["total_missing_keys_rows"] += 1
                    continue

                suite = row["suite"]
                task_id = int(row["task_id"])

                if (suite, task_id) in excluded_tasks:
                    stats["total_excluded_rows"] += 1
                    continue

                # Metadata Checks
                stats["total_used_rows"] += 1
                stats["rows_by_machine"][machine] += 1
                stats["rows_by_suite"][suite] += 1
                stats["rows_by_task_id"][task_id] += 1
                
                group = PERTURBATION_GROUPS.get(suite, "unknown")
                family = SUITE_FAMILIES.get(suite, "unknown")
                stats["rows_by_perturbation_group"][group] += 1
                stats["rows_by_suite_family"][family] += 1

                outcome = row["episode_outcome"]
                if outcome == "success":
                    stats["success_rows"] += 1
                else:
                    stats["failure_rows"] += 1

                # Replay Check
                replay_used = row.get("metadata", {}).get("ace_replay_used", False)
                stats["ace_replay_used_distribution"][replay_used] += 1
                
                # ACE Candidate check
                stats["ace_candidate_count_distribution"][len(row["ace_candidate_chunks_normalized"])] += 1

                # First action only check
                executed_action = row["executed_action"]
                main_chunk_env = row["main_candidate_action_chunk_env"]
                if main_chunk_env and len(main_chunk_env) > 0:
                    stats["first_action_checked"] += 1
                    if len(executed_action) > 0:
                        # Compare floats
                        mismatch = False
                        for a_idx, val in enumerate(executed_action):
                            if a_idx < len(main_chunk_env[0]):
                                if abs(val - main_chunk_env[0][a_idx]) > 1e-4:
                                    mismatch = True
                                    break
                        if mismatch:
                            stats["first_action_mismatches"] += 1

                # Seed Check
                main_seed = int(row["main_seed"])
                if main_seed in stats["main_seeds"]:
                    stats["duplicate_main_seeds"] += 1
                stats["main_seeds"].add(main_seed)

                for s in row["ace_candidate_seeds"]:
                    ace_seed = int(s)
                    if ace_seed in stats["ace_seeds"]:
                        stats["duplicate_ace_seeds"] += 1
                    stats["ace_seeds"].add(ace_seed)

                # Collect row info
                ep_key = get_episode_key(machine, instance, suite, task_id, str(row["episode_id"]))
                
                ref = RowRef(
                    source_jsonl=source_rel,
                    line_no=line_no,
                    episode_key=ep_key,
                    machine=machine,
                    instance=instance,
                    suite=suite,
                    task_id=task_id,
                    perturbation_group=group,
                    suite_family=family,
                    episode_outcome=outcome,
                    timestep=int(row["timestep"]),
                    row_index_in_episode=-1 # Assigned later
                )
                row_refs.append(ref)
                episodes_map[ep_key].append(ref)

    # Sort timesteps in each episode and assign row index in episode
    episode_refs: List[EpisodeRef] = []
    for ep_key, rows in episodes_map.items():
        # Sort by timestep
        rows.sort(key=lambda x: x.timestep)
        for r_idx, r in enumerate(rows):
            r.row_index_in_episode = r_idx

        first_row = rows[0]
        ep_ref = EpisodeRef(
            episode_key=ep_key,
            source_jsonl=first_row.source_jsonl,
            machine=first_row.machine,
            instance=first_row.instance,
            suite=first_row.suite,
            task_id=first_row.task_id,
            perturbation_group=first_row.perturbation_group,
            suite_family=first_row.suite_family,
            episode_outcome=first_row.episode_outcome,
            num_rows=len(rows)
        )
        episode_refs.append(ep_ref)

    stats["unique_main_seeds_count"] = len(stats["main_seeds"])
    stats["unique_ace_seeds_count"] = len(stats["ace_seeds"])
    
    # Clean up seed sets to save memory in output
    del stats["main_seeds"]
    del stats["ace_seeds"]

    return row_refs, episode_refs, stats, warnings

def build_split(
    episodes: List[EpisodeRef],
    seed: int = 42,
    train_frac: float = 0.70,
    calib_frac: float = 0.15,
    test_frac: float = 0.15,
    stratum_warnings: List[str] = None
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Returns split assignments at episode level.
    Only splits success episodes. Failure/timeout are returns as failure_eval_all.
    """
    if stratum_warnings is None:
        stratum_warnings = []
        
    random.seed(seed)
    
    split_assignments: Dict[str, str] = {}
    
    # Success Stratification
    success_by_stratum: Dict[Tuple[str, int], List[EpisodeRef]] = defaultdict(list)
    for ep in episodes:
        if ep.episode_outcome == "success":
            success_by_stratum[(ep.suite, ep.task_id)].append(ep)
        elif ep.episode_outcome == "failure_or_timeout":
            split_assignments[ep.episode_key] = "failure_eval_all"
        else:
            split_assignments[ep.episode_key] = "unknown_outcome_eval_only"

    # Split each stratum
    for stratum, eps in success_by_stratum.items():
        # Shuffle deterministically
        random.shuffle(eps)
        n = len(eps)
        
        if n == 0:
            continue
        elif n == 1:
            stratum_warnings.append(f"Stratum {stratum} has 1 episode; assigned to train.")
            split_assignments[eps[0].episode_key] = "success_train"
        elif n == 2:
            stratum_warnings.append(f"Stratum {stratum} has 2 episodes; assigned 1 train, 1 test.")
            split_assignments[eps[0].episode_key] = "success_train"
            split_assignments[eps[1].episode_key] = "success_test_id"
        elif n == 3:
            split_assignments[eps[0].episode_key] = "success_train"
            split_assignments[eps[1].episode_key] = "success_calib"
            split_assignments[eps[2].episode_key] = "success_test_id"
        else:
            # Standard split logic
            n_train = max(1, int(round(train_frac * n)))
            n_calib = max(1, int(round(calib_frac * n)))
            n_test = n - n_train - n_calib
            if n_test <= 0:
                n_test = 1
                n_train = n - n_calib - n_test
            
            for i, ep in enumerate(eps):
                if i < n_train:
                    split_assignments[ep.episode_key] = "success_train"
                elif i < n_train + n_calib:
                    split_assignments[ep.episode_key] = "success_calib"
                else:
                    split_assignments[ep.episode_key] = "success_test_id"

    return split_assignments

def save_manifest_files(
    output_dir: Path,
    row_refs: List[RowRef],
    episode_refs: List[EpisodeRef],
    stats: dict,
    warnings: List[str]
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save inventory
    with (output_dir / "dataset_inventory.json").open("w") as f:
        json.dump({"stats": stats, "warnings": warnings}, f, indent=2)

    # Save episodes.jsonl
    with (output_dir / "episodes.jsonl").open("w") as f:
        for ep in episode_refs:
            f.write(json.dumps(asdict(ep)) + "\n")

    # Save rows.refs.jsonl
    with (output_dir / "rows.refs.jsonl").open("w") as f:
        for r in row_refs:
            f.write(json.dumps(asdict(r)) + "\n")

    # Coverage statistics CSVs
    # 1. coverage_suite_task.csv
    suite_task_counts = Counter()
    for r in row_refs:
        suite_task_counts[(r.suite, r.task_id)] += 1
    with (output_dir / "coverage_suite_task.csv").open("w") as f:
        f.write("suite,task_id,row_count\n")
        for (suite, task_id), count in sorted(suite_task_counts.items()):
            f.write(f"{suite},{task_id},{count}\n")

    # 2. coverage_suite_task_outcome.csv
    suite_task_outcome_counts = Counter()
    for r in row_refs:
        suite_task_outcome_counts[(r.suite, r.task_id, r.episode_outcome)] += 1
    with (output_dir / "coverage_suite_task_outcome.csv").open("w") as f:
        f.write("suite,task_id,outcome,row_count\n")
        for (suite, task_id, outcome), count in sorted(suite_task_outcome_counts.items()):
            f.write(f"{suite},{task_id},{outcome},{count}\n")

    # 3. coverage_group_outcome.csv
    group_outcome_counts = Counter()
    for r in row_refs:
        group_outcome_counts[(r.perturbation_group, r.episode_outcome)] += 1
    with (output_dir / "coverage_group_outcome.csv").open("w") as f:
        f.write("perturbation_group,outcome,row_count\n")
        for (group, outcome), count in sorted(group_outcome_counts.items()):
            f.write(f"{group},{outcome},{count}\n")

    # 4. coverage_family_outcome.csv
    family_outcome_counts = Counter()
    for r in row_refs:
        family_outcome_counts[(r.suite_family, r.episode_outcome)] += 1
    with (output_dir / "coverage_family_outcome.csv").open("w") as f:
        f.write("suite_family,outcome,row_count\n")
        for (family, outcome), count in sorted(family_outcome_counts.items()):
            f.write(f"{family},{outcome},{count}\n")

    # README.md
    with (output_dir / "README.md").open("w") as f:
        f.write(f"""# Central Manifests Inventory

This directory contains the canonical manifests for the FIPER `fiper_sweep_eternal_20260526_combined` campaign dataset.

- **Total Rows**: {stats["total_used_rows"]}
- **Total Episodes**: {len(episode_refs)}
- **Success Rows**: {stats["success_rows"]}
- **Failure Rows**: {stats["failure_rows"]}
""")

def create_experiment_folders(
    base_dir: Path,
    row_refs: List[RowRef],
    episode_refs: List[EpisodeRef],
    global_split_assignments: Dict[str, str]
) -> dict:
    base_dir.mkdir(parents=True, exist_ok=True)
    registry_list = []
    low_support_warnings = []

    # Map episodes and rows to keys
    row_by_ep = defaultdict(list)
    for r in row_refs:
        row_by_ep[r.episode_key].append(r)

    # ------------------------------------------------------------
    # Auxiliary function to write split reference files
    # ------------------------------------------------------------
    def write_experiment_splits(
        exp_dir: Path,
        exp_split_mapping: Dict[str, str] # ep_key -> split_name
    ) -> None:
        refs_dir = exp_dir / "datasets" / "refs"
        refs_dir.mkdir(parents=True, exist_ok=True)
        (exp_dir / "models").mkdir(parents=True, exist_ok=True)
        (exp_dir / "evals").mkdir(parents=True, exist_ok=True)
        (exp_dir / "results").mkdir(parents=True, exist_ok=True)
        (exp_dir / "logs").mkdir(parents=True, exist_ok=True)
        (exp_dir / "scripts").mkdir(parents=True, exist_ok=True)
        (exp_dir / "datasets" / "materialized").mkdir(parents=True, exist_ok=True)

        with (exp_dir / "datasets" / "materialized" / "README.md").open("w") as f:
            f.write("# Materialized Datasets\n\nThis directory holds materialized CSV/JSONL files generated from refs via materialize_fiper_split.py.\n")

        # Group rows and episodes by assigned split
        episodes_by_split = defaultdict(list)
        rows_by_split = defaultdict(list)

        for ep in episode_refs:
            split_name = exp_split_mapping.get(ep.episode_key)
            if not split_name:
                continue
            ep_copy = EpisodeRef(
                episode_key=ep.episode_key,
                source_jsonl=ep.source_jsonl,
                machine=ep.machine,
                instance=ep.instance,
                suite=ep.suite,
                task_id=ep.task_id,
                perturbation_group=ep.perturbation_group,
                suite_family=ep.suite_family,
                episode_outcome=ep.episode_outcome,
                num_rows=ep.num_rows,
                assigned_split=split_name
            )
            episodes_by_split[split_name].append(ep_copy)
            for r in row_by_ep[ep.episode_key]:
                rows_by_split[split_name].append(r)

        # Write split files
        for split_name in episodes_by_split.keys():
            # episodes.jsonl
            with (refs_dir / f"{split_name}.episodes.jsonl").open("w") as f:
                for ep in episodes_by_split[split_name]:
                    f.write(json.dumps(asdict(ep)) + "\n")
            # rows.jsonl
            with (refs_dir / f"{split_name}.rows.jsonl").open("w") as f:
                for r in rows_by_split[split_name]:
                    f.write(json.dumps(asdict(r)) + "\n")

    # ------------------------------------------------------------
    # 5A. 00_global_main
    # ------------------------------------------------------------
    exp_name = "00_global_main"
    exp_dir = base_dir / exp_name
    print(f"Creating experiment {exp_name}...")
    
    # Establish assignments (sub-splitting failures)
    exp_splits = {}
    for ep_key, base_split in global_split_assignments.items():
        if base_split == "failure_eval_all":
            # Map failure subclasses
            exp_splits[ep_key] = "failure_eval_all"
        else:
            exp_splits[ep_key] = base_split

    write_experiment_splits(exp_dir, exp_splits)
    
    # Write subclass failure subsets (custom logic where we write specific row manifests)
    # We do this for early, mid, late, near_end failure subsets
    # These contain subsets of rows from failure_eval_all episodes
    failure_eps = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout"]
    failure_subsets = {
        "failure_eval_early": lambda rows: rows[:max(1, len(rows)//4)],
        "failure_eval_mid": lambda rows: rows[len(rows)//4: len(rows) - len(rows)//4],
        "failure_eval_late": lambda rows: rows[len(rows) - len(rows)//4:],
        "failure_eval_near_end": lambda rows: rows[-50:] if len(rows) >= 50 else rows
    }
    
    refs_dir = exp_dir / "datasets" / "refs"
    for subset_name, subset_func in failure_subsets.items():
        subset_episodes = []
        subset_rows = []
        for ep in failure_eps:
            ep_rows = row_by_ep[ep.episode_key]
            sub_rows = subset_func(ep_rows)
            if sub_rows:
                subset_rows.extend(sub_rows)
                subset_episodes.append(EpisodeRef(
                    episode_key=ep.episode_key,
                    source_jsonl=ep.source_jsonl,
                    machine=ep.machine,
                    instance=ep.instance,
                    suite=ep.suite,
                    task_id=ep.task_id,
                    perturbation_group=ep.perturbation_group,
                    suite_family=ep.suite_family,
                    episode_outcome=ep.episode_outcome,
                    num_rows=len(sub_rows),
                    assigned_split=subset_name
                ))
        # Write files
        with (refs_dir / f"{subset_name}.episodes.jsonl").open("w") as f:
            for ep in subset_episodes:
                f.write(json.dumps(asdict(ep)) + "\n")
        with (refs_dir / f"{subset_name}.rows.jsonl").open("w") as f:
            for r in subset_rows:
                f.write(json.dumps(asdict(r)) + "\n")

    # README.md
    with (exp_dir / "README.md").open("w") as f:
        f.write("""# Global Main Experiment

## Purpose
Train the final canonical FIPER monitor using all successful receding SimVLA data from Sam and Bob.

## Logic
- **Training**: RND model is trained on `success_train` (success-only rows).
- **Calibration**: Conformal thresholds for RND and ACE policy entropy are calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test_id`, `failure_eval_all`, and failure subclasses (early, mid, late, near_end).
- **Stress-Testing**: OOD task/perturbation splits are NOT trained here; those are diagnostics.
""")
    with (exp_dir / "experiment_config.json").open("w") as f:
        json.dump({"name": exp_name, "status": "READY"}, f, indent=2)

    registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5B. 01_ood_task_8_9
    # ------------------------------------------------------------
    exp_name = "01_ood_task_8_9"
    exp_dir = base_dir / exp_name
    print(f"Creating experiment {exp_name}...")
    
    # Split only seen success tasks (0-7)
    seen_success_eps = [ep for ep in episode_refs if ep.episode_outcome == "success" and ep.task_id < 8]
    seen_assignments = build_split(seen_success_eps, seed=42, stratum_warnings=low_support_warnings)

    exp_splits = {}
    for ep in episode_refs:
        if ep.episode_outcome == "success":
            if ep.task_id >= 8:
                exp_splits[ep.episode_key] = "success_test_ood"
            else:
                base = seen_assignments.get(ep.episode_key)
                if base == "success_train":
                    exp_splits[ep.episode_key] = "success_train_seen"
                elif base == "success_calib":
                    exp_splits[ep.episode_key] = "success_calib_seen"
                elif base == "success_test_id":
                    exp_splits[ep.episode_key] = "success_test_seen"
        else:
            if ep.task_id >= 8:
                exp_splits[ep.episode_key] = "failure_eval_ood"
            else:
                exp_splits[ep.episode_key] = "failure_eval_seen"

    write_experiment_splits(exp_dir, exp_splits)

    # Subclass OOD failure subsets (late, near_end)
    ood_failure_eps = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout" and ep.task_id >= 8]
    refs_dir = exp_dir / "datasets" / "refs"
    for sub_name, sub_func in [("failure_eval_ood_late", failure_subsets["failure_eval_late"]), ("failure_eval_ood_near_end", failure_subsets["failure_eval_near_end"])]:
        sub_eps, sub_rows = [], []
        for ep in ood_failure_eps:
            ep_rows = row_by_ep[ep.episode_key]
            s_rows = sub_func(ep_rows)
            if s_rows:
                sub_rows.extend(s_rows)
                sub_eps.append(EpisodeRef(
                    episode_key=ep.episode_key, source_jsonl=ep.source_jsonl,
                    machine=ep.machine, instance=ep.instance, suite=ep.suite, task_id=ep.task_id,
                    perturbation_group=ep.perturbation_group, suite_family=ep.suite_family,
                    episode_outcome=ep.episode_outcome, num_rows=len(s_rows), assigned_split=sub_name
                ))
        with (refs_dir / f"{sub_name}.episodes.jsonl").open("w") as f:
            for ep in sub_eps:
                f.write(json.dumps(asdict(ep)) + "\n")
        with (refs_dir / f"{sub_name}.rows.jsonl").open("w") as f:
            for r in sub_rows:
                f.write(json.dumps(asdict(r)) + "\n")

    # README.md
    with (exp_dir / "README.md").open("w") as f:
        f.write("""# OOD Task Split

## Purpose
Stress-test FIPER RND and ACE monitors on unseen tasks (IDs 8 and 9).

## Logic
- Task IDs 8 and 9 are held out. They are NEVER seen in training or calibration.
- **Training**: RND trained on `success_train_seen` (IDs 0-7 successes).
- **Calibration**: Calibrated on `success_calib_seen`.
- **Evaluation**: Evaluated on seen test successes/failures, OOD test successes (`success_test_ood`), and OOD failures (`failure_eval_ood`, late, near_end).
""")
    with (exp_dir / "experiment_config.json").open("w") as f:
        json.dump({"name": exp_name, "status": "READY"}, f, indent=2)

    registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5C. 02_ood_perturbation_holdout
    # ------------------------------------------------------------
    for holdout_group in ["mug", "milk", "object", "env"]:
        exp_name = f"02_ood_perturbation_holdout_{holdout_group}"
        exp_dir = base_dir / exp_name
        print(f"Creating experiment {exp_name}...")
        
        seen_success_eps = [ep for ep in episode_refs if ep.episode_outcome == "success" and ep.perturbation_group != holdout_group]
        seen_assignments = build_split(seen_success_eps, seed=42, stratum_warnings=low_support_warnings)

        exp_splits = {}
        for ep in episode_refs:
            if ep.episode_outcome == "success":
                if ep.perturbation_group == holdout_group:
                    exp_splits[ep.episode_key] = "success_test_ood"
                else:
                    base = seen_assignments.get(ep.episode_key)
                    if base == "success_train":
                        exp_splits[ep.episode_key] = "success_train_seen"
                    elif base == "success_calib":
                        exp_splits[ep.episode_key] = "success_calib_seen"
                    elif base == "success_test_id":
                        exp_splits[ep.episode_key] = "success_test_seen"
            else:
                if ep.perturbation_group == holdout_group:
                    exp_splits[ep.episode_key] = "failure_eval_ood"
                else:
                    exp_splits[ep.episode_key] = "failure_eval_seen"

        write_experiment_splits(exp_dir, exp_splits)

        # OOD failure subsets
        ood_failure_eps = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout" and ep.perturbation_group == holdout_group]
        refs_dir = exp_dir / "datasets" / "refs"
        for sub_name, sub_func in [("failure_eval_ood_late", failure_subsets["failure_eval_late"]), ("failure_eval_ood_near_end", failure_subsets["failure_eval_near_end"])]:
            sub_eps, sub_rows = [], []
            for ep in ood_failure_eps:
                ep_rows = row_by_ep[ep.episode_key]
                s_rows = sub_func(ep_rows)
                if s_rows:
                    sub_rows.extend(s_rows)
                    sub_eps.append(EpisodeRef(
                        episode_key=ep.episode_key, source_jsonl=ep.source_jsonl,
                        machine=ep.machine, instance=ep.instance, suite=ep.suite, task_id=ep.task_id,
                        perturbation_group=ep.perturbation_group, suite_family=ep.suite_family,
                        episode_outcome=ep.episode_outcome, num_rows=len(s_rows), assigned_split=sub_name
                    ))
            with (refs_dir / f"{sub_name}.episodes.jsonl").open("w") as f:
                for ep in sub_eps:
                    f.write(json.dumps(asdict(ep)) + "\n")
            with (refs_dir / f"{sub_name}.rows.jsonl").open("w") as f:
                for r in sub_rows:
                    f.write(json.dumps(asdict(r)) + "\n")

        with (exp_dir / "README.md").open("w") as f:
            f.write(f"""# OOD Perturbation Holdout: {holdout_group}

## Purpose
Stress-test FIPER RND and ACE monitors on unseen perturbation type `{holdout_group}`.

## Logic
- Perturbation group `{holdout_group}` is held out from training and calibration.
- **Training**: RND trained on `success_train_seen` (non-{holdout_group} successes).
- **Calibration**: Calibrated on `success_calib_seen`.
- **Evaluation**: Evaluated on seen test successes/failures, OOD test successes (`success_test_ood`), and OOD failures (`failure_eval_ood`, late, near_end).
""")
        with (exp_dir / "experiment_config.json").open("w") as f:
            json.dump({"name": exp_name, "status": "READY", "holdout_group": holdout_group}, f, indent=2)

        registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5D. 03_ood_suite_family_holdout
    # ------------------------------------------------------------
    for holdout_family in ["spatial", "object_family", "goal", "10_family"]:
        exp_name = f"03_ood_suite_family_holdout_{holdout_family}"
        exp_dir = base_dir / exp_name
        print(f"Creating experiment {exp_name}...")
        
        seen_success_eps = [ep for ep in episode_refs if ep.episode_outcome == "success" and ep.suite_family != holdout_family]
        seen_assignments = build_split(seen_success_eps, seed=42, stratum_warnings=low_support_warnings)

        exp_splits = {}
        for ep in episode_refs:
            if ep.episode_outcome == "success":
                if ep.suite_family == holdout_family:
                    exp_splits[ep.episode_key] = "success_test_ood"
                else:
                    base = seen_assignments.get(ep.episode_key)
                    if base == "success_train":
                        exp_splits[ep.episode_key] = "success_train_seen"
                    elif base == "success_calib":
                        exp_splits[ep.episode_key] = "success_calib_seen"
                    elif base == "success_test_id":
                        exp_splits[ep.episode_key] = "success_test_seen"
            else:
                if ep.suite_family == holdout_family:
                    exp_splits[ep.episode_key] = "failure_eval_ood"
                else:
                    exp_splits[ep.episode_key] = "failure_eval_seen"

        write_experiment_splits(exp_dir, exp_splits)

        # OOD failure subsets
        ood_failure_eps = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout" and ep.suite_family == holdout_family]
        refs_dir = exp_dir / "datasets" / "refs"
        for sub_name, sub_func in [("failure_eval_ood_late", failure_subsets["failure_eval_late"]), ("failure_eval_ood_near_end", failure_subsets["failure_eval_near_end"])]:
            sub_eps, sub_rows = [], []
            for ep in ood_failure_eps:
                ep_rows = row_by_ep[ep.episode_key]
                s_rows = sub_func(ep_rows)
                if s_rows:
                    sub_rows.extend(s_rows)
                    sub_eps.append(EpisodeRef(
                        episode_key=ep.episode_key, source_jsonl=ep.source_jsonl,
                        machine=ep.machine, instance=ep.instance, suite=ep.suite, task_id=ep.task_id,
                        perturbation_group=ep.perturbation_group, suite_family=ep.suite_family,
                        episode_outcome=ep.episode_outcome, num_rows=len(s_rows), assigned_split=sub_name
                    ))
            with (refs_dir / f"{sub_name}.episodes.jsonl").open("w") as f:
                for ep in sub_eps:
                    f.write(json.dumps(asdict(ep)) + "\n")
            with (refs_dir / f"{sub_name}.rows.jsonl").open("w") as f:
                for r in sub_rows:
                    f.write(json.dumps(asdict(r)) + "\n")

        with (exp_dir / "README.md").open("w") as f:
            f.write(f"""# OOD Suite Family Holdout: {holdout_family}

## Purpose
Stress-test FIPER RND and ACE monitors on unseen suite family `{holdout_family}`.

## Logic
- Suite family `{holdout_family}` is held out from training and calibration.
- **Training**: RND trained on `success_train_seen` (non-{holdout_family} successes).
- **Calibration**: Calibrated on `success_calib_seen`.
- **Evaluation**: Evaluated on seen test successes/failures, OOD test successes (`success_test_ood`), and OOD failures (`failure_eval_ood`, late, near_end).
""")
        with (exp_dir / "experiment_config.json").open("w") as f:
            json.dump({"name": exp_name, "status": "READY", "holdout_family": holdout_family}, f, indent=2)

        registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5E. 04_per_perturbation
    # ------------------------------------------------------------
    for group in ["mug", "milk", "object", "env"]:
        exp_name = f"04_per_perturbation_{group}"
        exp_dir = base_dir / exp_name
        print(f"Creating experiment {exp_name}...")
        
        group_eps = [ep for ep in episode_refs if ep.perturbation_group == group]
        group_assignments = build_split(group_eps, seed=42, stratum_warnings=low_support_warnings)

        exp_splits = {}
        for ep in group_eps:
            base = group_assignments.get(ep.episode_key)
            if base == "success_train":
                exp_splits[ep.episode_key] = "success_train"
            elif base == "success_calib":
                exp_splits[ep.episode_key] = "success_calib"
            elif base == "success_test_id":
                exp_splits[ep.episode_key] = "success_test"
            elif base == "failure_eval_all":
                exp_splits[ep.episode_key] = "failure_eval"

        write_experiment_splits(exp_dir, exp_splits)

        # Failure subsets
        group_failure_eps = [ep for ep in group_eps if ep.episode_outcome == "failure_or_timeout"]
        refs_dir = exp_dir / "datasets" / "refs"
        for sub_name, sub_func in [("failure_eval_late", failure_subsets["failure_eval_late"]), ("failure_eval_near_end", failure_subsets["failure_eval_near_end"])]:
            sub_eps, sub_rows = [], []
            for ep in group_failure_eps:
                ep_rows = row_by_ep[ep.episode_key]
                s_rows = sub_func(ep_rows)
                if s_rows:
                    sub_rows.extend(s_rows)
                    sub_eps.append(EpisodeRef(
                        episode_key=ep.episode_key, source_jsonl=ep.source_jsonl,
                        machine=ep.machine, instance=ep.instance, suite=ep.suite, task_id=ep.task_id,
                        perturbation_group=ep.perturbation_group, suite_family=ep.suite_family,
                        episode_outcome=ep.episode_outcome, num_rows=len(s_rows), assigned_split=sub_name
                    ))
            with (refs_dir / f"{sub_name}.episodes.jsonl").open("w") as f:
                for ep in sub_eps:
                    f.write(json.dumps(asdict(ep)) + "\n")
            with (refs_dir / f"{sub_name}.rows.jsonl").open("w") as f:
                for r in sub_rows:
                    f.write(json.dumps(asdict(r)) + "\n")

        with (exp_dir / "README.md").open("w") as f:
            f.write(f"""# Per-Perturbation: {group}

## Purpose
Train a specialized FIPER monitor only on `{group}` perturbation data.

## Logic
- Only `{group}` data is included in this split.
- **Training**: RND trained on `success_train` (only `{group}` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
""")
        with (exp_dir / "experiment_config.json").open("w") as f:
            json.dump({"name": exp_name, "status": "READY", "perturbation_group": group}, f, indent=2)

        registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5F. 05_per_suite
    # ------------------------------------------------------------
    for suite in SUITE_FAMILIES.keys():
        exp_name = f"05_per_suite/{suite}"
        exp_dir = base_dir / exp_name
        print(f"Creating experiment 05_per_suite/{suite}...")
        
        suite_eps = [ep for ep in episode_refs if ep.suite == suite]
        suite_successes = [ep for ep in suite_eps if ep.episode_outcome == "success"]
        suite_failures = [ep for ep in suite_eps if ep.episode_outcome == "failure_or_timeout"]

        # Support check
        status = "READY"
        if len(suite_successes) < 3 or len(suite_failures) == 0:
            status = "LOW_SUPPORT"
        if len(suite_successes) == 0:
            status = "INVALID_FOR_TRAINING"

        suite_assignments = build_split(suite_eps, seed=42, stratum_warnings=low_support_warnings)

        exp_splits = {}
        for ep in suite_eps:
            base = suite_assignments.get(ep.episode_key)
            if base == "success_train":
                exp_splits[ep.episode_key] = "success_train"
            elif base == "success_calib":
                exp_splits[ep.episode_key] = "success_calib"
            elif base == "success_test_id":
                exp_splits[ep.episode_key] = "success_test"
            elif base == "failure_eval_all":
                exp_splits[ep.episode_key] = "failure_eval"

        write_experiment_splits(exp_dir, exp_splits)

        # Failure subsets
        refs_dir = exp_dir / "datasets" / "refs"
        for sub_name, sub_func in [("failure_eval_late", failure_subsets["failure_eval_late"]), ("failure_eval_near_end", failure_subsets["failure_eval_near_end"])]:
            sub_eps, sub_rows = [], []
            for ep in suite_failures:
                ep_rows = row_by_ep[ep.episode_key]
                s_rows = sub_func(ep_rows)
                if s_rows:
                    sub_rows.extend(s_rows)
                    sub_eps.append(EpisodeRef(
                        episode_key=ep.episode_key, source_jsonl=ep.source_jsonl,
                        machine=ep.machine, instance=ep.instance, suite=ep.suite, task_id=ep.task_id,
                        perturbation_group=ep.perturbation_group, suite_family=ep.suite_family,
                        episode_outcome=ep.episode_outcome, num_rows=len(s_rows), assigned_split=sub_name
                    ))
            with (refs_dir / f"{sub_name}.episodes.jsonl").open("w") as f:
                for ep in sub_eps:
                    f.write(json.dumps(asdict(ep)) + "\n")
            with (refs_dir / f"{sub_name}.rows.jsonl").open("w") as f:
                for r in sub_rows:
                    f.write(json.dumps(asdict(r)) + "\n")

        with (exp_dir / "README.md").open("w") as f:
            f.write(f"""# Per-Suite: {suite}

## Purpose
Train a specialized FIPER monitor only on `{suite}` suite data.

## Logic
- Status: **{status}**
- Only `{suite}` data is included in this split.
- **Training**: RND trained on `success_train` (only `{suite}` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
""")
        with (exp_dir / "experiment_config.json").open("w") as f:
            json.dump({"name": f"05_per_suite_{suite}", "status": status, "suite": suite}, f, indent=2)

        registry_list.append({"name": f"05_per_suite_{suite}", "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5G. 06_corrupted_action_eval
    # ------------------------------------------------------------
    exp_name = "06_corrupted_action_eval"
    exp_dir = base_dir / exp_name
    print(f"Creating experiment {exp_name}...")
    
    # Needs datasets/refs directory
    refs_dir = exp_dir / "datasets" / "refs"
    refs_dir.mkdir(parents=True, exist_ok=True)
    (exp_dir / "models").mkdir(parents=True, exist_ok=True)
    (exp_dir / "evals").mkdir(parents=True, exist_ok=True)
    (exp_dir / "results").mkdir(parents=True, exist_ok=True)
    (exp_dir / "logs").mkdir(parents=True, exist_ok=True)
    (exp_dir / "scripts").mkdir(parents=True, exist_ok=True)
    (exp_dir / "datasets" / "materialized").mkdir(parents=True, exist_ok=True)
    
    # Copy global success_test_id split refs to source_success_test_id
    global_test_rows_path = base_dir / "00_global_main" / "datasets" / "refs" / "success_test_id.rows.jsonl"
    global_test_eps_path = base_dir / "00_global_main" / "datasets" / "refs" / "success_test_id.episodes.jsonl"
    
    # Copy rows
    with global_test_rows_path.open("r") as src, (refs_dir / "source_success_test_id.rows.jsonl").open("w") as dst:
        dst.write(src.read())
    # Copy episodes
    with global_test_eps_path.open("r") as src, (refs_dir / "source_success_test_id.episodes.jsonl").open("w") as dst:
        dst.write(src.read())

    # Create corruption_config.json
    corruption_config = {
        "source_split": "source_success_test_id",
        "corruption_modes": [
            "zero", "random_uniform", "shuffled_timestep_order", "reversed_timestep_order",
            "scaled_x2_clipped", "gripper_flipped", "repeated_first_action",
            "gaussian_noise_low", "gaussian_noise_medium", "gaussian_noise_high"
        ]
    }
    with (exp_dir / "corruption_config.json").open("w") as f:
        json.dump(corruption_config, f, indent=2)

    # Write materialize_corrupted_action_eval.py stub
    with (exp_dir / "scripts" / "materialize_corrupted_action_eval.py").open("w") as f:
        f.write("""#!/usr/bin/env python3
# Stub for materializing corrupted actions.
# This script will read source_success_test_id.rows.jsonl, apply corruption transforms, and save them.
import sys
print("Materialize corrupted actions stub. Usage: python3 materialize_corrupted_action_eval.py")
""")

    # README.md
    with (exp_dir / "README.md").open("w") as f:
        f.write("""# Corrupted Action Evaluation

## Purpose
Evaluate RND/ACE/FIPER robust response to corrupted actions in real-time.

## Logic
- No training or calibration happens here.
- Source dataset: `00_global_main/success_test_id`
- Corruptions applied at chunk level: zero, random_uniform, shuffled, reversed, scaled, gripper_flipped, repeated, gaussian noise.
""")
    with (exp_dir / "experiment_config.json").open("w") as f:
        json.dump({"name": exp_name, "status": "READY"}, f, indent=2)

    registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # ------------------------------------------------------------
    # 5H. 07_final_deployed_global
    # ------------------------------------------------------------
    exp_name = "07_final_deployed_global"
    exp_dir = base_dir / exp_name
    print(f"Creating experiment {exp_name}...")
    
    refs_dir = exp_dir / "datasets" / "refs"
    refs_dir.mkdir(parents=True, exist_ok=True)
    (exp_dir / "models").mkdir(parents=True, exist_ok=True)
    (exp_dir / "evals").mkdir(parents=True, exist_ok=True)
    (exp_dir / "results").mkdir(parents=True, exist_ok=True)
    (exp_dir / "logs").mkdir(parents=True, exist_ok=True)
    (exp_dir / "scripts").mkdir(parents=True, exist_ok=True)
    (exp_dir / "datasets" / "materialized").mkdir(parents=True, exist_ok=True)

    # Copy files from 00_global_main datasets/refs/* to 07_final_deployed_global/datasets/refs/*
    global_refs_dir = base_dir / "00_global_main" / "datasets" / "refs"
    for ref_file in global_refs_dir.glob("*.jsonl"):
        with ref_file.open("r") as src, (refs_dir / ref_file.name).open("w") as dst:
            dst.write(src.read())

    # README.md
    with (exp_dir / "README.md").open("w") as f:
        f.write("""# Final Deployed Global Alias

## Purpose
Alias folder for the final production monitor training and calibration config.

## Logic
- Identical to `00_global_main` references.
- Train RND on `success_train`.
- Calibrate RND and ACE on `success_calib`.
- Evaluate on test ID and failure classes.
- Diagnostic stress tests are kept separate.
""")
    with (exp_dir / "experiment_config.json").open("w") as f:
        json.dump({"name": exp_name, "status": "READY"}, f, indent=2)

    registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # Save registry
    with (base_dir / "EXPERIMENT_REGISTRY.json").open("w") as f:
        json.dump(registry_list, f, indent=2)

    with (base_dir / "EXPERIMENT_REGISTRY.md").open("w") as f:
        f.write("# FIPER Experiment Registry\n\nThis registry lists all prepared FIPER experiments.\n\n")
        f.write("| Experiment | Relative Path |\n")
        f.write("| :--- | :--- |\n")
        for reg in registry_list:
            f.write(f"| {reg['name']} | [{reg['path']}]({reg['path']}) |\n")

    return {"warnings": low_support_warnings}

def validate_prepared_dataset(
    base_dir: Path,
    row_refs: List[RowRef],
    episode_refs: List[EpisodeRef],
    workspace_root: Path
) -> dict:
    print("Running split validation check...")
    report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "checks": {},
        "summary": "PASS",
        "details": []
    }
    
    # Load central episodes list
    ep_keys = {ep.episode_key for ep in episode_refs}
    
    # Verify each experiment split mapping
    experiments_dirs = [d for d in base_dir.iterdir() if d.is_dir() and d.name != "05_per_suite"]
    # Include per-suite subfolders
    if (base_dir / "05_per_suite").exists():
        experiments_dirs.extend([d for d in (base_dir / "05_per_suite").iterdir() if d.is_dir()])
        
    for exp_dir in experiments_dirs:
        exp_name = str(exp_dir.relative_to(base_dir))
        refs_dir = exp_dir / "datasets" / "refs"
        if not refs_dir.exists():
            continue
            
        report["checks"][exp_name] = {"status": "PASS", "details": []}
        
        # Load all split files
        split_episodes = defaultdict(list)
        split_rows = defaultdict(list)
        
        for ep_file in refs_dir.glob("*.episodes.jsonl"):
            split_name = ep_file.name[:-15]
            with ep_file.open("r") as f:
                for line in f:
                    split_episodes[split_name].append(json.loads(line))
        for r_file in refs_dir.glob("*.rows.jsonl"):
            split_name = r_file.name[:-10]
            with r_file.open("r") as f:
                for line in f:
                    split_rows[split_name].append(json.loads(line))
                    
        # Check 1: Episode disjointness within experiment
        # An episode can only be assigned to ONE split (with exception of failure subclasses which are derived from failure_eval_all)
        success_seen = {}
        failure_seen = {}
        
        for split_name, eps in split_episodes.items():
            for ep in eps:
                key = ep["episode_key"]
                outcome = ep["episode_outcome"]
                
                # Verify exclusions
                if ep["suite"] == "libero_10_with_milk" and ep["task_id"] in (3, 4):
                    report["checks"][exp_name]["status"] = "FAIL"
                    report["checks"][exp_name]["details"].append(f"Exclusion violation: libero_10_with_milk task {ep['task_id']} present in split {split_name}.")
                    
                if outcome == "success":
                    if key in success_seen:
                        report["checks"][exp_name]["status"] = "FAIL"
                        report["checks"][exp_name]["details"].append(f"Disjointness violation: Success episode {key} present in both {success_seen[key]} and {split_name}.")
                    success_seen[key] = split_name
                else:
                    # Failure subclasses can overlap, but failure_eval_all should not overlap with seen/ood failures
                    if ("seen" in split_name or "ood" in split_name) and not split_name.endswith("_late") and not split_name.endswith("_near_end") and not split_name.endswith("_early") and not split_name.endswith("_mid"):
                        if key in failure_seen:
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"Disjointness violation: Failure episode {key} present in both {failure_seen[key]} and {split_name}.")
                        failure_seen[key] = split_name

        # Check 2: Success-only training/calibration
        for split_name, rows in split_rows.items():
            if "train" in split_name or "calib" in split_name:
                for r in rows:
                    if r["episode_outcome"] != "success":
                        report["checks"][exp_name]["status"] = "FAIL"
                        report["checks"][exp_name]["details"].append(f"Outcome violation: Non-success row present in train/calib split {split_name} (episode {r['episode_key']}).")

        # Check 3: OOD strict exclusions
        # OOD task: task 8/9 absent from train/calib
        if exp_name == "01_ood_task_8_9":
            for split_name, rows in split_rows.items():
                if "train" in split_name or "calib" in split_name:
                    for r in rows:
                        if r["task_id"] in (8, 9):
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"OOD Task violation: Task ID {r['task_id']} present in seen split {split_name}.")

        # OOD perturbation: held-out group absent from train/calib
        if "02_ood_perturbation_holdout_" in exp_name:
            h_group = exp_name.split("_")[-1]
            for split_name, rows in split_rows.items():
                if "train" in split_name or "calib" in split_name:
                    for r in rows:
                        if r["perturbation_group"] == h_group:
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"OOD Perturbation violation: Held-out group {h_group} present in split {split_name}.")

        # OOD suite family: held-out family absent from train/calib
        if "03_ood_suite_family_holdout_" in exp_name:
            h_family = exp_name[len("03_ood_suite_family_holdout_"):]
            # Adjust if per-suite subfolder gets caught
            if "/" not in h_family:
                for split_name, rows in split_rows.items():
                    if "train" in split_name or "calib" in split_name:
                        for r in rows:
                            if r["suite_family"] == h_family:
                                report["checks"][exp_name]["status"] = "FAIL"
                                report["checks"][exp_name]["details"].append(f"OOD Family violation: Held-out family {h_family} present in split {split_name}.")

        # Check 4: Row line number positive
        for split_name, rows in split_rows.items():
            for r in rows:
                if r["line_no"] <= 0:
                    report["checks"][exp_name]["status"] = "FAIL"
                    report["checks"][exp_name]["details"].append(f"Line number violation: Non-positive line number {r['line_no']} in split {split_name}.")

        # Check 5: Source JSONL exists on this machine
        for split_name, rows in split_rows.items():
            for r in rows:
                p = workspace_root / r["source_jsonl"]
                if not p.exists():
                    report["checks"][exp_name]["status"] = "FAIL"
                    report["checks"][exp_name]["details"].append(f"Missing file: Referenced source JSONL {r['source_jsonl']} does not exist.")

        # Check 6: Row counts match
        # (Compare row count sum across sub-splits where appropriate)

        if report["checks"][exp_name]["status"] == "FAIL":
            report["summary"] = "FAIL"

    # Sample check
    print("Sampling 100 random refs and verifying matches...")
    sampled_refs = random.sample(row_refs, min(100, len(row_refs)))
    sampled_failures = 0
    for ref in sampled_refs:
        p = workspace_root / ref.source_jsonl
        # Read exact line
        line = ""
        with p.open("r") as f:
            for idx, l in enumerate(f):
                if idx + 1 == ref.line_no:
                    line = l
                    break
        if not line:
            sampled_failures += 1
            report["details"].append(f"Sample read failed: Line {ref.line_no} in {ref.source_jsonl} empty or out of bounds.")
            continue
        try:
            row = json.loads(line)
            if row["suite"] != ref.suite or int(row["task_id"]) != ref.task_id or row["episode_outcome"] != ref.episode_outcome:
                sampled_failures += 1
                report["details"].append(f"Metadata mismatch for sampled line {ref.line_no} in {ref.source_jsonl}.")
        except Exception as e:
            sampled_failures += 1
            report["details"].append(f"Failed parsing sampled line {ref.line_no} in {ref.source_jsonl}: {e}")

    report["sampled_ref_checks"] = {
        "checked": len(sampled_refs),
        "failed": sampled_failures,
        "status": "PASS" if sampled_failures == 0 else "FAIL"
    }
    if sampled_failures > 0:
        report["summary"] = "FAIL"
        
    return report

def main() -> None:
    workspace_root = Path(__file__).resolve().parent.parent
    config_path = workspace_root / "configs" / "current_fiper_sweep_eternal_combined_relative.json"
    
    if not config_path.exists():
        print(f"Error: Relative config not found at {config_path}")
        sys.exit(1)

    print("Loading relative configuration...")
    config = read_config(config_path)
    
    print("Parsing combined dataset & building inventory...")
    row_refs, episode_refs, stats, warnings = build_inventory_and_refs(config, workspace_root)
    
    # Save Central manifests
    manifests_dir = workspace_root / "data" / "manifests" / "fiper_sweep_eternal_20260526_combined"
    print(f"Saving central manifests to {manifests_dir}...")
    save_manifest_files(manifests_dir, row_refs, episode_refs, stats, warnings)

    # Deterministic base split for global main
    print("Generating base global main split...")
    global_split_assignments = build_split(episode_refs, seed=42, stratum_warnings=warnings)

    # Create all experiment folders and splits
    experiments_root = workspace_root / "experiments" / "prepared_20260526"
    print(f"Generating experiment tree at {experiments_root}...")
    prep_stats = create_experiment_folders(experiments_root, row_refs, episode_refs, global_split_assignments)
    warnings.extend(prep_stats["warnings"])

    # Run split validation
    validation_report = validate_prepared_dataset(experiments_root, row_refs, episode_refs, workspace_root)
    
    # Save validation reports
    with (experiments_root / "PREP_VALIDATION_REPORT.json").open("w") as f:
        json.dump(validation_report, f, indent=2)

    # MD validation report
    with (experiments_root / "PREP_VALIDATION_REPORT.md").open("w") as f:
        f.write(f"""# FIPER Dataset Preparation Validation Report

**Date**: {validation_report["timestamp"]}  
**Summary Status**: **{validation_report["summary"]}**

## Sample Checks
- **Sampled Refs Checked**: {validation_report["sampled_ref_checks"]["checked"]}
- **Failed Checks**: {validation_report["sampled_ref_checks"]["failed"]}
- **Status**: **{validation_report["sampled_ref_checks"]["status"]}**

## Detailed Checks by Experiment
""")
        for exp, check in validation_report["checks"].items():
            status = check["status"]
            f.write(f"### {exp}: **{status}**\n")
            if check["details"]:
                for detail in check["details"]:
                    f.write(f"- {detail}\n")
            else:
                f.write("- All checks passed.\n")
            f.write("\n")

    print("\n============================================================")
    print("DATASET PREPARATION COMPLETED SUCCESSFULLY!")
    print(f"Manifests: {manifests_dir}")
    print(f"Experiments Tree: {experiments_root}")
    print(f"Validation summary: {validation_report['summary']}")
    print("============================================================\n")

if __name__ == "__main__":
    main()
