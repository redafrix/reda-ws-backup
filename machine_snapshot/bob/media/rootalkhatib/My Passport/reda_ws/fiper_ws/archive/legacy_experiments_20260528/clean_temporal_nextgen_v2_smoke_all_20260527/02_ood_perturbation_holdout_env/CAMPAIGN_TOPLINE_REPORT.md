# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 2.9877 | 0.08% | 100.00% | 100.00% | NA | NA |
| 2 | `v2_009_tcn_k32_verylong` | supervised | seq_tcn | 1.6836 | 0.08% | 95.50% | 36.94% | NA | NA |
| 3 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 1.0359 | 0.25% | 76.58% | 14.41% | NA | NA |
| 4 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 0.9167 | 0.08% | 80.18% | 6.31% | NA | NA |
| 5 | `v2_014_gru_k8` | supervised | seq_gru | 0.8918 | 0.17% | 81.08% | 4.50% | NA | NA |
| 6 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 0.8895 | 0.17% | 86.49% | 1.80% | NA | NA |
| 7 | `v2_018_transformer_k16` | supervised | seq_transformer | 0.8826 | 0.25% | 80.18% | 4.50% | NA | NA |
| 8 | `v2_026_tcn_k8_seqstats_static` | supervised | seq_tcn | 0.8726 | 0.17% | 81.08% | 3.60% | NA | NA |
| 9 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 0.8636 | 0.17% | 80.18% | 3.60% | NA | NA |
| 10 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 0.8625 | 0.17% | 81.98% | 2.70% | NA | NA |
| 11 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 0.8613 | 0.25% | 80.18% | 3.60% | NA | NA |
| 12 | `v2_012_lstm_k16_long` | supervised | seq_lstm | 0.8559 | 0.08% | 75.68% | 5.41% | NA | NA |
| 13 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 0.8556 | 0.25% | 77.48% | 4.50% | NA | NA |
| 14 | `v2_015_gru_k16` | supervised | seq_gru | 0.8511 | 0.25% | 81.08% | 2.70% | NA | NA |
| 15 | `v2_003_tcn_k4_short` | supervised | seq_tcn | 0.8500 | 0.25% | 79.28% | 3.60% | NA | NA |
| 16 | `v2_042_dynamics_tcn_k8_pastdelta` | supervised | seq_tcn | 0.8500 | 0.25% | 77.48% | 4.50% | 0.00% | 8.11% |
| 17 | `v2_010_lstm_k4_short` | supervised | seq_lstm | 0.8467 | 0.17% | 80.18% | 2.70% | NA | NA |
| 18 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 0.8445 | 0.17% | 80.18% | 2.70% | NA | NA |
| 19 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 0.8410 | 0.25% | 78.38% | 3.60% | NA | NA |
| 20 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 0.8378 | 0.08% | 81.08% | 1.80% | NA | NA |
