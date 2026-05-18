# ASYNCVLA SimVLA Stage 7 Execution And Robustness Report

## 1. Executive Summary

Stage 7 did not restart old work. It used the Stage 6 `context_gated_action` model as the baseline and focused on making the method more deployment-relevant.

What was completed in this pass:

- Bob/Sam parallel setup was audited.
- Sam was partially prepared, with a working Python/CUDA SimVLA environment and a Sam activation script.
- Extra controlled-OOD completion was launched on Bob under `nohup` for `holdout_libero_goal`, `holdout_scene_kitchen_scene2`, and `holdout_object_cabinet`.
- LIBERO rollout validation was inspected and scaffolded, but actual simulator execution is blocked because the active Bob env lacks `robosuite` and `openpi_client`.
- Flow-trace metadata extraction was added to the trace API and a flow-trace dataset builder was created.
- Calibration repair analysis was run from existing Stage 6 predictions.
- LIBERO-PRO feasibility and Isaac Sim data planning reports were written.

What truly improved:

- The trace API now exposes compact flow-generation metadata that can be used in Stage 7 feature experiments.
- Stage 7 has a reproducible job launcher and report collector.
- Calibration undercoverage is now explicitly quantified from existing predictions rather than hidden.

What failed or remains blocked:

- Sam is not yet model-ready because the SmolVLM backbone upload is incomplete; the network slowed badly during laptop-to-Sam relay.
- Actual LIBERO execution validation is blocked until `robosuite` and either `openpi_client` or a direct in-process policy loop are available.
- Extra OOD metrics are pending because the Bob `nohup` job is still running.
- No history model or progress-target model was trained yet because rollout/sequence data are not validated.

Decision at this checkpoint: run larger rollout validation first before claiming deployment legitimacy. The method is promising from Stage 6 SimVLA-only action-error tests, but Stage 7 has not yet proven real execution-risk prediction.

## 2. Parallel Setup

Bob:

- Host: `PCROBOTUBUNTU02`
- Workspace: `/media/rootalkhatib/My Passport/reda_ws`
- Branch: `bob`
- Python after activation: `/usr/bin/python3`, Python `3.10.12`
- Torch/CUDA: `torch 2.5.1+cu121`, CUDA available `True`
- GPU: `NVIDIA GeForce RTX 4070 Ti SUPER`, `16376 MiB`
- Status: active Stage 7 execution machine.

Sam:

- Host: `PCROBOTUBUNTU05`
- Workspace found: `/home/rootalkhatib/test/reda_ws`
- Branch: `sam`
- Python after activation: `/home/rootalkhatib/envs/simvla/bin/python3`, Python `3.10.20`
- Torch/CUDA: `torch 2.5.1+cu121`, CUDA available `True`
- GPU: `NVIDIA GeForce RTX 4070 Ti SUPER`, `16376 MiB`
- Created activation script: `asynchvla_ws/scripts/activate_simvla_sam.sh`
- Status: partially ready; SmolVLM backbone sync incomplete.

Important Sam blocker:

- `model.safetensors` on Sam is only `479232000` bytes after interrupted upload.
- Bob has the complete SmolVLM directory (`1023M`).
- Sam model-load smoke test was not run because the backbone is incomplete.

Detailed report:

- `asynchvla_ws/outputs/reports/stage7/stage7_parallel_setup.md`
- Duplicate: `/home/redafrix/tests/internship/codex_reports/stage7/stage7_parallel_setup.md`

## 3. Extra Controlled-OOD Splits

Launched on Bob with `nohup`:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
bash asynchvla_ws/scripts/stage7_parallel_job_launcher.sh extra-ood-bob
```

Scheduled splits:

- `holdout_libero_goal`
- `holdout_scene_kitchen_scene2`
- `holdout_object_cabinet`

Log:

- `asynchvla_ws/outputs/logs/stage7/extra_ood_completion_bob.log`

Observed progress at report time:

- `holdout_libero_goal` trace extraction running.
- At least `400` train contexts collected.
- Final metrics are pending job completion.

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_extra_ood_completion.md`

## 4. Execution Rollout Validation

Existing SimVLA LIBERO evaluation code was found:

- `intern_ship_ws/simvla/code/SimVLA_modified/evaluation/libero/libero_client.py`
- `intern_ship_ws/simvla/code/SimVLA_modified/evaluation/libero/serve_smolvlm_libero.py`

Created scaffold:

- `asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py`

Import check result on Bob active env:

- `libero`: OK
- `msgpack_numpy`: OK
- `imageio`: OK
- `robosuite`: missing
- `openpi_client`: missing

Result: real LIBERO execution rollout validation is blocked. No success/progress claims were made.

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_libero_execution_eval.md`

## 5. Flow-Trace Features

Modified:

- `asynchvla_ws/src/simvla_trace/trace.py`

Created:

- `asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py`
- `asynchvla_ws/src/features_stage7/flow_trace_features.py`

New compact flow metadata:

- `initial_noise_norm`
- `final_action_norm`
- `velocity_norm_mean`
- `velocity_norm_max`
- `velocity_norm_final`
- `update_norm_mean`
- `update_norm_max`
- `update_norm_last`
- `total_path_length`
- `final_update_over_mean_update`
- `action_state_norm_mean`
- `action_state_norm_delta`

Validation:

- New files pass `python3 -m py_compile`.
- Dataset build/training not launched yet because Bob GPU is busy with extra-OOD extraction.

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_flow_trace_features.md`

## 6. Target Comparison

No new target was trained yet.

Current status:

- T0 action L2 remains the only fully evaluated target.
- T1 multi-expert min-distance is planned but not yet implemented in this pass.
- T2/T3 progress targets are blocked until simulator rollouts are available.
- T4 hybrid target should not be stacked before T1/T2/T3 are independently tested.

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_target_comparison.md`

## 7. History Models

History/window models were not trained.

Reason: current candidate datasets are context/candidate rows, not validated future-free rollout sequences. Building windows from raw indices risks timestep/order leakage.

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_history_models.md`

## 8. Calibration Repair

Created and ran:

- `asynchvla_ws/src/calibration/calibrate_stage7_repair.py`

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_calibration_repair.md`

Summary:

- Uses existing Stage 6 `context_gated_action` predictions.
- Reports global residual conformal, SimVLA-only residual conformal, binned SimVLA conformal, and an analysis-only larger pool.
- Does not use candidate-type conditional calibration as a deployable method.
- `holdout_object_bowl` undercoverage remains a real issue when only designated calibration contexts are used.

## 9. LIBERO-PRO Feasibility

Local search found TDQC LIBERO-PRO evaluation logs only:

- `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_eval_libero_pro/.../*.log`

No raw LIBERO-PRO expert-action HDF5 demonstrations were found.

Decision: LIBERO-PRO is not locally ready for this rater method. Do not use TDQC logs as action-error rater data.

Report:

- `asynchvla_ws/outputs/reports/stage7/stage7_libero_pro_feasibility.md`

## 10. Isaac Sim Plan

Created:

- `asynchvla_ws/outputs/reports/stage7/stage7_isaac_sim_data_plan.md`

The plan defines tasks, expert/bad action collection, progress labels, OOD perturbations, and schema alignment with the current rater pipeline. No Isaac implementation was started.

## 11. Files Created/Modified

Created/modified Stage 7 files:

- `asynchvla_ws/scripts/stage7_parallel_job_launcher.sh`
- `asynchvla_ws/scripts/stage7_collect_reports.sh`
- `asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py`
- `asynchvla_ws/src/features_stage7/flow_trace_features.py`
- `asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py`
- `asynchvla_ws/src/calibration/calibrate_stage7_repair.py`
- `asynchvla_ws/src/simvla_trace/trace.py`
- `asynchvla_ws/outputs/reports/stage7/*.md`
- Sam-only: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh`

No commit or push was performed.

## 12. Final Decision

Run larger rollout validation first.

Do not integrate a runtime VLA/WM switch yet, because Stage 7 has not proven uncertainty predicts actual execution risk/progress. The Stage 6 action-error rater is strong, and Stage 7 added the right infrastructure, but deployment claims need simulator execution evidence.

## 13. Exact Next Commands

Resume Sam backbone sync when network is acceptable:

```bash
rsync -a --partial --info=progress2 /tmp/stage7_smolvlm/ \
  sam:/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct/
```

Check Bob extra-OOD job:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
bash asynchvla_ws/scripts/stage7_parallel_job_launcher.sh status
tail -100 asynchvla_ws/outputs/logs/stage7/extra_ood_completion_bob.log
```

After the extra-OOD job finishes, run flow-trace extraction:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py \
  --split-manifest asynchvla_ws/data/splits/holdout_libero_object.json \
  --split-name holdout_libero_object \
  --max-contexts 200 --max-calib 80 --max-test-id 80 --max-test-ood 80 \
  --cap-per-file 10 --simvla-seeds 0 1 2 3 4
```

Fix rollout blocker before execution validation:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
python3 - <<'PY'
for m in ['robosuite', 'openpi_client']:
    try:
        __import__(m); print(m, 'OK')
    except Exception as e:
        print(m, 'MISSING', repr(e))
PY
```

## 14. Duplicate Report Check

```text
/home/redafrix/tests/internship/codex_reports/ASYNCVLA_SIMVLA_STAGE6_IMPROVEMENT_REPORT.md
/home/redafrix/tests/internship/codex_reports/ASYNCVLA_SIMVLA_STAGE7_EXECUTION_AND_ROBUSTNESS_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/action_sensitivity_eval.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_AUDIT_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_IMPLEMENTATION_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE3_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE4_OOD_SPLITS_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE5_MULTI_SEED_REPORT.md
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
/home/redafrix/tests/internship/codex_reports/stage6/ASYNCVLA_SIMVLA_STAGE6_IMPROVEMENT_REPORT.md
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
/home/redafrix/tests/internship/codex_reports/stage7/stage7_calibration_repair.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_extra_ood_completion.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_flow_trace_features.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_history_models.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_isaac_sim_data_plan.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_libero_execution_eval.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_libero_pro_feasibility.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_parallel_jobs_status.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_parallel_setup.md
/home/redafrix/tests/internship/codex_reports/stage7/stage7_target_comparison.md
```
