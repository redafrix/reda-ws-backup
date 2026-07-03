# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 0.9986 | 83.20% | 100.00% | 74.68% |
| 2 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | 0.7685 | 92.32% | 100.00% | 69.96% |
| 3 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 0.7309 | 93.78% | 100.00% | 69.53% |
| 4 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 0.7171 | 89.42% | 99.57% | 65.67% |
| 5 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 0.6643 | 94.12% | 100.00% | 66.09% |
