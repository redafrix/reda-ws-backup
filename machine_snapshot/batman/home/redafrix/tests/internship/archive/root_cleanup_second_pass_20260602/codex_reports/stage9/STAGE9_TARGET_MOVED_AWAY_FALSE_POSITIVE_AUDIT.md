# Stage 9 Target Moved Away False Positive Audit

## Summary
The `target_moved_away_from_goal` mini-failure rule was found to produce significant false positives during broad collection. This audit identifies the root cause and implements a robust fix to ensure only high-confidence physical failures are labeled as RISKY.

## Root Cause Analysis
The original `target_moved_away_from_goal` rule was too permissive:
1. **Lack of Semantic Filtering:** It fired on any "place" task, regardless of whether the task parser was confident in the target and goal objects.
2. **Phase Agnostic:** It triggered during the "Approach" phase if the target object moved slightly (contact noise) and its distance to the goal increased, even before any transport attempt.
3. **Missing Held Constraint:** It did not verify if the object was actually under robot control (held) before penalizing distance increases.
4. **Already-Success Noise:** It fired on objects already at the goal if they were bumped slightly.

## Implemented Fixes
The detector in `detect_mini_failures.py` has been updated with the following constraints:

1. **Safety Switch:** Added `--enable-target-moved-away-risk` flag. This flag is **OFF** by default. When OFF, events are still detected for audit purposes but are downgraded to `UNCERTAIN` or `SAFE_WEAK` risk bins.
2. **High-Confidence Parsing:** The rule now requires `parse_confidence == "HIGH"`. This ensures the target and goal bases are physically meaningful before calculating distances.
3. **Transport/Held Requirement:** The rule only labels an event as `RISKY` if:
   - The target was recently held (`held_fraction >= 0.20`), OR
   - The episode is explicitly in the `TRANSPORT` or `PLACE_OR_GOAL` phase.
4. **Distance Thresholds:** Added a check to ensure the target was not already at the goal (`target_to_goal_before > 0.12m`) before the distance increase.
5. **Severity Downgrade:** Events that trigger the distance increase but fail the strict constraints are now automatically capped in severity and confidence, resolving to the `UNCERTAIN` bin instead of polluting the `RISKY` dataset.

## Wrong Object Picked Audit
The `wrong_object_picked` rule was audited and found to be robust. It successfully detects cases where a non-target object (e.g., 'ramekin' instead of 'soup_can') is moved and lifted while the target remains static.
- **Sample Evidence (Smoke Test):**
  - Episode: `wrong_object`
  - Non-target held: `['ramekin']`
  - Non-target motion: `2.51`
  - Target motion: `0.00`
  - EEF lift: `0.12`
  - Outcome: Correctly labeled as `RISKY_STRONG`.

## Verification Results
1. **Compilation:** `py_compile` passed.
2. **Synthetic Smoke Test:**
   - Total Episodes: 6
   - `target_moved_away_from_goal` Events (Default): 0 (Correctly suppressed/downgraded)
   - `wrong_object_picked` Events: 2 (Verified)
   - Total `RISKY` chunks: 17 (Target move noise removed)

## Recommendation
The detector is now **SAFE** to use for Stage 9 collection. By default, `target_moved_away_from_goal` will no longer generate risky labels. If distance-based risk is desired for specific high-precision tasks, it must be explicitly enabled via `--enable-target-moved-away-risk`, and it will still be protected by the new strict semantic and phase-based gates.

## Paths
- **Source Fix:** `stage9_v2_tools/data_collection_stage9/detect_mini_failures.py`
- **Smoke Output:** `/tmp/stage9_mini_failure_smoke_after_target_fix/out`
- **Report:** `/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_TARGET_MOVED_AWAY_FALSE_POSITIVE_AUDIT.md`
