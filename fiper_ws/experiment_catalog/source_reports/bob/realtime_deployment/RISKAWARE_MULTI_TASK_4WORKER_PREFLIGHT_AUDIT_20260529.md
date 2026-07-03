# Preflight Audit Report: Multi-Task 4-Worker Risk-Aware Campaign
**Audit Date:** May 29, 2026

This report provides the preflight audit, hardware verification, task selection, and setup plan for the upcoming 4-worker, multi-day risk-aware deployment campaign across Sam and Bob.

---

## 1. Remote Experiment Guide Summary

Based on `REMOTE_EXPERIMENT_GUIDE.md`, the verified connectivity and execution paths are:

*   **Bob (pcrobotubuntu02):**
    *   *SSH Alias:* `pcrobot` (or `bob`)
    *   *Workspace Path:* `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`
    *   *Activation Command:* `source ../asynchvla_ws/scripts/activate_simvla_bob.sh`
*   **Sam (pcrobotubuntu05):**
    *   *SSH Alias:* `sam`
    *   *Workspace Path:* `/home/rootalkhatib/test/reda_ws/fiper_ws`
    *   *Activation Command:* `source ../asynchvla_ws/scripts/activate_simvla_sam.sh`
*   **Execution Rule:** Long-running rollouts must be launched detached using `nohup` or `tmux` to prevent termination upon SSH disconnection.

---

## 2. Connectivity & Resource Audit

A live status check was performed on both machines:

*   **Sam (NVMe Internal):**
    *   *Connectivity:* Reachable ✅
    *   *GPU:* NVIDIA GeForce RTX 4070 Ti SUPER (16 GB) ✅
    *   *GPU Load:* 3.6 GB VRAM used (background process PID 816643). No active rollout processes.
    *   *Disk Space:* 68 GB available on root partition `/` ✅
*   **Bob (SSD External):**
    *   *Connectivity:* Reachable ✅
    *   *GPU:* NVIDIA GeForce RTX 4070 Ti SUPER (16 GB) ✅
    *   *GPU Load:* 3.2 GB VRAM used (Xorg/gnome). No active rollout processes.
    *   *Disk Space:* 619 GB available on external SSD mount `/media/rootalkhatib/My Passport` ✅

---

## 3. Detector & Artifact Audit

We verified the files and properties of the three detectors planned for this campaign:

| Detector Name | Job Directory | Target Task Type | q95 Threshold | q99 Threshold | Feature Hygiene |
|---|---|---|---|---|---|
| **00_global_main** | `experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16` | Seen Hard Control | `0.4611` | `0.9913` | Clean (No Leakage) ✅ |
| **01_ood_task_8_9** | `experiments/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16` | OOD Task ID | `0.4851` | `0.9277` | Clean (No Leakage) ✅ |
| **fold_00_holdout** | `experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16` | fold_00 Seen/Unseen | `0.5133` | `0.9693` | Clean (No Leakage) ✅ |

### Normalization Sync (Fixed)
During the audit, we identified that the `fold_00_holdout` job directory on both Bob and Sam lacked `normalization.json` (required by the runner). We successfully synchronized/copied this file from `00_global_main` to both machines' fold_00 folders, resolving a potential execution crash.

---

## 4. Policy & Threshold Audit

### Implementation Verification
The policy implementation in `run_riskaware_simvla_one_task_v1.py` exactly implements the requested `v2_strict` rules:
*   *Main script path:* `realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py` (lines 290–355).
*   *Margin rule check:* Evaluates whether $best\_idx \ne 0$, $main\_score \ge q95$, and $main\_score - best\_score \ge 0.10$.
*   *Conservative safety check:* Intervenes if $best\_score < q95$, or if the state is high-risk ($main\_score \ge q99$) and $main\_score - best\_score \ge 0.15$.
*   *Conformal Mass:* Only computed for logging and alarm statistics; it is **NOT** used for selecting actions, preventing accumulated delay traps.
*   *Self-Exclusion:* Candidate ACE calculations exclude the candidate itself.
*   *Uniqueness runtime checks:* Active and verified (zero collisions).

### Previous Task 7 Performance Recap
*   *Improvement:* Success rate increased from 58.00% to 61.00% (+3.00%).
*   *Interventions:* 25 successful recoveries vs. 22 timeouts (conservative degradation).
*   *Overhead:* 8.68x parallel slowdown (~9.1 minutes per episode).
*   *Recommendation:* Keep `v2_strict` as-is for this exploratory multi-day campaign to collect baseline stats on multiple tasks, and plan a v3 dynamic margin policy later.

---

## 5. 4-Worker Campaign Design & Task Selection

Tasks were selected using historical dataset evidence from `TARGET_OBJECT_LOTO_REGISTRY.json` and `all_pick_basket_episodes.jsonl` (no intuition or guessing):

### Selected Task Matrix
1.  **Sam Worker 0:** `worker_sam_0_seen_hard_control`
    *   *Task:* `libero_10_with_milk` / Task 7
    *   *Instruction:* "put the white mug on the plate and put the chocolate pudding to the right of the plate"
    *   *Detector:* `00_global_main` (global baseline)
2.  **Sam Worker 1:** `worker_sam_1_ood_task_id`
    *   *Task:* `libero_10_with_milk` / Task 8
    *   *Instruction:* "put the chocolate pudding on the plate and put the red mug to the right of the plate"
    *   *Detector:* `01_ood_task_8_9` (held-out OOD task detector)
3.  **Bob Worker 0:** `worker_bob_0_fold00_seen_target_object`
    *   *Task:* `libero_object_with_mug` / Task 2
    *   *Instruction:* "pick the butter and place it in the basket"
    *   *Target Object:* `butter` (Seen in fold_00 train/test splits)
    *   *Detector:* `fold_00_holdout`
4.  **Bob Worker 1:** `worker_bob_1_fold00_unseen_target_object`
    *   *Task:* `libero_object_with_mug` / Task 0
    *   *Instruction:* "pick the alphabet soup and place it in the basket"
    *   *Target Object:* `alphabet_soup` (Unseen/Held-out in fold_00)
    *   *Detector:* `fold_00_holdout`

### Task Selection Evidence (Bob Workers)
*   **Bob Worker 0 (Seen):** `libero_object_with_mug` t2 (butter) has a low success rate of **38%** (15 Success, 24 Failure, 10,050 Rows), making it a high-failure stress test.
*   **Bob Worker 1 (Unseen):** `libero_object_with_mug` t0 (alphabet_soup) is an OOD held-out task with a success rate of **68%** (27 Success, 13 Failure, 8,547 Rows) in dataset evaluations, serving as a clean target-object OOD test.
*   Both tasks belong to the same family (`libero_object_with_mug`), have identical pick/place templates, and feature enough failures for robust analysis.

---

## 6. Seed Plan (Deterministic RNG)

To support a multi-day run, we generated deterministic unique random seed lists (1,000 seeds per worker) using separate RNG seed bases to avoid overlaps.

### Seed Files (Stored in `realtime_deployment/configs/seed_plans/`)
*   **Worker Sam 0:** `worker_sam_0_seeds_1000.json` (Base: `202605290`)
    *   *SHA256:* `a5487dfece5d25cd60595956786fab0b24d292d367149308ce9c91f20a73c8b5`
*   **Worker Sam 1:** `worker_sam_1_seeds_1000.json` (Base: `202605291`)
    *   *SHA256:* `d50e5865206ed5f9f3d0f17ac618cac4e3d6fc8f70962831521816802fd3b253`
*   **Worker Bob 0:** `worker_bob_0_seeds_1000.json` (Base: `202605292`)
    *   *SHA256:* `513e62cd203c543cf79495b72379fa1e1cb867b2d2ddc76f93343a0d63808092`
*   **Worker Bob 1:** `worker_bob_1_seeds_1000.json` (Base: `202605293`)
    *   *SHA256:* `6d569449f52ba36fd53f0e113961f02197bb45445b232be7b70cfddb803aee78`

These files are fully synchronized to the configurations folder of both Sam and Bob.

---

## 7. Runtime & Campaign Estimates

*   **Average Episode Duration:** ~547 seconds (Bob) / ~500 seconds (Sam)
*   **Worker Throughput:** ~158 episodes/day (Bob) / ~172 episodes/day (Sam)
*   **Total Throughput (4 Workers parallel):** ~660 episodes/day
*   **3-Day Campaign Volume:** **~1,980 episodes total** (approx. 495 per task)
*   **Log Space Overhead (3-Day):** ~240 MB total (completely safe)
*   **Safety Verdict:** Parallel execution is GPU VRAM safe (2 workers per GPU consume ~13–14 GB out of 16 GB).

---

## 8. Setup & Synchronization Checklist (All Resolved)

*   [x] Sync `run_riskaware_simvla_one_task_v1.py` script to Sam ✅
*   [x] Copy global main `normalization.json` to fold_00 job directory on Bob ✅
*   [x] Copy global main `normalization.json` to fold_00 job directory on Sam ✅
*   [x] Generate and sync all 4 worker seed plans (1000 seeds each) ✅

There are **0** missing setup items remaining. The campaign is ready for launcher script creation.

---

## 9. Launch Plan Skeleton

When authorized, the workers can be launched using the following command structures:

### On Sam:
```bash
# Worker 0 (Seen Control, task 7)
nohup python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
  --config realtime_deployment/configs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528.json \
  --num-episodes 500 \
  --worker-id sam_w0 \
  --seeds-file realtime_deployment/configs/seed_plans/worker_sam_0_seeds_1000.json \
  > realtime_deployment/runs/worker_sam_0_run/logs/w0.log 2>&1 &

# Worker 1 (OOD Task ID, task 8)
nohup python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
  --config realtime_deployment/configs/riskaware_actionmod_v2_strict_libero10_milk_task8_sam_full_20260528.json \
  --num-episodes 500 \
  --worker-id sam_w1 \
  --seeds-file realtime_deployment/configs/seed_plans/worker_sam_1_seeds_1000.json \
  > realtime_deployment/runs/worker_sam_1_run/logs/w1.log 2>&1 &
```

### On Bob:
```bash
# Worker 0 (Fold 00 Seen, t2 butter)
nohup python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
  --config realtime_deployment/configs/riskaware_actionmod_v2_strict_fold00_seen_bob_full_20260528.json \
  --num-episodes 500 \
  --worker-id bob_w0 \
  --seeds-file realtime_deployment/configs/seed_plans/worker_bob_0_seeds_1000.json \
  > realtime_deployment/runs/worker_bob_0_run/logs/w0.log 2>&1 &

# Worker 1 (Fold 00 Unseen, t0 alphabet_soup)
nohup python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
  --config realtime_deployment/configs/riskaware_actionmod_v2_strict_fold00_unseen_bob_full_20260528.json \
  --num-episodes 500 \
  --worker-id bob_w1 \
  --seeds-file realtime_deployment/configs/seed_plans/worker_bob_1_seeds_1000.json \
  > realtime_deployment/runs/worker_bob_1_run/logs/w1.log 2>&1 &
```

---

## 10. Metadata Validation Fields

```ini
PREFLIGHT_PASS = YES
BOB_REACHABLE = YES
SAM_REACHABLE = YES
BATMAN_LOCAL_WORKSPACE_FOUND = /home/redafrix/tests/internship/fiper_ws
CURRENT_POLICY_VERIFIED = YES
CURRENT_POLICY_NAME = risk_filtered_lowest_score_candidate_v2_strict_margin
CURRENT_THRESHOLD_VERDICT = KEEP_V2_FOR_NEXT_CAMPAIGN
GLOBAL_DETECTOR_READY = YES
OOD_TASK_8_9_DETECTOR_READY = YES
FOLD00_DETECTOR_READY = YES
SAM_WORKER_0_TASK = libero_10_with_milk/7
SAM_WORKER_1_TASK = libero_10_with_milk/8
BOB_WORKER_0_TASK = libero_object_with_mug/2/butter
BOB_WORKER_1_TASK = libero_object_with_mug/0/alphabet_soup
MISSING_SETUP_ITEMS = 0
READY_TO_WRITE_LAUNCH_PROMPT_NEXT = YES
FINAL_REPORT_PATH = realtime_deployment/reports/RISKAWARE_MULTI_TASK_4WORKER_PREFLIGHT_AUDIT_20260529.md
```
