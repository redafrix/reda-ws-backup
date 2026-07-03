# Transformer K16 Dynamic Threshold Policy Sweep

## Setup

- Score root: `experiments/clean_temporal_nextgen_v2_full_all_20260527`
- Job: `v2_018_transformer_k16`
- Alpha: `0.15`
- Trained model changed: NO
- Calibration uses success_calib_seen for row thresholds and success_val_seen for conformal state thresholds.
- Dynamic threshold inputs: timestep and past/current scores only.

## Baseline

| Policy | Seen FA | OOD FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| fixed_q95_mass_conformal_alpha0p15 | 17.9% | 43.1% | 98.0% | 56.5% | 92.5% | 0.275 | 2.0% |

## Best Balanced Policies

| Rank | Policy | Seen FA | OOD FA | Failure Det | Det@25 | Det@50 | Mean Time | Never | Score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | fixed_q95_sliding_W20_alpha0p15 | 17.5% | 42.8% | 98.0% | 57.1% | 92.5% | 0.277 | 2.0% | 2.760 |
| 2 | fixed_q95_leaky_decay0p98_alpha0p15 | 18.1% | 43.0% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% | 2.754 |
| 3 | fixed_q95_reset_lowq90_K5_alpha0p15 | 18.2% | 43.0% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% | 2.754 |
| 4 | fixed_q95_leaky_decay0p99_alpha0p15 | 18.1% | 43.1% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% | 2.753 |
| 5 | fixed_q95_leaky_decay0p95_alpha0p15 | 18.4% | 43.0% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% | 2.753 |
| 6 | fixed_q95_leaky_decay0p9_alpha0p15 | 18.5% | 43.4% | 98.0% | 57.1% | 92.5% | 0.275 | 2.0% | 2.745 |
| 7 | fixed_q95_reset_lowq90_K20_alpha0p15 | 17.9% | 42.9% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% | 2.743 |
| 8 | fixed_q95_reset_lowq90_K10_alpha0p15 | 17.8% | 43.0% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% | 2.742 |
| 9 | fixed_q95_sliding_W40_alpha0p15 | 17.9% | 43.0% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% | 2.742 |
| 10 | fixed_q95_sliding_W80_alpha0p15 | 17.9% | 43.0% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% | 2.742 |
| 11 | fixed_q95_mass_conformal_alpha0p15 | 17.9% | 43.1% | 98.0% | 56.5% | 92.5% | 0.275 | 2.0% | 2.740 |
| 12 | fixed_q95_reset_lowq90_K3_alpha0p15 | 18.5% | 42.9% | 98.0% | 56.5% | 92.5% | 0.276 | 2.0% | 2.740 |

## Candidates That Beat Baseline OOD FA Without Major Detection Loss

| Rank | Policy | Seen FA | OOD FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | fixed_q95_sliding_W20_alpha0p15 | 17.5% | 42.8% | 98.0% | 57.1% | 92.5% | 0.277 | 2.0% |
| 2 | fixed_q95_reset_lowq90_K20_alpha0p15 | 17.9% | 42.9% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% |
| 3 | fixed_q95_reset_lowq90_K3_alpha0p15 | 18.5% | 42.9% | 98.0% | 56.5% | 92.5% | 0.276 | 2.0% |
| 4 | fixed_q95_leaky_decay0p98_alpha0p15 | 18.1% | 43.0% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% |
| 5 | fixed_q95_reset_lowq90_K5_alpha0p15 | 18.2% | 43.0% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% |
| 6 | fixed_q95_leaky_decay0p95_alpha0p15 | 18.4% | 43.0% | 98.0% | 57.1% | 92.5% | 0.276 | 2.0% |
| 7 | fixed_q95_reset_lowq90_K10_alpha0p15 | 17.8% | 43.0% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% |
| 8 | fixed_q95_sliding_W40_alpha0p15 | 17.9% | 43.0% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% |
| 9 | fixed_q95_sliding_W80_alpha0p15 | 17.9% | 43.0% | 98.0% | 56.5% | 92.5% | 0.277 | 2.0% |

## Verdict

- `DYNAMIC_POLICY_SWEEP_PASS` = **YES**
- `ANY_POLICY_REDUCES_OOD_FA_WITHOUT_MAJOR_DET_LOSS` = **YES**
- `BEST_RECOMMENDED_POLICY` = **fixed_q95_sliding_W20_alpha0p15**

## Output Files

- `experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528/dynamic_threshold_policy_sweep.csv`
- `experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528/dynamic_threshold_policy_sweep.json`
- `experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528/dynamic_threshold_policy_calibration.json`
