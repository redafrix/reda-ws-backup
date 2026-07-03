# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 1.4950 | 100.00% | 100.00% | 100.00% | NA | NA |
| 2 | `v2_009_tcn_k32_verylong` | supervised | seq_tcn | 1.4950 | 100.00% | 100.00% | 100.00% | NA | NA |
| 3 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 0.3215 | 1.83% | 35.71% | 0.00% | NA | NA |
| 4 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 0.3135 | 1.83% | 35.00% | 0.00% | NA | NA |
| 5 | `v2_019_tcn_k8_no_current_proprio` | supervised | seq_tcn | 0.3040 | 0.61% | 32.14% | 0.00% | NA | NA |
| 6 | `v2_018_transformer_k16` | supervised | seq_transformer | 0.2869 | 3.66% | 35.00% | 0.00% | NA | NA |
| 7 | `v2_014_gru_k8` | supervised | seq_gru | 0.2720 | 7.93% | 40.00% | 0.00% | NA | NA |
| 8 | `v2_043_dynamics_survival_tcn_k8` | supervised | seq_tcn | 0.2683 | 0.61% | 28.57% | 0.00% | 0.00% | 0.00% |
| 9 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 0.2629 | 8.54% | 40.00% | 0.00% | NA | NA |
| 10 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 0.2609 | 6.71% | 37.14% | 0.00% | NA | NA |
| 11 | `v2_034_survival_lstm_k8` | supervised | seq_lstm | 0.2557 | 0.61% | 27.14% | 0.00% | NA | NA |
| 12 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 0.2471 | 4.88% | 32.86% | 0.00% | NA | NA |
| 13 | `v2_035_survival_tcn_k16` | supervised | seq_tcn | 0.2429 | 1.83% | 27.86% | 0.00% | NA | NA |
| 14 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 0.2414 | 8.54% | 37.86% | 0.00% | NA | NA |
| 15 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 0.2360 | 6.10% | 33.57% | 0.00% | NA | NA |
| 16 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 0.2260 | 6.71% | 33.57% | 0.00% | NA | NA |
| 17 | `v2_023_tcn_k8_history_only` | supervised | seq_tcn | 0.2236 | 0.00% | 22.86% | 0.00% | NA | NA |
| 18 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 0.2191 | 10.98% | 39.29% | 0.00% | NA | NA |
| 19 | `v2_025_tcn_k8_flat_action_static` | supervised | seq_tcn | 0.1989 | 10.37% | 36.43% | 0.00% | NA | NA |
| 20 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 0.1775 | 10.37% | 34.29% | 0.00% | NA | NA |
