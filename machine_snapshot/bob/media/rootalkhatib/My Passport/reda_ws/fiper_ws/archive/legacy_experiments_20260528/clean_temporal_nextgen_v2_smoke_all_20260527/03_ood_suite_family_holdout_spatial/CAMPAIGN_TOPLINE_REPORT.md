# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 0.9692 | 0.35% | 92.27% | 3.00% | NA | NA |
| 2 | `v2_012_lstm_k16_long` | supervised | seq_lstm | 0.9687 | 0.35% | 91.85% | 3.43% | NA | NA |
| 3 | `v2_022_tcn_k8_action_tokens_only` | supervised | seq_tcn | 0.9673 | 0.35% | 90.13% | 3.86% | NA | NA |
| 4 | `v2_013_lstm_k24_long` | supervised | seq_lstm | 0.9602 | 0.42% | 92.70% | 2.58% | NA | NA |
| 5 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 0.9575 | 0.35% | 91.85% | 2.58% | NA | NA |
| 6 | `v2_019_tcn_k8_no_current_proprio` | supervised | seq_tcn | 0.9541 | 0.42% | 91.85% | 2.58% | NA | NA |
| 7 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 0.9508 | 0.35% | 90.56% | 3.00% | NA | NA |
| 8 | `v2_014_gru_k8` | supervised | seq_gru | 0.9492 | 0.42% | 91.85% | 2.58% | NA | NA |
| 9 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 0.9434 | 0.35% | 90.56% | 2.58% | NA | NA |
| 10 | `v2_003_tcn_k4_short` | supervised | seq_tcn | 0.9417 | 0.35% | 90.99% | 2.58% | NA | NA |
| 11 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 0.9405 | 0.35% | 90.99% | 2.58% | NA | NA |
| 12 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 0.9398 | 0.35% | 88.84% | 3.43% | NA | NA |
| 13 | `v2_020_tcn_k8_no_current_ace` | supervised | seq_tcn | 0.9393 | 0.35% | 90.99% | 2.58% | NA | NA |
| 14 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 0.9312 | 0.35% | 89.70% | 2.58% | NA | NA |
| 15 | `v2_040_adv_target_tcn_k8` | supervised | seq_tcn | 0.9312 | 0.35% | 88.84% | 3.00% | NA | NA |
| 16 | `v2_001_tcn_k1_baseline` | supervised | seq_tcn | 0.9306 | 0.35% | 89.27% | 2.58% | NA | NA |
| 17 | `v2_004_tcn_k6_midshort` | supervised | seq_tcn | 0.9269 | 0.35% | 89.27% | 2.58% | NA | NA |
| 18 | `v2_028_tcn_k8_lowdrop` | supervised | seq_tcn | 0.9221 | 0.35% | 89.27% | 2.58% | NA | NA |
| 19 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 0.9205 | 0.28% | 82.40% | 5.15% | NA | NA |
| 20 | `v2_037_groupdro_target_tcn_k8` | supervised | seq_tcn | 0.9196 | 0.35% | 88.41% | 2.58% | NA | NA |
