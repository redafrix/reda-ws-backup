# Target-Object OOD 50-Experiment Campaign Report

This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `clean_044_lstm_k16_with_current_proprio` | supervised | seq_lstm | 1.4615 | 49.34% | 97.22% | 72.22% |
| 2 | `clean_041_tcn_k16_no_current_proprio` | supervised | seq_tcn | 1.3420 | 46.92% | 95.83% | 65.28% |
| 3 | `clean_044_lstm_k8_with_current_proprio` | supervised | seq_lstm | 1.3350 | 49.56% | 97.22% | 66.67% |
| 4 | `clean_041_tcn_k8_no_current_proprio` | supervised | seq_tcn | 1.3002 | 49.12% | 100.00% | 62.50% |
| 5 | `clean_041_tcn_k8_with_current_proprio` | supervised | seq_tcn | 1.2935 | 47.58% | 97.22% | 62.50% |
