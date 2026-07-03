# Dean Top-K8 Fusion Policy v1

## Method

This test does not retrain the transformer. It reuses the canonical base detector and the `unc_topk8` detector, scores the same fixed buckets, then applies post-hoc fusion policies.

Thresholds are recalibrated per policy using the same conformal protocol: q95 from `success_calib_seen`, then conformal mass from `success_val_seen`.

Policy selection is reported two ways:

- `selected_by_validation`: chosen only from seen validation metrics.
- `best_eval_diagnostic`: best test/OOD trade-off after evaluation, useful for analysis but not a deployable selection rule.

## Results

### all_tasks_full

| Policy | Selected | Eval FA | Eval Det | Det@25 | Det@50 | Mean Time | Net vs Base |
|---|---:|---:|---:|---:|---:|---:|---:|
| base_ref |  | 14.23% | 95.78% | 54.01% | 89.03% | 0.231 | 0.0000 |
| topk8_ref | validation | 15.01% | 97.47% | 64.98% | 89.45% | 0.205 | 0.0091 |
| max_base_topk8 | eval-diagnostic | 10.72% | 97.05% | 51.90% | 88.61% | 0.248 | 0.0477 |
| topk_q95_rescue |  | 10.72% | 97.05% | 51.90% | 88.61% | 0.248 | 0.0477 |
| early_max_until_50 |  | 11.70% | 97.05% | 56.12% | 90.72% | 0.234 | 0.0380 |
| base_plus_topk_excess_1p0 |  | 11.50% | 96.20% | 56.12% | 89.45% | 0.231 | 0.0315 |
| base_plus_topk_excess_1p5 |  | 11.50% | 96.20% | 56.12% | 88.61% | 0.231 | 0.0315 |
| early_max_until_25 |  | 12.28% | 96.62% | 57.38% | 89.45% | 0.229 | 0.0279 |
| early_excess50_1p0 |  | 11.89% | 96.20% | 56.96% | 89.87% | 0.221 | 0.0276 |

- Validation-selected policy: `topk8_ref`.
- Eval-diagnostic best policy: `max_base_topk8`.
- Base reference: FA 14.23%, detection 95.78%, Det@25 54.01%, Det@50 89.03%.
- Top-K8 reference: FA 15.01%, detection 97.47%, Det@25 64.98%, Det@50 89.45%.

### ood_last2_taskids_full

| Policy | Selected | Eval FA | Eval Det | Det@25 | Det@50 | Mean Time | Net vs Base |
|---|---:|---:|---:|---:|---:|---:|---:|
| base_ref |  | 25.96% | 86.02% | 39.78% | 78.49% | 0.320 | 0.0000 |
| topk8_ref | eval-diagnostic | 22.98% | 89.25% | 37.63% | 77.42% | 0.339 | 0.0620 |
| early_excess50_1p0 | validation | 25.53% | 86.02% | 45.16% | 78.49% | 0.313 | 0.0043 |
| logit_avg_75topk |  | 22.13% | 88.17% | 45.16% | 77.42% | 0.330 | 0.0598 |
| prob_avg_75topk |  | 22.55% | 88.17% | 46.24% | 77.42% | 0.331 | 0.0555 |
| prob_avg_50topk |  | 23.40% | 87.10% | 50.54% | 78.49% | 0.319 | 0.0363 |
| logit_avg_50topk |  | 22.98% | 86.02% | 46.24% | 78.49% | 0.314 | 0.0298 |
| base_plus_topk_excess_1p5 |  | 23.83% | 86.02% | 44.09% | 78.49% | 0.323 | 0.0213 |
| prob_avg_25topk |  | 22.98% | 84.95% | 49.46% | 77.42% | 0.307 | 0.0190 |

- Validation-selected policy: `early_excess50_1p0`.
- Eval-diagnostic best policy: `topk8_ref`.
- Base reference: FA 25.96%, detection 86.02%, Det@25 39.78%, Det@50 78.49%.
- Top-K8 reference: FA 22.98%, detection 89.25%, Det@25 37.63%, Det@50 77.42%.

