# Key Results And Their Actual Meaning

This page is the human-curated map. The host indexes contain the exhaustive artifact inventory.

> [!IMPORTANT]
> Current cross-machine entrypoint: [CROSS_MACHINE_EXPERIMENT_MAP_20260703.md](CROSS_MACHINE_EXPERIMENT_MAP_20260703.md). Use it first for the latest model/dataset/report paths and Git/large-artifact policy.

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

## Sam Timeout800 Selected-Cap Result (2026-06-16)

Sam reran the selected-cap policy on the full `libero_goal_object_ood` suite with `max_steps=800` instead of the usual 300-step timeout. This makes the run a separate robustness/recovery test, not a direct replacement for the 300-step benchmark tables.

| Policy | Success | Rate | Mean steps | Successful episodes >300 steps |
|---|---:|---:|---:|---:|
| Original SimVLA | 1,716/1,800 | 95.33% | 153.98 | 40 |
| Modified SimVLA | 1,744/1,800 | 96.89% | 138.68 | 27 |
| Selected-cap risk-aware | 1,754/1,800 | 97.44% | 133.02 | 19 |

Paired selected-cap result: 72 rescues / 34 regressions, net +38 vs Original SimVLA; 37 rescues / 27 regressions, net +10 vs Modified SimVLA.

Meaning: this is the strongest Sam full-suite OOD result so far. It supports selected-cap as a useful recovery/robustness gate under a longer timeout. It should be presented with the timeout caveat because the 800-step setting changes the evaluation question.

## OpenVLA-OFT Risk Experiments (2026-06-16 to 2026-06-19)

OpenVLA-OFT is tracked separately from SimVLA because it uses `moojink/openvla-7b-oft-finetuned-libero-goal`, native horizon 8, no ACE/uncertainty candidate generator, and an OpenVLA-specific action/proprio/history feature schema. Full navigation is in [OPENVLA_EXPERIMENT_MAP_20260619.md](OPENVLA_EXPERIMENT_MAP_20260619.md).

### Final OpenVLA Goal-Object Dataset

The current final OpenVLA goal-object dataset is:

`/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618`

It contains 1,890 complete episodes from `libero_goal_object`: 787 successes and 1,103 failures, reset seeds `100000..100188`, 10 tasks per seed. This is the dataset to use for the current OpenVLA goal-object risk model. The older 6,009-episode folder named `openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded` is actually plain `libero_goal` and should not be treated as the final goal-object/pro dataset.

### Offline OpenVLA Risk Results

| Model | Train data | Test data | Key result | Meaning |
|---|---|---|---|---|
| Old 800-step goal model | 6,009 plain `libero_goal` episodes | old heldout split | AUROC 0.9953, AUPRC 0.9909, best-F1 threshold 0.7100 | Strong in-domain plain-goal classifier |
| Old 800-step goal model | same | full final goal-object dataset | AUROC 0.8302, AUPRC 0.9789, 15.63% episode false alarms, 100% failure detected at threshold 0.7100 | Partial OOD transfer, not clean enough as final goal-object policy |
| Old 300-step goal model | same old data with failed rows capped | full final goal-object dataset | AUROC 0.6782, AUPRC 0.9562, 22.11% episode false alarms, 84.50% failure detected at threshold 0.8700 | Worse OOD transfer than old 800-step model |
| Final goal-object model | final 1,890 `libero_goal_object` episodes | internal split | Online runner uses `model_300steps.pt` with validation Q95 threshold 0.8049 | Current model for OpenVLA goal-object and OOD online tests |

Meaning: the old plain-goal risk model learns a general difficulty signal, but its thresholds do not transfer cleanly to goal-object. The dedicated final 1,890-episode goal-object model is the current OpenVLA risk model.

### OpenVLA Risk-Head Input Forensic Audit

The 2026-06-19 forensic audit resolved the task-id confusion. The Transformer risk heads used online do **not** explicitly use task id or timestep. Their checkpoint shapes are `hist_proj.weight=[128,21]`, `action_proj.weight=[128,7]`, and `static.0.weight=[128,43]`. Training/inference feature builders construct:

- History token 21: proprio 8 + executed action 7 + ACE/dummy first 6.
- Action token 7: predicted action vector.
- Static vector 43: action stats 28 + ACE/dummy 7 + current proprio 8.

Old `risk_mlp.pt` and `risk_gru.pt` baseline files in the old 6,000-episode directory did use a 25D vector with task one-hot and normalized timestep, but those baselines are not the Transformer risk model used in the online OpenVLA OOD run. Remaining caveat: task identity may still be implicit in proprio/start-state geometry.

### OpenVLA Online OOD Result

Bob completed the full 18-task `libero_goal_object_ood` online comparison:

`online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`

The run produced `3,600/3,600` episode summaries with zero malformed JSON rows, and the supervisor log ends with `DONE`.

| Policy | Horizon rule | Success | Meaning |
|---|---|---:|---|
| `openvla_basic` | fixed H=8 | 976/1800 = 54.22% | OpenVLA-OFT baseline executing the native 8-action chunk |
| `openvla_risk_horizon` | H=1 if risk >= 0.8049, otherwise H=8 | 1014/1800 = 56.33% | Same OpenVLA policy, but using the final 1,890-episode risk head to shrink the execution horizon when risky |

Interpretation: this is a real positive result for OpenVLA horizon control, but modest globally: `+38` successes over the fixed-H8 OpenVLA baseline across 1,800 paired OOD episodes. The main gains are concentrated on difficult tasks such as task 2, task 8, and task 16. This is not selected-cap action replacement; OpenVLA still has one deterministic action chunk, and the risk model changes only how many real actions are executed before re-querying.

Final per-task result:

| Task | `openvla_basic` | `openvla_risk_horizon` | Delta |
|---:|---:|---:|---:|
| 0 | 98/100 | 98/100 | 0 |
| 1 | 95/100 | 96/100 | +1 |
| 2 | 70/100 | 78/100 | +8 |
| 3 | 100/100 | 100/100 | 0 |
| 4 | 100/100 | 100/100 | 0 |
| 5 | 98/100 | 98/100 | 0 |
| 6 | 98/100 | 98/100 | 0 |
| 7 | 1/100 | 3/100 | +2 |
| 8 | 0/100 | 19/100 | +19 |
| 9 | 0/100 | 0/100 | 0 |
| 10 | 0/100 | 0/100 | 0 |
| 11 | 100/100 | 100/100 | 0 |
| 12 | 100/100 | 100/100 | 0 |
| 13 | 10/100 | 9/100 | -1 |
| 14 | 4/100 | 6/100 | +2 |
| 15 | 2/100 | 0/100 | -2 |
| 16 | 0/100 | 9/100 | +9 |
| 17 | 100/100 | 100/100 | 0 |

A separate fixed-H1 baseline exists on Bob in `openvla_ood_basic_h1_100ep_20260619`. The 2026-06-29 audit found it partial/interrupted at `1,720/1,800` rows, then Codex resumed it in tmux `openvla_ood_basic_h1_100ep_20260619` using the same script and output root. The resume log confirms `1720/1800 already complete` and first resumed episode `[1721/1800] policy=openvla_basic_h1 task=17 seed=30`. Until it reaches 1,800 rows, cite only the partial aggregate: `947/1720` (55.06%).

Partial H1 per-task rows as of 2026-06-29:

| Task | `openvla_basic_h1` |
|---:|---:|
| 0 | 84/100 |
| 1 | 93/100 |
| 2 | 74/100 |
| 3 | 98/100 |
| 4 | 94/100 |
| 5 | 98/100 |
| 6 | 100/100 |
| 7 | 16/100 |
| 8 | 23/100 |
| 9 | 0/100 |
| 10 | 0/100 |
| 11 | 100/100 |
| 12 | 92/100 |
| 13 | 33/100 |
| 14 | 3/100 |
| 15 | 17/100 |
| 16 | 4/100 |
| 17 | 18/20 |

## SimVLA Plain-Goal to Goal-Object Offline OOD Test

Sam completed the offline diagnostic:

`/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622`

This trains an H10 TopK8-style SimVLA Transformer risk head on the frozen plain `libero_goal` collection and evaluates it on the full transferred `libero_goal_object` H10 flat dataset from Bob.

| Dataset | Rows | Episodes | Success eps | Failure eps |
|---|---:|---:|---:|---:|
| Source train, plain `libero_goal` | 594,842 | 3,787 | 3,584 | 203 |
| Source val, plain `libero_goal` | 127,939 | 812 | 768 | 44 |
| Source test, plain `libero_goal` | 129,244 | 811 | 768 | 43 |
| OOD target, `libero_goal_object` | 235,466 | 17,409 | 14,005 | 3,404 |

The model uses no explicit task id or timestep input. Checkpoint shapes verify the intended schema: `hist_proj.weight=[128,21]`, `action_proj.weight=[128,7]`, `static.0.weight=[128,51]`.

| Threshold | Source AUROC | Source AUPRC | Source false alarm | Source failure det | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| best-val-F1 0.6014 | 0.9307 | 0.9051 | 17.06% | 97.67% | 0.7627 | 0.6998 | 4.59% | 78.91% | 0.15% | 7.61% |
| q95-success 0.5641 | 0.9307 | 0.9051 | 17.84% | 97.67% | 0.7627 | 0.6998 | 5.83% | 80.64% | 0.18% | 8.46% |
| fixed 0.5 | 0.9307 | 0.9051 | 20.18% | 97.67% | 0.7627 | 0.6998 | 8.27% | 83.96% | 0.32% | 9.75% |

Interpretation: the detector learns the plain `libero_goal` heldout split well, but transfer to `libero_goal_object` is weak for early warning. It detects many OOD failures eventually, but too late for a strong online policy: Det@25 is near zero and Det@50 stays under 10% at the main thresholds. This supports keeping the goal-object-trained detector for goal-object/OOD online work instead of relying on plain-goal-only training.

### Same-Metric Comparison Against Previous Best Offline Detector

The previous best offline detector numbers come from the historical selected `v2_018_transformer_k16` / TopK8-style result used as the main offline reference. The new Sam run uses the same style of detector inputs and the same reported metric definitions, but trains on plain `libero_goal` and tests on full `libero_goal_object`.

| Metric | Previous best offline detector | New plain-goal-trained detector | Direction |
|---|---:|---:|---|
| Seen/source false alarm | 15.4% | 17.06% | worse |
| OOD false alarm | 25.6% | 4.59% | lower, but because it is much less sensitive early |
| OOD failure detection | 95.2% | 78.91% | worse |
| OOD Det@25 | 26.2% | 0.15% | much worse |
| OOD Det@50 | 85.7% | 7.61% | much worse |
| Mean detection time/fraction | 0.332 | 0.722 | much later |

Conclusion: the new result is correct but negative. Plain `libero_goal` training does not replace the previous best detector for goal-object/OOD use because it fails the early-warning requirement.

## Dean Official-FIPER Materialized-Code Run (Verified)

Dean completed the strict official-code path on 2026-06-23 (verified forensically on 2026-06-24):

`/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622`

This run materialized official-format FIPER tensors by reconstructing observations from saved MuJoCo states, extracting 960D SimVLA/SmolVLM observation embeddings, and feeding those into the official RND/OE + entropy code path. The run completed successfully for both Option A (in-domain) and Option B (hygiene cross-domain), and the metrics were independently verified from raw score trajectories across all 5 seeds.

### 1. Unseen (OOD) Test Split (253 Rollouts: 211 Success, 42 Failure)

This is the OOD-only test split. It shows how the methods generalize to completely unseen task distributions.

| Option | Method | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never | Accuracy | TPR | TNR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Option B | entropy | 35.1% | 100.0% | 7.1% | 47.6% | 71.4% | 0.393 | 0.0% | 82.5% | 1.000 | 0.649 |
| Option B | rnd_oe | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% | 50.0% | 1.000 | 0.000 |
| Option B | Fusion (AND) | 38.9% | 97.6% | 11.9% | 52.4% | 78.6% | 0.314 | 2.4% | 79.4% | 0.976 | 0.611 |
| Option A (s42) | entropy | 35.1% | 100.0% | 7.1% | 47.6% | 71.4% | 0.393 | 0.0% | 82.5% | 1.000 | 0.649 |
| Option A (s42) | rnd_oe | 0.0% | 50.0% | 0.0% | 0.0% | 0.0% | 0.931 | 50.0% | 75.0% | 0.500 | 1.000 |
| Option A (s42) | Fusion (AND) | 0.0% | 45.2% | 0.0% | 0.0% | 0.0% | 0.933 | 54.8% | 72.6% | 0.452 | 1.000 |

* **Option B (Hygiene Cross-Domain)**: RND-OE visual novelty detection completely breaks down under domain shift, triggering constant alarms at step 0 (100% Success FA). This pulls down the AND Fusion to act like a sensitive entropy-only detector (38.9% Success FA, 97.6% Failure Det).
* **Option A (In-Distribution RND - Seed 42)**: RND-OE is highly overfitted to the in-domain training set. When presented with OOD environments, it is unresponsive early on (0% false alarms but 50% of failures are never detected, and those that are detected are triggered extremely late at a Mean Time of 0.93).

### 2. Seen (ID) Test Split (157 Rollouts: 136 Success, 21 Failure)

This is the ID-only test split, where the robot is evaluated on the same tasks it trained on (but new rollouts).

| Option | Method | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never | Accuracy | TPR | TNR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Option B | entropy | 33.1% | 100.0% | 23.8% | 47.6% | 85.7% | 0.296 | 0.0% | 83.5% | 1.000 | 0.669 |
| Option B | rnd_oe | 9.1% | 68.6% | 14.3% | 14.3% | 20.0% | 0.610 | 31.4% | 79.7% | 0.686 | 0.909 |
| Option B | Fusion (AND) | 4.4% | 66.7% | 7.6% | 8.6% | 17.1% | 0.679 | 33.3% | 81.1% | 0.667 | 0.956 |
| Option A (s42) | entropy | 33.1% | 100.0% | 23.8% | 47.6% | 85.7% | 0.296 | 0.0% | 83.5% | 1.000 | 0.669 |
| Option A (s42) | rnd_oe | 9.6% | 81.0% | 4.8% | 4.8% | 9.5% | 0.796 | 19.0% | 85.7% | 0.810 | 0.904 |
| Option A (s42) | Fusion (AND) | 5.1% | 81.0% | 0.0% | 0.0% | 9.5% | 0.812 | 19.0% | 87.9% | 0.810 | 0.949 |

* **RND-OE Works Correctly in ID**: Because the environment visual distributions are in-domain, RND-OE does not saturate. For Option B, it keeps Success FA down to 9.1%.
* **Fusion Gating Works in ID**: The AND Fusion successfully uses RND-OE to filter out entropy false alarms, bringing Success FA down to 4.4% (Option B) / 5.1% (Option A) while maintaining a balanced accuracy of 81.1% / 87.9%.

### Complete Re-evaluated Results Table for Our Method (`v2_018_transformer_k16` score q95 K3)
We re-evaluated our offline baseline `v2_018_transformer_k16` (conformal mass policy, $\alpha=0.15$) on the entire dataset splits (410 total test episodes):

| Test Split | Total Episodes Evaluated | Success FA | Failure Det (Recall) | Det@10 | Det@25 | Det@50 | Mean Detection Time | Never Detected | Balanced Accuracy |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Seen (ID)** | **157** | **15.44%** *(21 / 136)* | **100.00%** *(21 / 21)* | 0.00% | 76.19% | 90.48% | 0.246 | 0.00% | **92.28%** |
| **Unseen (OOD)** | **253** | **25.59%** *(54 / 211)* | **95.24%** *(40 / 42)* | 0.00% | 26.19% | 85.71% | 0.333 | 4.76% *(2 / 42)* | **84.82%** |

Source: [OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md](entries/official_fiper_rndoe_entropy_fold00_20260622/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md).

### Focused Horizon Diagnostic On Rescue Seeds

The focused diagnostic compared fixed-horizon basic OpenVLA against adaptive risk-aware OpenVLA on identical rescue seeds: task 8 seeds `[11,18,19,22,25]` and task 2 seeds `[12,14,27,43,49]`.

| Policy / horizon | Task 8 stove | Task 2 drawer | Combined |
|---|---:|---:|---:|
| Basic OpenVLA, fixed H=8 | 0/5 | 0/5 | 0/10 |
| Basic OpenVLA, fixed H=1 | 0/5 | 3/5 | 3/10 |
| Risk-aware OpenVLA, adaptive H=1/8 | 5/5 | 5/5 | 10/10 |

Interpretation: fixed H=1 helps some precision drawer cases but does not solve the stove task. The adaptive risk policy succeeds on this selected diagnostic set by using H=8 for progress and shrinking to H=1 when the risk score crosses the validation Q95 threshold 0.8049.

## Forensic Audit Status (2026-06-09)

An 8-step forensic audit of the H10 campaign was completed on 2026-06-09. See [FORENSIC_AUDIT_MAP.md](FORENSIC_AUDIT_MAP.md) for the full map of audit steps and findings. Key verdicts:

- **Model Identity:** PASS (0 mismatches across all 60 configs)
- **Suite Identity:** PASS (0 fallbacks, LIBERO-PRO confirmed)
- **Seed Leakage:** NONE (0% overlap)
- **Feature Leakage:** NONE
- **Task-Level Overlap:** YES (Tasks 3/6 seen during training)
- **Final Verdict:** RESULTS_MECHANICALLY_VALID_BUT_WEAK

Updated: 2026-06-25

## Pi0.5 Goal-Object H10 Risk Offline Model (2026-06-25)

The Pi0.5 offline risk head was trained on Bob (`PCROBOTUBUNTU02`) using the frozen complete-round dataset (rollout index 2..410, 4,090 episodes total).

| Split | Episodes | Successes | Failures | Step AUROC | Step AUPRC | Step FPR | Step FNR |
|---|---|---|---|---|---|---|---|
| Train | 2,854 | 2,304 | 550 | — | — | — | — |
| Val | 606 | 491 | 115 | — | — | — | — |
| Test | 630 | 503 | 127 | 0.9534 | 0.9728 | 10.53% | 10.88% |

Conformal calibration thresholds on validation split:
* **Best F1 Threshold:** 0.4800
* **Q90 Score Threshold:** 0.4817
* **Q95 Score Threshold:** 0.7218
* **Q99 Score Threshold:** 0.9586

Episode-level test evaluation table:

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1  |  23.46% |    99.21% |  78.0% |  96.1% |  99.2% | 0.060 |   0.8% |
| q90          |  23.46% |    99.21% |  78.0% |  96.1% |  99.2% | 0.060 |   0.8% |
| q95          |  12.33% |    99.21% |  66.1% |  89.8% |  99.2% | 0.084 |   0.8% |
| q99          |   3.38% |    97.64% |  49.6% |  70.1% |  85.0% | 0.168 |   2.4% |
| q95_K3       |   9.74% |    99.21% |  65.4% |  89.0% |  98.4% | 0.088 |   0.8% |
| q99_K3       |   3.18% |    97.64% |  48.8% |  67.7% |  84.3% | 0.175 |   2.4% |
| q95_mass_1   |   6.96% |    99.21% |  53.5% |  87.4% |  98.4% | 0.109 |   0.8% |
| q95_mass_5   |   4.37% |    99.21% |  48.8% |  73.2% |  96.9% | 0.152 |   0.8% |
| q95_mass_10  |   2.98% |    99.21% |  48.8% |  63.8% |  92.1% | 0.190 |   0.8% |
| q95_mass_20  |   1.99% |    99.21% |  48.8% |  54.3% |  86.6% | 0.250 |   0.8% |
| q95_mass_50  |   0.60% |    98.43% |   0.0% |  48.8% |  65.4% | 0.406 |   1.6% |

Meaning: Pi0.5 data collection was stopped early at 4,090 episodes instead of the 10,000 target. Training a temporal sequence risk model on this dataset results in a highly effective risk head with step-level AUPRC 0.9728 and AUROC 0.9534. Conformal mass thresholding (`q95_mass_10`) achieves an optimal operational trade-off of 2.98% False Alarm rate with 99.21% Failure Detection (with detection happening at a mean time fraction of 0.190).

Verification:
* **No explicit task id input:** Yes.
* **No explicit timestep input:** Yes.
* **Train/Val/Test Split grouped by episode:** Yes.
* **Normalization on train split only:** Yes.
* **Thresholds calibrated on val split only:** Yes.
* **ACE is real and non-zero:** Yes (computed from candidate flows).
* **Uncertainty TopK8 masked:** Yes (exactly zero vector because Pi0.5 weights were unmodified).

Source: [Pi0.5 Goal-Object H10 Risk Model Offline Report](file:///home/redafrix/.gemini/antigravity-cli/brain/09273eaa-9875-45a1-a3ac-916fc99da365/PI05_GOAL_OBJECT_H10_RISK_OFFLINE_REPORT_20260625.md).


### Dean Official FIPER Matched-FA Caveat (2026-06-25 Codex audit)

The Dean official-FIPER ablation remains trusted, but the interpretation is nuanced. RND-OE novelty alone fails on OOD due immediate visual novelty saturation. The canonical Option B Fusion row has Success FA 38.9%, Failure Det 97.6%, Det@25 52.4%, Det@50 78.6%, Mean Time 0.314. Our `v2_018` score q95 K3 row has Success FA 25.59%, Failure Det 95.24%, Det@25 26.19%, Det@50 85.71%, Mean Time 0.333.

A full FIPER OOD sweep shows FIPER/entropy can match or beat our failure detection at similar false alarm but detects later, e.g. entropy window 37, quantile 0.97, `tvt_quantile`: Success FA 23.7%, Failure Det 100.0%, Mean Time 0.531. Therefore the defensible claim is: our model is stronger as an early-warning temporal risk detector at the selected operating point; official FIPER is not uniformly bad, but its RND-OE novelty component is brittle and its competitive low-FA points are late.

### Bob Official SimVLA `libero_goal_object` H10 Basic 500ep Reference (2026-06-26)

This is the byte-identical official `libero_goal_object` reference run requested to compare the local modified suite against the official LIBERO task files. The local modified `libero_goal_object` was not overwritten; official BDDL/init files were copied into separate `libero_goal_object_official` folders.

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `simvla_official_libero_goal_object_h10_basic_500ep_20260626` |
| **Output path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_basic_500ep_20260626` |
| **Script** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/scripts/run_simvla_official_goal_object_h10_50ep_20260626.py` |
| **Log** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/logs/simvla_official_goal_object_h10_basic_500ep_20260626/run.log` |
| **Coverage** | 50 init states per task, tasks 0..9; no duplicate `(task_id, initial_state_index)` pairs |
| **Final result** | 422/500 successes = 84.40%; 78 failures |

| Task | Stem | Success | Fail | Success Rate |
| ---: | :--- | ---: | ---: | ---: |
| 0 | open_the_middle_drawer_of_the_cabinet | 49 | 1 | 98.00% |
| 1 | put_the_bowl_on_the_stove | 49 | 1 | 98.00% |
| 2 | put_the_wine_bottle_on_top_of_the_cabinet | 50 | 0 | 100.00% |
| 3 | open_the_top_drawer_and_put_the_bowl_inside | 13 | 37 | 26.00% |
| 4 | put_the_bowl_on_top_of_the_cabinet | 49 | 1 | 98.00% |
| 5 | push_the_plate_to_the_front_of_the_stove | 50 | 0 | 100.00% |
| 6 | put_the_cream_cheese_in_the_bowl | 35 | 15 | 70.00% |
| 7 | turn_on_the_stove | 50 | 0 | 100.00% |
| 8 | put_the_bowl_on_the_plate | 49 | 1 | 98.00% |
| 9 | put_the_wine_bottle_on_the_rack | 28 | 22 | 56.00% |

### Dean No-Retrain Official FIPER vs H10 TopK8 on Same 180ep Goal-Object-OOD Dataset (2026-06-26 audit)

This is the clean no-retrain/no-recalibration audit requested for paper ablation. It uses the same OOD dataset as the H10 TopK8 detector-only audit: 180 episodes, 149 successes, 31 failures, 44,630 query rows, 10 episodes per task across the official 18-task `libero_goal_object_ood` suite. The official FIPER materialization contains 830 rollouts total: 500 seen train successes, 150 seen calibration successes, and exactly 180 OOD test rollouts. Verification passed: calibration/test overlap is zero, ID/OOD overlap is zero, and the TopK8 row-label order in `scores.npz` matches the JSONL summaries.

| Artifact | Path |
| :--- | :--- |
| OOD dataset | `/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` |
| Official FIPER CSV | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/official_fiper_ablation_results.csv` |
| Official FIPER validation | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/VALIDATION_SUMMARY.json` |
| TopK8 audited sweep | `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_audited_threshold_sweep/audited_policy_metrics.csv` |
| Combined audit report | `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_audited_threshold_sweep/AUDITED_TOPK8_AND_OFFICIAL_FIPER_OOD_REPORT_20260626.md` |

Official FIPER no-retrain result on the OOD test split:

| Method | Window | Style | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | :---: | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| entropy | 29 | actual steps | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.036 | 0.0% |
| rnd_oe | 48 | actual steps | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.001 | 0.0% |
| rnd_oe_and_entropy | 48/16 | actual steps | 100.0% | 100.0% | 96.8% | 100.0% | 100.0% | 0.051 | 0.0% |
| rnd_oe_and_entropy | 48/16 | max-300 forensic | 100.0% | 100.0% | 25.8% | 96.8% | 100.0% | 0.133 | 0.0% |

H10 TopK8 no-retrain threshold sweep on the same OOD rows:

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| saved `q95_mass_0.15` | 96.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.027 | 0.0% |
| `q95_mass_10` | 34.9% | 100.0% | 12.9% | 93.5% | 96.8% | 0.157 | 0.0% |
| `q95_mass_20` | 20.8% | 96.8% | 3.2% | 90.3% | 96.8% | 0.166 | 3.2% |
| `q95_mass_50` | 2.7% | 96.8% | 0.0% | 16.1% | 90.3% | 0.288 | 3.2% |
| `q99_mass_0.5` | 28.9% | 93.5% | 9.7% | 90.3% | 93.5% | 0.140 | 6.5% |
| `q99_mass_1` | 20.8% | 93.5% | 6.5% | 90.3% | 90.3% | 0.171 | 6.5% |

Interpretation: on this strict OOD-only no-retrain comparison, official FIPER is genuinely worse as a deployment alarm because every variant false-alarms on every successful OOD episode. The saved online TopK8 threshold is also badly under-calibrated for this dataset, but threshold sweeping exposes usable trade-offs that FIPER does not provide on the same split.

## Pi0.5 Official `libero_goal_swap` 50ep Online + Offline Audit (2026-06-26)

Bob completed the official `libero_goal_swap` 10-task, 50-seed-per-task online run comparing basic Pi0.5 H10 against selected-cap Pi0.5 risk. The run also saved query/step records for offline OOD scoring.

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625` |
| **Online root** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625` |
| **Offline result path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625` |
| **Threshold sweep JSON** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625/old_with_task9_q95_mass_threshold_sweep_20260626.json` |
| **Suite / seeds** | `libero_goal_swap`, tasks 0-9, 50 paired seeds per task |
| **Max steps / horizon** | Max 300 env steps, H10 execution |
| **Policies** | `pi05_basic_h10`; `pi05_risk_selected_cap_topk8_h10` |
| **Trust** | TRUST complete online run + detector-only offline threshold audit. Results show weak transfer to `goal_swap`; selected-cap is active but only modestly positive. |

Online success:

| Policy | Done | Success | Fail | Success Rate |
| :--- | ---: | ---: | ---: | ---: |
| `pi05_basic_h10` | 500 | 161 | 339 | 32.20% |
| `pi05_risk_selected_cap_topk8_h10` | 500 | 166 | 334 | 33.20% |

Per-task online comparison:

| Task | Instruction | Basic SR | Risk SR | Delta |
| ---: | :--- | :---: | :---: | ---: |
| 0 | open the middle drawer of the cabinet | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 1 | put the bowl on the stove | 41/50 = 82.00% | 41/50 = 82.00% | 0 |
| 2 | put the wine bottle on top of the cabinet | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 3 | open the top drawer and put the bowl inside | 48/50 = 96.00% | 49/50 = 98.00% | +1 |
| 4 | put the bowl on top of the cabinet | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 5 | push the plate to the front of the stove | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 6 | put the cream cheese in the bowl | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 7 | turn on the stove | 50/50 = 100.00% | 49/50 = 98.00% | -1 |
| 8 | put the bowl on the plate | 22/50 = 44.00% | 26/50 = 52.00% | +4 |
| 9 | put the wine bottle on the rack | 0/50 = 0.00% | 1/50 = 2.00% | +1 |

Selected-cap action modifications:

| Group | Episodes | Action Changes | Changed Episodes | Avg Changes / Episode |
| :--- | ---: | ---: | ---: | ---: |
| All risk episodes | 500 | 1306 | 383 | 2.61 |
| Successful risk episodes | 166 | 289 | 127 | 1.74 |
| Failed risk episodes | 334 | 1017 | 256 | 3.04 |

Matched by `(task_id, reset_seed)`, the selected-cap policy rescued 18 basic failures but regressed 13 basic successes, for a net gain of +5 successes. Most action modifications happened in failed episodes: 1017 / 1306 = 77.9%.

Dense offline threshold sweep, using only the Pi0.5 risk head trained with task 9 (`old_with_task9`) and the validation-calibrated `q95 = 0.7218163013458249`:

| Query Source | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Basic Pi0.5 | `q95_mass_0.05` | 100.00% | 100.00% | 100.0% | 100.0% | 100.0% | 0.033 | 0.0% |
| Basic Pi0.5 | `q95_mass_0.1` | 100.00% | 100.00% | 100.0% | 100.0% | 100.0% | 0.041 | 0.0% |
| Basic Pi0.5 | `q95_mass_0.15` | 100.00% | 100.00% | 98.8% | 99.1% | 99.7% | 0.054 | 0.0% |
| Basic Pi0.5 | `q95_mass_0.2` | 99.38% | 99.12% | 78.5% | 87.0% | 98.2% | 0.103 | 0.9% |
| Basic Pi0.5 | `q95_mass_0.3` | 93.79% | 95.58% | 40.1% | 49.0% | 88.8% | 0.230 | 4.4% |
| Basic Pi0.5 | `q95_mass_0.4` | 57.76% | 92.92% | 31.0% | 34.5% | 83.5% | 0.281 | 7.1% |
| Basic Pi0.5 | `q95_mass_0.5` | 45.96% | 89.68% | 29.5% | 30.7% | 77.9% | 0.298 | 10.3% |
| Basic Pi0.5 | `q95_mass_0.75` | 35.40% | 85.55% | 14.7% | 30.1% | 67.3% | 0.337 | 14.5% |
| Basic Pi0.5 | `q95_mass_1` | 31.06% | 83.19% | 0.0% | 29.5% | 59.6% | 0.385 | 16.8% |
| Basic Pi0.5 | `q95_mass_1.25` | 19.88% | 81.12% | 0.0% | 29.5% | 56.9% | 0.425 | 18.9% |
| Basic Pi0.5 | `q95_mass_1.5` | 4.97% | 77.58% | 0.0% | 29.5% | 56.0% | 0.452 | 22.4% |
| Basic Pi0.5 | `q95_mass_2` | 0.62% | 69.62% | 0.0% | 0.0% | 42.2% | 0.488 | 30.4% |
| Basic Pi0.5 | `q95_mass_2.5` | 0.62% | 64.01% | 0.0% | 0.0% | 29.8% | 0.528 | 36.0% |
| Basic Pi0.5 | `q95_mass_3` | 0.00% | 60.18% | 0.0% | 0.0% | 29.5% | 0.568 | 39.8% |
| Basic Pi0.5 | `q95_mass_4` | 0.00% | 53.98% | 0.0% | 0.0% | 14.2% | 0.658 | 46.0% |
| Basic Pi0.5 | `q95_mass_5` | 0.00% | 48.38% | 0.0% | 0.0% | 0.0% | 0.755 | 51.6% |
| Risk Pi0.5 | `q95_mass_0.05` | 100.00% | 100.00% | 100.0% | 100.0% | 100.0% | 0.033 | 0.0% |
| Risk Pi0.5 | `q95_mass_0.1` | 100.00% | 100.00% | 100.0% | 100.0% | 100.0% | 0.041 | 0.0% |
| Risk Pi0.5 | `q95_mass_0.15` | 100.00% | 100.00% | 98.5% | 99.4% | 100.0% | 0.054 | 0.0% |
| Risk Pi0.5 | `q95_mass_0.2` | 100.00% | 99.10% | 77.2% | 84.7% | 99.1% | 0.104 | 0.9% |
| Risk Pi0.5 | `q95_mass_0.3` | 92.17% | 95.21% | 41.0% | 51.2% | 91.3% | 0.223 | 4.8% |
| Risk Pi0.5 | `q95_mass_0.4` | 64.46% | 91.62% | 29.9% | 35.6% | 82.6% | 0.271 | 8.4% |
| Risk Pi0.5 | `q95_mass_0.5` | 53.01% | 89.82% | 29.6% | 29.9% | 77.2% | 0.300 | 10.2% |
| Risk Pi0.5 | `q95_mass_0.75` | 41.57% | 86.83% | 14.7% | 29.6% | 66.8% | 0.346 | 13.2% |
| Risk Pi0.5 | `q95_mass_1` | 33.13% | 85.03% | 0.0% | 29.6% | 60.8% | 0.396 | 15.0% |
| Risk Pi0.5 | `q95_mass_1.25` | 20.48% | 80.84% | 0.0% | 29.6% | 58.4% | 0.422 | 19.2% |
| Risk Pi0.5 | `q95_mass_1.5` | 4.82% | 76.05% | 0.0% | 29.6% | 56.3% | 0.439 | 24.0% |
| Risk Pi0.5 | `q95_mass_2` | 0.60% | 68.26% | 0.0% | 0.0% | 42.8% | 0.469 | 31.7% |
| Risk Pi0.5 | `q95_mass_2.5` | 0.60% | 64.37% | 0.0% | 0.0% | 29.9% | 0.516 | 35.6% |
| Risk Pi0.5 | `q95_mass_3` | 0.60% | 59.88% | 0.0% | 0.0% | 29.6% | 0.549 | 40.1% |
| Risk Pi0.5 | `q95_mass_4` | 0.60% | 57.49% | 0.0% | 0.0% | 14.4% | 0.666 | 42.5% |
| Risk Pi0.5 | `q95_mass_5` | 0.00% | 52.69% | 0.0% | 0.0% | 0.0% | 0.770 | 47.3% |

Interpretation: no threshold gives the strong in-distribution Pi0.5 trade-off on `libero_goal_swap`. `q95_mass_1` to `q95_mass_1.25` is the most balanced range if false alarms must be reduced, but it detects only about 81-85% of failures and misses early Det@10 entirely. Lower thresholds detect failures but alarm on almost every success.

## Pi0.5 Official `libero_goal_object_ood` 18-task 100ep Online + Offline Audit (2026-06-27, re-audited 2026-06-29)

Bob completed the larger official 18-task OOD run with 100 paired seeds per task and max 300. This is the full back-to-back Pi0.5 basic-vs-selected-cap run that also saved records for offline detector scoring.

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625` |
| **Online root** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625` |
| **Offline result path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_ood_18task_100ep_two_heads_eval_20260625` |
| **Suite / seeds** | official `libero_goal_object_ood`, tasks 0-17, 100 paired seeds per task |
| **Max steps / horizon** | Max 300 env steps, H10 execution |
| **Policies** | `pi05_basic_h10`; `pi05_risk_selected_cap_topk8_h10` |
| **Trust** | TRUST complete online/offline audit. The selected-cap policy is active but net-negative on this easy official OOD sample. |

Online success:

| Policy | Done | Success | Fail | Success Rate | Action Changes |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `pi05_basic_h10` | 1800 | 1754 | 46 | 97.44% | 0 |
| `pi05_risk_selected_cap_topk8_h10` | 1800 | 1736 | 64 | 96.44% | 759 |

Per-task online comparison:

| Task | Basic SR | Risk SR | Delta |
| ---: | :---: | :---: | ---: |
| 0 | 100/100 = 100.00% | 96/100 = 96.00% | -4 |
| 1 | 99/100 = 99.00% | 96/100 = 96.00% | -3 |
| 2 | 91/100 = 91.00% | 84/100 = 84.00% | -7 |
| 3 | 97/100 = 97.00% | 100/100 = 100.00% | +3 |
| 4 | 96/100 = 96.00% | 96/100 = 96.00% | 0 |
| 5 | 99/100 = 99.00% | 100/100 = 100.00% | +1 |
| 6 | 99/100 = 99.00% | 100/100 = 100.00% | +1 |
| 7 | 100/100 = 100.00% | 100/100 = 100.00% | 0 |
| 8 | 100/100 = 100.00% | 100/100 = 100.00% | 0 |
| 9 | 100/100 = 100.00% | 100/100 = 100.00% | 0 |
| 10 | 100/100 = 100.00% | 98/100 = 98.00% | -2 |
| 11 | 98/100 = 98.00% | 94/100 = 94.00% | -4 |
| 12 | 95/100 = 95.00% | 94/100 = 94.00% | -1 |
| 13 | 96/100 = 96.00% | 99/100 = 99.00% | +3 |
| 14 | 100/100 = 100.00% | 97/100 = 97.00% | -3 |
| 15 | 87/100 = 87.00% | 90/100 = 90.00% | +3 |
| 16 | 97/100 = 97.00% | 93/100 = 93.00% | -4 |
| 17 | 100/100 = 100.00% | 99/100 = 99.00% | -1 |

Selected-cap action modifications:

| Group | Episodes | Action Changes | Changed Episodes | Avg Changes / Episode |
| :--- | ---: | ---: | ---: | ---: |
| All risk episodes | 1800 | 759 | 529 | 0.42 |
| Successful risk episodes | 1736 | 645 | 490 | 0.37 |
| Failed risk episodes | 64 | 114 | 39 | 1.78 |

Interpretation: the suite is much easier for Pi0.5 than the earlier `goal_swap` audit, so the baseline is already extremely high. Selected-cap changes are not concentrated enough on only failures and produce a net -18 success regression on this run.

## Official FIPER OOD180 Threshold Sweep (Dean, 2026-06-29)

Dean ran a no-retrain threshold sweep for the official FIPER signals on the same 180-episode official `libero_goal_object_ood` dataset used for the H10 TopK8 comparison. This is a diagnostic operating-curve sweep on the OOD test set, not the unchanged FIPER deployment point.

| Property | Value |
| :--- | :--- |
| **Experiment path** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629` |
| **Report** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629/OFFICIAL_FIPER_OOD180_THRESHOLD_SWEEP_20260629.md` |
| **CSV** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629/official_fiper_ood180_threshold_sweep.csv` |
| **Dataset** | Same 180 OOD episodes: 149 success / 31 failure |
| **Training** | No retrain; reused official FIPER RND checkpoints |
| **Signals swept** | `entropy`, `rnd_oe`, `rnd_oe_and_entropy` |
| **Official deployment point** | `any_1`: normalized `tvt_quantile q=0.95` score crosses 1.0 |

Selected rows:

| Method | Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `entropy` | `any_1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.036 | 0.0% |
| `entropy` | `mass_above_1_100` | 20.1% | 100.0% | 0.0% | 96.8% | 100.0% | 0.168 | 0.0% |
| `entropy` | `mass_above_1_200` | 4.0% | 100.0% | 0.0% | 71.0% | 100.0% | 0.247 | 0.0% |
| `rnd_oe` | `any_1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.001 | 0.0% |
| `rnd_oe` | `any_5` | 5.4% | 6.5% | 6.5% | 6.5% | 6.5% | 0.812 | 93.5% |
| `rnd_oe` | `mass_above_1_200` | 85.6% | 100.0% | 6.5% | 100.0% | 100.0% | 0.109 | 0.0% |
| `rnd_oe_and_entropy` | `any_1` | 100.0% | 100.0% | 96.8% | 100.0% | 100.0% | 0.051 | 0.0% |
| `rnd_oe_and_entropy` | `any_1.5` | 53.0% | 100.0% | 51.6% | 90.3% | 96.8% | 0.152 | 0.0% |
| `rnd_oe_and_entropy` | `mass_above_1_20` | 31.5% | 100.0% | 3.2% | 96.8% | 96.8% | 0.152 | 0.0% |
| `rnd_oe_and_entropy` | `mass_above_1_50` | 6.0% | 100.0% | 0.0% | 80.6% | 96.8% | 0.221 | 0.0% |
| `rnd_oe_and_entropy` | `mass_above_1_100` | 2.7% | 96.8% | 0.0% | 38.7% | 96.8% | 0.288 | 3.2% |

Interpretation: the official deployment point still fails by false-alarming on every OOD success. The OOD threshold sweep shows that FIPER can be forced into lower false-alarm operating points, but only by using OOD-test-set operating-curve thresholds and usually sacrificing early detection. The best-looking diagnostic row is `rnd_oe_and_entropy mass_above_1_50` (6.0% FA / 100.0% Det / Det@50 96.8%), but it is not the unchanged paper deployment rule.

### Cap-300 Relabel Sweep

Dean also reran the same no-retrain official FIPER threshold sweep under the cap-300 label rule: truncate scores to the first 300 steps and relabel an episode as success only if it originally succeeded by step 300. This converts the 180-episode OOD set to 143 successes / 37 failures.

| Property | Value |
| :--- | :--- |
| **Experiment path** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_cap300_20260629` |
| **Report** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_cap300_20260629/OFFICIAL_FIPER_OOD180_CAP300_THRESHOLD_SWEEP_20260629.md` |
| **CSV** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_cap300_20260629/official_fiper_ood180_cap300_threshold_sweep.csv` |
| **Dataset labels** | 143 cap-300 successes / 37 cap-300 failures |

Selected cap-300 rows:

| Method | Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `entropy` | `any_1` | 100.0% | 100.0% | 81.1% | 100.0% | 100.0% | 0.097 | 0.0% |
| `entropy` | `mass_above_1_100` | 16.8% | 100.0% | 0.0% | 0.0% | 78.4% | 0.453 | 0.0% |
| `entropy` | `mass_above_1_200` | 0.0% | 91.9% | 0.0% | 0.0% | 0.0% | 0.638 | 8.1% |
| `rnd_oe` | `any_1` | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.003 | 0.0% |
| `rnd_oe` | `any_5` | 5.2% | 7.0% | 0.0% | 7.0% | 7.0% | 0.832 | 93.0% |
| `rnd_oe_and_entropy` | `any_1` | 100.0% | 100.0% | 27.0% | 97.3% | 100.0% | 0.137 | 0.0% |
| `rnd_oe_and_entropy` | `any_1.5` | 51.0% | 91.9% | 0.0% | 21.6% | 78.4% | 0.324 | 8.1% |
| `rnd_oe_and_entropy` | `mass_above_1_20` | 28.7% | 91.9% | 0.0% | 2.7% | 78.4% | 0.365 | 8.1% |
| `rnd_oe_and_entropy` | `mass_above_1_50` | 2.8% | 91.9% | 0.0% | 0.0% | 59.5% | 0.518 | 8.1% |
| `rnd_oe_and_entropy` | `mass_above_1_100` | 0.0% | 78.4% | 0.0% | 0.0% | 0.0% | 0.701 | 21.6% |

Interpretation: under cap-300 relabeling, the apparently strong full-length FIPER mass-threshold rows weaken substantially. Low false alarm thresholds miss many cap-300 failures or detect them too late; the unchanged official deployment point still false-alarms on every success.

### H10 TopK8 Extended Cap-300 Sweep on Same OOD180 Dataset

Dean then reran our H10 TopK8 detector on the same cap-300 labels with a wider threshold sweep. This does not retrain the model and does not recalibrate the model on OOD; it reuses saved row scores from the H10 TopK8 evaluation and sweeps episode-level alarm policies.

| Property | Value |
| :--- | :--- |
| **Experiment path** | `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629` |
| **Report** | `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629/TOPK8_OOD180_CAP300_EXTENDED_SWEEP_20260629.md` |
| **CSV** | `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629/topk8_ood180_cap300_extended_sweep.csv` |
| **Dataset labels** | 143 cap-300 successes / 37 cap-300 failures; 28,031 retained rows |
| **Saved row thresholds** | q95 = 0.615541; q99 = 0.966594; saved online mass = 0.15 |

Selected rows:

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `q95_mass_0.15` | 95.8% | 100.0% | 62.2% | 100.0% | 100.0% | 0.081 | 0.0% |
| `q95_mass_10` | 33.6% | 91.9% | 2.7% | 13.5% | 86.5% | 0.338 | 8.1% |
| `q95_mass_20` | 18.9% | 91.9% | 0.0% | 0.0% | 83.8% | 0.437 | 8.1% |
| `q95_mass_40` | 1.4% | 83.8% | 0.0% | 0.0% | 10.8% | 0.592 | 16.2% |
| `q99_mass_2` | 1.4% | 83.8% | 0.0% | 0.0% | 27.0% | 0.548 | 16.2% |
| `fixed_0.5_mass_30` | 17.5% | 91.9% | 0.0% | 0.0% | 83.8% | 0.445 | 8.1% |
| `fixed_0.5_mass_40` | 15.4% | 91.9% | 0.0% | 0.0% | 48.6% | 0.514 | 8.1% |
| `fixed_0.5_mass_50` | 6.3% | 86.5% | 0.0% | 0.0% | 10.8% | 0.573 | 13.5% |

Interpretation: the strongest balanced cap-300 diagnostic point found for our method is `fixed_0.5_mass_30` (17.5% Success FA / 91.9% Failure Det / 83.8% Det@50). The near-zero false-alarm region (`q99_mass_2` or `q95_mass_40`) preserves 83.8% detection but becomes late.

### H10 TopK8 Calibration Audit: Seen-Only and Distinct-OOD Calibration

On 2026-06-29, Codex audited whether the saved H10 TopK8 detector can support the strict paper protocol: train/calibrate only outside the final official OOD180 test set, then test once on unseen `libero_goal_object_ood`.

| Calibration Source | Policy | Test Set | Success FA | Failure Det | Det@25 | Det@50 | Mean Time | Verdict |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| seen `success_calib_seen` + `success_val_seen` | `q99_seen_success_FA010` | OOD180 max-800 | 57.7% | 100.0% | 90.3% | 96.8% | 0.147 | Best strict seen-only row found, but false alarms still too high |
| seen + `failure_val_seen` supervised calibration | `q99_seen_supervised_FAle25` | OOD180 max-800 | 66.4% | 100.0% | 93.5% | 100.0% | 0.106 | Failures help earliness but not false alarms |
| distinct OOD calibration, not test OOD180 | `cal_q95_oodcal_success_FA01` | OOD180 max-800 | 53.7% | 100.0% | 90.3% | 96.8% | 0.151 | Better than saved 96% FA, still not enough |
| seen-only cap-300 | `q99_seen_success_FA010` | OOD180 cap-300 | 57.3% | 89.2% | 16.2% | 86.5% | 0.287 | Poor under stricter horizon |
| distinct OOD calibration cap-300 | `cal_q95_oodcal_success_FA01` | OOD180 cap-300 | 53.1% | 89.2% | 13.5% | 86.5% | 0.298 | Still too high false alarm |

Reports:

- Seen-only calibration report: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260629_seen_calibrated_thresholds/H10_TOPK8_SEEN_CALIBRATED_ON_OFFICIAL_OOD180_20260629.md`
- Distinct-OOD calibration report: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260629_distinct_ood_calibration/H10_TOPK8_DISTINCT_OOD_CALIBRATION_ON_OOD180_20260629.md`

Conclusion: the current H10 TopK8 detector score has useful failure recall, but it does not provide a satisfying no-OOD-test-tuning operating point on official OOD180. The OOD false-alarm shift remains the limiting failure mode.

---

## Official FIPER Seen Calibration Baseline (Bob, 2026-07-02 audit)

This is the clean seen-only official FIPER baseline used as the threshold source for the next cross-suite OOD ablation.

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `official_fiper_seen_goal_object_train_eval_20260701` |
| **Output root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701` |
| **Dataset** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_data/libero_goal_object_official/processed_rollouts` |
| **Official FIPER repo** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/repos/fiper` at commit `13d79c5c3069def843e454787ff128defc249838` |
| **Protocol** | RND train/calibration on seen official `libero_goal_object`; held-out seen test only; no OOD data used |
| **Seeds** | `0, 1, 2, 42, 43` |
| **Aggregate CSV** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701/official_fiper_q95_aggregate.csv` |

Selected q95 seen operating points:

| Method | Threshold Style | Best Window | Balanced Score | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `entropy` | `ct_quantile` | 15 | 86.5% | 10.0% | 83.0% | 4.0% | 50.0% | 73.0% | 0.291 | 17.0% |
| `entropy` | `tvt_quantile` | 50 | 80.0% | 40.0% | 100.0% | 39.0% | 67.0% | 84.0% | 0.260 | 0.0% |
| `entropy` | `tvt_cp_band` | 50 | 96.5% | 6.0% | 99.0% | 0.0% | 0.0% | 53.0% | 0.533 | 1.0% |
| `rnd_oe` | `ct_quantile` | 3 | 47.9% | 4.1% | 0.0% | 0.0% | 0.0% | 0.0% | N/A | 100.0% |
| `rnd_oe` | `tvt_quantile` | 1 | 77.6% | 15.7% | 71.0% | 0.0% | 24.4% | 31.2% | 0.427 | 29.0% |
| `rnd_oe` | `tvt_cp_band` | 11 | 77.3% | 9.9% | 64.4% | 0.0% | 13.4% | 24.6% | 0.482 | 35.6% |
| `rnd_oe_and_entropy` | `ct_quantile` | 1 | 50.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | N/A | 100.0% |
| `rnd_oe_and_entropy` | `tvt_quantile` | 1/50 | 84.3% | 1.9% | 70.4% | 0.0% | 16.0% | 20.8% | 0.572 | 29.6% |
| `rnd_oe_and_entropy` | `tvt_cp_band` | 11/50 | 81.3% | 1.2% | 63.8% | 0.0% | 0.0% | 11.2% | 0.704 | 36.2% |

These rows are seen held-out results. The follow-up `official_fiper_seen_thresholds_cross_suite_ood_20260702` applies these exact operating points to all collected cross-suite OOD datasets with no OOD recalibration.

### Cross-Suite OOD Application With Seen Thresholds

Completed on Bob on 2026-07-02. This is the strict no-cheat cross-suite application of the seen FIPER thresholds above.

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `official_fiper_seen_thresholds_cross_suite_ood_20260702` |
| **Report** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/OFFICIAL_FIPER_SEEN_THRESHOLDS_CROSS_SUITE_OOD_20260702.md` |
| **Aggregate CSV** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv` |
| **Protocol** | 150 seen official `libero_goal_object` successful calibration rollouts + target OOD test rollouts only |
| **No OOD calibration** | YES |
| **No OOD threshold tuning** | YES |
| **RND checkpoints reused** | YES, seeds `0,1,2,42,43` |

Selected rows:

| Dataset | Best-looking official row under seen thresholds | Success FA | Failure Det | Det@50 | Notes |
| :--- | :--- | ---: | ---: | ---: | :--- |
| `goal_object_ood_180` | `entropy`/fusion `tvt_quantile` w50 / 1-50 | 18.0% | 70.7% | 48.8% | RND-OE alone false-alarms 100%; fusion with tvt quantile collapses to entropy behavior. |
| `goal_swap_100` | `entropy tvt_quantile w50` | 0.0% | 73.2% | 61.9% | Good FA due only 3 successes, but recall still incomplete. |
| `goal_task_100` | `entropy ct_quantile w15` | 0.0% | 42.2% | 4.4% | Low false alarm but weak and late detection. |
| `spatial_object_100` | `entropy/fusion tvt_quantile w50` | 21.5% | 100.0% | 100.0% | Strong detection but nontrivial false alarms on 93 successes. |
| `object_object_100` | `entropy tvt_quantile w50` | 3.2% | 8.1% | 5.4% | FIPER mostly misses failures. |
| `libero10_object_100` | `entropy tvt_quantile w50` | 0.0% | 10.4% | 7.8% | FIPER mostly misses failures. |

Interpretation: official FIPER is not uniformly strong under strict seen-only calibration. The RND-OE channel can either saturate to 100% false alarms (`goal_object_ood_180`, `spatial_object_100`, `object_object_100`, `libero10_object_100`) or become too conservative (`goal_swap_100`, `goal_task_100`). Entropy transfers better than RND on some suites, but failure detection becomes weak on `object_object_100` and `libero10_object_100`.


## Current Main Isaac 3cm350 Risk Model & Conformal Results (2026-08-19)

Canonical record: [`ISAAC_MAIN_3CM350_20260819.md`](ISAAC_MAIN_3CM350_20260819.md) and [`../../isaac_experiment_map/CURRENT_MAIN_ISAAC_RESULTS_20260819.md`](../../isaac_experiment_map/CURRENT_MAIN_ISAAC_RESULTS_20260819.md).

- Protocol: 3 cm threshold, 350 control ticks, 30 Hz, H10 execution, **NO DWELL**.
- Dataset: `isaac_seen4904_h10_3cm350_exact_v1` (4,904 episodes: 4,387 success, 517 failure, 96,813 rows; 96 timing-unresolvable episodes excluded).
- Split: Unified label-stratified 70/15/15 (Train: 3,433 eps; Val: 735 eps; Test: 736 eps; seed 20260819).
- Model: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2` (SeqRiskModel, 128 width, 3 layers, 4 heads, pos_weight=4.3453).
- Locked internal TEST (736 eps / 14,526 rows): query AUROC **0.9408** / AUPRC **0.8748**, episode-balanced AUROC **0.9987** / AUPRC **0.9782**.
- Conformal Best Val F1 Threshold (`0.5791`): **100.0% Failure Detection**, **7.60% Success False Alarm**.
- Scope: Locked internal TEST split. New-protocol OOD evaluation is pending.

## Historical Corrected True-H10 Isaac Sim Result (2026-08-18)

Canonical record: [`ISAAC_RESULTS_20260818.md`](ISAAC_RESULTS_20260818.md) and [`../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`](../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md).

- Seen4000: **4000 episodes**, **3908 success / 92 failure**, **75,603 decision rows**.
- V1 validation AUROC/AUPRC: **0.9344901338 / 0.8494462696**.
- Locked historical true-H10 OOD150 detector: **72 success / 78 failure**, **5,887 rows**, step **AUROC 0.9165517742 / AUPRC 0.9800307262**.
- Main detector threshold: `best_val_f1 = 0.7990124225616455`, calibrated on Seen validation.
- Definitive active controller: `A=0.7990124225616455`, `C=0.9`, `M=0.0`.
- Active result: **75/150 (50.0%)** versus historical same-membership **72/150 (48.0%)**, net **+3 episodes / +2.0 percentage points**.
- Paired: **11 rescues / 8 regressions / 64 persisted successes / 67 persisted failures**.
- Controller audit: **57 accepted replacements** across **36/150 episodes**, **0 selection mismatches**, **0 execution mismatches**, max selected-vs-executed action difference **0.0**.
- Exact membership: 150 expected / 150 actual / 150 unique, no missing, extra, or duplicate IDs; historical membership exact.
- `A` is Seen-calibrated. `C=0.9` is engineering-development-informed from preserved live nine-candidate OOD-development decisions, so the final 150 is **not** a pristine untouched holdout for controller hyperparameter selection.
- V1 is a current/main H10 proposal failure detector with multi-sample ACE/disagreement context; it was **not** trained on nine independently supervised counterfactual candidate outcomes.
- HARD1000 resumed safely from the preserved 249-episode state and is ongoing; intermediate HARD1000 counts are **not** final results.
- Commit `70327b4b31bde35c01fda29a807f9100b5295a62` is **invalid for historical candidate-wise alternative scores** because candidates 1–8 diffusion traces were not archived. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.
