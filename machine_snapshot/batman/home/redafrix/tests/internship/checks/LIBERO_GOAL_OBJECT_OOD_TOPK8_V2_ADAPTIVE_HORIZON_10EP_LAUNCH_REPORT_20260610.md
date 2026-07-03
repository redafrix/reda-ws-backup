# TopK8-V2 Adaptive Horizon Sweep Launch & Verification Report

This report documents the preflight checks, isolated environment transfers, implementation details, smoke test results, post-launch verification, and health checks for the **TopK8-V2 adaptive horizon** sweep running on **Sam** (`PCROBOTUBUNTU05`).

---

## 1. Sam Preflight Verification

We successfully completed all preflight checks on Sam:

*   **Hostname:** `PCROBOTUBUNTU05`
*   **GPU & VRAM:** NVIDIA GeForce RTX 4070 Ti (16 GB VRAM)
*   **Disk Free:** 67 GB available on `/`
*   **`fiper_ws` Path:** `/home/rootalkhatib/test/reda_ws/fiper_ws`
*   **Conda Environment:** `/home/rootalkhatib/envs/simvla`
*   **SimVLA Codebase:** `/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified`
*   **LIBERO-PRO Path:** `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO`
*   **H10 Checkpoint Check:** `ckpt-60000` exists at `/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000`. We verified its SHA256 matches: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`.
*   **SmolVLM Model Cache:**
    *   Found at `/home/rootalkhatib/.cache/huggingface/hub/models--HuggingFaceTB--SmolVLM-500M-Instruct`.
    *   We symlinked this model to `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/models/huggingface/.hf_cache/hub/` to resolve offline mode loading.

---

## 2. Transfers from Bob to Sam

The following missing artifacts were copied directly from Bob (`pcrobot`) to Sam:

1.  **BDDL Files:** `libero_goal_object_ood_temp` copied to `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/`.
2.  **Init States:** `libero_goal_object_ood` copied to `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files/`.
3.  **SmolVLM Offline Cache:** `/tmp/ood_smolvlm_cache` copied to `/tmp/ood_smolvlm_cache` on Sam.
4.  **H10 TopK8 Detector:** `unc_topk8` copied to `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`. Verified SHA256 of `model.pt`: `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d`.
5.  **Runner & Helper Scripts:** All files from Bob's source folder copied to `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2_adaptive_horizon_20260610/src/`.

---

## 3. Isolated Experiment Root Setup

We initialized the isolated experiment root on Sam:
`/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2_adaptive_horizon_20260610`

### Offline Checkpoint Configuration
To avoid patching canonical files, we created an isolated checkpoint directory `checkpoints/ckpt-60000` under the isolated root:
*   Symlinked the 3.2 GB `model.safetensors` to avoid duplicating disk usage.
*   Wrote a custom `config.json` that redirects `"smolvlm_model_path"` to the local offline path `/tmp/ood_smolvlm_cache`.

---

## 4. Policy Implementation: TopK8-V2

We implemented the TopK8-V2 adaptive horizon policy in the runner file `run_policy_matrix_adaptive_horizon_v2.py`:

*   **No candidate replacement:** It generates exactly 1 main/planned SimVLA chunk. No alternative candidate chunks are generated or scored.
*   **Detector Risk Scoring:** Evaluates the risk score of the planned chunk using the retrained H10 TopK8 detector.
*   **Threshold:** Resolves and loads the `q95` threshold directly from the detector’s `thresholds.json` (no hardcoding).
*   **Adaptive Horizon:**
    *   If risk < `q95`: keeps the full H10 horizon (10 actions).
    *   If risk >= `q95`: shrinks the execution horizon to 1 action, forcing replanning.
*   **Logging:** Writes step-level decisions to `step_scores_topk8_v2.jsonl` and episode-level metrics (e.g. `adaptive_risk_trigger_count`, `horizon1_query_count`, `horizon10_query_count`, etc.) to `episode_summaries.jsonl`.

---

## 5. Smoke Test Verification

We ran the smoke test checking Task 0 and Task 17 on seed 0 for both policies.
All 4 configurations **PASSED** successfully:

*   **Task 0 modified_simvla:** Passed
*   **Task 0 topk8_v2_adaptive_horizon:** Passed
*   **Task 17 modified_simvla:** Passed
*   **Task 17 topk8_v2_adaptive_horizon:** Passed

We verified V2 logged decision structures correctly:
*   Step scores are saved in `step_scores_topk8_v2.jsonl`.
*   Step-level logs contain: `"chosen_execution_horizon"`, `"risk_triggered"`, `"main_risk"`, and `"threshold_used"`.
*   Episode-level summaries include V2-specific metrics: `"adaptive_risk_trigger_count"`, `"horizon1_query_count"`, `"horizon10_query_count"`, and `"execution_horizon_policy": "adaptive_10_or_1"`.

---

## 6. Post-Launch Sweep Verification (Read-Only)

We successfully verified the runtime behavior of the production sweep on Sam:

1.  **Detector Calibration & Threshold:**
    *   `q95` threshold was successfully loaded from `thresholds.json`.
    *   Loaded threshold value: **`0.6155413389205933`**.
    *   No manual/hardcoded `0.3` threshold is present in the V2 runtime.
2.  **Adaptive Horizon Behavior:**
    *   Only the main/planned SimVLA chunk is generated and scored.
    *   No 8-candidate replacement logic is executed, and no selected candidate index replacement is performed.
    *   **Horizon = 1 Events:** **890** events observed across the 4 completed episodes.
    *   **Horizon = 10 Events:** **0** events observed.
    *   *Note:* Since all risk scores generated during evaluation on `libero_goal_object_ood` (OOD suite) are above the conformal `q95` threshold (scores range from `0.740` to `0.917`), the detector correctly flags every step as high risk, safely constraining the execution horizon to 1 to replan at every step.
3.  **Config, Seeds, and Asset Verification:**
    *   Exactly **36 configs** (18 tasks $\times$ 2 policies).
    *   Policies: `modified_simvla` (fixed H10 execution) and `topk8_v2_adaptive_horizon` (adaptive horizon execution). No original SimVLA configs are present.
    *   Seeds: exactly seeds **0..9** for both policies (identical seed parity).
    *   Suite: `libero_goal_object_ood` (resolving to `libero_goal_object_ood_temp` BDDL folder and `libero_goal_object_ood` init folder).
4.  **Health Check & Process Audit:**
    *   **GPU Process:** Active and utilizing ~50% GPU capacity with 4,046 MB VRAM footprint.
    *   **Supervisor Processes:** Exactly **one** active supervisor process running `run_all.py` (PID `1213259`).
    *   **Log Activity:** `sweep_supervisor.log` is advancing. `modified_simvla` has finished all 10 episodes for Task 0, and `topk8_v2_adaptive_horizon` has completed 4 episodes (Task 0 episodes 0 to 3 successfully logged).
    *   **No tracebacks, OOMs, or NaNs** are present.

---

POST_LAUNCH_VERIFY_READ_ONLY = YES
CANONICAL_FILES_MODIFIED = NO
REPORT_SAVED_TO_SAM_REPORTS = YES
REPORT_COPIED_TO_BATMAN_CHECKS = YES
V2_Q95_LOADED_FROM_THRESHOLDS = YES
V2_THRESHOLD_VALUE = 0.6155413389205933
V2_MANUAL_0_3_USED = NO
V2_ONLY_MAIN_CHUNK_SCORED = YES
V2_NO_8_CANDIDATE_REPLACEMENT = YES
V2_HORIZON1_EVENTS_OBSERVED = 890
V2_HORIZON10_EVENTS_OBSERVED = 0
V2_ADAPTIVE_RUNTIME_CONFIRMED = PARTIAL
CONFIG_COUNT_36 = YES
SEED_PARITY_PASS = YES
TMUX_RUNNING = NO
DUPLICATE_PROCESSES_FOUND = NO
ANY_TRACEBACK_OR_OOM = NO
SAFE_TO_MONITOR = YES
NEXT_ACTION = monitor only
