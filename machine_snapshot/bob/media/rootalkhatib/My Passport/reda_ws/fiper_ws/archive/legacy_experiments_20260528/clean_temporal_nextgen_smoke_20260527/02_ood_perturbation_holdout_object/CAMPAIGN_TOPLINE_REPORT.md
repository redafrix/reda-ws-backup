# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `ng_041_tcn_k8_score_only` | supervised | seq_tcn | 1.3706 | 52.94% | 100.00% | 71.43% | 2.94% | 78.57% |
| 2 | `ng_dynamics_tcn_k8` | supervised | seq_tcn | 1.2277 | 52.94% | 100.00% | 64.29% | 0.00% | 42.86% |
| 3 | `ng_groupdro_tcn_k8` | supervised | seq_tcn | 1.2138 | 52.94% | 100.00% | 64.29% | 2.94% | 78.57% |
| 4 | `ng_adversarial_tcn_k8` | supervised | seq_tcn | 1.1999 | 52.94% | 100.00% | 64.29% | 2.94% | 78.57% |
| 5 | `ng_044_lstm_k8_score_only` | supervised | seq_lstm | 1.0849 | 52.94% | 100.00% | 57.14% | 2.94% | 85.71% |
| 6 | `ng_survival_tcn_k8` | supervised | seq_tcn | 1.0710 | 52.94% | 100.00% | 57.14% | 0.00% | 64.29% |
| 7 | `ng_survival_lstm_k8` | supervised | seq_lstm | 1.0710 | 52.94% | 100.00% | 57.14% | 0.00% | 78.57% |
