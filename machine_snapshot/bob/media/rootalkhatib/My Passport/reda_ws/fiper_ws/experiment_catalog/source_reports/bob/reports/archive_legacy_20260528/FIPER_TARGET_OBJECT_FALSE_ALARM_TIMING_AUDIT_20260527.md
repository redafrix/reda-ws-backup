# Target-Object OOD False-Alarm Timing Audit

Split analyzed: `success_test_ood` for completed target-object folds `fold00` through `fold04`.

A false alarm is an OOD-success episode where the policy fires at least once. For K-step debounce, first false alarm time is the actual trigger step after K consecutive high-risk steps.

## Weighted Across All Target-Object Folds

| Job | Policy | FP Episodes | Total Episodes | FP Rate | Mean First Norm | Median First Norm | Mean First Step | Median First Step | Mean Alarm Steps per FP | Mean Alarm Steps per Success Ep |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `clean_041_tcn_k16_no_current_proprio` | `score_q95_K3` | 669 | 1114 | 60.05% | 0.328 | 0.329 | 51.852 | 54.000 | 46.567 | 27.965 |
| `clean_041_tcn_k16_no_current_proprio` | `score_q95_K5` | 616 | 1114 | 55.30% | 0.338 | 0.343 | 54.399 | 56.500 | 46.927 | 25.949 |
| `clean_041_tcn_k16_no_current_proprio` | `score_q99_K3` | 210 | 1114 | 18.85% | 0.418 | 0.386 | 72.000 | 65.000 | 36.000 | 6.786 |
| `clean_041_tcn_k16_no_current_proprio` | `or_q95_K3` | 770 | 1114 | 69.12% | 0.369 | 0.335 | 58.638 | 54.000 | 43.199 | 29.859 |
| `clean_041_tcn_k16_no_current_proprio` | `or_q99_K3` | 259 | 1114 | 23.25% | 0.455 | 0.389 | 79.405 | 65.000 | 30.764 | 7.153 |
| `clean_041_tcn_k16_no_current_proprio` | `and_q95_K3` | 182 | 1114 | 16.34% | 0.526 | 0.392 | 93.429 | 66.000 | 8.220 | 1.343 |
| `clean_041_tcn_k8_no_current_proprio` | `score_q95_K3` | 697 | 1114 | 62.57% | 0.321 | 0.322 | 50.316 | 53.000 | 31.888 | 19.952 |
| `clean_041_tcn_k8_no_current_proprio` | `score_q95_K5` | 621 | 1114 | 55.75% | 0.337 | 0.341 | 53.258 | 56.000 | 31.330 | 17.465 |
| `clean_041_tcn_k8_no_current_proprio` | `score_q99_K3` | 255 | 1114 | 22.89% | 0.409 | 0.395 | 67.412 | 58.000 | 28.800 | 6.592 |
| `clean_041_tcn_k8_no_current_proprio` | `or_q95_K3` | 802 | 1114 | 71.99% | 0.370 | 0.331 | 58.555 | 53.000 | 30.474 | 21.939 |
| `clean_041_tcn_k8_no_current_proprio` | `or_q99_K3` | 306 | 1114 | 27.47% | 0.450 | 0.397 | 76.255 | 63.000 | 25.467 | 6.996 |
| `clean_041_tcn_k8_no_current_proprio` | `and_q95_K3` | 167 | 1114 | 14.99% | 0.477 | 0.378 | 85.216 | 63.000 | 8.102 | 1.215 |
| `clean_041_tcn_k8_with_current_proprio` | `score_q95_K3` | 702 | 1114 | 63.02% | 0.334 | 0.320 | 51.120 | 52.000 | 40.101 | 25.270 |
| `clean_041_tcn_k8_with_current_proprio` | `score_q95_K5` | 639 | 1114 | 57.36% | 0.352 | 0.346 | 54.163 | 56.000 | 39.998 | 22.943 |
| `clean_041_tcn_k8_with_current_proprio` | `score_q99_K3` | 350 | 1114 | 31.42% | 0.417 | 0.377 | 64.280 | 61.000 | 30.580 | 9.608 |
| `clean_041_tcn_k8_with_current_proprio` | `or_q95_K3` | 807 | 1114 | 72.44% | 0.379 | 0.333 | 58.711 | 53.000 | 37.743 | 27.342 |
| `clean_041_tcn_k8_with_current_proprio` | `or_q99_K3` | 396 | 1114 | 35.55% | 0.445 | 0.380 | 71.207 | 63.000 | 28.220 | 10.031 |
| `clean_041_tcn_k8_with_current_proprio` | `and_q95_K3` | 171 | 1114 | 15.35% | 0.478 | 0.378 | 84.626 | 64.000 | 7.187 | 1.103 |
| `clean_044_lstm_k16_with_current_proprio` | `score_q95_K3` | 635 | 1114 | 57.00% | 0.348 | 0.344 | 53.691 | 55.000 | 37.918 | 21.614 |
| `clean_044_lstm_k16_with_current_proprio` | `score_q95_K5` | 566 | 1114 | 50.81% | 0.379 | 0.358 | 57.712 | 57.000 | 38.889 | 19.759 |
| `clean_044_lstm_k16_with_current_proprio` | `score_q99_K3` | 117 | 1114 | 10.50% | 0.392 | 0.361 | 69.060 | 58.000 | 49.000 | 5.146 |
| `clean_044_lstm_k16_with_current_proprio` | `or_q95_K3` | 766 | 1114 | 68.76% | 0.402 | 0.349 | 63.068 | 56.000 | 34.554 | 23.759 |
| `clean_044_lstm_k16_with_current_proprio` | `or_q99_K3` | 192 | 1114 | 17.24% | 0.481 | 0.388 | 86.448 | 62.000 | 32.307 | 5.568 |
| `clean_044_lstm_k16_with_current_proprio` | `and_q95_K3` | 139 | 1114 | 12.48% | 0.480 | 0.374 | 87.367 | 63.000 | 7.921 | 0.988 |
| `clean_044_lstm_k8_with_current_proprio` | `score_q95_K3` | 591 | 1114 | 53.05% | 0.329 | 0.322 | 53.723 | 53.000 | 39.279 | 20.838 |
| `clean_044_lstm_k8_with_current_proprio` | `score_q95_K5` | 524 | 1114 | 47.04% | 0.348 | 0.338 | 57.431 | 56.000 | 39.559 | 18.608 |
| `clean_044_lstm_k8_with_current_proprio` | `score_q99_K3` | 260 | 1114 | 23.34% | 0.342 | 0.317 | 53.815 | 44.000 | 28.973 | 6.762 |
| `clean_044_lstm_k8_with_current_proprio` | `or_q95_K3` | 698 | 1114 | 62.66% | 0.383 | 0.337 | 62.348 | 54.500 | 36.279 | 22.732 |
| `clean_044_lstm_k8_with_current_proprio` | `or_q99_K3` | 320 | 1114 | 28.73% | 0.393 | 0.326 | 64.891 | 49.000 | 25.113 | 7.214 |
| `clean_044_lstm_k8_with_current_proprio` | `and_q95_K3` | 178 | 1114 | 15.98% | 0.505 | 0.387 | 90.399 | 65.000 | 8.787 | 1.404 |

## Fold-Level Score q95 K3

This is the policy family that produced roughly 45-60% OOD-success episode false alarms in the previous fold averages.

| Fold | Job | FP Rate | Mean First Norm | Median First Norm | Mean First Step | Median First Step | Mean Alarm Steps per FP |
|---|---|---:|---:|---:|---:|---:|---:|
| `fold00` | `clean_041_tcn_k16_no_current_proprio` | 27.49% | 0.404 | 0.389 | 75.586 | 74.000 | 28.741 |
| `fold00` | `clean_041_tcn_k8_no_current_proprio` | 40.28% | 0.423 | 0.387 | 76.035 | 69.000 | 16.965 |
| `fold00` | `clean_041_tcn_k8_with_current_proprio` | 24.64% | 0.399 | 0.363 | 74.885 | 66.500 | 21.827 |
| `fold00` | `clean_044_lstm_k16_with_current_proprio` | 18.01% | 0.460 | 0.406 | 93.342 | 81.500 | 15.289 |
| `fold00` | `clean_044_lstm_k8_with_current_proprio` | 28.91% | 0.402 | 0.354 | 74.820 | 68.000 | 21.508 |
| `fold01` | `clean_041_tcn_k16_no_current_proprio` | 56.60% | 0.314 | 0.224 | 58.150 | 39.000 | 16.308 |
| `fold01` | `clean_041_tcn_k8_no_current_proprio` | 53.77% | 0.256 | 0.171 | 47.640 | 30.000 | 9.781 |
| `fold01` | `clean_041_tcn_k8_with_current_proprio` | 56.13% | 0.235 | 0.156 | 43.202 | 29.000 | 10.782 |
| `fold01` | `clean_044_lstm_k16_with_current_proprio` | 39.62% | 0.204 | 0.111 | 39.107 | 20.500 | 7.024 |
| `fold01` | `clean_044_lstm_k8_with_current_proprio` | 50.00% | 0.379 | 0.241 | 69.792 | 47.500 | 15.500 |
| `fold02` | `clean_041_tcn_k16_no_current_proprio` | 76.58% | 0.329 | 0.320 | 53.006 | 49.000 | 45.676 |
| `fold02` | `clean_041_tcn_k8_no_current_proprio` | 75.68% | 0.305 | 0.309 | 49.440 | 49.000 | 42.018 |
| `fold02` | `clean_041_tcn_k8_with_current_proprio` | 87.39% | 0.331 | 0.313 | 52.500 | 50.000 | 40.804 |
| `fold02` | `clean_044_lstm_k16_with_current_proprio` | 83.78% | 0.354 | 0.333 | 56.462 | 53.000 | 43.441 |
| `fold02` | `clean_044_lstm_k8_with_current_proprio` | 75.23% | 0.355 | 0.333 | 56.497 | 53.000 | 40.587 |
| `fold03` | `clean_041_tcn_k16_no_current_proprio` | 55.70% | 0.595 | 0.561 | 77.850 | 74.000 | 29.764 |
| `fold03` | `clean_041_tcn_k8_no_current_proprio` | 59.65% | 0.595 | 0.569 | 77.441 | 77.000 | 26.221 |
| `fold03` | `clean_041_tcn_k8_with_current_proprio` | 62.72% | 0.663 | 0.569 | 85.573 | 78.000 | 26.490 |
| `fold03` | `clean_044_lstm_k16_with_current_proprio` | 58.33% | 0.600 | 0.600 | 78.617 | 77.000 | 28.135 |
| `fold03` | `clean_044_lstm_k8_with_current_proprio` | 27.19% | 0.630 | 0.623 | 85.790 | 81.000 | 23.177 |
| `fold04` | `clean_041_tcn_k16_no_current_proprio` | 80.50% | 0.138 | 0.016 | 22.830 | 2.000 | 82.392 |
| `fold04` | `clean_041_tcn_k8_no_current_proprio` | 80.50% | 0.135 | 0.016 | 22.361 | 2.000 | 46.619 |
| `fold04` | `clean_041_tcn_k8_with_current_proprio` | 80.50% | 0.138 | 0.016 | 22.830 | 2.000 | 72.314 |
| `fold04` | `clean_044_lstm_k16_with_current_proprio` | 80.50% | 0.210 | 0.278 | 32.495 | 37.500 | 57.139 |
| `fold04` | `clean_044_lstm_k8_with_current_proprio` | 80.91% | 0.160 | 0.086 | 25.815 | 12.000 | 61.764 |

## Practical Reading

- Mean first norm near `0.50` means false alarms usually happen halfway through successful OOD episodes, not immediately at the start.
- Mean alarm steps per FP episode measures burden after an episode has already false-alarmed; mean alarm steps per success episode measures overall burden including clean episodes.
- If a policy has acceptable failure detection but first false alarms occur late, it may still be usable as a warning signal; if first false alarms are early and frequent, it is much worse operationally.

## Final Fields

```text
TARGET_OBJECT_FALSE_ALARM_TIMING_ROWS = 150
TARGET_OBJECT_FALSE_ALARM_TIMING_REPORT = reports/FIPER_TARGET_OBJECT_FALSE_ALARM_TIMING_AUDIT_20260527.md
```
