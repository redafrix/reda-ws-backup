# OOD Task Split

## Purpose
Stress-test FIPER RND and ACE monitors on unseen tasks (IDs 8 and 9).

## Logic
- Task IDs 8 and 9 are held out. They are NEVER seen in training or calibration.
- **Training**: RND trained on `success_train_seen` (IDs 0-7 successes).
- **Calibration**: Calibrated on `success_calib_seen`.
- **Evaluation**: Evaluated on seen test successes/failures, OOD test successes (`success_test_ood`), and OOD failures (`failure_eval_ood`, late, near_end).
