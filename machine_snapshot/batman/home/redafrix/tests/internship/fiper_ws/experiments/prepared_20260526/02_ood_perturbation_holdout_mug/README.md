# OOD Perturbation Holdout: mug

## Purpose
Stress-test FIPER RND and ACE monitors on unseen perturbation type `mug`.

## Logic
- Perturbation group `mug` is held out from training and calibration.
- **Training**: RND trained on `success_train_seen` (non-mug successes).
- **Calibration**: Calibrated on `success_calib_seen`.
- **Evaluation**: Evaluated on seen test successes/failures, OOD test successes (`success_test_ood`), and OOD failures (`failure_eval_ood`, late, near_end).
