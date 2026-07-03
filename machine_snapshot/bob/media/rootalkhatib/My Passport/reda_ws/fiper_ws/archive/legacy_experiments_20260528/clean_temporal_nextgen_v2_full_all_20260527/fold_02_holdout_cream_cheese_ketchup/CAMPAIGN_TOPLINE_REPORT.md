# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 1.8315 | 58.56% | 100.00% | 96.67% | NA | NA |
| 2 | `v2_034_survival_lstm_k8` | supervised | seq_lstm | 1.8007 | 55.41% | 100.00% | 93.33% | NA | NA |
| 3 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 1.7994 | 56.76% | 100.00% | 93.33% | NA | NA |
| 4 | `v2_009_tcn_k32_verylong` | supervised | seq_tcn | 1.7947 | 61.26% | 100.00% | 96.67% | NA | NA |
| 5 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 1.7947 | 61.26% | 100.00% | 96.67% | NA | NA |
| 6 | `v2_015_gru_k16` | supervised | seq_gru | 1.7783 | 57.66% | 100.00% | 93.33% | NA | NA |
| 7 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 1.7571 | 68.47% | 100.00% | 100.00% | NA | NA |
| 8 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 1.7454 | 60.36% | 100.00% | 93.33% | NA | NA |
| 9 | `v2_037_groupdro_target_tcn_k8` | supervised | seq_tcn | 1.7284 | 69.37% | 100.00% | 100.00% | NA | NA |
| 10 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 1.7281 | 61.26% | 100.00% | 93.33% | NA | NA |
| 11 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 1.7121 | 60.81% | 100.00% | 93.33% | NA | NA |
| 12 | `v2_010_lstm_k4_short` | supervised | seq_lstm | 1.7049 | 58.11% | 100.00% | 90.00% | NA | NA |
| 13 | `v2_006_tcn_k12_mid` | supervised | seq_tcn | 1.7039 | 67.57% | 100.00% | 96.67% | NA | NA |
| 14 | `v2_018_transformer_k16` | supervised | seq_transformer | 1.7022 | 71.62% | 100.00% | 100.00% | NA | NA |
| 15 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 1.7018 | 63.51% | 100.00% | 93.33% | NA | NA |
| 16 | `v2_017_transformer_medium_k8` | supervised | seq_transformer | 1.7000 | 72.52% | 100.00% | 100.00% | NA | NA |
| 17 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 1.6828 | 68.47% | 100.00% | 96.67% | NA | NA |
| 18 | `v2_035_survival_tcn_k16` | supervised | seq_tcn | 1.6799 | 68.92% | 100.00% | 96.67% | NA | NA |
| 19 | `v2_012_lstm_k16_long` | supervised | seq_lstm | 1.6752 | 73.42% | 100.00% | 100.00% | NA | NA |
| 20 | `v2_005_tcn_k8_idea41` | supervised | seq_tcn | 1.6663 | 69.82% | 100.00% | 96.67% | NA | NA |
