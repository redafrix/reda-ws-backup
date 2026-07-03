# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_009_tcn_k32_verylong` | supervised | seq_tcn | 0.9236 | 0.60% | 92.75% | 1.04% | NA | NA |
| 2 | `v2_001_tcn_k1_baseline` | supervised | seq_tcn | 0.7967 | 0.70% | 77.72% | 2.07% | NA | NA |
| 3 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 0.7786 | 0.80% | 77.20% | 1.55% | NA | NA |
| 4 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 0.7697 | 0.70% | 75.13% | 2.07% | NA | NA |
| 5 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 0.7687 | 0.70% | 77.20% | 1.04% | NA | NA |
| 6 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 0.7656 | 0.70% | 75.65% | 1.55% | NA | NA |
| 7 | `v2_014_gru_k8` | supervised | seq_gru | 0.7651 | 0.80% | 75.65% | 1.55% | NA | NA |
| 8 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 0.7645 | 0.70% | 76.68% | 1.04% | NA | NA |
| 9 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 0.7614 | 0.70% | 75.13% | 1.55% | NA | NA |
| 10 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 0.7594 | 0.70% | 75.13% | 1.55% | NA | NA |
| 11 | `v2_019_tcn_k8_no_current_proprio` | supervised | seq_tcn | 0.7583 | 0.70% | 74.61% | 1.55% | NA | NA |
| 12 | `v2_012_lstm_k16_long` | supervised | seq_lstm | 0.7552 | 0.70% | 73.58% | 2.07% | NA | NA |
| 13 | `v2_010_lstm_k4_short` | supervised | seq_lstm | 0.7542 | 0.70% | 74.61% | 1.55% | NA | NA |
| 14 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 0.7542 | 0.70% | 75.65% | 1.04% | NA | NA |
| 15 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 0.7527 | 0.80% | 74.61% | 1.55% | NA | NA |
| 16 | `v2_042_dynamics_tcn_k8_pastdelta` | supervised | seq_tcn | 0.7521 | 0.70% | 75.65% | 1.04% | 0.00% | 1.55% |
| 17 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 0.7511 | 0.70% | 74.09% | 1.55% | NA | NA |
| 18 | `v2_003_tcn_k4_short` | supervised | seq_tcn | 0.7511 | 0.70% | 74.61% | 1.55% | NA | NA |
| 19 | `v2_015_gru_k16` | supervised | seq_gru | 0.7496 | 0.80% | 75.13% | 1.04% | NA | NA |
| 20 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 0.7496 | 0.80% | 75.13% | 1.04% | NA | NA |
