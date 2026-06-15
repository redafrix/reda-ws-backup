# Baseline SimVLA Rollout Setup and Launch Report

This report documents the setup, verification, and launch of the baseline SimVLA-only rollout experiment on Sam for `libero_10_with_milk` Task 7.

## 1. Process & Workspace State Before Launch
The following machine resources were measured on Sam (PCROBOTUBUNTU05) before launching the rollout processes:
- **GPU memory usage:** `3645MiB` / `16376MiB` used (SmolVLM background model server occupied 3.5GB).
- **RAM usage:** `2.7GiB` used / `30GiB` total.
- **Disk space:** `377G` used / `468G` total (85% utilization).

## 2. Existing Scripts Inspected
- `asynchvla_ws/src/data_collection_stage9/collect_fiper_receding_all_outcomes_v2.py`
- `asynchvla_ws/src/data_collection_stage9/collect_fiper_receding_all_outcomes_v1.py`
- `asynchvla_ws/src/data_collection_stage9/libero_pro_env_utils.py`
- `asynchvla_ws/src/data_collection_stage9/simvla_candidate_sampler.py`
- `launch_eternal_fiper_sweep.sh`

## 3. New Files Created
- **Config:** `realtime_deployment/configs/baseline_simvla_libero10_milk_task7_sam_v1.json`
- **Runner script:** `realtime_deployment/scripts/run_baseline_simvla_one_task_v1.py`
- **Launch report:** `realtime_deployment/reports/BASELINE_SIMVLA_LIBERO10_MILK_TASK7_SAM_V1_SETUP_AND_LAUNCH_REPORT.md`

## 4. Config Values
```json
{
  "suite": "libero_10_with_milk",
  "task_id": 7,
  "mode": "baseline_simvla_only",
  "num_episodes_target": 100,
  "max_steps": 300,
  "execute_policy": "receding_horizon_execute_first_action_only",
  "sample_extra_ace_candidates": false,
  "save_action_chunks": false,
  "save_full_rows": false,
  "save_video": false,
  "save_lightweight_episode_summary": true,
  "seeds": [10000, 10001, ..., 10099],
  "output_dir": "realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1"
}
```

## 5. Smoke Test Results
- **Run command:**
  ```bash
  python3 realtime_deployment/scripts/run_baseline_simvla_one_task_v1.py \
    --config realtime_deployment/configs/baseline_simvla_libero10_milk_task7_sam_v1.json \
    --num-episodes 1 \
    --worker-id smoke \
    --episode-start 0 \
    --episode-end 1
  ```
- **Outcome:** PASS. Executed exactly 1 episode (Episode 0, reset seed 10000) for `libero_10_with_milk` Task 7. Finished successfully in `38.4s` (outcome: failure_or_timeout, 300 steps limit reached). No candidate action chunk NPZ or full JSONL rows were saved.

## 6. Execution Details
- **Full Run Launched:** YES (concurrently using 2 parallel workers).
- **Worker 0 (Episodes 0-49):**
  - **PID:** `3168360`
  - **Log path:** `realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs/worker_0.log`
- **Worker 1 (Episodes 50-99):**
  - **PID:** `3168361`
  - **Log path:** `realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs/worker_1.log`

## 7. Confirmations
- `ACE_USED` = **NO**
- `FIPER_USED` = **NO**
- `EXTRA_CANDIDATES_SAMPLED` = **NO**
- `FULL_STEP_JSONL_SAVED` = **NO**
- `SUITE` = **libero_10_with_milk`**
- `TASK_ID` = **7**

## 8. Progress Monitoring
- **Live Status File Path:** `realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/live_status.json`
- **Monitor Commands:**
  ```bash
  # View worker logs
  tail -f realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs/worker_0.log
  tail -f realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs/worker_1.log

  # Check live status stats
  cat realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/live_status.json
  ```
