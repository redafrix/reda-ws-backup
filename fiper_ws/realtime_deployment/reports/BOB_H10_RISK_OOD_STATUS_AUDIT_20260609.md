# Bob H10 Risk-Aware & OOD Status Audit (2026-06-09)

## 1. Executive Summary
The OOD goal-swap production campaign is **FULLY COMPLETED** (900/900 episodes). Seed parity is perfect across all policies.
The main `risk_proof` campaign is partially complete; Task 3 and Task 6 are finished, but Task 8 (modified policies) was interrupted by a `KeyboardInterrupt`.
Aggressive TopK8 ablations and old detector tests are **COMPLETED**.

**Overall Status:** READY FOR ANALYSIS (with Task 8 caveat).

## 2. Host & Process Status
- **Host:** PCROBOTUBUNTU02
- **Date:** Tue Jun  9 09:11:55 AM CEST 2026
- **GPU:** NVIDIA GeForce RTX 4070 (Usage: 53W / 285W, Memory: 3282MiB / 16376MiB)
- **Disk Space (/media/rootalkhatib/My Passport):** 72% used (527G available)
- **Active Processes:** No `run_policy_matrix` or `run_online_groups` processes found.
- **Active Tmux Sessions:**
  - `stage5`
  - `task6_aggressive_20260608`
  - `task6_aggressive_old_detector_20260608`
  Note: The `h10_goal_swap_ood_100ep_20260608` tmux session is **MISSING**, likely because the script finished and closed the session.

## 3. Experiment Status Details

### A. OOD Goal-Swap Production Campaign
**Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608`
**Status:** COMPLETE (900/900 episodes)

| Task | Policy | Episodes | Success Rate | Mean Steps | Mod Ep Count | Total Mods |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| top_drawer_bowl | original_simvla | 100 | 15% | 289.4 | 0 | 0 |
| top_drawer_bowl | modified_simvla | 100 | 9% | 294.2 | 0 | 0 |
| top_drawer_bowl | risk_topk8 | 100 | 8% | 295.5 | 70 | 200 |
| cream_cheese_bowl | original_simvla | 100 | 0% | 300.0 | 0 | 0 |
| cream_cheese_bowl | modified_simvla | 100 | 0% | 300.0 | 0 | 0 |
| cream_cheese_bowl | risk_topk8 | 100 | 0% | 300.0 | 100 | 530 |
| bowl_on_plate | original_simvla | 100 | 1% | 299.6 | 0 | 0 |
| bowl_on_plate | modified_simvla | 100 | 3% | 297.5 | 0 | 0 |
| bowl_on_plate | risk_topk8 | 100 | 2% | 298.5 | 93 | 371 |

**Seed Parity:** Verified. All policies share the same 100 seeds per task.

---

### B. Main H10 Goal-Object Campaign (Risk Proof)
**Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`
**Status:** PARTIAL (Interrupted at Task 8)

- **Task 3:** Complete (100 ep per policy) - ~10-18% success.
- **Task 6:** Complete (100 ep per policy) - ~48-62% success.
- **Task 8:**
  - `original_simvla`: 100 ep (Complete) - 91% success.
  - `original_h10_risk_base`: 100 ep (Complete) - 91% success.
  - `modified_simvla`: 5 ep (FAILED - KeyboardInterrupt).
  - `modified_h10_risk_topk8`: 2 ep (FAILED - KeyboardInterrupt).

---

### C. Aggressive TopK8 Ablations
**Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`
**Status:** COMPLETE

- **Task 3:** 100 ep - 19% success.
- **Task 6:** 100 ep - 62% success.
- High intervention rates observed on Task 6 (48/50 episodes modified).

---

### D. Old TopK8 Detector Task 6 Ablation
**Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`
**Status:** COMPLETE

- **Task 6:** 100 ep - 60% success.
- Seed parity across shards verified.

## 4. Warnings & Suspicious Findings
- **KeyboardInterrupt:** The interruption in the `risk_proof` campaign for Task 8 is unexplained but consistent across several logs. It likely happened during a manual intervention or a global stop command.
- **Low Success in OOD:** `cream_cheese_bowl` has 0% success across all policies. This suggests the OOD task is extremely difficult or there is a domain gap issue.
- **Intervention Count:** `risk_topk8` is intervening very frequently (up to 100% of episodes in some OOD tasks).

## 5. Important Paths
- **Summaries:** `episode_summaries.jsonl` files in respective `runs/` subdirectories.
- **Detailed Audit Data (Local):** `experiment_summaries.json` (created by Gemini CLI).
- **This Report:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/BOB_H10_RISK_OOD_STATUS_AUDIT_20260609.md`

## 6. Recommendations
1. **Analyze OOD:** Proceed with analysis of the 900 episodes.
2. **Restart Task 8:** If Task 8 results for modified policies are critical, they need to be restarted.
3. **Threshold Review:** The high intervention rate (70-100%) in OOD indicates the 0.3 threshold might be too sensitive for these tasks.
