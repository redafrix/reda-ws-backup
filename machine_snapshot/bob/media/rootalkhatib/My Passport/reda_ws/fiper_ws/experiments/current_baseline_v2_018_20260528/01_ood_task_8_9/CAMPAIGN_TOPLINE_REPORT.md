# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 1.5963 | 49.01% | 100.00% | 77.78% | NA | NA |
| 2 | `v2_010_lstm_k4_short` | supervised | seq_lstm | 1.5782 | 51.21% | 98.61% | 79.17% | NA | NA |
| 3 | `v2_022_tcn_k8_action_tokens_only` | supervised | seq_tcn | 1.5770 | 51.54% | 100.00% | 79.17% | NA | NA |
| 4 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 1.4897 | 48.57% | 100.00% | 72.22% | NA | NA |
| 5 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 1.4845 | 49.12% | 100.00% | 72.22% | NA | NA |
| 6 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 1.4788 | 55.05% | 100.00% | 76.39% | NA | NA |
| 7 | `v2_017_transformer_medium_k8` | supervised | seq_transformer | 1.4671 | 47.25% | 100.00% | 69.44% | NA | NA |
| 8 | `v2_014_gru_k8` | supervised | seq_gru | 1.4668 | 49.78% | 98.61% | 72.22% | NA | NA |
| 9 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 1.4552 | 51.21% | 100.00% | 72.22% | NA | NA |
| 10 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 1.4541 | 56.70% | 100.00% | 76.39% | NA | NA |
| 11 | `v2_003_tcn_k4_short` | supervised | seq_tcn | 1.4454 | 50.55% | 100.00% | 70.83% | NA | NA |
| 12 | `v2_033_survival_tcn_k8` | supervised | seq_tcn | 1.4380 | 50.44% | 100.00% | 70.83% | NA | NA |
| 13 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 1.4305 | 48.90% | 98.61% | 69.44% | NA | NA |
| 14 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 1.4301 | 49.45% | 100.00% | 69.44% | NA | NA |
| 15 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 1.4221 | 46.48% | 97.22% | 68.06% | NA | NA |
| 16 | `v2_042_dynamics_tcn_k8_pastdelta` | supervised | seq_tcn | 1.4140 | 52.31% | 100.00% | 70.83% | 22.64% | 81.94% |
| 17 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 1.4055 | 50.55% | 100.00% | 69.44% | NA | NA |
| 18 | `v2_034_survival_lstm_k8` | supervised | seq_lstm | 1.4016 | 50.22% | 98.61% | 69.44% | NA | NA |
| 19 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 1.3907 | 50.11% | 98.61% | 68.06% | NA | NA |
| 20 | `v2_035_survival_tcn_k16` | supervised | seq_tcn | 1.3738 | 49.23% | 100.00% | 66.67% | NA | NA |
