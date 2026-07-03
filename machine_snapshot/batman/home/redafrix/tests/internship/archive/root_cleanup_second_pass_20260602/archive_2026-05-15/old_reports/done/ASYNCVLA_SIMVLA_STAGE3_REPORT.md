# AsyncVLA-SimVLA Stage 3 Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`  
Workspace: `/media/rootalkhatib/My Passport/reda_ws`  
Branch: `bob`  
Date: 2026-05-13  
Scope: debug-scale SimVLA action-error uncertainty pipeline with same-observation candidate-action comparisons. No long training, no TDQC `.pt` rater data, no success/failure labels, no timestep/progress inputs.

## 1. Trace Debug Dataset Status

Status: `OK`

Dataset:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/trace_debug.pt`

Builder:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_debug_trace_dataset.py`

Validation report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/trace_debug_dataset_report.md`

Command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh >/dev/null
python3 asynchvla_ws/src/data_building/build_debug_trace_dataset.py --max-samples 200 --min-samples 50 --num-tasks 8 --seed 0 --steps 10
python3 asynchvla_ws/scripts/validate_trace_debug_dataset.py
```

Summary:

| Field | Value |
| --- | ---: |
| Samples | 200 |
| File size | 1,393,986 bytes |
| SimVLA checkpoint | `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000` |
| SimVLA generation seed | 0 |
| Flow steps | 10 |
| Split label | `debug_id` |

First-sample keys/shapes:

| Key | Shape / Type |
| --- | --- |
| `sample_id` | string |
| `context_id` | string |
| `task_name` | string |
| `task_id` | string |
| `demo_id` | `None`, unavailable from official loader |
| `source_hdf5` | string |
| `source_local_index` | integer from per-HDF5 loader iteration |
| `language_instruction` | string |
| `proprio` | `[8]` |
| `pooled_vlm_features` | `[960]` |
| `generated_normalized_action` | `[10,7]` |
| `generated_postprocessed_action` | `[10,7]` |
| `expert_normalized_action` | `[10,7]` |
| `expert_postprocessed_action` | `[10,7]` |
| `per_step_l2_error_normalized` | `[10]` |
| `chunk_l2_error_normalized` | scalar |
| `seed` | integer |
| `split` | string |

Action-error stats:

```text
chunk_l2_min_mean_max 0.4533155560493469 1.652939796447754 3.2215378284454346
```

Task coverage:

```text
close the top drawer of the cabinet: 50
open the top drawer of the cabinet: 50
put the chocolate pudding to the right of the plate: 25
turn on the stove: 50
put the bowl on the plate: 25
```

Notes:

- The official SimVLA loader exposes expert action chunks as `sample['action']` with shape `[10,7]`.
- The builder stores compact pooled VLM features only, not full VLM token tensors.
- No timestep, episode progress, trajectory length, success/failure labels, or TDQC fields are included.

## 2. Candidate-Action Dataset Status

Status: `OK`

Dataset:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`

Builder:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_candidate_action_dataset.py`

Validation report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/candidate_debug_dataset_report.md`

Summary:

| Field | Value |
| --- | ---: |
| Contexts | 200 |
| Candidates | 1200 |
| Candidates per context | 6 |
| File size | see validation report |

Candidate types and true error statistics:

| Candidate type | Count | Mean true chunk L2 error |
| --- | ---: | ---: |
| `expert_action` | 200 | 0.000000 |
| `perturb_small` | 200 | 0.255305 |
| `same_task_far` | 200 | 0.800747 |
| `other_demo_or_other_task` | 200 | 0.994390 |
| `simvla_seed0` | 200 | 1.652940 |
| `perturb_large` | 200 | 1.914658 |

Same-context proof from validation:

```text
context_id: ctx_000000
candidate types: ['expert_action', 'simvla_seed0', 'perturb_small', 'perturb_large', 'same_task_far', 'other_demo_or_other_task']
pooled VLM identical across candidates: True
proprio identical across candidates: True
target expert action identical across candidates: True
```

This is the core anti-cheat structure: the same observation/context appears with several candidate actions, and only `candidate_action_normalized` changes.

## 3. Debug Rater Training Status

Status: `OK`

Training script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/rater/train_debug_rater.py`

Dataset:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`

Checkpoint:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt`

Training log:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/logs/debug_rater_train.log`

Metrics report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/debug_rater_metrics.md`

Architecture:

- Small MLP: `Linear -> ReLU -> Dropout -> Linear -> ReLU -> Linear -> Softplus`.
- Target: chunk-level normalized action L2 error.
- Loss: Huber loss.
- Split: by `context_id`, 160 train contexts and 40 held-out validation contexts.
- Full rater input: pooled VLM features `[960]` + proprio `[8]` + candidate action `[10,7]` flattened.
- Context-only baseline input: pooled VLM features `[960]` + proprio `[8]` only.
- Action-only baseline input: candidate action `[10,7]` flattened only.

Full action-conditioned rater validation metrics:

| Metric | Value |
| --- | ---: |
| Pearson | 0.9247 |
| Spearman | 0.9128 |
| AUROC top-30% bad-action detection | 0.9373 |
| MSE | 0.0844 |
| MAE | 0.1540 |
| Expert lower than perturb_large | 1.0000 |
| Expert lower than other_task | 0.9750 |
| Expert lower than same_task_far | 1.0000 |
| Expert lower than SimVLA | 1.0000 |
| SimVLA pairwise true-order accuracy | 0.8625 |
| Same-context prediction std | 0.6571 |

Risk-coverage using lowest predicted uncertainty first:

| Coverage | Mean true error |
| ---: | ---: |
| 10% | 0.0779 |
| 25% | 0.0919 |
| 50% | 0.3230 |
| 75% | 0.6465 |
| 100% | 0.9394 |

## 4. Cheat Baseline Comparison

Status: `OK`

The action-conditioned rater clearly outperformed the context-only cheat baseline on same-context ranking.

| Model | Pearson | Spearman | AUROC bad-action | Expert < large | Expert < other task | Same-context pred std |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Full action-conditioned | 0.9247 | 0.9128 | 0.9373 | 1.0000 | 0.9750 | 0.6571 |
| Context-only cheat baseline | 0.1117 | 0.0886 | 0.5337 | 0.0000 | 0.0000 | 0.0000 |
| Action-only baseline | 0.8275 | 0.7269 | 0.9649 | 0.9750 | 0.4750 | 0.6100 |

Conclusion:

- The context-only baseline cannot distinguish candidate actions for the same observation; its same-context prediction std is exactly 0.
- The full rater changes predictions strongly when only candidate action changes.
- The action-only baseline is useful for synthetic perturbation detection but performs poorly on `expert < other_task` compared with the full rater, suggesting context is still useful.
- Current debug result is action-sensitive, not just image/task novelty based.

## 5. Calibration Status

Status: `OK`, but v1 calibration is global and debug-only.

Calibration script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/calibration/calibrate_debug_rater.py`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/debug_calibration_report.md`

Method:

`calibrated_uncertainty = predicted_error + eta`, where `eta` is the 90% conformal residual quantile on held-out validation contexts.

Summary:

| Field | Value |
| --- | ---: |
| Calibration contexts | 40 |
| Calibration rows | 240 |
| `eta_90` | 0.3203586042 |
| Empirical coverage | 0.9000 |
| Mean predicted error | 0.8642 |
| Mean calibrated uncertainty | 1.1845 |

Coverage per candidate type:

| Candidate type | Coverage | Mean true | Mean pred | Mean calibrated |
| --- | ---: | ---: | ---: | ---: |
| `expert_action` | 1.0000 | 0.0000 | 0.0752 | 0.3955 |
| `perturb_small` | 1.0000 | 0.2509 | 0.1450 | 0.4654 |
| `same_task_far` | 1.0000 | 0.8114 | 0.8478 | 1.1682 |
| `other_demo_or_other_task` | 0.9750 | 0.9965 | 0.9974 | 1.3178 |
| `simvla_seed0` | 1.0000 | 1.6785 | 1.7163 | 2.0367 |
| `perturb_large` | 0.4250 | 1.8994 | 1.4034 | 1.7237 |

Important limitation:

- Global conformal correction reaches 90% overall coverage but undercovers `perturb_large`. Before scaling, calibration should be reworked per candidate/error regime or with a better high-error tail model.

## 6. Action-Sensitivity Evaluation

Status: `OK`

Evaluation script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/eval/eval_action_sensitivity.py`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/action_sensitivity_eval.md`

Held-out validation behavior:

| Candidate type | Mean predicted uncertainty | Mean true error |
| --- | ---: | ---: |
| `expert_action` | 0.0752 | 0.0000 |
| `perturb_small` | 0.1450 | 0.2509 |
| `same_task_far` | 0.8478 | 0.8114 |
| `other_demo_or_other_task` | 0.9974 | 0.9965 |
| `perturb_large` | 1.4034 | 1.8994 |
| `simvla_seed0` | 1.7163 | 1.6785 |

Ranking highlights:

- `expert_action < perturb_large`: 1.0000
- `expert_action < other_demo_or_other_task`: 0.9750
- `expert_action < simvla_seed0`: 1.0000
- `perturb_small < perturb_large`: 1.0000
- `same_task_far < simvla_seed0`: 0.9750

Failure cases:

- One recorded failure where expert predicted uncertainty was slightly higher than an `other_demo_or_other_task` candidate for `ctx_000012`: expert 0.0572 vs other 0.0555.

Conclusion:

The rater does not appear to ignore actions on this ID debug set. The uncertainty changes when only the candidate action changes while pooled VLM features, proprio, instruction metadata, and expert target stay fixed.

## 7. OOD Expert Data Search

Status: raw OOD expert demos not found.

Search script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/find_ood_expert_data.py`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/ood_expert_data_search.md`

Search roots:

- `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/ood_data`
- `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data`
- `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/outputs/eval`
- `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla`
- `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc`

Corrected result:

```text
total_h5 130
hinted_h5 0
usable 0
```

The first OOD search implementation had a false positive because substring matching treated `wooden` as containing `ood`. The script was fixed to match OOD/unseen as path tokens. After correction, no HDF5/H5 file with OOD/unseen/novel token hints and raw expert actions was found.

Conclusion:

True OOD action-error evaluation is blocked because no OOD expert-action demonstrations were found. The existing OOD-named `.pt` files are TDQC/eval artifacts and were not used as rater data.

## 8. Files Created Or Modified

Created/updated:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_debug_trace_dataset.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/validate_trace_debug_dataset.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_candidate_action_dataset.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/validate_candidate_debug_dataset.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/rater/train_debug_rater.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/calibration/calibrate_debug_rater.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/eval/eval_action_sensitivity.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/find_ood_expert_data.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/trace_debug.pt`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/logs/debug_rater_train.log`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/trace_debug_dataset_report.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/candidate_debug_dataset_report.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/debug_rater_metrics.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/debug_calibration_report.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/action_sensitivity_eval.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/ood_expert_data_search.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE3_REPORT.md`

No TDQC experiment files were modified by this stage.

## 9. Final Recommendation

This method is promising enough to scale beyond debug on ID data.

Why:

- Same-observation candidate comparisons exist and validate correctly.
- The full action-conditioned rater strongly beats the context-only baseline.
- The rater ranks expert/correct actions below wrong/perturbed actions on held-out contexts.
- Risk-coverage is meaningful: low predicted uncertainty corresponds to lower true action error.

Fix before full-scale extraction:

- Improve calibration for high-error candidates, especially `perturb_large`, because global conformal correction undercovers that type.
- Add more natural wrong-action candidates from real trajectories and more SimVLA seeds if compute allows.
- Preserve the no-leakage rule: no timestep, progress, success label, episode length, or TDQC features.
- Consider per-step error prediction after the chunk-level rater is stable.

Next implementation step:

Extract a larger ID trace/candidate dataset using the same scripts via tmux/nohup, then retrain and rerun the same cheat-baseline tests. Do not claim OOD action-error performance until raw OOD expert demonstrations with images, proprio, instructions, and expert action chunks are available.
