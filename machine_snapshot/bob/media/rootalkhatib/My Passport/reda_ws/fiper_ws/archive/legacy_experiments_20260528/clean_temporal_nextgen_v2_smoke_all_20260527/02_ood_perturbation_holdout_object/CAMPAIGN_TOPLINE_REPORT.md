# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 2.9934 | 0.00% | 100.00% | 100.00% | NA | NA |
| 2 | `v2_009_tcn_k32_verylong` | supervised | seq_tcn | 1.4005 | 0.00% | 85.60% | 28.00% | NA | NA |
| 3 | `v2_014_gru_k8` | supervised | seq_gru | 1.0025 | 0.09% | 80.80% | 10.40% | NA | NA |
| 4 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 0.9899 | 0.17% | 84.80% | 8.00% | NA | NA |
| 5 | `v2_036_survival_tcn_k8_focal` | supervised | seq_tcn | 0.9843 | 0.09% | 80.80% | 9.60% | NA | NA |
| 6 | `v2_026_tcn_k8_seqstats_static` | supervised | seq_tcn | 0.9660 | 0.00% | 83.20% | 7.20% | NA | NA |
| 7 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 0.9488 | 0.09% | 68.80% | 13.60% | NA | NA |
| 8 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 0.9454 | 0.09% | 83.20% | 6.40% | NA | NA |
| 9 | `v2_022_tcn_k8_action_tokens_only` | supervised | seq_tcn | 0.9249 | 0.00% | 58.40% | 17.60% | NA | NA |
| 10 | `v2_011_lstm_k8_idea44` | supervised | seq_lstm | 0.9169 | 0.00% | 76.80% | 8.00% | NA | NA |
| 11 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 0.9168 | 0.09% | 80.00% | 6.40% | NA | NA |
| 12 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 0.9157 | 0.09% | 78.40% | 7.20% | NA | NA |
| 13 | `v2_038_groupdro_perturb_tcn_k8` | supervised | seq_tcn | 0.9088 | 0.09% | 82.40% | 4.80% | NA | NA |
| 14 | `v2_025_tcn_k8_flat_action_static` | supervised | seq_tcn | 0.9073 | 0.26% | 79.20% | 6.40% | NA | NA |
| 15 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 0.9065 | 0.09% | 79.20% | 6.40% | NA | NA |
| 16 | `v2_037_groupdro_target_tcn_k8` | supervised | seq_tcn | 0.9065 | 0.09% | 79.20% | 6.40% | NA | NA |
| 17 | `v2_015_gru_k16` | supervised | seq_gru | 0.9040 | 0.26% | 80.80% | 5.60% | NA | NA |
| 18 | `v2_029_tcn_k8_highdrop` | supervised | seq_tcn | 0.9031 | 0.17% | 79.20% | 6.40% | NA | NA |
| 19 | `v2_010_lstm_k4_short` | supervised | seq_lstm | 0.8998 | 0.00% | 78.40% | 6.40% | NA | NA |
| 20 | `v2_018_transformer_k16` | supervised | seq_transformer | 0.8997 | 0.09% | 72.00% | 9.60% | NA | NA |
