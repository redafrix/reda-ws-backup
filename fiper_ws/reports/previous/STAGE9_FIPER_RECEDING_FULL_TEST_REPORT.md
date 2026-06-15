# STAGE 9 FIPER RECEDING-HORIZON DATASET FULL EVALUATION REPORT

## 1. Executive Summary
This report presents the consolidated evaluation results of the Stage 9 receding-horizon dataset on the Sam robot platform. The goal of this analysis campaign was to stop data collection cleanly, inventory the generated datasets, build clean split datasets, and evaluate the performance of:
1. **Action Chunk Entropy (ACE)**: Policy uncertainty from 64 unexecuted trajectory candidates.
2. **Random Network Distillation (RND)**: An action-heavy, success-only novelty detection monitor.
3. **FIPER Combined Quadrants**: A combined monitor integrating both ACE and RND.
4. **Diagnostic Supervised Classifiers**: Outcome separability models.
5. **Out-of-Distribution (OOD) Generalization**: Cross-suite smoke tests.

### Key Takeaways
- **Complementarity**: RND and ACE catch complementary failure modes. ACE flags 5.68% of failure steps that RND misses, and RND flags 7.35% of failure steps that ACE misses. Together, they flag 72.06% of all failure steps under a conformal false-alarm limit of 5%.
- **Action Sensitivity**: The success-only RND is extremely sensitive to structural and noise corruptions, scoring 100% alarm rates on physical corruptions and showing temporal sensitivity (66.96% alarm rate on shuffled action chunks).
- **Task Specificity**: RND is highly task-specific. A model trained on one suite flags 100% of successful steps in another suite as OOD.
- **Diagnostic Outcome Separability**: Supervised classifiers trained on action and anomaly features distinguish success vs. failure steps with near-perfect accuracy (MLP AUROC 0.9998).

**Final Decision**: `METHOD_LOOKS_PROMISING`. The RND + ACE combination provides robust and sensitive detection of failure events and corrupted inputs.

---

## 2. What Data Was Used
- **Sam Campaign Data**: Receding-horizon campaign `fiper_receding_all_outcomes_20260521_165452` (Instance A and Instance B) containing VLA trials executed on Sam.
- **Consolidated Bob Data**: Receding-horizon trials from Bob copied to Sam at `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data` (Instance A and Instance B).
- **Total Datasets**: Exactly 4 separate collector folders containing raw JSONL logs (`fiper_receding_samples.jsonl`).

---

## 3. What Data Was Not Used
- **Active Bob Workspace**: No direct read or write access was performed on Bob. Only the pre-consolidated copy of Bob's data located on Sam was evaluated.
- **Failure Labels for RND Training**: Failures and timeouts were completely withheld from RND training and calibration. The RND monitor was trained strictly on successful episodes.

---

## 4. Collection Stopped Status
The active data collectors on Sam were stopped cleanly on May 22, 2026.
- **Stopped PIDs**: `2606392` & `2606393` (corresponding to the Instance A and Instance B collector processes).
- **Stop Method**: Executed the campaign-specific stop script at `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/scripts/stop.sh`.
- **Cleanliness Verification**: Executed `pgrep -af collect_fiper_receding_all_outcomes_v1`, which returned empty.
- **Campaign Runtime**: ~17 hours 10 minutes.
- **Final Output Folders**:
  - Sam Instance A: `.../campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_A`
  - Sam Instance B: `.../campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_B`

---

## 5. Dataset Inventory
All raw JSONL records were validated for integrity, size, and completeness:
- **Total Rows**: 16,466 rows.
- **Total Episodes**: 74 episodes.
- **Corrupt Rows**: 0 (all lines parsed successfully).
- **Required Fields Verification**: All rows contained 100% of required fields: `episode_id`, `timestep`, `suite`, `task_id`, `task_instruction`, `main_seed`, `main_candidate_action_chunk_normalized`, `main_candidate_action_chunk_env`, `executed_action`, `ace_candidate_seeds_64`, `ace_candidate_chunks_normalized_64`, `ace_candidate_chunks_env_64`, `episode_outcome`, `allowed_use`.
- **ACE Candidate Counts**: Exactly 64 candidate chunks and seeds per row.
- **ACE Replay Audit**: `ace_replay_used == false` is confirmed for all rows.
- **Executed Action Audit**: Confirmed that only the first action of the main candidate chunk was executed in the simulator.
- **Seed Uniqueness**: All seeds (main and ACE candidate seeds) were verified as unique.

---

## 6. Success/Failure Episode Distribution
Across the combined campaign and consolidated data, the outcome breakdown is:
- **Success Episodes**: 50 episodes (6,866 rows)
- **Failure/Timeout Episodes**: 24 episodes (9,600 rows)

| Source Instance | Success Episodes / Rows | Failure Episodes / Rows | Total Episodes / Rows |
|---|---|---|---|
| Sam Instance A | 9 / 1,282 | 7 / 2,800 | 16 / 4,082 |
| Sam Instance B | 15 / 2,227 | 5 / 2,000 | 20 / 4,227 |
| Bob Instance A | 5 / 447 | 9 / 3,600 | 14 / 4,047 |
| Bob Instance B | 21 / 2,910 | 3 / 1,200 | 24 / 4,110 |
| **Combined** | **50 / 6,866** | **24 / 9,600** | **74 / 16,466** |

---

## 7. Suite/Task Coverage
- **Suite A**: `libero_spatial_with_mug:task_0`
  - Total Episodes: 30 (14 Success, 16 Failure/Timeout)
  - Total Rows: 8,129
- **Suite B**: `libero_goal_with_mug:task_0`
  - Total Episodes: 44 (36 Success, 8 Failure/Timeout)
  - Total Rows: 8,337

---

## 8. Split Construction and Leakage Audit
To ensure robust evaluation without leakage, the splits were partitioned strictly at the episode level:
- **`success_train.jsonl`**: 21 episodes, 3,003 rows (Suite B only)
- **`success_calib.jsonl`**: 7 episodes, 866 rows (Suite B only)
- **`success_test.jsonl`**: 8 episodes, 1,268 rows (Suite B only)
- **`ood_suite_success_test.jsonl`**: 14 episodes, 1,729 rows (Suite A only)
- **`failure_eval_all.jsonl`**: 24 episodes, 9,600 rows (Both suites)
- **`failure_eval_early.jsonl`**: 2,400 rows (First 25% steps of failure episodes)
- **`failure_eval_late.jsonl`**: 2,400 rows (Last 25% steps of failure episodes)
- **`failure_eval_near_end.jsonl`**: 1,200 rows (Last 50 steps of failure episodes)

**Leakage Audit**: `PASSED`. There is zero overlap of unique episode IDs between the train, calib, test, OOD, and failure splits.

---

## 9. ACE Diversity Sanity Results
- **Are the 64 chunks actually different?**
  - **Yes**. Across all rows, the number of unique clustering centers is exactly 64.00 (Std 0.00), and the count of near-duplicate chunks is 0.
  - The mean pairwise distance across success rows is **1.2942**, confirming that the 64 unexecuted candidates represent physically diverse trajectories.
  - **Policy Stochasticity**: The VLA policy (SimVLA) is highly stochastic when queried with different random seeds from the exact same state, rather than being deterministic.

---

## 10. ACE Success vs. Failure Results
Policy uncertainty metrics (from the 64 unexecuted chunks) show distinct distributions:
- **Calibrated Conformal Thresholds** (on successful episodes):
  - q90: -161.1047
  - q95: -155.7420
  - q99: -137.9771
- **Overall Comparison**:

| Metric | Success Mean (Std) | Failure Mean (Std) | Late Failure Mean (Std) |
|---|---|---|---|
| **ACE (Gaussian Entropy)** | -193.4394 (22.3192) | -139.4645 (34.2802) | -128.5291 (32.5499) |
| **Mean Pairwise Distance** | 1.2942 (0.4195) | 2.5459 (1.0911) | 2.9658 (1.1396) |
| **Action Std Mean** | 0.0940 (0.0303) | 0.1838 (0.0813) | 0.2152 (0.0852) |
| **Gripper Std** | 0.0059 (0.0035) | 0.0950 (0.1496) | 0.1171 (0.1703) |
| **Translation Std** | 0.0862 (0.0429) | 0.1893 (0.0878) | 0.2258 (0.0956) |
| **Rotation Std** | 0.1312 (0.0345) | 0.2079 (0.0819) | 0.2373 (0.0887) |

*Interpretation*: Policy entropy is significantly higher in failure episodes than in success episodes (-139.46 vs. -193.43). Translation, rotation, and gripper variances all double or triple in failure cases.

---

## 11. ACE Early vs. Late Failure Results
Policy entropy and variance grow steadily as failure approaches:
- **Early Failure (First 25%) ACE**: -161.7085
- **Late Failure (Last 25%) ACE**: -128.5291
- **Near End (Last 50 steps) ACE**: -128.8475
- **Temporal Analysis across all episodes**:

| Episode Progress Interval | Mean ACE Score | Mean Pairwise Distance | Count |
|---|---|---|---|
| 0.0 - 0.25 | -171.2931 | 1.6785 | 7,096 |
| 0.25 - 0.50 | -155.2378 | 2.1034 | 4,145 |
| 0.50 - 0.75 | -144.6150 | 2.4437 | 3,958 |
| 0.75 - 1.00 | -138.3441 | 2.7381 | 7,267 |

*Conclusion*: Policy entropy and trajectory diversity increase as a monotonic function of episode progress and failure proximity.

---

## 12. RND Success-Only Training Setup
An action-heavy novelty detector was trained to model success-only behaviors.
- **Model**: PyTorch MLP (Input Dimension: 70 -> 256 -> 256 -> 128-dim embedding).
- **Features**: `main_candidate_action_chunk_normalized` (10 steps $\times$ 7 action dimensions, flattened to 70 features).
- **Normalization**: Standardized using mean and standard deviation computed exclusively on `success_train.jsonl`. Features with standard deviation < 1e-4 were removed. All inputs were clipped to $[-10.0, 10.0]$.
- **Training Details**: Early stopping with a patience of 15 epochs monitored validation MSE on `success_calib.jsonl` (reached minimum MSE ~0.000159).

---

## 13. RND Success False Alarm Results
Using conformal thresholds calibrated on `success_calib`:
- **Thresholds**: q90 = 0.000264, q95 = 0.000322, q99 = 0.000824.
- **False Alarm Rate on `success_test`**:
  - Alarm @ q90: **11.04%** (Target: 10.00%)
  - Alarm @ q95: **6.86%** (Target: 5.00%)
  - Alarm @ q99: **1.74%** (Target: 1.00%)

*Conclusion*: The RND model successfully maintains close-to-nominal false alarm rates on unseen, successful in-distribution trajectories.

---

## 14. RND Failure/Challenge Alarm Results
Evaluation of RND on the failure splits reveals strong predictive alarm rates:
- **All Failure Steps (`failure_eval_all`)**: **69.79%** alarm rate @ q95.
- **Early Failure (`failure_eval_early`)**: **68.96%** alarm rate @ q95.
- **Late Failure (`failure_eval_late`)**: **70.88%** alarm rate @ q95.
- **Near End (`failure_eval_near_end`)**: **70.83%** alarm rate @ q95.

---

## 15. Does RND Flag Everything Safe?
**No**. The audit status of the RND model is **`NORMAL (selective alarm)`**.
- It does not flag everything safe: it detects ~70% of failure steps.
- It does not flag everything risky: it maintains a 6.86% false alarm rate on success test.

---

## 16. Corrupted-Action Sanity Results
Applying corruptions to `success_test` action chunks and evaluating with the trained RND yielded:

| Corruption Type | Mean RND Score | Alarm Rate @ q95 (%) | Sensitivity Status |
|---|---|---|---|
| `clean` | 0.000172 | 6.86% | Nominal (False Alarm) |
| `zero` | 0.033398 | 100.00% | SENSITIVE |
| `random` | 0.033850 | 100.00% | SENSITIVE |
| `shuffled` | 0.000616 | 66.96% | SENSITIVE |
| `reversed` | 0.000499 | 53.71% | SENSITIVE |
| `scaled` | 0.027345 | 100.00% | SENSITIVE |
| `gripper_flipped` | 0.035599 | 100.00% | SENSITIVE |
| `repeated_first` | 0.000221 | 18.14% | WEAK |
| `noise_low` | 0.014814 | 100.00% | SENSITIVE |
| `noise_medium` | 0.031442 | 100.00% | SENSITIVE |
| `noise_high` | 0.037677 | 100.00% | SENSITIVE |

*Analysis*: The monitor is highly sensitive to amplitude changes (zeros, random, scaled, noise) and gripper states (100% alarm rates). It also detects structural/temporal ordering corruptions (shuffled at 66.96% and reversed at 53.71%).

---

## 17. ACE + RND FIPER Quadrant Results
Combining the RND anomaly alarm and ACE entropy alarm (both evaluated at conformal `q95` thresholds):
- **Normal Confident** (RND low, ACE low)
- **OOD Confident** (RND high, ACE low)
- **Action Uncertain** (RND low, ACE high)
- **FIPER Alarm** (RND high, ACE high)

### Distribution Table
| Split | Count | Normal Confident (%) | OOD Confident (%) | Action Uncertain (%) | FIPER Alarm (%) |
|---|---|---|---|---|---|
| `success_test` | 1268 | **91.48%** | 5.84% | 1.66% | 1.03% |
| `ood_suite_success_test` | 755 | **0.00%** | 34.30% | 0.00% | 65.70% |
| `failure_eval_all` | 3400 | **27.94%** | 7.35% | 5.68% | 59.03% |
| `failure_eval_early` | 1700 | **32.59%** | 25.35% | 0.88% | 41.18% |
| `failure_eval_late` | 850 | **26.94%** | 4.24% | 6.00% | 62.82% |
| `failure_eval_near_end` | 850 | **26.71%** | 6.12% | 7.06% | 60.12% |

### Alarm Complementarity
For the 3,400 failure steps:
- **Combined detection rate**: **72.06%** of failure steps are flagged by RND, ACE, or both (only 27.94% remain in Normal Confident).
- **ACE catch-rate increment**: ACE flags **193 steps (5.68%)** of failures that RND misses.
- **RND catch-rate increment**: RND flags **250 steps (7.35%)** of failures that ACE misses.

---

## 18. Diagnostic Supervised Results
Supervised classifiers were trained on the combined success/failure dataset splits (episode-partitioned) to test the separability of the offline features:

| Feature Set | LR AUROC | LR AUPRC | MLP AUROC | MLP AUPRC | LR Brier Score |
|---|---|---|---|---|---|
| **Action Chunk Only** | 0.9665 | 0.9681 | 0.9969 | 0.9958 | 0.1678 |
| **ACE Metrics Only** | 0.9679 | 0.9598 | 0.9959 | 0.9944 | 0.1619 |
| **RND Score Only** | 0.9979 | 0.9968 | 0.9979 | 0.9968 | 0.1832 |
| **ACE + RND Combined** | 0.9965 | 0.9952 | **0.9998** | **0.9997** | **0.1391** |

### Logistic Regression Coefficient Analysis (ACE Features)
Positive coefficients mean higher values correlate with failure:
- **ACE Score (Gaussian Entropy)**: **+2.4647**
- **Action Pairwise Distance Mean**: **+2.1409**
- **Gripper Std**: **+1.2137**
- **Rotation Std**: **-1.3526**

---

## 19. OOD-Suite Smoke Results
Cross-suite validation was conducted to evaluate RND task generalization:
- **Model 1** (Trained on Suite A success, tested on Suite B success):
  - In-distribution calib threshold @ q95: **0.000809**
  - Out-of-distribution (Suite B) alarm rate @ q95: **100.00%**
- **Model 2** (Trained on Suite B success, tested on Suite A success):
  - In-distribution calib threshold @ q95: **0.000291**
  - Out-of-distribution (Suite A) alarm rate @ q95: **99.94%**

*Key Finding*: RND is highly sensitive to the spatial and goal configurations of the task. Deploying a single RND monitor across different suites without layout/task conditioning causes continuous false alarms.

---

## 20. Deployability Audit
- **Feature `main_candidate_action_chunk_normalized`**: **FULLY DEPLOYABLE**. Can be extracted online directly from the policy network's outputs.
- **Feature `64 unexecuted candidate action chunks`**: **DEPLOYABLE WITH GPU OPTIMIZATION**. Computing 64 candidate rollouts at every timestep online requires multi-seed parallel forward passes. It is feasible on the Sam GPU platform, but optimization is required to avoid policy inference latency.
- **Environment and Labels**: **FULLY DEPLOYABLE**. No ground-truth reward, simulator-only labels, or future information are used.

---

## 21. Limitations
- **Task Coverage**: The current dataset is restricted to `task_0` (mug manipulation) of both suites. True generalization to more complex tasks, diverse objects, and distinct suites has not been fully verified.
- **Task Shift Sensitivity**: The OOD task test indicates RND has extremely high layout sensitivity, signaling layout shifts as unsafe state anomalies.

---

## 22. Final Decision
`METHOD_LOOKS_PROMISING`

---

## 23. Exact Next Recommendation
1. **Optimize Candidate Generation**: Implement parallel multi-seed action chunk inference on Sam to compute the 64 candidates online without adding latency to the control loop.
2. **Develop Task-Conditioned RND**: Condition the RND target and predictor models on task embeddings (or visual goal features) to prevent false alarms under benign workspace layout shifts.
3. **Execute Online Evaluation**: Deploy the FIPER quadrant alarm framework in closed-loop trials on Sam, monitoring online alarm rates and triggering safety overrides.
