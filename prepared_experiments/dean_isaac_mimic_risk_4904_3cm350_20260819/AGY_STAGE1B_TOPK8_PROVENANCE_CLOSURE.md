# AGY Stage 1B — TopK8 Seen4904 comparison provenance closure

This stage is provenance-only. The Mimic V3 held-out result from Stage1 is FINAL and MUST NOT be rerun.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Branch:
`experiment/dean-isaac-mimic-risk-4904-3cm350-20260819`

Mimic experiment:
`isaac_mimic_h10_strict_3cm350_seen4904_v3`

TopK8 model:
`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`

Known Mimic Stage1 commit:
`dc55454c180bc79fe0a91729c2bfbc5469799854`

## Purpose

Repair only the comparison provenance defect in Stage1:

- Stage1 mechanically proved exact 736/736 episode membership.
- Stage1 then wrote `query_key_equality=True` without mechanically proving all held-out `(episode_id, decision_index)` keys.
- Stage1 also treated TopK8 `best_val_f1` as matched without proving from an independent validation artifact that the threshold was selected on validation only by the same row-best-F1 rule.

Do NOT touch the Mimic scores.

## A. Query-key equality proof

Using existing frozen artifacts only:

1. Recover Mimic held-out query keys from the Stage1 raw held-out score package or from the frozen derived dataset test rows:
   - source `final_episode_id`
   - `decision_index`
2. Recover the exact held-out query keys used by TopK8 main-v2 from its frozen test dataset/result provenance.
3. Compare ordered key sequence and set identity.
4. Require:
   - Mimic keys = 14526
   - TopK8 keys = 14526
   - exact ordered equality = YES for direct row-metric delta
5. If TopK8 frozen artifacts do not retain enough evidence to recover exact query keys, report `NOT_PROVEN`; do not invent or infer equality from counts alone.

## B. TopK8 result artifact binding

Locate the exact existing:
`models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/test_results.json`

Compute SHA256 and verify:

- held-out rows = 14526
- held-out episodes = 736
- success/failure episodes = 658/78
- query AUROC/AUPRC values actually present in this file
- source split binding is the frozen split manifest SHA:
  `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`
  OR prove the equivalent exact episode membership directly from a bound artifact.

## C. TopK8 best-val-F1 threshold provenance

Mechanically locate the validation artifact / training summary / threshold freeze that produced the TopK8 test operating point named `best_val_f1`.

Prove all of the following:

1. threshold value exactly equals the threshold stored in `test_results.json` for `best_val_f1`;
2. threshold was selected using VALIDATION rows only;
3. selection criterion is row-level F1 over validation scores;
4. no held-out test labels/scores entered threshold selection;
5. the TopK8 validation split is the exact same 735-episode validation partition in split manifest SHA `34db754f...`;
6. threshold selection semantics are sufficiently equivalent to Mimic `row_best_f1` for a matched operating-point comparison.

If any item cannot be proved, report matched row-best-F1 as `NOT_PROVEN`. Do not use the name alone as proof.

## D. Existing numbers only

Do NOT run any model forward pass. Do NOT score any split. Do NOT recompute thresholds from raw scores. This is file/provenance inspection only.

If query-key equality is proven, freeze threshold-independent comparison from EXISTING results:

- TopK8 AUROC vs Mimic seed0 AUROC
- TopK8 AUPRC vs Mimic seed0 AUPRC
- deltas Mimic - TopK8

If matched best-F1 provenance is proven, freeze the matched operating-point comparison using EXISTING test results only. Include all available episode metrics, especially FA, Det, Det@10, Det@25, Det@50, never. If TopK8 test_results lacks early timing counts, do not fabricate them.

Mimic seed0 alpha0.10 remains separate and primary for Mimic; do not call it matched to TopK8 unless TopK8 has the same conformal calibration rule.

## Absolute prohibitions

Do NOT:
- rerun Mimic
- rerun TopK8
- train
- recalibrate
- rescore validation
- rescore held-out test
- choose another Mimic seed
- modify any existing held-out freeze
- score OOD
- touch HARD1000
- launch Isaac
- recollect

## Required return block

Return ONLY:

```text
TOPK8_RESULT_BINDING_V2:
  status: PROVEN|NOT_PROVEN
  path: ...
  sha256: ...
  rows/episodes/success/failure: ...
  split_binding: PROVEN|NOT_PROVEN
  auroc: ...
  auprc: ...

QUERY_KEY_PARITY_V2:
  mimic_keys: ...
  topk8_keys: ...
  intersection: ...
  exact_set_equal: YES|NO|NOT_PROVEN
  exact_order_equal: YES|NO|NOT_PROVEN
  mimic_key_sequence_sha256: ...
  topk8_key_sequence_sha256: ...

TOPK8_BEST_VAL_F1_PROVENANCE_V2:
  status: PROVEN|NOT_PROVEN
  validation_artifact_path: ...
  validation_artifact_sha256: ...
  threshold_from_validation: ...
  threshold_in_test_results: ...
  exact_threshold_match: YES|NO
  validation_only_selection: YES|NO|NOT_PROVEN
  criterion: ...
  same_validation_split: YES|NO|NOT_PROVEN
  matched_rule_equivalent_to_mimic_row_best_f1: YES|NO|NOT_PROVEN

FINAL_MATCHED_COMPARISON_V2:
  threshold_independent_status: VALID|NOT_PROVEN
  auroc_topk8/mimic/delta: ...
  auprc_topk8/mimic/delta: ...
  matched_row_best_f1_status: VALID|NOT_PROVEN
  matched_row_best_f1: ...
  mimic_primary_alpha010: ...

NO_MODEL_RERUN:
  YES
NO_SCORING:
  YES
OOD_SCORED:
  NO

COMMIT:
  <sha>
```
