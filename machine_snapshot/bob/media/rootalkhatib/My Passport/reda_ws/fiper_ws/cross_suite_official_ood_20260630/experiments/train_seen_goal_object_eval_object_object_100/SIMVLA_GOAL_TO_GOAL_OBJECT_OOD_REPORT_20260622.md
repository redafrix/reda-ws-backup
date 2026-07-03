# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- Target OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/object_object_100`
- Best epoch: `2`
- Runtime seconds: `997.3`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 740762 | 3129 | 2617 | 512 |
| source_val | 161506 | 671 | 561 | 110 |
| source_test | 158616 | 669 | 560 | 109 |
| target_goal_object_full | 20240 | 100 | 63 | 37 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.3831 | 0.9274 | 0.9341 | 28.04% | 0.7519 | 0.7390 | 100.00% | 100.00% | 100.00% | 100.00% |
| q90_success | 0.6932 | 0.9274 | 0.9341 | 14.64% | 0.7519 | 0.7390 | 100.00% | 100.00% | 100.00% | 100.00% |
| q95_success | 0.9713 | 0.9274 | 0.9341 | 6.25% | 0.7519 | 0.7390 | 53.97% | 86.49% | 86.49% | 86.49% |
| q99_success | 0.9997 | 0.9274 | 0.9341 | 1.43% | 0.7519 | 0.7390 | 0.00% | 0.00% | 0.00% | 0.00% |
| fixed_0.5 | 0.5000 | 0.9274 | 0.9341 | 21.61% | 0.7519 | 0.7390 | 100.00% | 100.00% | 100.00% | 100.00% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
