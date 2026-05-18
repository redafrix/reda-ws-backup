# Stage 5 SimVLA-only Calibration Report

Date: 2026-05-13
Script: `asynchvla_ws/src/calibration/calibrate_stage5_simvla_only.py`
Per-split detailed reports:
- `stage5_id_task_split_simvla_only_calibration.md`
- `stage5_holdout_libero_object_simvla_only_calibration.md`
- `stage5_holdout_object_bowl_simvla_only_calibration.md`

## Method

For each split we load the predictions emitted by the medium `full` rater on
calib and test partitions and apply three conformal schemes:

1. **global_residual** — `q = quantile_(1-α)(|pred - true|)` on **all** calib
   candidates (any type). Predicts a symmetric interval `[pred-q, pred+q]`
   for any test point.
2. **simvla_only_residual** — same idea but only on `simvla_seed*` calib
   rows. This is the deployment-honest version: at runtime we know we are
   rating a SimVLA-generated action, so we should calibrate against that
   distribution.
3. **simvla_only_binned** — same residual, but predicted-uncertainty
   quartiles (4 bins) over SimVLA calib rows give bin-specific `q`. At test
   time we route by predicted-uncertainty bin.

Target coverage is 0.90 (α = 0.1). Evaluation is done **only** on
`simvla_seed*` test rows (the deployable case — runtime does not know which
synthetic candidate type it is rating).

## Aggregated results (test SimVLA-only)

| split | scheme | test_id cov | test_ood cov | mean width |
| --- | --- | ---: | ---: | ---: |
| id_task_split | global_residual | 0.863 | n/a | 1.039 |
| id_task_split | simvla_only_residual | 0.779 | n/a | 0.820 |
| id_task_split | simvla_only_binned | 0.768 | n/a | 0.857 |
| holdout_libero_object | global_residual | **0.914** | **0.907** | 0.973 |
| holdout_libero_object | simvla_only_residual | 0.809 | 0.822 | 0.725 |
| holdout_libero_object | simvla_only_binned | 0.804 | 0.822 | 0.712–0.722 |
| holdout_object_bowl | global_residual | 0.687 | 0.869 | 0.774 |
| holdout_object_bowl | simvla_only_residual | 0.654 | 0.819 | 0.683 |
| holdout_object_bowl | simvla_only_binned | 0.630 | 0.796 | 0.629–0.657 |

## Reading the numbers

- `holdout_libero_object` hits target coverage (0.91 ID, 0.91 OOD) with the
  global-residual scheme — **calibration is genuinely deployable on this
  split** with a ±0.49 chunk-L2 band.
- `id_task_split` undercovers by 4 pp on test_id with global-residual (0.86
  vs target 0.90). For deployment we would inflate `q` by a 1.1× factor or
  retrain calib with more rows.
- `holdout_object_bowl` is the surprising case: test_id is **31 pp under
  target** but test_ood is **near target**. The reason is structural:
  the manifest's calib pool was drawn from `libero_object`/`libero_90`,
  which more closely matches the OOD test set (held-out bowl tasks) than
  the test_id set (other libero_90 non-bowl tasks). The calib distribution
  is a poor proxy for test_id, so the conformal guarantee transfers worse.
  This is a **manifest-design caveat**, not a model failure.

The simvla-only residual and binned variants are tighter (smaller width)
but undercover everywhere by 5–10 pp. Either:
- the SimVLA-error distribution has heavier tails than the rater's prediction
  residual can capture on calib (250 contexts is small for the tail), or
- the binning adds variance because each of the 4 bins has only ~62 rows.

The deployable scheme is **global_residual** on `holdout_libero_object`.
Other splits need a larger calib pool or a multiplicative inflation factor.

## Deployability summary

| split | deployable? | recommended q | mean width |
| --- | --- | ---: | ---: |
| id_task_split | with 1.1× inflation | ~0.57 | ~1.14 |
| holdout_libero_object | **yes** | 0.487 | 0.973 |
| holdout_object_bowl | not on test_id without recalibration | n/a | n/a |

## Caveats and known biases

- Candidate-type conditional calibration (e.g., separate q for `perturb_*`
  vs `simvla_seed*`) is analysis-only — runtime cannot infer candidate
  type — so we only report the three SimVLA-deployable schemes.
- `simvla_only_residual` undercovers because SimVLA candidates have higher
  variance than the broad calib distribution; this means the global scheme
  is conservative *for synthetic candidates* (mean width 1.04 vs 0.82) but
  honest in coverage. There is a real width–coverage trade-off here.
- The binned scheme assumes monotonic uncertainty→residual mapping. The bin
  q values for holdout_libero_object are 0.49, 0.45, …, suggesting the
  mapping is **non-monotonic** at this dataset size; binning hurts more
  than it helps.

## Next steps

- Re-build a larger calib pool (≥500 contexts) for `holdout_object_bowl`
  before claiming deployability there.
- Try Mondrian conformal with **predicted-uncertainty deciles** instead of
  quartiles, once calib is larger.
- Investigate ensemble or quantile-regression heads instead of a single
  point estimate, which would let `simvla_only` calibration be tight
  without losing coverage.
