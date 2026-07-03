# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 2.9925 | 0.00% | 100.00% | 100.00% | NA | NA |
| 2 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 2.5827 | 3.23% | 100.00% | 82.31% | NA | NA |
| 3 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 2.5379 | 3.95% | 99.32% | 80.95% | NA | NA |
| 4 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 2.4853 | 6.55% | 99.32% | 80.27% | NA | NA |
| 5 | `v2_024_tcn_k8_first_action_static` | supervised | seq_tcn | 2.3196 | 3.32% | 100.00% | 69.39% | NA | NA |
| 6 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 2.0921 | 1.62% | 100.00% | 56.46% | NA | NA |
| 7 | `v2_042_dynamics_tcn_k8_pastdelta` | supervised | seq_tcn | 1.9180 | 1.89% | 99.32% | 48.30% | 0.00% | 26.53% |
| 8 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 1.7054 | 1.62% | 99.32% | 37.41% | NA | NA |
| 9 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 1.6546 | 1.62% | 97.28% | 36.05% | NA | NA |
| 10 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 1.6113 | 2.06% | 97.28% | 34.01% | NA | NA |
| 11 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 1.6090 | 1.17% | 98.64% | 32.65% | NA | NA |
| 12 | `v2_006_tcn_k12_mid` | supervised | seq_tcn | 1.3511 | 1.44% | 99.32% | 19.73% | NA | NA |
| 13 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 1.3259 | 1.97% | 98.64% | 19.05% | NA | NA |
| 14 | `v2_015_gru_k16` | supervised | seq_gru | 1.2400 | 0.90% | 97.96% | 14.29% | NA | NA |
| 15 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 1.2335 | 0.81% | 98.64% | 13.61% | NA | NA |
| 16 | `v2_001_tcn_k1_baseline` | supervised | seq_tcn | 1.1692 | 0.63% | 97.28% | 10.88% | NA | NA |
| 17 | `v2_034_survival_lstm_k8` | supervised | seq_lstm | 1.1662 | 0.45% | 97.96% | 10.20% | NA | NA |
| 18 | `v2_035_survival_tcn_k16` | supervised | seq_tcn | 1.1301 | 0.90% | 96.60% | 9.52% | NA | NA |
| 19 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 1.1121 | 0.81% | 90.48% | 11.56% | NA | NA |
| 20 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 1.0953 | 1.26% | 93.88% | 9.52% | NA | NA |
