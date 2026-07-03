# Stage 9 Broad Mini-Failure Generalization Run

Generated: 2026-05-22

## Objective

Collect and mine mini-failures across many LIBERO-PRO perturbation suites, not only `libero_spatial_with_mug`.

## Code Changes

- Added `collect_raw_mini_failure_episodes_v1.py`.
  - Records raw full episodes for both success and failure outcomes.
  - Saves per-step action, observations, object body positions, contacts, proprio, agent/wrist images, state paths, history, task context, and parent episode outcome.
  - Uses real SimVLA actions only, chunk size 10.
  - Can scan all registered perturbation suites with `_with_` in the suite name.
- Generalized mini-failure detector:
  - Added `task_relation` / `parse_confidence` to features and labels.
  - Pick/place failure detectors are relation-aware, so pure articulation tasks are not mislabeled as pick failures.
  - Same-semantic-family matching is now generic instead of hard-coded to bowl/mug/plate/ramekin.
  - Keeps `pre_failure_steps=60`, `core_label_steps=10`, `stable_lift_steps=30`.

## Validation Before Broad Launch

Synthetic detector smoke on Bob:

- Status: PASS
- Healthy pickup negative control: 0 events
- Positive controls still detected:
  - missed pick
  - wrong object
  - drop/slip
  - missed place
  - unstable pick / failed lift

Real multi-suite collector smoke:

- Suites tried: `libero_object_with_mug`, `libero_spatial_with_red_box`, `libero_goal_with_mug`
- Recorded episodes: 2
- Outcomes: 1 failure, 1 success
- `libero_spatial_with_red_box` failed locally because its custom red-box asset XML is missing.
- Detector on smoke recorded 0 mini-failure events, which is acceptable for a tiny smoke because the clips did not visibly trigger the strict failure rules.

## Broad Run

Bob tmux session:

`stage9_broad_mini_failure_v1`

Log:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/broad_mini_failure_v1_20260522_1025.log`

Raw output:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_mini_failure_broad/broad_mini_failure_v1_20260522_1025`

Detector output after collection finishes:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/broad_mini_failure_v1_20260522_1025_labels`

Review frames after detection finishes:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/broad_mini_failure_v1_20260522_1025_labels/event_video_frames_pre60_core10`

Current launch config:

- all perturbed LIBERO-PRO suites registered as `libero_*_with_*`
- max task id: 9
- rollouts per task: 2
- max recorded episodes: 100
- max parent episodes: 220
- max runtime: 240 minutes
- parent max steps: 400
- record outcomes: all
- pre-failure labeling window: 60 steps
- failure core: 10 steps

## Current Status Snapshot

At the first progress check:

- tmux: running
- GPU: active
- recorded episodes: 4
- logged suite/task errors: 30
- observed usable new suite: `libero_10_with_milk`
- observed broken local suites so far:
  - `libero_10_with_alphabet_soup`
  - `libero_10_with_blue_stick`
  - `libero_10_with_diffpos_stick`

The broken suites are failing in `make_env` due missing local custom asset files, not due the detector.

## Next Check

After the tmux run finishes, run or inspect:

```bash
tmux attach -t stage9_broad_mini_failure_v1
tail -100 "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/broad_mini_failure_v1_20260522_1025.log"
cat "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_mini_failure_broad/broad_mini_failure_v1_20260522_1025/summary.json"
cat "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/broad_mini_failure_v1_20260522_1025_labels/mini_failure_summary.json"
```

## Final Run Result

The broad run completed successfully.

Raw episodes:

- Recorded episodes: 100
- Suites with recorded episodes:
  - `libero_10_with_milk`: 16 episodes, 12 success, 4 failure
  - `libero_10_with_mug`: 20 episodes, 17 success, 3 failure
  - `libero_goal_with_milk`: 20 episodes, 19 success, 1 failure
  - `libero_goal_with_mug`: 20 episodes, 18 success, 2 failure
  - `libero_goal_with_yellow_book`: 20 episodes, 20 success, 0 failure
  - `libero_object_with_mug`: 4 episodes, 4 success, 0 failure
- Total task groups covered: 50

Mini-failure detection:

- Events: 73
- Event types:
  - `wrong_object_picked`: 54
  - `target_moved_away_from_goal`: 19
- Chunk labels: 1756
- Risky chunks: 139
- Chunk risk bins:
  - `RISKY_STRONG`: 89
  - `RISKY_WEAK`: 50
  - `SAFE_STRONG`: 55
  - `SAFE_WEAK`: 943
  - `UNCERTAIN`: 619
- Step labels: 17176
- Step risk bins:
  - `RISKY_STRONG`: 540
  - `RISKY_WEAK`: 600
  - `SAFE_STRONG`: 1287
  - `SAFE_WEAK`: 9163
  - `UNCERTAIN`: 5586

Event distribution by suite:

- `libero_10_with_milk`: 4 wrong-object events
- `libero_10_with_mug`: 5 wrong-object events
- `libero_goal_with_milk`: 18 wrong-object events, 7 moved-away events
- `libero_goal_with_mug`: 14 wrong-object events, 6 moved-away events
- `libero_goal_with_yellow_book`: 13 wrong-object events, 6 moved-away events

Local review MP4s:

`/home/redafrix/tests/internship/codex_reports/stage9/broad_mini_failure_v1_20260522_1025_videos`

There are 30 encoded review videos with agent view + wrist view.

## Important Interpretation

This run proves the broad collector/detector is no longer mug-only. It produced mini-failure detections from `libero_10`, `libero_goal`, milk, mug, and yellow-book perturbation suites.

But this is not yet a final training dataset. The next required step is manual review of the 30 MP4s. If many are visually wrong, the detector rules need another correction before using the labels. If most are correct, the next move is to run a longer broad collection restricted to locally working suites.

## Local Asset Limitation

Many registered LIBERO-PRO perturbation suites failed before rollout because custom asset XML files are missing locally. These are environment/data-install problems, not detector-rule failures. The working broad run should focus on currently usable suites until those assets are restored.
