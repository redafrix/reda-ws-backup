# AsyncVLA-SimVLA Stage 4 Controlled LIBERO-OOD Splits Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`  
Workspace: `/media/rootalkhatib/My Passport/reda_ws`  
Branch: `bob`  
Date: 2026-05-13  
Scope: controlled LIBERO split protocols and medium pilot for SimVLA action-error uncertainty. These are controlled LIBERO-OOD splits, not external real-world OOD.

## 1. Inventory Summary

Inventory script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_libero_inventory.py`

Outputs:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/libero_inventory.json`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/libero_inventory_report.md`

Result: 130 HDF5 files scanned, 130 HDF5-loadable, 130 SimVLA-loader-loadable, 0 broken files.

| Suite | Files | Demos | Timesteps | Tasks |
| --- | ---: | ---: | ---: | ---: |
| `libero_10` | 10 | 500 | 138090 | 10 |
| `libero_90` | 90 | 4500 | 669043 | 74 |
| `libero_goal` | 10 | 500 | 63728 | 10 |
| `libero_object` | 10 | 500 | 74507 | 10 |
| `libero_spatial` | 10 | 500 | 62250 | 10 |

Top object tokens: `bowl` 38 files, `cabinet` 34, `plate` 29, `basket` 22, `drawer` 21, `book` 15, `stove` 14, `mug` 13.

Scene IDs are available for kitchen/living-room/study scenes, with enough files to create scene-heldout splits.

## 2. Split Definitions

Manifest script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/create_split_manifests.py`

Manifest directory:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/splits/`

Validation report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/split_manifest_report.md`

Created 32 manifests:

- `ID_TASK_SPLIT`: random HDF5-file split into train/calib/test_id.
- `OOD_SUITE_LEAVE_ONE_OUT`: one manifest per heldout suite.
- `OOD_OBJECT_HELDOUT`: one manifest per selected object token.
- `OOD_SCENE_HELDOUT`: one manifest per scene ID with enough files.

Pilot selected from inventory counts:

| Pilot | Manifest | Heldout | Train files | Calib files | Test ID files | Test OOD files |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| ID | `id_task_split` | none | 91 | 19 | 20 | 0 |
| Suite controlled-OOD | `holdout_libero_object` | `libero_object` | 84 | 18 | 18 | 10 |
| Object controlled-OOD | `holdout_object_bowl` | `bowl` | 64 | 13 | 15 | 38 |

## 3. Dataset Extraction Status

Builders:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_split_trace_dataset.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_split_candidate_dataset.py`

Build log:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/logs/stage4_build_datasets.log`

Command used:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh >/dev/null
for s in id_task_split holdout_libero_object holdout_object_bowl; do
  python3 asynchvla_ws/src/data_building/build_split_trace_dataset.py \
    --manifest asynchvla_ws/data/splits/${s}.json \
    --max-train 1000 --max-calib 250 --max-test-id 250 --max-test-ood 250 \
    --cap-per-file 20 --steps 10
  python3 asynchvla_ws/src/data_building/build_split_candidate_dataset.py --split-name $s
done
```

Pilot dataset counts:

| Split | Train contexts | Calib contexts | Test ID contexts | Test OOD contexts | Train candidates | Calib candidates | Test ID candidates | Test OOD candidates |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `id_task_split` | 1000 | 250 | 250 | 0 | 6000 | 1500 | 1500 | 0 |
| `holdout_libero_object` | 1000 | 250 | 250 | 200 | 6000 | 1500 | 1500 | 1200 |
| `holdout_object_bowl` | 1000 | 250 | 250 | 250 | 6000 | 1500 | 1500 | 1500 |

Representative file sizes:

- Trace train files: about 7 MB each.
- Candidate train files: about 34 MB each.
- Candidate calibration/test files: about 7-9 MB each.

Candidate types retained from Stage 3:

- `expert_action`
- `simvla_seed0`
- `perturb_small`
- `perturb_large`
- `same_task_far`
- `other_demo_or_other_task`

`simvla_seed1` and `simvla_seed2` were not added in this pilot to keep the first controlled split run bounded. The builder is structured so extra SimVLA seeds can be added later by extending trace generation.

## 4. Rater Results

Training/evaluation script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/rater/train_rater_from_split.py`

Checkpoints:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage4/`

Reports:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/stage4_id_task_split_metrics.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/stage4_holdout_libero_object_metrics.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/stage4_holdout_object_bowl_metrics.md`

### ID Task Split

| Model | Part | Pearson | Spearman | AUROC | Expert < large | Expert < other | Same-context std |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Full | test_id | 0.973 | 0.956 | 0.990 | 1.000 | 0.988 | 0.681 |
| Context-only | test_id | 0.070 | 0.084 | 0.550 | 0.004 | 0.004 | 0.000 |
| Action-only | test_id | 0.928 | 0.739 | 0.984 | 1.000 | 0.480 | 0.733 |

### Controlled Suite-OOD: Holdout `libero_object`

| Model | Part | Pearson | Spearman | AUROC | Expert < large | Expert < other | Same-context std |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Full | test_id | 0.965 | 0.942 | 0.991 | 1.000 | 0.976 | 0.680 |
| Full | test_ood | 0.988 | 0.956 | 0.999 | 1.000 | 0.965 | 0.697 |
| Context-only | test_ood | 0.033 | 0.028 | 0.510 | 0.000 | 0.000 | 0.000 |
| Action-only | test_ood | 0.960 | 0.769 | 0.999 | 1.000 | 0.500 | 0.735 |

### Controlled Object-OOD: Holdout `bowl`

| Model | Part | Pearson | Spearman | AUROC | Expert < large | Expert < other | Same-context std |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Full | test_id | 0.988 | 0.964 | 1.000 | 1.000 | 0.988 | 0.772 |
| Full | test_ood | 0.980 | 0.963 | 1.000 | 1.000 | 0.976 | 0.638 |
| Context-only | test_ood | 0.081 | 0.071 | 0.543 | 0.000 | 0.000 | 0.000 |
| Action-only | test_ood | 0.938 | 0.745 | 1.000 | 1.000 | 0.504 | 0.723 |

## 5. Anti-Cheat / Anti-OOD-Detector Result

Controlled suite-OOD, heldout `libero_object`, full rater mean predictions on OOD contexts:

| Candidate type | Mean true error | Mean predicted uncertainty |
| --- | ---: | ---: |
| `expert_action` | 0.000 | 0.121 |
| `perturb_small` | 0.255 | 0.301 |
| `same_task_far` | 0.535 | 0.484 |
| `other_demo_or_other_task` | 0.530 | 0.549 |
| `simvla_seed0` | 1.728 | 1.702 |
| `perturb_large` | 1.915 | 1.841 |

Controlled object-OOD, heldout `bowl`, full rater mean predictions on OOD contexts:

| Candidate type | Mean true error | Mean predicted uncertainty |
| --- | ---: | ---: |
| `expert_action` | 0.000 | 0.208 |
| `perturb_small` | 0.255 | 0.390 |
| `other_demo_or_other_task` | 0.609 | 0.714 |
| `same_task_far` | 0.666 | 0.747 |
| `simvla_seed0` | 1.691 | 1.634 |
| `perturb_large` | 1.923 | 1.832 |

Direct answer:

- Does the rater give low uncertainty to controlled-OOD expert actions? Yes. Expert-action predicted uncertainty remains the lowest candidate type on both controlled OOD splits.
- Does it give higher uncertainty to wrong actions for the same controlled-OOD observation? Yes. `perturb_large`, `simvla_seed0`, and wrong real-action candidates are higher than expert for the same contexts.
- Does it beat the context-only baseline on controlled-OOD same-context ranking? Yes. Context-only has zero same-context prediction std and cannot rank same-context candidates; full rater has nonzero same-context std and high ranking accuracy.

This pilot does not behave like a pure OOD detector. If it were using only image/task novelty, OOD `expert_action` rows would be high uncertainty and same-context candidate ranking would fail. That did not happen in the controlled LIBERO-OOD tests.

## 6. Calibration Result

Calibration script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/calibration/compare_stage4_calibration.py`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/stage4_calibration_comparison.md`

Implemented calibration variants:

1. Global 90% residual conformal.
2. Candidate-type conditional residual conformal, for analysis only.
3. Predicted-error-bin residual conformal with 3 calibration quantile bins.

A quantile rater was not trained in this pilot.

Coverage summary:

| Split | Part | Global | Candidate-type | Error-bin |
| --- | --- | ---: | ---: | ---: |
| `id_task_split` | test_id | 0.951 | 0.965 | 0.961 |
| `holdout_libero_object` | test_id | 0.923 | 0.943 | 0.942 |
| `holdout_libero_object` | test_ood | 0.923 | 0.945 | 0.888 |
| `holdout_object_bowl` | test_id | 0.931 | 0.945 | 0.925 |
| `holdout_object_bowl` | test_ood | 0.911 | 0.930 | 0.928 |

Calibration conclusion:

- Global conformal is already near or above 90% in all pilot test partitions.
- Candidate-type conditional calibration improves coverage but uses candidate labels and should remain analysis-only unless the deployment setting explicitly knows candidate class.
- Error-bin calibration is mixed: good on heldout `bowl`, slightly under 90% on heldout `libero_object` OOD.

## 7. Decision

Decision: scale to full LIBERO controlled splits, with calibration kept under review.

Why:

- The rater remains action-sensitive on ID, suite-heldout, and object-heldout controlled splits.
- Controlled-OOD expert actions are assigned low uncertainty relative to wrong actions from the same observation.
- Context-only baseline fails on same-context ranking, which directly addresses the main anti-OOD-detector concern.
- Action-only baseline is strong on synthetic perturbations but weaker on `expert < other_task`, so context still helps.

Caveats before scaling:

- These are controlled LIBERO-OOD splits, not external raw OOD demonstrations.
- Candidate construction still uses only `simvla_seed0`; add `simvla_seed1/2` for a larger run if compute budget allows.
- Calibration should be monitored per candidate/error regime.
- The current pilot caps per file and per split; full extraction should use tmux/nohup.

## 8. Next Stage 5 Commands

Recommended full controlled split extraction:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
mkdir -p asynchvla_ws/outputs/logs
nohup bash -lc '
for s in id_task_split holdout_libero_object holdout_object_bowl; do
  python3 asynchvla_ws/src/data_building/build_split_trace_dataset.py \
    --manifest asynchvla_ws/data/splits/${s}.json \
    --max-train 5000 --max-calib 1000 --max-test-id 1000 --max-test-ood 1000 \
    --cap-per-file 80 --steps 10
  python3 asynchvla_ws/src/data_building/build_split_candidate_dataset.py --split-name $s
  python3 asynchvla_ws/src/rater/train_rater_from_split.py --split-name $s
done
python3 asynchvla_ws/src/calibration/compare_stage4_calibration.py
' > asynchvla_ws/outputs/logs/stage5_full_controlled_splits.log 2>&1 &
```

Recommended next code improvement before Stage 5 if time allows:

- Extend `build_split_trace_dataset.py` to generate and store `simvla_seed1` and `simvla_seed2` for a configurable subset or all contexts.
- Extend `build_split_candidate_dataset.py` to add candidate types `simvla_seed1` and `simvla_seed2` when present.
