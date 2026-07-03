# Per-Suite: libero_object_object

## Purpose
Train a specialized FIPER monitor only on `libero_object_object` suite data.

## Logic
- Status: **READY**
- Only `libero_object_object` data is included in this split.
- **Training**: RND trained on `success_train` (only `libero_object_object` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
