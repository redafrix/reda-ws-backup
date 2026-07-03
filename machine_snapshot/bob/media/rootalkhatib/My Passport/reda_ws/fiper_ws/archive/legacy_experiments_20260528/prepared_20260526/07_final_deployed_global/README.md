# Final Deployed Global Alias

## Purpose
Alias folder for the final production monitor training and calibration config.

## Logic
- Identical to `00_global_main` references.
- Train RND on `success_train`.
- Calibrate RND and ACE on `success_calib`.
- Evaluate on test ID and failure classes.
- Diagnostic stress tests are kept separate.
