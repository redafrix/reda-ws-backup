# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_015_gru_k16` | supervised | seq_gru | 1.3959 | 76.89% | 100.00% | 87.50% | NA | NA |
| 2 | `v2_007_tcn_k16_long` | supervised | seq_tcn | 1.3667 | 72.17% | 100.00% | 82.50% | NA | NA |
| 3 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 1.3648 | 85.38% | 100.00% | 92.50% | NA | NA |
| 4 | `v2_019_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.3436 | 83.96% | 100.00% | 90.00% | NA | NA |
| 5 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 1.3426 | 83.02% | 100.00% | 90.00% | NA | NA |
| 6 | `v2_035_survival_tcn_k16` | supervised | seq_tcn | 1.3181 | 82.08% | 100.00% | 87.50% | NA | NA |
| 7 | `v2_018_transformer_k16` | supervised | seq_transformer | 1.3157 | 68.40% | 100.00% | 77.50% | NA | NA |
| 8 | `v2_014_gru_k8` | supervised | seq_gru | 1.3007 | 83.49% | 100.00% | 87.50% | NA | NA |
| 9 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 1.2926 | 80.19% | 100.00% | 85.00% | NA | NA |
| 10 | `v2_043_dynamics_survival_tcn_k8` | supervised | seq_tcn | 1.2903 | 90.09% | 100.00% | 92.50% | 0.00% | 75.00% |
| 11 | `v2_039_groupdro_suitefam_tcn_k8` | supervised | seq_tcn | 1.2851 | 77.36% | 100.00% | 82.50% | NA | NA |
| 12 | `v2_006_tcn_k12_mid` | supervised | seq_tcn | 1.2757 | 84.91% | 100.00% | 87.50% | NA | NA |
| 13 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 1.2662 | 71.70% | 100.00% | 77.50% | NA | NA |
| 14 | `v2_025_tcn_k8_flat_action_static` | supervised | seq_tcn | 1.2426 | 83.02% | 100.00% | 85.00% | NA | NA |
| 15 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 1.2393 | 80.66% | 100.00% | 82.50% | NA | NA |
| 16 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 1.2044 | 89.15% | 100.00% | 87.50% | NA | NA |
| 17 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 1.2035 | 79.72% | 100.00% | 80.00% | NA | NA |
| 18 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 1.2035 | 79.72% | 100.00% | 80.00% | NA | NA |
| 19 | `v2_024_tcn_k8_first_action_static` | supervised | seq_tcn | 1.1893 | 80.66% | 100.00% | 80.00% | NA | NA |
| 20 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 1.1812 | 83.02% | 100.00% | 82.50% | NA | NA |
