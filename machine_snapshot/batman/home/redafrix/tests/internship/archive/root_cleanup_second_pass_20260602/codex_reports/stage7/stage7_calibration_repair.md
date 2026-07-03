# Stage 7 Calibration Repair

- Variant: `context_gated_action`
- Target coverage: `0.90`
- Candidate-type conditional calibration is not used as the main deployable method.

## `id_task_split`

- Calib rows: `2500`; SimVLA calib rows: `1250`
- Global eta: `0.19605934228748081`
- SimVLA-only eta: `0.23749759197235218`
- Analysis-only train+calib eta: `0.03771773576736451`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_all_candidates` | 2500 | 0.934 | 0.196 |
| `test_id` | `global_simvla_only_eval` | 1250 | 0.900 | 0.196 |
| `test_id` | `simvla_only_eta_simvla_eval` | 1250 | 0.919 | 0.237 |
| `test_id` | `analysis_train_plus_calib_eta_simvla_eval` | 1250 | 0.666 | 0.038 |
| `test_id` | `binned_simvla_quantile_eta_simvla_eval` | 1157 | 0.889 | 0.161 |

## `holdout_libero_object`

- Calib rows: `2500`; SimVLA calib rows: `1250`
- Global eta: `0.09932879209518432`
- SimVLA-only eta: `0.12267944812774667`
- Analysis-only train+calib eta: `0.023020982742309577`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_all_candidates` | 2500 | 0.899 | 0.099 |
| `test_id` | `global_simvla_only_eval` | 1250 | 0.880 | 0.099 |
| `test_id` | `simvla_only_eta_simvla_eval` | 1250 | 0.915 | 0.123 |
| `test_id` | `analysis_train_plus_calib_eta_simvla_eval` | 1250 | 0.769 | 0.023 |
| `test_id` | `binned_simvla_quantile_eta_simvla_eval` | 1250 | 0.922 | 0.121 |
| `test_ood` | `global_all_candidates` | 2500 | 0.884 | 0.099 |
| `test_ood` | `global_simvla_only_eval` | 1250 | 0.854 | 0.099 |
| `test_ood` | `simvla_only_eta_simvla_eval` | 1250 | 0.899 | 0.123 |
| `test_ood` | `analysis_train_plus_calib_eta_simvla_eval` | 1250 | 0.498 | 0.023 |
| `test_ood` | `binned_simvla_quantile_eta_simvla_eval` | 1250 | 0.919 | 0.124 |

## `holdout_object_bowl`

- Calib rows: `2500`; SimVLA calib rows: `1250`
- Global eta: `0.1138805866241455`
- SimVLA-only eta: `0.1138634204864502`
- Analysis-only train+calib eta: `0.05553224682807923`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_all_candidates` | 2500 | 0.785 | 0.114 |
| `test_id` | `global_simvla_only_eval` | 1250 | 0.687 | 0.114 |
| `test_id` | `simvla_only_eta_simvla_eval` | 1250 | 0.687 | 0.114 |
| `test_id` | `analysis_train_plus_calib_eta_simvla_eval` | 1250 | 0.614 | 0.056 |
| `test_id` | `binned_simvla_quantile_eta_simvla_eval` | 1199 | 0.687 | 0.105 |
| `test_ood` | `global_all_candidates` | 2500 | 0.899 | 0.114 |
| `test_ood` | `global_simvla_only_eval` | 1250 | 0.936 | 0.114 |
| `test_ood` | `simvla_only_eta_simvla_eval` | 1250 | 0.936 | 0.114 |
| `test_ood` | `analysis_train_plus_calib_eta_simvla_eval` | 1250 | 0.819 | 0.056 |
| `test_ood` | `binned_simvla_quantile_eta_simvla_eval` | 1053 | 0.930 | 0.108 |

Holdout-object-bowl note: undercoverage remains visible when calibration uses only the designated calibration contexts. The analysis-only train+calib pool indicates whether the issue is calibration-set size/composition, but it is not a deployable claim unless such an additional labeled calibration pool is allowed.


## `holdout_libero_spatial`

- Calib rows: `2500`; SimVLA calib rows: `1250`
- Global eta: `0.11128985881805414`
- SimVLA-only eta: `0.14222283363342292`
- Analysis-only train+calib eta: `0.041628277301788336`

| Part | Method | N | Coverage | Mean width |
|---|---|---:|---:|---:|
| `test_id` | `global_all_candidates` | 2500 | 0.844 | 0.111 |
| `test_id` | `global_simvla_only_eval` | 1250 | 0.763 | 0.111 |
| `test_id` | `simvla_only_eta_simvla_eval` | 1250 | 0.791 | 0.142 |
| `test_id` | `analysis_train_plus_calib_eta_simvla_eval` | 1250 | 0.519 | 0.042 |
| `test_id` | `binned_simvla_quantile_eta_simvla_eval` | 1241 | 0.814 | 0.177 |
| `test_ood` | `global_all_candidates` | 2000 | 0.755 | 0.111 |
| `test_ood` | `global_simvla_only_eval` | 1000 | 0.611 | 0.111 |
| `test_ood` | `simvla_only_eta_simvla_eval` | 1000 | 0.699 | 0.142 |
| `test_ood` | `analysis_train_plus_calib_eta_simvla_eval` | 1000 | 0.326 | 0.042 |
| `test_ood` | `binned_simvla_quantile_eta_simvla_eval` | 1000 | 0.661 | 0.184 |

## Worst Case

- Worst observed coverage: `0.326` for split `holdout_libero_spatial`, part `test_ood`, method `analysis_train_plus_calib_eta_simvla_eval`.

