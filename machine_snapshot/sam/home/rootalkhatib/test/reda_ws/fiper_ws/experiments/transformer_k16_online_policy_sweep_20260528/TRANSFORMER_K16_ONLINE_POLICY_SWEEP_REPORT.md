# Transformer K16 Online Policy Sweep

Model: `v2_018_transformer_k16`.

This is a policy-only analysis over existing score traces. No model was retrained.
All new episode-level thresholds are calibrated only from `success_val_seen` episodes.

## Calibration Values

```json
{
  "q95_count_conformal_alpha0p05": 34,
  "q95_count_conformal_alpha0p1": 13,
  "q95_count_conformal_alpha0p15": 6,
  "q95_count_conformal_alpha0p2": 2,
  "q95_count_epq90": 12,
  "q95_count_epq95": 33,
  "q95_mass_conformal_alpha0p05": 7.74548602104187,
  "q95_mass_conformal_alpha0p1": 2.2850891947746277,
  "q95_mass_conformal_alpha0p15": 0.5283452868461609,
  "q95_mass_conformal_alpha0p2": 0.11291170120239258,
  "q95_mass_epq90": 2.0545735359191895,
  "q95_mass_epq95": 7.598891258239746,
  "q95_maxrun_conformal_alpha0p05": 21,
  "q95_maxrun_conformal_alpha0p1": 8,
  "q95_maxrun_conformal_alpha0p15": 3,
  "q95_maxrun_conformal_alpha0p2": 1,
  "q95_maxrun_epq90": 8,
  "q95_maxrun_epq95": 21,
  "q99_count_conformal_alpha0p05": 0,
  "q99_count_conformal_alpha0p1": 0,
  "q99_count_conformal_alpha0p15": 0,
  "q99_count_conformal_alpha0p2": 0,
  "q99_count_epq90": 0,
  "q99_count_epq95": 0,
  "q99_mass_conformal_alpha0p05": 0.0,
  "q99_mass_conformal_alpha0p1": 0.0,
  "q99_mass_conformal_alpha0p15": 0.0,
  "q99_mass_conformal_alpha0p2": 0.0,
  "q99_mass_epq90": 0.0,
  "q99_mass_epq95": 0.0,
  "q99_maxrun_conformal_alpha0p05": 0,
  "q99_maxrun_conformal_alpha0p1": 0,
  "q99_maxrun_conformal_alpha0p15": 0,
  "q99_maxrun_conformal_alpha0p2": 0,
  "q99_maxrun_epq90": 0,
  "q99_maxrun_epq95": 0
}
```

## Top Policies By Objective

| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `q95_count_conformal_alpha0p2` | split_conformal_count | 49.0% | 22.3% | 98.6% | 63.9% | 95.2% | 0.248 | 1.4% |
| 2 | `q95_mass_conformal_alpha0p2` | split_conformal_mass | 48.3% | 22.0% | 98.6% | 62.6% | 93.9% | 0.253 | 1.4% |
| 3 | `q95_consec_K1` | baseline_consecutive | 52.2% | 24.8% | 99.3% | 64.6% | 95.9% | 0.239 | 0.7% |
| 4 | `q95_maxrun_conformal_alpha0p2` | split_conformal_maxrun | 52.2% | 24.8% | 99.3% | 64.6% | 95.9% | 0.239 | 0.7% |
| 5 | `q95_consec_K2` | baseline_consecutive | 47.6% | 20.3% | 98.0% | 61.2% | 94.6% | 0.256 | 2.0% |
| 6 | `q95_count_5_reset_q90_R5` | recovery_reset_count | 43.6% | 18.8% | 98.0% | 57.1% | 92.5% | 0.272 | 2.0% |
| 7 | `q95_mass_conformal_alpha0p15` | split_conformal_mass | 43.2% | 17.9% | 98.0% | 56.5% | 92.5% | 0.275 | 2.0% |
| 8 | `q95_count_5_reset_q90_R10` | recovery_reset_count | 43.9% | 18.8% | 98.0% | 57.1% | 92.5% | 0.271 | 2.0% |
| 9 | `q95_consec_K3` | baseline_consecutive | 44.5% | 18.8% | 98.0% | 57.8% | 92.5% | 0.269 | 2.0% |
| 10 | `q95_maxrun_conformal_alpha0p15` | split_conformal_maxrun | 44.5% | 18.8% | 98.0% | 57.8% | 92.5% | 0.269 | 2.0% |
| 11 | `q95_count_5_reset_q90_R3` | recovery_reset_count | 43.4% | 18.7% | 97.3% | 57.1% | 92.5% | 0.269 | 2.7% |
| 12 | `q95_count_5` | manual_count | 44.9% | 19.3% | 98.0% | 57.1% | 92.5% | 0.270 | 2.0% |
| 13 | `q95_mass_1` | manual_mass | 40.2% | 16.1% | 98.0% | 52.4% | 90.5% | 0.293 | 2.0% |
| 14 | `q95_mass_1_reset_q90_R3` | recovery_reset_mass | 39.3% | 16.0% | 97.3% | 52.4% | 89.8% | 0.291 | 2.7% |
| 15 | `q95_mass_1_reset_q90_R5` | recovery_reset_mass | 39.5% | 16.0% | 97.3% | 52.4% | 89.8% | 0.289 | 2.7% |
| 16 | `q95_mass_1_reset_q90_R10` | recovery_reset_mass | 39.8% | 16.0% | 97.3% | 52.4% | 89.8% | 0.289 | 2.7% |
| 17 | `q95_consec_K5` | baseline_consecutive | 41.1% | 16.1% | 96.6% | 52.4% | 89.8% | 0.285 | 3.4% |
| 18 | `q95_count_conformal_alpha0p15` | split_conformal_count | 44.1% | 17.9% | 98.0% | 53.7% | 89.8% | 0.286 | 2.0% |
| 19 | `q99K1_or_q95_mass_2` | two_stage | 36.6% | 14.5% | 97.3% | 40.8% | 86.4% | 0.316 | 2.7% |
| 20 | `q95_mass_2` | manual_mass | 36.6% | 14.3% | 97.3% | 40.8% | 86.4% | 0.317 | 2.7% |
| 21 | `q95_mass_epq90` | episode_calibrated_mass | 36.4% | 14.3% | 97.3% | 40.1% | 86.4% | 0.318 | 2.7% |
| 22 | `q95_mass_conformal_alpha0p1` | split_conformal_mass | 35.9% | 13.9% | 96.6% | 39.5% | 85.7% | 0.316 | 3.4% |
| 23 | `q95_mass_2_reset_q90_R10` | recovery_reset_mass | 36.4% | 13.7% | 96.6% | 40.1% | 85.7% | 0.316 | 3.4% |
| 24 | `q99K1_or_q95_count_10` | two_stage | 39.9% | 16.0% | 98.0% | 42.2% | 86.4% | 0.309 | 2.0% |
| 25 | `q95_count_10` | manual_count | 39.9% | 15.7% | 98.0% | 42.2% | 86.4% | 0.313 | 2.0% |

## Best Policies With OOD Success FA <= 20.0%

| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `q95_count_40` | manual_count | 19.6% | 8.0% | 94.6% | 0.0% | 61.9% | 0.461 | 5.4% |
| 2 | `q95_mass_15` | manual_mass | 12.6% | 6.5% | 90.5% | 10.9% | 57.1% | 0.464 | 9.5% |
| 3 | `q95_count_60` | manual_count | 14.5% | 6.3% | 90.5% | 0.0% | 48.3% | 0.528 | 9.5% |
| 4 | `q99K1_or_q95_mass_20` | two_stage | 11.8% | 7.1% | 89.8% | 20.4% | 54.4% | 0.455 | 10.2% |
| 5 | `q95_mass_15_reset_q90_R5` | recovery_reset_mass | 12.3% | 6.2% | 89.1% | 10.9% | 55.8% | 0.474 | 10.9% |
| 6 | `q95_mass_15_reset_q90_R10` | recovery_reset_mass | 12.4% | 6.3% | 89.1% | 10.9% | 55.8% | 0.472 | 10.9% |
| 7 | `q95_mass_20` | manual_mass | 7.6% | 5.9% | 89.1% | 0.7% | 48.3% | 0.509 | 10.9% |
| 8 | `q95_count_80` | manual_count | 6.3% | 5.0% | 89.1% | 0.0% | 30.6% | 0.606 | 10.9% |
| 9 | `q95_mass_15_reset_q90_R3` | recovery_reset_mass | 12.2% | 6.2% | 88.4% | 10.9% | 54.4% | 0.474 | 11.6% |
| 10 | `q95_consec_K30` | baseline_consecutive | 19.5% | 6.8% | 87.1% | 4.8% | 57.1% | 0.448 | 12.9% |

## Best Policies With OOD Success FA <= 30.0%

| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `q99K1_or_q95_count_30` | two_stage | 26.8% | 10.2% | 95.9% | 21.1% | 68.0% | 0.393 | 4.1% |
| 2 | `q95_count_30` | manual_count | 24.6% | 9.5% | 95.2% | 6.1% | 67.3% | 0.416 | 4.8% |
| 3 | `q99K1_or_q95_count_40` | two_stage | 23.2% | 9.0% | 95.2% | 20.4% | 63.3% | 0.423 | 4.8% |
| 4 | `q95_count_epq95` | episode_calibrated_count | 22.9% | 9.0% | 94.6% | 3.4% | 66.0% | 0.425 | 5.4% |
| 5 | `q95_count_conformal_alpha0p05` | split_conformal_count | 22.3% | 9.0% | 94.6% | 2.0% | 66.0% | 0.429 | 5.4% |
| 6 | `q95_count_40` | manual_count | 19.6% | 8.0% | 94.6% | 0.0% | 61.9% | 0.461 | 5.4% |
| 7 | `q95_consec_K20` | baseline_consecutive | 28.8% | 8.3% | 93.2% | 19.0% | 73.5% | 0.377 | 6.8% |
| 8 | `q95_maxrun_conformal_alpha0p05` | split_conformal_maxrun | 27.6% | 8.1% | 93.2% | 17.7% | 73.5% | 0.381 | 6.8% |
| 9 | `q95_maxrun_epq95` | episode_calibrated_maxrun | 27.6% | 8.1% | 93.2% | 17.7% | 73.5% | 0.381 | 6.8% |
| 10 | `q99K1_or_q95_mass_10` | two_stage | 24.2% | 8.7% | 92.5% | 20.4% | 66.0% | 0.391 | 7.5% |

## Best Policies With OOD Success FA <= 35.0%

| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `q95_mass_3` | manual_mass | 34.7% | 12.3% | 96.6% | 36.7% | 83.7% | 0.328 | 3.4% |
| 2 | `q99K1_or_q95_count_20` | two_stage | 32.4% | 12.7% | 96.6% | 28.6% | 77.6% | 0.343 | 3.4% |
| 3 | `q95_mass_5` | manual_mass | 31.0% | 10.8% | 96.6% | 25.9% | 77.6% | 0.368 | 3.4% |
| 4 | `q99K1_or_q95_mass_5` | two_stage | 31.0% | 11.1% | 96.6% | 25.9% | 77.6% | 0.362 | 3.4% |
| 5 | `q95_count_20` | manual_count | 31.9% | 12.0% | 96.6% | 24.5% | 76.9% | 0.357 | 3.4% |
| 6 | `q95_mass_3_reset_q90_R10` | recovery_reset_mass | 34.5% | 11.7% | 95.9% | 34.7% | 83.7% | 0.327 | 4.1% |
| 7 | `q95_count_15_reset_q90_R3` | recovery_reset_count | 34.7% | 12.2% | 95.9% | 31.3% | 81.0% | 0.333 | 4.1% |
| 8 | `q99K1_or_q95_count_30` | two_stage | 26.8% | 10.2% | 95.9% | 21.1% | 68.0% | 0.393 | 4.1% |
| 9 | `q95_mass_3_reset_q90_R5` | recovery_reset_mass | 34.3% | 11.7% | 95.2% | 34.7% | 83.7% | 0.326 | 4.8% |
| 10 | `q95_count_20_reset_q90_R3` | recovery_reset_count | 30.9% | 10.5% | 95.2% | 23.1% | 76.2% | 0.360 | 4.8% |

## Best Policies With OOD Success FA <= 40.0%

| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `q95_count_10` | manual_count | 39.9% | 15.7% | 98.0% | 42.2% | 86.4% | 0.313 | 2.0% |
| 2 | `q99K1_or_q95_count_10` | two_stage | 39.9% | 16.0% | 98.0% | 42.2% | 86.4% | 0.309 | 2.0% |
| 3 | `q95_count_epq90` | episode_calibrated_count | 38.9% | 14.6% | 98.0% | 40.1% | 85.0% | 0.323 | 2.0% |
| 4 | `q95_count_conformal_alpha0p1` | split_conformal_count | 38.1% | 14.3% | 98.0% | 38.8% | 83.7% | 0.329 | 2.0% |
| 5 | `q95_mass_1_reset_q90_R3` | recovery_reset_mass | 39.3% | 16.0% | 97.3% | 52.4% | 89.8% | 0.291 | 2.7% |
| 6 | `q95_mass_1_reset_q90_R5` | recovery_reset_mass | 39.5% | 16.0% | 97.3% | 52.4% | 89.8% | 0.289 | 2.7% |
| 7 | `q95_mass_1_reset_q90_R10` | recovery_reset_mass | 39.8% | 16.0% | 97.3% | 52.4% | 89.8% | 0.289 | 2.7% |
| 8 | `q95_mass_2` | manual_mass | 36.6% | 14.3% | 97.3% | 40.8% | 86.4% | 0.317 | 2.7% |
| 9 | `q99K1_or_q95_mass_2` | two_stage | 36.6% | 14.5% | 97.3% | 40.8% | 86.4% | 0.316 | 2.7% |
| 10 | `q95_mass_epq90` | episode_calibrated_mass | 36.4% | 14.3% | 97.3% | 40.1% | 86.4% | 0.318 | 2.7% |

## Best Policies With OOD Success FA <= 45.0%

| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `q95_consec_K3` | baseline_consecutive | 44.5% | 18.8% | 98.0% | 57.8% | 92.5% | 0.269 | 2.0% |
| 2 | `q95_maxrun_conformal_alpha0p15` | split_conformal_maxrun | 44.5% | 18.8% | 98.0% | 57.8% | 92.5% | 0.269 | 2.0% |
| 3 | `q95_count_5_reset_q90_R5` | recovery_reset_count | 43.6% | 18.8% | 98.0% | 57.1% | 92.5% | 0.272 | 2.0% |
| 4 | `q95_count_5_reset_q90_R10` | recovery_reset_count | 43.9% | 18.8% | 98.0% | 57.1% | 92.5% | 0.271 | 2.0% |
| 5 | `q95_count_5` | manual_count | 44.9% | 19.3% | 98.0% | 57.1% | 92.5% | 0.270 | 2.0% |
| 6 | `q95_mass_conformal_alpha0p15` | split_conformal_mass | 43.2% | 17.9% | 98.0% | 56.5% | 92.5% | 0.275 | 2.0% |
| 7 | `q95_mass_1` | manual_mass | 40.2% | 16.1% | 98.0% | 52.4% | 90.5% | 0.293 | 2.0% |
| 8 | `q95_count_conformal_alpha0p15` | split_conformal_count | 44.1% | 17.9% | 98.0% | 53.7% | 89.8% | 0.286 | 2.0% |
| 9 | `q95_count_10` | manual_count | 39.9% | 15.7% | 98.0% | 42.2% | 86.4% | 0.313 | 2.0% |
| 10 | `q99K1_or_q95_count_10` | two_stage | 39.9% | 16.0% | 98.0% | 42.2% | 86.4% | 0.309 | 2.0% |

## Decision Notes

- `q95_consec_K3` is the original score-only reference.
- Count/mass policies are online accumulators over past score evidence.
- Recovery-reset policies reset accumulated evidence after sustained recovery below q90.
- Episode-calibrated policies use success validation episodes to target episode-level behavior instead of row-level behavior.
