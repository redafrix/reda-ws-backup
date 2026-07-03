# FIPER Training Script Fix Report

**Date:** Tuesday, May 26, 2026
**Status:** Success (Script Audited, Fixed, and Smoke-Tested)

## 1. Issues Identified in First Script
- **ACE Metrics:** Only implemented a simple variance-based mean, missing Gaussian entropy and component-wise breakdown (rotation, translation, gripper).
- **Sanity Checks:** Limited to 'zero' and 'noise' modes; lacked coverage for temporal shuffling, scaling, and gripper flipping.
- **Output Structure:** Used generic filenames and flat directory structure, inconsistent with the required audit-ready artifact organization.
- **Early Detection:** Lacked detailed temporal metrics (mean/median alarm time) and multi-quantile alarm rate summaries.

## 2. Fixes and Improvements
- **Comprehensive ACE:** Implemented `compute_ace_metrics` providing Gaussian entropy (via logdet of covariance), mean pairwise distance, and step/component-wise standard deviations.
- **Enhanced Sanity Suite:** Expanded `generate_corrupted_rows` to 10 modes including `shuffled_timestep_order`, `reversed_timestep_order`, `scaled_x2_clipped`, and `gripper_flipped`.
- **Structured Outputs:** Enforced organization into `models/`, `thresholds/`, `scores/`, `evals/`, and `reports/`.
- **Detailed Detection Metrics:** Implemented `summarize_episodes_detailed` to track first alarm indices and normalized times for RND, ACE, and FIPER (OR/AND) logic.
- **Reporting:** Added automated Markdown report generation summarizing detection performance and sanity check sensitivity.

## 3. Validation
- **py_compile:** PASSED.
- **smoke_v2:** PASSED.
    - **Experiment Dir:** `experiments/fiper_receding_only_global_v1_smoke_v2`
    - **Outcome:** Script completed training, calibration, multi-split evaluation, and sanity checks on CPU with limited data.

## 4. Produced Artifacts (Audit Ready)
- `models/rnd_predictor.pt`, `models/rnd_target.pt`
- `models/rnd_normalization.json`, `models/rnd_training_summary.json`
- `thresholds/rnd_thresholds.json`, `thresholds/ace_thresholds.json`
- `scores/rnd_scores_by_split.jsonl`, `scores/ace_scores_by_split.jsonl`, `scores/fiper_scores_by_split.jsonl`
- `evals/alarm_rates_by_split.json`, `evals/failure_early_detection_summary.json`
- `evals/failure_early_detection_by_episode.csv`, `evals/corrupted_action_eval.json`
- `reports/FIPER_RECEDING_ONLY_GLOBAL_V1_REPORT.md`

## 5. Final Verdict
The script is now fully compliant with the FIPER experiment design and is ready for the high-volume training run on Sam.

## 6. Recommended Full Training Command
```bash
cd /home/rootalkhatib/test/reda_ws/fiper_ws
source ../asynchvla_ws/scripts/activate_simvla_sam.sh
python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/fiper_receding_only_global_v1 \
  --device cuda \
  --epochs 20 \
  --batch-size 256 \
  --seed 42
```
