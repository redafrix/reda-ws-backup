# Prelaunch Validation

## Result

`PASS`

## Runtime Smokes

- Total distinct branches: 16
- Passed: 16
- Failed: 0
- Horizons: 1 and 10
- Checkpoints: original SimVLA and modified checkpoint 60000
- Detector compatibility enforced:
  - base with original or modified SimVLA
  - Top-8 only with modified SimVLA

## Fairness Check

For original/base shadow and modified/base or Top-8 shadow, baseline and shadow
traces matched exactly on:

- query index
- environment timestep
- main action seed
- main chunk SHA-256

Every shadow selected candidate zero. This proves ACE generation and risk
scoring do not alter the baseline main chunk when no action change is applied.

## CUDA Determinism

The initial smoke found the missing cuBLAS workspace setting. The campaign now
exports `CUBLAS_WORKSPACE_CONFIG=:4096:8` before Python starts. All 16 clean
reruns passed without the warning.

## Training Smoke

- Dataset: exact goal-object chunk10 collection
- Episodes: 200
- Successes: 162
- Failures: 38
- Policy queries: 2,657
- Variants: base and fixed Top-8
- Splits: all-task random and last-two-task holdout
- Result: all four detector artifacts produced successfully

## Launch

- Host: Bob (`pcrobot`)
- Tmux: `bob_risk_matrix_20260605`
- Queue jobs: 371
- Reboot recovery: installed through user crontab
- First production job: original SimVLA, exact first 100 identities, horizon 10
