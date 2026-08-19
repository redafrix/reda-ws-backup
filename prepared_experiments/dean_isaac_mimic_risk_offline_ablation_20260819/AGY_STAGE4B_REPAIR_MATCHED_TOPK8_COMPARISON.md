# Stage 4B — repair the TopK8 comparison provenance ONLY

Agy is a mechanical operator. Do NOT rerun either model. Do NOT retrain. Do NOT change any threshold. Do NOT touch OOD.

The Stage4 held-out Mimic results are frozen and must remain byte-identical.

The previous Stage4 conclusion `membership_exact_match: NO (133/600 overlap)` is suspected to be wrong because it conflicts with the cryptographic dataset provenance.

## Known cryptographic facts to verify mechanically

Current Mimic derived dataset V2 manifest:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_c0dyn_v1/dataset_manifest_v2.json`

It records:
- source frozen TopK8 dataset manifest SHA256 = `8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859`
- source split assignments SHA256 = `a4b82dd6e6d944b2719ea071d1e66636cc4816e5e159c23adee382ff9e9ecac3`
- current test rows = 11368
- current test episodes = 600

Historical TopK8 result:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_h10_topk8_temporal_v1/results.json`

Historical TopK8 dataset root:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen_h10_topk8_v1`

TopK8 result is expected to record dataset manifest SHA256:
`8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859`

## 1. Hash identity gate

Mechanically SHA256 these files:

- TopK8 `dataset_manifest.json`
- TopK8 `split_assignments.json`
- Mimic `dataset_manifest_v2.json`
- Mimic `episode_ids.json`
- Mimic `split_index.npy`
- Mimic `episode_index.npy`
- Mimic `decision_index.npy`

Require:
- TopK8 dataset manifest SHA == V2 `source_frozen_dataset_manifest_sha256`
- TopK8 split assignments SHA == V2 `source_split_assignments_sha256`
- TopK8 `results.json` dataset_manifest_sha256 == same manifest SHA

If any fails: STOP and return HASH_IDENTITY_FAILED.

## 2. Reconstruct current Mimic test episode IDs correctly

Do NOT compare integer `episode_index` values to string source episode IDs.

Current Mimic materialization defined `episode_index` as the ordinal index into `episode_ids.json`.

Mechanically reconstruct the set:

`mimic_test_ids = { episode_ids[episode_index[row]] for every row where split_index[row] == 2 }`

Verify:
- exactly 600 unique IDs
- exactly 11368 test rows
- no episode has rows in more than one split

## 3. Reconstruct source TopK8 test IDs from split_assignments.json

Parse the actual schema of `split_assignments.json` mechanically.

Construct:
`topk8_test_ids = exact episode/source IDs whose assigned split is test`

Do not use any unrelated historical split list, model output ordinal, scene ID list, or stale test membership file.

Verify exactly 600 unique test IDs.

## 4. Exact membership proof

Compare the two sets as strings.

Return:
- intersection count
- Mimic-only count
- TopK8-only count
- exact_set_equal YES/NO

If NO, write the first 50 IDs from each difference and identify precisely why the Mimic materializer can point to the same split-assignment SHA yet produce different membership. Do not invent an explanation.

If YES, mark the Stage4 `133/600 overlap` result as INVALID due to identifier-space/comparison error and identify the exact buggy comparison source if traceable.

## 5. Row-count / label proof

For the current Mimic test, report:
- 11368 rows expected
- 586 success episodes expected
- 14 failure episodes expected

For historical TopK8 `seen_test`, prove from `results.json` confusion counts / episode metrics:
- step rows total
- success episodes
- failure episodes

Do not rerun TopK8.

## 6. Correct matched-split comparison (ONLY if exact_set_equal=YES)

Use ONLY already-frozen results.

### Threshold-independent

TopK8 from historical `results.json` seen_test:
- row AUROC
- row AUPRC

Mimic primary seed0 from frozen held-out result:
- row AUROC
- row AUPRC

Compute Mimic minus TopK8 deltas.

### Same validation-selection/calibration rule: row best-F1

This is the primary thresholded architecture comparison because both use a validation-derived row best-F1 threshold.

TopK8:
- threshold from historical `thresholds.json` key `best_val_f1`
- test episode metrics from historical `results.json` key `seen_test.best_val_f1`

Mimic:
- threshold from seed0 frozen validation key `row_best_f1`
- test episode metrics from seed0 frozen held-out key `row_best_f1`

Report for each:
- success false alarms count/586 and percent
- failure detection count/14
- Det@10 count/14
- Det@25 count/14
- Det@50 count/14
- mean first detection fraction

Compute only integer-count deltas and percentage-point FA delta. Do not claim statistical significance.

### Fixed 0.5 supplemental

Report both models at fixed 0.5 as supplemental only.

### Mimic predeclared alpha=.10

Keep Mimic alpha=.10 as the primary Mimic operating point for its own result, but do NOT label it as the same calibration rule as TopK8 best-val-F1.

For descriptive context only, show TopK8 fixed0.5 beside Mimic alpha=.10 because their observed test episode FA rates are similar. Label this explicitly `DESCRIPTIVE_SIMILAR_OBSERVED_FA`, not a predeclared matched operating point.

## 7. Freeze corrected comparison

Create small artifacts only:

- `heldout_snapshot/TOPK8_MATCHED_SPLIT_PROVENANCE.json`
- `heldout_snapshot/TOPK8_MATCHED_COMPARISON.json`
- `heldout_snapshot/STAGE4B_CORRECTED_COMPARISON.md`

Do NOT modify `HELDOUT_SEEN_FREEZE.json`.

Commit exactly:
`audit(dean): repair TopK8 matched-split comparison`

Push branch.

## RETURN ONLY

HASH_IDENTITY:
topk8_dataset_manifest_sha256:
topk8_split_assignments_sha256:
mimic_source_manifest_expected_sha256:
mimic_source_split_expected_sha256:
all_match:

MEMBERSHIP:
mimic_test_unique:
topk8_test_unique:
intersection:
mimic_only:
topk8_only:
exact_set_equal:
previous_133_overlap_status:

ROW_LABEL_PARITY:
mimic_rows:
topk8_rows:
mimic_success/failure_eps:
topk8_success/failure_eps:

THRESHOLD_INDEPENDENT:
topk8_auroc:
mimic_auroc:
delta_mimic_minus_topk8:
topk8_auprc:
mimic_auprc:
delta_mimic_minus_topk8:

ROW_BEST_F1_MATCHED:
topk8_threshold:
topk8_FA:
topk8_Det:
topk8_Det10:
topk8_Det25:
topk8_Det50:
mimic_threshold:
mimic_FA:
mimic_Det:
mimic_Det10:
mimic_Det25:
mimic_Det50:
FA_delta_pp_mimic_minus_topk8:
Det_delta_count:
Det10_delta_count:
Det25_delta_count:
Det50_delta_count:

FIXED_05_SUPPLEMENTAL:
topk8_FA/Det/Det10/Det25/Det50:
mimic_FA/Det/Det10/Det25/Det50:

MIMIC_PRIMARY_ALPHA010:
threshold:
FA/Det/Det10/Det25/Det50:

NO_MODEL_RERUN:
YES
NO_TRAINING:
YES
OOD_SCORED:
NO
HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
