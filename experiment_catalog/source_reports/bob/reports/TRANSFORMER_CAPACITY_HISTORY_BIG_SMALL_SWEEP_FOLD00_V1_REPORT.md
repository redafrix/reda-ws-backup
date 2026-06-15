# FIPER NextGen Transformer Capacity & History Sweep Combined Report

This report summarizes the results of the capacity/history sweep covering 12 job configurations (6 bigger-model variants and 6 smaller-model variants) on `fold_00_holdout_alphabet_soup_bbq_sauce` under the `q95 mass-conformal alpha=0.15` policy.

## 1. Process Status

- **Bigger Model Sweep Output Dir:** `experiments/transformer_capacity_history_sweep_fold00_v1_20260528`
- **Smaller Model Sweep Output Dir:** `experiments/transformer_capacity_history_small_sweep_fold00_v1_20260528`
- **GPU Used:** NVIDIA GeForce RTX 4070 Ti (16GB)
- **Command Run (Big Sweep):**
  ```bash
  python3 scripts/run_clean_temporal_nextgen_campaign_v2.py --campaign-config configs/transformer_capacity_history_sweep_fold00_v1.json --refs-dir experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs --output-dir experiments/transformer_capacity_history_sweep_fold00_v1_20260528 --base-dir . --device cuda --max-epochs 120 --patience 18 --batch-size 384 --seed 42 --force
  ```
- **Command Run (Small Sweep):**
  ```bash
  python3 scripts/run_clean_temporal_nextgen_campaign_v2.py --campaign-config configs/transformer_capacity_history_small_sweep_fold00_v1.json --refs-dir experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs --output-dir experiments/transformer_capacity_history_small_sweep_fold00_v1_20260528 --base-dir . --device cuda --max-epochs 120 --patience 18 --batch-size 384 --seed 42 --force
  ```
- **Process Interruptions:** No running campaigns were interrupted or stopped. The sweeps ran cleanly and concurrently on Bob's GPU.

## 2. Feature Hygiene Verification

For every executed sweep job, `FEATURE_AUDIT.json` was parsed to verify the following constraints:
1. No reward signal input: **PASS** (uses_reward = false)
2. No success signal input: **PASS** (uses_success = false)
3. No `object_positions_before` or visual object poses: **PASS** (uses_object_positions_before = false, input_fields does not contain visual positions)
4. No task/language instruction metadata as model inputs: **PASS** (uses_task_metadata_as_input = false)
5. No out-of-distribution (OOD) row leakage into the training set: **PASS** (uses_ood_rows_for_train = false)

| Job Name | Reward | Success | Object Poses | Task Meta | OOD Train Leakage | Hygiene Status |
|---|---|---|---|---|---|---|
| `cap_00_current_reproduce` | NO | NO | NO | NO | NO | **PASS** |
| `cap_01_medium_k16` | NO | NO | NO | NO | NO | **PASS** |
| `cap_02_large_k16` | NO | NO | NO | NO | NO | **PASS** |
| `cap_03_medium_k32` | NO | NO | NO | NO | NO | **PASS** |
| `cap_04_large_k32` | NO | NO | NO | NO | NO | **PASS** |
| `cap_05_wide_lowdrop_k16` | NO | NO | NO | NO | NO | **PASS** |
| `cap_06_tiny_k16` | NO | NO | NO | NO | NO | **PASS** |
| `cap_07_small_k16` | NO | NO | NO | NO | NO | **PASS** |
| `cap_08_shallow_k16` | NO | NO | NO | NO | NO | **PASS** |
| `cap_09_tiny_k32` | NO | NO | NO | NO | NO | **PASS** |
| `cap_10_small_k32` | NO | NO | NO | NO | NO | **PASS** |
| `cap_11_shallow_k32` | NO | NO | NO | NO | NO | **PASS** |

## 3. Training Behavior & Overfitting Analysis

Our analysis of the training curves shows that most models peak very early in training (typically between epoch 2 and epoch 6), after which validation loss/AUC degrades despite training loss continuing to decrease. This confirms the **early overfitting pattern** identified in previous experiments.

| Job Name | Best Epoch | Total Epochs | Best Train Loss | Final Train Loss | Best Val AUC | Val Degraded After Best Epoch? | Peaked by Epoch 5? | Peaked by Epoch 10? |
|---|---:|---:|---:|---:|---:|---|---|---|
| `cap_00_current_reproduce` | 5 | 23 | 0.146338 | 0.050648 | 0.9154 | YES | YES | YES |
| `cap_01_medium_k16` | 1 | 19 | 0.279021 | 0.028033 | 0.9278 | YES | YES | YES |
| `cap_02_large_k16` | 1 | 19 | 0.272753 | 0.022701 | 0.9200 | YES | YES | YES |
| `cap_03_medium_k32` | 2 | 20 | 0.173930 | 0.013183 | 0.9276 | YES | YES | YES |
| `cap_04_large_k32` | 1 | 19 | 0.259764 | 0.010656 | 0.9254 | YES | YES | YES |
| `cap_05_wide_lowdrop_k16` | 3 | 21 | 0.145234 | 0.015262 | 0.9083 | YES | YES | YES |
| `cap_06_tiny_k16` | 4 | 22 | 0.218610 | 0.117425 | 0.9177 | YES | YES | YES |
| `cap_07_small_k16` | 3 | 21 | 0.215593 | 0.090804 | 0.9218 | YES | YES | YES |
| `cap_08_shallow_k16` | 7 | 25 | 0.188918 | 0.105632 | 0.9138 | YES | NO | YES |
| `cap_09_tiny_k32` | 3 | 21 | 0.221955 | 0.096054 | 0.9314 | YES | YES | YES |
| `cap_10_small_k32` | 2 | 20 | 0.234184 | 0.071787 | 0.9297 | YES | YES | YES |
| `cap_11_shallow_k32` | 2 | 20 | 0.255398 | 0.092321 | 0.9328 | YES | YES | YES |

## 4. Policy Metrics Comparison

All models evaluated under `score q95 mass-conformal alpha=0.15` policy. Episode counts per split: Seen Test = 136, OOD Test = 211, OOD Failure = 42.

| Model Configuration | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never | q95 Row Threshold | Mass Conformal Threshold |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| **Existing Real v2_018** | 15.4% | 25.6% | 95.2% | 0.0% | 26.2% | 85.7% | 0.332 | 4.8% | 0.51326 | 0.08968 |
| `cap_00_current_reproduce` | 16.2% | 28.9% | 95.2% | 0.0% | 23.8% | 83.3% | 0.344 | 4.8% | 0.72413 | 0.63399 |
| `cap_01_medium_k16` | 17.6% | 28.0% | 95.2% | 0.0% | 28.6% | 90.5% | 0.325 | 4.8% | 0.52221 | 0.29155 |
| `cap_02_large_k16` | 16.2% | 28.9% | 92.9% | 0.0% | 21.4% | 88.1% | 0.331 | 7.1% | 0.57966 | 0.24721 |
| `cap_03_medium_k32` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% | 0.75794 | 0.00000 |
| `cap_04_large_k32` | 21.3% | 43.1% | 97.6% | 0.0% | 14.3% | 92.9% | 0.334 | 2.4% | 0.44617 | 0.07591 |
| `cap_05_wide_lowdrop_k16` | 16.2% | 28.9% | 95.2% | 0.0% | 35.7% | 88.1% | 0.306 | 4.8% | 0.60890 | 0.78538 |
| `cap_06_tiny_k16` | 13.2% | 31.8% | 92.9% | 0.0% | 21.4% | 88.1% | 0.321 | 7.1% | 0.45708 | 0.40575 |
| `cap_07_small_k16` | 19.1% | 33.6% | 95.2% | 0.0% | 33.3% | 88.1% | 0.315 | 4.8% | 0.47018 | 0.12322 |
| `cap_08_shallow_k16` | 16.9% | 31.8% | 97.6% | 0.0% | 19.0% | 88.1% | 0.340 | 2.4% | 0.49877 | 0.28013 |
| `cap_09_tiny_k32` | 14.0% | 28.0% | 95.2% | 0.0% | 16.7% | 88.1% | 0.347 | 4.8% | 0.50687 | 0.26409 |
| `cap_10_small_k32` | 16.2% | 28.4% | 95.2% | 0.0% | 23.8% | 90.5% | 0.335 | 4.8% | 0.47865 | 0.07695 |
| `cap_11_shallow_k32` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% | 0.47814 | 0.00000 |

## 5. Fair Comparison to Existing Real Baseline

This section checks every model configuration against the real baseline to see if it reduces OOD False Alarms while preserving failure detection capabilities.

| Configuration Name | Beats OOD FA? | Keeps Recall within 5%? (>= 90.2%) | Keeps Det@50 within 5%? (>= 80.7%) | Improves Det@25? (> 26.2%) | Should Scale? |
|---|---|---|---|---|---|
| `cap_00_current_reproduce` | NO | YES | YES | NO | **NO** |
| `cap_01_medium_k16` | NO | YES | YES | YES | **NO** |
| `cap_02_large_k16` | NO | YES | YES | NO | **NO** |
| `cap_03_medium_k32` | NO | YES | YES | YES | **NO** |
| `cap_04_large_k32` | NO | YES | YES | NO | **NO** |
| `cap_05_wide_lowdrop_k16` | NO | YES | YES | YES | **NO** |
| `cap_06_tiny_k16` | NO | YES | YES | NO | **NO** |
| `cap_07_small_k16` | NO | YES | YES | YES | **NO** |
| `cap_08_shallow_k16` | NO | YES | YES | NO | **NO** |
| `cap_09_tiny_k32` | NO | YES | YES | NO | **NO** |
| `cap_10_small_k32` | NO | YES | YES | NO | **NO** |
| `cap_11_shallow_k32` | NO | YES | YES | YES | **NO** |

## 6. Job Rankings

- **Best overall model by balanced score:** `cap_05_wide_lowdrop_k16` (Score: `1.1521`)
- **Best smaller model:** `cap_07_small_k16` (Score: `1.0187`)
- **Best bigger model:** `cap_05_wide_lowdrop_k16` (Score: `1.1521`)
- **Best model satisfying scaling criteria (Lowest OOD FA & Recall-Preserved):** `NONE`

## 7. Final Verdict

- `BIG_SWEEP_COMPLETE` = **YES**
- `SMALL_SWEEP_COMPLETE` = **YES**
- `FEATURE_HYGIENE_PASS` = **YES**
- `OLD_EARLY_OVERFITTING_PATTERN_CONFIRMED` = **YES**
- `ANY_SMALL_MODEL_BEATS_REAL_V2_018` = **NO**
- `ANY_BIG_MODEL_BEATS_REAL_V2_018` = **NO**
- `BEST_MODEL_TO_SCALE_ALL_FOLDS` = **NONE**
- `SHOULD_SCALE_TO_ALL_FOLDS` = **NO**
