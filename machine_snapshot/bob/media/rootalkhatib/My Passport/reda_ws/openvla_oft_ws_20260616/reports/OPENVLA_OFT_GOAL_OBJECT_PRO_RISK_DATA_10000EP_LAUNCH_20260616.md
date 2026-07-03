# OpenVLA-OFT Risk Data Collection Launch Report

**Date:** 2026-06-16  
**Host:** Bob (`PCROBOTUBUNTU02`)  
**Workspace:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`  
**Task Suite:** `libero_goal` (10 tasks)  
**Model:** `moojink/openvla-7b-oft-finetuned-libero-goal`

---

## 1. Phase 1: Preflight Status

- **Hostname:** `PCROBOTUBUNTU02`
- **GPU Name:** `NVIDIA GeForce RTX 4070 Ti SUPER`
- **Free VRAM:** `13.09 GB` (out of 16.0 GB total)
- **Disk Free Space:** `504 GB` free space on `/media/rootalkhatib/My Passport`
- **Active Tmux Sessions:**
  - `ood_production_aggressive_fixed_100ep_20260609`
  - `stage5`
  - `task6_aggressive_20260608`
  - `task6_aggressive_old_detector_20260608`
  - `openvla_goal_object_pro_risk_data_10000ep_20260616` (just launched)
- **Active GPU Processes:**
  - `/usr/lib/xorg/Xorg` (90MiB)
  - `/usr/bin/gnome-shell` (8MiB)
- **Expected Output Size for 10,000 Episodes:**
  - Video logs (first 3 episodes per task + failures after step 300):
    - First 3 episodes * 10 tasks = 30 videos.
    - Failures: assuming 20% failure rate out of 10,000 episodes = 2,000 failed episodes.
    - Total videos = ~2,030. At ~15MB per GIF video = ~30 GB.
  - JSONL Trajectory logs + Action Chunks: ~1.3 GB.
  - Total expected dataset size: ~32 GB.
  - Is disk space sufficient? **YES** (504 GB available is more than 15x the requirement).

---

## 2. Phase 2: 10-Task Smoke Test Verification

- **Smoke Runner:** `src/run_openvla_goal_object_pro_10task_smoke_bob.py`
- **Smoke Output Root:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/goal_object_pro_10task_smoke_20260616/`
- **Smoke Log Root:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/goal_object_pro_10task_smoke_20260616/`
- **Verification Details:** All 10 tasks successfully initialized, reset, performed forward inference queries, produced valid action shapes `(8, 7)`, and completed without infrastructure errors.

---

## 3. Phase 3: Risk-Data Collection Details

- **Collection Runner:** `src/collect_openvla_oft_goal_object_pro_risk_data_round_robin_bob.py`
- **Tmux Session:** `openvla_goal_object_pro_risk_data_10000ep_20260616`
- **Log file:** `logs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616/collector_supervisor.log`
- **Output root:** `outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616`
- **Run Configurations:**
  - Total Target Episodes: 10000
  - Tasks: 0..9 (sequential in round-robin order)
  - Max Steps: 800
  - Reset Seed Plan: `reset_seed = 100000 + round_idx` (all tasks in same round share the seed)
  - Video policy: Save first 3 episodes of each task, and all failures after step 300.
  - Candidate Generation (ACE): `ACE_AVAILABLE = NO` (stochastic candidate generation is not available because OpenVLA uses L1 regression head deterministically). Saved `OPENVLA_ACTION_STAT_FEATURES` instead.
  - Rolling History: Saved history window of size 8 for proprio states, executed actions, and query statistics.

---

## 4. Phase 5: Initial Monitoring Verification

- Task 0, 1, 2, and 3 have completed at least one episode:
  - **Round 0, Task 0:** Success (True), 134 steps
  - **Round 0, Task 1:** Success (True), 82 steps
  - **Round 0, Task 2:** Success (True), 76 steps
  - **Round 0, Task 3:** Success (True), 173 steps
- Records are being written to:
  - `episode_summaries.jsonl`
  - `query_records.jsonl`
  - `step_records.jsonl`
  - `round_0_action_chunks.npz` (will save at end of round 0)
- Verified `collection_status.json` updates correctly:
  - `total_episodes_completed` is currently 4.
  - `next_round` is 0, `next_task` is 4.
- Verified rolling history window shifts and pads correctly.
- No NaNs or Infinite actions were observed.

---

## 5. Conclusion & Recommendations

The large-scale data collection was successfully initiated and is running stably in tmux. All dataset schemas, seed plans, and collection status tracking files are set up properly. It is safe to leave the collection running.
