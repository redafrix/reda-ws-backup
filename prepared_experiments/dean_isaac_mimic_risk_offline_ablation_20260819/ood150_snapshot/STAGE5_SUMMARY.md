# Stage 5 Summary — Frozen Historical OOD150 Transfer

## 1. Compatibility & Integrity Gate
- Source Root: /mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728
- Total Episodes: 150 (72 success / 78 failure)
- Total Decision Rows: 5887
- C0 Recurrence Worst Max Abs: 0.000e+00
- Compatibility Status: PASSED

## 2. Primary Predeclared Result (Seed 0, Conformal Alpha=0.10)
- Threshold: 0.736110
- Row AUROC: 0.772397
- Row AUPRC: 0.903282
- Success False Alarms: 72/72 (100.00%)
- Failure Detection: 78/78 (100.00%)
- Det@10: 78/78 (100.00%)
- Det@25: 78/78 (100.00%)
- Det@50: 78/78 (100.00%)
- Never Detected: 0/78
- Mean Detection Fraction: 0.0209

## 3. Robustness Across All 5 Seeds (Conformal Alpha=0.10)
| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| Seed 0 | 0.7724 | 0.9033 | 72/72 (100.00%) | 78/78 (100.00%) | 78/78 (100.00%) | 78/78 (100.00%) |
| Seed 1 | 0.5145 | 0.8076 | 71/72 (98.61%) | 78/78 (100.00%) | 75/78 (96.15%) | 76/78 (97.44%) |
| Seed 2 | 0.5332 | 0.8061 | 71/72 (98.61%) | 78/78 (100.00%) | 77/78 (98.72%) | 78/78 (100.00%) |
| Seed 3 | 0.5423 | 0.8251 | 71/72 (98.61%) | 78/78 (100.00%) | 75/78 (96.15%) | 77/78 (98.72%) |
| Seed 4 | 0.6163 | 0.8640 | 71/72 (98.61%) | 78/78 (100.00%) | 77/78 (98.72%) | 78/78 (100.00%) |

- Mean Row AUROC: 0.5957 +/- 0.0949
- Mean Row AUPRC: 0.8412 +/- 0.0374
- Mean FA Percent: 98.89% +/- 0.56%
- Mean Failure Detection: 100.00% +/- 0.00%
- Mean Det@25: 97.95% +/- 1.54%
- Mean Det@50: 99.23% +/- 1.03%

## 4. Full Operating Point Table (Seed 0)
| Operating Point | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| fixed_0.5 | 0.5000 | 72/72 | 78/78 | 78/78 | 78/78 | 78/78 |
| conformal_alpha_0.05 | 0.8860 | 72/72 | 78/78 | 75/78 | 78/78 | 78/78 |
| conformal_alpha_0.10 | 0.7361 | 72/72 | 78/78 | 78/78 | 78/78 | 78/78 |
| conformal_alpha_0.15 | 0.5655 | 72/72 | 78/78 | 78/78 | 78/78 | 78/78 |
| empirical_q90 | 0.7273 | 72/72 | 78/78 | 78/78 | 78/78 | 78/78 |
| empirical_q95 | 0.8806 | 72/72 | 78/78 | 76/78 | 78/78 | 78/78 |
| empirical_q99 | 0.9846 | 72/72 | 78/78 | 74/78 | 78/78 | 78/78 |
| row_best_f1 | 0.9380 | 72/72 | 78/78 | 75/78 | 78/78 | 78/78 |
