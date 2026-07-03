# SimVLA Goal to Goal-Object OOD Risk Evaluation

- Source train dataset: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622/fiper_receding_samples.jsonl`
- Target OOD dataset: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_object_h10_continuous_flat_from_bob_20260622`
- Best epoch: `2`
- Runtime seconds: `892.5`

## Dataset Summary

| Split | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| source_train | 594842 | 3787 | 3584 | 203 |
| source_val | 127939 | 812 | 768 | 44 |
| source_test | 129244 | 811 | 768 | 43 |
| target_goal_object_full | 235466 | 17409 | 14005 | 3404 |

## Threshold Metrics

| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 0.6014 | 0.9307 | 0.9051 | 17.06% | 0.7627 | 0.6998 | 4.59% | 78.91% | 0.15% | 7.61% |
| q90_success | 0.3156 | 0.9307 | 0.9051 | 32.68% | 0.7627 | 0.6998 | 16.82% | 92.89% | 23.74% | 38.92% |
| q95_success | 0.5641 | 0.9307 | 0.9051 | 17.84% | 0.7627 | 0.6998 | 5.83% | 80.64% | 0.18% | 8.46% |
| q99_success | 0.9471 | 0.9307 | 0.9051 | 4.95% | 0.7627 | 0.6998 | 0.55% | 35.25% | 0.00% | 0.88% |
| fixed_0.5 | 0.5000 | 0.9307 | 0.9051 | 20.18% | 0.7627 | 0.6998 | 8.27% | 83.96% | 0.32% | 9.75% |

## Legitimacy Notes

- Train split uses only plain `libero_goal` episodes.
- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.
- Inputs exclude explicit task id and explicit timestep.
- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.
