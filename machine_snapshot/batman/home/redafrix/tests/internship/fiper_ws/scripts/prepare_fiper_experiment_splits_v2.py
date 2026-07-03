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

def make_episode_key(machine: str, instance: str, suite: str, task_id: int, episode_id: str, start_line_no: int) -> str:
    """Key one contiguous rollout segment, not one stochastic timestep.

    The collectors can be restarted and appended into the same JSONL, so
    episode_id values such as *_r0 can repeat later in the file. The per-row
    main_seed is random at every timestep and must not be part of the episode
    key. We disambiguate repeated episode_id values by the first source line of
    the contiguous segment.
    """
    return f"{machine}_{instance}_{suite}_t{task_id}_ep{episode_id}_start{start_line_no}"

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
        current_signature = None
        current_episode_key = None
        current_timestep = None
        current_line_no = None
        
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

                replay_used = row.get("metadata", {}).get("ace_replay_used", False)
                stats["ace_replay_used_distribution"][replay_used] += 1
                stats["ace_candidate_count_distribution"][len(row["ace_candidate_chunks_normalized"])] += 1

                executed_action = row["executed_action"]
                main_chunk_env = row["main_candidate_action_chunk_env"]
                if main_chunk_env and len(main_chunk_env) > 0:
                    stats["first_action_checked"] += 1
                    if len(executed_action) > 0:
                        mismatch = False
                        for a_idx, val in enumerate(executed_action):
                            if a_idx < len(main_chunk_env[0]):
                                if abs(val - main_chunk_env[0][a_idx]) > 1e-4:
                                    mismatch = True
                                    break
                        if mismatch:
                            stats["first_action_mismatches"] += 1

                main_seed = int(row["main_seed"])
                if main_seed in stats["main_seeds"]:
                    stats["duplicate_main_seeds"] += 1
                stats["main_seeds"].add(main_seed)

                for s in row["ace_candidate_seeds"]:
                    ace_seed = int(s)
                    if ace_seed in stats["ace_seeds"]:
                        stats["duplicate_ace_seeds"] += 1
                    stats["ace_seeds"].add(ace_seed)

                timestep = int(row["timestep"])
                signature = (suite, task_id, str(row["episode_id"]))
                starts_new_segment = (
                    current_episode_key is None
                    or signature != current_signature
                    or current_timestep is None
                    or timestep <= current_timestep
                    or current_line_no is None
                    or line_no != current_line_no + 1
                )
                if starts_new_segment:
                    current_episode_key = make_episode_key(machine, instance, suite, task_id, str(row["episode_id"]), line_no)
                current_signature = signature
                current_timestep = timestep
                current_line_no = line_no
                ep_key = current_episode_key
                
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
                    timestep=timestep,
                    row_index_in_episode=-1
                )
                row_refs.append(ref)
                episodes_map[ep_key].append(ref)

    episode_refs: List[EpisodeRef] = []
    for ep_key, rows in episodes_map.items():
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
    
    del stats["main_seeds"]
    del stats["ace_seeds"]

    return row_refs, episode_refs, stats, warnings

def build_seen_splits(
    episodes: List[EpisodeRef],
    outcome: str, # "success" or "failure"
    seed: int = 42,
    stratum_warnings: List[str] = None
) -> Dict[str, str]:
    if stratum_warnings is None:
        stratum_warnings = []
        
    random.seed(seed)
    split_assignments: Dict[str, str] = {}
    
    by_stratum = defaultdict(list)
    for ep in episodes:
        by_stratum[(ep.suite, ep.task_id)].append(ep)
        
    for stratum, eps in by_stratum.items():
        random.shuffle(eps)
        n = len(eps)
        if n == 0:
            continue
            
        if outcome == "success":
            if n == 1:
                split_assignments[eps[0].episode_key] = "success_train_seen"
            elif n == 2:
                split_assignments[eps[0].episode_key] = "success_train_seen"
                split_assignments[eps[1].episode_key] = "success_test_seen"
            elif n == 3:
                split_assignments[eps[0].episode_key] = "success_train_seen"
                split_assignments[eps[1].episode_key] = "success_calib_seen"
                split_assignments[eps[2].episode_key] = "success_test_seen"
            elif n == 4:
                split_assignments[eps[0].episode_key] = "success_train_seen"
                split_assignments[eps[1].episode_key] = "success_val_seen"
                split_assignments[eps[2].episode_key] = "success_calib_seen"
                split_assignments[eps[3].episode_key] = "success_test_seen"
            else:
                n_train = max(1, int(round(0.55 * n)))
                n_val = max(1, int(round(0.15 * n)))
                n_calib = max(1, int(round(0.15 * n)))
                n_test = n - n_train - n_val - n_calib
                if n_test <= 0:
                    n_test = 1
                    n_train = n - n_val - n_calib - n_test
                    
                for i, ep in enumerate(eps):
                    if i < n_train:
                        split_assignments[ep.episode_key] = "success_train_seen"
                    elif i < n_train + n_val:
                        split_assignments[ep.episode_key] = "success_val_seen"
                    elif i < n_train + n_val + n_calib:
                        split_assignments[ep.episode_key] = "success_calib_seen"
                    else:
                        split_assignments[ep.episode_key] = "success_test_seen"
        else:
            if n == 1:
                split_assignments[eps[0].episode_key] = "failure_train_seen"
            elif n == 2:
                split_assignments[eps[0].episode_key] = "failure_train_seen"
                split_assignments[eps[1].episode_key] = "failure_test_seen"
            elif n == 3:
                split_assignments[eps[0].episode_key] = "failure_train_seen"
                split_assignments[eps[1].episode_key] = "failure_val_seen"
                split_assignments[eps[2].episode_key] = "failure_test_seen"
            else:
                n_train = max(1, int(round(0.60 * n)))
                n_val = max(1, int(round(0.20 * n)))
                n_test = n - n_train - n_val
                if n_test <= 0:
                    n_test = 1
                    n_train = n - n_val - n_test
                    
                for i, ep in enumerate(eps):
                    if i < n_train:
                        split_assignments[ep.episode_key] = "failure_train_seen"
                    elif i < n_train + n_val:
                        split_assignments[ep.episode_key] = "failure_val_seen"
                    else:
                        split_assignments[ep.episode_key] = "failure_test_seen"
                        
    return split_assignments

def save_manifest_files(
    output_dir: Path,
    row_refs: List[RowRef],
    episode_refs: List[EpisodeRef],
    stats: dict,
    warnings: List[str]
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "dataset_inventory.json").open("w") as f:
        json.dump({"stats": stats, "warnings": warnings}, f, indent=2)
    with (output_dir / "episodes.jsonl").open("w") as f:
        for ep in episode_refs:
            f.write(json.dumps(asdict(ep)) + "\n")
    with (output_dir / "rows.refs.jsonl").open("w") as f:
        for r in row_refs:
            f.write(json.dumps(asdict(r)) + "\n")

def create_experiment_folders(
    base_dir: Path,
    row_refs: List[RowRef],
    episode_refs: List[EpisodeRef],
    global_split_assignments: Dict[str, str] = None
) -> dict:
    base_dir.mkdir(parents=True, exist_ok=True)
    registry_list = []
    low_support_warnings = []

    row_by_ep = defaultdict(list)
    for r in row_refs:
        row_by_ep[r.episode_key].append(r)

    def write_experiment_splits(
        exp_dir: Path,
        exp_split_mapping: Dict[str, str]
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

        CANONICAL_SPLITS = [
            "success_train_seen",
            "success_val_seen",
            "success_calib_seen",
            "success_test_seen",
            "success_test_ood",
            "failure_train_seen",
            "failure_val_seen",
            "failure_test_seen",
            "failure_eval_ood"
        ]

        for split_name in CANONICAL_SPLITS:
            eps = sorted(episodes_by_split[split_name], key=lambda e: e.episode_key)
            rows = sorted(rows_by_split[split_name], key=lambda r: (r.source_jsonl, r.line_no))
            with (refs_dir / f"{split_name}.episodes.jsonl").open("w") as f:
                for ep in eps:
                    f.write(json.dumps(asdict(ep)) + "\n")
            with (refs_dir / f"{split_name}.rows.jsonl").open("w") as f:
                for r in rows:
                    f.write(json.dumps(asdict(r)) + "\n")

    # 5A. 00_global_main
    exp_name = "00_global_main"
    exp_dir = base_dir / exp_name
    print(f"Creating experiment {exp_name}...")
    success_eps = [ep for ep in episode_refs if ep.episode_outcome == "success"]
    failure_eps = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout"]
    success_splits = build_seen_splits(success_eps, "success", seed=42, stratum_warnings=low_support_warnings)
    failure_splits = build_seen_splits(failure_eps, "failure", seed=42, stratum_warnings=low_support_warnings)
    exp_splits = {}
    exp_splits.update(success_splits)
    exp_splits.update(failure_splits)
    write_experiment_splits(exp_dir, exp_splits)
    with (exp_dir / "README.md").open("w") as f:
        f.write("# Global Main\n")
    with (exp_dir / "experiment_config.json").open("w") as f:
        json.dump({"name": exp_name, "status": "READY"}, f, indent=2)
    registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # 5B. 01_ood_task_8_9
    exp_name = "01_ood_task_8_9"
    exp_dir = base_dir / exp_name
    print(f"Creating experiment {exp_name}...")
    seen_success = [ep for ep in episode_refs if ep.episode_outcome == "success" and ep.task_id < 8]
    seen_failure = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout" and ep.task_id < 8]
    success_splits = build_seen_splits(seen_success, "success", seed=42, stratum_warnings=low_support_warnings)
    failure_splits = build_seen_splits(seen_failure, "failure", seed=42, stratum_warnings=low_support_warnings)
    exp_splits = {}
    exp_splits.update(success_splits)
    exp_splits.update(failure_splits)
    for ep in episode_refs:
        if ep.task_id >= 8:
            if ep.episode_outcome == "success":
                exp_splits[ep.episode_key] = "success_test_ood"
            else:
                exp_splits[ep.episode_key] = "failure_eval_ood"
    write_experiment_splits(exp_dir, exp_splits)
    with (exp_dir / "README.md").open("w") as f:
        f.write("# OOD Task Split\n")
    with (exp_dir / "experiment_config.json").open("w") as f:
        json.dump({"name": exp_name, "status": "READY"}, f, indent=2)
    registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # 5C. 02_ood_perturbation_holdout
    for holdout_group in ["mug", "milk", "object", "env"]:
        exp_name = f"02_ood_perturbation_holdout_{holdout_group}"
        exp_dir = base_dir / exp_name
        print(f"Creating experiment {exp_name}...")
        seen_success = [ep for ep in episode_refs if ep.episode_outcome == "success" and ep.perturbation_group != holdout_group]
        seen_failure = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout" and ep.perturbation_group != holdout_group]
        success_splits = build_seen_splits(seen_success, "success", seed=42, stratum_warnings=low_support_warnings)
        failure_splits = build_seen_splits(seen_failure, "failure", seed=42, stratum_warnings=low_support_warnings)
        exp_splits = {}
        exp_splits.update(success_splits)
        exp_splits.update(failure_splits)
        for ep in episode_refs:
            if ep.perturbation_group == holdout_group:
                if ep.episode_outcome == "success":
                    exp_splits[ep.episode_key] = "success_test_ood"
                else:
                    exp_splits[ep.episode_key] = "failure_eval_ood"
        write_experiment_splits(exp_dir, exp_splits)
        with (exp_dir / "README.md").open("w") as f:
            f.write(f"# OOD Perturbation Holdout: {holdout_group}\n")
        with (exp_dir / "experiment_config.json").open("w") as f:
            json.dump({"name": exp_name, "status": "READY", "holdout_group": holdout_group}, f, indent=2)
        registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

    # 5D. 03_ood_suite_family_holdout
    for holdout_family in ["spatial", "object_family", "goal", "10_family"]:
        exp_name = f"03_ood_suite_family_holdout_{holdout_family}"
        exp_dir = base_dir / exp_name
        print(f"Creating experiment {exp_name}...")
        seen_success = [ep for ep in episode_refs if ep.episode_outcome == "success" and ep.suite_family != holdout_family]
        seen_failure = [ep for ep in episode_refs if ep.episode_outcome == "failure_or_timeout" and ep.suite_family != holdout_family]
        success_splits = build_seen_splits(seen_success, "success", seed=42, stratum_warnings=low_support_warnings)
        failure_splits = build_seen_splits(seen_failure, "failure", seed=42, stratum_warnings=low_support_warnings)
        exp_splits = {}
        exp_splits.update(success_splits)
        exp_splits.update(failure_splits)
        for ep in episode_refs:
            if ep.suite_family == holdout_family:
                if ep.episode_outcome == "success":
                    exp_splits[ep.episode_key] = "success_test_ood"
                else:
                    exp_splits[ep.episode_key] = "failure_eval_ood"
        write_experiment_splits(exp_dir, exp_splits)
        with (exp_dir / "README.md").open("w") as f:
            f.write(f"# OOD Suite Family Holdout: {holdout_family}\n")
        with (exp_dir / "experiment_config.json").open("w") as f:
            json.dump({"name": exp_name, "status": "READY", "holdout_family": holdout_family}, f, indent=2)
        registry_list.append({"name": exp_name, "path": str(exp_dir.relative_to(base_dir.parent.parent))})

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
    
    experiments_dirs = [d for d in base_dir.iterdir() if d.is_dir()]
    for exp_dir in experiments_dirs:
        exp_name = str(exp_dir.relative_to(base_dir))
        refs_dir = exp_dir / "datasets" / "refs"
        if not refs_dir.exists():
            continue
            
        report["checks"][exp_name] = {"status": "PASS", "details": []}
        
        split_episodes = defaultdict(list)
        split_rows = defaultdict(list)
        
        for ep_file in refs_dir.glob("*.episodes.jsonl"):
            split_name = ep_file.name.removesuffix(".episodes.jsonl")
            with ep_file.open("r") as f:
                for line in f:
                    if line.strip():
                        split_episodes[split_name].append(json.loads(line))
        for r_file in refs_dir.glob("*.rows.jsonl"):
            split_name = r_file.name.removesuffix(".rows.jsonl")
            with r_file.open("r") as f:
                for line in f:
                    if line.strip():
                        split_rows[split_name].append(json.loads(line))
                        
        success_seen = {}
        failure_seen = {}
        
        for split_name, eps in split_episodes.items():
            rows = split_rows.get(split_name, [])
            expected_rows = sum(int(ep.get("num_rows", 0)) for ep in eps)
            if expected_rows != len(rows):
                report["checks"][exp_name]["status"] = "FAIL"
                report["checks"][exp_name]["details"].append(
                    f"Episode/row count violation: split {split_name} episodes claim {expected_rows} rows but row refs contain {len(rows)} rows."
                )
            if len(rows) >= 500 and len(rows) == len(eps):
                report["checks"][exp_name]["status"] = "FAIL"
                report["checks"][exp_name]["details"].append(
                    f"Episode grouping violation: split {split_name} has {len(rows)} rows and {len(eps)} episodes; this usually means each timestep was keyed as its own episode."
                )
            for ep in eps:
                key = ep["episode_key"]
                outcome = ep["episode_outcome"]
                if "_seed" in key:
                    report["checks"][exp_name]["status"] = "FAIL"
                    report["checks"][exp_name]["details"].append(
                        f"Episode key violation: split {split_name} contains per-timestep seed key {key}."
                    )
                
                if ep["suite"] == "libero_10_with_milk" and ep["task_id"] in (3, 4):
                    report["checks"][exp_name]["status"] = "FAIL"
                    report["checks"][exp_name]["details"].append(f"Exclusion violation: libero_10_with_milk task {ep['task_id']} present in split {split_name}.")
                    
                if outcome == "success":
                    if split_name in ["success_train_seen", "success_val_seen", "success_calib_seen", "success_test_seen"]:
                        if key in success_seen:
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"Disjointness violation: Success episode {key} present in both {success_seen[key]} and {split_name}.")
                        success_seen[key] = split_name
                else:
                    if split_name in ["failure_train_seen", "failure_val_seen", "failure_test_seen"]:
                        if key in failure_seen:
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"Disjointness violation: Failure episode {key} present in both {failure_seen[key]} and {split_name}.")
                        failure_seen[key] = split_name

        # Check 2: Success-only / Failure-only splits outcome match
        for split_name, rows in split_rows.items():
            if split_name.startswith("success_"):
                for r in rows:
                    if r["episode_outcome"] != "success":
                        report["checks"][exp_name]["status"] = "FAIL"
                        report["checks"][exp_name]["details"].append(f"Outcome violation: Non-success row present in split {split_name} (episode {r['episode_key']}).")
            elif split_name.startswith("failure_"):
                for r in rows:
                    if r["episode_outcome"] == "success":
                        report["checks"][exp_name]["status"] = "FAIL"
                        report["checks"][exp_name]["details"].append(f"Outcome violation: Success row present in split {split_name} (episode {r['episode_key']}).")

        # Check 3: OOD strict exclusions
        if exp_name == "01_ood_task_8_9":
            for split_name, rows in split_rows.items():
                if split_name in ["success_train_seen", "success_val_seen", "success_calib_seen", "success_test_seen", "failure_train_seen", "failure_val_seen", "failure_test_seen"]:
                    for r in rows:
                        if r["task_id"] in (8, 9):
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"OOD Task violation: Task ID {r['task_id']} present in seen split {split_name}.")

        if "02_ood_perturbation_holdout_" in exp_name:
            h_group = exp_name.split("_")[-1]
            for split_name, rows in split_rows.items():
                if split_name in ["success_train_seen", "success_val_seen", "success_calib_seen", "success_test_seen", "failure_train_seen", "failure_val_seen", "failure_test_seen"]:
                    for r in rows:
                        if r["perturbation_group"] == h_group:
                            report["checks"][exp_name]["status"] = "FAIL"
                            report["checks"][exp_name]["details"].append(f"OOD Perturbation violation: Held-out group {h_group} present in split {split_name}.")

        if "03_ood_suite_family_holdout_" in exp_name:
            h_family = exp_name[len("03_ood_suite_family_holdout_"):]
            if "/" not in h_family:
                for split_name, rows in split_rows.items():
                    if split_name in ["success_train_seen", "success_val_seen", "success_calib_seen", "success_test_seen", "failure_train_seen", "failure_val_seen", "failure_test_seen"]:
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

        # Check 5: Source JSONL exists on Batman
        for split_name, rows in split_rows.items():
            for r in rows:
                p = workspace_root / r["source_jsonl"]
                if not p.exists():
                    report["checks"][exp_name]["status"] = "FAIL"
                    report["checks"][exp_name]["details"].append(f"Missing file: Referenced source JSONL {r['source_jsonl']} does not exist.")

        if report["checks"][exp_name]["status"] == "FAIL":
            report["summary"] = "FAIL"

    print("Sampling 100 random refs and verifying matches...")
    sampled_refs = random.sample(row_refs, min(100, len(row_refs)))
    sampled_failures = 0
    for ref in sampled_refs:
        p = workspace_root / ref.source_jsonl
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
    config_path = workspace_root / "configs" / "current_fiper_sweep_eternal_20260527_combined_relative.json"
    
    if not config_path.exists():
        print(f"Error: Config not found at {config_path}")
        sys.exit(1)

    print("Loading configuration...")
    config = read_config(config_path)
    
    print("Parsing combined dataset & building inventory...")
    row_refs, episode_refs, stats, warnings = build_inventory_and_refs(config, workspace_root)
    
    manifests_dir = workspace_root / "data" / "manifests" / "fiper_sweep_eternal_20260527_combined"
    print(f"Saving central manifests to {manifests_dir}...")
    save_manifest_files(manifests_dir, row_refs, episode_refs, stats, warnings)

    experiments_root = workspace_root / "experiments" / "prepared_20260527"
    print(f"Generating experiment tree at {experiments_root}...")
    prep_stats = create_experiment_folders(experiments_root, row_refs, episode_refs)
    warnings.extend(prep_stats["warnings"])

    validation_report = validate_prepared_dataset(experiments_root, row_refs, episode_refs, workspace_root)
    
    with (experiments_root / "PREP_VALIDATION_REPORT.json").open("w") as f:
        json.dump(validation_report, f, indent=2)

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
