# Pi0.5-LIBERO & Risk-Aware H10 Setup + Smoke Test Report

**Date:** 2026-06-23  
**Host:** Bob (`PCROBOTUBUNTU02`)  
**Target Workspace:** `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623`  
**Target Environment:** `/home/rootalkhatib/pi05_openpi_20260623_env`

---

## 1. System and Preflight Information

*   **Hostname:** `PCROBOTUBUNTU02`
*   **GPU:** NVIDIA GeForce RTX 4070 (16 GB)
*   **Disk Space on Passport:** 461 GB available (76% usage of 1.9 TB)
*   **Active Tmux Session Paused:** `openvla_ood_basic_h1_100ep_20260619`
*   **Original Python Runner Command:**
    ```bash
    source "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/activate_openvla_oft_bob.sh" && python3 -u "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/run_openvla_ood_basic_h1_full_20260619.py" --suite libero_goal_object_ood --output-root "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619" --episodes-per-task 100 --seed-start 10 --max-steps 800 --task-ids all > "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/libero_goal_object_ood_openvla_basic_h1_100ep_20260619/sweep_supervisor.log" 2>&1
    ```
*   **Pause and Resume Verification:**
    *   **Row count before pause:** 1698 rows in `episode_summaries.jsonl`.
    *   **Last completed episode:** Task 16, seed 107.
    *   **Safe pause boundary:** Sent `SIGINT` (Ctrl+C) to the tmux pane immediately after seed 107 completed.
    *   **Resume status:** Tmux session was recreated and command rerun. The runner loaded checkpoint shards, detected 1698 completed episodes, and successfully resumed from task 16 seed 108 without overwriting existing data.
    *   **Post-resume GPU Check:** Active and running on GPU (PID 171126, ~9.7 GB VRAM allocated, executing step 53+ of seed 108).

---

## 2. Setup Phase Details

1.  **Workspace Creation:** Successfully initialized `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623` with subfolders.
2.  **Environment:** A fresh isolated virtual environment was created on system drive `/home/rootalkhatib/pi05_openpi_20260623_env` using Python 3.10 and bootstrapped via `get-pip.py`.
3.  **openpi clone:** Cloned `Physical-Intelligence/openpi` (commit `15a9616a00943ada6c20a0f158e3adb39df2ccac`) with submodules `third_party/aloha` and `third_party/libero`.
4.  **openpi installation:** Installed `openpi` and package `openpi-client`. Installed additional dependencies (`robosuite==1.4.1`, `bddl`, `matplotlib`, `easydict`, `gym`). Modified `pyproject.toml` to support Python 3.10.
5.  **Checkpoint:** Downloaded the `pi05_libero` checkpoint from `gs://openpi-assets/checkpoints/pi05_libero` using anonymous `fsspec` access and cached it to the Passport drive.
6.  **Dummy Inference:** Verified on JAX GPU. Verified that it outputs finite actions of shape `(10, 7)`.
7.  **JAX OOM Fix:** Avoided memory allocation failures by exporting `XLA_PYTHON_CLIENT_PREALLOCATE=false` to prevent JAX from hogging 75% of GPU memory and leaving enough for MuJoCo rendering.

---

## 3. Adapters & Patches Created (Isolated to Workspace)

*   **Python 3.10 compatibility in `openpi`:**
    In [download.py](file:///media/rootalkhatib/My%20Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi/src/openpi/shared/download.py#L191), replaced `datetime.UTC` (Python 3.11+) with `datetime.timezone.utc`.
*   **Dynamic Wrist Masking in `libero_policy`:**
    In [libero_policy.py](file:///media/rootalkhatib/My%20Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi/src/openpi/policies/libero_policy.py#L66), patched `left_wrist_0_rgb` image mask to check for a dynamic `mask_left_wrist_false` flag in observation:
    ```python
    "left_wrist_0_rgb": np.False_ if data.get("mask_left_wrist_false", False) else np.True_
    ```
*   **PyTorch 2.6+ Compatibility in rollout script:**
    Monkeypatched `torch.load` to default `weights_only=False` to allow loading older LIBERO pickled state dictionaries.

---

## 4. Smoke Test Results

All smoke tests executed successfully on task 0 of `libero_goal_object` using seed 10 (1 rollout episode per test, max 300 steps):

### A. Smoke Test A: Two-Camera Mode (Wrist + Agent View)
*   **Wrist Camera:** Active (real environment frames)
*   **Wrist Mask:** `True` (active)
*   **Success:** `True` (completed successfully in **144 steps**)
*   **Video saved:** `smoke_two_camera_rollout.mp4`
*   **Summary saved:** `smoke_two_camera_summary.json`

### B. Smoke Test B1: One-Camera Mode (Wrist zeroed, Mask=True)
*   **Wrist Camera:** Zeros (`zeros_like(agentview_image)`)
*   **Wrist Mask:** `True` (policy thinks it's a real camera but gets zero pixels)
*   **Success:** `False` (timed out at 300 steps, no crash)
*   **Video saved:** `smoke_one_camera_mask_true_rollout.mp4`
*   **Summary saved:** `smoke_one_camera_mask_true_summary.json`

### C. Smoke Test B2: One-Camera Mode (Wrist zeroed, Mask=False)
*   **Wrist Camera:** Zeros (`zeros_like(agentview_image)`)
*   **Wrist Mask:** `False` (policy ignores the left wrist channel via attention mask)
*   **Success:** `False` (timed out at 300 steps, no crash)
*   **Video saved:** `smoke_one_camera_mask_false_rollout.mp4`
*   **Summary saved:** `smoke_one_camera_mask_false_summary.json`

### D. Flow Matching Candidate Generation Smoke Test
*   **Main Action Chunk:** `(10, 7)` finite actions.
*   **Flow Candidate Chunks:** Generated 8 candidate chunks of shape `(8, 10, 7)` using explicit flow noise tensors of shape `(10, 32)`.
*   **Variance Verification:** Confirmed that candidates are **not identical** (are_candidates_identical = `False`), indicating active variance due to flow noise seeds.
*   **Summary saved:** `smoke_candidate_generation_summary.json`

---

## 5. Status Flags

```text
PI05_WORKSPACE_CREATED = YES
PI05_LIBERO_CHECKPOINT_LOADED = YES
CURRENT_BOB_PROCESS_IDENTIFIED = YES
CURRENT_BOB_PROCESS_PAUSED_SAFELY = YES
CURRENT_BOB_PROCESS_RESUMED_CORRECTLY = YES
TWO_CAMERA_SMOKE_PASS = YES
ONE_CAMERA_AGENT_VIEW_SMOKE_PASS = YES
ACTION_SHAPE_10X7_CONFIRMED = YES
FINITE_ACTIONS_CONFIRMED = YES
H10_EXECUTION_CONFIRMED = YES
NO_EXISTING_WORKSPACES_MODIFIED = YES
SAFE_FOR_DATA_COLLECTION_PHASE = YES
REAL_DATA_COLLECTION_LAUNCHED = NO
WAITING_FOR_REDA_APPROVAL = YES
```

---
*Note: Existing workspaces (FIPER, openvla_oft, etc.) were not modified. The system has been returned to its running state. Stopped at phase boundary. Ready for Reda's approval before moving forward.*
