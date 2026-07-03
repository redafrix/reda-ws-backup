# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_003_tcn_k4_short` | supervised | seq_tcn | 0.5725 | 1.42% | 55.84% | 2.16% | NA | NA |
| 2 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 0.5684 | 0.83% | 56.28% | 1.30% | NA | NA |
| 3 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 0.5636 | 1.66% | 53.68% | 3.03% | NA | NA |
| 4 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 0.5587 | 1.18% | 55.84% | 1.30% | NA | NA |
| 5 | `v2_017_transformer_medium_k8` | supervised | seq_transformer | 0.5554 | 0.83% | 52.38% | 2.60% | NA | NA |
| 6 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 0.5509 | 0.71% | 55.41% | 0.87% | NA | NA |
| 7 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 0.5489 | 1.42% | 56.28% | 0.87% | NA | NA |
| 8 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 0.5294 | 0.83% | 51.52% | 1.73% | NA | NA |
| 9 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 0.5251 | 0.83% | 49.35% | 2.60% | NA | NA |
| 10 | `v2_015_gru_k16` | supervised | seq_gru | 0.5216 | 0.71% | 50.65% | 1.73% | NA | NA |
| 11 | `v2_026_tcn_k8_seqstats_static` | supervised | seq_tcn | 0.5216 | 0.71% | 50.65% | 1.73% | NA | NA |
| 12 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 0.5216 | 0.71% | 52.38% | 0.87% | NA | NA |
| 13 | `v2_006_tcn_k12_mid` | supervised | seq_tcn | 0.5196 | 1.07% | 52.81% | 0.87% | NA | NA |
| 14 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 0.5194 | 1.30% | 52.38% | 1.30% | NA | NA |
| 15 | `v2_024_tcn_k8_first_action_static` | supervised | seq_tcn | 0.5180 | 0.95% | 52.38% | 0.87% | NA | NA |
| 16 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 0.5172 | 1.07% | 51.52% | 1.30% | NA | NA |
| 17 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 0.5139 | 0.71% | 50.65% | 1.30% | NA | NA |
| 18 | `v2_012_lstm_k16_long` | supervised | seq_lstm | 0.5111 | 0.83% | 50.65% | 1.30% | NA | NA |
| 19 | `v2_005_tcn_k8_idea41` | supervised | seq_tcn | 0.5091 | 1.18% | 51.08% | 1.30% | NA | NA |
| 20 | `v2_018_transformer_k16` | supervised | seq_transformer | 0.5068 | 0.83% | 49.35% | 1.73% | NA | NA |
