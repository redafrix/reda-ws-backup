# AsyncVLA-SimVLA Stage 6 Improvement Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`  
Workspace: `/media/rootalkhatib/My Passport/reda_ws`  
Date: 2026-05-15  
Scope: improve the Stage 5 multi-seed SimVLA action-error rater so context/VLM/proprio help beyond action-only.

## 1. Executive Summary

Stage 6 improved over Stage 5 on the main SimVLA-only metrics.

The best Stage 6 variant is `context_gated_action`: a context-conditioned FiLM/gated action model using pooled VLM/proprio plus engineered action and seed-relative features. On the key controlled-OOD split `holdout_libero_object`, it reaches:

| Metric on `holdout_libero_object` test_ood | Stage 5 action-only | Stage 6 action-only rerun | Stage 6 context-gated |
| --- | ---: | ---: | ---: |
| SimVLA-only pairwise seed ranking | 0.865 | 0.751 | **0.916** |
| Improvement over seed0 | 0.0585 | 0.0473 | **0.0638** |
| Gap to oracle best seed | 0.0112 | 0.0224 | **0.0059** |
| AUROC top-30 worst SimVLA actions | Stage 5 not primary table | 0.707 | **0.972** |
| 50% risk-coverage accepted mean error | 1.378 | 1.472 | **1.358** |

Direct answer: context now helps. The improvement is meaningful on pairwise ranking (+0.051 absolute over the Stage 5 action-only baseline on the key split; +0.165 over the Stage 6 rerun action-only baseline). It is not a massive improvement in predicted-best mean error because Stage 5 already found the multi-seed oracle ceiling is small, but it closes most of the remaining oracle gap.

Switch readiness: promising for an offline VLA/WM switch proxy, but calibration is not uniformly deployable yet. `holdout_libero_object` is strong; `holdout_object_bowl` remains undercalibrated.

## 2. Stage 5 Baseline Recap

Stage 5 conclusion was strict:

- Full rater worked on full candidate sets and controlled LIBERO-OOD.
- Multi-seed SimVLA actions were diverse enough.
- But action-only was as good as or slightly better than full on SimVLA-only seed ranking.
- Stage 5 action-only pairwise on controlled OOD: `holdout_libero_object` 0.865, `holdout_object_bowl` 0.881.
- Stage 5 calibration: global residual conformal was deployable on `holdout_libero_object`, but `holdout_object_bowl` test_id undercovered badly.

Stage 6 therefore focused on seed-relative features, context/action interactions, and explicit context-gating rather than just scaling data.

## 3. Changes Implemented

New directories:

- `asynchvla_ws/src/rater_stage6/`
- `asynchvla_ws/src/features_stage6/`
- `asynchvla_ws/src/eval_stage6/`
- `asynchvla_ws/outputs/checkpoints/stage6/`
- `asynchvla_ws/outputs/reports/stage6/`
- `asynchvla_ws/outputs/logs/stage6/`

New/updated scripts:

- `asynchvla_ws/src/features_stage6/build_features.py`
- `asynchvla_ws/src/features_stage6/validate_stage6_features.py`
- `asynchvla_ws/src/rater_stage6/models.py`
- `asynchvla_ws/src/rater_stage6/common_metrics.py`
- `asynchvla_ws/src/rater_stage6/run_stage6_experiments.py`

Feature sets implemented: `A0_action_flat`, `A1_context`, `A2_full_old`, `F1_action_geometry`, `F2_proprio_action_delta`, `F3_seed_ensemble_features`, `F4_context_action_interactions`. `F5_flow_trace_features` is pending because Stage 5 datasets do not store flow path/update metadata.

Models/losses tested: action-only, context-only, full-old, engineered MLP, seed-relative, seed-relative plus pairwise loss, context-gated, per-step head, and SimVLA-focused variants. Heteroscedastic and ensemble variants were not run in the main ablation.

## 4. Pilot Ablation: `holdout_libero_object`

Pilot reports:

- `asynchvla_ws/outputs/reports/stage6/stage6_pilot_holdout_libero_object.md`
- `asynchvla_ws/outputs/reports/stage6/stage6_pilot_holdout_libero_object.json`

| Variant | Pairwise | Improvement over seed0 | Gap to oracle | AUROC | 50% accepted mean |
| --- | ---: | ---: | ---: | ---: | ---: |
| `action_only_baseline` | 0.7588 | 0.0506 | 0.0192 | 0.6762 | 1.4775 |
| `full_old_baseline` | 0.8088 | 0.0528 | 0.0170 | 0.9053 | 1.3766 |
| `full_engineered_mlp` | 0.9052 | 0.0634 | 0.0064 | 0.9466 | 1.3619 |
| `seed_relative_rater` | 0.9040 | 0.0643 | 0.0054 | 0.9446 | 1.3628 |
| `seed_relative_pairwise` | 0.8928 | 0.0631 | 0.0066 | 0.9693 | 1.3591 |
| `context_gated_action` | **0.9088** | 0.0632 | 0.0065 | 0.9642 | **1.3584** |
| `per_step_error_head` | 0.8952 | 0.0643 | 0.0055 | 0.9459 | 1.3632 |
| `seed_relative_simvla_focused` | 0.8964 | 0.0634 | 0.0064 | 0.9659 | 1.3586 |
| `full_engineered_simvla_focused` | 0.9080 | **0.0639** | **0.0058** | 0.9600 | 1.3609 |

Success criteria result: `context_gated_action` and `full_engineered_simvla_focused` are real Stage 6 winners. Pairwise improvement over Stage 5 action-only on the same split is about +0.044 absolute.

## 5. Winner Comparison Across Splits

Winner report:

- `asynchvla_ws/outputs/reports/stage6/stage6_all_splits_winner_comparison.md`

| Split | Winner | Part | Pairwise | Improvement | Gap oracle | AUROC | 50% accepted mean |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `id_task_split` | `context_gated_action` | test_id | 0.8932 | 0.0727 | 0.0079 | 0.9982 | 0.9406 |
| `holdout_libero_object` | `context_gated_action` | test_ood | 0.9160 | 0.0638 | 0.0059 | 0.9721 | 1.3581 |
| `holdout_object_bowl` | `context_gated_action` | test_ood | 0.9256 | 0.0660 | 0.0022 | 0.9968 | 1.1178 |

Action-only vs full conclusion:

- Context helps clearly after Stage 6.
- The biggest gain is pairwise seed ranking: +0.14 to +0.17 over the Stage 6 action-only rerun and +0.04 to +0.05 over the Stage 5 action-only baseline on comparable OOD splits.
- The improvement in predicted-best mean error is smaller because the five-seed oracle ceiling is low.

## 6. Extra Controlled-OOD

Extra report:

- `asynchvla_ws/outputs/reports/stage6/stage6_extra_ood_results.md`

Completed extra split: `holdout_libero_spatial`.

| Variant | Pairwise | Improvement | Gap oracle | AUROC | 50% accepted | 50% rejected |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `action_only_baseline` | 0.7075 | 0.0411 | 0.0219 | 0.7677 | 1.7787 | 2.0508 |
| `full_old_baseline` | 0.8715 | 0.0581 | 0.0048 | 0.9573 | 1.6485 | 2.1810 |
| `context_gated_action` | **0.9170** | **0.0614** | **0.0016** | **0.9657** | 1.6590 | 2.1705 |

Not completed in this session: `holdout_libero_goal`, a scene-heldout split, and a second object-heldout split. Reason: each requested five-seed extraction at this size takes about 16 minutes; the remaining jobs should run with nohup.

## 7. Calibration Conclusion

Calibration report:

- `asynchvla_ws/outputs/reports/stage6/stage6_calibration_best.md`

Best variant calibrated: `context_gated_action`.

| Split | Part | Global cov/width | SimVLA-only cov/width | Binned cov/width |
| --- | --- | ---: | ---: | ---: |
| `id_task_split` | test_id | 0.903 / 0.471 | 0.921 / 0.498 | 0.808 / 0.355 |
| `holdout_libero_object` | test_id | 0.969 / 0.530 | 0.994 / 0.603 | 0.838 / 0.364 |
| `holdout_libero_object` | test_ood | 0.993 / 0.530 | 0.994 / 0.603 | 0.918 / 0.320 |
| `holdout_object_bowl` | test_id | 0.681 / 0.360 | 0.625 / 0.300 | 0.558 / 0.275 |
| `holdout_object_bowl` | test_ood | 0.875 / 0.360 | 0.836 / 0.300 | 0.803 / 0.282 |
| `holdout_libero_spatial` | test_id | 0.855 / 0.479 | 0.889 / 0.570 | 0.870 / 0.415 |
| `holdout_libero_spatial` | test_ood | 0.898 / 0.479 | 0.963 / 0.570 | 0.702 / 0.422 |

Deployability:

- Deployable on `id_task_split` and `holdout_libero_object` with global residual conformal.
- Nearly deployable on `holdout_libero_spatial`; SimVLA-only residual gives 0.963 OOD coverage but wider bounds.
- Not deployable on `holdout_object_bowl` without recalibration. The manifest/calibration composition issue from Stage 5 remains.

## 8. Switch Conclusion

Switch analysis report:

- `asynchvla_ws/outputs/reports/stage6/stage6_switch_decision_analysis.md`

Single-action mode: use seed0, reject by predicted uncertainty. Deliberation mode: score five seeds and choose the lowest-uncertainty seed.

The best practical operating point remains 50% rejection for analysis: it gives a clear accepted/rejected error gap while retaining enough accepted samples. Runtime integration should start as an offline switch proxy with conservative thresholds, not as a final robot-control gate.

## 9. OOD Conclusion

These are controlled LIBERO-OOD results only.

The rater does not look like a pure OOD detector: same-context SimVLA seed ranking improves substantially, while context-only cannot rank seeds. Expert/wrong anti-cheat rankings remain strong in the full-candidate reports. Real SimVLA action uncertainty correlates with true error by pairwise ranking around 0.89–0.93 for the best model.

## 10. Failure Analysis

Remaining limitations:

- Predicted-best improvement over seed0 is still small because the oracle best among five seeds is only slightly better than seed0.
- Calibration is not fixed globally; `holdout_object_bowl` still undercovers.
- Candidate action geometry remains very informative. Context now helps, but the L2 action target still rewards action-only geometry.
- Next-state/task-space error may be a better target than normalized action L2.
- Flow internal features are still missing and should be added during trace extraction.
- Extra controlled-OOD expansion was only partially completed because five-seed extraction is slow.

## 11. Final Decision

Proceed toward runtime VLA/WM switch integration as a conservative offline prototype, while continuing calibration and target improvements.

Stage 6 answers the main Stage 5 weakness: context-aware models can beat action-only when using seed-relative features and explicit context/action gating.

Recommended next priorities:

1. Fix calibration with larger/split-stratified calibration pools.
2. Add flow-trace features during SimVLA generation.
3. Evaluate next-state/task-space error target, not only normalized action L2.
4. Finish extra controlled-OOD splits via nohup.
5. Build runtime switch wrapper that emits `accept/reject` for seed0 and optional five-seed deliberation.

## 12. Exact Next Commands

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
nohup bash -lc '
for s in holdout_libero_goal holdout_scene_kitchen_scene2 holdout_object_cabinet; do
  python3 asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py \
    --split-manifest asynchvla_ws/data/splits/${s}.json \
    --split-name $s \
    --max-contexts 1000 --max-calib 250 --max-test-id 250 --max-test-ood 250 \
    --cap-per-file 20 --steps 10 --simvla-seeds 0 1 2 3 4
  python3 asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py --split-name $s
  python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py \
    --split $s --epochs 80 \
    --variants action_only_baseline full_old_baseline context_gated_action \
    --out-prefix stage6_extra_${s}
done
' > asynchvla_ws/outputs/logs/stage6/extra_ood_remaining.log 2>&1 &
```

## 13. Duplicate Report Check

```text
/home/redafrix/tests/internship/codex_reports/ASYNCVLA_SIMVLA_STAGE5_MULTI_SEED_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/action_sensitivity_eval.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_AUDIT_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_IMPLEMENTATION_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE3_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE4_OOD_SPLITS_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/candidate_debug_dataset_report.md
/home/redafrix/tests/internship/codex_reports/done/checkpoint_smoke_test.md
/home/redafrix/tests/internship/codex_reports/done/debug_calibration_report.md
/home/redafrix/tests/internship/codex_reports/done/debug_rater_metrics.md
/home/redafrix/tests/internship/codex_reports/done/env_check.md
/home/redafrix/tests/internship/codex_reports/done/libero_inventory_report.md
/home/redafrix/tests/internship/codex_reports/done/ood_expert_data_search.md
/home/redafrix/tests/internship/codex_reports/done/phase2_unblock_and_trace_report.md
/home/redafrix/tests/internship/codex_reports/done/split_manifest_report.md
/home/redafrix/tests/internship/codex_reports/done/stage4_calibration_comparison.md
/home/redafrix/tests/internship/codex_reports/done/stage4_holdout_libero_object_metrics.md
/home/redafrix/tests/internship/codex_reports/done/stage4_holdout_object_bowl_metrics.md
/home/redafrix/tests/internship/codex_reports/done/stage4_id_task_split_metrics.md
/home/redafrix/tests/internship/codex_reports/done/trace_debug_dataset_report.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_claude_resume_precheck.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_interpretation.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_rater_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_rater_metrics_v2.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_rater_metrics_v2.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_libero_object_metrics.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_libero_object_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_libero_object_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_object_bowl_metrics.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_object_bowl_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_object_bowl_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_id_task_split_metrics.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_id_task_split_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_id_task_split_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_medium_dataset_build_report.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_multiseed_candidate_debug.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_multiseed_trace_debug.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_preflight.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_simvla_only_eval_utility.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_all_splits_winner_comparison.json
/home/redafrix/tests/internship/codex_reports/stage6/stage6_all_splits_winner_comparison.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_calibration_best.json
/home/redafrix/tests/internship/codex_reports/stage6/stage6_calibration_best.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_extra_ood_results.json
/home/redafrix/tests/internship/codex_reports/stage6/stage6_extra_ood_results.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_feature_validation.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_pilot_holdout_libero_object.json
/home/redafrix/tests/internship/codex_reports/stage6/stage6_pilot_holdout_libero_object.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_preflight.md
/home/redafrix/tests/internship/codex_reports/stage6/stage6_switch_decision_analysis.json
/home/redafrix/tests/internship/codex_reports/stage6/stage6_switch_decision_analysis.md

```
