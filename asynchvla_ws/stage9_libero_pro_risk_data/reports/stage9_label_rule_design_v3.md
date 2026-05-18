# Stage 9 Label Rule Design v3

Generated: `2026-05-18T11:21:23`

## Label Classes

- `GOOD_STRONG`: reliable positive target/task progress.
- `GOOD_WEAK`: weak useful signal, not reliable enough for strong training.
- `BAD`: clear bad event or clear no-progress failure.
- `AMBIGUOUS`: missing, tiny, mixed, or unreliable evidence.

## Strong GOOD Evidence

- `success_within_H` or `success_after`.
- target object moved closer to the parsed goal/receptacle enough: `target_to_goal_delta < -0.025`.
- target object lifted enough: `target_height_delta > 0.025` and `target_motion > 0.012`.
- target object moved in correct direction: `target_motion > 0.045` and `target_to_goal_delta < -0.010`.

## Weak GOOD Evidence

- EEF moved closer to parsed target before grasp: `target_to_eef_delta < -0.020` during approach/near-grasp.
- gripper closed near target.
- small target motion in plausible direction but below strong threshold.
- weak target alignment improvement.

## BAD Evidence

- target object dropped: `target_height_drop > 0.10`.
- some object had a large height drop: `height_drop_max > 0.18`.
- target moved away from goal: `target_to_goal_delta > 0.06` and `target_motion > 0.02`.
- EEF moved away from target during approach: `target_to_eef_delta > 0.045`.
- gripper opened near target plus target drop.
- confident bad contact, if a future contact classifier provides it.
- unstable state.
- zero reward and no EEF/target/goal progress.

## Ambiguous Evidence

- target or target position missing.
- only random/non-target object changed.
- weak/mixed progress below thresholds.
- missing goal for goal-distance tests.
- contact available but not confidently classifiable.

## Decision Order

1. If target object missing -> `AMBIGUOUS`.
2. If BAD evidence exists -> `BAD`.
3. Else if strong GOOD evidence exists -> `GOOD_STRONG`.
4. Else if only weak GOOD evidence exists -> `GOOD_WEAK`.
5. Else -> `AMBIGUOUS`.

## Training Recommendation

Use `GOOD_STRONG` and `BAD` as strong supervised labels. Down-weight or exclude `GOOD_WEAK`. Treat `AMBIGUOUS` as unlabeled/ignored unless doing semi-supervised analysis.
