# Dean OOD Last-2-TaskIds Full v1 (2026-06-01)

## Split Definition

OOD holdout uses the last two available task ids per suite:

- `libero_10_object`: task 8, 9
- `libero_90`: task 88, 89
- `libero_goal_object`: task 7, 8
- `libero_object_object`: task 8, 9
- `libero_spatial_object`: task 8, 9

All other valid Dean episodes are used for seen train/val/calib. There is no seen test set in this run.

## Episode Counts

| Bucket | Episodes | Rows |
|---|---:|---:|
| success_train_seen | 2219 | 299239 |
| failure_train_seen | 554 | 166200 |
| success_val_seen | 475 | 63629 |
| failure_val_seen | 139 | 41700 |
| success_calib_seen | 476 | 63841 |
| success_test_seen | 0 | 0 |
| failure_test_seen | 0 | 0 |
| success_test_ood | 235 | 23686 |
| failure_eval_ood | 93 | 27900 |

Total rows used: `686195`.

## Results

| Variant | OOD FA | OOD Detection | OOD Det@25 | OOD Det@50 | Mean Detection Time | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|
| base | 25.96% | 86.02% | 39.78% | 78.49% | 0.320 | 2 |
| unc_raw | 28.94% | 84.95% | 35.48% | 83.87% | 0.265 | 2 |

## Verdict

On this last-two-task-id OOD split, direct raw uncertainty features (`base + 98D`) do not beat the base model overall.

- `base` has lower OOD false alarms and slightly higher overall detection.
- `unc_raw` detects earlier on average and has better Det@50, but has worse FA and Det@25.

Current decision for this split: keep `base` as the main model. Use `unc_raw` only if the priority is later-before-end detection timing rather than false alarm rate.

