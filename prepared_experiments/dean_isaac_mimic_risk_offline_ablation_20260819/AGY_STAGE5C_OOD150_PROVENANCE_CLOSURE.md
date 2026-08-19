# Stage 5C — OOD150 provenance closure only; NO model/data rerun

Agy is an operator only. The repaired Mimic OOD150 V2 result from commit `d2adf5210e84b8c4d7b76fd9961bb5304ff8a8fb` is frozen and MUST NOT be recomputed.

Purpose: prove or reject exact episode membership equality between:

1. Mimic OOD150 V2 source:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728`

2. Historical TopK8 OOD150 evaluation:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/evaluations/locked_h10_ood150_topk8_v1/results.json`

The Stage5B comparison JSON hard-coded `membership_exact_match=true`; that boolean is NOT accepted as proof.

## Absolute prohibitions

- no training
- no model scoring
- no threshold recalibration
- no feature materialization
- no Isaac launch
- no SimVLA inference
- no collection/recollection
- do not modify Mimic seen/OOD arrays, checkpoints, thresholds or results
- do not rerun TopK8
- do not touch HARD1000
- do not touch OOD400

## A. Locate the exact historical TopK8 OOD dataset manifest

Read historical TopK8 results and obtain:
`ood_dataset_manifest_sha256 = e5b6cf816d9c10d346f62516d9770258512686b1aefa80c14b432fab5c3bc86a`

Search Dean under the canonical workspace for a file with EXACT SHA256 above. Do not infer by filename.

Return:
- absolute path
- SHA256
- schema/version
- source OOD root/path fields
- episode-ID source or membership fields
- row count
- episode count
- success/failure counts if present

If the manifest cannot be found, search for any historical dataset files referenced by the TopK8 evaluator/model artifacts that preserve episode IDs, and return their hashes/paths. Do not claim exact membership without an explicit ID mapping.

## B. Build exact episode-ID sets mechanically

Mimic set:
- read the 150 IDs from repaired V2 `episode_ids.json`, OR directly from `final_locked_h10_ood150_seed20260728/episode_summaries.jsonl`;
- SHA256 the ordered list and sorted-set canonical JSON.

TopK8 set:
- derive the 150 ORIGINAL SOURCE EPISODE IDs from the historical TopK8 OOD dataset manifest/mapping;
- do not compare local integer `episode_index` values to string IDs.

Compute:
- unique counts
- intersection
- mimic_only IDs
- topk8_only IDs
- exact_set_equal
- exact_order_equal if meaningful

Write first 20 mismatches if any.

## C. Row/label parity

Without model inference, verify:
- Mimic rows = 5887
- TopK8 rows = 5887
- Mimic success/failure episodes = 72/78
- TopK8 success/failure episodes = 72/78

If query-level source keys are available for TopK8, additionally prove exact `(episode_id, decision_index)` set equality and report count/intersection. If unavailable, state `QUERY_KEY_EQUALITY=NOT_PROVABLE_FROM_RETAINED_TOPK8_ARTIFACT` rather than inventing it.

## D. Matched existing-result comparison ONLY if exact episode membership passes

Use already-frozen historical numbers only.

Threshold-independent:
- TopK8 AUROC 0.9165517741946905
- TopK8 AUPRC 0.9800307261831581
- Mimic seed0 AUROC 0.9284076505286116
- Mimic seed0 AUPRC 0.9824945593128274

Matched validation-row-best-F1 operating points:

TopK8 `best_val_f1`:
- threshold 0.7990124225616455
- success FA 1/72
- failure detected 78/78
- Det@10 5/78
- Det@25 31/78
- Det@50 78/78

Mimic `row_best_f1`:
- threshold 0.9380214810371399
- success FA 3/72
- failure detected 78/78
- Det@10 13/78
- Det@25 35/78
- Det@50 78/78

Mechanically verify these numbers against the existing JSON files before writing the comparison.

Also record primary Mimic alpha=.10 separately; do NOT pretend it is the same calibration rule as TopK8 best-F1.

## E. Outputs

Create only small audit files under:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/ood150_snapshot/`

- `TOPK8_OOD150_MEMBERSHIP_PROOF_V2.json`
- `TOPK8_OOD150_MATCHED_COMPARISON_V2.json` only if exact_set_equal=true
- `STAGE5C_PROVENANCE_CLOSURE.md`

Do not modify existing Stage5B result files.

Commit exactly:
`audit(dean): prove exact matched OOD150 membership without rerun`

Push branch.

## RETURN ONLY

TOPK8_OOD_DATASET_MANIFEST:
path:
sha256:
source_root:

MEMBERSHIP:
mimic_unique:
topk8_unique:
intersection:
mimic_only:
topk8_only:
exact_set_equal:
exact_order_equal:
mimic_sorted_set_sha256:
topk8_sorted_set_sha256:

ROW_LABEL_PARITY:
mimic_rows:
topk8_rows:
mimic_success/failure:
topk8_success/failure:
query_key_equality:

MATCHED_COMPARISON:
status: VALID/NOT_VALID
auroc_topk8/mimic/delta:
auprc_topk8/mimic/delta:
row_best_f1_FA_topk8/mimic:
row_best_f1_Det_topk8/mimic:
row_best_f1_Det10_topk8/mimic:
row_best_f1_Det25_topk8/mimic:
row_best_f1_Det50_topk8/mimic:

NO_MODEL_RERUN:
YES

NO_TRAINING:
YES

OOD400_TOUCHED:
NO

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
