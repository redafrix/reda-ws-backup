# Per-Perturbation: env

## Purpose
Train a specialized FIPER monitor only on `env` perturbation data.

## Logic
- Only `env` data is included in this split.
- **Training**: RND trained on `success_train` (only `env` successes).
- **Calibration**: Calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test`, `failure_eval`, `failure_eval_late`, and `failure_eval_near_end`.
