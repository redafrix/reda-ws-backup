# Per-Suite: libero_10_with_milk

## Purpose
Train a specialized FIPER monitor only on `libero_10_with_milk` suite data.

## Logic
- Status: **READY**
- Only `libero_10_with_milk` data is included in this split.
- **Training**: RND trained on `success_train` (only `libero_10_with_milk` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
