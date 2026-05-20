# Stage 9 VLM Label Audit Experiment Report

Generated: `2026-05-19T17:35:00+02:00`

## Executive Summary

I implemented and ran a VLM audit layer on Bob and Sam. The VLM audit should be used as a disagreement detector, not as a final labeler.

Main result: the VLM experiment supports the earlier diagnosis. A large block of current `VALIDATED_BAD` labels is suspicious because the bad label comes from terminal failure / same-state outcome logic, not from clear local bad action evidence.

The strongest finding is from the blind Qwen3-VL pass on Bob:

- `bad_no_raw_local_bad`: `40/40` looked `good` to the blind VLM.
- `bad_terminal_alt_only`: `40/40` looked `good` to the blind VLM.
- `bad_terminal_timeout`: `40/40` looked `good` to the blind VLM.
- `bad_with_local_good_progress`: `39/40` looked `good` to the blind VLM.

This does not prove those actions are GOOD. It does prove they should not be trusted as final `VALIDATED_BAD` without replay/long-horizon simulator confirmation.

Final decision:

`CURRENT_VALIDATED_BAD_LABELS_ARE_NOT_CLEAN_ENOUGH_FOR_FINAL_TRAINING = YES`

## Code Added

Added under `asynchvla_ws/src/data_collection_stage9/` on Bob and Sam:

- `stage9_vlm_audit_prepare.py`
- `stage9_vlm_audit_run.py`
- `stage9_vlm_audit_aggregate.py`

These scripts:

1. Select suspicious and control samples from the frozen group-safe split.
2. Load full source samples from `source_jsonl`.
3. Build before/after candidate vs same-state sibling contact sheets.
4. Run Qwen VLMs with strict JSON prompts.
5. Aggregate behavior judgments and suspicious-label disagreements.

## Environment And Models

Bob:

- GPU: RTX 4070 Ti SUPER, 16GB.
- Working model: `Qwen/Qwen3-VL-2B-Instruct`.
- Added runtime deps: `qwen-vl-utils`, `decord`, `bitsandbytes`, `accelerate`, `av`, `imageio`, `imageio-ffmpeg`, `jinja2>=3.1`.
- Qwen3-VL-4B initially stalled on large shard download until `HF_HUB_DISABLE_XET=1`; to avoid wasting time, I used Qwen3-VL-2B for the completed audit.

Sam:

- GPU: RTX 4070 Ti SUPER, 16GB.
- Working model: `Qwen/Qwen2.5-VL-3B-Instruct`.
- `transformers==4.57.6` was incompatible with Sam Torch for Qwen imports, so Sam was pinned to `transformers==4.51.3`.
- Qwen2.5-VL-7B 4-bit download/setup was not used for the completed audit. Qwen2.5-VL-3B without 4-bit produced valid JSON.

## Review Sets

Metric/label-assisted audit:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519`
- Manifest size: `560` review sheets.
- Results: `640` VLM judgments because `bad_terminal_alt_only` was checked by both Bob and Sam.
- Aggregate: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/aggregate`

Blind audit:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind`
- Manifest size: `280` review sheets.
- Results: `320` VLM judgments.
- Aggregate: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/aggregate`

## Metric/Label-Assisted Audit Results

This pass shows the VLM the current label, reasons, and metrics. It is useful for triage, but it is label-biased.

Results:

- Total VLM outputs: `640`
- Status: `640 ok`
- Models:
  - Qwen3-VL-2B: `320`
  - Qwen2.5-VL-3B: `320`

Behavior by current label:

- `VALIDATED_BAD`: `478 bad`, `2 missing`
- `AMBIGUOUS`: `80 bad`
- `GOOD_STRONG`: `55 good`, `25 bad`

Interpretation:

Because the current label/reasons were visible, this pass over-confirms existing BAD labels. I do not treat it as independent evidence. It is still useful for finding review examples and confirming the pipeline works.

## Blind Audit Results

This pass hides the dataset label and simulator reasons from the visual sheet and prompt. It is a better disagreement detector, though still imperfect because only before/after images are available, not full replay videos.

Results:

- Total VLM outputs: `320`
- Status: `320 ok`
- Models:
  - Qwen3-VL-2B: `160`
  - Qwen2.5-VL-3B: `160`

Blind behavior by current label:

- `VALIDATED_BAD`: `160 good`, `80 bad`
- `AMBIGUOUS`: `40 bad`
- `GOOD_STRONG`: `40 bad`

Important model-specific result:

Bob/Qwen3-VL-2B on suspicious BAD categories:

- `bad_no_raw_local_bad`: `40 good`, `0 bad`
- `bad_terminal_alt_only`: `40 good`, `0 bad`
- `bad_terminal_timeout`: `40 good`, `0 bad`
- `bad_with_local_good_progress`: `39 good`, `1 bad`

Sam/Qwen2.5-VL-3B blind behavior:

- It called all `GOOD_STRONG` controls bad.
- It called all `AMBIGUOUS` controls bad.
- It called most random `VALIDATED_BAD` bad.

Interpretation:

Qwen2.5-VL-3B is too aggressive in blind before/after mode and should not be trusted alone. Qwen3-VL-2B gave the more useful signal: the exact suspicious BAD classes often visually look fine or successful.

## Deterministic Relabel Recommendation File

I also wrote a deterministic recommendation file for all current `VALIDATED_BAD` samples affected by the known terminal-label flaw:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/terminal_bad_relabel_recommendations.jsonl`

Unique samples recommended for downgrade/review:

- `2,230`

Issue counts, not mutually exclusive:

- `terminal_alt_only`: `1,948`
- `no_raw_local_bad`: `1,948`
- `has_local_good_progress`: `1,333`
- `terminal_timeout`: `738`

Recommendation for these samples:

`downgrade_to_AMBIGUOUS_pending_replay_or_long_horizon_success_check`

## What This Means

The current dataset is not clean enough to treat all `VALIDATED_BAD` labels as certified action-risk labels.

The VLM audit agrees with the simulator-code audit:

- Terminal timeout / no success by horizon is not strong BAD evidence.
- Same-state alternative success is useful, but not enough by itself.
- If local evidence shows progress, the sample should not remain `VALIDATED_BAD` unless there is explicit strong local damage.
- Before/after VLM review is useful for finding suspicious labels, but it cannot certify labels alone.

## Recommended Fix

Before retraining seriously, make a corrected frozen dataset v2:

1. Downgrade any `VALIDATED_BAD` whose only reason is `terminal_failure_with_successful_same_state_alternative`.
2. Downgrade any `VALIDATED_BAD` with no raw local bad evidence unless replay video/metrics prove real degradation.
3. Downgrade any `VALIDATED_BAD` with local strong/weak good progress unless a strong local bad event is also replay-confirmed.
4. Treat terminal timeout as `not_success_yet`, not failure.
5. Use terminal horizon only as audit metadata, not as a standalone BAD source.
6. Generate real replay videos for the remaining candidate BAD samples and rerun Qwen3-VL as a review tool.
7. Recreate group-safe splits and retrain.

## Best VLM Choice After This Experiment

Use `Qwen/Qwen3-VL-2B-Instruct` or a larger Qwen3-VL model if it downloads and fits. In this experiment, Qwen3 gave the most useful blind disagreement signal.

Do not use Qwen2.5-VL-3B blind before/after output as a final judge; it over-called BAD on controls. Qwen2.5-VL may still be useful with richer replay videos and metric context, but not as the primary blind auditor.

## Paths

Code:

- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/stage9_vlm_audit_prepare.py`
- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/stage9_vlm_audit_run.py`
- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/stage9_vlm_audit_aggregate.py`
- Sam: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9/`

Outputs:

- Assisted audit: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519`
- Blind audit: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind`
- Local copied aggregates: `/home/redafrix/tests/internship/codex_reports/stage9/vlm_audit/`

## Final Decision

`VLM_AUDIT_PIPELINE_WORKS = YES`

`VLM_CAN_CERTIFY_LABELS_ALONE = NO`

`CURRENT_DATASET_NEEDS_RELABEL_V2_BEFORE_FINAL_TRAINING = YES`

