# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- Target OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_swap_100`
- Best epoch: `1`
- Runtime seconds: `1017.6`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 740762 | 3129 | 2617 | 512 |
| source_val | 161506 | 671 | 561 | 110 |
| source_test | 158616 | 669 | 560 | 109 |
| target_goal_object_full | 29700 | 100 | 3 | 97 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.3560 | 0.9356 | 0.9397 | 27.50% | 0.6697 | 0.9913 | 100.00% | 100.00% | 93.81% | 100.00% |
| q90_success | 0.6905 | 0.9356 | 0.9397 | 11.79% | 0.6697 | 0.9913 | 100.00% | 100.00% | 85.57% | 100.00% |
| q95_success | 0.9054 | 0.9356 | 0.9397 | 5.71% | 0.6697 | 0.9913 | 66.67% | 98.97% | 71.13% | 94.85% |
| q99_success | 0.9976 | 0.9356 | 0.9397 | 1.43% | 0.6697 | 0.9913 | 0.00% | 49.48% | 9.28% | 29.90% |
| fixed_0.5 | 0.5000 | 0.9356 | 0.9397 | 20.36% | 0.6697 | 0.9913 | 100.00% | 100.00% | 91.75% | 100.00% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
