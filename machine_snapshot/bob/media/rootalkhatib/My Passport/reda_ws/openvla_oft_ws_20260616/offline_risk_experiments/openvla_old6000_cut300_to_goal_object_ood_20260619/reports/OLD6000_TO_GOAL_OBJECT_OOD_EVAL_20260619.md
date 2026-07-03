# Old-6000 OpenVLA Risk Model Cross-Dataset OOD Evaluation
## Setup
- Training source/model: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_risk_base_20260617_cut300`
- In-domain test dataset: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded` using old heldout test split only
- External OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618` using all complete 1890 goal-object episodes
- Evaluation only: CPU inference, no online rollout process touched.
- Model: old-6000 `SeqRiskModel` Transformer, `K=16`, action padded to `[10, 7]`, static dim `43`.
- Thresholds are the old-6000 validation thresholds, so the external OOD dataset is not used for calibration.

## Dataset Counts

| Dataset | Episodes | Success eps | Failure eps | Query rows |
|---|---:|---:|---:|---:|
| `old6000_test_id` | 916 | 883 | 33 | 15814 |
| `goal_object_ood_all1890` | 1890 | 787 | 1103 | 122839 |

## Threshold Results

### `old6000_test_id`

| Threshold | Value | AUROC | AUPRC | Step F1 | Step FPR | Step FNR | Episode false alarms | Episode failure detected | Failure detected by first 25% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `best_val_f1` | 0.8700 | 0.9270 | 0.9236 | 0.9108 | 0.46% | 14.91% | 2.94% (26/883) | 100.00% (33/33) | 100.00% (33/33) |
| `q95` | 0.3725 | 0.9270 | 0.9236 | 0.8623 | 4.59% | 11.00% | 32.84% (290/883) | 100.00% (33/33) | 100.00% (33/33) |
| `q99` | 0.7921 | 0.9270 | 0.9236 | 0.9109 | 0.74% | 14.03% | 5.78% (51/883) | 100.00% (33/33) | 100.00% (33/33) |
| `fixed_0.5` | 0.5000 | 0.9270 | 0.9236 | 0.8834 | 3.08% | 11.64% | 25.14% (222/883) | 100.00% (33/33) | 100.00% (33/33) |

### `goal_object_ood_all1890`

| Threshold | Value | AUROC | AUPRC | Step F1 | Step FPR | Step FNR | Episode false alarms | Episode failure detected | Failure detected by first 25% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `best_val_f1` | 0.8700 | 0.6782 | 0.9562 | 0.6856 | 9.96% | 47.25% | 22.11% (174/787) | 84.50% (932/1103) | 80.24% (885/1103) |
| `q95` | 0.3725 | 0.6782 | 0.9562 | 0.7256 | 16.07% | 42.03% | 48.41% (381/787) | 86.31% (952/1103) | 82.14% (906/1103) |
| `q99` | 0.7921 | 0.6782 | 0.9562 | 0.7011 | 10.44% | 45.39% | 24.02% (189/787) | 84.86% (936/1103) | 80.24% (885/1103) |
| `fixed_0.5` | 0.5000 | 0.6782 | 0.9562 | 0.7191 | 13.54% | 43.00% | 45.24% (356/787) | 85.95% (948/1103) | 81.78% (902/1103) |

## External OOD Per-Task Results At Old Validation Q95

| Task | Success eps | Failure eps | AUROC | AUPRC | Episode FA | Failure detected |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 177 | 12 | 0.7097 | 0.4365 | 29.38% | 100.00% |
| 1 | 35 | 154 | 0.7354 | 0.9846 | 100.00% | 100.00% |
| 2 | 0 | 189 | NA | NA | NA | 100.00% |
| 3 | 37 | 152 | 0.7355 | 0.9832 | 78.38% | 100.00% |
| 4 | 1 | 188 | 0.8353 | 0.9998 | 100.00% | 100.00% |
| 5 | 189 | 0 | NA | NA | 74.07% | NA |
| 6 | 34 | 155 | 0.6708 | 0.9776 | 52.94% | 100.00% |
| 7 | 189 | 0 | NA | NA | 0.00% | NA |
| 8 | 125 | 64 | 0.8178 | 0.9546 | 84.80% | 100.00% |
| 9 | 0 | 189 | NA | NA | NA | 20.11% |

## Interpretation

- This is a strict cross-dataset test: old plain `libero_goal` training/calibration, then external `libero_goal_object` evaluation without threshold tuning.
- If external OOD episode false alarms are high, that means the old goal-only risk model does not transfer cleanly as an online alarm policy to goal-object, even if AUROC remains useful for ranking.
- If external OOD failure detection remains high but false alarms rise, the model is detecting difficulty, but its old thresholds are not deployment-calibrated for the goal-object distribution.
