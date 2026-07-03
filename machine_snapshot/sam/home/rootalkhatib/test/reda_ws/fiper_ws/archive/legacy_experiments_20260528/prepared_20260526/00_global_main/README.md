# Global Main Experiment

## Purpose
Train the final canonical FIPER monitor using all successful receding SimVLA data from Sam and Bob.

## Logic
- **Training**: RND model is trained on `success_train` (success-only rows).
- **Calibration**: Conformal thresholds for RND and ACE policy entropy are calibrated on `success_calib`.
- **Evaluation**: Evaluated on `success_test_id`, `failure_eval_all`, and failure subclasses (early, mid, late, near_end).
- **Stress-Testing**: OOD task/perturbation splits are NOT trained here; those are diagnostics.
