# FIPER Previous Monitor Architecture Archaeology Report

## 1. Executive Summary
This report presents a thorough read-only archaeology audit of all previous experiments, scripts, and reports exploring alternative monitor architectures, inputs, and datasets beyond the current action-only RND + ACE pipeline for **Stage 9 / LIBERO-PRO / FIPER**. 

Key findings:
- **Expert Transfer Failure**: RND trained strictly on official LIBERO expert demos suffers from severe distribution shift when evaluated on closed-loop receding-horizon sweeps (Recall drops to **10.25%** compared to **55.10%** for ACE-only). Static expert demos do not match closed-loop feedback dynamics.
- **Observation RND Failure**: RND models using observation features (`observation_context_only`, `proprio_only`, and `action_free_with_vlm`) fail. They exhibit extreme distribution shift, flagging **100%** of standard receding rollout success states as anomalous.
- **Temporal History Risk Forecasting works**: Continuous neural risk models using temporal history sequences (specifically `TCN_history_k8` and `residual_mlp_large`) outperform all others in mapping states to continuous risk, achieving Brier scores as low as **0.0061** and generalizing well to held-out tasks.
- **Verification of Pipeline Issues**: Prior iterations suffered from critical validation data leakage (10 demos shared across train/eval splits) and the "Timer Trap" (uncalibrated raw outputs). Both issues have been resolved via group-safe splitting and Platt/Isotonic post-calibration.

---

## 2. Search Scope and Commands Run
We inspected the workspaces of **Sam** (`/home/rootalkhatib/test/reda_ws`) and **Bob** (`/media/rootalkhatib/My Passport/reda_ws`) using passwordless SSH to verify all relevant folders.

### Search Commands Executed:
```bash
# Search for files containing keywords on Sam and Bob
find /home/rootalkhatib/test/reda_ws/fiper_ws /home/rootalkhatib/test/reda_ws/asynchvla_ws -type f \
  \( -name '*scorer*' -o -name '*risk*' -o -name '*rnd*' -o -name '*ace*' -o -name '*entropy*' \
     -o -name '*conformal*' -o -name '*monitor*' -o -name '*anomaly*' -o -name '*ood*' \
     -o -name '*deployment*' -o -name '*fiper*' \) 2>/dev/null
```

### Key Paths Audited:
- [run_observation_rnd_campaign.py](file:///home/rootalkhatib/test/reda_ws/fiper_ws/stage9_v2_tools/run_observation_rnd_campaign.py)
- [stage9_models.py](file:///home/rootalkhatib/test/reda_ws/fiper_ws/stage9_training_experiments/stage9_models.py)
- [stage9_dataset.py](file:///home/rootalkhatib/test/reda_ws/fiper_ws/stage9_training_experiments/stage9_dataset.py)
- [evaluate_fiper_alarms.py](file:///home/rootalkhatib/test/reda_ws/fiper_ws/stage9_training_experiments/evaluate_fiper_alarms.py)
- [STAGE9_VLM_LABEL_AUDIT_EXPERIMENT_REPORT.md](file:///home/rootalkhatib/test/reda_ws/fiper_ws/reports/STAGE9_VLM_LABEL_AUDIT_EXPERIMENT_REPORT.md)
- [STAGE9_LIBERO_EXPERT_TO_RECEDING_ARCHIVE_EVAL_REPORT.md](file:///home/rootalkhatib/test/reda_ws/fiper_ws/reports/previous/STAGE9_LIBERO_EXPERT_TO_RECEDING_ARCHIVE_EVAL_REPORT.md)
- [STAGE9_ARCHIVE_20260522_FULL_ANALYSIS_REPORT.md](file:///home/rootalkhatib/test/reda_ws/fiper_ws/reports/previous/STAGE9_ARCHIVE_20260522_FULL_ANALYSIS_REPORT.md)
- [STAGE9_MIXED_OUTCOME_DIAGNOSTIC_REPORT.md](file:///home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/reports/STAGE9_MIXED_OUTCOME_DIAGNOSTIC_REPORT.md)
- [STAGE9_DENSE_FAILURE_TIMESTEP_TEST_REPORT.md](file:///home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/reports/STAGE9_DENSE_FAILURE_TIMESTEP_TEST_REPORT.md)

---

## 3. Inventory Table of All Relevant Old Experiments

| ID | Description / Feature Mode | Inputs Used | Architecture / Model | Datasets | Trustworthy / Obsolete | Key Metrics |
|---|---|---|---|---|---|---|
| **EXP1** | **Action RND-OE (Archive-Trained)** | Action chunk only (10x7, 70 dims) | PyTorch MLP target/predictor | Receding sweeps success train/calib | **Trustworthy** (best baseline) | FAR: **8.10%**, Recall: **14.55%**, Corrupted alarm: **94.85%** |
| **EXP2** | **Action RND-OE (Expert-Trained)** | Action chunk only (10x7, 70 dims) | PyTorch MLP target/predictor | Official LIBERO expert demos | **Obsolete** (Poor Closed-Loop Transfer) | FAR: **1.47%**, Recall: **10.25%**, Corrupted alarm: **99.93%** |
| **EXP3** | **Action Chunk Entropy (ACE)** | 8 parallel candidate chunks | Gaussian Entropy (unsupervised) | Receding sweeps calibration | **Trustworthy** (key policy variance signal) | FAR: **8.98%**, Recall: **55.10%** (Late failure: **82.23%**) |
| **EXP4** | **Combined FIPER OR/AND** | Action chunks + Candidate entropy | Conformal threshold OR/AND | Receding sweeps calib/test | **Trustworthy** (complementary) | Combined Recall (OR): **55.16%** - **58.52%** |
| **EXP5** | **Continuous Neural Risk (V2)** | Context (80) + Action (70) + History (136) | Residual MLP, LSTM, GRU, TCN | Final 20h Sweeps (`v2_mass` + failure) | **Partly Trustworthy** (split leakage found/fixed) | TCN Val Brier: **0.0061**, Res-MLP Val Brier: **0.0510** |
| **EXP6** | **Observation-Only RND** | Proprio + Joint states + EE states (21 dims) | RND-OE MLP | Receding sweeps train/calib | **Obsolete** (Extreme domain shift false alarms) | FAR on sweep test: **7.28%** (ID), **66.06%** (OOD task). Rollouts FAR: **100%** |
| **EXP7** | **VLM Label Auditor** | Contact sheets of visual states | Qwen3-VL-2B (blind) / Qwen2.5-VL-3B | Selected suspicious `VALIDATED_BAD` | **Trustworthy** (pipeline works) but not as standalone labeler | Blind Qwen3 judged **40/40** old `VALIDATED_BAD` samples as visually successful |
| **EXP8** | **Mini-Failure Heuristic Detector** | Gripper + EEF positions + object motion | Heuristic rule-based onset detector | Raw failure trajectories | **Trustworthy** (after approach motion fix) | Processed 7 episodes: 18 events (7 wrong object picked, 6 missed place) |

---

## 4. Detailed Findings Per Experiment

### EXP1 & EXP2: Action-Only RND-OE (Archive-Trained vs Expert-Trained)
- **Inputs**: Flattened action chunk `(10, 7) = 70` dimensions.
- **Findings**: RND trained on static expert demos fails when migrating to closed-loop rollouts. Closed-loop rollouts contain feedback oscillation patterns that RND flags as anomalous. RND trained on successful receding rollouts generalizes better, yielding **14.55%** recall compared to **10.25%** for expert-trained RND. 
- **Ablation**: Including `libero_90` tasks in expert training degraded performance by raising false alarm rates on standard test sets (Harmful overfit).

### EXP3 & EXP4: Action Chunk Entropy (ACE) and Combined FIPER
- **Inputs**: Unexecuted 8 candidate action chunks from SimVLA forward pass.
- **Findings**: Policy entropy (ACE) monotonically increases as the robot approaches failure (Early: **-199.16**, Late: **-194.45**). It is a highly robust domain-agnostic indicator because it generalizes across environmental and task perturbations. Combining RND and ACE via an **OR** trigger is highly recommended; RND catches high-amplitude structural anomalies (e.g., action corruptions) while ACE catches policy confusion (high entropy).

### EXP5: Continuous Neural Risk Models (Stage 9 / FIPER V2)
- **Inputs**: Full concatenated vector of context, action, and history (286 dims).
- **Findings**: History-based models outperform simple action-only or context-only MLPs. **`TCN_history_k8`** achieved the lowest validation Brier score (**0.0061**). Time-blind **`residual_mlp_large`** performed best among MLPs (Brier **0.0510**, MAE **0.0309**). 
- **Timer Trap**: Early training runs suffered from raw, uncalibrated probability outputs. This was fixed by using $(\text{AUROC}, -\text{Brier})$ as a validation checkpoint selection key, training for 100 epochs, and applying Isotonic or Platt calibration, which reduced ECE from **22.33%** to **0.00%**.
- **Critical Leakage**: Audit of splits under `STAGE9_FIPER_V2` revealed that chunks from the **exact same 10 expert demonstrations** leaked across train, calib, and test sets. This was resolved in `hard_eval_v2` by enforcing group-safe partitioning.

### EXP6: Observation RND-OE Campaign
- **Inputs**: Mode A: `observation_context_only` (21 dims); Mode B: `proprio_only` (8 dims).
- **Findings**: Complete failure. Observation space RND models are hyper-sensitive to closed-loop execution. Successful rollouts exhibit minor oscillations in joint/EE spaces that never occur in demonstration splits. As a result, the RND scores on rollout data were `0.0204`, far exceeding the calibrated threshold `0.0004`, causing **100% false alarms** on successful trials.

### EXP7: VLM Label Auditor
- **Method**: Running Qwen3-VL-2B (Bob) and Qwen2.5-VL-3B (Sam) blind to audit labels.
- **Findings**: Visual audits showed that the old `VALIDATED_BAD` labels were highly contaminated. The VLM judged 40/40 samples of `bad_no_raw_local_bad` and `bad_terminal_timeout` as successful. This confirmed that outcome-based labeling backfilled bad labels to visually correct steps. Over **2,230** samples were recommended for downgrade to `AMBIGUOUS`.

### EXP8: Heuristic Mini-Failure Event Detector
- **Method**: Local physical rules (object speed, gripper state, lift height).
- **Findings**: Successfully isolates precise failure onsets (e.g. `wrong_object_picked`, `missed_pick`, `drop_or_slip`). It avoids outcome contamination. The early version had false positives during `TRANSPORT` (EEF approach motion was credited as progress), which was fixed by restricting eef approach credit to the grasp phase.

---

## 5. Best Old Ideas Worth Reusing
1. **TCN History Architecture (`TCN_history_k8`)**: Excellent at processing temporal history sequences without the high latency of LSTMs.
2. **Action-Only RND-OE (Archive-Trained)**: Extremely sensitive to corrupted actions (94.85% recall) and acts as a strong safeguard when combined with ACE.
3. **Isotonic Regression / Platt Scaling Calibration**: Mandatory post-processing. Platt scaling reduces ECE to ~0.5%, and Isotonic regression reduces ECE to ~0.00% in-distribution, resolving the Timer Trap.
4. **Heuristic Mini-Failure Event Detector**: Crucial post-processor for clean local annotation of trajectory databases.

---

## 6. Ideas That Failed or Are Not Trustworthy
1. **Observation/Context-only RND-OE**: Failed completely due to closed-loop proprioceptive distribution shifts.
2. **Official LIBERO Expert Demo RND**: Poor transfer to closed-loop receding rollouts.
3. **Outcome-based Terminal BAD Labels**: Obsolete and contaminated. 
4. **Training directly on growing live JSONLs**: Fails due to script crash and concurrency conflicts. Data must be frozen first.

---

## 7. Any Context-Aware / Observation-Aware Models Found
Yes. 
- **RND-OE Campaign**: Evaluated `observation_context_only` (proprio + joints + ee states = 21 dims) and `proprio_only` (8 dims). Failed due to 100% false alarms.
- **Stage 9 Risk Models**: Evaluated `context_action_mlp` (150 dims) and `gated_context_action_mlp` (150 dims). These models combined proprio and 24 object positions (3D vectors) with candidate actions. They generalized successfully to held-out tasks when trained as neural regressors.

---

## 8. Any Action-Scorer Variants Found
Yes. 
- **Continuous Scorer (`local_chunk_quality.py`)**: Computes progress/no-progress scores based on physical credits (EEF approach, lift, object movement).
- **Mini-Failure Event Detector (`detect_mini_failures.py`)**: Classifies specific physical execution bugs.
- **Continuous Neural Risk Regressors**: Forecast risk scores using MLPs, RNNs, and TCNs.

---

## 9. Any Early-Detection/OOD Lessons Found
- **ACE Temporal Progression**: Policy entropy increases monotonically as failure approaches. ACE is highly robust to OOD task/layout shifts because it monitors internal generation stochasticity.
- **RND OOD False Alarms**: RND is highly layout-sensitive. Training on a single task layout (e.g. mug) causes a **29.00%** false alarm rate on held-out suites.
- **Calibration Shift**: Post-calibration ECE degrades on OOD tasks (e.g., ECE goes from 0.00% ID to **23.48%** on OOD tasks). Calibrating strictly on success data maintains low false alarm rates.

---

## 10. Recommended Next Model Design Based on Archaeology
Based on our findings, we recommend:
1. **Inputs**: Combine **Action Chunks** with **Temporal History Sequences (K=8)** containing `proprio` + `executed_actions` + `rewards` + `success`. Exclude task/suite ID embeddings to ensure domain transfer.
2. **Architecture**: Implement **`TCN_history_k8`** or **`residual_mlp_large`** as the main risk regression backbone.
3. **Out-of-Distribution Safeguard**: Combine the neural risk model with **ACE (Gaussian Entropy)** via an **OR** triggering condition.
4. **Calibration**: Apply **Isotonic Calibration** post-inference. Calibrate thresholds strictly on successful closed-loop receding trials to avoid the Timer Trap.

---

## 11. Exact Files Read
- [STAGE9_LIBERO_EXPERT_TO_RECEDING_ARCHIVE_EVAL_REPORT.md](file:///home/redafrix/tests/internship/fiper_ws/reports/previous/STAGE9_LIBERO_EXPERT_TO_RECEDING_ARCHIVE_EVAL_REPORT.md)
- [STAGE9_ARCHIVE_20260522_FULL_ANALYSIS_REPORT.md](file:///home/redafrix/tests/internship/fiper_ws/reports/previous/STAGE9_ARCHIVE_20260522_FULL_ANALYSIS_REPORT.md)
- [STAGE9_VLM_LABEL_AUDIT_EXPERIMENT_REPORT.md](file:///home/redafrix/tests/internship/codex_reports/stage9/STAGE9_VLM_LABEL_AUDIT_EXPERIMENT_REPORT.md)
- [STAGE9_CODEX_ONBOARDING_CURRENT_STATE_AUDIT.md](file:///home/redafrix/tests/internship/codex_reports/stage9/STAGE9_CODEX_ONBOARDING_CURRENT_STATE_AUDIT.md)
- [stage9_models.py](file:///home/redafrix/tests/internship/fiper_ws/stage9_training_experiments/stage9_models.py)
- [stage9_dataset.py](file:///home/redafrix/tests/internship/fiper_ws/stage9_training_experiments/stage9_dataset.py)
- [run_observation_rnd_campaign.py](file:///home/redafrix/tests/internship/fiper_ws/stage9_v2_tools/run_observation_rnd_campaign.py)
- [evaluate_fiper_alarms.py](file:///home/redafrix/tests/internship/fiper_ws/stage9_training_experiments/evaluate_fiper_alarms.py)

---

## 12. Exact Commands Run
- `ssh sam "find /home/rootalkhatib/test/reda_ws/fiper_ws /home/rootalkhatib/test/reda_ws/asynchvla_ws ..."`
- `ssh sam "cat /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/experiments/stage9_fiper_v2_sam_20h_20260520_173700/reports/STAGE9_FIPER_V2_HARD_EVAL_FINAL_REPORT.md"`
- `ssh sam "cat /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/experiments/stage9_fiper_v2_sam_20h_20260520_173700/reports/STAGE9_FIPER_V2_SAM_20H_FINAL_REPORT.md"`
- `ssh sam "cat /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/reports/STAGE9_DENSE_FAILURE_TIMESTEP_TEST_REPORT.md"`
- `ssh sam "cat /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/reports/STAGE9_MIXED_OUTCOME_DIAGNOSTIC_REPORT.md"`
- `ssh sam "cat /home/rootalkhatib/test/reda_ws/fiper_ws/experiments/success_only_fiper_20260521_102354/rnd_observation_only_fix_20260521_112832/all_modes_summary.json"`

---

## Final Fields
```text
CONTEXT_AWARE_MODEL_FOUND = YES
ACTION_SCORER_VARIANTS_FOUND = YES
BEST_REUSABLE_OLD_IDEA = TCN_history_k8
OLD_RESULTS_TRUSTWORTHY = MIXED
RECOMMENDED_NEXT_IMPLEMENTATION = TCN_history_k8 combined with ACE (OR trigger) and Isotonic calibration post-inference.
```
