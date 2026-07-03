# Stage 9 Label Validation Final Decision

Generated: `2026-05-18`

## Direct Decision

- Are current BAD labels trustworthy? `NO`
- Is final data collection allowed? `NO`

## Why

Strict validation was run on the current Bob snapshot:

- `risky_state_mining_v1`
- `risky_state_mining_medium_v1`
- `phase_balanced_v1_run2`

Current combined label distribution:

```json
{
  "AMBIGUOUS": 268,
  "BAD": 105,
  "GOOD_STRONG": 374,
  "GOOD_WEAK": 221
}
```

Strict BAD validation result:

```json
{
  "VALIDATED_BAD": 11,
  "DOWNGRADE_TO_AMBIGUOUS": 22,
  "INVALID_BAD": 72
}
```

Validated BAD percentage:

- `11 / 105 = 10.48%`

This is far below the required `80%` minimum.

## BAD Reason Diversity

BAD reasons before validation:

```json
{
  "eef_moved_away_from_target_during_approach": 72,
  "target_object_moved_away_from_goal": 8,
  "zero_reward_no_eef_target_or_goal_progress": 25
}
```

BAD reasons after strict validation:

```json
{
  "zero_reward_no_eef_target_or_goal_progress": 11
}
```

Only one BAD type survived, and even that is limited to no-progress/stuck evidence. Current BAD diversity is not enough for final collection.

## Replay And Horizon Result

Replay was attempted twice per BAD sample.

H=10 replay was available from saved action chunks:

```json
{
  "H10_ok_attempts": 210,
  "replay_labels": {
    "BAD": 168,
    "AMBIGUOUS": 27,
    "GOOD_WEAK": 15
  }
}
```

H=20, H=40, and H=80 could not be computed from the saved current datasets because candidate action chunks contain only 10 saved steps. The validator records those horizons as `not_available_saved_action_too_short`. Future collection must save or regenerate action chunks long enough for H=20/40/80 validation.

## Review Pack

Review pack exists:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/validation/review_pack`

Contents include 182 selected samples:

```json
{
  "invalid_or_suspicious_bad": 94,
  "top_bad": 48,
  "good_strong": 20,
  "ambiguous": 20
}
```

## Exact Rule/Sampler Fixes Required

1. Disable `eef_moved_away_from_target_during_approach` as standalone BAD.
   - It produced 72 BAD labels.
   - All 72 failed strict validation.
   - Main failures: parent phase was not APPROACH/NEAR_GRASP, no better same-state real seed, and replay mismatch.

2. Require saved parent phase confirmation for EEF-away.
   - EEF-away can only be considered if parent phase is `APPROACH` or `NEAR_GRASP`.
   - If parent phase is `TRANSPORT`, `PLACE_OR_GOAL`, or `STUCK_OR_NO_PROGRESS`, EEF-away must become `AMBIGUOUS`.

3. Require same-state sibling proof for BAD.
   - A BAD candidate must be worse than other real SimVLA seeds from the same simulator state.
   - If all seeds look equally bad, this is a risky state, not a candidate-specific BAD action.

4. Require replay-consistent BAD evidence.
   - If replay does not reproduce the BAD label and same BAD reason, downgrade to `AMBIGUOUS`.

5. Fix H=20/H=40/H=80 support.
   - Save longer candidate action chunks during collection, or add deterministic SimVLA regeneration in validation.
   - Without longer-horizon evidence, placement/transport risk remains under-proven.

6. Keep unknown/weak reasons out of strong training labels.
   - `unknown` BAD is invalid.
   - weak EEF-only evidence is not strong BAD.

## Minimum Gates For Approval

- Minimum validated BAD percentage: `>= 80%`
- Current validated BAD percentage: `10.48%`
- Minimum BAD reason diversity: at least two reliable BAD mechanisms, or explicitly collect only the one validated mechanism and report that limitation.
- Current reliable BAD mechanisms: `zero_reward_no_eef_target_or_goal_progress` only.

## Exact Next Step

Do not launch final collection.

Patch the labeler/sampler first:

- demote EEF-away BAD to `AMBIGUOUS` unless strict phase + same-state + replay gates pass;
- save/regenerate H=20/H=40/H=80 candidate actions;
- rerun the strict validation command on a new pilot snapshot.

Recommended validation command after patching:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
python3 -m data_collection_stage9.validate_bad_labels_strict \
  --replay \
  --replay-attempts 2 \
  --replay-horizons 10 20 40 80
```

Final collection remains blocked until the strict report passes the gates above and the review pack is regenerated.
