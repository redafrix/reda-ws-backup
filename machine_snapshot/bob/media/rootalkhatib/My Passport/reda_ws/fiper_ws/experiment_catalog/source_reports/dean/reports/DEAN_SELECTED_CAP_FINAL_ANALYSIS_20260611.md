# Dean Selected-Cap Final Analysis - 2026-06-11

This report records the completed 100-episode-per-task Dean selected-cap evaluation on the full generated `libero_goal_object_ood` suite.

## Run Identity

- Host: Dean, accessed through `dean-via-bob`
- Root: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610`
- Tmux: `dean_selected_cap_t03_c04_100ep_20260610` completed
- Suite: `libero_goal_object_ood`
- Tasks: 18 tasks, IDs 0-17
- Seeds: 300-399 for every task and both policies
- Policies: `modified_simvla` fixed H10 baseline vs `risk_topk8_selected_cap`
- Execution horizon: H10

## Verified Artifacts

| Artifact | SHA256 |
|---|---|
| Modified SimVLA ckpt-60000 `model.safetensors` | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` |
| H10 TopK8 detector `model.pt` | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` |
| TopK8 thresholds | `cef61220101dec3d808937fe028ca736b11ebdc8f1d9a25e9fde70cffa020756` |
| Selected-cap runner | `3e071164def5c48a9c54f9f4ab96b18069f4edd4238c29c5295e9d2522fa05c5` |

Thresholds:

- q95: `0.6155413389205933`
- q99: `0.9665935635566711`

## Gate

The risk policy used the same TopK8 candidate replacement mechanism as the aggressive policy, but added an absolute selected-candidate risk cap.

- `selection_main_threshold = 0.3`
- `selection_streak_threshold = 0.3`
- `selection_min_margin = 0.02`
- `selection_strong_margin = 0.05`
- `selection_max_selected_score = 0.4`
- `selection_min_high_risk_streak = 1`
- `selection_min_timestep = 0`
- `selection_cooldown_steps = 0`

## Final Global Result

| Metric | Modified SimVLA fixed H10 | TopK8 selected-cap |
|---|---:|---:|
| Episodes | 1,800 | 1,800 |
| Successes | 1,726/1,800 | 1,741/1,800 |
| Success rate | 95.89% | 96.72% |
| Mean steps | 117.71 | 116.69 |
| Paired rescues | - | 38 |
| Paired regressions | - | 23 |
| Paired net gain | - | +15 |
| Episodes with modifications | - | 653/1,800 |
| Total action modifications | - | 1,402 |
| Query modification rate | - | 1,402/21,800 = 6.43% |

This is the first full-suite 100ep OOD run in the catalog where the risk-aware policy beats its own paired modified-SimVLA baseline globally.

## Per-Task Results

| Task | Modified | Selected-cap | Rescues | Regressions | Net | Mods |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 75/100 | 90/100 | 21 | 6 | +15 | 261 |
| 1 | 94/100 | 95/100 | 1 | 0 | +1 | 68 |
| 2 | 91/100 | 90/100 | 0 | 1 | -1 | 69 |
| 3 | 98/100 | 96/100 | 0 | 2 | -2 | 7 |
| 4 | 100/100 | 100/100 | 0 | 0 | 0 | 5 |
| 5 | 99/100 | 99/100 | 0 | 0 | 0 | 33 |
| 6 | 100/100 | 100/100 | 0 | 0 | 0 | 27 |
| 7 | 95/100 | 94/100 | 0 | 1 | -1 | 24 |
| 8 | 97/100 | 97/100 | 1 | 1 | 0 | 17 |
| 9 | 100/100 | 99/100 | 0 | 1 | -1 | 58 |
| 10 | 100/100 | 100/100 | 0 | 0 | 0 | 39 |
| 11 | 97/100 | 96/100 | 1 | 2 | -1 | 176 |
| 12 | 98/100 | 94/100 | 2 | 6 | -4 | 137 |
| 13 | 88/100 | 96/100 | 10 | 2 | +8 | 308 |
| 14 | 97/100 | 97/100 | 1 | 1 | 0 | 151 |
| 15 | 98/100 | 98/100 | 0 | 0 | 0 | 5 |
| 16 | 100/100 | 100/100 | 0 | 0 | 0 | 0 |
| 17 | 99/100 | 100/100 | 1 | 0 | +1 | 17 |

## Integrity Checks

- Raw JSONL row count: 1,800 baseline rows and 1,800 risk rows.
- Seed order: exact `300..399` for every task and both policies.
- Seed parity: pass for all 18 tasks.
- Duplicate seeds: none found.
- Suite field: all episode and step rows use `libero_goal_object_ood`.
- Task IDs: episode task IDs match folder task IDs.
- Runtime manifests: checked on completed tasks and point to the expected detector directory.
- Step-score rows: 21,800 risk queries, 1,402 modified queries, no wrong-suite rows.

Selection reasons across risk queries:

| Reason | Count |
|---|---:|
| `insufficient_high_risk_streak` | 14,255 |
| `insufficient_margin` | 2,868 |
| `candidate_above_selected_score_cap` | 2,517 |
| `best_below_q95` | 1,402 |
| `main_is_lowest` | 758 |

## Interpretation

The selected-cap gate is mechanically valid and globally positive on this 18-task OOD suite. The gain is not uniform:

- Strongly positive tasks: task 0 and task 13.
- Neutral tasks: many high-success tasks where the baseline already has little headroom.
- Negative tasks: task 12 is the main failure case, with 2 rescues and 6 regressions.

The result supports the claim that a risk-aware replacement layer can improve the modified SimVLA policy on this generated OOD suite, but only under a selective gate. Plain 0.3, 0.5, q95, and adaptive-horizon variants did not produce this global win.

## Follow-Up Launched

A delayed-intervention replication was launched after this result:

- Root: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611`
- Tmux: `dean_selected_cap_delay30_100ep_20260611`
- Seeds: 400-499
- Difference from this run: `selection_min_timestep = 30`

Purpose: test whether suppressing very early replacements reduces regressions while preserving the rescues.
