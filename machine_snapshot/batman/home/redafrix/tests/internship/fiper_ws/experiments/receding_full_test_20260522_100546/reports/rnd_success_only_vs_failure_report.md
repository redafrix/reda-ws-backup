# RND Success-Only vs Failure Report

This report summarizes the training and evaluation of the Action-heavy Random Network Distillation (RND) safety monitor.

## Conformal Thresholds (Calibrated on `success_calib`)
- **q90**: 0.000264
- **q95**: 0.000322
- **q99**: 0.000824

## Split Evaluation & Alarm Rates
| Split | Count | Mean RND Score | Alarm @ q90 (%) | Alarm @ q95 (%) | Alarm @ q99 (%) |
|---|---|---|---|---|---|
| `success_train` | 3003 | 0.000095 | 0.53% | 0.03% | 0.00% |
| `success_calib` | 866 | 0.000159 | 10.05% | 5.08% | 1.04% |
| `success_test` | 1268 | 0.000172 | 11.04% | 6.86% | 1.74% |
| `ood_suite_success_test` | 1729 | 0.022752 | 100.00% | 100.00% | 97.46% |
| `failure_eval_all` | 9600 | 0.014331 | 72.23% | 69.79% | 66.07% |
| `failure_eval_early` | 2400 | 0.011665 | 70.42% | 68.96% | 65.79% |
| `failure_eval_late` | 2400 | 0.013969 | 73.25% | 70.88% | 67.00% |
| `failure_eval_near_end` | 1200 | 0.013372 | 72.83% | 70.83% | 66.67% |

## Model Diagnostic Audit
- **False Alarm Rate on success_test @ q95**: 6.86% (Target: 5.00%)
- **Alarm Rate on failure_eval_all @ q95**: 69.79%
- **Alarm Rate on failure_eval_late @ q95**: 70.88%
- **Alarm Rate on failure_eval_near_end @ q95**: 70.83%
- **Audit Status**: `NORMAL (selective alarm)`