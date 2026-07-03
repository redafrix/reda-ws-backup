# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | 1.2667 | 72.17% | 100.00% | 77.50% |
| 2 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 1.2644 | 79.25% | 100.00% | 82.50% |
| 3 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 1.1431 | 80.66% | 100.00% | 77.50% |
| 4 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.0002 | 80.19% | 100.00% | 70.00% |
| 5 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 0.9639 | 75.94% | 100.00% | 65.00% |
