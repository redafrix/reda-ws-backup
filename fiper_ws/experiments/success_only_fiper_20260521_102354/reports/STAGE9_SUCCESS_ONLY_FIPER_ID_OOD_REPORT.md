# STAGE 9 SUCCESS-ONLY FIPER ID & OOD EVALUATION REPORT

## 1. Executive Summary

This report evaluates a **success-only FIPER (RND-OE + ACE)** safety monitor calibrated on **Sam**. The objective is to verify if an anomaly detection monitor trained and calibrated *strictly* on successful expert demonstrations remains calm (low false alarm rates) when encountering unseen successful behaviors (OOD tasks and suites), while identifying when the system deviates into sub-optimal or risky behaviors.

### Final Decision:
**`SUCCESS_ONLY_FIPER_WORKS_ID_BUT_NOT_OOD`**

* **Why**: The success-only monitor stays exceptionally calm on in-distribution (ID) success data (4.67% false alarm at q95) and generalizes strongly to unseen **OOD tasks** (0.52% false alarm at q95). However, when transitioning to a completely unseen **OOD suite** (`libero_spatial`), the false alarm rate rises to **13.23% at q95** (a 2.6x increase over the nominal 5% rate). Additionally, we discovered a major numerical instability where RND scores explode into the billions when evaluated on non-expert rollout data due to feature variance collapse in the training set.

---

## 2. Experimental Data

### Exact Data Used:
* **Train Set**: `train_success_id.jsonl` (11,199 samples) - 60% of unique ID expert demos.
* **Calibration Set**: `calib_success_id.jsonl` (3,574 samples) - 20% of unique ID expert demos.
* **Test ID Set**: `test_success_id.jsonl` (3,944 samples) - 20% of unique ID expert demos.
* **Test OOD Task Set**: `test_success_ood_task.jsonl` (386 samples) - Held out all chunks from `KITCHEN_SCENE1_put_the_biscuit_box_to_the_left_of_the_plate_demo.hdf5` and `STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy_demo.hdf5`.
* **Test OOD Suite Set**: `test_success_ood_suite.jsonl` (2,351 samples) - Held out all chunks from the `libero_spatial` suite.

### Exact Data NOT Used (for Training/Calibration):
* **Failure-Mined Rollouts**: `replay_counterfactual_samples.jsonl` (8,192 samples) was not used.
* **Safe Mass Rollouts**: `counterfactual_samples.jsonl` (5,120 samples) was not used.
* **Risk Labels**: No supervised risk scores or failure bins (`RISKY_STRONG`, `state_context`, etc.) were used during training or threshold calibration.

---

## 3. Split Counts and Leakage Audit

To prevent demonstration memorization, splits were partitioned strictly at the demonstration level (grouped by `unique_demo_id = taskname_demoname`):

| Split | Sample Count | Unique Demos | Source Suites |
| :--- | :---: | :---: | :--- |
| **`train_success_id`** | 11,199 | 354 | libero_object, libero_goal, libero_10, libero_90 |
| **`calib_success_id`** | 3,574 | 118 | libero_object, libero_goal, libero_10, libero_90 |
| **`test_success_id`** | 3,944 | 118 | libero_object, libero_goal, libero_10, libero_90 |
| **`test_success_ood_task`** | 386 | 20 | libero_object, libero_10 (held-out tasks) |
| **`test_success_ood_suite`** | 2,351 | 80 | libero_spatial (held-out suite) |

### Leakage Audit Results:
* **Train vs. Calib Demo Overlap**: 0 demos shared.
* **Train vs. Test ID Demo Overlap**: 0 demos shared.
* **Calib vs. Test ID Demo Overlap**: 0 demos shared.
* **ID Splits vs. OOD Task Overlap**: 0 tasks shared.
* **ID Splits vs. OOD Suite Overlap**: 0 suites shared.

**Audit Status: SUCCESS. Zero demo-level leakage detected.**

---

## 4. RND-OE Training and Calibration

The RND-OE model was trained strictly on `train_success_id.jsonl` using deployable numeric features (81 dimensions).

### Training Loss:
* **Epoch 1**: 0.005052
* **Epoch 10**: 0.000471
* **Epoch 20**: 0.000339
* **Epoch 30 (Final)**: 0.000287

### Calibrated Conformal Thresholds (from `calib_success_id` only):
* **`q90` (90th percentile)**: `0.000592`
* **`q95` (95th percentile)**: `0.000754`
* **`q99` (99th percentile)**: `0.001125`

---

## 5. False Alarm Rate Evaluation

We scored each expert success split using the trained RND-OE model to measure false alarms (trigger rates):

| Split | Count | Mean RND Score | False Alarm @ q90 | False Alarm @ q95 | False Alarm @ q99 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`train_success_id`** | 11,199 | 0.000282 | 6.05% | 2.55% | 0.51% |
| **`test_success_id`** | 3,944 | 0.000309 | 9.18% | 4.67% | 1.01% |
| **`test_success_ood_task`** | 386 | 0.000269 | 1.30% | 0.52% | 0.26% |
| **`test_success_ood_suite`** | 2,351 | 0.000479 | 24.80% | **13.23%** | 3.62% |

### Key Observations:
1. **Excellent Calibration**: The false alarm rate on the held-out `test_success_id` (4.67% at q95) matches the nominal target (5.0%) almost perfectly.
2. **Task Generalization**: The RND-OE monitor stays exceptionally calm on unseen **OOD tasks** (only 0.52% false alarm rate at q95).
3. **Suite Shift Sensitivity**: When transitioning to the OOD suite (`libero_spatial`), the false alarm rate rises to **13.23%** (a 2.6x increase). This shows that the monitor is sensitive to broader environmental/visual domain shifts.

---

## 6. ACE and FIPER Signal Analysis

We ran unsupervised ACE audits on the 64-seed Sam datasets. The ACE threshold was calibrated using the 95th percentile of the safe mass dataset:
* **Calibrated ACE Threshold (`q95`)**: `-82.1781`

### Discovering RND Score Explosion:
When scoring the 64-seed counterfactual datasets (`safe_mass` and `failure_mined`), we observed RND scores exploding into the **billions** (e.g., `1.2e10`). 

A detailed audit of the trained RND-OE checkpoint revealed the mathematical cause:
- In the success-only training set, several features are constant. Specifically, `steps_executed` and `H_used` are always `10` (since chunks are exactly 10 steps), and flowtrace features are always `0.0` (as they are absent in expert demos).
- Consequently, the training standard deviations for these features collapsed and were clipped to the minimum epsilon value of `1e-6` in the checkpoint.
- During evaluation on rollout datasets, the environment chunks vary in length or exhibit different flowtrace values. When normalized, these small differences are divided by `1e-6` (effectively multiplied by `1,000,000`), blowing up the input layer of the RND networks and generating astronomical RND scores.

As a result of this RND score explosion, RND is classified as "high" for almost every state in both rollout datasets.

### FIPER Quadrant Distributions:

#### Safe Mass Dataset (80 states / 5,120 samples):
* **`OOD_confident` (RND high, ACE low)**: 76 states (95.00%)
* **`FIPER_alarm` (RND high, ACE high)**: 4 states (5.00%)
* **`action_uncertain` (RND low, ACE high)**: 0 states (0.00%)
* **`normal_confident` (RND low, ACE low)**: 0 states (0.00%)

#### Failure Mined Dataset (128 states / 8,192 samples):
* **`OOD_confident` (RND high, ACE low)**: 128 states (100.00%)
* **`FIPER_alarm` (RND high, ACE high)**: 0 states (0.00%)
* **`action_uncertain` (RND low, ACE high)**: 0 states (0.00%)
* **`normal_confident` (RND low, ACE low)**: 0 states (0.00%)

---

## 7. Future Mining Queue Summary

We generated a future mining queue containing **208 unique states** sorted by combined priority score:
* **`fiper_candidate_states.jsonl`**

The queue contains states from both `safe_mass` and `failure_mined` datasets. Due to the RND score explosion, priority scores are dominated by RND values. 

The top 3 mining candidates are:
1. `libero_spatial_with_mug_t0_r13_pSTUCK_OR_NO_PROGRESS_s119_state` (Priority: 1.595e13, Quadrant: `OOD_confident`)
2. `libero_spatial_with_mug_t1_r3_pseed3_window014_state` (Priority: 1.595e13, Quadrant: `OOD_confident`)
3. `libero_spatial_with_mug_t0_r5_pSTUCK_OR_NO_PROGRESS_s119_state` (Priority: 1.595e13, Quadrant: `FIPER_alarm`)

---

## 8. Code Files Created/Modified

All tools are located under `fiper_ws/stage9_v2_tools/` on Sam:
1. **`prepare_success_only_splits.py`**: Extracts expert success chunks across 5 suites and partitions them into group-safe splits.
2. **`train_rnd_success_only.sh`**: Command-line wrapper to train RND-OE on train success data and calibrate thresholds strictly on calibration data.
3. **`evaluate_success_only_fiper.py`**: Scores splits, runs ACE analysis, maps RND to state groups, classifies quadrants, and creates the mining queue.

---

## 9. Next Steps and Recommendations

1. **Remove Flat Features from RND**: To resolve the numerical explosion, future iterations of RND-OE should exclude features that are static in expert trajectories (e.g., `steps_executed`, `H_used`, and unpopulated flowtrace features) before training.
2. **Suite-Specific Calibration**: Because RND is sensitive to visual domain shifts (13.23% false alarms on OOD suite), conformal thresholds should be calibrated per suite if the robot transitions between distinct visual environments.
