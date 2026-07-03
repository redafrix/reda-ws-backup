# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `v2_027_tcn_k8_wide256` | supervised | seq_tcn | 1.2736 | 54.98% | 100.00% | 64.29% | NA | NA |
| 2 | `v2_004_tcn_k6_midshort` | supervised | seq_tcn | 1.1276 | 48.34% | 100.00% | 52.38% | NA | NA |
| 3 | `v2_031_tcn_k8_pos2` | supervised | seq_tcn | 1.0958 | 50.71% | 100.00% | 52.38% | NA | NA |
| 4 | `v2_032_tcn_k8_label_smooth` | supervised | seq_tcn | 1.0695 | 49.29% | 100.00% | 50.00% | NA | NA |
| 5 | `v2_026_tcn_k8_seqstats_static` | supervised | seq_tcn | 1.0682 | 46.45% | 100.00% | 47.62% | NA | NA |
| 6 | `v2_041_adv_perturb_tcn_k8` | supervised | seq_tcn | 1.0615 | 55.92% | 100.00% | 54.76% | NA | NA |
| 7 | `v2_017_transformer_medium_k8` | supervised | seq_transformer | 1.0277 | 45.97% | 100.00% | 45.24% | NA | NA |
| 8 | `v2_001_tcn_k1_baseline` | supervised | seq_tcn | 1.0253 | 48.82% | 100.00% | 47.62% | NA | NA |
| 9 | `v2_019_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.0124 | 52.61% | 100.00% | 50.00% | NA | NA |
| 10 | `v2_016_transformer_small_k8` | supervised | seq_transformer | 1.0027 | 47.39% | 100.00% | 45.24% | NA | NA |
| 11 | `v2_030_tcn_k8_focal` | supervised | seq_tcn | 1.0018 | 53.55% | 100.00% | 50.00% | NA | NA |
| 12 | `v2_044_transformer_k8_focal` | supervised | seq_transformer | 0.9947 | 54.03% | 100.00% | 50.00% | NA | NA |
| 13 | `v2_021_tcn_k8_no_ace_history` | supervised | seq_tcn | 0.9755 | 52.13% | 100.00% | 47.62% | NA | NA |
| 14 | `v2_002_tcn_k2_short` | supervised | seq_tcn | 0.9740 | 48.82% | 100.00% | 45.24% | NA | NA |
| 15 | `v2_008_tcn_k24_long` | supervised | seq_tcn | 0.9740 | 48.82% | 100.00% | 45.24% | NA | NA |
| 16 | `v2_014_gru_k8` | supervised | seq_gru | 0.9708 | 49.76% | 100.00% | 45.24% | NA | NA |
| 17 | `v2_005_tcn_k8_idea41` | supervised | seq_tcn | 0.9693 | 46.45% | 100.00% | 42.86% | NA | NA |
| 18 | `v2_033_survival_tcn_k8` | supervised | seq_tcn | 0.9669 | 49.29% | 100.00% | 45.24% | NA | NA |
| 19 | `v2_043_dynamics_survival_tcn_k8` | supervised | seq_tcn | 0.9600 | 50.24% | 100.00% | 45.24% | 0.95% | 54.76% |
| 20 | `v2_042_dynamics_tcn_k8_pastdelta` | supervised | seq_tcn | 0.9374 | 48.82% | 100.00% | 42.86% | 3.79% | 61.90% |
