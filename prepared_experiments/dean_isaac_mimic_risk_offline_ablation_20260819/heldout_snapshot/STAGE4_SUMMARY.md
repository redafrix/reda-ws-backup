# Stage 4 Summary — One-Time Held-Out Seen Evaluation

## 1. Primary Predeclared Result (Seed 0, Conformal Alpha=0.10)
- Threshold: 0.736110
- Row AUROC: 0.917093
- Row AUPRC: 0.808009
- Success False Alarms: 43/586 (7.34%)
- Failure Detection: 14/14 (100.00%)
- Det@10: 4/14 (28.57%)
- Det@25: 8/14 (57.14%)
- Det@50: 14/14 (100.00%)
- Never Detected: 0/14
- Mean Detection Fraction: 0.2036

## 2. Robustness Across All 5 Seeds (Conformal Alpha=0.10)
| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| Seed 0 | 0.9171 | 0.8080 | 43/586 (7.34%) | 14/14 (100.00%) | 8/14 (57.14%) | 14/14 (100.00%) |
| Seed 1 | 0.8919 | 0.7293 | 58/586 (9.90%) | 14/14 (100.00%) | 6/14 (42.86%) | 14/14 (100.00%) |
| Seed 2 | 0.9004 | 0.7640 | 54/586 (9.22%) | 14/14 (100.00%) | 5/14 (35.71%) | 14/14 (100.00%) |
| Seed 3 | 0.8986 | 0.7541 | 56/586 (9.56%) | 14/14 (100.00%) | 5/14 (35.71%) | 14/14 (100.00%) |
| Seed 4 | 0.8992 | 0.7586 | 59/586 (10.07%) | 14/14 (100.00%) | 7/14 (50.00%) | 14/14 (100.00%) |

- Mean Row AUROC: 0.9014 +/- 0.0084
- Mean Row AUPRC: 0.7628 +/- 0.0255
- Mean FA Percent: 9.22% +/- 0.98%
- Mean Failure Detection: 100.00% +/- 0.00%
- Mean Det@25: 44.29% +/- 8.33%
- Mean Det@50: 100.00% +/- 0.00%

## 3. Full Operating Point Table (Seed 0)
| Operating Point | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| fixed_0.5 | 0.5000 | 94/586 | 14/14 | 6/14 | 10/14 | 14/14 |
| conformal_alpha_0.05 | 0.8860 | 24/586 | 14/14 | 1/14 | 5/14 | 14/14 |
| conformal_alpha_0.10 | 0.7361 | 43/586 | 14/14 | 4/14 | 8/14 | 14/14 |
| conformal_alpha_0.15 | 0.5655 | 77/586 | 14/14 | 6/14 | 10/14 | 14/14 |
| empirical_q90 | 0.7273 | 44/586 | 14/14 | 4/14 | 8/14 | 14/14 |
| empirical_q95 | 0.8806 | 24/586 | 14/14 | 1/14 | 5/14 | 14/14 |
| empirical_q99 | 0.9846 | 8/586 | 14/14 | 0/14 | 3/14 | 14/14 |
| row_best_f1 | 0.9380 | 17/586 | 14/14 | 1/14 | 5/14 | 14/14 |
