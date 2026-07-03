# Per-Suite: libero_spatial_env

## Purpose
Train a specialized FIPER monitor only on `libero_spatial_env` suite data.

## Logic
- Status: **READY**
- Only `libero_spatial_env` data is included in this split.
- **Training**: RND trained on `success_train` (only `libero_spatial_env` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
