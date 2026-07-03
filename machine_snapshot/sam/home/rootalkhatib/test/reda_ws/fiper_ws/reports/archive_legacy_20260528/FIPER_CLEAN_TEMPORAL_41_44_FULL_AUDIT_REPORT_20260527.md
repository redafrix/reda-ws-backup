# FIPER Clean Temporal 41/44 Full Audit Report

## Executive Summary

- Completed campaigns found: `9`
- Completed job directories found: `45`
- Policy rows summarized: `270`
- Feature audit failures: `0`

This report is generated strictly from completed `summary.json`, `metrics.json`, `training_history.json`, and `FEATURE_AUDIT.json` artifacts. It excludes smoke and invalid row-leakage runs.

## Completed Campaigns

- `ood_perturbation_milk`: 5 jobs
- `ood_perturbation_mug`: 5 jobs
- `ood_perturbation_object`: 5 jobs
- `ood_task_8_9`: 5 jobs
- `target_object_fold00`: 5 jobs
- `target_object_fold01`: 5 jobs
- `target_object_fold02`: 5 jobs
- `target_object_fold03`: 5 jobs
- `target_object_fold04`: 5 jobs

## Feature Audit

All completed jobs report no object-position oracle, no reward, no success flag, no task metadata, and no OOD rows for training.

## Top Balanced Policies

| Rank | Campaign | Job | Policy | Score | Seen Succ FA | OOD Succ FA | OOD Fail Det | OOD Det@25 | OOD Mean Time | OOD Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 2.2875 | 13.27% | 7.88% | 96.80% | 76.80% | 0.1634 | 3.20% |
| 2 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 2.2827 | 14.60% | 8.82% | 96.80% | 77.60% | 0.1594 | 3.20% |
| 3 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 2.2378 | 11.06% | 6.59% | 95.20% | 74.40% | 0.1778 | 4.80% |
| 4 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 2.2259 | 12.17% | 7.02% | 96.00% | 73.60% | 0.1710 | 4.00% |
| 5 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 2.1982 | 12.83% | 6.51% | 94.40% | 73.60% | 0.1696 | 5.60% |
| 6 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `score_q99_K3` | 2.1801 | 7.58% | 43.24% | 100.00% | 93.33% | 0.1914 | 0.00% |
| 7 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `or_q99_K3` | 2.1688 | 9.85% | 43.24% | 100.00% | 93.33% | 0.1914 | 0.00% |
| 8 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 2.1613 | 12.39% | 8.05% | 98.40% | 68.80% | 0.1861 | 1.60% |
| 9 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 2.1551 | 12.61% | 8.39% | 94.40% | 72.80% | 0.1747 | 5.60% |
| 10 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `score_q99_K3` | 2.1489 | 4.55% | 41.89% | 100.00% | 90.00% | 0.2101 | 0.00% |
| 11 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 2.1412 | 11.06% | 5.57% | 93.60% | 70.40% | 0.1763 | 6.40% |
| 12 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 2.1300 | 8.33% | 41.89% | 100.00% | 90.00% | 0.2088 | 0.00% |
| 13 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 2.0978 | 11.28% | 6.25% | 96.00% | 66.40% | 0.1964 | 4.00% |
| 14 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 2.0896 | 10.62% | 7.02% | 92.80% | 69.60% | 0.1795 | 7.20% |
| 15 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `or_q95_K3` | 2.0023 | 36.50% | 22.35% | 97.60% | 78.40% | 0.1566 | 2.40% |
| 16 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `or_q95_K3` | 1.9762 | 37.61% | 23.72% | 97.60% | 78.40% | 0.1539 | 2.40% |
| 17 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 1.9689 | 14.35% | 17.67% | 97.93% | 67.36% | 0.2270 | 2.07% |
| 18 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `or_q95_K3` | 1.9438 | 36.06% | 21.06% | 97.60% | 74.40% | 0.1630 | 2.40% |
| 19 | `ood_perturbation_mug` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.9401 | 11.85% | 16.97% | 98.45% | 64.25% | 0.2264 | 1.55% |
| 20 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `or_q95_K3` | 1.9378 | 35.84% | 22.60% | 97.60% | 75.20% | 0.1669 | 2.40% |
| 21 | `ood_perturbation_mug` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 1.9349 | 14.97% | 16.97% | 98.45% | 64.77% | 0.2397 | 1.55% |
| 22 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 1.9145 | 14.76% | 19.78% | 97.93% | 66.32% | 0.2205 | 2.07% |
| 23 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 1.8919 | 11.43% | 16.87% | 97.93% | 62.18% | 0.2457 | 2.07% |
| 24 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.8771 | 11.23% | 15.16% | 97.41% | 60.62% | 0.2534 | 2.59% |
| 25 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `or_q95_K3` | 1.8708 | 35.40% | 22.95% | 98.40% | 71.20% | 0.1692 | 1.60% |

## Low False-Alarm Candidates

| Rank | Campaign | Job | Policy | Seen Succ FA | OOD Succ FA | OOD Fail Det | OOD Det@25 | OOD Mean Time |
|---:|---|---|---|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `or_q95_K3` | 36.50% | 22.35% | 97.60% | 78.40% | 0.1566 |
| 2 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `or_q95_K3` | 37.61% | 23.72% | 97.60% | 78.40% | 0.1539 |
| 3 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 14.60% | 8.82% | 96.80% | 77.60% | 0.1594 |
| 4 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 13.27% | 7.88% | 96.80% | 76.80% | 0.1634 |
| 5 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `or_q95_K3` | 35.84% | 22.60% | 97.60% | 75.20% | 0.1669 |
| 6 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 11.06% | 6.59% | 95.20% | 74.40% | 0.1778 |
| 7 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `or_q95_K3` | 36.06% | 21.06% | 97.60% | 74.40% | 0.1630 |
| 8 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 12.83% | 6.51% | 94.40% | 73.60% | 0.1696 |
| 9 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 12.17% | 7.02% | 96.00% | 73.60% | 0.1710 |
| 10 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 12.61% | 8.39% | 94.40% | 72.80% | 0.1747 |
| 11 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `or_q95_K3` | 35.40% | 22.95% | 98.40% | 71.20% | 0.1692 |
| 12 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 11.06% | 5.57% | 93.60% | 70.40% | 0.1763 |
| 13 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 10.62% | 7.02% | 92.80% | 69.60% | 0.1795 |
| 14 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 12.39% | 8.05% | 98.40% | 68.80% | 0.1861 |
| 15 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 14.35% | 17.67% | 97.93% | 67.36% | 0.2270 |
| 16 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 11.28% | 6.25% | 96.00% | 66.40% | 0.1964 |
| 17 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 14.76% | 19.78% | 97.93% | 66.32% | 0.2205 |
| 18 | `ood_task_8_9` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 12.78% | 28.24% | 94.44% | 65.28% | 0.2496 |
| 19 | `ood_perturbation_mug` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 14.97% | 16.97% | 98.45% | 64.77% | 0.2397 |
| 20 | `ood_perturbation_mug` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 11.85% | 16.97% | 98.45% | 64.25% | 0.2264 |
| 21 | `ood_task_8_9` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 12.37% | 27.69% | 93.06% | 63.89% | 0.2657 |
| 22 | `ood_task_8_9` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 15.21% | 28.57% | 94.44% | 63.89% | 0.2638 |
| 23 | `ood_task_8_9` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 15.62% | 28.57% | 93.06% | 62.50% | 0.2834 |
| 24 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 11.43% | 16.87% | 97.93% | 62.18% | 0.2457 |
| 25 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 12.25% | 29.62% | 94.81% | 61.04% | 0.1849 |

## Final Fields

```text
CLEAN_TEMPORAL_COMPLETED_CAMPAIGNS = 9
CLEAN_TEMPORAL_COMPLETED_JOBS = 45
CLEAN_FEATURE_AUDIT_FAILURES = 0
CSV_RESULTS = reports/FIPER_CLEAN_TEMPORAL_41_44_FULL_AUDIT_RESULTS_20260527.csv
```
