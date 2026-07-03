# Step 7 Forensic Sanity Audit Report: Model Identity and Policy-Label Correctness

> [!IMPORTANT]
> This is Step 7 of the read-only forensic sanity audit conducted on the simulation campaign results stored on host **pcrobot**. No experiments were run, no files modified, and no processes restarted. All findings are derived from files, logs, configs, and checksums.

---

## 1. Executive Summary

This audit proves the identity and correctness of all model backbones and risk detectors used across the four simulation campaign roots on Bob (`pcrobot`):
1. **Campaign 1 (In-Distribution Main Campaign):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`
2. **Campaign 2 (In-Distribution Task 3 Aggressive):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`
3. **Campaign 3 (In-Distribution Task 6 Old Detector Aggressive):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`
4. **Campaign 4 (OOD Goal-Swap Campaign):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608`

**Key Findings:**
* **Backbone Verification:** The original SimVLA backbone and the modified SimVLA backbone (with uncertainty head) are verified as architecturally distinct. The modified SimVLA weights (`model.safetensors`) are exactly `28,924 bytes` larger than the original SimVLA weights, corresponding to the added weights of the uncertainty projection and variance prediction layers. Their SHA256 hashes are entirely distinct.
* **Label Correctness:** There are **0 mismatches** between policy labels, configuration files, output directories, and loaded checkpoints/detectors.
* **Risk Base Policy:** The `original_h10_risk_base` policy correctly loaded the original SimVLA backbone and the base risk detector, with no uncertainty head outputs logged.
* **Risk TopK8 Policy:** The `modified_h10_risk_topk8` policy correctly loaded the modified SimVLA (`ckpt-60000`) backbone and the TopK8 risk detector, using the correct dimension indices `[6, 21, 25, 27, 23, 2, 26, 24]`.
* **Ablation Validity:** Campaign 3 successfully ablated the old TopK8 detector, loading the exact old detector weights file (`0ea8e943...`). This old detector was never accidentally loaded in any other campaigns.
* **OOD Integrity:** OOD goal-swap policies strictly adhered to their identity rules, loading the intended backbones and detectors.

---

## 2. Checkpoint Existence and Hash Verification

The following table summarizes the verified file system attributes and SHA256 hashes of all checkpoints and detectors stored on Bob.

| Model / Checkpoint | Target weights file | File Size (Bytes) | SHA256 Hash of weights | Confirmed Files in Folder |
| :--- | :--- | :---: | :--- | :--- |
| **Original SimVLA** | `model.safetensors` | 3,245,529,028 | `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be` | `config.json`, `model.safetensors`, `state.json`, `README.md`, `.gitattributes` |
| **Modified SimVLA (ckpt-60000)** | `model.safetensors` | 3,245,557,952 | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` | `config.json`, `model.safetensors`, `state.json` |
| **H10 Base Detector** | `model.pt` | 2,598,868 | `802413d2b4acfd1e5094da726ad5b0489315efbdf1bd91cc962e73fe8149f702` | `config.json`, `model.pt`, `thresholds.json`, `history.json`, `metrics.json`, `normalization.json` |
| **H10 TopK8 Detector** | `model.pt` | 2,602,964 | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` | `config.json`, `model.pt`, `thresholds.json`, `history.json`, `metrics.json`, `normalization.json` |
| **Old TopK8 Detector** | `model.pt` | 2,602,964 | `0ea8e9431a67c1096cd4342b78e93766767234db294d4d9f86d10937e6a966c7` | `model.pt`, `thresholds.json`, `history.json`, `metrics.json`, `normalization.json` |

> [!NOTE]
> The modified SimVLA weights file is exactly **28,924 bytes** larger than the original SimVLA weights file. This corresponds to the 추가 projection matrices and linear layer parameters of the added uncertainty head, proving they are mathematically distinct.

---

## 3. Detailed Model Identity Analysis

### Original SimVLA: Validation as Paper/Basic Model
* **Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
* **Metadata Evidence:** The folder name corresponds to the Hugging Face repo name of the paper's original model (`YuankaiLuo/SimVLA-LIBERO`). Inside `config.json`, the model type is defined as `"smolvlm_vla"` and the architecture is `"SmolVLMVLA"`. The config contains **no** uncertainty-related parameters.
* **Weights Size:** 3,245,529,028 bytes.
* **Uncertainty Head presence:** Confirmed **ABSENT**.

### Modified SimVLA: Validation of Uncertainty Modification
* **Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
* **Metadata Evidence:** The `config.json` inside the directory contains the following explicit uncertainty parameters:
  * `"predict_uncertainty": true`
  * `"uncertainty_beta": 0.5`
  * `"uncertainty_eps": 1e-06`
* **Weights Size:** 3,245,557,952 bytes (28.9 KB larger).
* **Uncertainty Head presence:** Confirmed **PRESENT**.

---

## 4. Verification of Policy Backbone & Detector Identities

### original_h10_risk_base / risk_base
* **Backbone:** Verified as the **original SimVLA** backbone (hash starting `9d3b1767...`).
* **Detector:** Verified as the **base risk detector** (hash starting `802413d2...`), which does not ingest uncertainty features.
* **Logs & Code:** Logs (e.g. `prod_task3_original_h10_risk_base_s0.log`) confirm no uncertainty log statements or features were output or processed.
* **Naming:** The naming `original_h10_risk_base` is accurate: it uses the `original` SimVLA backbone, execution horizon `10` (`h10`), and the `base` risk detector.

### modified_h10_risk_topk8 / risk_topk8 (Conservative and Aggressive)
* **Backbone:** Verified as the **modified SimVLA** backbone (hash starting `3fab12d9...`).
* **Detector:** Verified as the new **TopK8 risk detector** (hash starting `687b5d35...`) in Campaigns 1, 2, and 4. In Campaign 3 (ablation), it correctly loaded the **old TopK8 detector** (hash starting `0ea8e943...`).
* **Logs & Code:** Step-level scoring logs (`step_scores_risk_topk8.jsonl`) confirm the active ingestion of uncertainty outputs, selecting the TopK8 dimension indices `[6, 21, 25, 27, 23, 2, 26, 24]`.
* **Naming:** The naming is accurate: `modified` matches the modified SimVLA backbone, and `risk_topk8` matches the TopK8 risk detector.

---

## 5. Production Configuration Inventory

Across the four campaign roots, the configuration files were audited and grouped into distinct configurations:

1. **Original SimVLA Baseline (In-Distribution):**
   * Config files: `configs/online/task3_original_simvla_h10_s*.json`, `configs/online/task6_original_simvla_h10_s*.json`, `configs/online/task8_original_simvla_h10_s*.json`
   * Backbone: `YuankaiLuo_SimVLA-LIBERO` (hash: `9d3b1767...`)
   * Detector: None
   * Horizon: 10
   * Output directory: `/runs/online/task{3,6,8}/original_simvla/shard_*`
   * Runner script: `/src/run_policy_matrix.py` (hash: `2e7c64425bdb9f58b8fd612d6af9d50dc6346c8d495cf66774aebc9d601cbf82`)

2. **Modified SimVLA Baseline (In-Distribution):**
   * Config files: `configs/online/task3_modified_simvla_h10_s*.json`, `configs/online/task6_modified_simvla_h10_s*.json`, `configs/online/task8_modified_simvla_h10_s*.json`
   * Backbone: `ckpt-60000` (hash: `3fab12d9...`)
   * Detector: None
   * Horizon: 10
   * Output directory: `/runs/online/task{3,6,8}/modified_simvla/shard_*`
   * Runner script: `/src/run_policy_matrix.py`

3. **Original H10 Risk Base (In-Distribution):**
   * Config files: `configs/online/task3_original_h10_risk_base_h10_s*.json`, `configs/online/task6_original_h10_risk_base_h10_s*.json`, `configs/online/task8_original_h10_risk_base_h10_s*.json`
   * Backbone: `YuankaiLuo_SimVLA-LIBERO` (hash: `9d3b1767...`)
   * Detector: `/models/h10_continuous/all_tasks_random/base` (hash: `802413d2...`)
   * Horizon: 10
   * Output directory: `/runs/online/task{3,6,8}/original_h10_risk_base/shard_*`
   * Runner script: `/src/run_policy_matrix.py`

4. **Modified H10 Risk TopK8 (In-Distribution - Conservative):**
   * Config files: `configs/online/task3_modified_h10_risk_topk8_h10_s*.json`, `configs/online/task6_modified_h10_risk_topk8_h10_s*.json`, `configs/online/task8_modified_h10_risk_topk8_h10_s*.json`
   * Backbone: `ckpt-60000` (hash: `3fab12d9...`)
   * Detector: `/models/h10_continuous/all_tasks_random/unc_topk8` (hash: `687b5d35...`)
   * Uncertainty Dims: `[6, 21, 25, 27, 23, 2, 26, 24]`
   * Threshold: `q95` (conformal)
   * Output directory: `/runs/online/task{3,6,8}/modified_h10_risk_topk8/shard_*`
   * Runner script: `/src/run_policy_matrix.py`

5. **Modified H10 Risk TopK8 (In-Distribution - Aggressive):**
   * Config files: `configs/online/task3_modified_h10_risk_topk8_h10_s*.json`, `configs/online/task6_modified_h10_risk_topk8_h10_s*.json` in Campaign 2
   * Backbone: `ckpt-60000` (hash: `3fab12d9...`)
   * Detector: `/models/h10_continuous/all_tasks_random/unc_topk8` (hash: `687b5d35...`)
   * Uncertainty Dims: `[6, 21, 25, 27, 23, 2, 26, 24]`
   * Threshold: `0.3` (dynamically overridden at run time)
   * Output directory: `/runs/online/task{3,6}/modified_h10_risk_topk8/shard_*`
   * Runner script: `/src/run_policy_matrix.py`

6. **Old TopK8 Detector Aggressive (In-Distribution - Ablation):**
   * Config files: `configs/online/task6_modified_h10_risk_topk8_h10_s*.json` in Campaign 3
   * Backbone: `ckpt-60000` (hash: `3fab12d9...`)
   * Detector: `/realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8` (hash: `0ea8e943...`)
   * Uncertainty Dims: `[6, 21, 25, 27, 23, 2, 26, 24]`
   * Threshold: `0.3`
   * Output directory: `/runs/online/task6/modified_h10_risk_topk8/shard_*`
   * Runner script: `/src/run_policy_matrix.py`

7. **OOD original_simvla (Campaign 4):**
   * Config files: `/configs/production_goal_swap_100ep_20260608/*_original_simvla_100ep.json`
   * Backbone: `YuankaiLuo_SimVLA-LIBERO` (hash: `9d3b1767...`)
   * Detector: None
   * Horizon: 10
   * Output directory: `/runs/production_goal_swap_100ep_20260608/{task_name}/original_simvla`
   * Runner script: `/src/run_policy_matrix.py`

8. **OOD modified_simvla (Campaign 4):**
   * Config files: `/configs/production_goal_swap_100ep_20260608/*_modified_simvla_100ep.json`
   * Backbone: `ckpt-60000` (hash: `3fab12d9...`)
   * Detector: None
   * Horizon: 10
   * Output directory: `/runs/production_goal_swap_100ep_20260608/{task_name}/modified_simvla`
   * Runner script: `/src/run_policy_matrix.py`

9. **OOD risk_topk8 (Campaign 4):**
   * Config files: `/configs/production_goal_swap_100ep_20260608/*_risk_topk8_100ep.json`
   * Backbone: `ckpt-60000` (hash: `3fab12d9...`)
   * Detector: `/models/h10_continuous/all_tasks_random/unc_topk8` (hash: `687b5d35...`)
   * Horizon: 10
   * Threshold: `0.3`
   * Output directory: `/runs/production_goal_swap_100ep_20260608/{task_name}/risk_topk8`
   * Runner script: `/src/run_policy_matrix.py`

---

## 6. Mismatch & Leakage Check Results

A strict validator scanned all 60 configurations and run directories to find any directory or label mismatches, wrong checkpoint folders, base vs TopK8 crossovers, or old detector leakage.
* **Directory vs Checkpoint:** **0 mismatches**. Runs named original loaded original SimVLA, runs named modified loaded `ckpt-60000`.
* **Policy vs Detector:** **0 mismatches**. Base risk runs loaded the base detector, TopK8 runs loaded the TopK8 detector.
* **Old Detector Leakage:** **0 leakage incidents**. The old detector (hash starting `0ea8e943...`) was loaded only in Campaign 3 Task 6 runs. No other campaigns or tasks ever loaded the old detector.
* **OOD goal-swap runs:** **0 conflicts**. All OOD production JSONL policy fields aligned perfectly with their configuration settings and output directories.

---

## 7. Verification of Runtime Logs

Representative logs from Task 3, Task 6, and Campaign 4 OOD runs were inspected.
* **Checkpoint Loading:** Logs contain the line: `[startup] policy=<policy> config=<cfg_path> checkpoint=<ckpt_path>`. The printed checkpoint paths matched the config specification exactly.
* **Uncertainty Output:** In modified SimVLA runs (`modified_simvla` and `modified_h10_risk_topk8`), log signatures and step files show the uncertainty head outputting log-variances. Original SimVLA runs show no uncertainty telemetry, verifying that the uncertainty head did not activate.
* **Threshold Override:** Logs for Campaign 2 and 3 confirm that the gating logic used the aggressive `0.3` threshold.
* **Execution Horizon:** Logged step traces confirm that actions were executed in chunks of `10` steps (H10), consistent with the configs.

---

## 8. Final Audit Table

| Policy Family / Run | Intended Backbone | Verified Backbone | Intended Detector | Verified Detector | Uncertainty Features Used | Checkpoint Hash | Detector Hash | Verdict |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **original_simvla** (ID) | original_simvla | original_simvla | None | None | No | `9d3b1767...` | N/A | **PASS** |
| **modified_simvla** (ID) | modified_simvla | modified_simvla | None | None | Yes | `3fab12d9...` | N/A | **PASS** |
| **original_h10_risk_base** (ID) | original_simvla | original_simvla | base_detector | base_detector | No | `9d3b1767...` | `802413d2...` | **PASS** |
| **modified_h10_risk_topk8 conservative** | modified_simvla | modified_simvla | topk8_detector | topk8_detector | Yes | `3fab12d9...` | `687b5d35...` | **PASS** |
| **modified_h10_risk_topk8 aggressive** | modified_simvla | modified_simvla | topk8_detector | topk8_detector | Yes | `3fab12d9...` | `687b5d35...` | **PASS** |
| **old detector aggressive** (Ablation) | modified_simvla | modified_simvla | old_detector | old_detector | Yes | `3fab12d9...` | `0ea8e943...` | **PASS** |
| **OOD original_simvla** | original_simvla | original_simvla | None | None | No | `9d3b1767...` | N/A | **PASS** |
| **OOD modified_simvla** | modified_simvla | modified_simvla | None | None | Yes | `3fab12d9...` | N/A | **PASS** |
| **OOD risk_topk8** | modified_simvla | modified_simvla | topk8_detector | topk8_detector | Yes | `3fab12d9...` | `687b5d35...` | **PASS** |

---

## 9. Audit Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
ORIGINAL_SIMVLA_IDENTITY_PASS = YES
MODIFIED_SIMVLA_IDENTITY_PASS = YES
ORIGINAL_AND_MODIFIED_DISTINCT = YES
MODIFIED_UNCERTAINTY_HEAD_CONFIRMED = YES
RISK_BASE_BACKBONE = original_simvla
RISK_BASE_DETECTOR_PASS = YES
RISK_TOPK8_BACKBONE = modified_simvla
RISK_TOPK8_DETECTOR_PASS = YES
OLD_DETECTOR_USED_ONLY_IN_OLD_ABLATION = YES
OOD_POLICY_IDENTITY_PASS = YES
ANY_POLICY_LABEL_MISMATCH = NO
ANY_WRONG_CHECKPOINT_FOUND = NO
ANY_WRONG_DETECTOR_FOUND = NO
MODEL_IDENTITY_FINAL_VERDICT = PASS
MOST_IMPORTANT_FINDING = Checkpoints and detectors are verified distinct and correct; no policy label, checkpoint, or detector mismatches were found in any run.
NEXT_AUDIT_STEP = Conclude the forensic audit as all checks (data, seeds, thresholds, and model identities) have passed successfully.
