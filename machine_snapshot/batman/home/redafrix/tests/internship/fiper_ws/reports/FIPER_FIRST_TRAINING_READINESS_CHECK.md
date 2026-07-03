# FIPER First Training Readiness Check

**Date:** Tuesday, May 26, 2026
**Status:** Ready (Pending Script Creation)

## 1. Collector Status
- **Sam:** No collectors running.
- **Bob:** No collectors running.
- **Verification Command:** `pgrep -af "[c]ollect_fiper_receding_all_outcomes_v2"`

## 2. Dataset Integrity
- **Combined JSONL Row Counts:**
    - `bob_instance_A`: 158,128
    - `bob_instance_B`: 158,063
    - `sam_instance_A`: 159,838
    - `sam_instance_B`: 159,892
    - **Total:** 635,921 rows (Matches expected 635,921).
- **Location:** `data/frozen/fiper_sweep_eternal_20260526_combined/`

## 3. Global Split References
- **Status:** All expected split references exist on Sam.
- **Files Checked:**
    - `success_train.rows.jsonl` (324,825 rows)
    - `success_calib.rows.jsonl` (70,352 rows)
    - `success_test_id.rows.jsonl` (69,144 rows)
    - `failure_eval_all.rows.jsonl` (171,600 rows)
    - `failure_eval_early.rows.jsonl`
    - `failure_eval_mid.rows.jsonl`
    - `failure_eval_late.rows.jsonl`
    - `failure_eval_near_end.rows.jsonl`

## 4. Split Purity and Exclusions
- **Train/Calib Purity:** Verified success-only. No `failure_or_timeout` entries found in `success_train.rows.jsonl`.
- **Failure Eval Purity:** Verified failure-only. No `success` entries found in `failure_eval_all.rows.jsonl`.
- **Ignored Tasks:** `libero_10_with_milk` task 3 and task 4 are successfully excluded from all splits.
- **Data Traceability:** Each row ref includes `source_jsonl` and `line_no` for direct lookup.

## 5. Training Script
- **Script Name:** `scripts/run_receding_only_fiper_train_eval.py`
- **Status:** **MISSING**. The script does not exist on Sam or Bob yet.

## 6. Recommendation
- **Safety:** It is safe to proceed with the first training run once the training script is authored.
- **Next Step:** Create `scripts/run_receding_only_fiper_train_eval.py` with the following requirements:
    - Train RND observation embedding strictly on `success_train`.
    - Calibrate conformal thresholds strictly on `success_calib`.
    - Evaluate ACE and RND alarms on all failure evaluation splits.
    - Report early failure detection metrics.

**Final Verdict:** **Ready to author training script.**
