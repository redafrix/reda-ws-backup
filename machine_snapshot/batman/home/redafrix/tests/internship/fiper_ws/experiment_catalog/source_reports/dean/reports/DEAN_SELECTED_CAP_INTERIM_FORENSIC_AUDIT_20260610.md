# Dean Selected-Cap Interim Forensic Audit - 2026-06-10

This report records Codex checks performed directly against the active Dean selected-cap 100ep run. It is an interim audit, not a final result report, because the 18-task campaign is still running.

## Active Run

- Host: Dean, reachable from Batman through `dean-via-bob`
- Direct `ssh dean`: currently times out from Batman
- Tmux: `dean_selected_cap_t03_c04_100ep_20260610`
- Root: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610`
- Runner: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/src/run_policy_matrix_selected_cap.py`
- Runner SHA256: `3e071164def5c48a9c54f9f4ab96b18069f4edd4238c29c5295e9d2522fa05c5`

## Identity Checks

| Item | Value |
|---|---|
| Suite | `libero_goal_object_ood` |
| Policies | `modified_simvla` fixed H10 baseline vs `risk_topk8_selected_cap` |
| Seeds | `300..399`, identical for both policies per task |
| Config count | 36 task policy configs plus `seed_plan.json` |
| Execution horizon | `10` |
| Checkpoint | `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors` |
| Checkpoint SHA256 | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` |
| Detector | `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/unc_topk8/model.pt` |
| Detector SHA256 | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` |
| Thresholds SHA256 | `cef61220101dec3d808937fe028ca736b11ebdc8f1d9a25e9fde70cffa020756` |
| q95 / q99 | `0.6155413389205933` / `0.9665935635566711` |

The runtime manifests for completed risk tasks point to:

`/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/unc_topk8`

The config schema uses `risk_model_unc_topk8_dir`, not `risk_model_dir`. Audits must check that key; treating missing `risk_model_dir` as an error is a schema false positive.

## Gate Verified

The active selected-cap gate is:

- `selection_main_threshold = 0.3`
- `selection_streak_threshold = 0.3`
- `selection_min_margin = 0.02`
- `selection_strong_margin = 0.05`
- `selection_max_selected_score = 0.4`
- `selection_min_high_risk_streak = 1`
- `selection_min_timestep = 0`
- `selection_cooldown_steps = 0`

The runner rejects a replacement candidate when its selected risk exceeds the cap via `candidate_above_selected_score_cap`; accepted replacements are logged with `selection_reason = best_below_q95` when the chosen candidate is below q95.

## Results Snapshot

Snapshot time: 2026-06-10 21:32 CEST.

| Task | Modified SimVLA | TopK8 selected-cap | Paired result |
|---:|---:|---:|---:|
| 0 | 75/100 | 90/100 | 21 rescues / 6 regressions, net +15 |
| 1 | 94/100 | 95/100 | 1 rescue / 0 regressions, net +1 |
| 2 | 91/100 | 90/100 | 0 rescues / 1 regression, net -1 |
| 3 | 98/100 | 96/100 | 0 rescues / 2 regressions, net -2 |
| 4 | 100/100 | 53/53 active | 53 common seeds so far, no paired difference so far |

Completed-task cumulative result:

| Metric | Modified SimVLA | TopK8 selected-cap |
|---|---:|---:|
| Completed tasks | 4 | 4 |
| Episodes | 400 | 400 |
| Successes | 358/400 | 371/400 |
| Success rate | 89.50% | 92.75% |
| Paired rescues | - | 22 |
| Paired regressions | - | 9 |
| Net paired gain | - | +13 |

## Outcome-Changing Episode Analysis

On Tasks 0-3, every rescue and every regression had at least one actual replacement. The regressions are therefore real policy-caused failures, not episodes where the risk policy simply followed the baseline unchanged.

Rescue seeds:

- Task 0: `302, 311, 313, 316, 318, 324, 326, 334, 335, 341, 343, 345, 363, 367, 369, 386, 387, 388, 389, 393, 396`
- Task 1: `392`

Regression seeds:

- Task 0: `307, 342, 360, 365, 366, 397`
- Task 2: `306`
- Task 3: `327, 349`

Aggregate replacement statistics for outcome-changing episodes:

| Class | Episodes | Mean mods | Median mods | Mean first query | Mean first selected risk | Mean first action L2 | Mean max main risk |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rescues | 22 | 2.95 | 3 | 5.23 | 0.2699 | 0.7597 | 0.6314 |
| Regressions | 9 | 2.89 | 3 | 7.56 | 0.2879 | 0.5253 | 0.9960 |

The first-action L2 does not cleanly separate rescues from regressions. Rescues often use larger action deviations than regressions, so a simple L2 cap is not currently the best next gate.

## Post-Hoc Gate Sweep

The current gate has completed-task paired net `+13` on Tasks 0-3.

A post-hoc sweep over the recorded interventions suggests one plausible next gate:

- keep `selection_max_selected_score <= 0.4`
- add `risk_reduction = main_score - selected_score >= 0.08`

On the 400 completed episodes, this rule would still touch 20/22 rescue episodes and only 5/9 regression episodes. This is only a counterfactual screening heuristic, not a proven result, because removing a subset of interventions changes future trajectory state.

Do not launch this variant until the active 100ep selected-cap run finishes, unless Dean has a second free GPU, which it does not.

## Interim Verdict

- Mechanical validity: **PASS so far**
- Checkpoint identity: **PASS**
- Detector identity: **PASS**
- Suite identity: **PASS**
- Seed parity: **PASS**
- Current scientific signal: **positive but incomplete**

The run is currently the strongest OOD risk-aware signal in the workspace, but the final claim depends on the full 18-task 100ep campaign.
