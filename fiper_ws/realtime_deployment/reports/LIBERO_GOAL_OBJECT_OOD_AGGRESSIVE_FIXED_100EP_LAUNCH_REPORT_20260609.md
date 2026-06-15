# Launch Report: LIBERO Goal Object OOD 100-Episode Aggressive-Fixed Sweep

**Date:** 2026-06-09  
**Audit Author:** Antigravity (Workspace Catalog & Forensic Audit)  
**Target Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`

---

## 1. Preflight & Hardware Health Status
* **Old Session Check:** Verified no other supervisor or tmux sessions are active for this campaign on **Bob**.
* **GPU memory:** 7.1 GB used out of 16.3 GB (rtx 4070 Ti). Process `2456295` successfully active on GPU.
* **Disk Space:** 526 GB available on `/media/rootalkhatib/My Passport` mount (72% utilized), which is ample for 5,400 episodes.

---

## 2. Configuration & Seed Plan Verification
* **New 100ep Root Created:** Yes, at `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`.
* **Config Count:** Exactly 54 configs generated (18 tasks × 3 policies).
* **Reset Seeds:** Generated 100 unique, deterministic seeds (`range(10, 110)`, seeds 10 to 109). These are disjoint from the smoke/10ep seeds (0-9).
* **Seed Plan Saved:** Verified saved to `configs/seed_plan.json`.
* **Seed Parity:** Verified that all 3 policies within each task use the exact same 100 seeds.
* **Config Parameter Audit:**
  - `suite`: Checked. Set to exactly `libero_goal_object_ood` everywhere.
  - `checkpoint`: Checked. `original_simvla` points to paper SimVLA; `modified_simvla` and `modified_h10_risk_topk8` point to `/tmp/ood_ckpt60000` (SHA256: `3fab12d9...`).
  - `detector`: Checked. Points to `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`.
  - `selection_controls`: Aggressive values are explicitly defined at the config level:
    * `selection_main_threshold = 0.3`
    * `selection_streak_threshold = 0.3`
    * `selection_min_margin = 0.02`
    * `selection_strong_margin = 0.05`
  - No broken zip files or deprecated `/tmp/ckpt-60000-tmp` checkpoints are referenced.

---

## 3. Config Audit Table (Step 3 Summary)

| Task Range | Policies | Seed Count | Suite | Output Root | Checkpoint Paths | Detector Path | Gating controls |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| Tasks 0-17 | `original_simvla` | 100 | `libero_goal_object_ood` | `runs/task{id}/original_simvla` | `checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO` | N/A | None |
| Tasks 0-17 | `modified_simvla` | 100 | `libero_goal_object_ood` | `runs/task{id}/modified_simvla` | `/tmp/ood_ckpt60000` | N/A | None |
| Tasks 0-17 | `modified_h10_risk_topk8` | 100 | `libero_goal_object_ood` | `runs/task{id}/modified_h10_risk_topk8` | `/tmp/ood_ckpt60000` | `unc_topk8` retrained | Threshold 0.3 / Margins 0.02, 0.05 |

---

## 4. Production Launch & Immediate Health Check
* **Detached Tmux Session:** Successfully created and running under name `ood_production_aggressive_fixed_100ep_20260609`.
* **Active Processes:**
  - One supervisor: `python3 run_all.py` (PID `2456294`).
  - One active job: `python3 .../run_policy_matrix.py ...` (PID `2456295`).
* **Persistent Log:** Stdout/Stderr redirected to `sweep_supervisor.log` in the root folder.
* **Log Status:** Advancing. 3 episodes of Task 0 `original_simvla` have already completed successfully with seeds 10, 11, and 12.
* **Tracebacks/OOMs:** None. Log is clean.
* **Estimated Execution Time:** ~15 hours (5,400 episodes total × ~10s average per episode).

---

## FINAL REPORT FLAGS
```text
NEW_100EP_ROOT_CREATED = YES
CONFIG_COUNT_54 = YES
TOTAL_EXPECTED_EPISODES = 5400
ALL_18_TASKS_PRESENT = YES
ALL_3_POLICIES_PRESENT = YES
NEW_100_SEEDS_USED = YES
SEED_PARITY_PASS = YES
OLD_10_SEEDS_ONLY_USED = NO
ASSET_MAPPING_PASS = YES
NO_BROKEN_ZIP_REFERENCE = YES
NO_DEPRECATED_TMP_CKPT_REFERENCE = YES
CHECKPOINT_SHA256_PASS = YES
RISK_CONFIGS_AGGRESSIVE_PASS = YES
RISK_RUNTIME_AGGRESSIVE_PASS = NOT_YET_AVAILABLE
Q95_FALLBACK_USED = NO
PRODUCTION_LAUNCHED = YES
TMUX_SESSION = ood_production_aggressive_fixed_100ep_20260609
DUPLICATE_PROCESSES_FOUND = NO
SAFE_TO_MONITOR = YES
ESTIMATED_TIME_REMAINING = ~15 hours
CATALOG_UPDATED = YES
OBSIDIAN_FINAL_RESULTS_UPDATED = NO
MOST_IMPORTANT_FINDING = The corrected 100ep OOD sweep has been successfully launched in a detached tmux session with deterministic seeds 10-109 and verified aggressive gating controls.
NEXT_ACTION = monitor only
```
