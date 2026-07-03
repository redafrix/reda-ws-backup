# DEAN FIPER UNCERTAINTY COLLECTION DISCOVERY & AUDIT REPORT

**Date:** May 29, 2026  
**Status:** BLOCKED (Pending Checkpoint Sync and Environment Repair)  
**Workspace:** `/home/redafrix/tests/internship/fiper_ws`

---

## 1. Executive Summary

This report evaluates the readiness of the remote host **Dean** (IP: `100.124.50.124`) for running a new FIPER-style data collection campaign using the fine-tuned SimVLA checkpoint `/home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-60000`. Our investigation reveals that while Dean's hardware (RTX A5000, 24GB VRAM) and the LIBERO-PRO simulation environments are fully operational, the campaign is currently **blocked** by two major missing pieces: (1) the `ckpt-60000` weight file (`model.safetensors`) is missing on Dean (it only exists on Sam at `/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000`), and (2) the `simvla` Conda environment on Dean is broken due to a missing `tqdm` dependency, preventing Hugging Face `transformers` from importing. We recommend resolving these blockers, copying the trusted FIPER collector scripts to Dean, and adapting them to compute and record the 49-dimensional uncertainty trace features during rollouts.

---

## 2. Dean Access and Hardware

System information and hardware statistics were audited directly on Dean:

*   **Hostname:** `Batman` (Identified as remote host `100.124.50.124` running Tailscale).
*   **GPU Model:** `NVIDIA RTX A5000` (Persistence-M: On, Driver Version: 580.95.05, CUDA Version: 13.0).
*   **VRAM status:**
    *   **Total:** `24,564 MiB`
    *   **Used:** `15 MiB` (Idle, only standard Xorg process of 4MiB active).
*   **GPU Temperature & Utilization:**
    *   **Utilization:** `0%`
    *   **Temperature:** `43°C`
    *   **Power Draw:** `21W / 230W`
*   **RAM status:**
    *   **Total:** `31 GiB`
    *   **Used:** `7.5 GiB`
    *   **Free/Cache:** `23.2 GiB` (available memory: `22 GiB`).
*   **Disk space (Relevant paths `/` and `/home/redafrix`):**
    *   **Filesystem:** `/dev/sda2`
    *   **Total Size:** `469 GiB`
    *   **Used:** `347 GiB`
    *   **Free Space:** `98 GiB` (79% Utilization).
*   **Active Python/Tmux processes:** No active data-collection processes or tmux sessions are running. Only standard background system processes (`networkd-dispatcher`, `unattended-upgrades`, `gnome-terminal`) are present.

---

## 3. Workspace and Path Inventory

A detailed directory audit on Dean verified the presence of the following paths:

*   **`/home/redafrix/SimVLA_modified`:** **EXISTS** (Healthy git workspace).
*   **`/home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-60000`:** **PARTIALLY EXISTS** (Contains only `config.json` and `state.json`. **`model.safetensors` weight file is MISSING**).
*   **`/home/redafrix/SimVLA_modified/evaluation/libero/collect_phase2_tdqc_balanced_per_task.sh`:** **EXISTS** (Shell collector script).
*   **`reda_ws`:** **DOES NOT EXIST** on Dean (Exists locally and on Bob/Sam).
*   **`fiper_ws`:** **DOES NOT EXIST** on Dean (Exists locally and on Bob/Sam).
*   **`asynchvla_ws`:** **DOES NOT EXIST** on Dean (Exists on Sam).
*   **LIBERO assets/config paths:** **EXISTS** (Configured benchmark root `/home/redafrix/LIBERO-PRO/libero/libero`).
*   **BDDL paths:** **EXISTS** (`/home/redafrix/LIBERO-PRO/libero/libero/bddl_files`).
*   **Official LIBERO dataset/demo paths:** **DOES NOT EXIST** (Missing HDF5 files).
*   **LIBERO-PRO/custom suite paths:** **EXISTS** (`/home/redafrix/LIBERO-PRO`).

---

## 4. Environment Audit

Dean has two primary Conda environments: `libero` and `simvla`.

### Libero Conda Environment (`libero`)
*   **Path:** `/home/redafrix/miniconda3/envs/libero`
*   **Python version:** `3.8.13`
*   **Torch version:** `1.11.0+cu113`
*   **CUDA available:** `True`
*   **CUDA device name:** `NVIDIA RTX A5000`
*   **Import verification:**
    *   `torch` -> `import successful`
    *   `libero` -> `import successful`
    *   `robosuite` -> `import successful` (resolves to `/home/redafrix/miniconda3/envs/libero/lib/python3.8/site-packages/robosuite/__init__.py`)
    *   `mujoco` -> `import successful` (version `3.2.3`)

### SimVLA Conda Environment (`simvla`)
*   **Path:** `/home/redafrix/miniconda3/envs/simvla`
*   **Python version:** `3.10.20`
*   **Torch version:** `2.6.0+cu124`
*   **CUDA available:** `True`
*   **Import verification:**
    *   `torch` -> `import successful`
    *   `transformers` / `huggingface_hub` -> **FAILED** due to missing `tqdm` module.
*   **Traceback Snippet:**
    ```python
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/transformers/__init__.py", line 27, in <module>
        from . import dependency_versions_check
      ...
      File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/huggingface_hub/__init__.py", line 1044, in __getattr__
        submod = importlib.import_module(submod_path)
      File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/huggingface_hub/hf_api.py", line 52, in <module>
    Error importing huggingface_hub.hf_api: No module named 'tqdm'
        from tqdm.auto import tqdm as base_tqdm
    ModuleNotFoundError: No module named 'tqdm'
    ```

---

## 5. Checkpoint Audit

The checkpoint `/home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-60000` was audited:

*   **Files present on Dean:**
    *   `config.json` (Size: 570 bytes)
    *   `state.json` (Size: 22 bytes, specifies `{"global_step": 60000}`)
*   **Missing Files on Dean:** `model.safetensors` (Should be ~3.1GB, is missing on Dean).
*   **Load Test:** The checkpoint **fails to load** on Dean due to the missing weight file. However, a verified full copy of `ckpt-60000` exists on Sam at `/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000` with the 3.1GB `model.safetensors` weight file.
*   **Model Configuration details:**
    *   **Class/Architecture:** `SmolVLMVLA` (specified as `smolvlm_vla` model type).
    *   **Backbone VLM:** `HuggingFaceTB/SmolVLM-500M-Instruct`.
    *   **Uncertainty prediction:** `predict_uncertainty = True`, `uncertainty_beta = 0.5`.
*   **Verification Command used:**
    `ssh -i id_dean dean@100.124.50.124 "cat /home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-60000/config.json"`

---

## 6. Phase 2 TDQC Collector Audit

The collector `/home/redafrix/SimVLA_modified/evaluation/libero/collect_phase2_tdqc_balanced_per_task.sh` uses a WebSocket client-server design:

*   **Command Structure:**
    *   It activates the `libero` env and waits for the SimVLA model servers.
    *   It parallelizes rollouts across multiple ports (e.g., 8103, 8104, 8105) by invoking `./run_libero_pro_eval.sh`.
    *   It executes the evaluation client (`libero_client.py`) which connects to the model servers via WebSockets.
*   **Env Variables Set:** `LIBERO_PRO_ROOT`, `FORCE_LIBERO_PRO_REGEN`, `EXTRA_PERTURBATIONS`, `OBJECT_PERTURBATION_LEVEL`, `TASK_SUITE`, `TASK_ID`, `NUM_TRIALS`, `SEED`, `PORT`, `REPLAN_STEPS`, `NO_VIDEO`, `STATE_STATS_PATH`, `UNCERTAINTY_LOG`.
*   **Episode Balancing Logic:** Runs a loop that launches demo batches in parallel. It checks if the saved jsonl has successes and failures, retaining exactly `TARGET_PER_CLASS` (default: 50) successful episodes and 50 failed episodes per task.
*   **Recorded Data & Features:**
    *   **Successes/Failures:** Recorded.
    *   **Per-step Rows:** No. It outputs one row per *episode*, where `uncertainty_trace` is nested as a list of dictionaries for all steps.
    *   **Action Chunks:** No. It only records the final executed action (7D) at each environment step, discarding the full 10-step predicted action chunks.
    *   **Uncertainty Features:** Logs 12 scalar features per planning step, such as `mean_path_var`, `mean_last_var`, and `denoise_delta` (specified under `PLAN_SCALAR_UNCERTAINTY_KEYS` in the client).
    *   **49D Features and Deltas:** Not natively computed in the collection shell script. These are calculated post-hoc by dataset compilation scripts.
*   **Usability as-is:** **NOT USABLE AS-IS**. It produces episode-level JSONL records and lacks the image saving, `.npz` state saving, and ACE candidate chunk sampling required by FIPER formats.

---

## 7. Called Python Scripts Audit

### `libero_client.py`
*   **Exact Path:** `/home/redafrix/SimVLA_modified/evaluation/libero/libero_client.py`
*   **What it does:** Instantiates the Robosuite gym environment, receives images/states from the simulation, packs them, calls the SimVLA server over WebSockets for actions, steps the environment, and writes per-episode records containing nested step traces to `--uncertainty_log`.
*   **Key Arguments:** `--host`, `--port`, `--task_suite`, `--num_trials`, `--seed`, `--replan_steps`, `--uncertainty_log`, `--no_video`.
*   **Model Inference Location:** Offloaded to the server via WebSocket policy client (`client.step`).
*   **Env Reset/Step Location:** Lines 326 (reset) and 377 (step).
*   **Row Writing Location:** Line 422 (to `--uncertainty_log` JSONL file).
*   **Inference Style:** Causal (sequential environment steps).
*   **Leakage Risk:** None.

### `serve_smolvlm_libero.py`
*   **Exact Path:** `/home/redafrix/SimVLA_modified/evaluation/libero/serve_smolvlm_libero.py`
*   **What it does:** Runs a FastAPI server hosting the `SmolVLMVLA` model, handles incoming requests to `/act`, runs model inference to generate action plans and uncertainty values, and sends them back to the client.
*   **Key Arguments:** `--checkpoint`, `--host`, `--port`, `--device`, `--num_action_samples`.
*   **Model Inference Location:** Line 233 (`model.generate_actions_with_uncertainty`).
*   **Env Reset/Step Location:** None (does not touch gym envs).

---

## 8. Trusted FIPER Collector Comparison

We compare the Phase 2 TDQC client-server setup against the trusted FIPER collector:
*   `collect_fiper_receding_all_outcomes_v2.py`
*   `simvla_candidate_sampler.py`

### Location Audit
*   **Exists on Dean:** **NO** (Neither file is present).
*   **Exists locally on Batman:** **YES** (At `fiper_ws/collection/data_collection_stage9/` and `reda_ws/video_labeling_ws/src/`).

### Main Differences
*   **Execution Model:** FIPER collector runs entirely in-process, managing both the gym environment and PyTorch model loading. Phase 2 TDQC splits them into a WebSocket server/client.
*   **Logging Granularity:** FIPER writes **one JSONL row per environment step**, containing absolute paths to dumped camera images (`.png`) and saved physics simulator states (`.npz`). Phase 2 TDQC writes **one JSONL row per episode**, nesting step-level scalars inside an array without saving `.npz` states or image frames.
*   **ACE Sampling:** FIPER generates 8 alternative candidate action chunks (`ace_candidate_chunks_env`) at each step using randomized seeds to compute disagreement. Phase 2 TDQC only logs the single executed action.

### Safest Implementation Choice
**Adapt the trusted FIPER collector (`collect_fiper_receding_all_outcomes_v2.py`) to load `ckpt-60000`** rather than adapting the Phase 2 WebSocket client.  
*   *Rationale:* FIPER datasets require image frame logging, simulator `.npz` saving, and ACE candidate chunks. The FIPER collector already contains robust, vetted logic for state management, image saving, and receding-horizon execution. Adapting the client-server Phase 2 setup to write individual step rows, dump `.npz` files, and evaluate 8 parallel ACE candidates would require duplicating FIPER's entire data-logging pipeline, increasing the risk of code drift.

---

## 9. Uncertainty 49D Feature Discovery

The 49-dimensional features are logged at the environment step level. We verified their structure by auditing a valid dataset on Sam (`/home/rootalkhatib/test/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp04/data/v9_full_49d.pt`).

### Key Structure & Breakdown
The 49 feature keys consist of four distinct feature families:
1.  **Default Trace Features (6 keys):** Measures statistics of the predicted action variance across the 10-step plan horizon.
    *   `path_step_mean`, `last_step_mean`, `mean_path_var`, `mean_last_var`, `max_path_var`, `max_last_var`
2.  **Denoising Trace Features (17 keys):** Captures temporal behavior of the variance during the reverse flow-matching steps.
    *   `denoise_initial_mean`, `denoise_final_mean`, `denoise_delta` ($initial - final$), `denoise_slope` (regression slope of variance over flow steps), `denoise_final_max`, `denoise_spike` (max positive variance step change), `denoise_final_gripper`, `denoise_final_rotation_mean`
    *   `denoise_velocity_norm_mean`, `denoise_velocity_norm_max`, `denoise_update_norm_mean`, `denoise_update_norm_max`, `denoise_update_norm_final`, `denoise_update_spike`, `denoise_update_oscillation_mean`, `denoise_update_direction_flip_mean` (cosine similarity flip rate), `denoise_final_initial_action_l2`
3.  **Action Trace Features (17 keys):** Evaluates differences and norm distributions of action samples.
    *   `sample_action_var_mean`, `sample_action_var_max`, `sample_action_l2_mean`, `sample_action_l2_max`, `sample_action_translation_var`, `sample_action_rotation_var`, `sample_action_gripper_var`
    *   `action_norm`, `action_max_abs`, `action_translation_norm`, `action_rotation_norm`, `action_gripper_abs`, `action_delta_prev_norm` ($||a_t - a_{t-1}||$), `action_delta_prev_max_abs`
    *   `plan_drift_l2`, `plan_drift_mean_l2`, `plan_drift_max_l2`
4.  **State Features (9 keys):** Mahalanobis distances of proprioception vectors and raw state norms relative to expert statistics.
    *   `state_mahalanobis`, `state_mahalanobis_eef`, `state_mahalanobis_rotation`, `state_mahalanobis_gripper`, `state_eef_norm`, `state_rotation_norm`, `state_gripper_norm`, `state_gripper_width`, `state_delta_prev_norm`

### Computation and Runtime Safety
*   **Inference-time calculation:** Denoise and action trace features are computed directly inside `generate_actions_with_uncertainty` during reverse flow-matching.
*   **Real-time suitability:** Yes. It requires no environment resets, no future labels, and uses only forward inference passes, making it safe for real-time deployment.
*   **Deltas:** Computed as previous-timestep difference ($x_t - x_{t-1}$).
*   **JSON Field Names:** `simvla_uncertainty_49d` (array of 49 floats) and `simvla_uncertainty_delta_49d` (array of 49 floats representing the step-wise change).

---

## 10. Proposed New Dataset Schema

Each JSONL file will record one environment step per line. The recommended schema format:

```json
{
  "episode_id": "libero_spatial_with_mug_t0_r12",
  "timestep": 45,
  "suite": "libero_spatial_with_mug",
  "task_id": 0,
  "task_instruction": "pick up the red mug and place it on the plate",
  "current": {
    "proprio": [0.12, -0.05, 0.45, 0.0, 0.0, 0.0, 0.1, 0.04],
    "object_positions_before": {
      "red_mug": [0.15, -0.22, 0.02, 0.0, 0.0, 0.707, 0.707]
    },
    "sim_state_path": "states/libero_spatial_with_mug_t0_r12_s45_state.npz",
    "before_image_path": "images/libero_spatial_with_mug_t0_r12_s45_before_agent.png",
    "before_wrist_image_path": "images/libero_spatial_with_mug_t0_r12_s45_before_wrist.png",
    "task_context": "mug_on_table"
  },
  "history": [
    {
      "reward": 0.0,
      "success": false,
      "proprio": [0.11, -0.05, 0.44, 0.0, 0.0, 0.0, 0.1, 0.04],
      "executed_action": [0.01, 0.0, 0.01, 0.0, 0.0, 0.0, -1.0]
    }
  ],
  "main_seed": 1048259,
  "main_candidate_action_chunk_normalized": [[0.1, 0.0, 0.1, 0.0, 0.0, 0.0, -1.0]],
  "main_candidate_action_chunk_env": [[0.01, 0.0, 0.01, 0.0, 0.0, 0.0, -1.0]],
  "executed_action": [0.01, 0.0, 0.01, 0.0, 0.0, 0.0, -1.0],
  "simvla_uncertainty_49d": [0.012, 0.354, 0.045, 0.92, 0.0, 0.012, 0.0, 0.0, 0.01, 0.02, 0.32, 0.01, 0.005, 0.0, 0.1, 0.2, 0.05, 0.1, 0.08, 0.01, 0.002, 0.1, 0.04, 0.02, 0.01, 0.01, 0.02, 0.01, 0.0, 0.005, 0.12, 0.32, 0.1, 0.05, 0.02, 0.01, 0.03, 0.01, 0.01, 0.02, 0.45, 0.22, 0.15, 0.08, 0.11, 0.02, 0.03, 0.04, 0.01],
  "simvla_uncertainty_delta_49d": [0.001, -0.012, 0.003, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.02, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, -0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  "ace_candidate_seeds": [492841, 1029482],
  "ace_candidate_chunks_normalized": [[[0.09, 0.0, 0.11, 0.0, 0.0, 0.0, -1.0]]],
  "ace_candidate_chunks_env": [[[0.009, 0.0, 0.011, 0.0, 0.0, 0.0, -1.0]]],
  "metadata": {
    "collection_time": "2026-05-29T15:55:21",
    "checkpoint": "ckpt-60000",
    "machine": "Dean",
    "collector_version": "v2.1_uncertainty"
  },
  "deployability_flags": {
    "proprio_deployable": true,
    "history_deployable": true,
    "candidate_action_deployable": true,
    "object_positions_deployable": true,
    "sim_state_deployable": false,
    "before_image_deployable": true
  },
  "episode_outcome": "success",
  "parent_episode_success": true,
  "parent_failed_or_timeout": false,
  "allowed_use": "train_calib_eval_success"
}
```

---

## 11. Tiny Smoke Test

*   **Smoke Test Status:** **NOT EXECUTED / FAILED ON LOAD**
*   **Why no smoke run:** 
    1.  The `simvla` Conda environment on Dean cannot import `transformers` due to a missing dependency `tqdm` (ModuleNotFoundError).
    2.  The target checkpoint folder `runs/simvla_libero_uncertainty/ckpt-60000` is missing the PyTorch weights file `model.safetensors`, preventing model initialization.

---

## 12. Missing Items and Required Transfers

The following items must be transferred or resolved before starting implementation:

1.  **Weights file:** Copy `model.safetensors` (~3.1GB) from Sam (`/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000/model.safetensors`) to Dean (`/home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-60000/`).
2.  **`simvla` environment repair:** Install `tqdm` in Dean's `simvla` Conda env.
3.  **FIPER Scripts:** Copy the FIPER collection workspace folder (`fiper_ws/collection/data_collection_stage9`) containing `collect_fiper_receding_all_outcomes_v2.py` from Batman to Dean.
4.  **`simvla_trace` Source Code:** Copy `simvla_trace` from Sam (`/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/simvla_trace/`) to Dean, ensuring it is in the Python PATH.

---

## 13. Recommended Next Implementation Plan

Once the missing items are synced and the environment is fixed, execute these steps in the next prompt:

1.  **Base Script:** Modify `collect_fiper_receding_all_outcomes_v2.py`.
2.  **Modifications:** 
    *   Import `generate_actions_trace` from `simvla_trace.trace`.
    *   Modify `generate_chunk` to set `flowtrace=True` in `sample_candidate`, extracting the 49-dimensional features and computing step-level temporal deltas ($x_t - x_{t-1}$).
    *   Inject the resulting `simvla_uncertainty_49d` and `simvla_uncertainty_delta_49d` arrays into the step row dictionary.
3.  **Smoke Test:** Run a single-step test using a task from `libero_spatial_with_mug` with no video outputs (`--no_video`) to verify that features are correctly extracted and saved.
4.  **Launch Campaign:** Start a long-running collection using a detached tmux session:
    ```bash
    tmux new -s fiper_uncertainty_run
    conda activate simvla
    python3 collect_fiper_receding_all_outcomes_v2.py --suites libero_spatial_with_mug --out-dir ./campaign_out
    ```

---

## 14. Final Decision Fields

```text
DEAN_REACHABLE = YES
DEAN_GPU = YES
CHECKPOINT_EXISTS = NO ON DEAN (Weights missing on Dean; config exists; full weight file exists on Sam)
SIMVLA_ENV_WORKS = NO (Missing tqdm)
LIBERO_IMPORT_WORKS = YES
LIBERO_PRO_AVAILABLE = YES
TRUSTED_FIPER_COLLECTOR_AVAILABLE_ON_DEAN = NO
PHASE2_TDQC_SCRIPT_EXISTS = YES
UNCERTAINTY_49D_SOURCE_FOUND = YES
UNCERTAINTY_DELTAS_SOURCE_FOUND = YES
FIPER_FORMAT_COMPATIBLE = YES
TINY_SMOKE_RUN_DONE = NO
TINY_SMOKE_PASS = NO
READY_TO_IMPLEMENT_DEAN_COLLECTION = NO
MISSING_ITEMS = [model.safetensors weights file for ckpt-60000, tqdm dependency in simvla environment, FIPER collector python scripts, simvla_trace source code]
RECOMMENDED_COLLECTION_SCRIPT_BASE = collect_fiper_receding_all_outcomes_v2.py
REPORT_PATH = /home/redafrix/tests/internship/fiper_ws/reports/DEAN_FIPER_UNCERTAINTY_COLLECTION_DISCOVERY_20260529.md
```
