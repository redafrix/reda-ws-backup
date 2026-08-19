# Stage 1 Summary — isaac_mimic_h10_strict_3cm350_seen4904_v3 Held-Out Test Evaluation

## 1. Primary Result (Seed 0, Conformal Alpha=0.10)
- Threshold: 0.890776
- Row AUROC: 0.801239
- Row AUPRC: 0.669797
- Success False Alarms: 66/658 (10.03%)
- Failure Detection: 77/78 (98.72%)
- Det@10: 0/78 (0.00%)
- Det@25: 0/78 (0.00%)
- Det@50: 27/78 (34.62%)
- Never Detected: 1/78
- Mean Detection Fraction: 0.5210

## 2. Robustness Across All 5 Seeds (Conformal Alpha=0.10)
| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| Seed 0 | 0.8012 | 0.6698 | 66/658 (10.03%) | 77/78 (98.72%) | 0/78 (0.00%) | 27/78 (34.62%) |
| Seed 1 | 0.7925 | 0.6657 | 64/658 (9.73%) | 78/78 (100.00%) | 0/78 (0.00%) | 26/78 (33.33%) |
| Seed 2 | 0.8897 | 0.8183 | 45/658 (6.84%) | 78/78 (100.00%) | 32/78 (41.03%) | 58/78 (74.36%) |
| Seed 3 | 0.7869 | 0.6593 | 53/658 (8.05%) | 78/78 (100.00%) | 0/78 (0.00%) | 18/78 (23.08%) |
| Seed 4 | 0.7856 | 0.6608 | 54/658 (8.21%) | 77/78 (98.72%) | 1/78 (1.28%) | 26/78 (33.33%) |

- Mean Row AUROC: 0.8112 +/- 0.0397
- Mean Row AUPRC: 0.6948 +/- 0.0619
- Mean FA Percent: 8.57% +/- 1.17%
- Mean Failure Detection: 99.49% +/- 0.63%
- Mean Det@25: 8.46% +/- 16.29%
- Mean Det@50: 39.74% +/- 17.80%

## 3. Matched TopK8 Comparison
- TopK8 AUROC: 0.9408 | Mimic Seed0 AUROC: 0.8012 (Delta: -0.1395)
- TopK8 AUPRC: 0.8748 | Mimic Seed0 AUPRC: 0.6698 (Delta: -0.2050)
- TopK8 Best-F1 FA: 50/658 (7.60%) | Mimic Best-F1 FA: 243/658 (36.93%)
- TopK8 Best-F1 Det: 78/78 (100.00%) | Mimic Best-F1 Det: 78/78 (100.00%)
