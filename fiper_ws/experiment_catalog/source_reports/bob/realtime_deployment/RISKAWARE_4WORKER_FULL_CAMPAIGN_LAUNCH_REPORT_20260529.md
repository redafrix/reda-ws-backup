# 🚀 Multi-Task 4-Worker Risk-Aware Full Campaign Launch Report

**Date:** May 29, 2026  
**Campaign Scope:** 4 parallel workers, 5,000 episodes per task (Total: 20,000 episodes)  
**Launch Status:** ALL WORKERS LAUNCHED DETACHED & RUNNING SUCCESSFULLY  

---

## 1. Pre-Launch Sanity Checks & Verification

### 1. CONFIDENTIAL PROCESS CONFLICT CHECK
*   **Status:** **PASS** ✅
*   **Audit Details:** Verified no active `run_riskaware_simvla_one_task_v1.py` or chunk-exec or old smoke test processes existed on either Sam or Bob before launch.

### 2. CHUNK-EXEC WORK ARCHIVAL VERIFICATION (CLI 2)
*   **Status:** **PASS** ✅
*   **Audit Details:** Confirmed that `run_riskaware_simvla_chunk_exec_v2.py`, `run_baseline_simvla_chunk_exec_h5_v1.py`, `chunk_exec_rerun`, and `h5_baseline` are completely inactive on Bob, keeping the CLI 2 chunk-exec work correctly stopped and archived.

### 3. DETECTOR ARTIFACTS HYGIENE VERIFICATION
*   **Status:** **PASS** ✅
*   **Audit Details:** For all three detectors, we verified the presence of `model.pt`, `config.json`, `thresholds.json` / `policy_thresholds.json`, `normalization.json`, and `FEATURE_AUDIT.json`. 
*   **Feature Leakage Check:** Inspected `FEATURE_AUDIT.json` contents on Sam and Bob nodes. Features successfully use only normalized actions, action statistics, current proprioception history, and previous execution metrics. Verified:
    *   No object positions (`uses_object_positions_before = false`)
    *   No reward inputs (`uses_reward = false`)
    *   No success flags (`uses_success = false`)
    *   No future timesteps (`uses_future_timestep = false`)
    *   No OOD training rows (`uses_ood_rows_for_train = false`)

### 4. SMOKE REVALIDATION CHECK
*   **Status:** **PASS** ✅
*   **Audit Details:** Revalidated all previous 4 smoke runs:
    *   *Sam Worker 0 (Seen task 7):* 286 steps, Success, 0 collisions, 286 step scores lines, conformal quantile thresholds matched.
    *   *Sam Worker 1 (OOD task 8):* 232 steps, Success, 0 collisions, 232 step scores lines, conformal quantile thresholds matched.
    *   *Bob Worker 0 (Seen butter task 2):* 202 steps, Success, 0 collisions, 202 step scores lines, conformal quantile thresholds matched.
    *   *Bob Worker 1 (Unseen alphabet_soup task 0):* 300 steps, Timeout, 0 collisions, 300 step scores lines, conformal quantile thresholds matched.

---

## 2. Config & Seed Plans Audit (5,000 Seeds Upgrade)

A deterministic seed generation script (`generate_and_update_5000_configs.py`) was executed to upgrade the configs to 5,000 episodes. Separate deterministic RNG seeds were generated to avoid overlap:

### Seed Files (Stored in `realtime_deployment/configs/seed_plans/`)
1.  **worker_sam_0_seeds_5000.json** (RNG Base: `202605290`)  
    *   *SHA256:* `ff3c3c581616aaeb5123bef90b0bcf88351e8f8e07bd321a8b4a6ee2fab32e97`
2.  **worker_sam_1_seeds_5000.json** (RNG Base: `202605291`)  
    *   *SHA256:* `80fc38898e4d7d3fd9bdabca4bb43215aa55d0dea989f568aed26ae0930a9b80`
3.  **worker_bob_0_seeds_5000.json** (RNG Base: `202605292`)  
    *   *SHA256:* `e02f1bee1ae3a07475b8d3b5c7b10930cc0a4ea2c60dc6edb07d705f22fe99c1`
4.  **worker_bob_1_seeds_5000.json** (RNG Base: `202605293`)  
    *   *SHA256:* `2a3f790e4cfa403f5889bed5ec261d7c59a43e4b3c873f656ac81790fc3a5e89`

### Worker Configs (Distributed & Synced)
1.  **riskaware_actionmod_v2_strict_sam_seen_task7_20260529.json**  
    *   *SHA256:* `e78e2b7ea24855b938272eb50b460d244a91614ab2897aa8b21ff79e860344bd`
2.  **riskaware_actionmod_v2_strict_sam_ood_task8_20260529.json**  
    *   *SHA256:* `d65462308dfe2a323594b5a8989888f459506e475f84177c4e6b65d0c1124f17`
3.  **riskaware_actionmod_v2_strict_bob_fold00_seen_butter_task2_20260529.json**  
    *   *SHA256:* `9f4027e53f74d0f3369641e7c12bb780f41e2e228c32189b9bfa38800a010bb8`
4.  **riskaware_actionmod_v2_strict_bob_fold00_unseen_alphabet_soup_task0_20260529.json**  
    *   *SHA256:* `957eeadf9b32acf25a61017566acea6d72b0da572dfcc5836c270056bd2b1f5d`

---

## 3. Historical Support Audit Table

We verified historical rollout stats from previous train/eval sweeps. All tasks satisfy the condition of having at least 10 historical failure episodes:

| Task Name | Suite | Task ID | Target Object | Successes | Failures | Total Episodes | Failure Rate | Enough Failures (>= 10) |
|---|---|---|---|---|---|---|---|---|
| `libero_10_with_milk_t7` | `libero_10_with_milk` | 7 | N/A | 18 | 15 | 33 | 45.45% | **YES** ✅ |
| `libero_10_with_milk_t8` | `libero_10_with_milk` | 8 | N/A | 23 | 10 | 33 | 30.30% | **YES** ✅ |
| `libero_object_with_mug_t2` | `libero_object_with_mug` | 2 | butter | 15 | 24 | 39 | 61.54% | **YES** ✅ |
| `libero_object_with_mug_t0` | `libero_object_with_mug` | 0 | alphabet_soup | 27 | 13 | 40 | 32.50% | **YES** ✅ |

---

## 4. Detached Launch Configuration

Tmux was installed on Sam to allow matching session controls across both machines:

*   **Sam TMUX Session:** `riskaware_4worker_sam_20260529`
*   **Bob TMUX Session:** `riskaware_4worker_bob_20260529`

### Run Command Mapping
*   **Sam Worker 0:**
    ```bash
    python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
      --config realtime_deployment/configs/riskaware_actionmod_v2_strict_sam_seen_task7_20260529.json \
      --num-episodes 5000 \
      --episode-offset 0 \
      --worker-id sam_w0_seen_task7 \
      > realtime_deployment/runs/riskaware_4worker_20260529/sam_w0_seen_task7/logs/worker.log 2>&1
    ```
*   **Sam Worker 1:**
    ```bash
    python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
      --config realtime_deployment/configs/riskaware_actionmod_v2_strict_sam_ood_task8_20260529.json \
      --num-episodes 5000 \
      --episode-offset 0 \
      --worker-id sam_w1_ood_task8 \
      > realtime_deployment/runs/riskaware_4worker_20260529/sam_w1_ood_task8/logs/worker.log 2>&1
    ```
*   **Bob Worker 0:**
    ```bash
    python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
      --config realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_seen_butter_task2_20260529.json \
      --num-episodes 5000 \
      --episode-offset 0 \
      --worker-id bob_w0_fold00_seen_butter_t2 \
      > realtime_deployment/runs/riskaware_4worker_20260529/bob_w0_fold00_seen_butter_t2/logs/worker.log 2>&1
    ```
*   **Bob Worker 1:**
    ```bash
    python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
      --config realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_unseen_alphabet_soup_task0_20260529.json \
      --num-episodes 5000 \
      --episode-offset 0 \
      --worker-id bob_w1_fold00_unseen_alphabet_soup_t0 \
      > realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0/logs/worker.log 2>&1
    ```

---

## 5. Live Process PIDs and Resource Allocation

Verified active processes at 14:47:04:

*   **Sam Worker 0 (Seen task 7):** PID `3829646` (Active on GPU 0)
*   **Sam Worker 1 (OOD task 8):** PID `3829811` (Active on GPU 0)
*   **Bob Worker 0 (Seen butter t2):** PID `2605930` (Active on GPU 0)
*   **Bob Worker 1 (Unseen alphabet_soup t0):** PID `2606244` (Active on GPU 0)

### GPU Resource Check (nvidia-smi)
*   **Sam Node GPU:** 11,889 MiB / 16,376 MiB VRAM used (~72% memory load). Temp: 68°C. GPU Util: 97%.
*   **Bob Node GPU:** 11,341 MiB / 16,376 MiB VRAM used (~69% memory load). Temp: 80°C. GPU Util: 96%.
*   *Verdict:* GPU resource allocations are completely safe and thermal stats are within limits.

---

## 6. First Live Status Check (Episode 0 Progress)

Inspected logs at 14:47:00. All four workers successfully booted up and are processing Episode 0:

### Sam Worker 0:
*   *Step:* Step 19 reached.
*   *Current Seeds:* `main = 1128104980`, `ace = [62964921, 671433031, 1065729763, 1750068445, 1248579531, 1717874031, 1218178916, 2054423134]`.
*   *Error/Warnings:* None.

### Sam Worker 1:
*   *Step:* Step 19 reached.
*   *Current Seeds:* `main = 59381448`, `ace = [408853650, 975926840, 1946221845, 1716445732, 1893627512, 1603398322, 1491337163, 1104660461]`.
*   *Error/Warnings:* None.

### Bob Worker 0:
*   *Step:* Step 18 reached.
*   *Current Seeds:* `main = 1333920052`, `ace = [1098901328, 79817327, 1155447456, 234662733, 1191555509, 899932474, 80208970, 1558409761]`.
*   *Error/Warnings:* None.

### Bob Worker 1:
*   *Step:* Step 18 reached.
*   *Current Seeds:* `main = 343882360`, `ace = [1306708097, 1160321592, 519695260, 745271115, 919204205, 1004640771, 291359594, 1471791122]`.
*   *Error/Warnings:* None.

---

## 7. Monitoring Instructions

To monitor the status of the campaign over the next few days:

### On Sam:
```bash
# Attach to tmux session:
tmux attach-t riskaware_4worker_sam_20260529
# Check worker 0 log:
tail -f realtime_deployment/runs/riskaware_4worker_20260529/sam_w0_seen_task7/logs/worker.log
# Check worker 1 log:
tail -f realtime_deployment/runs/riskaware_4worker_20260529/sam_w1_ood_task8/logs/worker.log
```

### On Bob:
```bash
# Attach to tmux session:
tmux attach -t riskaware_4worker_bob_20260529
# Check worker 0 log:
tail -f realtime_deployment/runs/riskaware_4worker_20260529/bob_w0_fold00_seen_butter_t2/logs/worker.log
# Check worker 1 log:
tail -f realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0/logs/worker.log
```
