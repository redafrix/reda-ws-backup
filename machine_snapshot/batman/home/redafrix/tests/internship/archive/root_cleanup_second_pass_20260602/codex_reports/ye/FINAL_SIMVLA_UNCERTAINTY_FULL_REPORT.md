# Final SimVLA / AsyncVLA-Style Uncertainty Experiment Report

Generated locally: `2026-05-18T09:19:39`

Local report folder: `/home/redafrix/tests/internship/codex_reports/ye`

## Executive Summary

- The 72-hour Stage 8 campaign mostly completed successfully: `26` jobs were done, `0` were failed, Sam was fully done, and Bob still had one long 50-episode backup rollout running at the snapshot time.
- LIBERO-PRO became the main execution benchmark. The strongest completed LIBERO-PRO result is the 20 episodes/task expanded run: 20 task/mode groups, 1600 episodes total.
- The uncertainty/rater is useful for offline action reliability and controlled OOD SimVLA-seed ranking. The strongest family remains context/seed-aware models, not action-only.
- For real rollout control, multi-seed deliberation was not clearly better than seed0. On LIBERO-PRO, B_deliberation improved success only slightly over A_passive but took slightly more steps; C_random_seed was similar or slightly better in aggregate, which means the current uncertainty score is not yet a reliable seed selector for execution.
- Calibration improved but is not deployable across all domains. 90% conformal-style coverage still undercovers badly on some splits, especially heldout spatial and some ID/OOD mismatches.
- Flowtrace features did not improve pairwise ranking in the completed small/medium runs. Flow-only had high bad-action AUROC in some splits, but poor seed ranking, so it is not a replacement for the context/seed/action rater.
- Multi-expert targets did not beat the original single-expert L2 target on average. They may help individual splits, but the simple target remains the most stable completed training target.
- History models were not actually trained because the available rollout outputs were aggregate episode JSON, not clean sequential per-step windows with previous action/uncertainty/proprio/VLM features.

## Final Decision

**Do not integrate a real VLA/WM switch yet.** The method is promising as a warning/risk-ranking signal and for offline action-error filtering, but it is not yet a reliable runtime switch policy. The next scientific step should be progress/next-state labels from rollouts, not more synthetic action-L2 sweeps.

## Queue / Machine Status

| job_id | machine | state | completed_at | started_at |
|---|---|---|---|---|
| smoke_bob_cpu | bob | DONE | 2026-05-15T15:09:43+02:00 |  |
| smoke_sam_cpu | sam | DONE | 2026-05-15T15:09:44+02:00 |  |
| smoke_dependency_child | bob | DONE | 2026-05-15T15:09:51+02:00 |  |
| smoke_retry_failure | bob | DONE | 2026-05-15T15:10:18+02:00 |  |
| libero_pro_pilot_bob | bob | DONE | 2026-05-15T16:00:59+02:00 |  |
| stage8_sam_model_sweep | sam | DONE | 2026-05-15T15:39:23+02:00 |  |
| stage8_sam_calibration_sweep | sam | DONE | 2026-05-15T15:39:35+02:00 |  |
| stage8_sam_flowtrace_real | sam | DONE | 2026-05-15T21:37:12+02:00 |  |
| stage8_sam_target_real | sam | DONE | 2026-05-15T22:58:07+02:00 |  |
| stage8_sam_arch_big | sam | DONE | 2026-05-16T00:49:45+02:00 |  |
| flowtrace_experiments_sam | sam | DONE | 2026-05-15T16:14:44+02:00 |  |
| stage8_sam_calibration_real | sam | DONE | 2026-05-16T01:00:00+02:00 |  |
| stage8_sam_history_real | sam | DONE | 2026-05-16T01:00:08+02:00 |  |
| target_sweep_sam | sam | DONE | 2026-05-15T16:14:55+02:00 |  |
| architecture_loss_sweep_sam | sam | DONE | 2026-05-15T16:49:59+02:00 |  |
| normal_libero_hard_baseline_bob | bob | DONE | 2026-05-15T19:41:31+02:00 |  |
| libero_pro_expanded_rollout_bob | bob | DONE | 2026-05-15T22:58:09+02:00 |  |
| flowtrace_medium_bob | bob | DONE | 2026-05-15T23:08:24+02:00 |  |
| calibration_mega_sam | sam | DONE | 2026-05-15T16:50:11+02:00 |  |
| normal_libero_hard_30eps_bob | bob | DONE | 2026-05-16T07:23:52+02:00 |  |
| libero_pro_expanded_30eps_bob | bob | DONE | 2026-05-17T00:33:56+02:00 |  |
| history_models_sam | sam | DONE | 2026-05-15T16:15:03+02:00 |  |
| switch_policy_analysis_bob | bob | DONE | 2026-05-16T07:24:01+02:00 |  |
| stage8_libero_pro_20eps_bob | bob | DONE | 2026-05-17T12:00:41+02:00 |  |
| stage8_libero_pro_50eps_backup_bob | bob | RUNNING |  | 2026-05-17T12:00:44+02:00 |
| stage8_normal_libero_50eps_backup_bob | bob | PENDING |  |  |
| stage8_switch_policy_extended_bob | bob | DONE | 2026-05-17T12:10:53+02:00 |  |
| stage8_final_report_bob | bob | DONE | 2026-05-17T00:34:05+02:00 |  |

Snapshot interpretation:
- Sam: all Stage 8 jobs done.
- Bob: `stage8_libero_pro_50eps_backup_bob` still running at snapshot, `stage8_normal_libero_50eps_backup_bob` pending. This is a backup extension, not a blocker for the completed 20/30 episode analysis.

## LIBERO-PRO Rollout Results

Source: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md`

### Aggregate by mode, 20 episodes/task

| mode | episodes | tasks | success | avg_steps | avg_unc | avg_rejects | min_task_success |
|---|---|---|---|---|---|---|---|
| A_passive | 400 | 20 | 0.945 | 176.09 | 1.576 | 9.78 | 0.750 |
| B_deliberation | 400 | 20 | 0.955 | 177.21 | 1.588 | 9.89 | 0.700 |
| C_random_seed | 400 | 20 | 0.958 | 176.30 | 1.590 | 10.28 | 0.800 |
| D_low_uncertainty_reject_log | 400 | 20 | 0.945 | 176.08 | 1.576 | 9.78 | 0.750 |

Key reading:
- `A_passive` seed0 baseline: 94.5% success, 176.09 avg steps.
- `B_deliberation`: 95.5% success, 177.21 avg steps. This is +1.0 success point but slightly slower.
- `C_random_seed`: 95.75% success, 176.30 avg steps. Random seed selection slightly beat deliberation, so the current rater does not yet prove it can choose the best seed in live execution.
- `D_low_uncertainty_reject_log` exactly mirrors seed0 execution, as expected, because it logs reject decisions without changing actions.

Worst LIBERO-PRO seed0 tasks:
| suite | task | success | avg_steps | avg_unc | max_unc |
|---|---|---|---|---|---|
| libero_spatial_with_mug | 0 | 0.750 | 221.45 | 1.732 | 3.039 |
| libero_goal_with_mug | 2 | 0.850 | 166.05 | 2.123 | 4.368 |
| libero_goal_with_mug | 0 | 0.850 | 234.20 | 2.146 | 3.250 |
| libero_10_with_mug | 2 | 0.850 | 288.90 | 1.564 | 3.701 |
| libero_goal_with_mug | 3 | 0.900 | 219.25 | 1.592 | 3.219 |
| libero_10_with_mug | 1 | 0.900 | 277.65 | 1.365 | 2.305 |

Best task-level improvements from non-seed0 modes:
| suite/task | mode | success_delta | steps_delta_vs_A | mode_success | A_success |
|---|---|---|---|---|---|
| libero_10_with_mug 2 | C_random_seed | 0.150 | 52.80 | 1.000 | 0.850 |
| libero_goal_with_mug 2 | C_random_seed | 0.100 | 47.25 | 0.950 | 0.850 |
| libero_goal_with_mug 3 | B_deliberation | 0.100 | 41.10 | 1.000 | 0.900 |
| libero_goal_with_mug 0 | C_random_seed | 0.100 | 24.60 | 0.950 | 0.850 |
| libero_10_with_mug 2 | B_deliberation | 0.100 | 23.65 | 0.950 | 0.850 |
| libero_goal_with_mug 2 | B_deliberation | 0.050 | 25.95 | 0.900 | 0.850 |

Largest regressions:

| suite/task | mode | success_delta | steps_delta_vs_A | mode_success | A_success |
|---|---|---|---|---|---|
| libero_object_with_mug 2 | C_random_seed | -0.100 | -40.60 | 0.850 | 0.950 |
| libero_object_with_mug 1 | C_random_seed | -0.050 | -30.95 | 0.950 | 1.000 |
| libero_goal_with_mug 1 | B_deliberation | -0.050 | -27.75 | 0.950 | 1.000 |
| libero_spatial_with_mug 3 | B_deliberation | -0.050 | -26.55 | 0.950 | 1.000 |
| libero_spatial_with_mug 1 | B_deliberation | -0.050 | -25.45 | 0.950 | 1.000 |
| libero_spatial_with_mug 0 | B_deliberation | -0.050 | -17.30 | 0.700 | 0.750 |

Interpretation: uncertainty-guided deliberation sometimes helps specific tasks, but the task-level regressions and the random-seed baseline mean this is not yet a robust runtime policy.

## Normal LIBERO Hard-Task Baseline

Source: `stage8_normal_libero_hard_task_results.md`, 30 episodes/task, 840 episodes total.

| mode | episodes | tasks | success | avg_steps | avg_unc | avg_rejects | min_task_success |
|---|---|---|---|---|---|---|---|
| A_passive | 210 | 7 | 0.833 | 242.11 | 1.792 | 14.46 | 0.133 |
| B_deliberation | 210 | 7 | 0.814 | 259.78 | 1.771 | 15.17 | 0.133 |
| C_random_seed | 210 | 7 | 0.843 | 241.25 | 1.806 | 15.45 | 0.133 |
| D_low_uncertainty_reject_log | 210 | 7 | 0.833 | 242.11 | 1.792 | 14.46 | 0.133 |

Hardest task remains `libero_spatial task 5`: seed0 success 0.133, avg 540.93 steps. Deliberation and random did not fix it. This task is useful as a failure/stress benchmark.

## Switch Policy Analysis

Source: `stage8_switch_policy_results.md`, 4065 parsed episodes.

| mode | episodes | success | avg_steps | avg_rejects | avg_unc |
|---|---:|---:|---:|---:|---:|
| A_passive | 995 | 0.910 | 197.14 | 11.12 | 1.630 |
| B_deliberation | 995 | 0.910 | 202.76 | 11.34 | 1.634 |
| C_random_seed | 995 | 0.921 | 195.86 | 11.43 | 1.643 |
| D_reject_log | 995 | 0.910 | 197.14 | 11.15 | 1.630 |
| E_conservative_switch_proxy | 85 | 0.824 | 244.02 | 12.89 | 1.690 |

Interpretation: the current offline switch proxy does not yet demonstrate deployment benefit. Conservative fallback underperformed on the small available subset. The main reliable use is warning/rejection analysis, not automatic action replacement.

## Model / Architecture Results

Source: Sam `stage8_big_arch_*.json`, test_ood SimVLA-only metrics averaged across 6 controlled OOD splits.

| variant | splits | pairwise_seed_rank | improvement_over_seed0 | AUROC_top30_worst |
|---|---|---|---|---|
| seed_relative_pairwise | 6 | 0.917 | 0.066 | 0.984 |
| full_engineered_simvla_focused | 6 | 0.916 | 0.066 | 0.983 |
| full_engineered_mlp | 6 | 0.915 | 0.066 | 0.978 |
| context_gated_action | 6 | 0.914 | 0.066 | 0.975 |
| seed_relative_simvla_focused | 6 | 0.913 | 0.066 | 0.986 |
| heteroscedastic_simvla_focused | 6 | 0.912 | 0.066 | 0.973 |
| seed_relative_rater | 6 | 0.911 | 0.066 | 0.978 |
| per_step_error_head | 6 | 0.907 | 0.066 | 0.978 |
| heteroscedastic_head | 6 | 0.907 | 0.065 | 0.973 |
| full_old_baseline | 6 | 0.874 | 0.062 | 0.952 |
| action_only_baseline | 6 | 0.751 | 0.050 | 0.802 |

Important result: action-only is clearly worse after Stage 8. Average test_ood pairwise seed ranking was `0.7515` for action-only versus `0.9174` for `seed_relative_pairwise`, `0.9161` for `full_engineered_simvla_focused`, and `0.9141` for `context_gated_action`.

Best per controlled-OOD split:

| split/part | best_variant | pairwise | improvement | AUROC |
|---|---|---|---|---|
| ('holdout_object_bowl', 'test_ood') | context_gated_action | 0.925 | 0.064 | 0.997 |
| ('holdout_libero_goal', 'test_ood') | seed_relative_pairwise | 0.917 | 0.084 | 0.994 |
| ('holdout_libero_object', 'test_ood') | full_engineered_mlp | 0.916 | 0.064 | 0.969 |
| ('holdout_libero_spatial', 'test_ood') | heteroscedastic_simvla_focused | 0.929 | 0.062 | 0.973 |
| ('holdout_object_cabinet', 'test_ood') | seed_relative_simvla_focused | 0.934 | 0.043 | 0.992 |
| ('holdout_scene_kitchen_scene2', 'test_ood') | full_engineered_mlp | 0.933 | 0.082 | 0.971 |

Recommended model family from completed offline metrics: `seed_relative_pairwise` or `full_engineered_simvla_focused` for action-error ranking; `context_gated_action` remains the simplest strong baseline.

## Flowtrace Feature Results

Source: `stage7_flowtrace_*.json`, smaller/medium flowtrace runs.

| variant | splits | pairwise | improvement | AUROC |
|---|---|---|---|---|
| context_gated_action_no_flow | 3 | 0.798 | 0.048 | 0.892 |
| seed_relative_plus_flow | 3 | 0.776 | 0.044 | 0.895 |
| action_only_plus_flow | 3 | 0.738 | 0.045 | 0.902 |
| context_gated_action_plus_flow | 3 | 0.729 | 0.042 | 0.916 |
| flow_only | 3 | 0.667 | 0.038 | 0.970 |

Interpretation: flowtrace did not improve SimVLA seed ranking. `context_gated_action_no_flow` beat all flow-augmented variants on pairwise ranking in this run. `flow_only` had high AUROC but poor pairwise ranking, so flow dynamics may help bad-action detection but not seed selection yet.

## Target Sweep Results

Source: detailed Sam `stage7_multi_expert_target_*.json` outputs.

| target | rows | avg_pairwise | avg_improvement | avg_AUROC |
|---|---|---|---|---|
| target_chunk_l2_single_expert | 24 | 0.868 | 0.062 | 0.931 |
| target_chunk_min_l2_K10 | 24 | 0.861 | 0.062 | 0.931 |
| target_chunk_min_l2_K5 | 24 | 0.861 | 0.062 | 0.930 |
| target_chunk_min_l2_K20 | 24 | 0.859 | 0.062 | 0.929 |
| target_chunk_mean_top3_l2_K10 | 24 | 0.859 | 0.062 | 0.930 |
| target_chunk_softmin_l2_K10 | 23 | 0.813 | 0.056 | 0.889 |

Interpretation: the original single-expert L2 target remained best on average. Multi-expert min-distance K=5/K=10 helped some individual splits, but did not produce a global improvement. Softmin was worst/unstable in this completed sweep.

## Calibration Results

Source: `stage8_calibration_real_q*.json`, context_gated_action, SimVLA-only evals.

| target_coverage | method | eval_rows | avg_coverage | min_coverage | avg_width | avg_AUROC |
|---|---|---|---|---|---|---|
| 0.80 | global_residual_all | 13 | 0.753 | 0.480 | 0.061 | 0.983 |
| 0.80 | affine_plus_residual_all | 13 | 0.755 | 0.487 | 0.068 | 0.983 |
| 0.80 | global_residual_simvla | 13 | 0.791 | 0.504 | 0.084 | 0.983 |
| 0.80 | affine_plus_residual_simvla | 13 | 0.790 | 0.593 | 0.080 | 0.983 |
| 0.90 | global_residual_all | 13 | 0.845 | 0.629 | 0.114 | 0.983 |
| 0.90 | affine_plus_residual_all | 13 | 0.842 | 0.634 | 0.116 | 0.983 |
| 0.90 | global_residual_simvla | 13 | 0.859 | 0.653 | 0.140 | 0.983 |
| 0.90 | affine_plus_residual_simvla | 13 | 0.860 | 0.648 | 0.130 | 0.983 |
| 0.95 | global_residual_all | 13 | 0.894 | 0.694 | 0.188 | 0.983 |
| 0.95 | affine_plus_residual_all | 13 | 0.894 | 0.685 | 0.189 | 0.983 |
| 0.95 | global_residual_simvla | 13 | 0.917 | 0.688 | 0.241 | 0.983 |
| 0.95 | affine_plus_residual_simvla | 13 | 0.917 | 0.674 | 0.211 | 0.983 |

Interpretation:
- Calibration ranking/AUROC is strong, but coverage is not reliable enough. At target 90%, average SimVLA-only coverage was only 0.845-0.860 depending on method, with worst split around 0.629-0.648.
- At target 95%, average coverage improved to 0.894-0.917, but still undercovered badly in the worst split and widened bounds.
- Best deployable current choice if forced: `global_residual_simvla` or `affine_plus_residual_simvla` at 95% target, but this is conservative and still not guaranteed on all splits.
- Needed next: small target-domain calibration pools or progress-risk probability calibration, not just residual bounds on action L2.

## History Models

History models were not trained. The Stage 8 history job truthfully reported that only aggregate rollout JSON was available on Sam; clean sequential rollout traces with previous action, previous uncertainty, previous proprio, previous VLM features, and current candidate action were not available in a usable dataset. This remains future work.

## Previous Uncertainty Feature Assets

An inventory was written to `stage8_uncertainty_feature_assets_inventory.md`. Stage 5/6 rater checkpoints and predictions are reusable as baselines or ensembles. TDQC/failure-oriented artifacts should remain baselines only and must not become primary training data for this action-error method.

## Failures / Blockers / Caveats

- One backup job, `stage8_libero_pro_50eps_backup_bob`, was still running at the final snapshot. The completed analysis uses the robust 20 episodes/task LIBERO-PRO report plus completed 30-episode normal-LIBERO hard-task report.
- `stage8_normal_libero_50eps_backup_bob` was still pending. This does not invalidate the completed 30-episode hard-task benchmark.
- LIBERO-PRO logs still contain `FileNotFoundError` for some missing `.pruned_init` states. The runner skipped/continued on available suites; not all perturbation/task combinations were valid.
- The Stage 8 final report generated on Bob at `2026-05-17T00:34:03` was interim; this report is the consolidated local post-run report using later collected artifacts.
- Flowtrace and target sweeps ran after path fixes; earlier placeholder jobs should be ignored in favor of the `*_real_*` reports.
- Runtime deployment was not tested with a real world-model fallback. `E_conservative_switch_proxy` is SimVLA-only fallback, not a WM switch.

## What Worked

- SimVLA action-error uncertainty is feasible and scientifically meaningful for offline SimVLA candidate ranking.
- Context/seed-relative models now beat action-only clearly across controlled OOD splits.
- LIBERO-PRO rollout infrastructure works enough to run large execution benchmarks.
- Hard normal-LIBERO benchmark identifies real hard tasks, especially `libero_spatial task 5`.
- Calibration code produces useful risk separation and AUROC, even though bound coverage is not yet reliable.

## What Did Not Work Yet

- Uncertainty-guided seed deliberation did not reliably beat random seed choice in real LIBERO-PRO execution.
- Conservative switch proxy did not improve execution on the parsed subset.
- Flowtrace features did not improve pairwise ranking.
- Multi-expert L2 target did not beat single-expert L2 on average.
- History models were blocked by missing sequential rollout logs.
- Calibration is still undercovered on several controlled OOD/ID combinations.

## Recommended Next Steps

1. Instrument rollout logging at every decision step: context id, task, observation metadata, selected action, all seed actions, predicted uncertainty, reward delta, success/progress within H steps, proprio, and optional VLM features. This is required for progress targets and history models.
2. Train a progress/risk target, not only action L2: predict slow/failure risk or success-within-H from the current action and context.
3. Use `seed_relative_pairwise` / `full_engineered_simvla_focused` as the offline ranking baseline, and keep `context_gated_action` as the simple deployable baseline.
4. Do not use deliberation as a default runtime policy yet. If deploying anything now, use uncertainty as a warning/reject signal only.
5. Re-run calibration with small target-domain calibration pools and probability calibration for bad/slow actions once progress labels exist.
6. Keep LIBERO-PRO as the main benchmark, but fix or filter missing `.pruned_init` task configs so every reported perturbation suite has a known valid task set.
7. Use `libero_spatial task 5` as a normal-LIBERO stress test because all current policies fail it.

## Exact Artifacts To Read First

- This report: `/home/redafrix/tests/internship/codex_reports/ye/FINAL_SIMVLA_UNCERTAINTY_FULL_REPORT.md`
- Parsed summary: `/home/redafrix/tests/internship/codex_reports/ye/parsed_summary.json`
- LIBERO-PRO rollout: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md`
- Hard normal LIBERO: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_results.md`
- Switch analysis: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_switch_policy_results.md`
- Big model sweep: `sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_architecture_loss_big_sweep_results.md` plus `stage8_big_arch_*.json`
- Calibration: `sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep_results.md` and `stage8_calibration_real_q*.json`
- Flowtrace: `sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_real_results.md` and `stage7_flowtrace_*.json`
- Target sweep: `sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_*.json`

## Final Recommendation

**Proceed, but change the claim.** The project has a strong action-error rater for ranking SimVLA-generated candidate actions under controlled OOD, and context-aware models beat action-only. However, the current uncertainty is not yet validated as a robust runtime VLA/WM switch. The next claim should be: “SimVLA action-error uncertainty can rank candidate action reliability and identify risky actions; execution-risk deployment requires progress-target training and better calibration.”

Do not write a paper claim that deliberation improves execution based on this run; the LIBERO-PRO results do not support that strongly enough.

## Local Artifact List

```text
analyze_stage8.py
bob_bundle/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md
bob_bundle/asynchvla_ws/stage8_ultimate/configs/stage8_job_manifest.json
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_method.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_by_domain.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_smoke.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.json
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_threshold_transfer.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_final_72h_audit_before_expansion.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_final_72h_launch_report.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_final_plan_before_72h.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_final_smoke_before_72h_launch.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_full_orchestration_manifest_report.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_pilot_results.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_setup_and_smoke.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_machine_roles.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_manager_smoke.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_baseline.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_results.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_plan_and_smoke_status.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_scheduler_cleanup_final.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_status_check.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_switch_policy_results.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_three_day_queue_expansion.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_uncertainty_feature_assets_inventory.md
bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_watchdog_launch_report.md
bob_bundle/asynchvla_ws/stage8_ultimate/status/flowtrace_medium_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/flowtrace_medium_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/libero_pro_expanded_30eps_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/libero_pro_expanded_30eps_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/libero_pro_expanded_rollout_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/libero_pro_expanded_rollout_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/libero_pro_pilot_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/libero_pro_pilot_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_30eps_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_30eps_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_baseline_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_baseline_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_bob_cpu.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_bob_cpu.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_dependency_child.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_dependency_child.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json.fail_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_final_report_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_final_report_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_libero_pro_20eps_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_libero_pro_20eps_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_libero_pro_50eps_backup_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_switch_policy_extended_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_switch_policy_extended_bob.json.done_marker
bob_bundle/asynchvla_ws/stage8_ultimate/status/stage8_watchdog.pid
bob_bundle/asynchvla_ws/stage8_ultimate/status/switch_policy_analysis_bob.json
bob_bundle/asynchvla_ws/stage8_ultimate/status/switch_policy_analysis_bob.json.done_marker
bob_logs_list.txt
bob_logs_tail/all_bob_logs_tail.txt
bob_reports_list.txt
bob_results_files.txt
bob_stage8_status.json
parsed_summary.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage7_flowtrace_holdout_libero_object.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage7_flowtrace_holdout_libero_object.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage7_flowtrace_holdout_libero_spatial.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage7_flowtrace_holdout_libero_spatial.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage7_flowtrace_holdout_object_bowl.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage7_flowtrace_holdout_object_bowl.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_holdout_libero_object.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_holdout_libero_object.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_holdout_libero_spatial.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_holdout_libero_spatial.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_holdout_object_bowl.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_holdout_object_bowl.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_id_task_split.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_arch_id_task_split.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_architecture_loss_big_sweep_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_libero_goal.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_libero_goal.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_libero_object.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_libero_object.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_libero_spatial.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_libero_spatial.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_object_bowl.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_object_bowl.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_object_cabinet.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_object_cabinet.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_scene_kitchen_scene2.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_holdout_scene_kitchen_scene2.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_id_task_split.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_big_arch_id_task_split.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_deployable_method.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_method.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_by_domain.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q0.80.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q0.80.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q0.90.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q0.90.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q0.95.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q0.95.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q0.80.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q0.80.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q0.90.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q0.90.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q0.95.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q0.95.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_threshold_transfer.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_10_context_smoke.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_real_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_history_models.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_history_real_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_object_model_sweep.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_object_model_sweep.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_spatial_model_sweep.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_spatial_model_sweep.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_object_bowl_model_sweep.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_object_bowl_model_sweep.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_model_sweep_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_quantile_head_results.json
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_quantile_head_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_sam_path_fix_and_real_smokes.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_sam_training_smoke.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_target_comparison.md
sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_target_sweep_real_results.md
sam_bundle/asynchvla_ws/stage8_ultimate/status/architecture_loss_sweep_sam.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/architecture_loss_sweep_sam.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/calibration_mega_sam.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/calibration_mega_sam.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/flowtrace_experiments_sam.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/flowtrace_experiments_sam.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/history_models_sam.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/history_models_sam.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/smoke_sam_cpu.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/smoke_sam_cpu.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_arch_big.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_arch_big.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_real.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_real.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_sweep.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_sweep.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_flowtrace_real.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_flowtrace_real.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_history_real.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_history_real.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_model_sweep.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_model_sweep.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_target_real.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/stage8_sam_target_real.json.done_marker
sam_bundle/asynchvla_ws/stage8_ultimate/status/target_sweep_sam.json
sam_bundle/asynchvla_ws/stage8_ultimate/status/target_sweep_sam.json.done_marker
sam_logs_list.txt
sam_logs_tail/all_sam_logs_tail.txt
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_goal.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_goal.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_object.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_object.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_spatial.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_spatial.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_object_bowl.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_object_bowl.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_object_cabinet.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_object_cabinet.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_scene_kitchen_scene2.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_scene_kitchen_scene2.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_holdout_libero_object.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_holdout_libero_object.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_holdout_libero_spatial.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_holdout_libero_spatial.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_holdout_object_bowl.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_holdout_object_bowl.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_id_task_split.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_arch_id_task_split.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_libero_goal.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_libero_goal.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_libero_object.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_libero_object.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_libero_spatial.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_libero_spatial.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_object_bowl.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_object_bowl.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_object_cabinet.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_object_cabinet.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_scene_kitchen_scene2.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_holdout_scene_kitchen_scene2.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_id_task_split.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_big_arch_id_task_split.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_final_tiny_model_smoke.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_final_tiny_model_smoke.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_holdout_libero_object_model_sweep.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_holdout_libero_object_model_sweep.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_holdout_libero_spatial_model_sweep.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_holdout_libero_spatial_model_sweep.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_holdout_object_bowl_model_sweep.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_holdout_object_bowl_model_sweep.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_sam_training_smoke_portable.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage8_sam_training_smoke_portable.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_holdout_libero_object.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_holdout_libero_object.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_holdout_libero_spatial.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_holdout_libero_spatial.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_holdout_object_bowl.json
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_holdout_object_bowl.md
sam_outputs_stage7/asynchvla_ws/outputs/reports/stage7/stage7_sam_ready_check.md
sam_reports_list.txt
sam_results_files.txt
stage8_job_manifest.json
stage8_live_dashboard.md
write_final_report.py
```
