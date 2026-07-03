# Forensic Audit & Checking Artifacts Directory

This directory contains only the forensic audit and checking artifacts created or used during the forensic sanity audit of the H10 risk-aware SimVLA simulation results.

> [!NOTE]
> No experiment data, raw outputs, or project source code from the main repository was moved to this folder. All files here are strictly for checking, audit analysis, and report generation purposes.

---

## 1. Reports Uploaded to Bob (`pcrobot`)

The final versions of the audit reports were uploaded to the remote host **`pcrobot`** at their designated paths:

| Audit Step | Report File Name | Remote Path on `pcrobot` |
| :--- | :--- | :--- |
| **Step 1** | `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md` |
| **Step 2** | `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md` |
| **Step 3** | `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md` |
| **Step 4** | `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md` |
| **Step 5** | `H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md` |
| **Step 6** | `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md` | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md` |

---

## 2. Audit Helper Scripts

The following scripts were used to extract data, compute statistics, or generate the local and remote reports:

* **Step 1 & 2 Setup and Data Analysis:**
  * `remote_audit.py` - Collects campaign-wide directories, checks log files for exceptions, and compiles model SHAs.
  * `analyze_results.py` - Computes basic success/failure metrics from campaigns.
  * `check_cross_campaign_seeds.py` - Evaluates seed overlap and parity across campaigns.
  * `calculate_rescues_remote.py` - Computes basic rescues and regressions based on parsed stats.
  * `check_interventions_remote.py` - Scans remote logs for intervention timesteps.
  * `extract_fragility_details.py` - Extracts step scores, risk scores, and reasons for rescues and regressions.
  * `generate_step2_report.py` - Compiles the Step 2 markdown report.
  * `run_detailed_checks.py`, `summarize_bob_experiments.py`, `validate_smoke.py`, `deep_analyze_ood.py`, `compute_paired_rescues.py`, `generate_final_report.py` - Additional helper and plotting scripts.
* **Step 3 (Pairing Bugcheck):**
  * `audit_jsonl_detail.py` - Bottom-up scan of raw JSONLs for row counts, keys, duplicates, and shard overlaps.
  * `run_pairing_remote.py` - Computes clean seed-by-seed rescues, regressions, and shared successes/failures from raw JSONLs.
  * `generate_step3_report.py` - Compiles the Step 3 report.
* **Step 4 (Risk Score Analysis & Threshold Sweep):**
  * `calculate_step4_metrics.py` - Groups episodes by seed status and calculates detailed query risk score statistics.
  * `calculate_step4_thresholds.py` - SWEPT threshold sensitivity metrics using risk logs.
  * `generate_step4_report.py` - Compiles the Step 4 report.
* **Step 5 (Forensic Synthesis):**
  * `generate_final_synthesis.py` - Integrates Step 1-4 reports and OOD goal-swap reports to compile the Step 5 synthesis.
* **Step 6 (Gating & Finer Sweep Audit):**
  * `calculate_step6_all.py` - Performs recomputations of intervention rates, threshold sweeps, and evaluates alternative gating options.
  * `generate_step6_report.py` - Compiles the Step 6 report.

---

## 3. Directory File Breakdown

### Final Forensic Reports
* `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md`
* `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md`
* `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md`
* `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md`
* `H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md`
* `H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md`
* `OOD_GOAL_SWAP_FINAL_PAIRED_ANALYSIS_20260609.md`
* `BOB_H10_RISK_OOD_STATUS_AUDIT_20260609.md`
* `report_draft.md`

### Temporary Data & Output Logs
* `audit_results.json`
* `audit_results_detail.json`
* `ood_paired_analysis.json`
* `pairing_results.txt`
* `extract_results.txt`
* `step4_analysis.txt`
* `step4_thresholds.txt`
* `step6_all_analysis.txt`
