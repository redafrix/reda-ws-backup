# Stage 9 64-Seed Smart Labeling Experiment

Date: 2026-05-20

## Executive Summary

I did not continue the old path unchanged.

I changed the collector to use 64 real SimVLA seeds by default and changed the mining strategy to look for action-specific failures from preterminal successful-episode branchpoints, not only from failure tails. I also fixed a real evidence bug: safe preterminal samples were carrying `no_progress_strong` as strong negative evidence even when the final continuous score was safe/weak.

Current result:

- 64-seed counterfactual replay works.
- Seeded SimVLA actions are diverse, so the seed plumbing is not dead.
- The labeler now avoids falsely treating context-free no-progress as strong BAD evidence.
- The pilot still found no action-specific BAD groups.
- The only high-risk labels found are repeatable `state_context` no-progress groups where all 64 seeds fail.

Conclusion:

The pipeline is better and stricter now, but it is not yet the final perfect action-specific dataset. The next real blocker is mining states where some real SimVLA seeds are good and other real SimVLA seeds are bad. Current sampled successful states are robustly safe across all 64 seeds; current failed states are bad across all 64 seeds.

## Code Changes

Changed files:

- `asynchvla_ws/src/data_collection_stage9/collect_failed_episode_mining_v2.py`
- `asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py`
- `asynchvla_ws/src/data_collection_stage9/collect_continuous_risk_dataset_v2.py`
- `asynchvla_ws/src/data_collection_stage9/collect_outcome_advantage_dataset.py`

Synced and compiled on:

- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9`
- Sam: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9`

Compile command passed on both:

```bash
python3 -m py_compile asynchvla_ws/src/data_collection_stage9/*.py
```

## 64 Seeds Now Default

Updated defaults:

- `collect_failed_episode_mining_v2.py`: `--replay-seeds` defaults to `0..63`
- `collect_continuous_risk_dataset_v2.py`: `--simvla-seeds` defaults to `0..63`
- `collect_outcome_advantage_dataset.py`: `--simvla-seeds` defaults to `0..63`

## Same-State Group Summary

New saved label metadata:

```text
same_state_group_summary_v2
```

It records whether the 64-seed state group is:

- `action_specific_mixed`
- `mixed_needs_review`
- `all_risky_state_context_candidate`
- `all_safe_or_weak_safe`
- `uncertain_or_low_confidence`

This is audit/analysis metadata, not model input.

Smoke output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/group_summary_64seed_smoke_20260520
```

Smoke result:

- Replay samples: 64
- Samples with `same_state_group_summary_v2`: 64
- Group type: `all_safe_or_weak_safe`
- Risk bins: 11 `SAFE_STRONG`, 53 `SAFE_WEAK`
- Strong negative evidence on safe samples: 0

## Smarter Branchpoint Mining

Problem with previous success-branchpoint miner:

- It mostly picked the highest-progress/final chunks in successful episodes.
- Those states were too easy, and all seeds looked safe.

New behavior:

- Selects preterminal branchpoints from successful episodes.
- Prefers `NEAR_GRASP`, `GRASP_OR_LIFT`, `TRANSPORT`, and `PLACE_OR_GOAL`.
- Avoids chunks that already have sparse task reward/success when possible.
- Picks phase-diverse and position-diverse chunks instead of only top-progress chunks.
- Replays 64 real SimVLA seeds from the exact same state.

## Evidence Rule Fix

Bug found:

Many safe preterminal samples were labeled with:

```text
negative_evidence = ["no_progress_strong"]
```

even though their risk score was safe/weak.

Fix:

- Context-free local no-progress is now weak evidence:

```text
no_progress_observed_without_context
```

- Strong no-progress is only strong when confirmed by:
  - failure-window context,
  - `STUCK_OR_NO_PROGRESS` phase,
  - same-state alternatives clearly doing better,
  - or majority same-state state-context no-progress.

This prevents a normal preterminal chunk with no sparse reward from looking like a certified BAD chunk.

## Experiments Run

### 1. Failed-episode 64-seed branchpoint pilot

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/branchpoint_64seed_pilot_20260520
```

Results:

- Episodes: 2
- Successful episodes: 1
- Failed/timeout episodes: 1
- Replay samples: 512
- Replay seeds: 0..63
- `RISKY_STRONG`: 512
- `state_context`: 512
- `action_specific`: 0

Interpretation:

This confirmed real repeatable state-context no-progress, but not action-specific bad actions.

### 2. Original success-branchpoint 64-seed pilot

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/success_branchpoint_64seed_pilot_20260520
```

Results:

- Episodes: 1 successful
- Success branchpoint windows: 2
- Replay samples: 128
- `SAFE_STRONG`: 128
- `action_specific`: 0

Interpretation:

Useful false-positive check. Easy successful states stayed safe for all 64 seeds.

### 3. Mixed 64-seed branchpoint pilot

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/mixed_branchpoint_64seed_pilot_20260520
```

Results:

- Episodes: 8
- Successful episodes: 6
- Failed/timeout episodes: 2
- Replay samples: 1,152
- `RISKY_STRONG`: 768
- `SAFE_STRONG`: 361
- `SAFE_WEAK`: 23
- `state_context`: 768
- `unknown`: 384
- `action_specific`: 0

Same-state group result:

- Failed windows: all 64 seeds risky.
- Success branchpoints: all 64 seeds safe or weak-safe.
- Mixed action-specific groups: 0

### 4. New preterminal success-branchpoint 64-seed pilot

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/action_specific_preterminal_64seed_pilot_20260520
```

Command shape:

```bash
python3 -m data_collection_stage9.collect_failed_episode_mining_v2 \
  --suites libero_spatial_with_mug libero_object_with_mug \
  --task-ids 0 1 2 3 4 5 \
  --rollouts-per-task 4 \
  --max-episodes-total 12 \
  --max-episode-chunks 16 \
  --initial-chunk-steps 10 \
  --history-k 8 \
  --mine-success-branchpoints \
  --success-branchpoint-strategy diverse_preterminal \
  --success-windows-per-episode 4 \
  --success-branchpoints-preterminal-only \
  --success-branchpoint-phases NEAR_GRASP GRASP_OR_LIFT TRANSPORT PLACE_OR_GOAL \
  --max-windows-per-failed-episode 2 \
  --scan-all-failed-windows \
  --out-dir .../action_specific_preterminal_64seed_pilot_20260520
```

Results:

- Episodes: 12
- Successful episodes: 10
- Failed/timeout episodes: 2
- Episode chunks: 144
- Success branchpoint windows: 40
- Failure windows: 4
- Replay samples: 2,816
- Replay seeds: 0..63

Original scoring:

- `SAFE_WEAK`: 2,560
- `RISKY_STRONG`: 256
- `state_context`: 256
- `action_specific`: 0

Offline rescore after no-progress context fix:

- `SAFE_WEAK`: 2,560
- `RISKY_STRONG`: 256
- `GOOD_WEAK`: 2,560
- `VALIDATED_BAD`: 256
- `state_context`: 256
- `action_specific`: 0

Evidence after fix:

- Safe preterminal samples:
  - strong negative evidence: none
  - weak negative evidence: `no_progress_observed_without_context`
- Failed-window samples:
  - strong negative evidence: `no_progress_strong`
  - subtype: `state_context`

Same-state group result:

- Groups total: 44
- All-risk groups: 4
- All-safe groups: 40
- Mixed action-specific groups: 0

## Seed Diversity Check

I checked action-vector diversity across the 64 seeds.

Result:

- Seeds are not identical.
- Some same-state groups had substantial action-vector diversity.
- Despite action diversity, outcome labels were still not mixed: success branchpoints stayed safe, failed windows stayed state-context risky.

This means 64 seeds are useful, but they do not automatically solve action-specific BAD mining.

## What This Means

The current labeler now behaves more sanely:

- It does not turn sparse reward/no reward into BAD.
- It does not make EEF-away a standalone BAD.
- It does not make terminal timeout the main label source in V2.
- It distinguishes weak no-progress from confirmed no-progress.
- It can certify repeatable state-context risk with 64 seeds.

But the current sampler still does not find action-specific BAD examples.

## Current Best Diagnosis

The problem is no longer mainly the BAD rule.

The problem is the state/action mining distribution:

1. Failure-window states are often already unrecoverable/stuck.
   - All 64 seeds fail.
   - These are valid `state_context` risk, but not action-specific risk.

2. Successful-episode branchpoints sampled so far are robust.
   - All 64 seeds are safe/weak-safe.
   - These are good positives but do not create BAD negatives.

3. We have not yet found the narrow boundary states where:
   - one real SimVLA seed makes progress,
   - another real SimVLA seed drops/losses/worsens/stalls,
   - and the bad seed is clearly worse from the exact same state.

## Next Fix To Try

The next collector should be an active mixed-branchpoint miner:

1. Collect many successful SimVLA parent trajectories.
2. Keep only preterminal states with real phase transition potential.
3. Replay 64 seeds.
4. Keep a state for training only if the 64-seed outcome distribution is mixed.
5. Store all-safe states as positives, but cap them.
6. Store all-risk states as `state_context`, but cap them.
7. Spend most compute searching for mixed states.

Additional high-value target states:

- expert-demo states if matching LIBERO-PRO expert states become available,
- near-grasp/lift states with object close to gripper,
- transport states where object is currently lifted,
- place states where target is close to goal but not completed,
- recovery states immediately before the parent trajectory changes from moving/progress to stuck/no-progress.

## Dataset Readiness

DATASET_READY_FOR_FULL_TRAINING = NO

Reason:

The pipeline can now produce good positives and repeatable state-context risk, but it still has zero discovered action-specific BAD groups in the 64-seed pilots.

Training only on current labels would mostly teach:

```text
this state is hopeless/stuck
```

instead of:

```text
this candidate action chunk is risky compared with other possible real SimVLA chunks from the same state
```

That is not the final risk detector we want.
