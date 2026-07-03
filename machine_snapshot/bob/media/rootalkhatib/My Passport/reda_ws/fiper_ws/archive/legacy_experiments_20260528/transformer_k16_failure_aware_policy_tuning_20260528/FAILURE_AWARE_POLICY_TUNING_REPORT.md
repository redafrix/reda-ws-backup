# Failure-Aware Policy Tuning Report

Model: `v2_018_transformer_k16`
Held-out final fold: `fold_00_holdout_alphabet_soup_bbq_sauce`
Dev folds: `fold_01_holdout_butter_chocolate_pudding, fold_02_holdout_cream_cheese_ketchup, fold_03_holdout_milk_orange_juice, fold_04_holdout_salad_dressing_tomato_sauce`

The policy is selected using success+failure metrics on dev folds, then evaluated on the held-out fold.
No held-out fold metrics are used for selection.

| FA Budget | Selected Policy | Family | Dev OOD FA | Dev Det | Dev Det@25 | Dev Det@50 | Heldout OOD FA | Heldout Det | Heldout Det@25 | Heldout Det@50 | Heldout Mean Time |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20.0% | `q99K1_or_q95_mass_20` | two_stage | 14.3% | 97.1% | 28.6% | 59.0% | 1.4% | 71.4% | 0.0% | 42.9% | 0.517 |
| 30.0% | `q99K1_or_q95_count_40` | two_stage | 28.0% | 100.0% | 28.6% | 69.5% | 2.8% | 83.3% | 0.0% | 47.6% | 0.520 |
| 35.0% | `q95_mass_5_reset_q90_R5` | recovery_reset_mass | 34.9% | 97.1% | 34.3% | 85.7% | 12.8% | 85.7% | 2.4% | 57.1% | 0.473 |
| 40.0% | `q95_mass_epq90` | episode_calibrated_mass | 39.9% | 100.0% | 50.5% | 93.3% | 22.3% | 92.9% | 14.3% | 76.2% | 0.400 |
| 45.0% | `q95_mass_1_reset_q90_R3` | recovery_reset_mass | 43.4% | 100.0% | 67.6% | 96.2% | 21.8% | 90.5% | 14.3% | 73.8% | 0.393 |
| 50.0% | `q95_count_5_reset_q90_R5` | recovery_reset_count | 48.2% | 100.0% | 73.3% | 96.2% | 24.2% | 92.9% | 16.7% | 83.3% | 0.358 |

## Held-Out Baselines

| Policy | Family | OOD FA | Seen FA | Det | Det@25 | Det@50 | Mean Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `q95_consec_K3` | baseline_consecutive | 23.7% | 13.2% | 92.9% | 21.4% | 83.3% | 0.356 | 7.1% |
| `q95_mass_conformal_alpha0p15` | split_conformal_mass | 25.6% | 15.4% | 95.2% | 26.2% | 85.7% | 0.332 | 4.8% |
| `q95_mass_1` | manual_mass | 22.3% | 13.2% | 92.9% | 14.3% | 76.2% | 0.400 | 7.1% |
| `q95_mass_3` | manual_mass | 19.0% | 11.0% | 88.1% | 9.5% | 66.7% | 0.409 | 11.9% |
