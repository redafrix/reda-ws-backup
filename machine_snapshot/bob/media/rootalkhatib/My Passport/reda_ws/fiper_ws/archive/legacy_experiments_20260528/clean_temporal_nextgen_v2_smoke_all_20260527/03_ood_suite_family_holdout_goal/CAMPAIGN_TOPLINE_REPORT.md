# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 2.9893 | 0.14% | 100.00% | 100.00% | NA | NA |
| 2 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 0.9658 | 0.34% | 91.43% | 3.57% | NA | NA |
| 3 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 0.9646 | 0.34% | 78.57% | 10.00% | NA | NA |
| 4 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 0.9537 | 0.34% | 79.29% | 9.29% | NA | NA |
| 5 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 0.9309 | 0.20% | 85.00% | 5.00% | NA | NA |
| 6 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 0.9158 | 0.34% | 87.86% | 2.86% | NA | NA |
| 7 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 0.8454 | 0.27% | 76.43% | 5.00% | NA | NA |
| 8 | `v2_025_tcn_k8_flat_action_static` | supervised | seq_tcn | 0.8334 | 0.20% | 79.29% | 2.86% | NA | NA |
| 9 | `v2_024_tcn_k8_first_action_static` | supervised | seq_tcn | 0.8011 | 0.20% | 75.00% | 3.57% | NA | NA |
| 10 | `v2_004_tcn_k6_midshort` | supervised | seq_tcn | 0.7952 | 0.20% | 65.71% | 7.86% | NA | NA |
| 11 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 0.7580 | 0.14% | 60.71% | 8.57% | NA | NA |
| 12 | `v2_001_tcn_k1_baseline` | supervised | seq_tcn | 0.7558 | 0.14% | 65.71% | 5.71% | NA | NA |
| 13 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 0.7546 | 0.14% | 74.29% | 1.43% | NA | NA |
| 14 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 0.7378 | 0.14% | 70.00% | 2.86% | NA | NA |
| 15 | `v2_037_groupdro_target_tcn_k8` | supervised | seq_tcn | 0.7235 | 0.14% | 58.57% | 7.86% | NA | NA |
| 16 | `v2_017_transformer_medium_k8` | supervised | seq_transformer | 0.7142 | 0.14% | 64.29% | 4.29% | NA | NA |
| 17 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 0.6974 | 0.14% | 58.57% | 6.43% | NA | NA |
| 18 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 0.6878 | 0.14% | 59.29% | 5.71% | NA | NA |
| 19 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 0.6868 | 0.20% | 55.00% | 7.86% | NA | NA |
| 20 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 0.6866 | 0.14% | 55.00% | 7.86% | NA | NA |
