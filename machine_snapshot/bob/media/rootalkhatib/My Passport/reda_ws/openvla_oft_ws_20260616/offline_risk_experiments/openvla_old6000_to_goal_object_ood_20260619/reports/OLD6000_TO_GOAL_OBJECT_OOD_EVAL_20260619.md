# Old-6000 OpenVLA Risk Model Cross-Dataset OOD Evaluation
## Setup
- Training source/model: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_risk_base_20260617`
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
| `best_val_f1` | 0.7100 | 0.9953 | 0.9909 | 0.9609 | 0.38% | 6.18% | 4.76% (42/883) | 100.00% (33/33) | 100.00% (33/33) |
| `q95` | 0.1950 | 0.9953 | 0.9909 | 0.9129 | 4.61% | 1.33% | 30.01% (265/883) | 100.00% (33/33) | 100.00% (33/33) |
| `q99` | 0.5780 | 0.9953 | 0.9909 | 0.9573 | 1.03% | 4.61% | 9.17% (81/883) | 100.00% (33/33) | 100.00% (33/33) |
| `fixed_0.5` | 0.5000 | 0.9953 | 0.9909 | 0.9539 | 1.40% | 3.97% | 12.68% (112/883) | 100.00% (33/33) | 100.00% (33/33) |

### `goal_object_ood_all1890`

| Threshold | Value | AUROC | AUPRC | Step F1 | Step FPR | Step FNR | Episode false alarms | Episode failure detected | Failure detected by first 25% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `best_val_f1` | 0.7100 | 0.8302 | 0.9789 | 0.8409 | 9.14% | 26.69% | 15.63% (123/787) | 100.00% (1103/1103) | 83.14% (917/1103) |
| `q95` | 0.1950 | 0.8302 | 0.9789 | 0.8546 | 17.16% | 23.93% | 49.94% (393/787) | 100.00% (1103/1103) | 83.14% (917/1103) |
| `q99` | 0.5780 | 0.8302 | 0.9789 | 0.8440 | 10.38% | 26.13% | 22.24% (175/787) | 100.00% (1103/1103) | 83.14% (917/1103) |
| `fixed_0.5` | 0.5000 | 0.8302 | 0.9789 | 0.8460 | 11.30% | 25.74% | 27.06% (213/787) | 100.00% (1103/1103) | 83.14% (917/1103) |

## External OOD Per-Task Results At Old Validation Q95

| Task | Success eps | Failure eps | AUROC | AUPRC | Episode FA | Failure detected |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 177 | 12 | 0.6977 | 0.4357 | 19.21% | 100.00% |
| 1 | 35 | 154 | 0.8464 | 0.9920 | 100.00% | 100.00% |
| 2 | 0 | 189 | NA | NA | NA | 100.00% |
| 3 | 37 | 152 | 0.8925 | 0.9945 | 100.00% | 100.00% |
| 4 | 1 | 188 | 0.8947 | 0.9999 | 100.00% | 100.00% |
| 5 | 189 | 0 | NA | NA | 83.60% | NA |
| 6 | 34 | 155 | 0.7682 | 0.9852 | 44.12% | 100.00% |
| 7 | 189 | 0 | NA | NA | 0.00% | NA |
| 8 | 125 | 64 | 0.8245 | 0.9571 | 90.40% | 100.00% |
| 9 | 0 | 189 | NA | NA | NA | 100.00% |

## Interpretation

- This is a strict cross-dataset test: old plain `libero_goal` training/calibration, then external `libero_goal_object` evaluation without threshold tuning.
- If external OOD episode false alarms are high, that means the old goal-only risk model does not transfer cleanly as an online alarm policy to goal-object, even if AUROC remains useful for ranking.
- If external OOD failure detection remains high but false alarms rise, the model is detecting difficulty, but its old thresholds are not deployment-calibrated for the goal-object distribution.
