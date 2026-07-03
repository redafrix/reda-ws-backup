# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `ng_041_tcn_k8_score_only` | supervised | seq_tcn | 1.2120 | 60.87% | 100.00% | 64.29% | 0.00% | 7.14% |
| 2 | `ng_groupdro_tcn_k8` | supervised | seq_tcn | 1.2120 | 60.87% | 100.00% | 64.29% | 0.00% | 42.86% |
| 3 | `ng_adversarial_tcn_k8` | supervised | seq_tcn | 1.2120 | 60.87% | 100.00% | 64.29% | 0.00% | 7.14% |
| 4 | `ng_dynamics_tcn_k8` | supervised | seq_tcn | 1.2120 | 60.87% | 100.00% | 64.29% | 0.00% | 7.14% |
| 5 | `ng_044_lstm_k8_score_only` | supervised | seq_lstm | 1.1941 | 60.87% | 100.00% | 64.29% | 0.00% | 0.00% |
| 6 | `ng_survival_tcn_k8` | supervised | seq_tcn | 1.1941 | 60.87% | 100.00% | 64.29% | 0.00% | 0.00% |
| 7 | `ng_survival_lstm_k8` | supervised | seq_lstm | 1.1762 | 60.87% | 100.00% | 64.29% | 0.00% | 7.14% |
