# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 1.1690 | 68.84% | 98.70% | 70.56% |
| 2 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 1.0949 | 70.50% | 98.70% | 68.40% |
| 3 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.0941 | 68.72% | 98.70% | 66.23% |
| 4 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 1.0059 | 69.43% | 98.27% | 62.77% |
| 5 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | 0.7134 | 67.77% | 98.27% | 46.75% |
