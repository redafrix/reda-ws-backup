# Forensic Sanity Audit Report: Step 3 - Pairing Bugcheck

> [!IMPORTANT]
> This is Step 3 of the forensic sanity audit conducted on SimVLA risk-aware simulation results on host **pcrobot**. The audit is strictly read-only; no code, configurations, or simulation data were modified.

## 1. Executive Summary & Verification

We conducted a bottom-up verification of the paired comparison logic using exclusively raw JSONL files.
Our audit confirms:
1. **Raw JSONL Integrity:** There are absolutely no duplicate seeds or episode indices inside any single shard JSONL file. Each shard file contains exactly 50 unique rows.
2. **Shard Disjointness:** Shard 0 and Shard 1 have completely disjoint seed pools (0 overlap). Each policy evaluation contains exactly 100 unique seeds.
3. **Step 2 Report Bug Identified:** The Step 2 report had a manual compilation/hardcoding template error. While the total counts of rescues (19) and regressions (14) for Task 6 Aggressive New TopK8 were correct, the listed seed IDs were wrong and contained overlaps (e.g. `273198307`, `447329467`, `831403058` listed as both rescues and regressions).
4. **Disjointness Confirmed:** Under a clean recomputation directly from the raw JSONLs, the intersection between rescues and regressions is **strictly empty**.

---

## 2. Raw JSONL File Audit

| File Key | Path on `pcrobot` | Rows | Keys count | Unique Seeds | Dup Seeds | Unique Ep Idx | Dup Ep Idx | Stale Rows | Shard Overlap |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `t3_simvla_s0` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/runs/online/task3/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | Overlap: 0 |
| `t3_simvla_s1` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/runs/online/task3/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | N/A |
| `t3_risk_s0` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608/runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | Overlap: 0 |
| `t3_risk_s1` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608/runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | N/A |
| `t6_simvla_s0` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/runs/online/task6/modified_simvla/shard_0/simvla_only/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | Overlap: 0 |
| `t6_simvla_s1` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/runs/online/task6/modified_simvla/shard_1/simvla_only/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | N/A |
| `t6_risk_s0` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | Overlap: 0 |
| `t6_risk_s1` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | N/A |
| `t6_old_s0` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608/runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | Overlap: 0 |
| `t6_old_s1` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608/runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8/episode_summaries.jsonl` | 50 | 31 | 50 | 0 | 50 | 0 | NO | N/A |


### Keys Available in Raw Row:
* `action_modifications_count`
* `episode_index`
* `episode_uid`
* `error_message`
* `execution_horizon`
* `first_modification_timestep`
* `last_modification_timestep`
* `main_seed_collisions_with_ace`
* `num_queries`
* `num_steps`
* `outcome`
* `policy`
* `proposed_action_modifications_count`
* `reset_seed`
* `risk_model_dir`
* `risk_score_max`
* `risk_score_mean`
* `risk_score_min`
* `risk_static_dim`
* `schema_version`
* `seed_collisions`
* `selected_risk_max`
* `selected_risk_mean`
* `selected_risk_min`
* `selected_uncertainty_dims`
* `success`
* `suite`
* `task_id`
* `terminal_done`
* `updated_at`
* `wall_time_seconds`

---

## 3. Recomputed Paired Comparisons

### Task 3 Aggressive New TopK8 vs Baseline

* **Shared keys count:** 100
* **Baseline-only keys count:** 0
* **Risk-only keys count:** 0
* **Shared success count:** 17
* **Shared failure count:** 81
* **Rescues count:** 2
* **Regressions count:** 0
* **Net gain:** 2
* **Final baseline success count:** 17
* **Final risk success count:** 19
* **Disjointness validation:** PASS (Rescue intersect Regression empty: True)

#### Rescues List:

| Reset Seed | Baseline Shard | Risk Shard | Base Success | Risk Success | Base Steps | Risk Steps | Mods count | Modified Chunk Indices |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 211088021 | shard_1 | shard_1 | False | True | 300 | 232 | 5 | 12, 13, 14, 15, 17 |
| 923894520 | shard_0 | shard_0 | False | True | 300 | 209 | 2 | 14, 16 |

#### Regressions List:

*None*


### Task 6 Aggressive New TopK8 vs Baseline

* **Shared keys count:** 100
* **Baseline-only keys count:** 0
* **Risk-only keys count:** 0
* **Shared success count:** 43
* **Shared failure count:** 24
* **Rescues count:** 19
* **Regressions count:** 14
* **Net gain:** 5
* **Final baseline success count:** 57
* **Final risk success count:** 62
* **Disjointness validation:** PASS (Rescue intersect Regression empty: True)

#### Rescues List:

| Reset Seed | Baseline Shard | Risk Shard | Base Success | Risk Success | Base Steps | Risk Steps | Mods count | Modified Chunk Indices |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 273198307 | shard_0 | shard_0 | False | True | 300 | 89 | 3 | 3, 4, 6 |
| 287547146 | shard_1 | shard_1 | False | True | 300 | 101 | 5 | 0, 1, 3, 6, 8 |
| 287639521 | shard_0 | shard_0 | False | True | 300 | 97 | 5 | 0, 2, 3, 6, 8 |
| 352560642 | shard_0 | shard_0 | False | True | 300 | 179 | 4 | 6, 7, 8, 17 |
| 368480630 | shard_0 | shard_0 | False | True | 300 | 90 | 6 | 0, 1, 3, 4, 7, 8 |
| 386737046 | shard_1 | shard_1 | False | True | 300 | 97 | 6 | 0, 1, 4, 6, 7, 9 |
| 430862118 | shard_1 | shard_1 | False | True | 300 | 90 | 3 | 1, 2, 7 |
| 448048899 | shard_0 | shard_0 | False | True | 300 | 88 | 3 | 1, 2, 4 |
| 767279481 | shard_1 | shard_1 | False | True | 300 | 127 | 3 | 0, 1, 3 |
| 1173749532 | shard_0 | shard_0 | False | True | 300 | 169 | 3 | 0, 1, 4 |
| 1291487306 | shard_1 | shard_1 | False | True | 300 | 262 | 4 | 0, 7, 8, 10 |
| 1345465790 | shard_1 | shard_1 | False | True | 300 | 96 | 7 | 0, 1, 2, 3, 4, 5, 8 |
| 1481978104 | shard_0 | shard_0 | False | True | 300 | 210 | 10 | 0, 2, 3, 4, 5, 7, 8, 12, 14, 15 |
| 1501306169 | shard_0 | shard_0 | False | True | 300 | 154 | 4 | 1, 3, 8, 10 |
| 1546683890 | shard_0 | shard_0 | False | True | 300 | 84 | 7 | 0, 1, 2, 3, 4, 5, 6 |
| 1717619211 | shard_1 | shard_1 | False | True | 300 | 174 | 1 | 1 |
| 1720788673 | shard_0 | shard_0 | False | True | 300 | 114 | 6 | 1, 7, 8, 9, 10, 11 |
| 2038011754 | shard_0 | shard_0 | False | True | 300 | 108 | 4 | 4, 6, 8, 10 |
| 2060901849 | shard_0 | shard_0 | False | True | 300 | 263 | 4 | 0, 2, 3, 4 |

#### Regressions List:

| Reset Seed | Baseline Shard | Risk Shard | Base Success | Risk Success | Base Steps | Risk Steps | Mods count | Modified Chunk Indices |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 57394074 | shard_0 | shard_0 | True | False | 96 | 300 | 12 | 1, 2, 3, 6, 7, 8, 9, 10, 12, 13, 14, 19 |
| 143160192 | shard_1 | shard_1 | True | False | 183 | 300 | 9 | 2, 3, 4, 5, 8, 9, 11, 12, 13 |
| 212142211 | shard_0 | shard_0 | True | False | 121 | 300 | 4 | 0, 1, 3, 6 |
| 286956518 | shard_0 | shard_0 | True | False | 92 | 300 | 2 | 3, 4 |
| 305916219 | shard_1 | shard_1 | True | False | 95 | 300 | 4 | 0, 1, 2, 11 |
| 402897139 | shard_0 | shard_0 | True | False | 169 | 300 | 1 | 0 |
| 438935613 | shard_0 | shard_0 | True | False | 188 | 300 | 5 | 3, 8, 10, 11, 13 |
| 740482034 | shard_0 | shard_0 | True | False | 92 | 300 | 14 | 0, 2, 5, 8, 9, 10, 11, 13, 14, 15, 19, 21, 22, 24 |
| 831403058 | shard_0 | shard_0 | True | False | 205 | 300 | 2 | 0, 1 |
| 834120148 | shard_0 | shard_0 | True | False | 95 | 300 | 5 | 1, 3, 6, 7, 21 |
| 996418799 | shard_1 | shard_1 | True | False | 240 | 300 | 7 | 0, 2, 4, 11, 12, 14, 15 |
| 1505471023 | shard_0 | shard_0 | True | False | 95 | 300 | 2 | 0, 1 |
| 1557548213 | shard_0 | shard_0 | True | False | 135 | 300 | 4 | 0, 3, 4, 7 |
| 2078809338 | shard_1 | shard_1 | True | False | 91 | 300 | 5 | 1, 2, 3, 5, 9 |


### Task 6 Aggressive Old Detector vs Baseline

* **Shared keys count:** 100
* **Baseline-only keys count:** 0
* **Risk-only keys count:** 0
* **Shared success count:** 47
* **Shared failure count:** 30
* **Rescues count:** 13
* **Regressions count:** 10
* **Net gain:** 3
* **Final baseline success count:** 57
* **Final risk success count:** 60
* **Disjointness validation:** PASS (Rescue intersect Regression empty: True)

#### Rescues List:

| Reset Seed | Baseline Shard | Risk Shard | Base Success | Risk Success | Base Steps | Risk Steps | Mods count | Modified Chunk Indices |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 287639521 | shard_0 | shard_0 | False | True | 300 | 98 | 3 | 1, 5, 6 |
| 368480630 | shard_0 | shard_0 | False | True | 300 | 107 | 3 | 0, 8, 9 |
| 375394911 | shard_1 | shard_1 | False | True | 300 | 135 | 3 | 0, 1, 13 |
| 386737046 | shard_1 | shard_1 | False | True | 300 | 100 | 3 | 0, 1, 9 |
| 392453968 | shard_1 | shard_1 | False | True | 300 | 91 | 3 | 1, 8, 9 |
| 430862118 | shard_1 | shard_1 | False | True | 300 | 149 | 4 | 1, 12, 13, 14 |
| 1142167292 | shard_0 | shard_0 | False | True | 300 | 92 | 3 | 1, 5, 9 |
| 1277227977 | shard_0 | shard_0 | False | True | 300 | 131 | 5 | 1, 8, 9, 10, 11 |
| 1291487306 | shard_1 | shard_1 | False | True | 300 | 147 | 5 | 10, 11, 12, 13, 14 |
| 1501306169 | shard_0 | shard_0 | False | True | 300 | 175 | 7 | 0, 1, 11, 12, 13, 15, 16 |
| 1546683890 | shard_0 | shard_0 | False | True | 300 | 214 | 9 | 0, 1, 9, 10, 15, 16, 17, 18, 21 |
| 2060901849 | shard_0 | shard_0 | False | True | 300 | 258 | 8 | 1, 8, 9, 10, 11, 12, 18, 22 |
| 2118586852 | shard_1 | shard_1 | False | True | 300 | 136 | 5 | 0, 2, 6, 7, 13 |

#### Regressions List:

| Reset Seed | Baseline Shard | Risk Shard | Base Success | Risk Success | Base Steps | Risk Steps | Mods count | Modified Chunk Indices |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 47766804 | shard_1 | shard_1 | True | False | 98 | 300 | 10 | 0, 1, 8, 9, 10, 11, 12, 13, 15, 28 |
| 109459806 | shard_0 | shard_0 | True | False | 243 | 300 | 7 | 0, 9, 10, 12, 20, 21, 26 |
| 286956518 | shard_0 | shard_0 | True | False | 92 | 300 | 10 | 0, 7, 8, 10, 11, 12, 13, 14, 25, 26 |
| 402897139 | shard_0 | shard_0 | True | False | 169 | 300 | 8 | 0, 5, 8, 11, 12, 13, 17, 19 |
| 468260798 | shard_1 | shard_1 | True | False | 95 | 300 | 9 | 1, 9, 10, 11, 12, 13, 14, 20, 21 |
| 684664532 | shard_0 | shard_0 | True | False | 211 | 300 | 10 | 0, 1, 6, 11, 14, 18, 21, 22, 23, 24 |
| 996418799 | shard_1 | shard_1 | True | False | 240 | 300 | 11 | 0, 1, 8, 11, 12, 13, 14, 15, 17, 18, 19 |
| 1165183492 | shard_0 | shard_0 | True | False | 283 | 300 | 11 | 1, 5, 12, 13, 15, 16, 17, 18, 19, 20, 26 |
| 2007355477 | shard_1 | shard_1 | True | False | 246 | 300 | 10 | 1, 10, 15, 18, 19, 20, 21, 23, 25, 26 |
| 2078809338 | shard_1 | shard_1 | True | False | 91 | 300 | 7 | 0, 1, 8, 10, 11, 14, 15 |



---

## 4. Step 2 Pairing Bug Diagnosis & Cause

* **STEP2_PAIRED_ANALYSIS_CORRECT = NO**
* **Bug Cause:** The analysis scripts themselves (like `extract_fragility_details.py` and `calculate_rescues_remote.py`) were correct and computed the exact correct numbers (19 rescues and 14 regressions for the new detector, 13 rescues and 10 regressions for the old detector). However, during the compilation of the Step 2 report via `generate_step2_report.py`, the author manually entered/hardcoded an incorrect list of seeds for the new detector Task 6 rescues and regressions.
* **Mixed seeds source:** The incorrect lists in Step 2 included some seeds from the old detector's runs and some seeds that merely had interventions (modification counts > 0) but were shared successes/failures rather than actual rescues or regressions.

---

## 5. Audit Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
RAW_JSONL_ONLY = YES
TASK3_PAIRING_TRUSTWORTHY = YES
TASK6_NEW_TOPK8_PAIRING_TRUSTWORTHY = YES
TASK6_OLD_TOPK8_PAIRING_TRUSTWORTHY = YES
STEP2_PAIRED_ANALYSIS_CORRECT = NO
DUPLICATE_SEEDS_FOUND = NO
RESCUE_REGRESSION_INTERSECTION_EMPTY = YES
CORRECTED_TASK3_NET_GAIN = 2
CORRECTED_TASK6_NEW_TOPK8_NET_GAIN = 5
CORRECTED_TASK6_OLD_TOPK8_NET_GAIN = 3
MOST_IMPORTANT_FINDING = The Step 2 report had a manual hardcoding template error that listed incorrect seed IDs, but the raw JSONL data is clean with zero duplicates or overlap between rescues and regressions.
NEXT_AUDIT_STEP = Audit zero-shot generalization on held-out tasks (e.g. Tasks 8 and 9) using the ood_last2_taskids_full detector split.
