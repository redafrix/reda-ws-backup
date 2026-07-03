# Stage 9 Corrected Label Pipeline Report

Generated: 2026-05-18

## 1. Executive Summary

The old Stage 9 BAD labels are not trustworthy. The main failure was treating weak local geometric evidence, especially `eef_moved_away_from_target_during_approach`, as BAD. I replaced that with a stricter outcome/advantage pipeline:

`real SimVLA candidate action -> H=40 trace -> SimVLA policy continuation -> same-state seed comparison -> final label`

Final labels are now:

- `GOOD_STRONG`: the real SimVLA branch reaches terminal success under policy continuation.
- `GOOD_WEAK`: local progress exists, but terminal success is not proven.
- `VALIDATED_BAD`: terminal failure/timeout is supported by strict evidence and same-state/parent context.
- `AMBIGUOUS`: anything weak, mixed, or under-proven.

The corrected pilot now produces defended `VALIDATED_BAD` labels. The best pilot run, `outcome_advantage_v3`, produced 96 samples from 12 selected states:

| Final label | Count |
|---|---:|
| `VALIDATED_BAD` | 72 |
| `GOOD_STRONG` | 16 |
| `AMBIGUOUS` | 8 |

Validation checks passed for this pilot: no unknown BAD reason, no EEF-away BAD, full H=40 trace or terminal-before-H evidence, same-state comparison present, zero suspicious labels.

Final huge data collection is **NO** for now. The corrected pipeline works, but the validated BAD diversity is still narrow: the current reliable BAD type is repeated same-state failure-tail/no-progress. The next step is an expanded multi-task pilot, not the final huge dataset.

## 2. Why Previous BAD Labels Failed

Previous BAD labels were mostly produced by weak local cues. The worst one was:

`eef_moved_away_from_target_during_approach`

Manual review showed that many such samples looked possibly fine. Strict validation confirmed the issue: earlier validation found 105 BAD labels audited, only 11 validated, 22 downgraded, and 72 invalid.

The core bug was conceptual: a short local motion can look bad while the full branch is still recoverable or successful. A risk detector needs action outcome evidence, not just a geometric delta.

## 3. Exact Label Rule Changes

Changed in `asynchvla_ws/src/data_collection_stage9/label_rules.py`.

Current rule version:

`stage9_rules_v7_corrected_strong_bad_only`

`eef_moved_away_from_target_during_approach` is no longer a BAD rule. It is weak negative evidence only.

Raw local BAD can only come from strong local events:

- `target_object_dropped`
- `large_object_height_drop`
- `target_object_moved_away_from_goal`
- `gripper_lost_or_released_target`
- `confident_bad_contact`
- `unstable_state`
- `no_progress_strong`

Raw local BAD is not automatically a final BAD. Final BAD must pass strict validation and becomes `VALIDATED_BAD`; otherwise the final label stays `AMBIGUOUS`.

## 4. Files Changed

Core changes:

- `asynchvla_ws/src/data_collection_stage9/label_rules.py`
- `asynchvla_ws/src/data_collection_stage9/strict_label_utils.py`
- `asynchvla_ws/src/data_collection_stage9/outcome_metrics.py`
- `asynchvla_ws/src/data_collection_stage9/sim_state_utils.py`
- `asynchvla_ws/src/data_collection_stage9/collect_counterfactual_dataset.py`
- `asynchvla_ws/src/data_collection_stage9/collect_outcome_advantage_dataset.py`
- `asynchvla_ws/src/data_collection_stage9/analyze_outcome_pilot.py`

Important implementation fixes:

- Full H-step trace arrays are saved instead of only before/after metrics.
- Restored MuJoCo states now clear robosuite/LIBERO termination flags before replay.
- Policy continuation records trace chunks across H=40, not just the first 10-step SimVLA chunk.
- Same-state sibling summaries are recomputed after final labels, so proof bundles show final sibling labels.
- Pre-failure state selection now supports `--pre-failure-distances 40 24 12 1`.

## 5. New Final Label Policy

For each selected simulator state S:

1. Generate real SimVLA candidates using seeds `0 1 2 3 4 5 6 7`.
2. Reset to the exact same simulator state S for every seed.
3. Execute the candidate action chunk and save H=40 trace evidence.
4. Continue with real SimVLA policy actions up to terminal horizon.
5. Compare all same-state seed outcomes.
6. Assign final label.

`GOOD_STRONG`:

- terminal success under SimVLA continuation.

`GOOD_WEAK`:

- local progress exists, but terminal success is not proven.

`VALIDATED_BAD`:

- terminal failure/timeout with successful same-state alternative and strong score gap, or
- repeated same-state failure-tail/no-progress:
  - parent episode failed/timed out,
  - selected state is near failure,
  - same-state seed majority fails,
  - no local success/progress,
  - failure or timeout repeats under real SimVLA continuation.

`AMBIGUOUS`:

- weak local evidence,
- raw BAD without terminal proof,
- terminal failure but insufficient local/no-progress support,
- mixed or unclear evidence.

## 6. H=40 Trace Schema

Each sample now stores a `horizon_trace` with:

- `rewards`
- `success_flags`
- `done_flags`
- `eef_positions`
- `target_object_positions`
- `target_object_heights`
- `object_goal_distances`
- `eef_target_distances`
- `gripper_states`
- `contact_summaries`
- `frame_paths` when saved
- `initial`
- `final`
- `requested_horizon`
- `steps_executed`
- `terminal_steps`
- `terminal_success`
- `terminal_failure`
- `terminal_timeout`

Short traces are allowed only when the branch reaches terminal success/done before H=40.

## 7. Corrected Pilot Commands

Main validated pilot:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

python3 -m data_collection_stage9.collect_outcome_advantage_dataset \
  --suites libero_spatial_with_mug \
  --task-ids 5 \
  --max-total-states 12 \
  --max-parent-episodes 6 \
  --max-states-per-parent 2 \
  --parent-roll-steps 120 \
  --risk-window 12 \
  --simvla-seeds 0 1 2 3 4 5 6 7 \
  --eval-horizon 40 \
  --terminal-horizon 80 \
  --history-k 8 \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v3 \
  --save-images \
  --save-trace-frames \
  --trace-frame-stride 20
```

Broader pre-failure selector pilot:

```bash
python3 -m data_collection_stage9.collect_outcome_advantage_dataset \
  --suites libero_spatial_with_mug \
  --task-ids 5 \
  --max-total-states 16 \
  --max-parent-episodes 4 \
  --max-states-per-parent 4 \
  --parent-roll-steps 120 \
  --risk-window 12 \
  --pre-failure-distances 40 24 12 1 \
  --simvla-seeds 0 1 2 3 4 5 6 7 \
  --eval-horizon 40 \
  --terminal-horizon 80 \
  --history-k 8 \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v4 \
  --save-images
```

## 8. Corrected Pilot Results

### outcome_advantage_v3

Dataset:

`asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v3`

Log:

`asynchvla_ws/stage9_libero_pro_risk_data/logs/outcome_advantage_v3_collection.log`

Counts:

| Metric | Value |
|---|---:|
| Samples | 96 |
| Selected states | 12 |
| SimVLA seeds per state | 8 |
| Eval horizon | 40 |
| Terminal horizon | 80 |

Final label distribution:

| Label | Count |
|---|---:|
| `VALIDATED_BAD` | 72 |
| `GOOD_STRONG` | 16 |
| `AMBIGUOUS` | 8 |

Raw local label distribution:

| Raw label | Count |
|---|---:|
| `AMBIGUOUS` | 50 |
| `BAD` | 30 |
| `GOOD_STRONG` | 14 |
| `GOOD_WEAK` | 2 |

Raw-to-final movement:

| Raw -> Final | Count |
|---|---:|
| `AMBIGUOUS -> VALIDATED_BAD` | 42 |
| `BAD -> VALIDATED_BAD` | 30 |
| `GOOD_STRONG -> GOOD_STRONG` | 14 |
| `GOOD_WEAK -> GOOD_STRONG` | 2 |
| `AMBIGUOUS -> AMBIGUOUS` | 8 |

BAD reasons:

| Reason | Count |
|---|---:|
| `repeated_same_state_failure_tail_no_progress` | 72 |
| `no_progress_strong` | 30 |

Phase distribution:

| Phase | Count |
|---|---:|
| `STUCK_OR_NO_PROGRESS` | 88 |
| `TRANSPORT` | 8 |

Trace coverage:

| Trace length | Count |
|---|---:|
| 40 | 55 |
| 1 | 30 |
| 2 | 3 |
| 5 | 2 |
| 6 | 1 |
| 7 | 1 |
| 8 | 1 |
| 10 | 1 |
| 11 | 1 |
| 14 | 1 |

All 96 samples had either full H=40 trace or terminal-before-H evidence.

### outcome_advantage_v4

Dataset:

`asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v4`

This pilot used broader pre-failure distances. It intentionally sampled earlier failed-episode states and therefore produced more `AMBIGUOUS`, which is correct behavior.

Final label distribution:

| Label | Count |
|---|---:|
| `AMBIGUOUS` | 69 |
| `VALIDATED_BAD` | 58 |
| `GOOD_WEAK` | 1 |

Raw local label distribution:

| Raw label | Count |
|---|---:|
| `BAD` | 73 |
| `AMBIGUOUS` | 54 |
| `GOOD_WEAK` | 1 |

Important: 15 raw BAD samples were downgraded to `AMBIGUOUS`. This proves the corrected pipeline does not blindly preserve raw BAD labels.

## 9. Strict Validation Results

Validation artifacts:

- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v3_analysis.json`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v3_review/`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v4_analysis.json`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v4_review/`

`outcome_advantage_v3` validation checks:

| Check | Result |
|---|---|
| No final BAD unknown reason | PASS |
| No final BAD from EEF-away alone | PASS |
| Some `VALIDATED_BAD` exists | PASS |
| `GOOD_STRONG` has terminal success | PASS |
| `AMBIGUOUS` used when unsure | PASS |
| Same-state comparison exists | PASS |
| Full H=40 trace or terminal-before-H | PASS |
| No zero-step samples | PASS |
| Suspicious labels | 0 |

`outcome_advantage_v4` validation checks also passed with 0 suspicious labels.

## 10. Examples of VALIDATED_BAD

Example 1:

- Sample: `libero_spatial_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s114_state_seed0`
- Phase: `STUCK_OR_NO_PROGRESS`
- Parent failed/timed out: true
- Distance to failure/timeout: 6
- Terminal steps: 80
- Terminal success: false
- Terminal failure: true
- Terminal timeout: true
- H trace length: 40
- Reward sum H: 0.0
- Same-state terminal successes: 0/8
- Same-state terminal failures: 8/8
- Final reason: `repeated_same_state_failure_tail_no_progress`

Example 2:

- Sample: `libero_spatial_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s114_state_seed1`
- Evidence: same state, seed 1, terminal timeout at 80, 0 reward, 8/8 same-state seed failures.
- Final reason: `repeated_same_state_failure_tail_no_progress`

These are reliable risk labels for failure-tail/no-progress states. They are not produced by EEF-away.

## 11. Examples of Downgraded BAD

In `outcome_advantage_v4`, raw local BAD was not enough:

- Sample: `libero_spatial_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s96_state_seed3`
- Raw label: `BAD`
- Raw reason: `no_progress_strong`
- Final label: `AMBIGUOUS`
- Phase: `STUCK_OR_NO_PROGRESS`
- Distance to failure/timeout: 24
- Terminal failure: true
- Terminal timeout: false
- H trace length: 1
- Final reason: `terminal_outcome_ambiguous`

Reason for downgrade: failure existed, but strict no-progress/failure-tail proof was not strong enough for final `VALIDATED_BAD`.

## 12. GOOD_STRONG Evidence Examples

Example:

- Sample: `libero_spatial_with_mug_t5_r4_pSTUCK_OR_NO_PROGRESS_s106_state_seed0`
- Parent failed/timed out: false
- Terminal steps: 5
- Terminal success: true
- Terminal failure: false
- Reward sum H: 1.0
- Same-state terminal successes: 8/8
- Final reason: `terminal_success_under_policy_continuation`

Other seeds from the same state also succeeded in 5 to 8 steps. These are strong GOOD labels because they are backed by terminal success, not a weak local metric.

## 13. Remaining Suspicious Labels

Current automated suspicious label count:

- `outcome_advantage_v3`: 0
- `outcome_advantage_v4`: 0

Remaining limitations:

- BAD reason diversity is still low.
- Current reliable BAD is mostly repeated failure-tail/no-progress.
- The pilot did not yet find many exact same-state action-advantage cases where one seed succeeds and another fails from the same S.
- `outcome_advantage_v4` deliberately sampled earlier failed-episode states; many were correctly left `AMBIGUOUS`.
- More tasks/suites are needed before final collection.

## 14. Is Final Data Collection Allowed?

**NO.**

The corrected pipeline is now viable, but final huge collection is not allowed yet because the pilot is still too narrow:

- only one LIBERO-PRO task was deeply piloted after the final selector change,
- only one reliable BAD family is currently demonstrated,
- exact same-state success-vs-failure action-advantage BADs are not yet common,
- the final multi-task pilot has not yet been run.

## 15. Exact Blocker

The blocker is no longer the false EEF-away BAD rule. That is fixed.

The current blocker is coverage: the corrected outcome/advantage collector must be run on both mug suites and tasks `0 1 2 3 4 5` with broader pre-failure sampling. We need to verify:

- enough `GOOD_STRONG`,
- enough `VALIDATED_BAD`,
- at least one or more BAD types beyond repeated failure-tail/no-progress, or a clear decision that this is the only reliable BAD type for now,
- no suspicious labels,
- H=40 traces across the expanded pilot.

## 16. Exact Next Command

Run this expanded corrected pilot next. This is still not the huge final collection:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

python3 -m data_collection_stage9.collect_outcome_advantage_dataset \
  --suites libero_spatial_with_mug libero_object_with_mug \
  --task-ids 0 1 2 3 4 5 \
  --max-total-states 80 \
  --max-parent-episodes 20 \
  --max-states-per-parent 4 \
  --parent-roll-steps 160 \
  --risk-window 12 \
  --pre-failure-distances 40 24 12 1 \
  --simvla-seeds 0 1 2 3 4 5 6 7 \
  --eval-horizon 40 \
  --terminal-horizon 120 \
  --history-k 8 \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/corrected_outcome_advantage_v5 \
  --save-images \
  --save-trace-frames \
  --trace-frame-stride 20 \
  2>&1 | tee asynchvla_ws/stage9_libero_pro_risk_data/logs/corrected_outcome_advantage_v5_collection.log
```

After that, run:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9"
python3 analyze_outcome_pilot.py \
  "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/corrected_outcome_advantage_v5" \
  "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/validation" \
  "/media/rootalkhatib/My Passport/reda_ws"
```

## 17. Paths

Code:

- `asynchvla_ws/src/data_collection_stage9/collect_outcome_advantage_dataset.py`
- `asynchvla_ws/src/data_collection_stage9/analyze_outcome_pilot.py`
- `asynchvla_ws/src/data_collection_stage9/label_rules.py`
- `asynchvla_ws/src/data_collection_stage9/outcome_metrics.py`
- `asynchvla_ws/src/data_collection_stage9/sim_state_utils.py`

Pilot datasets:

- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v3`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v4`

Logs:

- `asynchvla_ws/stage9_libero_pro_risk_data/logs/outcome_advantage_v3_collection.log`
- `asynchvla_ws/stage9_libero_pro_risk_data/logs/outcome_advantage_v4_collection.log`

Validation/review:

- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v3_analysis.json`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v3_review/`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v4_analysis.json`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/outcome_advantage_v4_review/`

Report duplicate:

- `/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_CORRECTED_LABEL_PIPELINE_REPORT.md`

