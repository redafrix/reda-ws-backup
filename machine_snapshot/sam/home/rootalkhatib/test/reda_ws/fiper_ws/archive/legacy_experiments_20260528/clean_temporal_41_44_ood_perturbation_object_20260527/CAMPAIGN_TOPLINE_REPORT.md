# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 2.0263 | 22.35% | 97.60% | 78.40% |
| 2 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 2.0002 | 23.72% | 97.60% | 78.40% |
| 3 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.9678 | 21.06% | 97.60% | 74.40% |
| 4 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 1.9618 | 22.60% | 97.60% | 75.20% |
| 5 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | 1.8868 | 22.95% | 98.40% | 71.20% |
