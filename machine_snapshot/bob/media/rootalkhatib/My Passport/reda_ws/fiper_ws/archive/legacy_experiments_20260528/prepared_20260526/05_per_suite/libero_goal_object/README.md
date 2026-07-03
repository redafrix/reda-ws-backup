# Per-Suite: libero_goal_object

## Purpose
Train a specialized FIPER monitor only on `libero_goal_object` suite data.

## Logic
- Status: **READY**
- Only `libero_goal_object` data is included in this split.
- **Training**: RND trained on `success_train` (only `libero_goal_object` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
