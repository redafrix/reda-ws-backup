# FIPER Experiment Dataset Preparation Report

**Date**: 2026-05-26  
**Status**: **COMPLETE & SYNCHRONIZED**

## 1. Executive Summary
This report summarizes the consolidation, synchronization, and experiment preparation tasks for the FIPER project. We have combined the dataset campaigns from Sam (`sam`) and Bob (`pcrobot`) into a unified frozen dataset consisting of **635,921** raw rows. 

We generated central manifests and split references for 8 distinct experiment groups (covering global training, OOD task stress testing, OOD perturbation testing, OOD suite family testing, per-perturbation testing, per-suite testing, and action corruption evaluations). Validation checks passed successfully on all experiments on both machines, confirming dataset partition disjointness, metadata mapping accuracy, and row referencing consistency.

## 2. Collector Status
No collector processes are active. Verified using:
```bash
pgrep -af "[c]ollect_fiper_receding_all_outcomes_v2"
```
Output: *None* (Confirmed stopped on both Sam and Bob).

## 3. Final Row Counts and Combined Dataset Availability
The final row counts for the raw receding samples on both hosts are as follows:

| Host | Instance / Path | Row Count |
| :--- | :--- | :---: |
| **Sam** | `instance_A/fiper_receding_samples.jsonl` | 159,838 |
| **Sam** | `instance_B/fiper_receding_samples.jsonl` | 159,892 |
| | **Sam Raw Total** | **319,730** |
| **Bob** | `instance_A/fiper_receding_samples.jsonl` | 158,128 |
| **Bob** | `instance_B/fiper_receding_samples.jsonl` | 158,063 |
| | **Bob Raw Total** | **316,191** |
| | **Combined Raw Total** | **635,921** |

### Relative Frozen Layout
The following identical dataset structure is available on both hosts under `fiper_ws/data/frozen/fiper_sweep_eternal_20260526_combined/`:
```text
fiper_sweep_eternal_20260526_combined/
  sam_instance_A/fiper_receding_samples.jsonl (159,838 rows)
  sam_instance_B/fiper_receding_samples.jsonl (159,892 rows)
  bob_instance_A/fiper_receding_samples.jsonl (158,128 rows)
  bob_instance_B/fiper_receding_samples.jsonl (158,063 rows)
  logs/
    sam_mug.log
    sam_milk.log
    bob_obj.log
    bob_env.log
  SOURCE_PATHS.md
```

- **Sam Workspace Details**: Sam's workspace is on an ext4 mount. Files under `sam_instance_A` and `sam_instance_B` are symlinked to local raw campaigns to conserve space, while `bob_instance_A` and `bob_instance_B` are real copies transferred over the local network.
- **Bob Workspace Details**: Bob's workspace resides on `/media/rootalkhatib/My Passport/`, which is formatted as exFAT. Since exFAT does not support symlinks, all combined dataset files on Bob are real copies.
- **Row Counts Verification**: The line count for all JSONLs has been verified via `wc -l` on both machines to sum to exactly **635,921**.

## 4. Central Manifest Inventory Summary
Central manifests have been written under `fiper_ws/data/manifests/fiper_sweep_eternal_20260526_combined/`.

### Key Metrics
- **Total Rows**: 635,921 (Success: 464,321, Failure/Timeout: 171,600)
- **Total Episodes**: 4,221 (Success: 3,649, Failure/Timeout: 572)
- **Episode Length**: Avg: 150.66, Min: 66, Max: 300
- **Corrupt Rows**: 0
- **Missing Required Fields**: 0
- **ACE Candidate Counts**: 8 candidates for all 635,921 rows.
- **ACE Replay Used**: 0 violations (0 instances where `ace_replay_used` was incorrectly set).
- **First-Action Execution Checks**: 635,921 rows checked; 0 mismatches between `executed_action` and the first element of `main_candidate_action_chunk_normalized` (within $1\times 10^{-4}$ tolerance).
- **Seed Diversity**: 635,826 unique main seeds (95 duplicates) and 5,081,284 unique ACE candidate seeds.
- **Exclusion Confirmation**: The task exclusion criteria successfully ignored `libero_10_with_milk` task 3 and task 4. Grep searches verified that no records for task 3 or 4 are present in the raw campaign data.

### Rows by Perturbation Group
- **mug** (`*_with_mug` suites): 159,838 rows
- **milk** (`*_with_milk` and `libero_10_with_milk` suites): 159,892 rows
- **object** (`*_object` suites): 221,191 rows
- **env** (`*_env` suites): 95,000 rows

### Rows by Suite Family
- **spatial** (`libero_spatial_*`): 198,959 rows
- **object_family** (`libero_object_*`): 186,681 rows
- **goal** (`libero_goal_*`): 180,831 rows
- **10_family** (`libero_10_*`): 69,450 rows

## 5. Prepared Experiment Folders and Splits
The prepared experiments directory structure is set up under `fiper_ws/experiments/prepared_20260526/`:

```text
prepared_20260526/
  00_global_main/
  01_ood_task_8_9/
  02_ood_perturbation_holdout_mug/
  02_ood_perturbation_holdout_milk/
  02_ood_perturbation_holdout_object/
  02_ood_perturbation_holdout_env/
  03_ood_suite_family_holdout_spatial/
  03_ood_suite_family_holdout_object_family/
  03_ood_suite_family_holdout_goal/
  03_ood_suite_family_holdout_10_family/
  04_per_perturbation_mug/
  04_per_perturbation_milk/
  04_per_perturbation_object/
  04_per_perturbation_env/
  05_per_suite/
    libero_spatial_with_mug/
    libero_object_with_mug/
    libero_goal_with_mug/
    libero_spatial_with_milk/
    libero_10_with_milk/
    libero_goal_with_milk/
    libero_spatial_object/
    libero_object_object/
    libero_goal_object/
    libero_spatial_env/
    libero_object_env/
    libero_goal_env/
  06_corrupted_action_eval/
  07_final_deployed_global/
```

### Split Definitions & Rules
- **Global Main (`00_global_main`)**:
  - Success splits: `success_train` (70%), `success_calib` (15%), `success_test_id` (15%).
  - Failure splits: `failure_eval_all` (100% failure/timeout episodes).
  - Failure subsets: `early` (first 25%), `mid` (middle 50%), `late` (last 25%), `near_end` (last 50 steps).
- **OOD Task (`01_ood_task_8_9`)**:
  - Unseen task IDs 8 & 9 are excluded from both training and calibration.
  - OOD successes assigned to `success_test_ood`. OOD failures assigned to `failure_eval_ood` and sub-splits.
- **OOD Perturbation (`02_ood_perturbation_holdout_*`)**:
  - Held-out perturbation group is excluded from both training and calibration.
  - Held-out successes/failures assigned to OOD evaluation splits.
- **OOD Suite-Family (`03_ood_suite_family_holdout_*`)**:
  - Held-out suite family is excluded from both training and calibration.
  - Held-out successes/failures assigned to OOD evaluation splits.
- **Per-Perturbation (`04_per_perturbation_*`)**:
  - Special splits containing only data matching the targeted perturbation.
- **Per-Suite (`05_per_suite/*`)**:
  - Isolated split sets for each valid libero suite.
- **Corrupted Action Eval (`06_corrupted_action_eval`)**:
  - Configured with `corruption_config.json` referencing `success_test_id` and action corruption modes.
- **Final Deployed Global (`07_final_deployed_global`)**:
  - Points to the `00_global_main` splits.

### Support & Status
- All suites, families, and groups have sufficient data. No low-support warnings were issued. All experiment configs are marked as `"status": "READY"`.

## 6. Validation Results
The validation suite checks:
1. Disjointness: No episode key is shared across multiple splits (except failure subsets derived from `failure_eval_all`).
2. Outcome constraints: No failure or timeout episode is included in training or calibration.
3. OOD strict boundaries: Unseen groups/tasks/families are completely absent from training/calibration.
4. Positive line numbers and file existence on host.
5. Random sampling (100 rows) verify matching suite, task, and outcome.

**Summary Status**: **PASS** (on both Sam and Bob).

## 7. What Was NOT Done
- **No Model Training**: Model training has not been initialized.
- **No Split Materialization**: Split files under `datasets/materialized/` remain un-materialized to save disk space. They will be materialized on-demand using `materialize_fiper_split.py`.
- **No Data Deletion**: No raw collector campaigns or log files were removed.

## 8. Exact Commands Run
1. To parse datasets and prepare splits on Sam:
   ```bash
   cd /home/rootalkhatib/test/reda_ws/fiper_ws
   source ../asynchvla_ws/scripts/activate_simvla_sam.sh
   python3 scripts/prepare_fiper_experiment_splits.py
   ```
2. To compile all scripts:
   ```bash
   python3 -m py_compile scripts/prepare_fiper_experiment_splits.py scripts/materialize_fiper_split.py scripts/analyze_current_fiper_sweep.py
   ```
3. To run the audit check on Sam:
   ```bash
   python3 scripts/analyze_current_fiper_sweep.py \
     --config configs/current_fiper_sweep_eternal_combined_relative.json \
     --output-dir experiments/audit_only_combined_20260526
   ```
4. To run the audit check on Bob:
   ```bash
   cd "/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
   source ../asynchvla_ws/scripts/activate_simvla_bob.sh
   python3 scripts/analyze_current_fiper_sweep.py \
     --config configs/current_fiper_sweep_eternal_combined_relative.json \
     --output-dir experiments/audit_only_combined_20260526
   ```

## 9. Exact Next Commands for Future Steps
1. **Materialize a Split** (e.g., Global Train split on Sam):
   ```bash
   python3 scripts/materialize_fiper_split.py \
     --ref-rows experiments/prepared_20260526/00_global_main/datasets/refs/success_train.rows.jsonl \
     --output-jsonl experiments/prepared_20260526/00_global_main/datasets/materialized/success_train.jsonl
   ```
2. **Materialize Corrupted Actions**:
   To materialize action corruption test-sets later:
   ```bash
   python3 experiments/prepared_20260526/06_corrupted_action_eval/scripts/materialize_corrupted_action_eval.py
   ```
