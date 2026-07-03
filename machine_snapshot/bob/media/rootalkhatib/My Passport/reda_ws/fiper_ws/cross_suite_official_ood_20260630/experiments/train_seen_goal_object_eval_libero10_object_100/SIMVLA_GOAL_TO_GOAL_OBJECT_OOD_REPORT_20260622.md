# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- Target OOD dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/libero10_object_100`
- Best epoch: `2`
- Runtime seconds: `1015.3`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 740762 | 3129 | 2617 | 512 |
| source_val | 161506 | 671 | 561 | 110 |
| source_test | 158616 | 669 | 560 | 109 |
| target_goal_object_full | 29262 | 100 | 23 | 77 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.3220 | 0.9266 | 0.9345 | 29.29% | 0.6687 | 0.8756 | 100.00% | 100.00% | 100.00% | 100.00% |
| q90_success | 0.6983 | 0.9266 | 0.9345 | 14.64% | 0.6687 | 0.8756 | 100.00% | 100.00% | 83.12% | 100.00% |
| q95_success | 0.9445 | 0.9266 | 0.9345 | 7.14% | 0.6687 | 0.8756 | 91.30% | 97.40% | 54.55% | 89.61% |
| q99_success | 0.9996 | 0.9266 | 0.9345 | 1.96% | 0.6687 | 0.8756 | 4.35% | 35.06% | 1.30% | 24.68% |
| fixed_0.5 | 0.5000 | 0.9266 | 0.9345 | 20.18% | 0.6687 | 0.8756 | 100.00% | 100.00% | 94.81% | 100.00% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
