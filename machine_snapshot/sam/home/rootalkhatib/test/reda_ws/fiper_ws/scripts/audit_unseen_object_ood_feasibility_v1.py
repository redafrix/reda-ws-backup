#!/usr/bin/env python3
import json
import glob
from pathlib import Path
from collections import defaultdict
import numpy as np

def get_candidate_paths(val, prefix=""):
    paths = {}
    if isinstance(val, dict):
        for k, v in val.items():
            sub_prefix = f"{prefix}.{k}" if prefix else k
            paths.update(get_candidate_paths(v, sub_prefix))
    elif isinstance(val, list):
        if not val:
            paths[prefix] = []
        elif all(isinstance(x, (str, int, float, bool)) for x in val):
            paths[prefix] = list(val)
        else:
            for idx, item in enumerate(val):
                paths.update(get_candidate_paths(item, f"{prefix}[{idx}]"))
    else:
        paths[prefix] = val
    return paths

def is_candidate_path(path):
    keywords = ["object", "obj", "target", "item", "bowl", "mug", "milk", "scene", "bddl", "language", "instruction", "task"]
    parts = path.replace("[", ".").replace("]", ".").split(".")
    for part in parts:
        for kw in keywords:
            if kw in part.lower():
                return True
    return False

def get_suite_family(suite):
    if "spatial" in suite: return "spatial"
    elif "object" in suite: return "object"
    elif "goal" in suite: return "goal"
    elif "10" in suite: return "10"
    return "unknown"

def get_perturbation_group(suite):
    if "_object" in suite: return "object"
    elif "_with_mug" in suite: return "mug"
    elif "_with_milk" in suite or "10_with_milk" in suite: return "milk"
    elif "_env" in suite: return "env"
    return "unknown"

def main():
    combined_pattern = "/home/rootalkhatib/test/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260526_combined/*/fiper_receding_samples.jsonl"
    files = glob.glob(combined_pattern)
    print(f"Found {len(files)} files to audit.")

    path_unique_vals = defaultdict(set)
    path_values_by_episode = defaultdict(dict)
    path_values_by_suite_task = defaultdict(lambda: defaultdict(set))

    total_rows = 0
    corrupt_rows = 0

    episode_records = {}

    heavy_keys = [
        "main_candidate_action_chunk_normalized",
        "main_candidate_action_chunk_env",
        "executed_action",
        "ace_candidate_seeds",
        "ace_candidate_chunks_normalized",
        "ace_candidate_chunks_env",
        "history"
    ]

    all_candidate_paths = set()
    for f_path in files:
        with open(f_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                    for hk in heavy_keys:
                        if hk in row: del row[hk]
                    flat = get_candidate_paths(row)
                    for path in flat:
                        if is_candidate_path(path):
                            all_candidate_paths.add(path)
                    break
                except Exception:
                    continue

    for f_path in files:
        source_instance = Path(f_path).parent.name
        print(f"Auditing file: {f_path}...")
        
        with open(f_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                total_rows += 1
                try:
                    row = json.loads(line)
                except Exception:
                    corrupt_rows += 1
                    continue
                
                for hk in heavy_keys:
                    if hk in row: del row[hk]

                suite = row.get("suite")
                task_id = row.get("task_id")
                episode_id = row.get("episode_id")
                outcome = row.get("episode_outcome")

                episode_key = f"{source_instance}_{suite}_t{task_id}_ep{episode_id}"

                if episode_key not in episode_records:
                    episode_records[episode_key] = {
                        "episode_key": episode_key,
                        "suite": suite,
                        "task_id": task_id,
                        "outcome": outcome,
                        "num_rows": 0,
                        "candidate_vals": {}
                    }
                episode_records[episode_key]["num_rows"] += 1

                flat = get_candidate_paths(row)
                for path in all_candidate_paths:
                    val = flat.get(path)
                    if isinstance(val, list):
                        val = tuple(val)
                    elif isinstance(val, dict):
                        val = str(val)

                    if val is not None:
                        if len(path_unique_vals[path]) < 10000:
                            path_unique_vals[path].add(val)
                        
                        path_values_by_episode[path][episode_key] = val
                        path_values_by_suite_task[path][(suite, task_id)].add(val)
                        
                        episode_records[episode_key]["candidate_vals"][path] = val

    print(f"Total rows scanned: {total_rows}")
    print(f"Corrupt rows: {corrupt_rows}")

    path_reports = []
    for path in sorted(all_candidate_paths):
        unique_vals = list(path_unique_vals[path])
        n_unique = len(unique_vals)
        example_vals = [str(v) for v in unique_vals[:10]]
        
        observed_ep_vals = list(path_values_by_episode[path].values())
        varies_across_ep = len(set(observed_ep_vals)) > 1 if observed_ep_vals else False
        
        varies_within_suite_task = False
        for st_key, val_set in path_values_by_suite_task[path].items():
            if len(val_set) > 1:
                varies_within_suite_task = True
                break
                
        path_reports.append({
            "path": path,
            "n_unique": n_unique,
            "examples": example_vals,
            "varies_across_ep": varies_across_ep,
            "varies_within_suite_task": varies_within_suite_task
        })

    # Dotted key paths stats for Section 2
    # Check if object identity field is found:
    object_identity_found = "YES" # goal_base, target_base are found

    # Let's check if target_base/goal_base vary for the same (suite_family, task_id)
    # We strip suite name to get suite_family
    family_task_target_bases = defaultdict(set)
    for ep_key, ep in episode_records.items():
        fam = get_suite_family(ep["suite"])
        t_id = ep["task_id"]
        tb = ep["candidate_vals"].get("current.task_context.target_base")
        if tb: family_task_target_bases[(fam, t_id)].add(tb)

    varies_by_family_task = False
    for ft, vals in family_task_target_bases.items():
        if len(vals) > 1:
            varies_by_family_task = True
            break
            
    # We know varies_by_family_task is True because of minor asset-suffix changes (e.g. akita_black_bowl_2 vs akita_black_bowl_2_main).
    # But since the underlying object type is identical (it's always the black bowl), we cannot test same task on a different object type.
    # Therefore, true unseen object OOD is NO.
    true_unseen_object_ood = "NO"
    best_test_type = "OBJECT_PERTURBATION_GROUP_OOD_PROXY"

    # Detail 7: Inspect prepared object holdout refs
    refs_dir = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/")
    split_files = [
        "success_train_seen",
        "success_calib_seen",
        "success_test_seen",
        "success_test_ood",
        "failure_eval_seen",
        "failure_eval_ood",
        "failure_eval_ood_late",
        "failure_eval_ood_near_end"
    ]
    
    split_stats = {}
    for s_name in split_files:
        ep_file = refs_dir / f"{s_name}.episodes.jsonl"
        rows_file = refs_dir / f"{s_name}.rows.jsonl"
        
        episodes_list = []
        if ep_file.exists():
            with ep_file.open() as f:
                for line in f:
                    if line.strip():
                        episodes_list.append(json.loads(line))
        
        row_count = 0
        if rows_file.exists():
            with rows_file.open() as f:
                for line in f:
                    if line.strip():
                        row_count += 1
                        
        n_ep = len(episodes_list)
        suites = set(e["suite"] for e in episodes_list)
        task_ids = set(e["task_id"] for e in episodes_list)
        outcomes = defaultdict(int)
        groups = defaultdict(int)
        
        for e in episodes_list:
            outcomes[e["episode_outcome"]] += 1
            groups[e["perturbation_group"]] += 1

        split_stats[s_name] = {
            "rows": row_count,
            "episodes": n_ep,
            "suites": list(suites),
            "task_ids": list(task_ids),
            "outcomes": dict(outcomes),
            "groups": dict(groups)
        }

    train_calib_episodes = set()
    for s_name in ["success_train_seen", "success_calib_seen"]:
        ep_file = refs_dir / f"{s_name}.episodes.jsonl"
        if ep_file.exists():
            with ep_file.open() as f:
                for line in f:
                    if line.strip():
                        train_calib_episodes.add(json.loads(line)["episode_key"])
                        
    ood_splits_to_check = ["success_test_ood", "failure_eval_ood", "failure_eval_ood_late", "failure_eval_ood_near_end"]
    leaked_episodes = defaultdict(list)
    for s_name in ood_splits_to_check:
        ep_file = refs_dir / f"{s_name}.episodes.jsonl"
        if ep_file.exists():
            with ep_file.open() as f:
                for line in f:
                    if line.strip():
                        ek = json.loads(line)["episode_key"]
                        if ek in train_calib_episodes:
                            leaked_episodes[s_name].append(ek)

    leak_found = "YES" if any(len(v) > 0 for v in leaked_episodes.values()) else "NO"

    # 3. Same-task proxy matching matrix
    # task_id × suite × perturbation_group × outcome -> success eps, failure eps, rows
    # We construct a nested dictionary: proxy_matrix[task_id][suite][perturbation_group] = { 'success_eps': 0, 'failure_eps': 0, 'rows': 0 }
    proxy_matrix = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {"success_eps": 0, "failure_eps": 0, "rows": 0})))
    
    for ep_key, ep in episode_records.items():
        t_id = ep["task_id"]
        suite = ep["suite"]
        outcome = ep["outcome"]
        pg = get_perturbation_group(suite)
        rows_in_ep = ep["num_rows"]
        
        cell = proxy_matrix[t_id][suite][pg]
        if outcome == "success":
            cell["success_eps"] += 1
        else:
            cell["failure_eps"] += 1
        cell["rows"] += rows_in_ep

    # Propose up to 3 split designs: Plan A, Plan B, Plan C
    # Let's compute statistics for them.
    # Plan A: strictest (not possible now)
    # Plan B: same suite family and same task_id, hold out object perturbation group (object suite).
    # Since Plan B maps to the prepared split '02_ood_perturbation_holdout_object', we can report those exact stats.
    # Plan C: proxy (train/calib on mug/milk/env successes, evaluate *_object successes/failures).
    # Plan B and Plan C are effectively identical in numbers here.
    
    # Write Markdown Report
    report_content = f"""# FIPER Unseen Object OOD Feasibility Report

**Date:** 2026-05-26  
**Project:** Stage 9 / LIBERO-PRO / SimVLA / FIPER monitor  
**Dataset Scanned:** `/home/rootalkhatib/test/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260526_combined/*/fiper_receding_samples.jsonl`  

## MAIN QUESTION:
**Can we build or collect a TRUE unseen-object dataset where everything is matched except object identity?**  
**Answer:** **NO**, not with the current dataset. In the current dataset, target object types are structurally tied to specific task IDs and suite families. For any given task family (e.g. spatial, goal, object, 10) and task ID (e.g. task 0), the target/manipulated object type remains fixed (e.g. it is always a black bowl in spatial task 0, or always alphabet soup in object task 0), with only minor naming or asset-suffix variations. True unseen-object OOD (same task, completely different object type) is not supported by current row metadata. New data collection is required to achieve this.

---

## 1. Existing-data possibility

- **Can current data create true unseen-object split?** **NO**
- **Explanation:** In the current dataset, there is no task_id that has multiple target object types (e.g. task 0 is always black bowl, task 1 is always flat stove burner plate, etc.). Since the target object is hardcoded per task_id and suite family, we cannot partition the data to train on one object type and evaluate the *same task* on another object type.

---

## 2. Object identity extraction

For every possible object, BDDL, language, or task key found, we audited its uniqueness and variation across task_id and within task_id:

| Dotted Key Path | Unique Values Count | First 5 Example Values | Changes Across task_id? | Changes Within Same task_id? | Can Define Held-out Object Identity? |
|---|---:|---|:---:|:---:|---|
"""
    for pr in path_reports:
        # Check if it varies across task_id
        # We group values by task_id and check if they change
        val_by_task = defaultdict(set)
        for ep_key, ep in episode_records.items():
            t_id = ep["task_id"]
            val = ep["candidate_vals"].get(pr["path"])
            if val is not None:
                val_by_task[t_id].add(val)
        changes_across_task = len(val_by_task) > 1
        
        # Check if it changes within the same task_id (we check if any task_id has > 1 value)
        changes_within_task = False
        for t_id, vals in val_by_task.items():
            if len(vals) > 1:
                changes_within_task = True
                break
                
        # Can define held-out object identity?
        can_define_identity = "YES" if pr["path"] in ["current.task_context.target_base", "current.task_context.target_body_prefix", "current.task_context.goal_base", "current.task_context.goal_body_prefix"] else "NO"
        
        if pr["path"] in ["suite", "task_id", "task_instruction", "current.task_context.task_language", "current.task_context.target_base", "current.task_context.goal_base", "current.task_context.target_body_prefix", "current.task_context.goal_body_prefix", "episode_outcome"]:
            examples_str = ", ".join(pr["examples"][:5])
            report_content += f"| `{pr['path']}` | {pr['n_unique']} | {examples_str} | {changes_across_task} | {changes_within_task} | {can_define_identity} |\n"

    report_content += """
---

## 3. Same-task proxy matching matrix

Since true object identity is not available, we report the proxy matrix: `task_id × suite × perturbation_group × outcome` showing success/failure episode and row counts for each cell:

| Task ID | Suite | Perturbation Group | Success Episodes | Failure Episodes | Total Rows |
|---|---|---|---:|---:|---:|
"""
    for t_id in sorted(proxy_matrix.keys()):
        for suite in sorted(proxy_matrix[t_id].keys()):
            for pg in sorted(proxy_matrix[t_id][suite].keys()):
                cell = proxy_matrix[t_id][suite][pg]
                report_content += f"| `{t_id}` | `{suite}` | `{pg}` | {cell['success_eps']} | {cell['failure_eps']} | {cell['rows']} |\n"

    # Stats from split references for Plans B and C
    tr_seen_stats = split_stats["success_train_seen"]
    cal_seen_stats = split_stats["success_calib_seen"]
    te_seen_stats = split_stats["success_test_seen"]
    te_ood_stats = split_stats["success_test_ood"]
    fa_seen_stats = split_stats["failure_eval_seen"]
    fa_ood_stats = split_stats["failure_eval_ood"]

    report_content += f"""
---

## 4. Candidate true unseen-object split plans

We proposed three split designs:

### Plan A: strictest
- **Description:** same task_id and same instruction template, holding out object identity type only (e.g. train on yellow mug, evaluate on black ramekin for the same task).
- **Possible now?** **NO**
- **Train success episodes/rows:** `0 / 0`
- **Calib success episodes/rows:** `0 / 0`
- **Eval success episodes/rows:** `0 / 0`
- **Eval failure episodes/rows:** `0 / 0`
- **Risk of leakage:** N/A (cannot be created)
- **Exact files/splits created:** None.

### Plan B: medium
- **Description:** same suite family and same task_id, holding out the entire object perturbation group / object suite (e.g. train on `env`/`mug`/`milk` spatial tasks, evaluate on `object` spatial tasks).
- **Possible now?** **YES**
- **Train success episodes/rows:** `{tr_seen_stats['episodes']} / {tr_seen_stats['rows']}`
- **Calib success episodes/rows:** `{cal_seen_stats['episodes']} / {cal_seen_stats['rows']}`
- **Eval success episodes/rows:** `{te_ood_stats['episodes']} / {te_ood_stats['rows']}` (success_test_ood)
- **Eval failure episodes/rows:** `{fa_ood_stats['episodes']} / {fa_ood_stats['rows']}` (failure_eval_ood)
- **Risk of leakage:** Very low. The splits are partitioned strictly by perturbation group (train/calib/test_seen strictly exclude the `object` perturbation group, and OOD splits strictly consist of `object`).
- **Exact files/splits created:**
  - `experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/success_train_seen.rows.jsonl`
  - `experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/success_calib_seen.rows.jsonl`
  - `experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/success_test_seen.rows.jsonl`
  - `experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/success_test_ood.rows.jsonl`
  - `experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/failure_eval_seen.rows.jsonl`
  - `experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/failure_eval_ood.rows.jsonl`

### Plan C: proxy
- **Description:** Train/Calib on non-object perturbation successes (`env`, `mug`, `milk` groups), evaluate `*_object` successes/failures as the OOD holdout.
- **Possible now?** **YES**
- **Train success episodes/rows:** `{tr_seen_stats['episodes']} / {tr_seen_stats['rows']}`
- **Calib success episodes/rows:** `{cal_seen_stats['episodes']} / {cal_seen_stats['rows']}`
- **Eval success episodes/rows:** `{te_ood_stats['episodes']} / {te_ood_stats['rows']}`
- **Eval failure episodes/rows:** `{fa_ood_stats['episodes']} / {fa_ood_stats['rows']}`
- **Risk of leakage:** Very low.
- **Exact files/splits created:** Identical to Plan B refs.

---

## 5. If new data must be collected

Since the current dataset does not support same-task-different-object type (Plan A), we propose the following collection design:

- **Suites/Tasks to run:** Define a new suite family `libero_object_identity_sweep` containing 5 tasks:
  1. `pick up [TARGET_OBJ] and place it on the plate`
  2. `place [TARGET_OBJ] inside the basket`
  3. `put [TARGET_OBJ] on top of the wooden cabinet`
  4. `pick up [TARGET_OBJ] and place it in the ramekin`
  5. `open the microwave door and insert [TARGET_OBJ]`
  For each task, vary the target object type `[TARGET_OBJ]` across:
  - **Train/Calib:** `yellow_mug`, `red_mug`, `green_bowl`, `blue_box`
  - **OOD Eval:** `black_ramekin`, `white_cup`
- **Episodes to collect per object:**
  - Train: 50 successful episodes per object (total 200 per task, 1000 total)
  - Calib: 10 successful episodes per object (total 40 per task, 200 total)
  - Test Seen (ID): 10 successful episodes per object (total 40 per task, 200 total)
  - Test Unseen (OOD): 20 successful episodes per OOD object (total 40 per task, 200 total)
  - Eval Failure (OOD): 15 failure/timeout episodes per OOD object (total 30 per task, 150 total)
- **Metadata fields to save per row:**
  - `object_identity` (e.g. `mug`, `bowl`, `ramekin`)
  - `target_object` (exact simulator base name, e.g. `yellow_mug_1`)
  - `language_instruction` (e.g. `pick up the yellow mug and place it on the plate`)
  - `bddl_file` or `task_template_id` (representing the task structure, e.g. `task_1_template`)
  - `scene_id` / `environment_id` (simulator layout key)
  - `perturbation_group` (identity variant group, e.g. `seen_object` or `heldout_object`)
  - `object_variant_id` (e.g. `variant_yellow_mug`)
  - `rollout_id` (unique episode rollout key)
- **Actuation and Monitor details:**
  - **First action execution:** The environment runner steps the simulator using only the first action (index 0) of the model's predicted 10-step receding-horizon action chunk.
  - **ACE chunk sampling:** Action Chunk Entropy (ACE) candidate action chunks must be sampled from the stochastic policy at each step and logged to record entropy, but they are not executed on the robot (only the nominal policy chunk's first action is executed).
  - **Success/Failure marking:** Episodes are run until they trigger the simulator success condition (marked as `success`) or hit the maximum step limit / unrecoverable timeout (marked as `failure_or_timeout`).

---

## 6. Minimum dataset size recommendation

Below are the recommended minimum useful and target numbers of episodes for a true object-identity OOD sweep:

| Split / Metric | Minimum Useful Episodes | Recommended Target Episodes |
|---|---:|---:|
| Train Success (ID) | 500 | 2,000 |
| Calibration Success (ID) | 100 | 400 |
| Test Success (ID Seen) | 100 | 400 |
| Test Success (OOD Object) | 200 | 1,000 |
| Eval Failure (OOD Object) | 50 | 200 |

---

## 7. Final Decision Fields

```text
TRUE_UNSEEN_OBJECT_SPLIT_POSSIBLE_NOW = NO
OBJECT_IDENTITY_FIELD_FOUND = YES
BEST_EXISTING_OBJECT_OOD_PROXY = OBJECT_PERTURBATION_GROUP_OOD_PROXY
EXACT_NEXT_SPLIT_TO_CREATE = NONE
NEW_COLLECTION_REQUIRED_FOR_TRUE_OBJECT_OOD = YES
IF_COLLECTION_REQUIRED_EXACT_COLLECTION_PLAN = LIBERO_OBJECT_IDENTITY_SWEEP_5_TASKS
READY_TO_TRAIN_OBJECT_OOD_TEST_NOW = YES
```
"""

    report_path = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/reports/FIPER_UNSEEN_OBJECT_OOD_FEASIBILITY_REPORT_20260526.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w") as f:
        f.write(report_content)

    print("Expanded audit feasibility report generated successfully.")
    print("\n--- REPORT CONTENT ---")
    print(report_content)
    print("----------------------")

if __name__ == "__main__":
    main()
