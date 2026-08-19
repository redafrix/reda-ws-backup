# AGY Stage 0B — FORENSIC PRETEST AUDIT ONLY

Agy is mechanical only. This stage exists because Stage0 hard-coded several audit conclusions instead of proving them.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Branch:
`experiment/dean-isaac-mimic-risk-4904-3cm350-20260819`

Current provisional Stage0 commit:
`1d6dfb84cbd25e4438e92acd8332bd789379adf2`

Current provisional derived dataset:
`$W/derived_datasets/isaac_mimic_h10_strict_3cm350_seen4904_v3`

DO NOT SCORE HELD-OUT TEST.
DO NOT SCORE OOD.
DO NOT RETRAIN.
DO NOT MODIFY EXISTING HEAVY ARRAYS OR CHECKPOINTS.
DO NOT LAUNCH ISAAC/SIMVLA.
DO NOT TOUCH HARD1000.

The output of this stage is EVIDENCE ONLY. ChatGPT decides whether the existing training may be accepted or must be discarded/rebuilt.

## A. Prove the protocol from actual files — no hard-coded description

Read exactly:

`$W/frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1/PROTOCOL_3CM350.json`
`$W/frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1/manifest.json`

1. Compute SHA256 of both.
2. Copy the COMPLETE UTF-8 JSON content of `PROTOCOL_3CM350.json` into the small snapshot as `SOURCE_PROTOCOL_3CM350_VERBATIM.json` without changing values/order other than normal JSON pretty printing if needed.
3. Copy the complete source `manifest.json` into the snapshot as `SOURCE_DATASET_MANIFEST_VERBATIM.json` if it is reasonably small; otherwise copy all top-level keys plus every protocol/label/census/source-lineage field and record the original file SHA.
4. Mechanically identify the exact JSON key paths, values and units that prove or disprove:
   - threshold = 0.030 m
   - control-tick horizon = 350
   - control frequency = 30 Hz
   - success = first reach / any reach within horizon
   - dwell requirement = none / zero
   - execution action horizon H10
5. Do NOT emit PASS just because filename contains `3CM350`.
6. If the files do not explicitly prove one of these semantics, mark that item `NOT_EXPLICITLY_PROVEN` and return the raw evidence. Do not infer.

Write `PROTOCOL_PROOF_V2.json` with exact key paths and values.

## B. Prove complete source lineage and action binding

Do not assume the new 4904 dataset came only from Round0 and Round2.

1. Read all 4904 entries in source `episodes.json`.
2. Enumerate every distinct source collection/run/root/manfiest reference present in those entries and/or source manifest lineage.
3. For each distinct source collection:
   - locate its actual run/source manifest;
   - SHA256 it;
   - record collector source SHA from the manifest;
   - record action dimension from the manifest if explicit;
   - record action horizon if explicit;
   - record execution mode if explicit;
   - record any controller source path/SHA if explicit.
4. Also hash the live verified controller source used for the 7D action semantics if present:
   `/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/control/reaching_pose_actions.py`
   and compare to previously verified SHA256:
   `8c0acff1bc1a1d3d78341f15d5e5ba6b7d7aae92a17e6aeb93dd59b43d4914f9`
5. `ACTION_BINDING_V2 = PROVEN` only if EVERY source lineage component used by the 4904 episodes is compatible and the manifest evidence explicitly supports H10 / 7D / chunk_h10 semantics. If some field is not explicit, return `INCOMPLETE_EVIDENCE`; do not hard-code it.

Write `SOURCE_LINEAGE_AND_ACTION_BINDING_V2.json`.

## C. TRUE full schema census over all 96,813 rows

Stream every row again, read-only.

For every row recursively walk all JSON dictionaries/lists and count exact occurrences / JSON paths for these exact key names:

- `sample_pairwise_mse_mean`
- `sample_variance_max`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`

For EACH of the five keys report:

- rows containing key anywhere recursively / 96813
- all distinct JSON paths where found
- all observed value shapes/lengths
- finite values count
- first 3 `(episode_id, decision_index, path, shape)` examples if found

Also recursively inventory keys whose lowercase name contains any of:

`denois`, `pairwise`, `variance`, `velocity`, `vector_field`, `sample_`, `uncert`, `trace`, `update_vector`, `initial_noise`

For those candidate keys report unique key name, JSON paths, row-presence count, and shapes. This is evidence only; do NOT map alternative names to the Mimic contract yourself.

Separately prove on ALL 96813 rows:

- `main_candidate_action_chunk_env` exists and shape exactly `[10,7]`
- `ace_candidate_chunks_env` exists with at least 7 alternatives and every selected first-7 shape `[7,10,7]`
- `decision_index` exists, integer, and per episode is exactly contiguous from 0 to N-1 with no duplicate/gap
- episode row count equals `retained_decision_rows`
- parent label for each row equals source episode `binary_label`

Write:

`FULL_SCHEMA_CENSUS_V2.json`
`MIMIC_FIVE_TRACE_FIELD_AUDIT_V2.json`

Do not write `dynamics_mode` as a freehand decision. Instead mechanically output:

`exact_five_named_traces_present_all_rows = YES|NO`

If YES, do NOT modify the existing dataset; stop after audit so ChatGPT can inspect semantics/source code before deciding EXACT mode.
If NO, existing STRICT_MISSING remains a candidate pending the rest of this audit.

## D. Recompute fresh feature parity against current derived dataset

This does not alter files.

Using the source rows and the already frozen formulas from `NEW4904_MIMIC_RETRAIN_SPEC.md`, independently recompute for ALL 96813 rows:

- nine disagreement scalars from main + first seven ENV alternatives
- H10 `[10,6]` horizon tensor
- three temporal-change scalars
- parent labels
- episode ordinal/index
- decision index
- split index from the exact TopK8 split artifact

Compare against the current derived arrays:

`$W/derived_datasets/isaac_mimic_h10_strict_3cm350_seen4904_v3`

Report exact equality where dtype/serialization permits and maximum absolute error otherwise.

Required checks:

- dims0..8 parity
- dims34..36 parity
- horizon parity
- labels exact
- episode_index exact
- decision_index exact
- split_index exact
- dims9..33 are exactly zero in current provisional dataset
- all array hashes still equal the hashes in current dataset manifest

Write `CURRENT_DERIVED_PARITY_AUDIT_V2.json`.

## E. Prove split identity, not just counts

Read:
`$W/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/split_manifest.json`

Compare the exact episode ID set assigned to train/validation/test with the provisional Mimic `episode_ids.json + split_index.npy` mapping.

For every split report:

- TopK8 unique episode IDs
- Mimic unique episode IDs
- intersection
- TopK8-only
- Mimic-only
- sorted-set SHA256 TopK8
- sorted-set SHA256 Mimic
- exact set equality

Also prove no episode occurs in more than one split.

Write `EXACT_SPLIT_IDENTITY_V2.json`.

## F. Training-history integrity audit — NO retraining

For seeds 0..4 read the ACTUAL Dean files:

`$W/models/isaac_mimic_h10_strict_3cm350_seen4904_v3/seed_<s>/training_summary.json`

For each seed:

1. SHA256 training summary.
2. Prove exactly 25 epoch records, epochs 0..24 once each.
3. Prove all train losses / validation AUROC / validation AUPRC finite.
4. Mechanically recompute argmax validation AUPRC with earliest exact tie.
5. Verify recomputed best epoch/AUPRC equals the summary, TRAINING_FREEZE and selected checkpoint metadata.
6. SHA256 selected checkpoint and verify freeze binding.
7. Verify every seed starts from its own seed and no resume/old checkpoint path appears in summary/code/checkpoint metadata.
8. Record NEW4904 train positive/negative row counts used for `pos_weight`; prove they are 12670 positive and 55055 negative and recompute the ratio.
9. Copy all five training summaries into `stage0b_snapshot/` so ChatGPT can inspect the complete epoch histories.

### Seed-2 outlier audit

Seed2 validation AUPRC is much higher than seeds 0/1/3/4. Do NOT label it good/bad and do NOT rerun it.

Mechanically:

- reload seed2 selected checkpoint;
- score VALIDATION ONLY again;
- recompute row AUROC/AUPRC from those scores;
- verify exact/small-tolerance parity with its frozen validation result;
- verify the validation row indices are exactly the same 14,562 rows used for every other seed;
- verify validation labels are the same shared array and 77 failure episodes / 658 success episodes;
- verify no test indices occur in the validation dataset object;
- save SHA256 of rescore scores array plus recomputed metrics.

Repeat the same validation rescore for seed0 as a control.

Write `SEED2_OUTLIER_INTEGRITY_AUDIT.json`.

Do NOT choose seed2 as primary. Primary remains seed0 regardless.

## G. Calibration integrity

For each frozen seed validation result:

- confirm 735 validation episodes = 658 success / 77 failure;
- recompute successful-episode maximum scores from VALIDATION only;
- independently recompute conformal alpha .05/.10/.15 using:
  `k=min(n,ceil((n+1)*(1-alpha)))`, kth 1-based order statistic;
- verify stored thresholds;
- recompute row-best-F1 and q90/q95/q99;
- verify freeze contents and SHA.

Do not access test scores.

Write `VALIDATION_CALIBRATION_RECHECK_V2.json`.

## H. Tests and no-test proof

Run the existing tests plus any new audit tests needed.

Mechanically search the NEW experiment model/evaluation roots for any held-out score/result files created before this audit. Listing file names is allowed; do not score anything.

Prove:

- no test scoring invocation occurred in Stage0 code;
- no OOD scoring invocation occurred;
- current `held_out_test_observed_by_training=false` and `ood_observed_by_training=false` remain unchanged.

Write `NO_TEST_ACCESS_PROOF_V2.json`.

## I. Commit only small evidence

Commit:

- Stage0B audit code
- the small JSON audits above
- copies of all five `training_summary.json`
- no model checkpoints
- no raw/heavy arrays
- no score arrays if large; hashes/metrics only

Do not change the provisional dataset/model/evaluation artifacts.

## Required return block

Return ONLY:

```text
PROTOCOL_PROOF_V2:
  status: PROVEN|INCOMPLETE_EVIDENCE|FAILED
  protocol_file_sha256: ...
  manifest_sha256: ...
  threshold_key_path/value: ...
  horizon_ticks_key_path/value: ...
  hz_key_path/value: ...
  success_semantics_key_path/value: ...
  dwell_key_path/value: ...
  action_horizon_key_path/value: ...

SOURCE_LINEAGE_ACTION_V2:
  distinct_source_collections: ...
  all_source_manifests_hashed: YES|NO
  all_collector_shas_compatible: YES|NO
  all_action_dim_7_proven: YES|NO|INCOMPLETE
  all_h10_proven: YES|NO|INCOMPLETE
  all_chunk_h10_proven: YES|NO|INCOMPLETE
  live_controller_sha_match: YES|NO
  status: PROVEN|INCOMPLETE_EVIDENCE|FAILED

MIMIC_TRACE_AUDIT_V2:
  rows_streamed: .../96813
  sample_pairwise_mse_mean_rows: ...
  sample_variance_max_rows: ...
  sample_variance_mean_rows: ...
  sample_velocity_mse_mean_rows: ...
  vector_field_l2_mean_rows: ...
  exact_five_named_traces_present_all_rows: YES|NO
  candidate_trace_like_keys_found: <count>

SOURCE_ROW_SCHEMA_V2:
  main_env_all_10x7: YES|NO
  first7_alt_env_all_7x10x7: YES|NO
  decision_indices_contiguous_all_eps: YES|NO
  row_counts_match_episode_metadata: YES|NO
  row_parent_labels_match: YES|NO

DERIVED_PARITY_V2:
  dims0_8_max_abs: ...
  dims34_36_max_abs: ...
  horizon_max_abs: ...
  labels_exact: YES|NO
  episode_index_exact: YES|NO
  decision_index_exact: YES|NO
  split_index_exact: YES|NO
  dims9_33_exact_zero: YES|NO
  heavy_hashes_match_manifest: YES|NO

SPLIT_IDENTITY_V2:
  train_exact_set_equal: YES|NO
  validation_exact_set_equal: YES|NO
  test_exact_set_equal: YES|NO
  cross_split_duplicate_episodes: ...

TRAINING_INTEGRITY_V2:
  seed0: <25logs yes/no> | <recomputed best epoch> | <recomputed AUPRC> | <checkpoint SHA match yes/no>
  seed1: ...
  seed2: ...
  seed3: ...
  seed4: ...
  pos_weight_counts: 12670/55055 VERIFIED|FAILED
  old_checkpoint_resume_detected: YES|NO

SEED2_OUTLIER_AUDIT:
  seed2_validation_rescore_auroc: ...
  seed2_validation_rescore_auprc: ...
  seed2_freeze_parity: YES|NO
  seed0_control_parity: YES|NO
  validation_indices_shared_exactly: YES|NO
  test_indices_in_validation: 0|<count>

CALIBRATION_RECHECK_V2:
  all5_threshold_freezes_match: YES|NO
  validation_only: YES|NO

NO_TEST_ACCESS_V2:
  heldout_score_files_found_before_test_stage: <count>
  stage0_test_scoring_invocation: YES|NO
  stage0_ood_scoring_invocation: YES|NO

PROVISIONAL_STAGE0_DISPOSITION:
  DO_NOT_DECIDE — ChatGPT will decide from evidence

HELD_OUT_TEST_SCORED:
  NO
OOD_SCORED:
  NO

COMMIT:
  <sha>
```
