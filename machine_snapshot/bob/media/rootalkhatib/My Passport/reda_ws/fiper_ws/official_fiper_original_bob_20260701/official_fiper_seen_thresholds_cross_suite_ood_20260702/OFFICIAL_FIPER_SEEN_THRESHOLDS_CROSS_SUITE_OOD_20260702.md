# Official FIPER Seen-Calibrated Cross-Suite OOD Evaluation

## Protocol

- Calibration data: official seen `libero_goal_object` success rollouts only.
- Test data: each OOD dataset is test-only; no OOD calibration and no OOD threshold tuning.
- RND checkpoints: reused the official FIPER RND-OE checkpoints trained on seen calibration for seeds 0, 1, 2, 42, 43.
- Method code: official FIPER `EvaluationManager` and method classes are used; this script is only a dataset/materialization adapter.
- Reported rows: the exact q95 operating points selected from the seen held-out FIPER table.

## Dataset Validation

| Dataset | Episodes | Success | Failure | Rows |
|---|---:|---:|---:|---:|
| `goal_object_ood_180` | 330 | 139 | 41 | 50323 |
| `goal_swap_100` | 250 | 3 | 97 | 50906 |
| `goal_task_100` | 250 | 10 | 90 | 48659 |
| `spatial_object_100` | 250 | 93 | 7 | 33473 |
| `object_object_100` | 250 | 63 | 37 | 41446 |
| `libero10_object_100` | 250 | 23 | 77 | 50468 |

## `goal_object_ood_180`

| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `entropy` | `ct_quantile` | `15` | 5.0% | 51.2% | 0.0% | 0.0% | 29.3% | 0.526 | 48.8% |
| `entropy` | `tvt_cp_band` | `50` | 0.0% | 48.8% | 0.0% | 0.0% | 0.0% | 0.801 | 51.2% |
| `entropy` | `tvt_quantile` | `50` | 18.0% | 70.7% | 9.8% | 24.4% | 48.8% | 0.367 | 29.3% |
| `rnd_oe` | `ct_quantile` | `3` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_cp_band` | `11` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_quantile` | `1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe_and_entropy` | `ct_quantile` | `1` | 0.0% | 26.8% | 0.0% | 0.0% | 9.8% | 0.597 | 73.2% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | `11/50` | 0.0% | 48.8% | 0.0% | 0.0% | 0.0% | 0.801 | 51.2% |
| `rnd_oe_and_entropy` | `tvt_quantile` | `1/50` | 18.0% | 70.7% | 9.8% | 24.4% | 48.8% | 0.367 | 29.3% |

## `goal_swap_100`

| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `entropy` | `ct_quantile` | `15` | 0.0% | 67.0% | 0.0% | 9.3% | 29.9% | 0.546 | 33.0% |
| `entropy` | `tvt_cp_band` | `50` | 0.0% | 63.9% | 0.0% | 0.0% | 0.0% | 0.807 | 36.1% |
| `entropy` | `tvt_quantile` | `50` | 0.0% | 73.2% | 30.9% | 43.3% | 61.9% | 0.244 | 26.8% |
| `rnd_oe` | `ct_quantile` | `3` | 0.0% | 6.4% | 4.3% | 4.3% | 4.3% | 0.326 | 93.6% |
| `rnd_oe` | `tvt_cp_band` | `11` | 0.0% | 36.7% | 2.1% | 8.5% | 20.6% | 0.406 | 63.3% |
| `rnd_oe` | `tvt_quantile` | `1` | 0.0% | 34.8% | 8.5% | 12.6% | 33.0% | 0.269 | 65.2% |
| `rnd_oe_and_entropy` | `ct_quantile` | `1` | 0.0% | 1.9% | 0.0% | 0.0% | 0.4% | 0.666 | 98.1% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | `11/50` | 0.0% | 19.8% | 0.0% | 0.0% | 0.0% | 0.784 | 80.2% |
| `rnd_oe_and_entropy` | `tvt_quantile` | `1/50` | 0.0% | 21.4% | 2.1% | 2.5% | 15.3% | 0.446 | 78.6% |

## `goal_task_100`

| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `entropy` | `ct_quantile` | `15` | 0.0% | 42.2% | 0.0% | 1.1% | 4.4% | 0.722 | 57.8% |
| `entropy` | `tvt_cp_band` | `50` | 0.0% | 26.7% | 0.0% | 0.0% | 0.0% | 0.846 | 73.3% |
| `entropy` | `tvt_quantile` | `50` | 70.0% | 22.2% | 8.9% | 8.9% | 12.2% | 0.359 | 77.8% |
| `rnd_oe` | `ct_quantile` | `3` | 2.0% | 6.7% | 4.4% | 4.4% | 4.4% | 0.326 | 93.3% |
| `rnd_oe` | `tvt_cp_band` | `11` | 0.0% | 31.1% | 2.2% | 6.7% | 15.6% | 0.457 | 68.9% |
| `rnd_oe` | `tvt_quantile` | `1` | 22.0% | 28.9% | 6.7% | 8.9% | 26.7% | 0.288 | 71.1% |
| `rnd_oe_and_entropy` | `ct_quantile` | `1` | 0.0% | 0.4% | 0.0% | 0.0% | 0.0% | 0.677 | 99.6% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | `11/50` | 0.0% | 6.7% | 0.0% | 0.0% | 0.0% | 0.831 | 93.3% |
| `rnd_oe_and_entropy` | `tvt_quantile` | `1/50` | 14.0% | 4.7% | 0.0% | 0.0% | 0.4% | 0.580 | 95.3% |

## `spatial_object_100`

| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `entropy` | `ct_quantile` | `15` | 2.2% | 85.7% | 0.0% | 0.0% | 71.4% | 0.456 | 14.3% |
| `entropy` | `tvt_cp_band` | `50` | 0.0% | 85.7% | 0.0% | 0.0% | 0.0% | 0.756 | 14.3% |
| `entropy` | `tvt_quantile` | `50` | 21.5% | 100.0% | 0.0% | 57.1% | 100.0% | 0.309 | 0.0% |
| `rnd_oe` | `ct_quantile` | `3` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_cp_band` | `11` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_quantile` | `1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe_and_entropy` | `ct_quantile` | `1` | 0.0% | 42.9% | 0.0% | 0.0% | 14.3% | 0.578 | 57.1% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | `11/50` | 0.0% | 85.7% | 0.0% | 0.0% | 0.0% | 0.756 | 14.3% |
| `rnd_oe_and_entropy` | `tvt_quantile` | `1/50` | 21.5% | 100.0% | 0.0% | 57.1% | 100.0% | 0.309 | 0.0% |

## `object_object_100`

| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `entropy` | `ct_quantile` | `15` | 1.6% | 5.4% | 0.0% | 0.0% | 0.0% | 0.680 | 94.6% |
| `entropy` | `tvt_cp_band` | `50` | 0.0% | 8.1% | 0.0% | 0.0% | 0.0% | 0.847 | 91.9% |
| `entropy` | `tvt_quantile` | `50` | 3.2% | 8.1% | 0.0% | 5.4% | 5.4% | 0.437 | 91.9% |
| `rnd_oe` | `ct_quantile` | `3` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_cp_band` | `11` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_quantile` | `1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe_and_entropy` | `ct_quantile` | `1` | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | N/A | 100.0% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | `11/50` | 0.0% | 8.1% | 0.0% | 0.0% | 0.0% | 0.847 | 91.9% |
| `rnd_oe_and_entropy` | `tvt_quantile` | `1/50` | 3.2% | 8.1% | 0.0% | 5.4% | 5.4% | 0.437 | 91.9% |

## `libero10_object_100`

| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `entropy` | `ct_quantile` | `15` | 0.0% | 9.1% | 0.0% | 0.0% | 1.3% | 0.767 | 90.9% |
| `entropy` | `tvt_cp_band` | `50` | 0.0% | 7.8% | 0.0% | 0.0% | 0.0% | 0.903 | 92.2% |
| `entropy` | `tvt_quantile` | `50` | 0.0% | 10.4% | 0.0% | 3.9% | 7.8% | 0.407 | 89.6% |
| `rnd_oe` | `ct_quantile` | `3` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_cp_band` | `11` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe` | `tvt_quantile` | `1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% |
| `rnd_oe_and_entropy` | `ct_quantile` | `1` | 0.0% | 2.6% | 0.0% | 0.0% | 0.0% | 0.807 | 97.4% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | `11/50` | 0.0% | 7.8% | 0.0% | 0.0% | 0.0% | 0.903 | 92.2% |
| `rnd_oe_and_entropy` | `tvt_quantile` | `1/50` | 0.0% | 10.4% | 0.0% | 3.9% | 7.8% | 0.407 | 89.6% |

## Output Files

- Aggregate CSV: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv`
- Per-seed CSV: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/official_fiper_seen_thresholds_cross_suite_ood_per_seed.csv`

## Flags

- `NO_OOD_CALIBRATION = YES`
- `NO_OOD_THRESHOLD_TUNING = YES`
- `SEEN_CALIBRATION_ONLY = YES`
- `RND_CHECKPOINTS_REUSED = YES`
- `OFFICIAL_FIPER_METHOD_CLASSES_USED = YES`
- `RUN_COMPLETE = YES`
