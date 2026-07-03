# Forensic Audit Report: LIBERO Goal Object OOD 10-Episode Aggressive-Fixed Run

**Date:** 2026-06-09  
**Audit Author:** Antigravity (Workspace Catalog & Forensic Audit)  
**Target Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609`

---

## 1. Executive Summary
This report presents the forensic sanity audit of the corrected 10-episode aggressive-fixed out-of-distribution (OOD) evaluation on **Bob**. The audit is strictly read-only. No configurations, scripts, checkpoints, or active runs were modified.

The old q95 run was successfully invalidated and excluded from all result calculations because it did not use the intended aggressive threshold settings. 

The corrected 10-episode aggressive-fixed run completed successfully, executing a total of **540 episodes** across 18 tasks and 3 policies. 

---

## 2. Mechanical Trustworthiness & Configuration Check
We verified the mechanical validity of the completed 10-episode aggressive-fixed run:
* **Root Verification:** Verified as `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609`. The old deprecated `h10_goal_object_ood_all_tasks_10ep_20260609` directory was ignored.
* **Task Presence:** All 18 tasks (`task0` to `task17`) are present in the `runs/` folder.
* **Policy Presence:** All 3 policies (`original_simvla`, `modified_simvla`, `modified_h10_risk_topk8`) are present under each task.
* **Episode Counts:** Exactly 10 episodes were executed per task/policy (540 episodes total).
* **Seed Parity & Uniqueness:** Verified. All policies share the same 10 seeds (`range(10)`, seeds 0-9) per task. There are no duplicate seeds and no missing tasks.
* **Row Integrity:** No stale rows, no error rows (0-step rows), and no tracebacks, OOMs, or missing files are present in the logs.
* **Suite Name Verification:** The suite is verified as exactly `libero_goal_object_ood` in all configs and JSONL outputs. No fallback occurred.
* **Aggressive Controls Verification:** The `run_manifest.json` files for the risk policy confirm that the intended selection controls were used at runtime:
  - `selection_main_threshold = 0.3`
  - `selection_streak_threshold = 0.3`
  - `selection_min_margin = 0.02`
  - `selection_strong_margin = 0.05`
* **Checkpoint Identity Audit:**
  - `original_simvla` successfully used the original paper SimVLA checkpoint (SHA256: `9d3b1767...`).
  - `modified_simvla` used `ckpt-60000` (SHA256: `3fab12d9...`).
  - `risk_topk8` used `ckpt-60000` (SHA256: `3fab12d9...`) and the H10 TopK8 detector (`unc_topk8` from `h10_goal_object_risk_proof_20260608`).

---

## 3. Performance & Paired Analysis (10-Episode Run)

Because this evaluation contains only 10 seeds per task, we explicitly mark the statistical strength of these results as **WEAK (early signal only)**.

### Success Rates & Step Counts
* **original_simvla:** **93.9%** (169 / 180 successes), Mean Steps: **127.16**
* **modified_simvla:** **93.3%** (168 / 180 successes), Mean Steps: **122.41**
* **risk_topk8:** **95.6%** (172 / 180 successes), Mean Steps: **118.49**

### Paired Outcome Composition (Total)
* **Modified SimVLA vs Original SimVLA:**
  - **Rescues:** 8
  - **Regressions:** 9
  - **Both Success:** 160
  - **Both Fail:** 3
  - *Net Gain:* **-1** success (-0.6%)
* **Risk TopK8 vs Modified SimVLA:**
  - **Rescues:** 6
  - **Regressions:** 2
  - **Both Success:** 166
  - **Both Fail:** 6
  - *Net Gain:* **+4** successes (+2.2%)
* **Risk TopK8 vs Original SimVLA:**
  - **Rescues:** 9
  - **Regressions:** 6
  - **Both Success:** 163
  - **Both Fail:** 2
  - *Net Gain:* **+3** successes (+1.7%)

### Action Modification Statistics (risk_topk8)
* **Episodes with Modifications:** 80 / 180 (44.4%)
* **Total Modifications:** 254 mods
* **Modifications per Episode:** 1.41
* **Query Modification Rate:** **5.31%** (108 modifications out of 2,034 queries)

---

## 4. Per-Task Success Rate & Paired Details

| Task | Orig SR | Mod SR | Risk SR | Risk vs Mod (Res/Reg) | Risk vs Orig (Res/Reg) |
|---|---|---|---|---|---|
| 0 | 80.0% | 80.0% | 80.0% | 2 / 2 | 1 / 1 |
| 1 | 100.0% | 90.0% | 90.0% | 0 / 0 | 0 / 1 |
| 2 | 90.0% | 80.0% | 90.0% | 1 / 0 | 1 / 1 |
| 3 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 4 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 5 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 6 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 7 | 90.0% | 90.0% | 90.0% | 0 / 0 | 1 / 1 |
| 8 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 9 | 100.0% | 90.0% | 90.0% | 0 / 0 | 0 / 1 |
| 10 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 11 | 90.0% | 100.0% | 100.0% | 0 / 0 | 1 / 0 |
| 12 | 90.0% | 100.0% | 100.0% | 0 / 0 | 1 / 0 |
| 13 | 60.0% | 80.0% | 90.0% | 1 / 0 | 3 / 0 |
| 14 | 100.0% | 90.0% | 100.0% | 1 / 0 | 0 / 0 |
| 15 | 100.0% | 100.0% | 100.0% | 0 / 0 | 0 / 0 |
| 16 | 100.0% | 90.0% | 90.0% | 0 / 0 | 0 / 1 |
| 17 | 90.0% | 90.0% | 100.0% | 1 / 0 | 1 / 0 |

---

## 5. Read-Only Status Check of 100-Episode Run
* **100ep Root Exists:** **NO** (Checked `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/` for `h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`, folder is not created yet).
* **Launch Report Exists:** **NO**
* **Tmux Session `ood_production_aggressive_fixed_100ep_20260609` Alive:** **NO** (Not running).
* **Completed Jobs/Episodes:** 0 / 54 jobs, 0 / 5,400 episodes.
* **Tracebacks/OOM:** None (the experiment has not launched).
* **Verdict:** CLI 1 is preparing or has not yet kicked off the 100ep campaign. It is safe to let CLI 1 proceed with launching and managing the run.

---

## SUMMARY FLAGS
AUDIT_READ_ONLY = YES
ANY_EXPERIMENT_LAUNCHED = NO
ANY_RUNNING_JOB_TOUCHED = NO
TEN_EP_ROOT_CORRECT = YES
TEN_EP_TOTAL_540 = YES
TEN_EP_SEED_PARITY_PASS = YES
TEN_EP_THRESHOLD_RUNTIME_PASS = YES
TEN_EP_CHECKPOINT_IDENTITY_PASS = YES
TEN_EP_SUITE_IDENTITY_PASS = YES
TEN_EP_RESULTS_TRUSTWORTHY_MECHANICALLY = YES
TEN_EP_SCIENTIFIC_STRENGTH = WEAK
HUNDRED_EP_ROOT_EXISTS = NO
HUNDRED_EP_RUNNING = NO
HUNDRED_EP_SAFE_TO_LET_CLI1_CONTINUE = YES
MOST_IMPORTANT_FINDING = The corrected 10ep OOD sweep completed successfully, demonstrating a slight net gain (+4 over modified baseline) under aggressive settings, while the 100ep sweep is not yet launched.
NEXT_STEP = Let CLI 1 launch and run the 100-episode campaign.
