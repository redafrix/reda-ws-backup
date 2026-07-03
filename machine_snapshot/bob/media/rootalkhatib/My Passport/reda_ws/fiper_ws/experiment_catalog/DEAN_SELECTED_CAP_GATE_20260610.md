# Dean Selected-Cap Gate - 2026-06-10

## Purpose

This experiment tests a stricter TopK8 replacement rule on the full `libero_goal_object_ood` suite. The goal is to preserve rescues while reducing regressions by refusing replacement candidates whose own predicted risk is still too high.

## Mechanism

Compared with the plain aggressive TopK8 policy, the runner adds:

- `selection_main_threshold = 0.3`
- `selection_min_margin = 0.02`
- `selection_strong_margin = 0.05`
- `selection_max_selected_score = 0.4`

So a candidate can replace the main SimVLA chunk only if:

1. the main chunk is risky enough,
2. the candidate reduces risk by enough margin,
3. the candidate's absolute risk score is at most `0.4`.

The runner is isolated at:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/src/run_policy_matrix_selected_cap.py`

## 10ep Diagnostic Result

Root:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_10ep_20260610`

Configuration:

- Suite: `libero_goal_object_ood`
- Tasks: 18 tasks, task IDs 0-17
- Seeds: 200-209
- Policies: modified SimVLA fixed H10 baseline vs TopK8 selected-cap risk policy
- Checkpoint: modified SimVLA `ckpt-60000`, SHA256 `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- Risk detector: H10 TopK8, SHA256 `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d`

| Metric | Modified SimVLA | TopK8 selected-cap |
|---|---:|---:|
| Successes | 170/180 | 176/180 |
| Success rate | 94.44% | 97.78% |
| Paired rescues | - | 7 |
| Paired regressions | - | 1 |
| Net paired gain | - | +6 |
| Modified queries | - | 121/2,160 |

Rescued seeds:

| Task | Seed | Baseline steps | Risk steps | Risk modifications |
|---:|---:|---:|---:|---:|
| 0 | 202 | 300 | 246 | 6 |
| 4 | 200 | 300 | 196 | 1 |
| 12 | 208 | 300 | 89 | 1 |
| 12 | 209 | 300 | 92 | 3 |
| 13 | 204 | 300 | 133 | 2 |
| 14 | 207 | 300 | 136 | 3 |
| 17 | 206 | 300 | 129 | 1 |

Regression:

| Task | Seed | Baseline steps | Risk steps | Risk modifications |
|---:|---:|---:|---:|---:|
| 11 | 200 | 93 | 300 | 2 |

## Interpretation

This is the strongest recent risk-aware online signal. It improves over the fixed H10 modified SimVLA baseline across the full 18-task OOD goal-object suite, with low regression count and moderate query modification rate.

It is still a 10-seed-per-task diagnostic. Treat it as promising, not final.

## 100ep Confirmation

The 100ep confirmation completed on Dean:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610`

Configuration:

- Seeds: 300-399
- Same tasks, checkpoint, detector, and gate
- Tmux: `dean_selected_cap_t03_c04_100ep_20260610` completed
- Rows: 1,800 modified SimVLA + 1,800 TopK8 selected-cap
- Trust: mechanically valid and globally positive after raw paired JSONL analysis.

### Final 100ep Result

Final report:

`/home/redafrix/tests/internship/fiper_ws/experiment_catalog/source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md`

| Metric | Modified SimVLA | TopK8 selected-cap |
|---|---:|---:|
| Successes | 1,726/1,800 | 1,741/1,800 |
| Success rate | 95.89% | 96.72% |
| Mean steps | 117.71 | 116.69 |
| Paired rescues | - | 38 |
| Paired regressions | - | 23 |
| Net paired gain | - | +15 |
| Episodes with modifications | - | 653/1,800 |
| Total action modifications | - | 1,402 |
| Query modification rate | - | 1,402/21,800 (6.43%) |

Per-task summary:

| Task | Modified | Selected-cap | Rescues | Regressions | Net |
|---:|---:|---:|---:|---:|---:|
| 0 | 75/100 | 90/100 | 21 | 6 | +15 |
| 1 | 94/100 | 95/100 | 1 | 0 | +1 |
| 2 | 91/100 | 90/100 | 0 | 1 | -1 |
| 3 | 98/100 | 96/100 | 0 | 2 | -2 |
| 4 | 100/100 | 100/100 | 0 | 0 | 0 |
| 5 | 99/100 | 99/100 | 0 | 0 | 0 |
| 6 | 100/100 | 100/100 | 0 | 0 | 0 |
| 7 | 95/100 | 94/100 | 0 | 1 | -1 |
| 8 | 97/100 | 97/100 | 1 | 1 | 0 |
| 9 | 100/100 | 99/100 | 0 | 1 | -1 |
| 10 | 100/100 | 100/100 | 0 | 0 | 0 |
| 11 | 97/100 | 96/100 | 1 | 2 | -1 |
| 12 | 98/100 | 94/100 | 2 | 6 | -4 |
| 13 | 88/100 | 96/100 | 10 | 2 | +8 |
| 14 | 97/100 | 97/100 | 1 | 1 | 0 |
| 15 | 98/100 | 98/100 | 0 | 0 | 0 |
| 16 | 100/100 | 100/100 | 0 | 0 | 0 |
| 17 | 99/100 | 100/100 | 1 | 0 | +1 |

Interpretation: this is the first trusted full-suite N=100 OOD run where the risk-aware policy beats its own paired modified-SimVLA baseline. The gain is concentrated mainly in Tasks 0 and 13; Task 12 remains the largest regression cluster.

### Delay30 Replication

After the positive final result, a stricter replication was launched on Dean:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611`

- Seeds: 400-499
- Same suite, checkpoint, detector, H10 execution, and selected-cap gate
- New condition: `selection_min_timestep = 30`
- Tmux: `dean_selected_cap_delay30_100ep_20260611`
- Purpose: test whether suppressing replacements before query 3 reduces regressions while keeping rescues.

### Task 0-3 Interim Milestone

Tasks 0, 1, 2, and 3 finished for both policies on 2026-06-10 while the full 18-task run continued.

| Metric | Modified SimVLA | TopK8 selected-cap |
|---|---:|---:|
| Task 0 successes | 75/100 | 90/100 |
| Task 0 paired outcome | - | 21 rescues / 6 regressions, net +15 |
| Task 0 mean steps | 183.45 | 157.38 |
| Task 0 modified queries | - | 261/1,623 (16.08%) |
| Task 1 successes | 94/100 | 95/100 |
| Task 1 paired outcome | - | 1 rescue / 0 regressions, net +1 |
| Task 1 mean steps | 180.49 | 181.10 |
| Task 1 modified queries | - | 68/1,848 (3.68%) |
| Task 2 successes | 91/100 | 90/100 |
| Task 2 paired outcome | - | 0 rescues / 1 regression, net -1 |
| Task 3 successes | 98/100 | 96/100 |
| Task 3 paired outcome | - | 0 rescues / 2 regressions, net -2 |
| Cumulative Task 0-3 successes | 358/400 | 371/400 |
| Cumulative Task 0-3 paired outcome | - | 22 rescues / 9 regressions, net +13 |

Rescued seeds by completed task:

- Task 0: `302, 311, 313, 316, 318, 324, 326, 334, 335, 341, 343, 345, 363, 367, 369, 386, 387, 388, 389, 393, 396`
- Task 1: `392`
- Task 2: none
- Task 3: none

Regression seeds by completed task:

- Task 0: `307, 342, 360, 365, 366, 397`
- Task 1: none
- Task 2: `306`
- Task 3: `327, 349`

This is still a strong early N=100 task-level signal, but it is not yet the final claim. Tasks 2 and 3 are negative reminders that the benefit is not uniform. The full 18-task confirmation must finish because Bob's earlier 10ep positive signal did not hold globally at N=100.

### Codex Interim Forensic Audit

Codex rechecked the active 100ep run directly from Dean raw configs, manifests, episode summaries, and step-score JSONL on 2026-06-10.

Source report:

`/home/redafrix/tests/internship/fiper_ws/experiment_catalog/source_reports/dean/reports/DEAN_SELECTED_CAP_INTERIM_FORENSIC_AUDIT_20260610.md`

Verified identities:

- Runner SHA256: `3e071164def5c48a9c54f9f4ab96b18069f4edd4238c29c5295e9d2522fa05c5`
- Modified SimVLA checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- TopK8 detector SHA256: `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d`
- Thresholds: q95 `0.6155413389205933`, q99 `0.9665935635566711`
- Config schema note: risk configs use `risk_model_unc_topk8_dir`, not `risk_model_dir`.

Snapshot at 2026-06-10 21:32 CEST:

- Tasks 0-3 are complete for both policies: modified `358/400`, selected-cap `371/400`, paired `22 rescues / 9 regressions`, net `+13`.
- Task 4 baseline is complete at `100/100`; selected-cap is active at `53/53`, with 4 total action modifications and no paired difference so far.

Outcome-changing episode audit:

- Every Task 0-3 rescue and regression had at least one actual replacement.
- The regressions are therefore real policy-caused failures, not unchanged baseline-following episodes.
- A post-hoc gate sweep suggests `main_score - selected_score >= 0.08` as the next candidate if the final 100ep result needs improvement, but this is only a screening heuristic until tested online.

## Margin 0.10 Diagnostic

A stricter risk-only follow-up completed on Dean:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_m10_10ep_20260610`

It keeps the same checkpoint, detector, OOD suite, ACE candidates, H10 execution, selected-score cap `0.4`, threshold `0.3`, and seeds `200-209` as the 10ep diagnostic. The only behavioral change is:

- `selection_min_margin = 0.10` instead of `0.02`

This was chosen from the Task 0 100ep intervention analysis: the stricter margin was expected to reduce regression-touching interventions.

Final result:

| Metric | Modified SimVLA | selected-cap m02 | selected-cap m10 |
|---|---:|---:|---:|
| Successes | 170/180 | 176/180 | 175/180 |
| Mean steps | 121.71 | 115.52 | 115.27 |
| Action modifications | 0 | 121 | 49 |
| Episodes with modifications | 0 | 71 | 39 |
| Paired vs baseline | - | 7 rescues / 1 regression, net +6 | 5 rescues / 0 regressions, net +5 |
| Paired vs m02 | - | - | 1 rescue / 2 regressions, net -1 |

Verdict: m10 is useful as a conservative ablation because it reduces action modifications by 59.5% and removes the single m02 regression, but it also loses two m02 rescues. It should not be scaled before the m02 100ep confirmation finishes.
