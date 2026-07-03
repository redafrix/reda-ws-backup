# Catalog and Obsidian Update Report: OOD Sweep Audit

**Date:** 2026-06-09  
**Audit Author:** Antigravity (Workspace Catalog Audit)

This report logs the updates performed on the experiment catalog and the main Obsidian report following the forensic sanity audit of the LIBERO-PRO Goal-Object-OOD aggressive campaigns on Bob.

---

## 1. Backups Created
The following backups were created prior to any modifications:
* **Obsidian report backup:** `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md.20260609_164500.bak`
* **Local inventory backup (created in previous phase):** `fiper_ws/experiment_catalog/inventory.json.20260609_153500.bak`

---

## 2. Experiment Catalog Updates
The canonical local experiment catalog directory (`/home/redafrix/tests/internship/fiper_ws/experiment_catalog/`) was updated with the following:
* **MASTER_EXPERIMENT_INDEX.md:** Added entries for Campaign 5 (invalid OOD sweep), Campaign 6 (corrected 10ep OOD sweep), and Campaign 7 (100ep OOD sweep).
* **TRUSTED_RESULTS_SUMMARY.md:** Added a dedicated section detailing the success rates, paired metrics, and query modification counts for the corrected 10ep OOD sweep, and marked the 100ep run as Preparing / Running. Added the campaigns to the final Trust Verdicts Summary table.
* **FORENSIC_AUDIT_MAP.md:** Appended Step 9 outlining the purpose and mechanical/scientific trust results of the OOD Sweep Audit.
* **inventory.json:** Updated the machine-readable JSON inventory with structured entries for `h10_goal_object_ood_all_tasks_10ep_20260609` (invalid q95 run), `h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609` (corrected 10ep run), and `h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609` (100ep run).

---

## 3. Obsidian Report Updates
We successfully appended **Section 19 ("June 9: LIBERO-PRO Goal-Object-OOD Aggressive Check")** to the end of `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`.
The section outlines:
* The motivation and setup of the aggressive OOD check.
* Explicit warning/exclusion of the invalid initial sweep.
* The verified 10ep setup and detailed performance metrics (Original: 93.9%, Modified: 93.3%, Risk: 95.6%).
* The paired rescue/regression breakdown (+4 successes over modified baseline, 6 rescues vs 2 regressions).
* True modification stats (254 mods, 5.31% query modification rate).
* A per-task 10-episode success rate table.
* The Preparing/Running status of the 100-episode campaign, with a clear warning on the weak statistical strength of 10-episode data.
* Links to the local forensic audit report and the completed 10ep experiment root on Bob.

---

## 4. Sync Status
All modified catalog files (`MASTER_EXPERIMENT_INDEX.md`, `TRUSTED_RESULTS_SUMMARY.md`, `FORENSIC_AUDIT_MAP.md`, and `inventory.json`) were successfully synchronized to:
* **Bob:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiment_catalog/`
* **Dean:** `/home/dean/fiper_uncertainty_collection/experiment_catalog/`
* **Sam:** `/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog/`

---

## 5. Remaining Risk Analysis
* **100ep Campaign Execution:** The 100-episode sweep is currently preparing. It is fully managed by CLI 1. No other runs on Bob are active or in conflict.
* **No Interventions:** We did not interfere with any running configurations or tmux sessions. It is safe for CLI 1 to continue launching and managing the production run.

---

## SUMMARY FLAGS
```text
CATALOG_UPDATED = YES
OBSIDIAN_BACKUP_CREATED = YES
OBSIDIAN_SECTION_ADDED = YES
BOB_SYNCED = YES
DEAN_SYNCED = YES
SAM_SYNCED = YES
HUNDRED_EP_STATUS_REGISTERED = YES
FINAL_VERDICT = COMPLETE
```
