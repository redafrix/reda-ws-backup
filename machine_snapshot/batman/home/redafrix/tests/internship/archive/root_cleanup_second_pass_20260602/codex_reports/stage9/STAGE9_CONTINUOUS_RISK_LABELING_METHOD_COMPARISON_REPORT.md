# Stage 9 Continuous Risk Labeling Method Comparison Report

Generated: `2026-05-20T11:20:00+02:00`

## Executive Summary

I implemented the Stage 9 V2 continuous action-risk labeling layer on Bob and Sam.

The main training target is now:

```text
risk_score in [0.0, 1.0]
```

Meaning:

```text
0.0 = clearly good / safe / expert-like action chunk
0.5 = uncertain or mixed evidence
1.0 = clearly risky / bad / damaging / no-progress action chunk
```

This changes the target from a discrete final label to a continuous local chunk-risk label. The old labels `GOOD_STRONG`, `GOOD_WEAK`, `VALIDATED_BAD`, and `AMBIGUOUS` are now only audit/debug bins derived from the continuous score.

Most important result:

```text
The old frozen dataset does NOT contain usable high-risk continuous labels under local chunk evidence.
```

Static relabel result:

```text
Samples scored: 37,632
Old VALIDATED_BAD: 6,914
Confident high-risk continuous chunks: 0
Old VALIDATED_BAD downgraded to low/uncertain local risk: 6,914 / 6,914
CONTINUOUS_RISK_LABELS_READY_FOR_TRAINING = NO
```

This is the correct outcome for a strict relabeler. It confirms the previous diagnosis: the old `VALIDATED_BAD` labels were mostly terminal-outcome artifacts, not locally proven bad action chunks.

## What Changed

New files added on Bob and Sam:

```text
asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py
asynchvla_ws/src/data_collection_stage9/relabel_stage9_continuous_v2.py
asynchvla_ws/src/data_collection_stage9/collect_continuous_risk_dataset_v2.py
asynchvla_ws/src/data_collection_stage9/compare_stage9_labeling_methods.py
asynchvla_ws/src/data_collection_stage9/evaluate_local_quality_on_experts.py
asynchvla_ws/src/data_collection_stage9/mine_failure_windows_scripted.py
```

The old collector was not destroyed. The V2 path is separate so we can compare against the old terminal-outcome labeler.

## New Label Policy

The target is the candidate SimVLA action chunk, not the full future episode.

The V2 scorer uses:

```text
local simulator trace
target-object motion
target-goal distance change
target height change
EEF-target distance change
gripper/contact evidence when available
same-state sibling comparison
expert/VLM/failure-onset hooks when available
```

The V2 scorer does not use:

```text
terminal timeout as BAD proof
terminal failure as BAD proof
terminal success as automatic GOOD proof
parent failure as label proof
VLM-only evidence as label proof
low expert likelihood alone as BAD proof
EEF moved away alone as BAD proof
```

Terminal outcome is stored only as audit metadata.

## Continuous Score Formula

Implemented formula:

```text
risk_raw =
  0.30 * local_damage_risk
+ 0.25 * no_progress_risk
+ 0.20 * same_state_disadvantage_risk
+ 0.15 * expert_deviation_risk
+ 0.10 * failure_onset_risk
- 0.20 * local_progress_credit
```

Then:

```text
risk_score = confidence * risk_raw + (1 - confidence) * 0.5
```

This matters: low-confidence samples are pulled toward `0.5`, not forced safe or bad.

The scorer also outputs:

```text
chunk_quality = 1.0 - risk_score
risk_confidence
risk_bin
positive_evidence
negative_evidence
weak_negative_evidence
ambiguous_evidence
same_state_comparison_v2
bad_subtype
```

## Risk Bins

The bins are only for audit:

```text
SAFE_STRONG: risk_score <= 0.20
SAFE_WEAK: 0.20 < risk_score <= 0.40
UNCERTAIN: 0.40 < risk_score < 0.65
RISKY_WEAK: 0.65 <= risk_score < 0.80
RISKY_STRONG: risk_score >= 0.80
```

Training should use `risk_score` and `risk_confidence`, not hard labels.

## Static Relabel Run

Input:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940
```

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/continuous_v2/relabel_static_20260520
```

Command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
python3 -m data_collection_stage9.relabel_stage9_continuous_v2 \
  --input "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940" \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/continuous_v2/relabel_static_20260520"
```

## Static Relabel Results

Risk bins:

| risk_bin | count |
|---|---:|
| `SAFE_STRONG` | 27,938 |
| `SAFE_WEAK` | 9,686 |
| `UNCERTAIN` | 8 |

Legacy audit suggestions:

| suggestion | count |
|---|---:|
| `GOOD_WEAK` | 22,522 |
| `GOOD_STRONG` | 15,102 |
| `AMBIGUOUS` | 8 |

Old labels:

| old_label | count |
|---|---:|
| `GOOD_STRONG` | 17,930 |
| `AMBIGUOUS` | 9,025 |
| `VALIDATED_BAD` | 6,914 |
| `GOOD_WEAK` | 3,763 |

Old label by new risk bin:

| old_label / risk_bin | count |
|---|---:|
| `GOOD_STRONG / SAFE_STRONG` | 17,323 |
| `AMBIGUOUS / SAFE_STRONG` | 5,051 |
| `VALIDATED_BAD / SAFE_WEAK` | 5,042 |
| `AMBIGUOUS / SAFE_WEAK` | 3,974 |
| `GOOD_WEAK / SAFE_STRONG` | 3,700 |
| `VALIDATED_BAD / SAFE_STRONG` | 1,864 |
| `GOOD_STRONG / SAFE_WEAK` | 607 |
| `GOOD_WEAK / SAFE_WEAK` | 63 |
| `VALIDATED_BAD / UNCERTAIN` | 8 |

Key metrics:

```text
risk_score_mean: 0.1058
risk_score_max: 0.4651
risk_confidence_mean: 0.9751
confident high-risk count: 0
old VALIDATED_BAD low/uncertain under local risk: 6,914
```

Conclusion:

```text
The old frozen dataset should not be used for final risk-detector training.
```

## Scripted Failure Mining Result

Input:

```text
continuous_v2/relabel_static_20260520/continuous_risk_labels.jsonl
```

Command:

```bash
python3 -m data_collection_stage9.mine_failure_windows_scripted \
  --continuous-labels asynchvla_ws/stage9_libero_pro_risk_data/data/continuous_v2/relabel_static_20260520/continuous_risk_labels.jsonl \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/continuous_v2/relabel_static_20260520/scripted_failure_mining \
  --risk-threshold 0.75
```

Result:

```text
input samples: 37,632
episode keys: 543
scripted high-risk failure windows: 0
```

This is consistent with the static relabel: the old data does not contain locally certified high-risk chunks under the new policy.

## V2 Collector Smoke Test

I ran a tiny Bob smoke with the new local-only collector.

Output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/continuous_v2_bob_smoke_20260520
```

Command:

```bash
python3 -m data_collection_stage9.collect_continuous_risk_dataset_v2 \
  --suites libero_spatial_with_mug \
  --task-ids 0 \
  --max-parent-episodes 1 \
  --max-total-states 2 \
  --max-states-per-parent 2 \
  --parent-roll-steps 30 \
  --simvla-seeds 0 1 \
  --initial-chunk-steps 10 \
  --history-k 8 \
  --save-images \
  --save-trace-frames \
  --trace-frame-stride 5 \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/continuous_v2_bob_smoke_20260520"
```

Smoke result:

```text
selected_states: 2
samples: 4
risk_bin_counts: SAFE_WEAK = 4
terminal_continuation_used_for_label: false
candidate chunk steps: 10
trace length per sample: 10
same_state_comparison_v2: present
before agent image: present
before wrist image: present
after agent image: present
after wrist image: present
trace frames: present for agent view
```

Example sample:

```text
sample_id: libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed0
risk_score: 0.2060
risk_confidence: 0.8400
chunk_quality: 0.7940
risk_bin: SAFE_WEAK
legacy_label_suggestion: GOOD_WEAK
negative_evidence: []
weak_negative_evidence: no_progress_weak
terminal_continuation_used_for_label: false
```

## Bob/Sam Status

Bob:

```text
continuous-risk modules synced
py_compile passed
static relabel completed
method comparison completed
scripted failure mining completed
V2 local collector smoke passed
```

Sam:

```text
continuous-risk modules synced
py_compile passed
```

Sam was not used for a rollout smoke in this pass because Bob already verified the real LIBERO/SimVLA execution path and the next meaningful step is a larger V2 pilot, not another tiny duplicate smoke.

## Method Ranking After Implementation

### 1. Local simulator continuous chunk reward

Status: implemented and smoke-tested.

This is the main solution. It labels the local action chunk directly and avoids the future-terminal shortcut.

### 2. Same-state local counterfactual ranking

Status: implemented.

The scorer adds `same_state_comparison_v2` and uses sibling risk spread smoothly instead of hard terminal success/failure.

### 3. Expert LIBERO low-risk calibration

Status: interface implemented, not yet run.

Script:

```text
evaluate_local_quality_on_experts.py
```

This requires expert chunks converted into Stage 9 sample-like JSONL. Once available, the gate is:

```text
expert false high-risk rate <= 1%
```

### 4. Scripted failed-episode onset mining

Status: implemented and run on the static relabel output.

It found zero high-risk windows because the old frozen dataset has no high-risk continuous chunks. This is a diagnostic result, not a failure of the script.

### 5. VLM/AHA failure-onset mining

Status: not rerun in this implementation pass.

The previous VLM audit already showed the old `VALIDATED_BAD` set was visually suspicious. The VLM should stay an auditor/miner, not the final label source.

### 6. Horizon sensitivity

Status: deprioritized.

The V2 labeler does not use terminal horizon as label proof anymore, so horizon sensitivity is now only a diagnostic for the old dataset.

## What This Means

The implementation fixed the label target and the label format, but it also exposed the next real blocker:

```text
We still need to collect or mine real high-risk local action chunks.
```

The old frozen dataset is useful for safe/good behavior and for proving that terminal-label BADs were wrong. It is not enough for training a serious risk detector because the new strict continuous labels contain no confident high-risk examples.

## Exact Next Step

Run a V2 pilot that explicitly mines local bad chunks without terminal-horizon shortcuts:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

python3 -m data_collection_stage9.collect_continuous_risk_dataset_v2 \
  --suites libero_spatial_with_mug libero_object_with_mug libero_goal_with_mug libero_10_with_mug \
  --task-ids 0 1 2 3 4 5 6 7 8 9 \
  --max-parent-episodes 8 \
  --max-total-states 400 \
  --max-states-per-parent 3 \
  --parent-roll-steps 160 \
  --simvla-seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \
  --initial-chunk-steps 10 \
  --history-k 8 \
  --preferred-phases NEAR_GRASP GRASP_OR_LIFT TRANSPORT PLACE_OR_GOAL STUCK_OR_NO_PROGRESS \
  --save-images \
  --save-trace-frames \
  --trace-frame-stride 5 \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/continuous_v2_local_pilot_001"
```

Then run:

```bash
python3 -m data_collection_stage9.relabel_stage9_continuous_v2 \
  --input "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/continuous_v2_local_pilot_001" \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/continuous_v2_local_pilot_001_relabel"
```

If this still produces zero high-risk chunks, the sampler needs to deliberately mine failed episodes and replay chunks around scripted/VLM failure onsets. Do not lower the risk thresholds just to create positives.

## Final Decision

```text
CONTINUOUS_RISK_LABELING_CODE_IMPLEMENTED = YES
BOB_COMPILE_PASS = YES
SAM_COMPILE_PASS = YES
BOB_V2_SMOKE_PASS = YES
OLD_FROZEN_DATASET_READY_FOR_CONTINUOUS_RISK_TRAINING = NO
REASON = zero confident high-risk chunks after strict local relabeling
NEXT_REQUIRED_ACTION = run V2 local pilot plus expert calibration and failure-onset mining
```

The goal is not many BAD labels. The goal is a continuous risk signal that is actually true for the action chunk.
