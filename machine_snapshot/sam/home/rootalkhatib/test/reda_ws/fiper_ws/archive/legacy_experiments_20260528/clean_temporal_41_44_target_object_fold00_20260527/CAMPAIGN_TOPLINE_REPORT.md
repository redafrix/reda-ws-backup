# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.0773 | 58.29% | 100.00% | 57.14% |
| 2 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 1.0098 | 46.92% | 100.00% | 45.24% |
| 3 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 0.9445 | 48.34% | 100.00% | 42.86% |
| 4 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 0.8311 | 48.82% | 100.00% | 38.10% |
| 5 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | 0.8229 | 42.65% | 97.62% | 33.33% |
