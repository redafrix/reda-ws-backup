# FIPER Target-Object Pick-Basket Fold 01 Smoke Test Report

**Date:** 2026-05-26  
**Project:** Stage 9 / LIBERO-PRO / SimVLA / FIPER monitor  
**Sam Workspace:** `/home/rootalkhatib/test/reda_ws/fiper_ws`  
**Experiment Directory:** `experiments/fiper_target_object_pick_basket_fold_01_smoke_20260526`  

---

## 1. Execution Verdict & Status

The CPU smoke test command completed successfully on the Sam node without any errors or warnings.

- **Command Status:** **COMPLETED SUCCESS**
- **Sanity Checks Status:** **PASS**
- **Verdict:**
  - `TARGET_OBJECT_FOLD_01_SMOKE_PASS = YES`
  - `READY_FOR_FULL_FOLD_01_TRAINING = YES`

---

## 2. Loaded Split Row Counts

The row limits specified in the smoke test command were respected exactly, and all splits successfully loaded the maximum allowed data rows from the LOTO reference files:

| Split Name | Row Limit | Loaded Rows | Source Files |
|---|---:|---:|---|
| `success_train_seen` | 3,000 | **3,000** | `bob_instance_A/fiper_receding_samples.jsonl` |
| `success_calib_seen` | 1,500 | **1,500** | `bob_instance_A/fiper_receding_samples.jsonl` |
| `success_test_seen` | 1,500 | **1,500** | `bob_instance_A/fiper_receding_samples.jsonl` |
| `success_test_ood` | 1,500 | **1,500** | `bob_instance_A/fiper_receding_samples.jsonl` |
| `failure_eval_seen` | 1,500 | **1,500** | `bob_instance_A/fiper_receding_samples.jsonl` |
| `failure_eval_ood` | 1,500 | **1,500** | `bob_instance_A/fiper_receding_samples.jsonl` (600), `bob_instance_B` (900) |
| `failure_eval_ood_late` | 1,500 | **1,500** | `bob_instance_A` (150), `bob_instance_B` (225), `sam_instance_A` (1,125) |
| `failure_eval_ood_near_end` | 1,500 | **1,500** | `bob_instance_A` (100), `bob_instance_B` (150), `sam_instance_A` (1,250) |

All split reference paths resolved correctly and populated the loaders.

---

## 3. Score File Output Verification

Score rows were successfully written for every evaluated split. The size of the generated `.jsonl` files in the `scores/` directory contains exactly 9,000 lines, matching the sum of evaluated rows across the 6 eval splits:

- `scores/rnd_scores_by_split.jsonl`: **9,000 lines**
- `scores/ace_scores_by_split.jsonl`: **9,000 lines**
- `scores/fiper_scores_by_split.jsonl`: **9,000 lines**

Both `success_test_ood` and `failure_eval_ood` are represented correctly in the evaluations and written output lines.

---

## 4. Calibrated Thresholds from Smoke Run

The conformal thresholds calibrated on the 1,500 success calibration rows are:

- **RND Thresholds:**
  - `q90`: `0.408230`
  - `q95`: `0.491808`
  - `q99`: `0.749678`
- **ACE Thresholds:**
  - `q90`: `-343.114335`
  - `q95`: `-342.285971`
  - `q99`: `-340.994082`

---

## 5. Potential Issues, Warnings, or Suspicious Behavior

None. The execution logs were clean:
- No `RuntimeError` or `KeyError` exceptions.
- No splits resulted in zero-row warning or empty loaders.
- Training loss decreased nominally for the single epoch (`Loss: 0.004806`).
- Conformal calibration successfully completed and wrote JSON thresholds files.

---

## 6. Final Key Fields

```text
TARGET_OBJECT_FOLD_01_SMOKE_PASS = YES
READY_FOR_FULL_FOLD_01_TRAINING = YES
```
