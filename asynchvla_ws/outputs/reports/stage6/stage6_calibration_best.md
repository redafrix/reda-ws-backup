# Stage 6 Calibration Best Variant

Best variant calibrated: `context_gated_action`. Methods: global residual conformal, SimVLA-only residual conformal, and SimVLA-only predicted-quantile binned conformal. Candidate-type conditional calibration is not used as main deployable result.

| Split | Part | Global cov/width | SimVLA cov/width | Binned cov/width |
|---|---|---:|---:|---:|
| `id_task_split` | `test_id` | 0.903/0.471 | 0.921/0.498 | 0.808/0.355 |
| `holdout_libero_object` | `test_id` | 0.969/0.530 | 0.994/0.603 | 0.838/0.364 |
| `holdout_libero_object` | `test_ood` | 0.993/0.530 | 0.994/0.603 | 0.918/0.320 |
| `holdout_object_bowl` | `test_id` | 0.681/0.360 | 0.625/0.300 | 0.558/0.275 |
| `holdout_object_bowl` | `test_ood` | 0.875/0.360 | 0.836/0.300 | 0.803/0.282 |
| `holdout_libero_spatial` | `test_id` | 0.855/0.479 | 0.889/0.570 | 0.870/0.415 |
| `holdout_libero_spatial` | `test_ood` | 0.898/0.479 | 0.963/0.570 | 0.702/0.422 |

Holdout_object_bowl Stage 5 undercoverage was caused by calibration/test composition mismatch. Stage 6 context-gated calibration is reported transparently above; if undercoverage remains, the fix is a larger or split-stratified calibration pool, not candidate-type conditional calibration.
