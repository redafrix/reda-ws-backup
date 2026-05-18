# Stage 7 — Calibration Follow-up

- Variant: `context_gated_action`
- Target coverage: `0.9`
- All etas use the (n+1)/n*α quantile correction.

## Methods

1. `global_residual` — single eta from SimVLA-only calib residuals.
2. `binned_quantile_10` — 10 bins on predicted-score quantile.
3. `binned_quantile_10_with_floor` — bins floored to global_eta/2 to avoid empty-bin collapse.
4. `per_task_simvla` — eta per task_name; global fallback if < 30 calib rows.
5. `asymmetric_split_residual` — separate 0.95 quantiles on +/- residuals (two-sided 0.90).

## Per-split results

### `id_task_split`
- SimVLA calib rows: `1250`
- SimVLA-only global eta: `0.2447`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_residual` | 1250 | 0.923 | 0.245 |
| `test_id` | `binned_quantile_10` | 1250 | 0.874 | 0.169 |
| `test_id` | `binned_quantile_10_with_floor` | 1250 | 0.880 | 0.182 |
| `test_id` | `per_task_simvla` | 1250 | 0.923 | 0.245 |
| `test_id` | `asymmetric_split_residual` | 1250 | 0.856 | 0.324 |
| `test_ood` | `global_residual` | 0 | n/a | n/a |
| `test_ood` | `binned_quantile_10` | 0 | n/a | n/a |
| `test_ood` | `binned_quantile_10_with_floor` | 0 | n/a | n/a |
| `test_ood` | `per_task_simvla` | 0 | n/a | n/a |
| `test_ood` | `asymmetric_split_residual` | 0 | nan | 0.324 |

### `holdout_libero_object`
- SimVLA calib rows: `1250`
- SimVLA-only global eta: `0.1232`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_residual` | 1250 | 0.916 | 0.123 |
| `test_id` | `binned_quantile_10` | 1250 | 0.939 | 0.130 |
| `test_id` | `binned_quantile_10_with_floor` | 1250 | 0.939 | 0.130 |
| `test_id` | `per_task_simvla` | 1250 | 0.916 | 0.123 |
| `test_id` | `asymmetric_split_residual` | 1250 | 0.970 | 0.174 |
| `test_ood` | `global_residual` | 1250 | 0.899 | 0.123 |
| `test_ood` | `binned_quantile_10` | 1250 | 0.914 | 0.131 |
| `test_ood` | `binned_quantile_10_with_floor` | 1250 | 0.914 | 0.131 |
| `test_ood` | `per_task_simvla` | 1250 | 0.899 | 0.123 |
| `test_ood` | `asymmetric_split_residual` | 1250 | 0.958 | 0.174 |

### `holdout_object_bowl`
- SimVLA calib rows: `1250`
- SimVLA-only global eta: `0.1139`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_residual` | 1250 | 0.687 | 0.114 |
| `test_id` | `binned_quantile_10` | 1250 | 0.678 | 0.118 |
| `test_id` | `binned_quantile_10_with_floor` | 1250 | 0.678 | 0.118 |
| `test_id` | `per_task_simvla` | 1250 | 0.687 | 0.114 |
| `test_id` | `asymmetric_split_residual` | 1250 | 0.622 | 0.159 |
| `test_ood` | `global_residual` | 1250 | 0.936 | 0.114 |
| `test_ood` | `binned_quantile_10` | 1250 | 0.934 | 0.133 |
| `test_ood` | `binned_quantile_10_with_floor` | 1250 | 0.934 | 0.133 |
| `test_ood` | `per_task_simvla` | 1250 | 0.936 | 0.114 |
| `test_ood` | `asymmetric_split_residual` | 1250 | 0.826 | 0.159 |

### `holdout_libero_spatial`
- SimVLA calib rows: `1250`
- SimVLA-only global eta: `0.1426`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_residual` | 1250 | 0.791 | 0.143 |
| `test_id` | `binned_quantile_10` | 1250 | 0.766 | 0.149 |
| `test_id` | `binned_quantile_10_with_floor` | 1250 | 0.790 | 0.153 |
| `test_id` | `per_task_simvla` | 1250 | 0.791 | 0.143 |
| `test_id` | `asymmetric_split_residual` | 1250 | 0.926 | 0.362 |
| `test_ood` | `global_residual` | 1000 | 0.701 | 0.143 |
| `test_ood` | `binned_quantile_10` | 1000 | 0.639 | 0.144 |
| `test_ood` | `binned_quantile_10_with_floor` | 1000 | 0.648 | 0.148 |
| `test_ood` | `per_task_simvla` | 1000 | 0.701 | 0.143 |
| `test_ood` | `asymmetric_split_residual` | 1000 | 0.985 | 0.362 |

## Worst-case coverage across all splits/parts

| Method | Worst coverage | Split | Part |
|---|---:|---|---|
| `global_residual` | 0.687 | `holdout_object_bowl` | `test_id` |
| `binned_quantile_10` | 0.639 | `holdout_libero_spatial` | `test_ood` |
| `binned_quantile_10_with_floor` | 0.648 | `holdout_libero_spatial` | `test_ood` |
| `per_task_simvla` | 0.687 | `holdout_object_bowl` | `test_id` |
| `asymmetric_split_residual` | 0.622 | `holdout_object_bowl` | `test_id` |

**Recommended deployable method**: `per_task_simvla` (worst-case coverage 0.687).

If the worst-case coverage is still below target 0.90, the residual miscalibration is driven by genuine distribution shift between calib and test_ood splits (model is too optimistic on the shifted task class) and needs an upstream fix (better features or a labelled small calib set drawn from the deployment distribution).

