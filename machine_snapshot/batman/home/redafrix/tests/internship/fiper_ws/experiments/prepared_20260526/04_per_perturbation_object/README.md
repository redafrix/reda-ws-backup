# Per-Perturbation: object

## Purpose
Train a specialized FIPER monitor only on `object` perturbation data.

## Logic
- Only `object` data is included in this split.
- **Training**: RND trained on `success_train` (only `object` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
