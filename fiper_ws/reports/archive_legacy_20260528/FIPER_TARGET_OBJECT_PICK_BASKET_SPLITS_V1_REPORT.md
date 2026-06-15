# FIPER Target-Object Pick-Basket Split Report

## Executive Summary

Created a real picked-object identity OOD benchmark from existing data. This is not perturbation-group OOD.

The benchmark is restricted to object-family pick/place-in-basket tasks, where the instruction template, suite family, and goal container are as matched as current data allows:

- Suites: `libero_object_env`, `libero_object_object`, `libero_object_with_mug`
- Template: `pick [target object] and place it in the basket`
- OOD axis: held-out actual picked object label extracted from instruction text

Limitation: task_id changes with object identity in LIBERO, so this is TARGET_OBJECT_OOD, not perfectly same-task same-instruction object-only OOD.

## Dataset Inventory

- Raw rows scanned: `635921`
- Pick-basket rows used: `186681`
- Pick-basket episodes used: `1091`
- Target object labels: `alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, ketchup, milk, orange_juice, salad_dressing, tomato_sauce`

## Target Object Coverage

| Target Object | Success Episodes | Failure Episodes | Rows | Suites | Task IDs |
|---|---:|---:|---:|---|---|
| `alphabet_soup` | 83 | 27 | 22915 | `libero_object_env;libero_object_object;libero_object_with_mug` | `0` |
| `bbq_sauce` | 103 | 6 | 17823 | `libero_object_env;libero_object_object;libero_object_with_mug` | `1;3` |
| `butter` | 84 | 25 | 22959 | `libero_object_env;libero_object_object;libero_object_with_mug` | `2;6` |
| `chocolate_pudding` | 99 | 10 | 19667 | `libero_object_env;libero_object_object;libero_object_with_mug` | `3;8` |
| `cream_cheese` | 85 | 24 | 23048 | `libero_object_env;libero_object_object;libero_object_with_mug` | `1;4` |
| `ketchup` | 107 | 2 | 16696 | `libero_object_env;libero_object_object;libero_object_with_mug` | `4;5` |
| `milk` | 91 | 18 | 17923 | `libero_object_env;libero_object_object;libero_object_with_mug` | `6;7` |
| `orange_juice` | 105 | 4 | 13988 | `libero_object_env;libero_object_object;libero_object_with_mug` | `7;9` |
| `salad_dressing` | 101 | 8 | 16801 | `libero_object_env;libero_object_object;libero_object_with_mug` | `2;8` |
| `tomato_sauce` | 108 | 1 | 14861 | `libero_object_env;libero_object_object;libero_object_with_mug` | `5;9` |

## Leave-Two-Objects-Out Folds

| Fold | Held-Out Objects | Status | Train Task IDs | OOD Task IDs | Train Success Ep/Rows | Calib Success Ep/Rows | Seen Test Success Ep/Rows | OOD Success Ep/Rows | OOD Failure Ep/Rows |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| `fold_00_holdout_alphabet_soup_bbq_sauce` | `alphabet_soup, bbq_sauce` | `READY_STRONG` | `1,2,3,4,5,6,7,8,9` | `0,1,3` | 547/83065 | 118/17385 | 115/17893 | 186/30838 | 33/9900 |
| `fold_01_holdout_butter_chocolate_pudding` | `butter, chocolate_pudding` | `READY_STRONG` | `0,1,2,3,4,5,6,7,8,9` | `2,3,6,8` | 549/82151 | 118/17334 | 116/17570 | 183/32126 | 35/10500 |
| `fold_02_holdout_cream_cheese_ketchup` | `cream_cheese, ketchup` | `READY_STRONG` | `0,1,2,3,5,6,7,8,9` | `1,4,5` | 542/82068 | 116/17107 | 116/18062 | 192/31944 | 26/7800 |
| `fold_03_holdout_milk_orange_juice` | `milk, orange_juice` | `READY_STRONG` | `0,1,2,3,4,5,6,8,9` | `6,7,9` | 539/86597 | 115/18097 | 116/19176 | 196/25311 | 22/6600 |
| `fold_04_holdout_salad_dressing_tomato_sauce` | `salad_dressing, tomato_sauce` | `LOW_OOD_FAILURE_SUPPORT` | `0,1,2,3,4,5,6,7,8,9` | `2,5,8,9` | 531/84427 | 113/17485 | 113/18307 | 209/28962 | 9/2700 |

## Leakage Checks

- `fold_00_holdout_alphabet_soup_bbq_sauce` held-out leakage into seen train/calib/test/failure splits: `[]`
- `fold_01_holdout_butter_chocolate_pudding` held-out leakage into seen train/calib/test/failure splits: `[]`
- `fold_02_holdout_cream_cheese_ketchup` held-out leakage into seen train/calib/test/failure splits: `[]`
- `fold_03_holdout_milk_orange_juice` held-out leakage into seen train/calib/test/failure splits: `[]`
- `fold_04_holdout_salad_dressing_tomato_sauce` held-out leakage into seen train/calib/test/failure splits: `[]`

## Exact Files Created

- Root: `experiments/prepared_20260526/08_target_object_pick_basket_loto_v1`
- `all_pick_basket_rows.refs.jsonl`
- `all_pick_basket_episodes.jsonl`
- `coverage_by_target_object.csv`
- `TARGET_OBJECT_LOTO_REGISTRY.json`
- `TARGET_OBJECT_LOTO_SUMMARY.json`
- Per-fold `datasets/refs/*.rows.jsonl` and `*.episodes.jsonl`

## Recommended First Training Command

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

## Final Decision Fields

```text
TARGET_OBJECT_OOD_DATASET_CREATED = YES
TRUE_SAME_TASK_ONLY_OBJECT_CHANGED = NO
BEST_POSSIBLE_CURRENT_OBJECT_OOD = TARGET_OBJECT_PICK_BASKET_LOTO
USES_ACTUAL_PICKED_OBJECT_LABEL = YES
USES_PERTURBATION_GROUP_AS_OOD_AXIS = NO
LEAKAGE_CHECK_PASSED = YES
READY_TO_TRAIN_TARGET_OBJECT_OOD = YES_FOR_READY_STRONG_FOLDS
```
