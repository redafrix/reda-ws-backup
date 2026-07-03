# Stage 8 Final Smoke Before 72h Launch

Generated: `2026-05-15T21:19:39`

## Smokes Run
- Sam target build smoke: passed (`stage8_sam_path_fix_and_real_smokes.md`).
- Sam target experiment smoke: passed.
- Sam tiny model train smoke: passed.
- Sam calibration smoke: passed.
- Sam flowtrace import/help smoke: passed.
- Sam flowtrace 10-context real build: passed after path remap, producing nonzero train/calib/test_id/test_ood `.pt` files.
- Bob LIBERO-PRO smoke/pilot: already completed earlier and active expanded rollout is healthy.
- Job manager smoke: already completed earlier (`smoke_bob_cpu`, `smoke_sam_cpu`, dependency, retry jobs all DONE).

## Independent Blockers
- History models still require sequential rollout logs; a truthful history job is queued to report/build only if usable logs exist.
- Some advanced calibration methods may require future code additions if absent from `run_calibration_sweep.py`; current real calibration sweep covers implemented methods and target coverages.
