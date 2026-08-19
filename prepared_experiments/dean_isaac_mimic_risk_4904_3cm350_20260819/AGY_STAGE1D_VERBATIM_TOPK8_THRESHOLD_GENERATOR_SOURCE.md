# AGY Stage 1D — verbatim TopK8 threshold-generator source proof

Pure provenance only. No scoring, no training, no recalibration.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Branch:
`experiment/dean-isaac-mimic-risk-4904-3cm350-20260819`

## Purpose

Stage1C still asserted semantic booleans in its audit script. Close the final gap by committing VERBATIM source evidence from the exact local files whose SHA256s Stage1C reported:

- `$W/risk_head_pipeline/train_isaac_topk8.py`
  expected SHA256 `adc0f368c5f277df83590540d3a2bd656ca19ba5228648ef8e4d19a0f640a660`
- `$W/risk_head_pipeline/common.py`
  expected SHA256 `e89a69592ed75b8bb52850019780f6c8d4309e9a82186c59d3e01afbc2822c46`

Do not edit those source files.

## Required evidence

1. Hash both exact local files and require the expected SHA256s above.
2. Copy VERBATIM into the Stage1D snapshot:
   - the complete definition of `threshold_table` from `common.py`, including every line needed to see how precision, recall, F1, threshold indexing and tie behavior are computed;
   - the complete contiguous block in `train_isaac_topk8.py` that:
     a. constructs/identifies train, validation and test datasets/indices;
     b. scores validation;
     c. calls `threshold_table` with validation labels and validation scores;
     d. writes/freezes `thresholds.json`;
     e. only afterwards scores/applies thresholds to test.
3. Include enough surrounding source lines to make variable identities unambiguous. Do not paraphrase.
4. Record exact source line numbers from each original local file.
5. Mechanically hash the copied verbatim text snippets and record their hashes.

## Semantic decision rule

From those verbatim snippets only, return:

- `validation_only_selection=YES` only if the call site visibly passes validation labels and validation scores to the threshold function.
- `row_level_f1_argmax=YES` only if the function visibly computes row-level precision/recall/F1 from the supplied arrays and chooses the maximum-F1 threshold.
- `test_independent_selection=YES` only if source execution order visibly freezes thresholds before test evaluation uses them.
- `matched_rule_equivalent_to_mimic_row_best_f1=YES` only if this is the same rule already frozen for Mimic: validation-row precision/recall curve -> maximum F1 threshold -> unchanged application to test.

Do not infer any YES from file names, comments, JSON key names or Stage1C outputs.

## Prohibitions

Do NOT run any model.
Do NOT score any split.
Do NOT recompute predictions.
Do NOT retrain.
Do NOT alter thresholds.
Do NOT touch OOD/HARD1000/Isaac.

## Required return block

Return ONLY:

```text
VERBATIM_SOURCE_BINDING_V4:
  train_source_path: ...
  train_source_sha256: ...
  train_source_expected_sha_match: YES|NO
  common_source_path: ...
  common_source_sha256: ...
  common_source_expected_sha_match: YES|NO
  threshold_table_line_range: ...
  train_validation_threshold_test_order_line_range: ...
  threshold_table_snippet_sha256: ...
  train_order_snippet_sha256: ...

SOURCE_SEMANTICS_V4:
  validation_only_selection: YES|NO|NOT_PROVEN
  row_level_f1_argmax: YES|NO|NOT_PROVEN
  test_independent_selection: YES|NO|NOT_PROVEN
  matched_rule_equivalent_to_mimic_row_best_f1: YES|NO|NOT_PROVEN

FINAL_ABLATION_COMPARISON_DISPOSITION_V4:
  threshold_independent_comparison: FINAL
  matched_row_best_f1_comparison: FINAL|NOT_PROVEN
  reason: ...

NO_MODEL_RERUN:
  YES
NO_SCORING:
  YES

COMMIT:
  <sha>
```
