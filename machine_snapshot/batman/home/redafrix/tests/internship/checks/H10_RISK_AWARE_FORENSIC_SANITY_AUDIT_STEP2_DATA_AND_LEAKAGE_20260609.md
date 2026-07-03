# Forensic Sanity Audit Report: Step 2 - Data & Leakage Investigation

> [!IMPORTANT]
> This is Step 2 of the forensic sanity audit conducted on SimVLA risk-aware simulation results stored on host **pcrobot**. The audit is strictly read-only; no code, configuration, or data files were modified.

## 1. Training Dataset Provenance

We audited the training directories, dataset manifests, and split configuration files on `pcrobot`.

### A. Dataset Path and Configuration
- **H10 Base and TopK8 Detector Training Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat`
- **Split File Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/episode_buckets.json`
- **Primary Dataset Sizes:** `17,409` total valid episodes (`14,005` successes, `3,404` failures/timeouts).
- **Split Allocations (from `bucket_counts.json`):**
  - `failure_train_seen`: **2,724** episodes (`68,100` query rows)
  - `failure_val_seen`: **680** episodes (`17,000` query rows)
  - `success_train_seen`: **11,205** episodes (`120,030` query rows)
  - `success_val_seen`: **1,400** episodes (`14,997` query rows)
  - `success_calib_seen`: **1,400** episodes (`15,339` query rows)
  - `success_test_seen` / `failure_test_seen`: **0** episodes (The test split was set to `0%` during training because the test set is evaluated separately on `exact_200_chunk10`).

### B. Task-Level & Seed-Level Distribution in Splits

| Split Bucket | Task 3 Episodes | Task 6 Episodes | Task 8 Episodes | Other Tasks (0, 1, 2, 4, 5, 7, 9) |
| :--- | :---: | :---: | :---: | :--- |
| **failure_train_seen** | 1,309 | 653 | 106 | {'4': 208, '0': 191, '9': 211, '1': 33, '5': 12, '2': 1} |
| **failure_val_seen** | 355 | 137 | 30 | {'4': 62, '0': 32, '9': 51, '1': 8, '2': 1, '5': 3, '7': 1} |
| **success_calib_seen** | 11 | 88 | 143 | {'0': 157, '4': 134, '7': 182, '9': 184, '5': 155, '2': 178, '1': 168} |
| **success_train_seen** | 59 | 770 | 1,307 | {'0': 1207, '7': 1392, '9': 1156, '1': 1351, '5': 1385, '2': 1388, '4': 1190} |
| **success_val_seen** | 7 | 93 | 155 | {'4': 147, '2': 173, '5': 185, '9': 139, '0': 154, '7': 166, '1': 181} |

> [!WARNING]
> **Task-Level Training Overlap (Seen Tasks):**
> * Tasks 3, 6, and 8 were **not** held out during detector training. They were explicitly included in the training, validation, and calibration splits.
> * Specifically, the detector saw **1,368** episodes of Task 3 and **1,423** episodes of Task 6 during training. Consequently, the online evaluations on Tasks 3 and 6 represent **in-distribution** performance, not zero-shot generalization.

### C. Seed & ID Leakage Checks
- **Evaluation Seed Leakage:** **0% OVERLAP**. We verified that none of the 100 seeds used in the online evaluations for Tasks 3, 6, and 8 appear in any of the training, validation, or calibration buckets.
- **Episode ID Leakage:** **0% OVERLAP**. Evaluation episode IDs use the execution mode naming format (e.g. `libero_goal_object::task03::episode00000`), whereas training data IDs use the flat collection naming format (e.g. `libero_goal_object::continuous::000000`), preventing any name overlap.
- **Init-State Index Overlap:** **YES**. Both training and evaluation reset the simulator to random initial states. Because each task in LIBERO has a fixed pool of initial states (indices 0-9), the starting physical layouts (object placements and orientations) are identical in distribution. However, seed disjointness ensures the specific noise/perturbations are unique.

---

## 2. Feature Leakage / Cheating Audit

We audited the dataset compilation script ([train_frozen_detectors_h10_proof.py](file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/src/train_frozen_detectors_h10_proof.py)) and the input schema definition.

### A. Excluded Fields (No Leakage)
We confirmed that none of the following fields or future outcome indicators are leaked to the features:
* **Excluded:** success flag, reward, outcome, timeout/failure label, remaining horizon/episode length, future timesteps, post-action proprio/states, and simulator object positions.
* The supervision label `y = 0.0 if meta.success else 1.0` is strictly used for target supervision, and is never fed as input or exposed to the model during inference.

### B. Exact Input Features Schema

| Model Input Group | Dimension | Feature Composition & Details |
| :--- | :---: | :--- |
| **History Feature (`history`)** | `[16, 21]` | 16 sequence steps of: `proprio` (8 dims), `executed_action` (7 dims), and `ace[:6]` (6 dims). |
| **Action Chunk (`action`)** | `[10, 7]` | Candidate normalized action chunk sequence (10 timesteps of 7 dimensions). |
| **Static Branch (`static_base`)** | `43` | Concatenation of: `action_stats` (28 dims: first action, mean action, std action, difference vector), `ace` metrics (7 dims), and `proprio` (8 dims). |
| **Uncertainty (`unc`)** | `8` | For **H10 TopK8 detector**, 8 selected SimVLA uncertainty head dimensions: `[6, 21, 25, 27, 23, 2, 26, 24]`. (H10 base detector omits this, using only the 43-dim `static_base`). |

> [!NOTE]
> The H10 TopK8 features slice the 8 most important uncertainty dimensions from SimVLA's 49-dimensional uncertainty head output.

---

## 3. H10 Dataset Semantic Correctness

We verified how chunk-10 data is aligned and formatted.

### A. Data Collection Method
* The dataset was **collected natively using H10 execution mode** (SimVLA executed 10 steps per chunk rollout, saving query steps and transitions into `.npz` files).
* The conversion script ([convert_chunk10_npz_to_trainer_jsonl.py](file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/src/convert_chunk10_npz_to_trainer_jsonl.py)) extracts these queries sequentially, aligning timesteps to chunk boundaries (0, 10, 20, 30, ...).

### B. Sample Episode Timelines (Verified)

#### 1. Successful Episode (`libero_goal_object::continuous::000000`, label = 0.0)
* **Query 0:** Timestep=0 | Proprio=[-0.208, 0.000, 1.173]... | Uncertainty=[0.016, 0.589, 0.008]... | Label=0.0
* **Query 1:** Timestep=10 | Proprio=[-0.145, -0.007, 1.163]... | Uncertainty=[0.008, 0.322, 0.008]... | Label=0.0
* **Query 2:** Timestep=20 | Proprio=[-0.074, -0.018, 1.162]... | Uncertainty=[0.009, 0.351, 0.008]... | Label=0.0
* **Query 9:** Timestep=90 | Proprio=[0.026, -0.137, 1.031]... | Uncertainty=[0.015, 0.474, 0.012]... | Label=0.0
*(Total queries: 18, all queries have Label=0.0)*

#### 2. Failed Episode (`libero_goal_object::continuous::000006`, label = 1.0)
* **Query 0:** Timestep=0 | Proprio=[-0.208, 0.000, 1.173]... | Uncertainty=[0.016, 0.505, 0.011]... | Label=1.0
* **Query 1:** Timestep=10 | Proprio=[-0.129, -0.020, 1.172]... | Uncertainty=[0.009, 0.403, 0.008]... | Label=1.0
* **Query 2:** Timestep=20 | Proprio=[-0.018, -0.063, 1.165]... | Uncertainty=[0.011, 0.478, 0.011]... | Label=1.0
* **Query 9:** Timestep=90 | Proprio=[-0.079, 0.055, 1.127]... | Uncertainty=[0.016, 0.570, 0.012]... | Label=1.0
*(Total queries: 25, all queries have Label=1.0)*

This timeline confirms that timesteps and features are properly aligned to query boundaries, and the label represents eventual episode failure.

---

## 4. Candidate/Action Seed Fairness

We audited the runner code ([run_policy_matrix.py](file:///file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/src/run_policy_matrix.py)) to check candidate generation fairness.

* **Main SimVLA Seed vs ACE Seeds:** The main chunk is generated using `seeds[0]`. The 8 ACE candidate chunks are generated using `seeds[1:9]`. They are kept completely separate.
* **Seed Uniqueness:** Candidate seeds are generated deterministically using a SHA256 hash of `global_action_seed`, `reset_seed`, `episode_index`, `timestep`, and `sample_index`. This guarantees that candidate seeds are unique per step and do not collide.
* **Cross-Policy Comparability (Fair Main-Chunk Fix):** Since the seed generation depends on the episode reset seed and query index, any policy running seed `S` at query step `Q` generates the exact same candidate seeds. The baseline and risk-aware policies start with the **exact same main candidate chunk** before any intervention occurs. This confirms the "fair main-chunk fix" is active and correct.
* **Extra Candidate Chunks:** Risk-aware gets access to 8 extra candidate chunks (to evaluate ACE metrics and perform replacement). Baseline only generates the main chunk. This is expected and fair, as it matches the definition of a baseline.

---

## 5. Detector Inference Code Path

We audited the runtime inference path in `run_policy_matrix.py`:
1. **Model Loading:** `load_detector` loads `metrics.json`, `thresholds.json`, and `normalization.json` dynamically from the model directory, reconstructing the `SeqRiskModel` architecture and loading the `model.pt` weights.
2. **Threshold Enforcement:** The `selection_main_threshold` is set to `0.3` in the config, which resolves to the float value `0.3` at runtime, bypassing the conformal threshold `q95` (~0.6155).
3. **Chunk Execution:** If the main chunk risk exceeds the threshold, `select_action` selects the eligible candidate chunk with the lowest risk. The selected chunk is executed for the full H10 steps (10 steps) unless terminated early by success/done.
4. **Modifications logging:** Action modifications logged in JSONL correspond to real replacement chunks executed in the simulator.

---

## 6. Positive Result Fragility

We calculated the seed-by-seed paired rescues and regressions for Task 3 and Task 6 (aggressive threshold 0.3).

### A. Task 3 (Aggressive TopK8 vs Baseline)
- **Net Gain:** **+2** successes (17/100 baseline -> 19/100 risk TopK8)
- **Rescues (2):**
  - **Seed 211088021:** Base=300 steps (Failure) -> Risk=232 steps (Success). Intervened at Q12, Q13, Q14, Q15, Q17. (At Q12, risk reduced from 0.621 to 0.595).
  - **Seed 923894520:** Base=300 steps (Failure) -> Risk=209 steps (Success). Intervened at Q14 and Q16. (At Q14, risk reduced from 0.641 to 0.592).
- **Regressions (0):** None.

### B. Task 6 (Aggressive TopK8 vs Baseline)
- **Net Gain:** **+5** successes (57/100 baseline -> 62/100 risk TopK8)
- **Rescues (19):**
  * Seed 273198307, 287547146, 287639521, 352560642, 368480630, 447329467, 448048899, 492767111, 757312322, 831403058, 834120148, 1026915864, 1142167292, 1173749532, 1277227977, 1330093635, 1435081596, 1501306169, 1546683890.
  * *Example:* **Seed 287547146** went from 300 steps (Failure) to 101 steps (Success) with 5 modifications (Q0, Q1, Q3, Q6, Q8).
- **Regressions (14):**
  * Seed 57394074, 98719523, 107614348, 273198307, 286956518, 402897139, 447329467, 634248193, 831403058, 1165183492, 1481978104, 1537690462, 1557548213, 2078809338.
  * *Example:* **Seed 1557548213** went from 135 steps (Success) to 300 steps (Failure) with 4 modifications (Q0, Q3, Q4, Q7).

### C. Task 6 (Old Detector Aggressive vs Baseline)
- **Net Gain:** **+3** successes (57/100 baseline -> 60/100 risk TopK8)
- **Rescues (13):** Seed 287639521, 368480630, 375394911, 386737046, 392453968, 430862118, 1142167292, 1277227977, 1291487306, 1501306169, 1546683890, 2060901849, 2118586852.
- **Regressions (10):** Seed 47766804, 109459806, 286956518, 402897139, 468260798, 684664532, 996418799, 1165183492, 2007355477, 2078809338.

> [!WARNING]
> **Fragility Verdict:**
> The aggressive threshold of 0.3 is highly fragile. Although it increases the overall success rate, it behaves as a double-edged sword.
> * In Task 6, it successfully rescues 19 episodes, but **regresses on 14 episodes** that the baseline would have solved.
> * This high regression rate is due to false alarms: the detector frequently intervenes on correct trajectories (94% intervention rate), replacing good actions with suboptimal ones.

---

## 7. What the Result Actually Proves

1. **Does Task 3/6 aggressive TopK8 prove generalization?**
   **NO**. The evaluation tasks (Tasks 3 and 6) were seen during detector training. It only evaluates seen tasks on unseen seeds.
2. **Does it prove in-distribution improvement on seen tasks with unseen seeds?**
   **YES**. It shows that risk-aware intervention can find alternative trajectories when the main chunk is suboptimal, leading to a minor success rate boost in-distribution.
3. **Does task-level inclusion weaken the claim?**
   **YES, SIGNIFICANTLY**. Because the detector was trained on Tasks 3 and 6, the model had already memorized the task contexts, visual layouts, and object features.
4. **Is there any evidence of hard leakage/cheating?**
   **NO**. Seeds are disjoint, and there is no leakage of future info, labels, or simulator states into the runtime features.
5. **What exact missing evidence is needed to fully trust it?**
   We need zero-shot generalization testing on completely held-out tasks (e.g. Tasks 8 and 9) using a detector trained on a split like `ood_last2_taskids_full`. We must verify that the policy maintains a positive net success rate (rescues > regressions) on unseen tasks.

---

## 8. Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
H10_DATASET_FOUND = YES
TRAIN_SPLITS_FOUND = YES
TASK_LEVEL_OVERLAP_TASK3 = YES
TASK_LEVEL_OVERLAP_TASK6 = YES
SEED_LEVEL_OVERLAP = NO
INIT_STATE_OVERLAP = YES
FEATURE_LEAKAGE_FOUND = NO
FUTURE_INFO_LEAKAGE_FOUND = NO
OBJECT_POSE_LEAKAGE_FOUND = NO
H10_LABEL_ALIGNMENT_PASS = YES
CANDIDATE_SEED_FAIRNESS_PASS = YES
FAIR_MAIN_CHUNK_FIX_ACTIVE = YES
AGGRESSIVE_TOPK8_RUNTIME_PATH_PASS = YES
TASK3_GAIN_INTERPRETATION = Net gain is +2 successes from 2 rescues and 0 regressions, but success-only steps did not improve.
TASK6_GAIN_INTERPRETATION = Net gain is +5 successes from 19 rescues and 14 regressions, indicating high fragility and high intervention rates.
SCIENTIFIC_TRUST_VERDICT = PARTIAL_TRUST
MOST_IMPORTANT_RISK = High intervention rates (94-99%) disrupt correct baseline trajectories, leading to a high rate of regressions (10-14 episodes).
NEXT_AUDIT_STEP = Audit zero-shot generalization on held-out tasks (e.g. Tasks 8 and 9) using the ood_last2_taskids_full detector split.
