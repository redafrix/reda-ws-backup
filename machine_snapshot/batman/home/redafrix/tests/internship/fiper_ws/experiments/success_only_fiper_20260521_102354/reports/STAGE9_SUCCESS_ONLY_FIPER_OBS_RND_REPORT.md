# STAGE 9 SUCCESS-ONLY FIPER — OBSERVATION RND REPORT

## 1. Executive Summary

This report presents the final evaluation of the **observation-only RND-OE safety monitors** on **Sam**. The objective was to test whether shifting RND-OE from action patterns to robot observation/proprioception features provides a more robust and suite-invariant anomaly detection monitor. We evaluated two primary observation-only configurations against a new, more realistic OOD setting (unseen objects/tasks within trained suites) and rollout datasets.

### Final Decision:
**`OBS_RND_FAILS`**

* **Why**: While observation-only monitors avoid modeling action-sequence profiles, they introduce severe generalization failures and engineering vulnerabilities that make them unsuitable for deployment. 
  1. **Extreme Task False Alarms**: In seen suites, when encountering unseen tasks/objects (`test_success_ood_task`), the false alarm rate at $q_{95}$ is **60.88%** for `proprio_only` and **66.06%** for `observation_context_only` (nominal: 5.0%). The monitor flags almost two-thirds of valid expert success trajectories as anomalous because robot trajectories and physical positions are highly task-dependent.
  2. **Failure to Detect OOD Suite**: The `proprio_only` monitor failed to flag rollout datasets as OOD (0% of `safe_mass` flagged as `OOD_confident` / `FIPER_alarm`) even though they were generated from `libero_spatial` (an OOD suite relative to the training set). This is because the spatial coordinates of the arm overlap heavily with seen suites.
  3. **Telemetry Inconsistency Vulnerability**: The `observation_context_only` monitor depends on joint and end-effector states that are absent from rollout telemetry logs. This mismatch results in default/zero values at evaluation time, triggering a massive, artificial 100% OOD alarm.
  4. **Coordinate Frame Discrepancies**: Different LIBERO suites store coordinates in inconsistent frames (e.g., table-relative vs world-relative), causing trained models to falsely identify spatial coordinate offsets as OOD.

---

## 2. Experimental Setup & Split Construction

To thoroughly evaluate the spatial generalization of the observation-only monitors, we constructed a new **OOD-Object** test split in addition to standard ID, OOD-task, and OOD-suite splits.

### 2.1 OOD-Object Task Holdout Design
For the ID suites (`libero_object`, `libero_goal`, `libero_10`, and `libero_90`), we held out 2 specific object-centric tasks per suite from the training/calibration pools:
* **`libero_object`**:
  * *Task 1*: "pick up the cream cheese and place it in the basket"
  * *Task 2*: "pick up the salad dressing and place it in the basket"
* **`libero_goal`**:
  * *Task 1*: "put the bowl on the plate"
  * *Task 2*: "put the cream cheese in the bowl"
* **`libero_10`**:
  * *Task 1*: "put the yellow and white mug in the microwave and close it"
  * *Task 2*: "put the black bowl in the bottom drawer of the cabinet and close it"
* **`libero_90`**:
  * *Task 1*: "pick up the alphabet soup and place it in the basket"
  * *Task 2*: "turn on the stove"

All expert chunks belonging to these tasks were routed exclusively to `test_success_ood_object_enriched.jsonl` (2,110 samples).

### 2.2 Split Breakdown and Leakage Audit

A demo-level audit was conducted to verify that no demonstration-level leakage existed between splits:

| Split Name | Sample Count | Unique Demos | Description / Purpose |
|:---|:---:|:---:|:---|
| **`train_success_id_enriched`** | 10,082 | 318 | ID Training data (60% of remaining ID demos) |
| **`calib_success_id_enriched`** | 3,051 | 102 | Threshold Calibration (20% of remaining ID demos) |
| **`test_success_id_enriched`** | 3,474 | 102 | ID Generalization Test (20% of remaining ID demos) |
| **`test_success_ood_task_enriched`**| 386 | 20 | Unseen tasks from seen suites |
| **`test_success_ood_object_enriched`**| 2,110 | 72 | Unseen objects/tasks from seen suites |
| **`test_success_ood_suite_enriched`**| 2,351 | 80 | Unseen suite (`libero_spatial`) |

**Leakage Audit Status**: **SUCCESS**. 0 demo-level overlap detected between training, calibration, and test splits.

---

## 3. Evaluated Feature Modes

We implemented and trained RND-OE models for two observation-based feature spaces:
1. **`observation_context_only`** (21 dimensions):
   * End-effector position ($x, y, z$) - 3 dims
   * End-effector orientation (quaternion) - 3 dims
   * Gripper states - 2 dims
   * Joint states - 7 dims
   * End-effector state - 6 dims
2. **`proprio_only`** (8 dimensions):
   * End-effector position ($x, y, z$) - 3 dims
   * End-effector orientation (quaternion) - 3 dims
   * Gripper states - 2 dims
3. **`action_free_with_vlm`**:
   * Skipped because VLM features are absent in the expert datasets.

---

## 4. Evaluation Results

### 4.1 Comparative False Alarm Rates (FAR)
We evaluated the false alarm rates (FAR) at conformal quantiles $q_{90}$, $q_{95}$, and $q_{99}$ calibrated on the `calib_success` split:

| Evaluation Split | Metric | Action-Heavy RND (71 dims) | Observation-Context (21 dims) | Proprio-Only (8 dims) |
|:---|:---:|:---:|:---:|:---:|
| **`test_success_id`** (ID Test) | FA@q90<br>FA@q95<br>FA@q99 | 9.18%<br>4.94%<br>0.91% | 13.04%<br>7.28%<br>1.78% | 12.58%<br>7.48%<br>2.13% |
| **`test_success_ood_task`** (OOD Task) | FA@q90<br>FA@q95<br>FA@q99 | 1.30%<br>0.52%<br>0.26% | 76.94%<br>**66.06%**<br>47.67% | 63.99%<br>**60.88%**<br>48.45% |
| **`test_success_ood_object`** (OOD Obj) | FA@q90<br>FA@q95<br>FA@q99 | N/A | 24.83%<br>**18.48%**<br>9.62% | 24.88%<br>**16.87%**<br>7.49% |
| **`test_success_ood_suite`** (OOD Suite) | FA@q90<br>FA@q95<br>FA@q99 | 24.80%<br>13.44%<br>3.70% | 32.88%<br>**22.76%**<br>8.68% | 21.57%<br>**14.55%**<br>6.64% |

### 4.2 Training Summary and Conformal Thresholds

* **`observation_context_only`**:
  * Training Epochs: 30 (Best loss: `0.000159` on 10,082 samples)
  * Calibrated thresholds: $q_{90} = 0.000340$, $q_{95} = 0.000433$, $q_{99} = 0.000710$
* **`proprio_only`**:
  * Training Epochs: 30 (Best loss: `0.000105` on 10,082 samples)
  * Calibrated thresholds: $q_{90} = 0.000233$, $q_{95} = 0.000303$, $q_{99} = 0.000516$

---

## 5. In-Depth Analysis of Major Failures

### 5.1 The Telemetry Gap in Rollouts (`observation_context_only`)
When scoring the rollout datasets (`safe_mass` and `failure_mined`), the `observation_context_only` model exhibited an RND score explosion:
* **`safe_mass` Mean RND**: `0.0204` (vs nominal $q_{95}$ threshold of `0.000433`)
* **`failure_mined` Mean RND**: `0.0207` (vs nominal $q_{95}$ threshold of `0.000433`)

**Diagnosis**: The rollout datasets (recorded from live simulations) only contain the `proprio` field (8 dimensions) in their logged dictionaries. The keys `joint_states` and `ee_states` are missing. During scoring, these missing features defaulted to `0.0`. Since the RND model was trained on actual non-zero joint/ee telemetry from expert demonstrations, the sudden step-function drop to zero was detected as a massive anomaly, causing 100% of states to be classified in the `OOD_confident` / `FIPER_alarm` quadrants.

### 5.2 Coordinate Frame Inconsistencies in HDF5 Files
We discovered that LIBERO expert demonstrations across different suites use inconsistent coordinate reference systems:
* In `libero_object`, the end-effector z-position is stored relative to the tabletop height ($z \approx 0.25$).
* In `libero_spatial` and `libero_goal`, the z-position is stored relative to the world/base frame ($z \approx 1.18$).
* In the rollout logs, the observation-to-proprio converter (`obs_to_proprio()`) always extracts absolute coordinates in the world frame ($z \approx 1.08 \text{ to } 1.18$).

This coordinate frame mismatch means a model trained on mixed expert data will falsely flag physical coordinates as out-of-distribution, creating a major systematic bias.

### 5.3 Generalization vs. Overlap Failures (`proprio_only`)
By using only the 8-dim proprioception features (which were fully present in the rollout logs), the `proprio_only` monitor avoided the telemetry gap bug:
* **`safe_mass` Mean RND**: `0.000117` (vs nominal $q_{95}$ threshold of `0.000303`)
* **`failure_mined` Mean RND**: `0.000159` (vs nominal $q_{95}$ threshold of `0.000303`)

However, this revealed two fatal shortcomings:
1. **0% OOD Detection on Rollouts**: Because `safe_mass` was generated from the OOD suite `libero_spatial`, the RND monitor *should* have flagged it as OOD. However, because the arm's physical trajectories in the workspace overlap with the coordinates seen in the training suites, the `proprio_only` model classified 0% of `safe_mass` states as OOD.
2. **High OOD-Task False Alarm Rate**: Even though it failed to detect the OOD suite, it was overly sensitive to unseen tasks in the *same* suite, flagging **60.88%** of valid expert successes as OOD.

---

## 6. FIPER Quadrant Classifications

Using the calibrated conformal thresholds, rollout states were classified into FIPER quadrants (using the calibrated ACE threshold of `-82.1781`):

### 6.1 `observation_context_only` (Vulnerable to Telemetry Gap)
* **Safe Mass (80 states)**:
  * `OOD_confident`: 76 states (95.0%)
  * `FIPER_alarm`: 4 states (5.0%)
  * `action_uncertain`: 0 states (0.0%)
  * `normal_confident`: 0 states (0.0%)
* **Failure Mined (128 states)**:
  * `OOD_confident`: 128 states (100.0%)
  * `FIPER_alarm`: 0 states (0.0%)
  * `action_uncertain`: 0 states (0.0%)
  * `normal_confident`: 0 states (0.0%)

### 6.2 `proprio_only` (Vulnerable to Overlap / Generalization Failure)
* **Safe Mass (80 states)**:
  * `OOD_confident`: 0 states (0.0%)
  * `FIPER_alarm`: 0 states (0.0%)
  * `action_uncertain`: 4 states (5.0%)
  * `normal_confident`: 76 states (95.0%)
* **Failure Mined (128 states)**:
  * `OOD_confident`: 21 states (16.4%)
  * `FIPER_alarm`: 0 states (0.0%)
  * `action_uncertain`: 0 states (0.0%)
  * `normal_confident`: 107 states (83.6%)

---

## 7. Conclusions & Recommendations

1. **Abandon Observation-Only RND**: Relying strictly on robot joint states and Cartesian coordinates results in a monitor that is either too sensitive to task-specific trajectory differences (60%+ false alarm rate) or completely blind to suite shifts due to coordinate overlap.
2. **Standardize Logging pipelines**: If observation or action features are to be used across datasets, the logging environment and dataset extraction scripts must use identical pipelines to prevent telemetry missingness.
3. **Action-Heavy RND is Superior**: The action-pattern RND-OE model (from the previous campaign) is far more suitable: it has a near-zero false alarm rate on unseen tasks within suites (0.52%), keeps a calibrated 4.94% false alarm rate on ID data, and captures visual/suite distribution shifts better than coordinate-based models.
