# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 0.9506 | 91.46% | 97.86% | 77.14% |
| 2 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 0.7026 | 97.56% | 100.00% | 68.57% |
| 3 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 0.6217 | 94.51% | 97.86% | 62.86% |
| 4 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 0.4793 | 96.95% | 99.29% | 57.14% |
| 5 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | -0.0635 | 92.07% | 96.43% | 27.86% |
