# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_022_tcn_k8_action_tokens_only` | supervised | seq_tcn | 1.4526 | 69.43% | 99.57% | 84.85% | NA | NA |
| 2 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 1.3918 | 68.48% | 99.57% | 80.95% | NA | NA |
| 3 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 1.3386 | 69.43% | 98.27% | 79.65% | NA | NA |
| 4 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 1.3292 | 68.48% | 99.57% | 77.92% | NA | NA |
| 5 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 1.3072 | 69.19% | 98.70% | 77.49% | NA | NA |
| 6 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 1.2888 | 69.67% | 99.13% | 77.06% | NA | NA |
| 7 | `v2_043_dynamics_survival_tcn_k8` | supervised | seq_tcn | 1.2887 | 68.25% | 98.70% | 75.76% | 12.68% | 67.97% |
| 8 | `v2_003_tcn_k4_short` | supervised | seq_tcn | 1.2469 | 69.91% | 99.13% | 74.89% | NA | NA |
| 9 | `v2_017_transformer_medium_k8` | supervised | seq_transformer | 1.2155 | 68.96% | 99.57% | 72.29% | NA | NA |
| 10 | `v2_005_tcn_k8_idea41` | supervised | seq_tcn | 1.2076 | 69.55% | 99.57% | 72.29% | NA | NA |
| 11 | `v2_004_tcn_k6_midshort` | supervised | seq_tcn | 1.1708 | 69.43% | 98.70% | 71.00% | NA | NA |
| 12 | `v2_026_tcn_k8_seqstats_static` | supervised | seq_tcn | 1.1645 | 70.14% | 100.00% | 70.56% | NA | NA |
| 13 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 1.1375 | 70.73% | 98.27% | 70.13% | NA | NA |
| 14 | `v2_024_tcn_k8_first_action_static` | supervised | seq_tcn | 1.1318 | 69.19% | 98.70% | 69.26% | NA | NA |
| 15 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 1.1226 | 68.25% | 99.13% | 67.53% | NA | NA |
| 16 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 1.1132 | 69.43% | 99.57% | 67.53% | NA | NA |
| 17 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 1.1029 | 69.43% | 100.00% | 67.10% | NA | NA |
| 18 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 1.0994 | 69.55% | 98.27% | 67.53% | NA | NA |
| 19 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 1.0973 | 68.60% | 99.13% | 66.23% | NA | NA |
| 20 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 1.0947 | 68.96% | 100.00% | 66.23% | NA | NA |
