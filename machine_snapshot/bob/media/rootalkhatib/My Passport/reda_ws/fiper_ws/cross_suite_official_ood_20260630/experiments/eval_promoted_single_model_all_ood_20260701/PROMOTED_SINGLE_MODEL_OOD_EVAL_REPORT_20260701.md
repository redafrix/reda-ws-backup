# Promoted Single-Checkpoint Cross-Suite OOD Evaluation

Promoted model: `simvla_h10_topk8_official_goal_object_seen_main_20260701`
Selection rule: highest source validation AUPRC among the six repeated same-source trainings; no OOD performance used for selection

## Best Per Dataset Among Seen-Calibrated Thresholds

| Dataset | Threshold | Value | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| goal_swap_100 | q99_success | 0.9976 | 0.00% | 49.48% | n/a | 9.28% | 29.90% | 0.489 |
| goal_task_100 | best_val_f1 | 0.3560 | 0.00% | 93.33% | n/a | 54.44% | 87.78% | 0.210 |
| goal_object_ood_180 | q95_success | 0.9054 | 20.14% | 92.68% | n/a | 26.83% | 73.17% | 0.334 |
| spatial_object_100 | q95_success | 0.9054 | 60.22% | 100.00% | n/a | 100.00% | 100.00% | 0.079 |
| object_object_100 | q95_success | 0.9054 | 34.92% | 81.08% | n/a | 75.68% | 81.08% | 0.030 |
| libero10_object_100 | q99_success | 0.9976 | 13.04% | 22.08% | n/a | 0.00% | 6.49% | 0.641 |

## Full Threshold Table

| Dataset | Threshold | Value | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| goal_swap_100 | best_val_f1 | 0.3560 | 100.00% | 100.00% | n/a | 93.81% | 100.00% | 0.106 |
| goal_swap_100 | fixed_0.5 | 0.5000 | 100.00% | 100.00% | n/a | 91.75% | 100.00% | 0.123 |
| goal_swap_100 | q90_success | 0.6905 | 100.00% | 100.00% | n/a | 85.57% | 100.00% | 0.149 |
| goal_swap_100 | q95_success | 0.9054 | 66.67% | 98.97% | n/a | 71.13% | 94.85% | 0.210 |
| goal_swap_100 | q99_success | 0.9976 | 0.00% | 49.48% | n/a | 9.28% | 29.90% | 0.489 |
| goal_task_100 | best_val_f1 | 0.3560 | 0.00% | 93.33% | n/a | 54.44% | 87.78% | 0.210 |
| goal_task_100 | fixed_0.5 | 0.5000 | 0.00% | 93.33% | n/a | 32.22% | 86.67% | 0.284 |
| goal_task_100 | q90_success | 0.6905 | 0.00% | 93.33% | n/a | 18.89% | 81.11% | 0.344 |
| goal_task_100 | q95_success | 0.9054 | 0.00% | 91.11% | n/a | 6.67% | 57.78% | 0.452 |
| goal_task_100 | q99_success | 0.9976 | 0.00% | 45.56% | n/a | 0.00% | 20.00% | 0.567 |
| goal_object_ood_180 | best_val_f1 | 0.3560 | 69.78% | 100.00% | n/a | 73.17% | 92.68% | 0.177 |
| goal_object_ood_180 | fixed_0.5 | 0.5000 | 61.15% | 100.00% | n/a | 73.17% | 92.68% | 0.195 |
| goal_object_ood_180 | q90_success | 0.6905 | 47.48% | 97.56% | n/a | 53.66% | 87.80% | 0.245 |
| goal_object_ood_180 | q95_success | 0.9054 | 20.14% | 92.68% | n/a | 26.83% | 73.17% | 0.334 |
| goal_object_ood_180 | q99_success | 0.9976 | 2.88% | 58.54% | n/a | 14.63% | 46.34% | 0.376 |
| spatial_object_100 | best_val_f1 | 0.3560 | 100.00% | 100.00% | n/a | 100.00% | 100.00% | 0.024 |
| spatial_object_100 | fixed_0.5 | 0.5000 | 96.77% | 100.00% | n/a | 100.00% | 100.00% | 0.030 |
| spatial_object_100 | q90_success | 0.6905 | 80.65% | 100.00% | n/a | 100.00% | 100.00% | 0.047 |
| spatial_object_100 | q95_success | 0.9054 | 60.22% | 100.00% | n/a | 100.00% | 100.00% | 0.079 |
| spatial_object_100 | q99_success | 0.9976 | 5.38% | 42.86% | n/a | 14.29% | 28.57% | 0.483 |
| object_object_100 | best_val_f1 | 0.3560 | 100.00% | 100.00% | n/a | 100.00% | 100.00% | 0.004 |
| object_object_100 | fixed_0.5 | 0.5000 | 100.00% | 100.00% | n/a | 100.00% | 100.00% | 0.014 |
| object_object_100 | q90_success | 0.6905 | 73.02% | 94.59% | n/a | 94.59% | 94.59% | 0.021 |
| object_object_100 | q95_success | 0.9054 | 34.92% | 81.08% | n/a | 75.68% | 81.08% | 0.030 |
| object_object_100 | q99_success | 0.9976 | 0.00% | 0.00% | n/a | 0.00% | 0.00% | n/a |
| libero10_object_100 | best_val_f1 | 0.3560 | 100.00% | 100.00% | n/a | 100.00% | 100.00% | 0.004 |
| libero10_object_100 | fixed_0.5 | 0.5000 | 100.00% | 100.00% | n/a | 100.00% | 100.00% | 0.009 |
| libero10_object_100 | q90_success | 0.6905 | 100.00% | 100.00% | n/a | 96.10% | 100.00% | 0.056 |
| libero10_object_100 | q95_success | 0.9054 | 95.65% | 90.91% | n/a | 67.53% | 90.91% | 0.130 |
| libero10_object_100 | q99_success | 0.9976 | 13.04% | 22.08% | n/a | 0.00% | 6.49% | 0.641 |

## Legitimacy Notes

- This evaluation uses one promoted checkpoint for every OOD dataset.
- The checkpoint was selected by source validation AUPRC only.
- Threshold values are carried from the promoted model's source validation calibration.
- The per-dataset best row is diagnostic only because it chooses among seen-calibrated threshold rules after seeing OOD outcomes.
