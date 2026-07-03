# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- Target OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/spatial_object_100`
- Best epoch: `2`
- Runtime seconds: `995.4`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 740762 | 3129 | 2617 | 512 |
| source_val | 161506 | 671 | 561 | 110 |
| source_test | 158616 | 669 | 560 | 109 |
| target_goal_object_full | 12267 | 100 | 93 | 7 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.3949 | 0.9237 | 0.9285 | 27.68% | 0.7377 | 0.3494 | 100.00% | 100.00% | 100.00% | 100.00% |
| q90_success | 0.7565 | 0.9237 | 0.9285 | 15.71% | 0.7377 | 0.3494 | 79.57% | 100.00% | 100.00% | 100.00% |
| q95_success | 0.9827 | 0.9237 | 0.9285 | 6.96% | 0.7377 | 0.3494 | 33.33% | 100.00% | 42.86% | 85.71% |
| q99_success | 0.9998 | 0.9237 | 0.9285 | 1.96% | 0.7377 | 0.3494 | 10.75% | 14.29% | 0.00% | 0.00% |
| fixed_0.5 | 0.5000 | 0.9237 | 0.9285 | 23.21% | 0.7377 | 0.3494 | 96.77% | 100.00% | 100.00% | 100.00% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
