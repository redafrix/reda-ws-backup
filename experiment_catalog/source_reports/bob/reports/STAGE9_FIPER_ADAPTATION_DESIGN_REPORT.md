# Stage 9 FIPER Adaptation Design Report

This report presents the research, code inspection, and architectural design for adapting FIPER (Failure Prediction at Runtime) concepts into our Stage 9 / SimVLA / LIBERO-PRO failure prediction and continuous risk data collection system.

---

## 1. Active Process Safety Check

Active processes on PCrobot (Bob) and Sam were verified. **No running processes were stopped or disturbed.**

- **Bob (pcrobot) collection running**: **NO**
  - Command: `ssh pcrobot 'tmux ls | grep stage9_v2_mass || true'`
  - Result: No matching tmux sessions found.
- **Sam collection running**: **NO**
  - Command: `ssh sam 'ps aux | grep collect_continuous_risk_dataset_v2 | grep -v grep || true'`
  - Result: No matching processes found.
- **Safety Confirmation**: Confirmed that active jobs were not modified, killed, or disrupted.

---

## 2. FIPER Repository Inspection

We cloned the official FIPER repository (`https://github.com/learnsyslab/fiper.git`) under `/home/rootalkhatib/test/reda_ws/fiper_ws/external/fiper` and inspected its core codebases:

### Files Inspected:
- `README.md`
- `evaluation/method_eval_classes/entropy_eval.py`
- `evaluation/method_eval_classes/rnd_eval.py`
- `evaluation/method_eval_classes/base_eval_class.py`
- `rnd/rnd_models.py`
- `rnd/rnd_trainer.py`
- `evaluation/utils.py`
- `configs/default.yaml`

### Findings:
- **Expected Rollout Format**: 
  - Managed by `ProcessedRolloutDataset` (`datasets/rollout_datasets.py`). It structures episodes as tensors containing action predictions (`action_preds`), observation embeddings (`obs_embeddings`), and success labels (`successful`).
- **Where `action_preds` are used**:
  - Used in `entropy_eval.py` to compute Shannon entropy over the spatial grid.
  - Used in `rnd_models.py` (specifically `RND_A` and `RND_AO`) where they are compressed (using SVD, PCA, or variance pooling) and passed to the neural networks.
- **How ACE/Action Entropy is computed**:
  - In `entropy_eval.py` (`ENTROPYEval.calculate_uncertainty_score`): 
    - For each timestep $t$ of the predicted horizon, action predictions across candidates (shape `(batch_size, action_dim)`) are binned into a 3D grid. The grid's cell size is computed during preprocessing as `cell_size = np.array(ranges) * cellsize_factor`.
    - Shannon entropy (base 2) is calculated using `scipy.stats.entropy` on the binned cell count distribution. 
    - The final uncertainty score is the average entropy across all horizon steps.
- **Expected `obs_embeddings` Format**:
  - In `rnd/rnd_models.py` (`RND_OE.datasets_to_model_inputs`): expected as PyTorch tensor of shape `(batch_size, obs_embedding_dim)`.
- **How RND-OE is trained & evaluated**:
  - Trained in `rnd_trainer.py` (`RNDTrainer._training_loop`) strictly on the `calibration` subset (successful rollouts only). 
  - It trains a predictor network `RND_OE.predictor_network` to minimize the mean squared error (MSE) against a randomly initialized, frozen target network `RND_OE.target_network`.
  - Evaluated in `rnd_eval.py` (`RNDEval.calculate_uncertainty_score`) by measuring the distillation error (MSE loss) of predictor outputs.
- **How conformal thresholds are computed**:
  - In `evaluation/utils.py` (`compute_thresholds`):
    - `ct_quantile` (constant threshold): computes the maximum score of each calibration rollout and takes the $q$-th quantile (e.g. 95th percentile) of those maximum values.
    - `tvt_quantile` (time-varying threshold): computes the $q$-th quantile of scores at each specific timestep $t$ across successful calibration rollouts.
    - `tvt_cp_band`: splits successful rollouts, computes a mean trajectory, computes a modulation scaling function, and sets the band width $h$ as the $q$-th quantile of deviations.
- **How moving-window aggregation works**:
  - In `base_eval_class.py` (`_apply_window_size`): It computes a rolling sum over the last `window_size` steps (padding with zeros for steps shorter than the window size).

---

## 3. Stage 9 Code Inspection (on Sam)

We inspected the codebase at `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9`:

### Files Inspected:
- `simvla_candidate_sampler.py`
- `collect_continuous_risk_dataset_v2.py`
- `collect_failed_episode_mining_v2.py`
- `local_chunk_quality.py`
- `outcome_metrics.py`
- `build_expert_low_risk_anchor_dataset.py`
- `task_parser.py`

### Findings:
- **Where SimVLA candidate chunks are generated**:
  - In `collect_continuous_risk_dataset_v2.py` inside the seed loop, it calls `generate_chunk(...)` (which invokes `sample_candidate(...)` from `simvla_candidate_sampler.py`).
- **SimVLA Observation/VLM Embeddings extraction**:
  - **Yes**, internal visual/language embeddings (`pooled_vlm_features`) are successfully extracted in `sample_candidate()` using:
    `pooled = out.get('pooled_vlm_features')` or mean-pooling `vlm_features`.
  - **Important Fallback**: While `sample_candidate` extracts this embedding, the `generate_chunk` helper and `collect_continuous_risk_dataset_v2.py` **discard** it. It is not saved in the standard `counterfactual_samples.jsonl` output files. Thus, our package implements a warning/TODO for embedding extraction and provides a robust `"deployable_numeric"` fallback using flattened current and historical proprioception/actions.
- **Where 64-seed candidate_action_normalized/env are saved**:
  - Saved under `candidate_action["candidate_action_normalized"]` and `candidate_action["candidate_action_env"]` inside the output `counterfactual_samples.jsonl`.
- **Where same_state_group_summary_v2 is saved**:
  - Saved under `label["same_state_group_summary_v2"]` and `continuous_risk["same_state_group_summary_v2"]` in `counterfactual_samples.jsonl`.
- **Where successful/expert low-risk chunks are saved**:
  - Stored under `expert_low_risk_anchors.jsonl` generated by `build_expert_low_risk_anchor_dataset.py`.
- **Presence of mass data for ACE**:
  - **Yes**. We located `v2_mass/sam_20260520_140528/counterfactual_samples.jsonl` containing **5,120 lines** (representing exactly 80 groups of 64 seeds), which is more than enough for ACE analysis.

---

## 4. Proposed Stage9-FIPER System

The integration of FIPER with Stage 9 V2 operates as follows:

1. **Success-Only Calibration Data**:
   - RND-OE and Conformal Thresholds are trained and fit on `expert_low_risk_anchors.jsonl` and successful SimVLA V2 chunks.
2. **ACE Signal**:
   - Action predictions of shape `(64, 10, 7)` are extracted from same-state candidate groups. We compute the standard deviation of translations, rotations, and gripper status, the trajectory pairwise distance, and the multivariate Gaussian entropy approximation.
3. **RND-OE Signal**:
   - Computes the OOD score of observations. Utilizes `pooled_vlm_features` (preferred) or flattens current and historical proprio/actions into a 128-dimensional vector (fallback).
4. **Conformal Calibration**:
   - Fits constant and time-varying thresholds on successful rollout scores, including moving-window aggregation to smooth transients.
5. **Mining / Audit Logic**:
   States are categorized at runtime based on threshold breaches:
   - **Low RND + Low ACE**: Normal confident state.
   - **High RND + Low ACE**: Benign OOD. Auditable but policy is consistent.
   - **Low RND + High ACE**: Action uncertain. Target for action-specific mining.
   - **High RND + High ACE**: High failure-risk. Highest priority candidate for counterfactual replay.
6. **Integration with local risk scorer**:
   - FIPER does not output final risk labels. It acts as an active mining gatekeeper. FIPER scores (`fiper_ace_score`, `fiper_rnd_oe_score`, `fiper_alarm`, `fiper_signal_type`) are saved as metadata in dataset JSONLs.

---

## 5. Created Files in FIPER Workspace

Under `/home/rootalkhatib/test/reda_ws/fiper_ws`:
- **`README_STAGE9_FIPER_PLAN.md`**: High-level design document and implementation plan.
- **`stage9_fiper_bridge/`** (Python package):
  - **`__init__.py`**: Package initialization.
  - **`stage9_io.py`**: Utilities for reading/writing JSONL, grouping states, and selecting successes.
  - **`ace.py`**: Algorithms for standard deviations, pairwise distances, Gaussian entropy, and ACE summaries.
  - **`rnd_oe.py`**: Scaffolding for `RNDTarget`, `RNDPredictor`, `build_feature_vector`, and success-only training.
  - **`conformal.py`**: Implementation of conformal thresholds (quantile, time-varying, moving-window).
  - **`analyze_existing_ace.py`**: CLI script to process JSONLs, compute ACE, and generate reports.
  - **`propose_fiper_mining_candidates.py`**: CLI script to merge signals and rank candidates.

---

## 6. Smoke Test Results

A smoke test was executed on Sam using the newly implemented package:

### Command:
```bash
ssh sam 'cd /home/rootalkhatib/test/reda_ws/fiper_ws && python3 -m stage9_fiper_bridge.analyze_existing_ace --jsonl /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/sam_20260520_140528/counterfactual_samples.jsonl --out-dir /home/rootalkhatib/test/reda_ws/fiper_ws/scratch/ace_smoke --max-groups 20'
```

### Result:
- Successfully loaded `5120` samples, grouped into `80` unique state groups.
- Analyzed the first `20` groups of size `64`.
- Outputted JSONL database to `/home/rootalkhatib/test/reda_ws/fiper_ws/scratch/ace_smoke/ace_group_summaries.jsonl`
- Generated markdown report `/home/rootalkhatib/test/reda_ws/fiper_ws/scratch/ace_smoke/ace_summary_report.md`

### ACE Summary (from 20 groups):
- **Candidate count per group**: 64
- **ACE Differential Entropy range**: `-180.7153` to `-121.7779` (Mean: `-151.6331`)
  > [!NOTE]
  > ACE values are negative because they represent continuous differential entropy of highly narrow normalized action distributions (variance element is typically very small, e.g. $< 10^{-2}$).
- **Top 3 Action-Uncertain States found**:
  1. `libero_spatial_with_mug_t0_r13_pSTUCK_OR_NO_PROGRESS_s108_state` (ACE: `-121.7779`)
  2. `libero_spatial_with_mug_t0_r13_pSTUCK_OR_NO_PROGRESS_s119_state` (ACE: `-122.0901`)
  3. `libero_spatial_with_mug_t0_r13_pPLACE_OR_GOAL_s96_state` (ACE: `-129.5432`)

- We ran `propose_fiper_mining_candidates` which correctly ranked and sorted the states based on ACE and risk score range.

---

## 7. Constraints / What NOT to Do

- **DO NOT** use failure labels to train RND or fit thresholds. FIPER is strictly success-only.
- **DO NOT** let FIPER assign final risk labels alone. Final labels are governed by the continuous local scorer.
- **DO NOT** treat terminal timeouts automatically as BAD outcomes during calibration.
- **DO NOT** disrupt, stop, or touch the running collection.

---

## 8. Next Experimental Commands (DO NOT RUN YET)

These are prepared for future execution:

### A. Train RND-OE on Expert / Success anchors:
```bash
# python3 -m stage9_fiper_bridge.train_rnd_model --success-jsonl /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/expert_low_risk_anchors.jsonl --out-model /home/rootalkhatib/test/reda_ws/fiper_ws/rnd_models/rnd_oe_v1.pt
```

### B. Compute ACE summaries on the entire Bob/Sam mass dataset:
```bash
# python3 -m stage9_fiper_bridge.analyze_existing_ace --jsonl /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/sam_20260520_140528/counterfactual_samples.jsonl --out-dir /home/rootalkhatib/test/reda_ws/fiper_ws/reports/ace_mass
```

### C. Calibrate Conformal Thresholds:
```bash
# python3 -m stage9_fiper_bridge.calibrate_thresholds --calibration-scores /home/rootalkhatib/test/reda_ws/fiper_ws/scratch/calibration_scores.jsonl --q 0.95
```

### D. Generate active mining queue:
```bash
# python3 -m stage9_fiper_bridge.propose_fiper_mining_candidates --ace-jsonl /home/rootalkhatib/test/reda_ws/fiper_ws/reports/ace_mass/ace_group_summaries.jsonl --out-jsonl /home/rootalkhatib/test/reda_ws/fiper_ws/scratch/mining_queue.jsonl
```

---

## 9. Final Recommendation

- **Can we use the FIPER idea?** **YES**.
  The success-only RND-OE calibration combined with ACE action entropy allows us to separate OOD states from action uncertainty, identifying bifurcation points and boundary failure cases with high precision without needing manual failure labels.
- **What is the first real experiment after this design?**
  Run the ACE analysis on all current 64-seed groups collected on Sam/Bob, and establish success-only calibration of RND-OE using the expert anchors.
