# AGY Stage 1C — TopK8 best-F1 threshold semantics proof

This stage is provenance-only. It exists because Stage1B mechanically proved query-key equality but still hard-coded several semantic booleans for the TopK8 best-val-F1 operating point.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Branch:
`experiment/dean-isaac-mimic-risk-4904-3cm350-20260819`

Mimic Stage1 result is FINAL. Do not score anything.

## Goal

Prove from source artifact CONTENTS, not from names or hard-coded booleans, whether TopK8 threshold `0.579133152961731` is:

1. derived from validation only;
2. selected by row-level maximum F1 over validation predictions;
3. tied to the same frozen 735-episode validation split used by split manifest SHA `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`;
4. independent of held-out test labels/scores at selection time;
5. therefore rule-equivalent to Mimic `row_best_f1` for matched operating-point comparison.

## Required source files

Read and SHA256:

- `$W/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/thresholds.json`
- `$W/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/CONFORMAL_THRESHOLD_SWEEP.json`
- `$W/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/split_manifest.json`
- any training/validation metadata or script artifact explicitly referenced by those files as producing `best_val_f1`

Copy the COMPLETE text contents of `thresholds.json` and `CONFORMAL_THRESHOLD_SWEEP.json` into the Stage1C snapshot verbatim. If they are too large for a normal small JSON audit commit, copy all metadata plus the full `validation_table` and the exact fields describing how `best_val_f1` was produced; do not summarize away the evidence.

## Mechanical proof requirements

Do not set any of the following fields to YES merely because the file/key is named `validation_table` or `best_val_f1`.

For `validation_only_selection=YES`, identify explicit artifact content or generating-code evidence showing threshold search consumed validation predictions/labels and did not consume test predictions/labels.

For `criterion=row-level maximum F1`, identify explicit artifact content or generating-code evidence showing the threshold is the argmax of row-level F1. If candidate threshold rows are stored, mechanically verify that `0.579133152961731` has the maximum validation F1, using earliest-tie behavior if relevant.

For `same_validation_split=YES`, recover the exact episode IDs or a bound split SHA from the validation threshold artifact/generator. Compare against the 735 IDs in split manifest SHA `34db754f...`. If only counts are available, this is NOT enough.

For `test_independent_selection=YES`, identify explicit evidence that the threshold was frozen before or independently of test scoring. A `test_table` in a later sweep file is acceptable only if the threshold itself is already bound to the validation selection and the test table merely applies it.

For `matched_rule_equivalent_to_mimic_row_best_f1=YES`, require both sides to use the same semantics: row score threshold chosen by validation row-level F1, then frozen and applied unchanged to test.

If any required semantic fact cannot be proven from existing frozen files/code, return NOT_PROVEN. Do not infer.

## Absolute prohibitions

Do NOT:
- run any model
- score any split
- recompute model predictions
- train
- recalibrate from raw scores
- change thresholds
- modify any existing result
- touch OOD/HARD1000/Isaac

Pure file inspection and deterministic arithmetic over already-stored validation threshold tables are allowed.

## Required return block

Return ONLY:

```text
TOPK8_THRESHOLD_SOURCE_FILES_V3:
  thresholds_path: ...
  thresholds_sha256: ...
  sweep_path: ...
  sweep_sha256: ...
  split_manifest_sha256: ...
  generator_or_metadata_evidence: ...

BEST_VAL_F1_SEMANTICS_V3:
  threshold: ...
  validation_only_selection: YES|NO|NOT_PROVEN
  row_level_f1_argmax: YES|NO|NOT_PROVEN
  argmax_verified_from_stored_table: YES|NO|NOT_AVAILABLE
  same_validation_split_735_ids: YES|NO|NOT_PROVEN
  test_independent_selection: YES|NO|NOT_PROVEN
  threshold_matches_thresholds_json: YES|NO
  threshold_matches_test_results: YES|NO
  matched_rule_equivalent_to_mimic_row_best_f1: YES|NO|NOT_PROVEN

MATCHED_BEST_F1_DISPOSITION_V3:
  status: VALID|NOT_PROVEN
  reason: ...

NO_MODEL_RERUN:
  YES
NO_SCORING:
  YES

COMMIT:
  <sha>
```
