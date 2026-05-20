# Stage 9 Continuous Risk Failure-Mining Implementation Report

Generated: `2026-05-20T11:45:00+02:00`

## Executive Summary

Implemented and tested the next Stage 9 V2 pipeline needed to make continuous action-risk labeling work.

The core fix is:

```text
Do not wait for random states to contain BAD actions.
Collect failed SimVLA episodes, mine the likely failure windows, then replay same-state real SimVLA candidates around those windows and score the local action chunks continuously.
```

The pilot now produces the first useful high-risk labels:

```text
Bob failed-episode pilot:
episodes: 6
failed/timeout episodes: 5
success episodes: 1
episode chunks: 58
mined failure windows: 15
same-state replay samples: 120
RISKY_STRONG replay samples: 72
SAFE_STRONG replay samples: 48
high-risk subtype: state_context
high-risk reason: no_progress_strong
same-state proof: 8/8 replay seeds no-progress in those windows
```

This is not final training data yet, but it proves the new mining route works. The old frozen dataset still should not be used as final risk data.

```text
PIPELINE_IMPLEMENTED = YES
BOB_REAL_LIBERO_PRO_PILOT = PASS
SAM_CODE_SYNC_AND_COMPILE = PASS
SAM_LIBERO_PRO_ROLLOUT = BLOCKED_BY_SUITE_CONFIG
READY_FOR_FULL_TRAINING = NO
READY_FOR_LARGER_V2_COLLECTION = YES
```

## Why This Was Needed

The previous continuous relabel pass over the old frozen data found:

```text
samples scored: 37,632
old VALIDATED_BAD: 6,914
confident high-risk chunks: 0
old VALIDATED_BAD downgraded to low/uncertain risk: 6,914 / 6,914
```

That showed the old dataset was not a real BAD-action dataset. Its BAD labels came from terminal outcome logic, not local action-chunk evidence.

The new solution changes the search strategy:

```text
old strategy:
  sample states -> try random same-state candidates -> hope BAD exists

new strategy:
  run full SimVLA episodes -> keep failed episodes -> mine failure windows -> replay same-state candidates -> score local chunks
```

## Code Implemented

Added:

```text
asynchvla_ws/src/data_collection_stage9/collect_failed_episode_mining_v2.py
asynchvla_ws/src/data_collection_stage9/build_expert_low_risk_anchor_dataset.py
asynchvla_ws/src/data_collection_stage9/make_continuous_risk_review_pack.py
```

Updated:

```text
asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py
asynchvla_ws/src/data_collection_stage9/outcome_metrics.py
```

Existing V2 tools kept:

```text
asynchvla_ws/src/data_collection_stage9/collect_continuous_risk_dataset_v2.py
asynchvla_ws/src/data_collection_stage9/relabel_stage9_continuous_v2.py
asynchvla_ws/src/data_collection_stage9/compare_stage9_labeling_methods.py
asynchvla_ws/src/data_collection_stage9/evaluate_local_quality_on_experts.py
asynchvla_ws/src/data_collection_stage9/mine_failure_windows_scripted.py
```

## Important Labeling Policy

The primary label is continuous:

```text
risk_score in [0.0, 1.0]
```

Meaning:

```text
0.0 = clearly safe / good / expert-like
0.5 = uncertain / mixed
1.0 = clearly risky / bad local chunk
```

The target is:

```text
SimVLA candidate action chunk
```

Not:

```text
single scalar terminal episode result
future policy continuation success/failure
parent episode failure alone
```

## Failure Mining Collector

Script:

```text
collect_failed_episode_mining_v2.py
```

Behavior:

1. Run full real SimVLA episodes.
2. Save every pre-chunk state.
3. Execute real SimVLA action chunks.
4. Score each chunk with local continuous risk.
5. If the episode fails/timeouts, select failure windows from:
   - high local risk
   - local negative evidence
   - final failure tail
   - top local-risk chunks
6. Reset to the exact state before each mined window.
7. Generate real SimVLA candidate seeds.
8. Replay only the local chunk.
9. Score same-state replay candidates continuously.

Episode failure is used only for mining candidate windows, not as the label itself.

## State-Context No-Progress Fix

The first failed-episode pilot found strong no-progress in failure windows, but the risk score stayed too low because all same-state seeds were equally bad. That is not action-specific risk; it is state-context risk.

I fixed the scorer so:

```text
if most/all same-state candidates in a failed-window replay have no_progress_strong,
then risk_score can become high with bad_subtype = state_context.
```

This is not weakening the rules. It still requires:

```text
failure-window context
no_progress_strong
same-state replay agreement
no local positive progress
```

It does not allow:

```text
terminal timeout alone
EEF moved away alone
VLM-only evidence
low expert likelihood alone
```

## Expert Low-Risk Anchor Pilot

Script:

```text
build_expert_low_risk_anchor_dataset.py
```

Command run on Bob:

```bash
python3 -m data_collection_stage9.build_expert_low_risk_anchor_dataset \
  --dataset-root "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets" \
  --glob "libero_object/*demo.hdf5" \
  --max-files 4 \
  --max-demos-per-file 3 \
  --chunk-steps 10 \
  --stride 20 \
  --save-images \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/continuous_v2/expert_low_risk_anchor_pilot_20260520"
```

Results:

```text
files processed: 4
demos processed: 12
expert low-risk chunks: 94
risk_score: 0.05
risk_confidence: 0.90
```

Path:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/continuous_v2/expert_low_risk_anchor_pilot_20260520
```

Important: these are low-risk anchors only. They do not create BAD labels.

## Failed-Episode Mining Pilot

Script:

```text
collect_failed_episode_mining_v2.py
```

Fixed pilot output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2_pilot_fixed_20260520
```

Command run on Bob:

```bash
python3 -m data_collection_stage9.collect_failed_episode_mining_v2 \
  --suites libero_spatial_with_mug libero_object_with_mug \
  --task-ids 0 1 \
  --rollouts-per-task 2 \
  --max-episodes-total 6 \
  --max-episode-chunks 10 \
  --initial-chunk-steps 10 \
  --history-k 8 \
  --replay-seeds 0 1 2 3 4 5 6 7 \
  --max-windows-per-failed-episode 3 \
  --tail-windows 2 \
  --top-risk-windows 2 \
  --window-risk-threshold 0.65 \
  --save-images \
  --save-trace-frames \
  --trace-frame-stride 5 \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2_pilot_fixed_20260520"
```

Episode-level result:

```text
episodes_total: 6
episodes_success: 1
episodes_failed_or_timeout: 5
episode_chunks: 58
failure_windows: 15
replay_samples: 120
```

Episode chunk bins:

| risk_bin | count |
|---|---:|
| `SAFE_WEAK` | 37 |
| `SAFE_STRONG` | 21 |

Replay candidate bins:

| risk_bin | count |
|---|---:|
| `RISKY_STRONG` | 72 |
| `SAFE_STRONG` | 48 |

Replay candidate subtypes:

| bad_subtype | count |
|---|---:|
| `state_context` | 72 |
| `unknown` | 48 |

High-risk example:

```json
{
  "risk_score": 0.85,
  "risk_confidence": 1.0,
  "risk_bin": "RISKY_STRONG",
  "bad_subtype": "state_context",
  "negative_evidence": ["no_progress_strong"],
  "same_state": {
    "num_siblings": 8,
    "high_risk_candidate_count": 8,
    "no_progress_context_count": 8,
    "majority_high_risk": true,
    "majority_no_progress_context": true
  }
}
```

This is the first useful high-risk signal, but it is state-context risk, not action-specific risk.

## Review Pack

Script:

```text
make_continuous_risk_review_pack.py
```

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2_pilot_fixed_20260520/review_pack
```

Contents:

```text
20 high-risk sheets
20 low-risk sheets
agent before/after view
wrist before/after view
risk score
same-state evidence
positive/negative evidence
```

The V2 collector now also saves wrist trace frame files alongside agent trace frames for future runs.

## Bob And Sam Status

Bob:

```text
code synced: yes
py_compile: pass
expert anchor pilot: pass
failed-episode mining pilot: pass
review pack: pass
```

Sam:

```text
code synced: yes
py_compile: pass
LIBERO-PRO with_mug rollout: blocked
```

Sam blocker:

```text
Sam's LIBERO registry currently exposes normal suite names:
libero_spatial, libero_object, libero_goal, libero_90, libero_10, libero_100

It does not expose:
libero_spatial_with_mug
libero_object_with_mug
```

So Sam should not collect final LIBERO-PRO data until its LIBERO-PRO suite registry/config is aligned with Bob. It can still run code checks, analysis, review, VLM audit, and training later.

## What Worked

The following parts now work:

```text
continuous risk target
expert low-risk anchors
failed-episode mining
failure-window replay
same-state replay comparison
state_context high-risk labels
agent+wrist visual evidence
review pack generation
Bob real LIBERO-PRO execution
```

## What Still Does Not Work Yet

We do not yet have enough action-specific high-risk labels.

Current high-risk samples are:

```text
state_context / no_progress_strong
```

That is useful, but not sufficient for the whole risk detector. We still need:

```text
action_specific high-risk chunks
object_drop high-risk chunks
lost_grasp high-risk chunks
target_moved_away high-risk chunks
wrong-object / bad-contact if reliable
more task diversity
expert anchor coverage across more tasks
manual/VLM review of high-risk sheets
```

## Immediate Next Command

Run a larger Bob V2 pilot:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

python3 -m data_collection_stage9.collect_failed_episode_mining_v2 \
  --suites libero_spatial_with_mug libero_object_with_mug libero_goal_with_mug libero_10_with_mug \
  --task-ids 0 1 2 3 4 5 6 7 8 9 \
  --rollouts-per-task 8 \
  --max-episodes-total 120 \
  --max-episode-chunks 18 \
  --initial-chunk-steps 10 \
  --history-k 8 \
  --replay-seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \
  --max-windows-per-failed-episode 4 \
  --tail-windows 2 \
  --top-risk-windows 3 \
  --window-risk-threshold 0.65 \
  --save-images \
  --save-trace-frames \
  --trace-frame-stride 5 \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2_scale_001"
```

Then generate the review pack:

```bash
python3 -m data_collection_stage9.make_continuous_risk_review_pack \
  --jsonl asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2_scale_001/replay_counterfactual_samples.jsonl \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2_scale_001/review_pack \
  --top-k 100
```

## Final Decision

```text
CONTINUOUS_RISK_FAILURE_MINING_IMPLEMENTED = YES
FIRST_HIGH_RISK_SIGNAL_FOUND = YES
HIGH_RISK_LABEL_TYPE_FOUND = state_context / no_progress_strong
ACTION_SPECIFIC_HIGH_RISK_FOUND = NOT YET
FULL_DATASET_READY_FOR_TRAINING = NO
NEXT_STEP = scale failed-episode mining on Bob and fix Sam LIBERO-PRO registry before using Sam for rollout
```

The important outcome is that the system no longer has to fake BAD labels from terminal timeout. It can now mine actual failure windows, replay them, and produce continuous high-risk state-context labels with same-state proof.
