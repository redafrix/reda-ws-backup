# Key Results And Their Actual Meaning

This page is the human-curated map. The host indexes contain the exhaustive artifact inventory.

## Current Offline Detector Baseline

The selected historical detector is `v2_018_transformer_k16`: width 128, three transformer layers, four attention heads, and 16 history steps. Its inputs are action statistics, current and historical ACE values, and proprioception. On the selected historical OOD evaluation it reported 15.4% seen false alarms, 25.6% OOD false alarms, and 95.2% OOD failure detection.

Meaning: this establishes that the detector can classify risky trajectories offline. It does not by itself prove that replacing online actions improves task success.

Source: [current baseline report](source_reports/bob/reports/FIPER_WS_CURRENT_BASELINE_AND_ORGANIZATION_REPORT_20260528.md).

## Dean All-Task Offline Comparison

The all-task split used 4,191 episodes: 3,405 successes and 786 failures/timeouts.

| Detector | False alarms | Failure detection | Detection by 25% | Mean detection time |
|---|---:|---:|---:|---:|
| Base transformer | 14.2% | 95.8% | 54.0% | 0.231 |
| Base + raw 98D uncertainty | 16.8% | 97.5% | 67.1% | 0.207 |

Meaning: raw uncertainty improved detection and earliness but worsened false alarms. It was not an unambiguous replacement for the base detector.

Source: [Dean all-task report](source_reports/dean/experiments/dean_all_tasks_full_uncertainty_test_20260601/DEAN_ALL_TASKS_FULL_UNCERTAINTY_TEST_20260601.md).

## Dean Held-Out-Task OOD Comparison

The OOD split held out the final two task IDs from each suite and used all remaining valid episodes for training, validation, and calibration.

| Detector | OOD false alarms | OOD failure detection | Detection by 25% | Detection by 50% |
|---|---:|---:|---:|---:|
| Base transformer | 26.0% | 86.0% | 39.8% | 78.5% |
| Base + raw 98D uncertainty | 28.9% | 84.9% | 35.5% | 83.9% |

Meaning: direct 98D uncertainty input did not improve the overall OOD trade-off.

Source: [held-out-task report](source_reports/dean/experiments/dean_ood_last2_taskids_full_v1_20260601/DEAN_OOD_LAST2_TASKIDS_FULL_V1_20260601.md).

## Selected Top-8 Uncertainty Features

Feature ranking used only seen training and validation rows. The selected `unc_topk8` model adds eight uncertainty dimensions to the detector's static branch while preserving the temporal transformer.

| Split | Detector | False alarms | Failure detection | Detection by 25% |
|---|---:|---:|---:|---:|
| All tasks | Base | 14.2% | 95.8% | 54.0% |
| All tasks | Top-8 uncertainty | 15.0% | 97.5% | 65.0% |
| Held-out task IDs | Base | 26.0% | 86.0% | 39.8% |
| Held-out task IDs | Top-8 uncertainty | 23.0% | 89.2% | 37.6% |

Meaning: top-8 produced a useful offline trade-off and was retained for online evaluation. Offline gains still do not prove that intervention improves robot success.

Source: [top-K report](source_reports/dean/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/DEAN_UNCERTAINTY_TOPK_FEATURE_SWEEP_REPORT.md).

## Historical Four-Task Online Campaign

| Task | No-risk modified SimVLA | Modified SimVLA + base risk | Net gain |
|---|---:|---:|---:|
| Task 7 seen | 244/450 | 281/450 | +37 |
| Task 8 held-out | 210/429 | 213/429 | +3 |
| Object Task 2 | 172/450 | 184/450 | +12 |
| Object Task 0 | 395/552 | 399/552 | +4 |
| **Total** | **1,021/1,881** | **1,077/1,881** | **+56** |

Actual meaning: this campaign compared modified SimVLA `ckpt-60000` without risk intervention against the same modified checkpoint plus the base risk detector. Older reports incorrectly called the no-risk side vanilla SimVLA. Task 7 was individually persuasive; the other three task-level differences were small.

It therefore supports “the base risk policy may help modified SimVLA on some tasks,” not “risk-aware original SimVLA beats original SimVLA.”

Source: [corrected four-task summary](source_reports/batman/FOUR_TASK_RESULTS_SUMMARY.md).

## Canonical Bob And Dean Four-Policy Replication

All four policies ran back-to-back on 100 common reset seeds per host for `libero_object_object`, Task 0.

| Host | Original SimVLA | Modified ckpt-60000 | Base risk | Top-8 risk |
|---|---:|---:|---:|---:|
| Bob | 10% | 28% | 25% | 26% |
| Dean | 14% | 22% | 25% | 20% |

Meaning: modified SimVLA beat original SimVLA on this task. Neither risk-aware policy showed a stable replicated advantage over modified SimVLA. Cross-host differences are expected because different GPUs produce slightly different actions that amplify through closed-loop control.

Source: [canonical four-policy audit](source_reports/batman/CANONICAL_DEAN_BOB_4POLICY_FINAL_AUDIT_20260605.md).

## Historical Full-Chunk Task 7 Result

The full ten-action chunk baseline achieved 98/100 successes and failed seeds `1865224713` and `1517830958`. This was replicated and spot-checked. It used the modified checkpoint through the shared sampler default and is a different execution protocol from first-action receding horizon.

Meaning: full-chunk execution dramatically changed Task 7 performance. It is not evidence about original SimVLA and must not be pooled with first-action results.

## Goal-Object Chunk10 Diagnostic

On 2026-06-05, Gemini launched a disposable Bob diagnostic using the exact `libero_goal_object` reproduction bundle with 100 episodes, tasks 0-9 and init rows 0-9. Both policies used chunk10 open-loop execution with no risk detector, no ACE candidates, and no uncertainty features.

| Policy | Success | Mean environment steps |
|---|---:|---:|
| Modified SimVLA `ckpt-60000` | 80/100 | 130.92 |
| Official/original SimVLA | 78/100 | 132.38 |

Paired modified-vs-official result: 8 rescues / 6 regressions, net +2 for the modified checkpoint.

Meaning: this is a useful checkpoint sanity diagnostic, not a risk-aware result and not part of the H10 OOD proof chain.

## Current Active Work

As of the 2026-06-10 Codex audit, Bob's `libero_goal_object_ood` 0.3, 0.5, and q95 full-suite sweeps are complete. Sam is back online and idle after completing the V2B/V2C/V2D adaptive-horizon diagnostics. Dean is reachable via `dean-via-bob` and is running the selected-cap 100ep confirmation in tmux `dean_selected_cap_t03_c04_100ep_20260610`.

## Task 3 and 6 H10 Aggressive TopK8 Ablation (2026-06-08)

The H10-retrained TopK8 detector was tested at an aggressive **0.3 threshold** on Bob. It outperformed both the greedy baseline and the conservative q95 detector.

| Task | SimVLA (Greedy) | Risk-TopK8 (q95) | Risk-TopK8 (0.3 Aggr) | Net Gain (Aggr vs Greedy) |
|---|---:|---:|---:|---:|
| Task 3 | 17.0% | 17.0% | **19.0%** | +2.0 pts |
| Task 6 | 57.0% | 57.0% | **62.0%** | +5.0 pts |

Meaning: Lowering the risk threshold to 0.3 improved success on these specific precision tasks. The H10-retrained model was also verified as superior to the older Dean detector on Task 6.

> **Forensic correction (2026-06-09):** Tasks 3 and 6 were seen during detector training (1,368 and 1,423 training episodes respectively). These results are **in-distribution** (seen tasks, unseen seeds), not zero-shot generalization. The Synthesis report's claim of "98.9% intervention rate" for Task 3 was wrong—the true query-level modification rate is **1.04%** (29 out of 2,776 queries). For Task 6, the true rate is **22.98%** (443 out of 1,928 queries). See [TRUSTED_RESULTS_SUMMARY.md](TRUSTED_RESULTS_SUMMARY.md) for full details.

## OOD Goal-Swap Results (2026-06-08)

The aggressive TopK8 detector was tested on the `libero_goal_swap` OOD suite (Tasks 3, 6, 8) on Bob. The result was **net negative**.

| Metric | Baseline (modified SimVLA) | Risk-Aware (TopK8 @ 0.3) |
|---|---:|---:|
| Success Rate | 8/300 (2.7%) | 6/300 (2.0%) |
| Net Gain | — | **-2** |
| Rescues | — | 2 |
| Regressions | — | 4 |

Meaning: The risk detector caused regressions on configurations the base policy could not solve. Full-suite OOD goal-swap was never run (only 3 of 10 tasks tested). Do not claim OOD generalization from these results.

## OOD Goal-Object Full-Suite Results (2026-06-09/10)

The corrected `libero_goal_object_ood` full-suite assets contain 18 tasks. Bob and Sam both used the generated OOD BDDL folder `libero_goal_object_ood_temp` plus the `libero_goal_object_ood` init folder. The standard `libero_goal_object_ood` BDDL folder does not exist; the experiment-local runner maps the suite to `_temp`.

| Run | Original SimVLA | Modified SimVLA | Risk-Aware TopK8 | Main Meaning |
|---|---:|---:|---:|---|
| 10ep full suite, threshold 0.3 | 169/180 (93.9%) | 168/180 (93.3%) | 172/180 (95.6%) | Positive early signal only; weak N=10 evidence |
| 100ep full suite, threshold 0.3 | 1,668/1,800 (92.67%) | 1,718/1,800 (95.44%) | 1,713/1,800 (95.17%) | Mechanically valid but net negative vs modified baseline: 24 rescues / 29 regressions |
| 100ep full suite, threshold 0.5 | same baselines | 1,718/1,800 (95.44%) | 1,718/1,800 (95.44%) | Threshold 0.5 reduces modifications and removes the global loss, but does not outperform modified SimVLA |
| 100ep full suite, q95 | same baselines | 1,718/1,800 (95.44%) | 1,710/1,800 (95.00%) | Conservative q95 is mechanically valid but net negative: 10 rescues / 18 regressions |

Meaning: on full-suite OOD goal-object, the modified SimVLA checkpoint is already very strong. Current risk-aware action replacement has not beaten it globally at N=100.

## Dean Selected-Cap Gate Result (2026-06-10)

After the negative H1/H5/commit-gate diagnostics, a stricter action-replacement gate was tested on Dean. The policy still uses the TopK8 detector and candidates, but only accepts a replacement when the selected candidate's absolute risk score is at most `0.4`.

| Run | Modified SimVLA | Risk TopK8 selected-cap | Paired Outcome |
|---|---:|---:|---|
| Dean 10ep full suite, seeds 200-209 | 170/180 (94.4%) | 176/180 (97.8%) | 7 rescues, 1 regression, net +6 |
| Dean 100ep full suite, seeds 300-399 | 1,726/1,800 (95.9%) | 1,741/1,800 (96.7%) | 38 rescues, 23 regressions, net +15 |

Meaning: this remains the best verified risk-aware online result. Unlike the plain 0.3 aggressive threshold, the selected-cap gate is selective enough to beat the modified SimVLA baseline globally on Dean. The gain is real but task-dependent; task 12 remains a clear negative case. Forensic details are in `source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md`.

The follow-up delay30 replication on Dean completed with new seeds 400-499 and did **not** improve the result: Modified SimVLA scored 1,721/1,800 (95.61%) while selected-cap delay30 scored 1,718/1,800 (95.44%), with 19 rescues / 22 regressions, net -3. Delaying replacements before query 3 is therefore not a robust improvement.

## Bob Selected-Cap Replication Results (2026-06-12)

Bob reran the selected-cap family on the existing full-suite OOD 100ep seed block `10..109`, making the results directly comparable against the earlier Bob Original SimVLA, Modified SimVLA, and TopK8 threshold 0.3 runs.

| Policy | Success | Paired vs Modified | Total Mods | Meaning |
|---|---:|---:|---:|---|
| Original SimVLA | 1,668/1,800 (92.67%) | -50 | 0 | Weaker than modified checkpoint |
| Modified SimVLA | 1,718/1,800 (95.44%) | baseline | 0 | Strong baseline |
| TopK8 threshold 0.3 | 1,713/1,800 (95.17%) | -5 | 2,553 | Too many replacements |
| Selected-cap | 1,713/1,800 (95.17%) | -5 | 1,440 | Fewer modifications, no success gain |
| Selected-cap delay30 | 1,723/1,800 (95.72%) | +5 | 1,013 | Best Bob result, but small effect |

Meaning: on Bob, `delay30` produced a small positive result and reduced modifications substantially, but this does not overturn the Dean replication where delay30 was net negative. The stable conclusion is that selected-cap gating is useful for reducing bad replacements, while delay30 is seed/host dependent and should not be presented as a final robust method.

## Sam Adaptive-Horizon Diagnostics (2026-06-10)

These were tests of alternative ways to use the TopK8 risk score without replacing actions. The first V2 attempt is invalid because it skipped ACE candidate generation; V2B/V2C/V2D restored ACE candidate generation and only changed execution scheduling.

| Variant | Success | Net vs Modified SimVLA | Meaning |
|---|---:|---:|---|
| Modified SimVLA fixed H10 baseline | 171/180 (95.0%) | — | Baseline |
| V2B q95 adaptive H1/H10 | 167/180 (92.8%) | -4 | Frequent H1 replanning hurts |
| V2C q95 adaptive H5/H10 | 169/180 (93.9%) | -2 | H5 is less harmful but still worse |
| V2D first5/tail5 commit gate | 168/180 (93.3%) | -3 | Tail commit/replan gate still regresses too often |

Meaning: these are useful negative controls. Simply shortening or committing horizons based on the current TopK8 risk score does not solve the problem.

## Forensic Audit Status (2026-06-09)

An 8-step forensic audit of the H10 campaign was completed on 2026-06-09. See [FORENSIC_AUDIT_MAP.md](FORENSIC_AUDIT_MAP.md) for the full map of audit steps and findings. Key verdicts:

- **Model Identity:** PASS (0 mismatches across all 60 configs)
- **Suite Identity:** PASS (0 fallbacks, LIBERO-PRO confirmed)
- **Seed Leakage:** NONE (0% overlap)
- **Feature Leakage:** NONE
- **Task-Level Overlap:** YES (Tasks 3/6 seen during training)
- **Final Verdict:** RESULTS_MECHANICALLY_VALID_BUT_WEAK

Updated: 2026-06-10
