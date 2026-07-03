# OOD Suite Family Holdout: spatial

## Purpose
Stress-test FIPER RND and ACE monitors on unseen suite family `spatial`.

## Logic
- Suite family `spatial` is held out from training and calibration.
- **Training**: RND trained on `success_train_seen` (non-spatial successes).
- **Calibration**: Calibrated on `success_calib_seen`.
- **Evaluation**: Evaluated on seen test successes/failures, OOD test successes (`success_test_ood`), and OOD failures (`failure_eval_ood`, late, near_end).
