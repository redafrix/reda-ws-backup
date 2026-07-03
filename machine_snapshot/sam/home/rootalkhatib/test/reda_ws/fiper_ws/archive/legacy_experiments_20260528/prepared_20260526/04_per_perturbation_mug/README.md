# Per-Perturbation: mug

## Purpose
Train a specialized FIPER monitor only on `mug` perturbation data.

## Logic
- Only `mug` data is included in this split.
- **Training**: RND trained on `success_train` (only `mug` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
