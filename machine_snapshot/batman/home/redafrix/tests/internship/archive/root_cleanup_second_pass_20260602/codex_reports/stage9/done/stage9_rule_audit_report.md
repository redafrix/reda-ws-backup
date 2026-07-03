# Stage 9 Rule Audit Report

Generated: `2026-05-18T11:20:15`

## Current Label Rules Before This Fix

The current labeler is `stage9_rules_v5_phase_aware_local_progress` and still returns the old classes `GOOD`, `BAD`, and `AMBIGUOUS`.

## Strong / Weak Rule Status

- Success within H is strong GOOD evidence.
- Target object closer to goal and target lift are treated as GOOD, but not explicitly separated into strong vs weak labels.
- EEF-target approach is treated as GOOD. This is the remaining unacceptable shortcut.
- No-progress and object-drop are BAD rules.
- Unknown target/object is AMBIGUOUS.

## Where EEF Approach Is Used

`label_rules.py` currently uses `target_to_eef_delta < -0.025` during approach/near-grasp as `GOOD`. This must become `GOOD_WEAK`, not strong GOOD.

## Target / Goal Parsing

`task_parser.py` parses target and goal/receptacle from task language and observation keys. Target parsing is medium reliability for object/receptacle tasks. Goal parsing is heuristic and not fully reliable.

## Available Signals

- Object pose/body positions: available.
- Object height/drop: available from object positions.
- Target-to-EEF distance: available.
- Target-to-goal/receptacle distance: available when both target and goal parse.
- Contact: available, but raw contact is not reliable as strong BAD because floor contacts exist at rest.
- Before images: saved.
- After images: saved after the previous collector patch.

## Why Previous Pilot Got 64 GOOD / 0 BAD / 32 AMBIGUOUS

The pilot was dominated by early approach states. SimVLA moved the EEF closer to the target object without object/reward/success progress. Because the old v5 labeler allowed EEF-target approach to become GOOD, those became `GOOD`. Under the corrected design these should be `GOOD_WEAK`, not `GOOD_STRONG`.
