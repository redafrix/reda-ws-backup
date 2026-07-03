# FIPER Clean Temporal 41/44 Partial Results Audit

## Scope

Read-only analysis of completed artifacts while the full sequential Sam sweep may still be running. Smoke runs are excluded.

## Artifact Integrity

- Completed jobs: `45`
- Incomplete/failed job dirs: `5`
- Completed campaigns: `9`
- Policy rows loaded: `270`
- Feature audit failures: `0`
- Score-row mismatches: `0`
- Supervised risk jobs: `45`

Completed campaign job counts:
- `target_object_fold00`: 5 / 5 jobs
- `target_object_fold01`: 5 / 5 jobs
- `target_object_fold02`: 5 / 5 jobs
- `target_object_fold03`: 5 / 5 jobs
- `target_object_fold04`: 5 / 5 jobs
- `global_main`: 0 / 5 jobs
- `ood_task_8_9`: 5 / 5 jobs
- `ood_perturbation_mug`: 5 / 5 jobs
- `ood_perturbation_milk`: 5 / 5 jobs
- `ood_perturbation_object`: 5 / 5 jobs
- `ood_perturbation_env`: 0 / 5 jobs
- `ood_family_spatial`: 0 / 5 jobs
- `ood_family_object_family`: 0 / 5 jobs
- `ood_family_goal`: 0 / 5 jobs
- `ood_family_10_family`: 0 / 5 jobs

Interpretation guardrail: jobs marked `supervised` train on seen success plus seen failure rows. They are not success-only RND; they are legitimate only if OOD rows remain excluded from train/val/calib.

## Top Overall Completed Policies

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 2.2875 | 13.27% | 7.88% | 96.80% | 38.40% | 76.80% | 91.20% | 0.1634 | 3.20% |
| 2 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 2.2827 | 14.60% | 8.82% | 96.80% | 33.60% | 77.60% | 92.80% | 0.1594 | 3.20% |
| 3 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 2.2378 | 11.06% | 6.59% | 95.20% | 35.20% | 74.40% | 88.80% | 0.1778 | 4.80% |
| 4 | `ood_perturbation_object` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 2.2259 | 12.17% | 7.02% | 96.00% | 32.80% | 73.60% | 91.20% | 0.1710 | 4.00% |
| 5 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 2.1982 | 12.83% | 6.51% | 94.40% | 39.20% | 73.60% | 88.80% | 0.1696 | 5.60% |
| 6 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `score_q99_K3` | 2.1801 | 7.58% | 43.24% | 100.00% | 0.00% | 93.33% | 96.67% | 0.1914 | 0.00% |
| 7 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `or_q99_K3` | 2.1688 | 9.85% | 43.24% | 100.00% | 0.00% | 93.33% | 96.67% | 0.1914 | 0.00% |
| 8 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 2.1613 | 12.39% | 8.05% | 98.40% | 37.60% | 68.80% | 91.20% | 0.1861 | 1.60% |
| 9 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 2.1551 | 12.61% | 8.39% | 94.40% | 34.40% | 72.80% | 87.20% | 0.1747 | 5.60% |
| 10 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `score_q99_K3` | 2.1489 | 4.55% | 41.89% | 100.00% | 0.00% | 90.00% | 93.33% | 0.2101 | 0.00% |
| 11 | `ood_perturbation_object` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 2.1412 | 11.06% | 5.57% | 93.60% | 36.80% | 70.40% | 88.00% | 0.1763 | 6.40% |
| 12 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 2.1300 | 8.33% | 41.89% | 100.00% | 0.00% | 90.00% | 93.33% | 0.2088 | 0.00% |
| 13 | `ood_perturbation_object` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 2.0978 | 11.28% | 6.25% | 96.00% | 35.20% | 66.40% | 88.80% | 0.1964 | 4.00% |
| 14 | `ood_perturbation_object` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 2.0896 | 10.62% | 7.02% | 92.80% | 32.80% | 69.60% | 87.20% | 0.1795 | 7.20% |
| 15 | `ood_perturbation_object` | `clean_041_tcn_k8_with_current_proprio` | `or_q95_K3` | 2.0023 | 36.50% | 22.35% | 97.60% | 38.40% | 78.40% | 92.80% | 0.1566 | 2.40% |

## Top Target-Object Policies

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `score_q99_K3` | 2.1801 | 7.58% | 43.24% | 100.00% | 0.00% | 93.33% | 96.67% | 0.1914 | 0.00% |
| 2 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `or_q99_K3` | 2.1688 | 9.85% | 43.24% | 100.00% | 0.00% | 93.33% | 96.67% | 0.1914 | 0.00% |
| 3 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `score_q99_K3` | 2.1489 | 4.55% | 41.89% | 100.00% | 0.00% | 90.00% | 93.33% | 0.2101 | 0.00% |
| 4 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 2.1300 | 8.33% | 41.89% | 100.00% | 0.00% | 90.00% | 93.33% | 0.2088 | 0.00% |
| 5 | `target_object_fold02` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 1.8542 | 19.70% | 69.82% | 100.00% | 0.00% | 100.00% | 100.00% | 0.1740 | 0.00% |
| 6 | `target_object_fold02` | `clean_041_tcn_k8_no_current_proprio` | `score_q99_K3` | 1.8506 | 6.82% | 43.24% | 96.67% | 0.00% | 80.00% | 96.67% | 0.2087 | 3.33% |
| 7 | `target_object_fold02` | `clean_041_tcn_k8_no_current_proprio` | `or_q99_K3` | 1.8317 | 10.61% | 43.24% | 96.67% | 0.00% | 80.00% | 96.67% | 0.2087 | 3.33% |
| 8 | `target_object_fold02` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 1.7893 | 18.18% | 65.77% | 100.00% | 0.00% | 93.33% | 100.00% | 0.1753 | 0.00% |
| 9 | `target_object_fold02` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 1.7512 | 22.73% | 75.68% | 100.00% | 0.00% | 100.00% | 100.00% | 0.1630 | 0.00% |
| 10 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 1.7478 | 18.18% | 72.97% | 100.00% | 0.00% | 96.67% | 100.00% | 0.1567 | 0.00% |
| 11 | `target_object_fold02` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.7301 | 24.24% | 76.58% | 100.00% | 0.00% | 100.00% | 100.00% | 0.1474 | 0.00% |
| 12 | `target_object_fold02` | `clean_041_tcn_k8_with_current_proprio` | `or_q99_K3` | 1.7059 | 9.09% | 43.24% | 100.00% | 0.00% | 70.00% | 93.33% | 0.2572 | 0.00% |
| 13 | `target_object_fold02` | `clean_044_lstm_k16_with_current_proprio` | `score_q99_K3` | 1.7025 | 4.55% | 40.54% | 96.67% | 0.00% | 70.00% | 93.33% | 0.2446 | 3.33% |
| 14 | `target_object_fold02` | `clean_044_lstm_k16_with_current_proprio` | `or_q99_K3` | 1.6836 | 8.33% | 40.54% | 96.67% | 0.00% | 70.00% | 93.33% | 0.2420 | 3.33% |
| 15 | `target_object_fold02` | `clean_041_tcn_k8_with_current_proprio` | `score_q99_K3` | 1.6582 | 5.30% | 43.24% | 96.67% | 0.00% | 70.00% | 93.33% | 0.2344 | 3.33% |

## Target-Object Low-FA Candidates

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `target_object_fold03` | `clean_044_lstm_k8_with_current_proprio` | `or_q95_K3` | 1.4322 | 44.70% | 28.51% | 100.00% | 0.00% | 54.17% | 100.00% | 0.2732 | 0.00% |
| 2 | `target_object_fold03` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 1.3156 | 21.97% | 27.19% | 100.00% | 0.00% | 41.67% | 100.00% | 0.2825 | 0.00% |
| 3 | `target_object_fold01` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 1.2101 | 14.39% | 24.53% | 97.50% | 22.50% | 35.00% | 75.00% | 0.3350 | 2.50% |
| 4 | `target_object_fold01` | `clean_041_tcn_k8_with_current_proprio` | `and_q95_K3` | 1.2650 | 7.58% | 19.81% | 100.00% | 0.00% | 30.00% | 75.00% | 0.3795 | 0.00% |
| 5 | `target_object_fold00` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 0.9378 | 14.71% | 24.64% | 90.48% | 0.00% | 28.57% | 85.71% | 0.3239 | 9.52% |
| 6 | `target_object_fold04` | `clean_041_tcn_k16_no_current_proprio` | `score_q99_K3` | 0.9426 | 4.55% | 26.56% | 90.91% | 0.00% | 27.27% | 72.73% | 0.3887 | 9.09% |
| 7 | `target_object_fold04` | `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 0.8625 | 10.61% | 29.88% | 90.91% | 0.00% | 27.27% | 72.73% | 0.3623 | 9.09% |
| 8 | `target_object_fold00` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 0.8712 | 13.24% | 23.22% | 88.10% | 0.00% | 26.19% | 80.95% | 0.3337 | 11.90% |
| 9 | `target_object_fold00` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 0.9177 | 15.44% | 28.91% | 95.24% | 0.00% | 26.19% | 88.10% | 0.3256 | 4.76% |
| 10 | `target_object_fold03` | `clean_044_lstm_k8_with_current_proprio` | `or_q99_K3` | 1.3511 | 11.36% | 6.14% | 100.00% | 0.00% | 25.00% | 83.33% | 0.3721 | 0.00% |
| 11 | `target_object_fold03` | `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 1.2412 | 8.33% | 14.47% | 100.00% | 0.00% | 25.00% | 95.83% | 0.3371 | 0.00% |
| 12 | `target_object_fold03` | `clean_044_lstm_k16_with_current_proprio` | `or_q99_K3` | 1.2594 | 9.09% | 7.46% | 100.00% | 0.00% | 20.83% | 83.33% | 0.3906 | 0.00% |
| 13 | `target_object_fold03` | `clean_041_tcn_k8_with_current_proprio` | `and_q95_K3` | 1.2538 | 7.58% | 8.33% | 100.00% | 0.00% | 20.83% | 66.67% | 0.4338 | 0.00% |
| 14 | `target_object_fold03` | `clean_041_tcn_k8_no_current_proprio` | `or_q99_K3` | 1.1136 | 10.61% | 16.67% | 100.00% | 0.00% | 20.83% | 95.83% | 0.3446 | 0.00% |
| 15 | `target_object_fold03` | `clean_041_tcn_k8_with_current_proprio` | `or_q99_K3` | 1.0977 | 9.85% | 17.98% | 100.00% | 0.00% | 20.83% | 95.83% | 0.3403 | 0.00% |

## Top OOD Task 8/9 Policies

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_task_8_9` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 1.7848 | 15.42% | 31.43% | 95.83% | 34.72% | 70.83% | 88.89% | 0.2043 | 4.17% |
| 2 | `ood_task_8_9` | `clean_044_lstm_k16_with_current_proprio` | `or_q99_K3` | 1.7350 | 8.92% | 10.99% | 93.06% | 13.89% | 54.17% | 77.78% | 0.3053 | 6.94% |
| 3 | `ood_task_8_9` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 1.7069 | 12.78% | 28.24% | 94.44% | 20.83% | 65.28% | 83.33% | 0.2496 | 5.56% |
| 4 | `ood_task_8_9` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.6672 | 12.58% | 27.25% | 97.22% | 25.00% | 59.72% | 80.56% | 0.2757 | 2.78% |
| 5 | `ood_task_8_9` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 1.6669 | 14.81% | 32.09% | 100.00% | 26.39% | 61.11% | 93.06% | 0.2372 | 0.00% |
| 6 | `ood_task_8_9` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.6620 | 15.21% | 28.57% | 94.44% | 26.39% | 63.89% | 76.39% | 0.2638 | 5.56% |
| 7 | `ood_task_8_9` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 1.6616 | 12.37% | 27.69% | 93.06% | 20.83% | 63.89% | 76.39% | 0.2657 | 6.94% |
| 8 | `ood_task_8_9` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 1.6520 | 13.59% | 29.78% | 98.61% | 26.39% | 59.72% | 87.50% | 0.2493 | 1.39% |
| 9 | `ood_task_8_9` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 1.6430 | 18.26% | 32.53% | 95.83% | 22.22% | 65.28% | 77.78% | 0.2748 | 4.17% |
| 10 | `ood_task_8_9` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 1.6336 | 15.01% | 28.68% | 97.22% | 26.39% | 59.72% | 80.56% | 0.2622 | 2.78% |

## OOD Task 8/9 Low-FA Candidates

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_task_8_9` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 1.7069 | 12.78% | 28.24% | 94.44% | 20.83% | 65.28% | 83.33% | 0.2496 | 5.56% |
| 2 | `ood_task_8_9` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 1.6616 | 12.37% | 27.69% | 93.06% | 20.83% | 63.89% | 76.39% | 0.2657 | 6.94% |
| 3 | `ood_task_8_9` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.6620 | 15.21% | 28.57% | 94.44% | 26.39% | 63.89% | 76.39% | 0.2638 | 5.56% |
| 4 | `ood_task_8_9` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 1.6044 | 15.62% | 28.57% | 93.06% | 18.06% | 62.50% | 75.00% | 0.2834 | 6.94% |
| 5 | `ood_task_8_9` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.6672 | 12.58% | 27.25% | 97.22% | 25.00% | 59.72% | 80.56% | 0.2757 | 2.78% |
| 6 | `ood_task_8_9` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 1.6336 | 15.01% | 28.68% | 97.22% | 26.39% | 59.72% | 80.56% | 0.2622 | 2.78% |
| 7 | `ood_task_8_9` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 1.6520 | 13.59% | 29.78% | 98.61% | 26.39% | 59.72% | 87.50% | 0.2493 | 1.39% |
| 8 | `ood_task_8_9` | `clean_044_lstm_k16_with_current_proprio` | `or_q99_K3` | 1.7350 | 8.92% | 10.99% | 93.06% | 13.89% | 54.17% | 77.78% | 0.3053 | 6.94% |
| 9 | `ood_task_8_9` | `clean_044_lstm_k8_with_current_proprio` | `or_q99_K3` | 1.5596 | 9.53% | 16.92% | 91.67% | 15.28% | 51.39% | 75.00% | 0.3110 | 8.33% |
| 10 | `ood_task_8_9` | `clean_041_tcn_k8_with_current_proprio` | `or_q99_K3` | 1.4271 | 9.33% | 25.82% | 91.67% | 18.06% | 51.39% | 75.00% | 0.3029 | 8.33% |

## Top OOD Perturbation Mug Policies

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 1.9689 | 14.35% | 17.67% | 97.93% | 25.39% | 67.36% | 84.97% | 0.2270 | 2.07% |
| 2 | `ood_perturbation_mug` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.9401 | 11.85% | 16.97% | 98.45% | 26.94% | 64.25% | 89.12% | 0.2264 | 1.55% |
| 3 | `ood_perturbation_mug` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 1.9349 | 14.97% | 16.97% | 98.45% | 20.21% | 64.77% | 86.53% | 0.2397 | 1.55% |
| 4 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 1.9145 | 14.76% | 19.78% | 97.93% | 27.46% | 66.32% | 89.64% | 0.2205 | 2.07% |
| 5 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 1.8919 | 11.43% | 16.87% | 97.93% | 24.35% | 62.18% | 86.53% | 0.2457 | 2.07% |
| 6 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.8771 | 11.23% | 15.16% | 97.41% | 22.28% | 60.62% | 82.38% | 0.2534 | 2.59% |
| 7 | `ood_perturbation_mug` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 1.8544 | 14.76% | 17.57% | 99.48% | 24.35% | 60.10% | 86.01% | 0.2467 | 0.52% |
| 8 | `ood_perturbation_mug` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 1.8445 | 10.40% | 14.16% | 95.85% | 24.87% | 59.59% | 84.46% | 0.2394 | 4.15% |
| 9 | `ood_perturbation_mug` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 1.8310 | 11.02% | 14.16% | 99.48% | 23.32% | 55.44% | 81.87% | 0.2728 | 0.52% |
| 10 | `ood_perturbation_mug` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 1.7944 | 11.85% | 13.55% | 97.41% | 18.13% | 55.44% | 82.38% | 0.2684 | 2.59% |

## OOD Perturbation Mug Low-FA Candidates

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 1.9689 | 14.35% | 17.67% | 97.93% | 25.39% | 67.36% | 84.97% | 0.2270 | 2.07% |
| 2 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 1.9145 | 14.76% | 19.78% | 97.93% | 27.46% | 66.32% | 89.64% | 0.2205 | 2.07% |
| 3 | `ood_perturbation_mug` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 1.9349 | 14.97% | 16.97% | 98.45% | 20.21% | 64.77% | 86.53% | 0.2397 | 1.55% |
| 4 | `ood_perturbation_mug` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.9401 | 11.85% | 16.97% | 98.45% | 26.94% | 64.25% | 89.12% | 0.2264 | 1.55% |
| 5 | `ood_perturbation_mug` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 1.8919 | 11.43% | 16.87% | 97.93% | 24.35% | 62.18% | 86.53% | 0.2457 | 2.07% |
| 6 | `ood_perturbation_mug` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.8771 | 11.23% | 15.16% | 97.41% | 22.28% | 60.62% | 82.38% | 0.2534 | 2.59% |
| 7 | `ood_perturbation_mug` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 1.8544 | 14.76% | 17.57% | 99.48% | 24.35% | 60.10% | 86.01% | 0.2467 | 0.52% |
| 8 | `ood_perturbation_mug` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 1.8445 | 10.40% | 14.16% | 95.85% | 24.87% | 59.59% | 84.46% | 0.2394 | 4.15% |
| 9 | `ood_perturbation_mug` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 1.7944 | 11.85% | 13.55% | 97.41% | 18.13% | 55.44% | 82.38% | 0.2684 | 2.59% |
| 10 | `ood_perturbation_mug` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 1.8310 | 11.02% | 14.16% | 99.48% | 23.32% | 55.44% | 81.87% | 0.2728 | 0.52% |

## Top OOD Perturbation Milk Policies

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 1.6600 | 16.01% | 34.36% | 95.24% | 48.92% | 67.53% | 91.34% | 0.1644 | 4.76% |
| 2 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.6113 | 12.25% | 29.62% | 94.81% | 45.02% | 61.04% | 90.48% | 0.1849 | 5.19% |
| 3 | `ood_perturbation_milk` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 1.6060 | 14.23% | 35.66% | 95.24% | 37.23% | 65.37% | 88.74% | 0.1986 | 4.76% |
| 4 | `ood_perturbation_milk` | `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 1.6008 | 11.46% | 31.16% | 94.81% | 34.20% | 61.47% | 87.88% | 0.2063 | 5.19% |
| 5 | `ood_perturbation_milk` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 1.5822 | 17.79% | 37.80% | 96.97% | 27.27% | 64.94% | 89.61% | 0.2261 | 3.03% |
| 6 | `ood_perturbation_milk` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 1.5092 | 12.65% | 33.41% | 96.10% | 34.20% | 57.58% | 91.34% | 0.2149 | 3.90% |
| 7 | `ood_perturbation_milk` | `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 1.4950 | 15.22% | 36.97% | 96.10% | 38.96% | 60.17% | 91.77% | 0.1966 | 3.90% |
| 8 | `ood_perturbation_milk` | `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 1.4713 | 12.85% | 34.72% | 96.97% | 22.08% | 55.84% | 87.88% | 0.2545 | 3.03% |
| 9 | `ood_perturbation_milk` | `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 1.1595 | 14.03% | 33.18% | 93.51% | 25.97% | 42.86% | 87.01% | 0.2765 | 6.49% |
| 10 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `or_q95_K3` | 1.1561 | 39.33% | 68.84% | 98.70% | 49.35% | 70.56% | 94.81% | 0.1624 | 1.30% |

## OOD Perturbation Milk Low-FA Candidates

| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 1.6113 | 12.25% | 29.62% | 94.81% | 45.02% | 61.04% | 90.48% | 0.1849 | 5.19% |
| 2 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `or_q99_K3` | 0.8122 | 5.93% | 28.44% | 87.88% | 1.73% | 25.54% | 71.00% | 0.3779 | 12.12% |
| 3 | `ood_perturbation_milk` | `clean_041_tcn_k8_no_current_proprio` | `or_q99_K3` | 0.7886 | 6.13% | 28.79% | 87.45% | 1.73% | 25.11% | 71.86% | 0.3547 | 12.55% |
| 4 | `ood_perturbation_milk` | `clean_044_lstm_k8_with_current_proprio` | `score_q99_K3` | 0.9597 | 3.36% | 20.62% | 90.04% | 3.90% | 24.24% | 73.59% | 0.3668 | 9.96% |
| 5 | `ood_perturbation_milk` | `clean_041_tcn_k8_with_current_proprio` | `score_q99_K3` | 0.9370 | 1.78% | 14.57% | 84.85% | 1.73% | 23.38% | 65.80% | 0.4024 | 15.15% |
| 6 | `ood_perturbation_milk` | `clean_041_tcn_k8_no_current_proprio` | `score_q99_K3` | 0.9037 | 2.17% | 14.93% | 83.98% | 1.73% | 22.94% | 67.53% | 0.3669 | 16.02% |
| 7 | `ood_perturbation_milk` | `clean_044_lstm_k16_with_current_proprio` | `or_q99_K3` | 0.7058 | 6.52% | 27.25% | 85.71% | 3.90% | 21.65% | 65.80% | 0.3948 | 14.29% |
| 8 | `ood_perturbation_milk` | `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 0.6973 | 5.73% | 28.08% | 86.58% | 5.63% | 20.78% | 66.23% | 0.4000 | 13.42% |
| 9 | `ood_perturbation_milk` | `clean_044_lstm_k16_with_current_proprio` | `score_q99_K3` | 0.7554 | 3.16% | 14.10% | 79.65% | 3.90% | 19.48% | 61.90% | 0.3961 | 20.35% |
| 10 | `ood_perturbation_milk` | `clean_041_tcn_k16_no_current_proprio` | `score_q99_K3` | 0.8069 | 2.17% | 14.45% | 83.55% | 5.63% | 18.18% | 61.90% | 0.4217 | 16.45% |

## Target-Object Fold Average By Job

Averaged over folds 00-03 only; fold04 is lower support and should not drive decisions.

| Job | Folds | Seen FA | OOD Success FA | OOD Failure Det | OOD Det@25 | Mean Time |
|---|---:|---:|---:|---:|---:|---:|
| `clean_041_tcn_k16_no_current_proprio` | 4 | 22.96% | 54.09% | 98.81% | 53.96% | 0.2368 |
| `clean_041_tcn_k8_no_current_proprio` | 4 | 21.08% | 57.35% | 98.81% | 58.96% | 0.2390 |
| `clean_041_tcn_k8_with_current_proprio` | 4 | 21.48% | 57.72% | 97.62% | 58.81% | 0.2489 |
| `clean_044_lstm_k16_with_current_proprio` | 4 | 20.18% | 49.94% | 97.62% | 41.64% | 0.2829 |
| `clean_044_lstm_k8_with_current_proprio` | 4 | 20.91% | 45.33% | 98.81% | 52.80% | 0.2580 |

Same policy averaged over all target-object folds, including low-support fold04:

| Job | Folds | Seen FA | OOD Success FA | OOD Failure Det | OOD Det@25 | Mean Time |
|---|---:|---:|---:|---:|---:|---:|
| `clean_041_tcn_k16_no_current_proprio` | 5 | 22.91% | 59.37% | 99.05% | 55.89% | 0.2356 |
| `clean_041_tcn_k8_no_current_proprio` | 5 | 21.56% | 61.98% | 99.05% | 59.89% | 0.2365 |
| `clean_041_tcn_k8_with_current_proprio` | 5 | 22.18% | 62.28% | 98.10% | 59.77% | 0.2447 |
| `clean_044_lstm_k16_with_current_proprio` | 5 | 20.54% | 56.05% | 98.10% | 42.40% | 0.2766 |
| `clean_044_lstm_k8_with_current_proprio` | 5 | 22.03% | 52.45% | 99.05% | 51.33% | 0.2533 |

## Current Judgment

The completed artifacts pass the local sanity checks: no forbidden feature flags and score row counts match the evaluated rows.

- The clean temporal supervised models are clearly less pathological than the old action-only target-object result, but target-object OOD is not solved: useful detection usually still costs substantial successful-OOD alarms.
- OOD task 8/9 and OOD perturbation mug look substantially healthier than target-object folds so far.
- The sweep is incomplete until the remaining perturbation/family/global reruns finish; current conclusions are partial.
- `global_main` must be rerun after the empty-OOD split patch; old global-main job dirs only contain configs and are not valid results.

## Final Fields

```text
PARTIAL_AUDIT_COMPLETED_JOBS = 45
PARTIAL_AUDIT_COMPLETED_CAMPAIGNS = 9
PARTIAL_AUDIT_PARTIAL_CAMPAIGNS = NONE
PARTIAL_AUDIT_MISSING_CAMPAIGNS = global_main, ood_perturbation_env, ood_family_spatial, ood_family_object_family, ood_family_goal, ood_family_10_family
PARTIAL_AUDIT_FEATURE_FAILURES = 0
PARTIAL_AUDIT_SCORE_ROW_MISMATCHES = 0
RESULTS_ARE_FINAL = NO
```
