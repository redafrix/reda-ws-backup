# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_018_transformer_k16` | supervised | seq_transformer | 1.6212 | 16.67% | 100.00% | 54.17% | NA | NA |
| 2 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 1.3610 | 43.86% | 100.00% | 62.50% | NA | NA |
| 3 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 1.3062 | 53.07% | 100.00% | 66.67% | NA | NA |
| 4 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 1.2554 | 55.70% | 100.00% | 66.67% | NA | NA |
| 5 | `v2_009_tcn_k32_verylong` | supervised | seq_tcn | 1.2490 | 24.56% | 100.00% | 41.67% | NA | NA |
| 6 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 1.2147 | 47.81% | 100.00% | 58.33% | NA | NA |
| 7 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 1.2043 | 48.25% | 100.00% | 58.33% | NA | NA |
| 8 | `v2_015_gru_k16` | supervised | seq_gru | 1.1928 | 38.16% | 100.00% | 50.00% | NA | NA |
| 9 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 1.1549 | 46.49% | 100.00% | 54.17% | NA | NA |
| 10 | `v2_012_lstm_k16_long` | supervised | seq_lstm | 1.1300 | 27.19% | 100.00% | 37.50% | NA | NA |
| 11 | `v2_043_dynamics_survival_tcn_k8` | supervised | seq_tcn | 1.1176 | 43.42% | 100.00% | 50.00% | 4.39% | 95.83% |
| 12 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 1.1093 | 44.74% | 100.00% | 50.00% | NA | NA |
| 13 | `v2_042_dynamics_tcn_k8_pastdelta` | supervised | seq_tcn | 1.0831 | 56.58% | 100.00% | 58.33% | 5.70% | 91.67% |
| 14 | `v2_033_survival_tcn_k8` | supervised | seq_tcn | 1.0809 | 45.61% | 100.00% | 50.00% | NA | NA |
| 15 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 1.0486 | 86.40% | 100.00% | 79.17% | NA | NA |
| 16 | `v2_014_gru_k8` | supervised | seq_gru | 1.0447 | 42.98% | 100.00% | 45.83% | NA | NA |
| 17 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 1.0349 | 48.68% | 100.00% | 50.00% | NA | NA |
| 18 | `v2_022_tcn_k8_action_tokens_only` | supervised | seq_tcn | 1.0265 | 83.33% | 100.00% | 75.00% | NA | NA |
| 19 | `v2_026_tcn_k8_seqstats_static` | supervised | seq_tcn | 1.0096 | 67.54% | 100.00% | 62.50% | NA | NA |
| 20 | `v2_006_tcn_k12_mid` | supervised | seq_tcn | 1.0002 | 51.75% | 100.00% | 50.00% | NA | NA |
