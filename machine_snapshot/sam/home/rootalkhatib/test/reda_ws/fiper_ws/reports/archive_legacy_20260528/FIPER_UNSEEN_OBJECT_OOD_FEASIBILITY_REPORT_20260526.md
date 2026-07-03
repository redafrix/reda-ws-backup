# FIPER Unseen Object OOD Feasibility Report

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
| `current.task_context.goal_base` | 15 | plate_2, wooden_cabinet_1_cabinet_middle, akita_black_bowl_2_main, flat_stove_1_burner, basket_1 | True | True | YES |
| `current.task_context.goal_body_prefix` | 15 | plate_2, wooden_cabinet_1_cabinet_middle, akita_black_bowl_2_main, flat_stove_1_burner, basket_1 | True | True | YES |
| `current.task_context.target_base` | 21 | akita_black_bowl_1, desk_caddy_1_main, flat_stove_1_burner_plate, bbq_sauce_1, moka_pot_2 | True | True | YES |
| `current.task_context.target_body_prefix` | 21 | akita_black_bowl_1, desk_caddy_1_main, flat_stove_1_burner_plate, bbq_sauce_1, moka_pot_2 | True | True | YES |
| `current.task_context.task_language` | 63 | put the white mug on the left plate and put the yellow and white mug on the right plate, pick the akita black bowl in the top layer of the wooden cabinet and place it on the plate, open the top layer of the drawer and put the bowl inside, pick the milk and place it in the basket, put the wine bottle on top of the cabinet | True | True | NO |
| `task_id` | 10 | 0, 1, 2, 3, 4 | True | False | NO |
| `task_instruction` | 63 | put the white mug on the left plate and put the yellow and white mug on the right plate, pick the akita black bowl in the top layer of the wooden cabinet and place it on the plate, open the top layer of the drawer and put the bowl inside, pick the milk and place it in the basket, put the wine bottle on top of the cabinet | True | True | NO |

---

## 3. Same-task proxy matching matrix

Since true object identity is not available, we report the proxy matrix: `task_id × suite × perturbation_group × outcome` showing success/failure episode and row counts for each cell:

| Task ID | Suite | Perturbation Group | Success Episodes | Failure Episodes | Total Rows |
|---|---|---|---:|---:|---:|
| `0` | `libero_10_with_milk` | `milk` | 29 | 4 | 6523 |
| `0` | `libero_goal_env` | `env` | 28 | 10 | 7438 |
| `0` | `libero_goal_object` | `object` | 24 | 13 | 7338 |
| `0` | `libero_goal_with_milk` | `milk` | 20 | 13 | 6947 |
| `0` | `libero_goal_with_mug` | `mug` | 23 | 11 | 6417 |
| `0` | `libero_object_env` | `object` | 27 | 11 | 8139 |
| `0` | `libero_object_object` | `object` | 30 | 7 | 7636 |
| `0` | `libero_object_with_mug` | `object` | 26 | 9 | 7140 |
| `0` | `libero_spatial_env` | `env` | 39 | 0 | 2938 |
| `0` | `libero_spatial_object` | `object` | 38 | 0 | 2865 |
| `0` | `libero_spatial_with_milk` | `milk` | 34 | 0 | 3021 |
| `0` | `libero_spatial_with_mug` | `mug` | 23 | 12 | 6383 |
| `1` | `libero_10_with_milk` | `milk` | 0 | 33 | 9900 |
| `1` | `libero_goal_env` | `env` | 35 | 3 | 3809 |
| `1` | `libero_goal_object` | `object` | 33 | 4 | 3992 |
| `1` | `libero_goal_with_milk` | `milk` | 31 | 2 | 6351 |
| `1` | `libero_goal_with_mug` | `mug` | 30 | 4 | 3854 |
| `1` | `libero_object_env` | `object` | 26 | 12 | 8638 |
| `1` | `libero_object_object` | `object` | 28 | 9 | 8042 |
| `1` | `libero_object_with_mug` | `object` | 33 | 1 | 5277 |
| `1` | `libero_spatial_env` | `env` | 38 | 1 | 4706 |
| `1` | `libero_spatial_object` | `object` | 38 | 0 | 4330 |
| `1` | `libero_spatial_with_milk` | `milk` | 33 | 1 | 3512 |
| `1` | `libero_spatial_with_mug` | `mug` | 32 | 3 | 4750 |
| `2` | `libero_10_with_milk` | `milk` | 9 | 24 | 9487 |
| `2` | `libero_goal_env` | `env` | 33 | 5 | 4714 |
| `2` | `libero_goal_object` | `object` | 30 | 7 | 5012 |
| `2` | `libero_goal_with_milk` | `milk` | 31 | 2 | 4144 |
| `2` | `libero_goal_with_mug` | `mug` | 29 | 5 | 4110 |
| `2` | `libero_object_env` | `object` | 36 | 2 | 5999 |
| `2` | `libero_object_object` | `object` | 33 | 4 | 6338 |
| `2` | `libero_object_with_mug` | `object` | 13 | 21 | 8702 |
| `2` | `libero_spatial_env` | `env` | 38 | 0 | 3537 |
| `2` | `libero_spatial_object` | `object` | 38 | 0 | 3739 |
| `2` | `libero_spatial_with_milk` | `milk` | 27 | 7 | 5917 |
| `2` | `libero_spatial_with_mug` | `mug` | 35 | 0 | 4011 |
| `3` | `libero_goal_env` | `env` | 34 | 4 | 7414 |
| `3` | `libero_goal_object` | `object` | 31 | 6 | 7538 |
| `3` | `libero_goal_with_milk` | `milk` | 32 | 1 | 3233 |
| `3` | `libero_goal_with_mug` | `mug` | 29 | 5 | 6947 |
| `3` | `libero_object_env` | `object` | 36 | 2 | 6334 |
| `3` | `libero_object_object` | `object` | 34 | 3 | 6212 |
| `3` | `libero_object_with_mug` | `object` | 25 | 9 | 7463 |
| `3` | `libero_spatial_env` | `env` | 38 | 0 | 3191 |
| `3` | `libero_spatial_object` | `object` | 38 | 0 | 3147 |
| `3` | `libero_spatial_with_milk` | `milk` | 34 | 0 | 3784 |
| `3` | `libero_spatial_with_mug` | `mug` | 35 | 0 | 3095 |
| `4` | `libero_goal_env` | `env` | 38 | 0 | 3223 |
| `4` | `libero_goal_object` | `object` | 37 | 0 | 3192 |
| `4` | `libero_goal_with_milk` | `milk` | 32 | 1 | 2993 |
| `4` | `libero_goal_with_mug` | `mug` | 34 | 0 | 2895 |
| `4` | `libero_object_env` | `object` | 37 | 1 | 5856 |
| `4` | `libero_object_object` | `object` | 36 | 1 | 5687 |
| `4` | `libero_object_with_mug` | `object` | 31 | 3 | 6368 |
| `4` | `libero_spatial_env` | `env` | 36 | 2 | 5083 |
| `4` | `libero_spatial_object` | `object` | 35 | 3 | 5493 |
| `4` | `libero_spatial_with_milk` | `milk` | 32 | 2 | 4227 |
| `4` | `libero_spatial_with_mug` | `mug` | 34 | 1 | 4901 |
| `5` | `libero_10_with_milk` | `milk` | 28 | 5 | 7672 |
| `5` | `libero_goal_env` | `env` | 37 | 1 | 5291 |
| `5` | `libero_goal_object` | `object` | 37 | 0 | 5006 |
| `5` | `libero_goal_with_milk` | `milk` | 32 | 1 | 3238 |
| `5` | `libero_goal_with_mug` | `mug` | 34 | 0 | 4326 |
| `5` | `libero_object_env` | `object` | 38 | 0 | 5080 |
| `5` | `libero_object_object` | `object` | 37 | 0 | 4933 |
| `5` | `libero_object_with_mug` | `object` | 34 | 0 | 5153 |
| `5` | `libero_spatial_env` | `env` | 7 | 31 | 10594 |
| `5` | `libero_spatial_object` | `object` | 3 | 35 | 10972 |
| `5` | `libero_spatial_with_milk` | `milk` | 33 | 1 | 4066 |
| `5` | `libero_spatial_with_mug` | `mug` | 7 | 28 | 9466 |
| `6` | `libero_10_with_milk` | `milk` | 11 | 22 | 9386 |
| `6` | `libero_goal_env` | `env` | 38 | 0 | 3427 |
| `6` | `libero_goal_object` | `object` | 36 | 1 | 3629 |
| `6` | `libero_goal_with_milk` | `milk` | 26 | 7 | 4751 |
| `6` | `libero_goal_with_mug` | `mug` | 28 | 6 | 4623 |
| `6` | `libero_object_env` | `object` | 35 | 3 | 7236 |
| `6` | `libero_object_object` | `object` | 36 | 1 | 7021 |
| `6` | `libero_object_with_mug` | `object` | 19 | 15 | 7391 |
| `6` | `libero_spatial_env` | `env` | 38 | 0 | 3915 |
| `6` | `libero_spatial_object` | `object` | 38 | 0 | 3925 |
| `6` | `libero_spatial_with_milk` | `milk` | 32 | 1 | 3488 |
| `6` | `libero_spatial_with_mug` | `mug` | 35 | 0 | 3903 |
| `7` | `libero_10_with_milk` | `milk` | 18 | 15 | 8921 |
| `7` | `libero_goal_env` | `env` | 38 | 0 | 2692 |
| `7` | `libero_goal_object` | `object` | 37 | 0 | 2695 |
| `7` | `libero_goal_with_milk` | `milk` | 33 | 0 | 4676 |
| `7` | `libero_goal_with_mug` | `mug` | 34 | 0 | 2491 |
| `7` | `libero_object_env` | `object` | 38 | 0 | 5061 |
| `7` | `libero_object_object` | `object` | 34 | 3 | 5471 |
| `7` | `libero_object_with_mug` | `object` | 30 | 4 | 4975 |
| `7` | `libero_spatial_env` | `env` | 36 | 2 | 5995 |
| `7` | `libero_spatial_object` | `object` | 37 | 1 | 5889 |
| `7` | `libero_spatial_with_milk` | `milk` | 2 | 31 | 9515 |
| `7` | `libero_spatial_with_mug` | `mug` | 25 | 10 | 7286 |
| `8` | `libero_10_with_milk` | `milk` | 23 | 10 | 8922 |
| `8` | `libero_goal_env` | `env` | 36 | 2 | 3553 |
| `8` | `libero_goal_object` | `object` | 34 | 3 | 3621 |
| `8` | `libero_goal_with_milk` | `milk` | 31 | 2 | 3745 |
| `8` | `libero_goal_with_mug` | `mug` | 34 | 0 | 3049 |
| `8` | `libero_object_env` | `object` | 38 | 0 | 6156 |
| `8` | `libero_object_object` | `object` | 36 | 1 | 6048 |
| `8` | `libero_object_with_mug` | `object` | 32 | 2 | 4464 |
| `8` | `libero_spatial_env` | `env` | 37 | 1 | 3596 |
| `8` | `libero_spatial_object` | `object` | 36 | 1 | 3502 |
| `8` | `libero_spatial_with_milk` | `milk` | 29 | 4 | 5987 |
| `8` | `libero_spatial_with_mug` | `mug` | 22 | 13 | 6261 |
| `9` | `libero_10_with_milk` | `milk` | 24 | 9 | 8639 |
| `9` | `libero_goal_env` | `env` | 36 | 2 | 5349 |
| `9` | `libero_goal_object` | `object` | 32 | 5 | 6025 |
| `9` | `libero_goal_with_milk` | `milk` | 33 | 0 | 2372 |
| `9` | `libero_goal_with_mug` | `mug` | 34 | 0 | 4711 |
| `9` | `libero_object_env` | `object` | 38 | 0 | 4564 |
| `9` | `libero_object_object` | `object` | 37 | 0 | 4449 |
| `9` | `libero_object_with_mug` | `object` | 33 | 1 | 4848 |
| `9` | `libero_spatial_env` | `env` | 37 | 1 | 4535 |
| `9` | `libero_spatial_object` | `object` | 36 | 1 | 4381 |
| `9` | `libero_spatial_with_milk` | `milk` | 30 | 3 | 4475 |
| `9` | `libero_spatial_with_mug` | `mug` | 32 | 3 | 4578 |

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
- **Train success episodes/rows:** `1848 / 237336`
- **Calib success episodes/rows:** `396 / 51025`
- **Eval success episodes/rows:** `1009 / 125428` (success_test_ood)
- **Eval failure episodes/rows:** `109 / 32700` (failure_eval_ood)
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
- **Train success episodes/rows:** `1848 / 237336`
- **Calib success episodes/rows:** `396 / 51025`
- **Eval success episodes/rows:** `1009 / 125428`
- **Eval failure episodes/rows:** `109 / 32700`
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
