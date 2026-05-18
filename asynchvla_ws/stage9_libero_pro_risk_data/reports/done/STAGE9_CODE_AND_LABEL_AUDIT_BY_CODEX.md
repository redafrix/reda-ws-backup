# Stage 9 Code And Label Audit By Codex

Generated: `2026-05-18`

## Scope

Audited the current Stage 9 implementation on Bob via `pcrobot` under:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/`

Also read the local handoff/report copies under:

- `/home/redafrix/tests/internship/codex_reports/stage9/`
- `/home/redafrix/tests/internship/gemini_handoff_current/`
- `/home/redafrix/tests/internship/gemini_handoff_archive/`

## What Gemini Implemented

Gemini implemented a same-state LIBERO-PRO counterfactual data pipeline:

- `collect_counterfactual_dataset.py`: parent rollout, phase/risky-state sampling, saved simulator state, real SimVLA candidate action sampling by seed, same-state short-horizon execution, image/state/action/outcome/label serialization.
- `task_parser.py`: heuristic target and goal parsing from task language plus observation/body keys.
- `outcome_metrics.py`: reward/success, EEF motion, object body positions, target motion/height, target-goal distance, target-EEF distance, contact diagnostics, and phase detection.
- `label_rules.py`: four-class labeler returning `GOOD_STRONG`, `GOOD_WEAK`, `BAD`, or `AMBIGUOUS`.
- `run_rule_unit_tests.py` and validation scripts: synthetic rule tests, reset determinism, observation signal checks, controlled-action checks, SimVLA seed repeatability, dataset quality analysis.
- `make_bad_sample_videos.py` is referenced by reports/handoff, but was not present in the current `src/data_collection_stage9/` mirror at audit time.

The reset and action-seed mechanics are promising, but the label validator is not yet strict enough for high-precision BAD labels.

## Where Label Rules Are

Core rules are in:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/label_rules.py`

Current rule version:

- `stage9_rules_v6_four_class_evidence`

Supporting metric code:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/outcome_metrics.py`

## Exact BAD Rules

`label_rules.py::_bad_evidence()` currently marks BAD when any of the following holds:

- `target_object_dropped`: `target_height_drop > 0.10`
- `large_object_height_drop`: `height_drop_max > 0.18`
- `target_object_moved_away_from_goal`: `target_to_goal_delta > 0.06` and `target_motion > 0.02`
- `eef_moved_away_from_target_during_approach`: internal labeler phase in `{approach, near_grasp}` and `target_to_eef_delta > 0.045`
- `gripper_lost_or_released_target`: `gripper_opened_near_target` and `target_height_drop > 0.04`
- `confident_bad_contact`: `bad_contact_confident`
- `unstable_state`: `unstable_state`
- `zero_reward_no_eef_target_or_goal_progress`: zero nonzero rewards, `eef_delta < 0.008`, `target_motion < 0.003`, no goal progress, and no target approach

Important audit finding: the EEF-away rule uses the labeler-derived phase, not the saved parent phase. In current risky datasets, many samples saved as parent `TRANSPORT` are BAD only because the labeler internally judged the outcome phase as approach/near-grasp. That is suspicious and must be downgraded unless same-state alternatives and replay prove real risk.

## Exact GOOD_STRONG Rules

`label_rules.py::_strong_good_evidence()` currently marks strong GOOD when any of the following holds:

- `success_within_horizon`: `success_within_H` or `success_after`
- `target_object_closer_to_goal`: `target_to_goal_delta < -0.025`
- `target_object_lifted`: `target_height_delta > 0.025` and `target_motion > 0.012`
- `target_object_moved_correct_direction`: `target_motion > 0.045` and `target_to_goal_delta < -0.010`

Weak GOOD remains intentionally separate:

- EEF closer to target during approach/near-grasp: `target_to_eef_delta < -0.020`
- gripper closed near target
- small target motion in plausible direction
- weak target alignment improvement

## Current Dataset Paths And BAD Counts

Audited target datasets:

| Dataset | Path | Rows | BAD |
|---|---|---:|---:|
| risky_state_mining_v1 | `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1/counterfactual_samples.jsonl` | 320 | 42 |
| risky_state_mining_medium_v1 | `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1/counterfactual_samples.jsonl` | 496 | 42 |
| phase_balanced_v1_run2 | `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2/counterfactual_samples.jsonl` | 56 | 0 |

Label distributions:

- `risky_state_mining_v1`: `BAD=42`, `AMBIGUOUS=90`, `GOOD_STRONG=108`, `GOOD_WEAK=80`
- `risky_state_mining_medium_v1`: `BAD=42`, `AMBIGUOUS=127`, `GOOD_STRONG=211`, `GOOD_WEAK=116`
- `phase_balanced_v1_run2`: `GOOD_WEAK=25`, `GOOD_STRONG=23`, `AMBIGUOUS=8`

BAD reason distribution:

- `risky_state_mining_v1`: `eef_moved_away_from_target_during_approach=40`, `zero_reward_no_eef_target_or_goal_progress=2`
- `risky_state_mining_medium_v1`: `eef_moved_away_from_target_during_approach=32`, `target_object_moved_away_from_goal=8`, `zero_reward_no_eef_target_or_goal_progress=2`

## Why BAD Labels May Be Suspicious

The current BAD labels are not trustworthy yet for training:

- Most BAD labels come from `eef_moved_away_from_target_during_approach`, which is explicitly a fragile rule.
- Many of those samples have saved parent phase `TRANSPORT`, so the "during approach" assumption is not proven.
- The local video handoff contains 10 BAD videos but only sidecar summaries, not full proof bundles; video is not enough evidence.
- The video report table says some BAD reasons are `unknown`, while the copied sidecar JSON shows concrete reasons. This reporting inconsistency needs cleanup.
- Current samples store only H=10 action chunks, so H=20/40/80 evidence requires regeneration or must be marked unavailable.
- Parent outcome fields exist for risky-state datasets, but distance-to-failure/timeout and reward context around the selected state are not systematically audited.
- Same-state sibling comparison exists implicitly because each state has seed siblings, but no script verifies that BAD candidates are worse than sibling real SimVLA candidates.
- Replay consistency is not required by the current labeler.

## Missing Validation

Required before final collection:

- Strict BAD proof bundle per sample.
- Anti-false-BAD gate that downgrades `unknown` or weak EEF-only BAD.
- Replay same saved state/action at least twice and compare evidence.
- Same-state sibling ranking across all real SimVLA seed candidates.
- Parent episode alignment: parent success/failure, timeout, steps, state position relative to failure/timeout.
- H=20/H=40/H=80 metrics when enough actions can be regenerated; otherwise explicitly record `not_available`.
- Missed-BAD audit over `GOOD_STRONG`, `GOOD_WEAK`, and `AMBIGUOUS`.
- Review pack with suspicious/invalid BAD, top BAD, GOOD_STRONG, AMBIGUOUS, metrics JSON, before/after images, and tables.

## Initial Decision

Current BAD labels are not approved for final data collection. The strict validation system must downgrade uncertain BAD to `AMBIGUOUS`, especially EEF-away BAD without phase confirmation, same-state comparison, and replay consistency.
