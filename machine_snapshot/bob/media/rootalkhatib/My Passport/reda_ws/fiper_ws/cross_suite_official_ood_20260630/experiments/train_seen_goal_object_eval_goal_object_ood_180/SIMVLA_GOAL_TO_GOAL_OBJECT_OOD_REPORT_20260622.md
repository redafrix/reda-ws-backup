# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- Target OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_object_ood_180`
- Best epoch: `1`
- Runtime seconds: `1023.6`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 740762 | 3129 | 2617 | 512 |
| source_val | 161506 | 671 | 561 | 110 |
| source_test | 158616 | 669 | 560 | 109 |
| target_goal_object_full | 29117 | 180 | 139 | 41 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.3895 | 0.9330 | 0.9386 | 27.32% | 0.8152 | 0.8185 | 65.47% | 100.00% | 58.54% | 90.24% |
| q90_success | 0.6722 | 0.9330 | 0.9386 | 12.32% | 0.8152 | 0.8185 | 34.53% | 100.00% | 43.90% | 82.93% |
| q95_success | 0.9161 | 0.9330 | 0.9386 | 7.50% | 0.8152 | 0.8185 | 6.47% | 95.12% | 21.95% | 68.29% |
| q99_success | 0.9982 | 0.9330 | 0.9386 | 1.25% | 0.8152 | 0.8185 | 3.60% | 58.54% | 14.63% | 41.46% |
| fixed_0.5 | 0.5000 | 0.9330 | 0.9386 | 18.21% | 0.8152 | 0.8185 | 47.48% | 100.00% | 48.78% | 85.37% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
