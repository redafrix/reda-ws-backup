# FIPER Target-Object Pick-Basket Splits Sync & Validation Report

**Date:** 2026-05-26  
**Project:** Stage 9 / LIBERO-PRO / SimVLA / FIPER monitor  
**Sam Workspace:** `/home/rootalkhatib/test/reda_ws/fiper_ws`  
**Bob Workspace:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`  

---

## 1. Executive Summary & Context

This audit independent verification was conducted to validate the leave-two-target-objects-out (LOTO) splits constructed by Codex on the Sam and Bob nodes. 

### What Codex Created:
- **Build Script:** [build_target_object_pick_basket_splits_v1.py](file:///home/redafrix/tests/internship/fiper_ws/scripts/build_target_object_pick_basket_splits_v1.py)
  - Targets the object-family pick-and-place-in-basket tasks from suites `libero_object_env`, `libero_object_object`, and `libero_object_with_mug`.
  - Parses actual picked target object labels directly from task instructions via regular expression matching.
  - Automatically structures five leave-two-target-objects-out benchmark folds.
- **Root Output Directory:** `experiments/prepared_20260526/08_target_object_pick_basket_loto_v1/`
- **Benchmark Fold Report:** [FIPER_TARGET_OBJECT_PICK_BASKET_SPLITS_V1_REPORT.md](file:///home/redafrix/tests/internship/fiper_ws/reports/FIPER_TARGET_OBJECT_PICK_BASKET_SPLITS_V1_REPORT.md)

### Important Limitations:
> [!IMPORTANT]
> This is a **TARGET_OBJECT_OOD** benchmark, not a true object-only same-task Same-Instruction OOD, because in the LIBERO dataset, the `task_id` is structurally tied to the object identity (e.g. changing the target object from butter to chocolate pudding changes the `task_id`). However, this represents the highest-fidelity picked-object identity OOD possible from existing trajectories.

---

## 2. Independent Validation Results

We wrote and executed a dedicated validation script [validate_target_object_splits.py](file:///home/redafrix/tests/internship/fiper_ws/scripts/validate_target_object_splits.py) to audit the generated splits.

### Sam Validation Results:
- **Pass Status:** **PASS**
- **Ref File Verification:** All files (`.rows.jsonl` and `.episodes.jsonl` for all 8 splits per fold) exist and are complete.
- **Leakage Check:** Passed. Verified that no held-out objects are leaked into the `seen` splits (`success_train_seen`, `success_calib_seen`, `success_test_seen`, `failure_eval_seen`) and that `ood` splits contain exclusively the held-out target objects.
- **Split Disjointness:** Passed. Episode partitions between train, calib, test, and OOD evaluations are strictly disjoint.
- **Row/Episode Consistency:** Passed. Verified that the sum of episodes' `num_rows` matches the row file count exactly.

### Bob Validation Results:
- **Pass Status:** **PASS**
- **Ref File Verification:** All folder structures and files exist on `pcrobot` under `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/prepared_20260526/08_target_object_pick_basket_loto_v1/` and match Sam's properties exactly.
- **Leakage Check:** Passed.
- **Split Disjointness:** Passed.
- **Row/Episode Consistency:** Passed.

### Synchronicity and Hash Verification:
We computed SHA256 hashes of all critical files on both Sam and Bob:

| File Name / Path | Sam SHA256 Hash | Bob SHA256 Hash | Status |
|---|---|---|:---:|
| `scripts/build_target_object_pick_basket_splits_v1.py` | `be3beb413f56b53c4e5a689833251d109a39f0d9954d0367bdd4c8f4e8d1c527` | `be3beb413f56b53c4e5a689833251d109a39f0d9954d0367bdd4c8f4e8d1c527` | **MATCH** |
| `reports/FIPER_TARGET_OBJECT_PICK_BASKET_SPLITS_V1_REPORT.md` | `47e2f48fab8ae8d1d798ad89b403fbc436ab4dbd741aa4a1e198f618c0f4c444` | `47e2f48fab8ae8d1d798ad89b403fbc436ab4dbd741aa4a1e198f618c0f4c444` | **MATCH** |
| `TARGET_OBJECT_LOTO_REGISTRY.json` | `6c7f273c7b076dfae3fb520375db2baaeda19a1238bbd992a802519a7eeef26e` | `6c7f273c7b076dfae3fb520375db2baaeda19a1238bbd992a802519a7eeef26e` | **MATCH** |
| `TARGET_OBJECT_LOTO_SUMMARY.json` | `b7513b244f4488da8eeed703eda7c6dc39670e149619d49fc6b04084ac0ad91a` | `b7513b244f4488da8eeed703eda7c6dc39670e149619d49fc6b04084ac0ad91a` | **MATCH** |

Both nodes are in **100% perfect sync**.

---

## 3. Leave-Two-Objects-Out Folds Inventory

Below is the verified summary of splits, row, and episode distributions across the five folds:

| Fold | Held-Out Objects | Status | Train Task IDs | OOD Task IDs | Train Success (Ep/Rows) | Calib Success (Ep/Rows) | Seen Test Success (Ep/Rows) | OOD Success (Ep/Rows) | OOD Failure (Ep/Rows) |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| `fold_00` | `alphabet_soup`, `bbq_sauce` | `READY_STRONG` | `1,2,3,4,5,6,7,8,9` | `0,1,3` | `547 / 83,065` | `118 / 17,385` | `115 / 17,893` | `186 / 30,838` | `33 / 9,900` |
| `fold_01` | `butter`, `chocolate_pudding` | `READY_STRONG` | `0,1,2,3,4,5,6,7,8,9` | `2,3,6,8` | `549 / 82,151` | `118 / 17,334` | `116 / 17,570` | `183 / 32,126` | `35 / 10,500` |
| `fold_02` | `cream_cheese`, `ketchup` | `READY_STRONG` | `0,1,2,3,5,6,7,8,9` | `1,4,5` | `542 / 82,068` | `116 / 17,107` | `116 / 18,062` | `192 / 31,944` | `26 / 7,800` |
| `fold_03` | `milk`, `orange_juice` | `READY_STRONG` | `0,1,2,3,4,5,6,8,9` | `6,7,9` | `539 / 86,597` | `115 / 18,097` | `116 / 19,176` | `196 / 25,311` | `22 / 6,600` |
| `fold_04` | `salad_dressing`, `tomato_sauce` | `LOW_OOD_FAILURE_SUPPORT` | `0,1,2,3,4,5,6,7,8,9` | `2,5,8,9` | `531 / 84,427` | `113 / 17,485` | `113 / 18,307` | `209 / 28,962` | `9 / 2,700` |

### Support Classifications:
- **Strong Folds (`READY_STRONG`):** `fold_00`, `fold_01`, `fold_02`, `fold_03`. These have high OOD evaluation failure episode counts (>= 20), providing stable statistics for failure detection metric calculations.
- **Low Support Fold (`LOW_OOD_FAILURE_SUPPORT`):** `fold_04` is labeled low support due to having only 9 failure episodes in its OOD eval split.

---

## 4. Recommended Next Steps & Training Commands

The recommended fold for the first training campaign is **`fold_01_holdout_butter_chocolate_pudding`**, because it maximizes training task coverage (includes all 10 tasks in train) and contains the largest OOD failure evaluation support (35 episodes).

### Next Training Command (DO NOT RUN YET):
```bash
cd /home/rootalkhatib/test/reda_ws/fiper_ws
source ../asynchvla_ws/scripts/activate_simvla_sam.sh

python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/fiper_target_object_pick_basket_fold_01_holdout_butter_chocolate_pudding_loaderfix_20260526 \
  --refs-dir experiments/prepared_20260526/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs \
  --train-split success_train_seen \
  --calib-split success_calib_seen \
  --success-eval-splits success_test_seen success_test_ood \
  --failure-eval-splits failure_eval_seen failure_eval_ood failure_eval_ood_late failure_eval_ood_near_end \
  --device cuda \
  --epochs 20 \
  --batch-size 256 \
  --seed 42 \
  --report-name FIPER_TARGET_OBJECT_PICK_BASKET_FOLD_01_HOLDOUT_BUTTER_CHOCOLATE_PUDDING_REPORT.md
```

---

## 5. Final Key Fields

```text
TARGET_OBJECT_OOD_SPLITS_CREATED = YES
SAM_VALIDATION_PASS = YES
BOB_VALIDATION_PASS = YES
READY_STRONG_FOLDS = fold_00_holdout_alphabet_soup_bbq_sauce, fold_01_holdout_butter_chocolate_pudding, fold_02_holdout_cream_cheese_ketchup, fold_03_holdout_milk_orange_juice
LOW_SUPPORT_FOLDS = fold_04_holdout_salad_dressing_tomato_sauce
READY_TO_TRAIN_FIRST_TARGET_OBJECT_OOD_FOLD = YES
RECOMMENDED_FIRST_FOLD = fold_01_holdout_butter_chocolate_pudding
DO_NOT_USE_AS_TRUE_SAME_TASK_OBJECT_ONLY_OOD = YES
```
