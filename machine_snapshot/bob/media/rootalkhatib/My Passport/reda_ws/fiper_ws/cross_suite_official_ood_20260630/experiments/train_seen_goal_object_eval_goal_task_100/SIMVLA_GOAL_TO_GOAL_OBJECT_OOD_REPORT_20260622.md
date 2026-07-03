# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- Target OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_task_100`
- Best epoch: `1`
- Runtime seconds: `1022.8`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 740762 | 3129 | 2617 | 512 |
| source_val | 161506 | 671 | 561 | 110 |
| source_test | 158616 | 669 | 560 | 109 |
| target_goal_object_full | 27453 | 100 | 10 | 90 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.3091 | 0.9313 | 0.9396 | 36.07% | 0.9415 | 0.9990 | 0.00% | 93.33% | 40.00% | 87.78% |
| q90_success | 0.6542 | 0.9313 | 0.9396 | 14.82% | 0.9415 | 0.9990 | 0.00% | 92.22% | 13.33% | 73.33% |
| q95_success | 0.9326 | 0.9313 | 0.9396 | 6.79% | 0.9415 | 0.9990 | 0.00% | 85.56% | 4.44% | 41.11% |
| q99_success | 0.9984 | 0.9313 | 0.9396 | 1.96% | 0.9415 | 0.9990 | 0.00% | 38.89% | 0.00% | 8.89% |
| fixed_0.5 | 0.5000 | 0.9313 | 0.9396 | 18.93% | 0.9415 | 0.9990 | 0.00% | 93.33% | 18.89% | 78.89% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
