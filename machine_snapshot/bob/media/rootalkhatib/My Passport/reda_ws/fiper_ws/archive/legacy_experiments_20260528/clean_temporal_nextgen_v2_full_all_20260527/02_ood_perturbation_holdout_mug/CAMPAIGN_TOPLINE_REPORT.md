# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_019_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.4885 | 50.70% | 98.96% | 74.09% | NA | NA |
| 2 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 1.4771 | 55.12% | 100.00% | 76.68% | NA | NA |
| 3 | `v2_043_dynamics_survival_tcn_k8` | supervised | seq_tcn | 1.4667 | 50.50% | 99.48% | 72.54% | 1.20% | 47.15% |
| 4 | `v2_005_tcn_k8_idea41` | supervised | seq_tcn | 1.4661 | 50.40% | 98.96% | 72.54% | NA | NA |
| 5 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 1.4473 | 50.20% | 98.96% | 72.02% | NA | NA |
| 6 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 1.4456 | 51.00% | 100.00% | 72.02% | NA | NA |
| 7 | `v2_004_tcn_k6_midshort` | supervised | seq_tcn | 1.4405 | 51.00% | 98.96% | 72.02% | NA | NA |
| 8 | `v2_037_groupdro_target_tcn_k8` | supervised | seq_tcn | 1.4354 | 50.30% | 98.96% | 71.50% | NA | NA |
| 9 | `v2_014_gru_k8` | supervised | seq_gru | 1.4328 | 49.10% | 98.45% | 69.95% | NA | NA |
| 10 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 1.4323 | 49.20% | 98.96% | 70.47% | NA | NA |
| 11 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 1.4322 | 49.90% | 98.45% | 70.47% | NA | NA |
| 12 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 1.4151 | 50.00% | 98.96% | 69.95% | NA | NA |
| 13 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 1.4147 | 49.20% | 98.96% | 69.43% | NA | NA |
| 14 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 1.4012 | 49.20% | 98.45% | 68.91% | NA | NA |
| 15 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 1.4000 | 49.90% | 98.96% | 68.91% | NA | NA |
| 16 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 1.3999 | 50.60% | 99.48% | 69.43% | NA | NA |
| 17 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 1.3963 | 50.70% | 99.48% | 68.91% | NA | NA |
| 18 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 1.3899 | 51.41% | 99.48% | 69.43% | NA | NA |
| 19 | `v2_018_transformer_k16` | supervised | seq_transformer | 1.3899 | 50.30% | 98.45% | 68.91% | NA | NA |
| 20 | `v2_024_tcn_k8_first_action_static` | supervised | seq_tcn | 1.3887 | 51.20% | 98.96% | 69.95% | NA | NA |
