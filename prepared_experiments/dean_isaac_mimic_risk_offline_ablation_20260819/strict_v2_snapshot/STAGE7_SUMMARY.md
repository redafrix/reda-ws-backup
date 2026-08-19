# Stage 7 Summary — Strict Mimic Fidelity V2 Held-Out Seen Evaluation

## 1. Primary Result (Seed 0, Conformal Alpha=0.10)
- Threshold: 0.628429
- Row AUROC: 0.873869
- Row AUPRC: 0.730364
- Success False Alarms: 51/586 (8.70%)
- Failure Detection: 14/14 (100.00%)
- Det@10: 0/14 (0.00%)
- Det@25: 3/14 (21.43%)
- Det@50: 14/14 (100.00%)
- Never Detected: 0/14
- Mean Detection Fraction: 0.3333

## 2. Robustness Across All 5 Seeds (Conformal Alpha=0.10)
| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| Seed 0 | 0.8739 | 0.7304 | 51/586 (8.70%) | 14/14 (100.00%) | 3/14 (21.43%) | 14/14 (100.00%) |
| Seed 1 | 0.8903 | 0.7344 | 57/586 (9.73%) | 14/14 (100.00%) | 0/14 (0.00%) | 12/14 (85.71%) |
| Seed 2 | 0.8656 | 0.6787 | 42/586 (7.17%) | 14/14 (100.00%) | 5/14 (35.71%) | 14/14 (100.00%) |
| Seed 3 | 0.8635 | 0.6745 | 38/586 (6.48%) | 14/14 (100.00%) | 2/14 (14.29%) | 14/14 (100.00%) |
| Seed 4 | 0.8610 | 0.7148 | 37/586 (6.31%) | 14/14 (100.00%) | 2/14 (14.29%) | 14/14 (100.00%) |

- Mean Row AUROC: 0.8708 +/- 0.0107
- Mean Row AUPRC: 0.7066 +/- 0.0254
- Mean FA Percent: 7.68% +/- 1.33%
- Mean Failure Detection: 100.00% +/- 0.00%
- Mean Det@25: 17.14% +/- 11.61%
- Mean Det@50: 97.14% +/- 5.71%

## 3. Matched TopK8 Comparison (Row Best-F1)
- TopK8 AUROC: 0.9311 | Strict V2 Seed0 AUROC: 0.8739 (Delta: -0.0572)
- TopK8 AUPRC: 0.8186 | Strict V2 Seed0 AUPRC: 0.7304 (Delta: -0.0883)
- TopK8 Best-F1 FA: 12/586 (2.05%) | Strict V2 Best-F1 FA: 5/586 (0.85%)
- TopK8 Best-F1 Det@25: 5/14 (35.71%) | Strict V2 Best-F1 Det@25: 0/14 (0.00%)
