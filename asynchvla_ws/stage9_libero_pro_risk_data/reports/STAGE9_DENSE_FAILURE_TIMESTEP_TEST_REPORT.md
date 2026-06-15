# Stage 9 Dense Failure Timestep Test Report

Date: 2026-05-20

## Why This Test Exists

The previous miner only labeled states at SimVLA chunk boundaries. With `initial_chunk_steps=10`, it checked roughly steps `0, 10, 20, ...`, not every simulator timestep. That could miss the exact failure onset.

This test fixes that. The new miner runs long parent episodes, keeps every simulator timestep from step 10 onward for failed episodes, and replays many real SimVLA seeds from each timestep state.

## Code Added

New collector:

- `stage9_v2_tools/data_collection_stage9/collect_dense_failure_timestep_mining_v2.py`
- Bob copy: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/collect_dense_failure_timestep_mining_v2.py`
- Sam copy: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9/collect_dense_failure_timestep_mining_v2.py`

Updated scorer:

- `stage9_v2_tools/data_collection_stage9/local_chunk_quality.py`
- Bob copy: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py`
- Sam copy: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py`

Updated diagnostics:

- `stage9_v2_tools/data_collection_stage9/diagnose_v2_collection.py`
- It now reads `dense_replay_counterfactual_samples.jsonl`.

Compile status:

- Local compile passed.
- Bob compile passed.
- Sam compile passed.

## Scorer Fixes Made During This Test

The smoke test found another real scorer issue:

- In `TRANSPORT`, EEF moving closer to the object was reducing no-progress risk.
- That is wrong because transport should require object motion, goal progress, lift/hold progress, or task reward/success.
- EEF approach is now only counted as no-progress relief during `APPROACH`, `NEAR_GRASP`, or `APPROACH_OR_NEAR_GRASP`.

The scorer now also stores continuous diagnostic components:

- `eef_motion_credit`
- `target_motion_credit`
- `goal_progress_credit`
- `goal_worsening_credit`
- `eef_approach_credit`
- `eef_away_credit`
- `lift_credit`
- `height_drop_credit`

The scorer is still conservative: no parent failure alone becomes a label. Dense failure context only contributes when local no-progress evidence also exists.

## Dense Miner Behavior

Parent rollout:

- Executes SimVLA policy chunks end-to-end.
- Parent policy chunk length: `10`.
- Parent episode max length: `400` env steps.
- If episode fails/timeouts, it keeps every timestep state from step `10`.

Replay:

- Candidate action target: SimVLA action chunk.
- Candidate chunk length: `10`.
- Same-state replay seeds: `200`.
- Replay actions are real SimVLA outputs, no synthetic/no-op/random actions.
- Saves full local H trace for each replayed candidate chunk.

Labels:

- Continuous risk score is primary.
- Risk bins are still saved for diagnosis.
- `episode_failure_used_for_label = false`.
- `terminal_continuation_used_for_label = false`.

## Smoke Test Results

Bob smoke:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/dense_failure_timestep_smoke_bob_v3_20260520`
- Parent result: one success, one 120-step failure/timeout.
- Dense states replayed: `2`
- Replay seeds/state: `5`
- Replay samples: `10`
- Result: early timestep states were `UNCERTAIN`, as expected.

Sam smoke:

- Path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/dense_failure_timestep_smoke_sam_v3_20260520`
- Parent result: one success, one 120-step failure/timeout.
- Dense states replayed: `2`
- Replay seeds/state: `5`
- Replay samples: `10`
- Result: early timestep states were `UNCERTAIN`, as expected.

Important smoke finding:

- Before the second scorer fix, EEF approach in `TRANSPORT` was hiding no-progress.
- After the fix, no-progress risk is visible, but early states far before timeout remain ambiguous.

## Full Dense 200-Seed Tests Running

Bob:

- Session: `tmux stage9_dense_200_bob`
- Output: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_failure_timestep_200seed_bob_20260520`
- Log: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/dense_failure_timestep_200seed_bob_20260520.log`
- Tasks: `libero_spatial_with_mug` task ids `0 1 2`
- Found failure: `libero_spatial_with_mug_t0_r1_pseed1`
- Parent steps: `400`
- Dense states to replay: `390`
- Replay seeds/state: `200`
- Expected replay samples if complete: `78,000`

Bob live progress:

- Replay samples written: `2,200`
- Same-state timestep groups written: `11`
- Current risk bins: `UNCERTAIN 2,200`
- Current group types: `uncertain_or_other 11`
- Duplicate seed groups: `0`
- Possible scorer saturation groups: `0`
- Mean action diversity/group: `0.2829`
- Max action diversity/group: `0.3311`
- Mean risk-score range/group: `0.0018`
- Max risk-score range/group: `0.0175`

Sam first attempt:

- Tasks: task ids `3 4 5`
- Result: all `16` parent episodes succeeded, so no failure was available to replay.
- This was not a crash.

Sam retry:

- Process: `python3 -m data_collection_stage9.collect_dense_failure_timestep_mining_v2`
- Output: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_failure_timestep_200seed_sam_retry_20260520`
- Log: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/dense_failure_timestep_200seed_sam_retry_20260520.log`
- Tasks: `libero_spatial_with_mug` task ids `0 1 2`
- Policy seed base: `100`
- Found failure: `libero_spatial_with_mug_t0_r1_pseed101`
- Parent steps: `400`
- Dense states to replay: `390`
- Replay seeds/state: `200`
- Expected replay samples if complete: `78,000`

Sam retry live progress:

- Replay samples written: `800`
- Same-state timestep groups written: `4`
- Current risk bins: `UNCERTAIN 800`
- Current group types: `uncertain_or_other 4`
- Duplicate seed groups: `0`
- Possible scorer saturation groups: `0`
- Mean action diversity/group: `0.2265`
- Max action diversity/group: `0.2572`
- Mean risk-score range/group: `0.0044`
- Max risk-score range/group: `0.0175`

## Current Interpretation

It is too early to judge the full dense test because both machines have only replayed early timesteps so far. Those early states are far before timeout, so `UNCERTAIN` is acceptable.

The important improvement is that scorer saturation is no longer showing up in the live diagnostic:

- Actions differ.
- Seeds are unique.
- Score ranges are no longer exactly zero.
- Same-state score spread is small but nonzero.

If later timesteps near timeout still produce only uncertain labels, then either:

1. The scorer is still missing the relevant failure signal, or
2. SimVLA failure in this task is not action-specific and needs a different state-context risk formulation.

## Commands To Monitor

Bob:

```bash
ssh pcrobot "tail -f '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/dense_failure_timestep_200seed_bob_20260520.log'"
```

Sam:

```bash
ssh sam "tail -f '/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/dense_failure_timestep_200seed_sam_retry_20260520.log'"
```

Live diagnosis:

```bash
python3 -m data_collection_stage9.diagnose_v2_collection <dense_output_dir>
```

## Next Check

Wait until at least 100 dense timestep groups have been replayed on each machine, then rerun diagnosis and inspect:

- whether late timesteps become `RISKY_WEAK` / `RISKY_STRONG`,
- whether any mixed action-specific groups appear,
- whether score spread grows near failure,
- whether state-context risk appears near timeout,
- whether the scorer still misses obvious no-progress failure.
