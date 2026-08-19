# Stage 1 amendment — Agy is an operator, not the experiment designer

This file OVERRIDES any interpretive or design language in `AGY_STAGE1_READONLY_AUDIT.md`.

Agy's role in Stage 1 is ONLY to execute filesystem searches, hashes, schema scans, deterministic arithmetic on retained rows, and return raw evidence.

Agy MUST NOT:
- choose the authoritative friend contract when multiple artifacts exist;
- reconcile conflicts between friend artifacts;
- choose which candidate subset to use;
- decide which proxies will be used in the final model;
- design the adapted feature vector;
- choose architecture changes;
- choose normalization, loss, class weighting, sampling, calibration, thresholds, or hyperparameters;
- decide whether reinference should be attempted;
- write training/materialization/model code;
- call any result "the final adaptation";
- infer missing semantics.

For Section 6 of the base audit:
- return EVERY plausible friend-head artifact with path, SHA256, file type, and exact extracted facts;
- do not rank them as authoritative;
- where artifacts disagree, return the conflict literally.

For Section 7 of the base audit:
- do NOT produce a chosen feature matrix.
- instead produce `audit/RAW_FEATURE_SOURCE_TABLE.json` with one row per friend feature/input found in source artifacts and only these factual columns:
  - friend_artifact_path
  - friend_feature_name
  - friend_formula_or_shape_verbatim_from_source
  - matching_round0_field_paths_if_any
  - matching_round0_shapes_if_any
  - exact_saved_boolean
  - deterministically_recomputable_from_final_chunks_boolean
  - candidate0_only_related_fields
  - alternative_internal_dynamics_present_boolean
  - missing_raw_evidence
- do not label any field as an accepted proxy.

For Section 9:
- only return the retained-state inventory. Do not recommend reinference.

The experiment-design decisions will be made after Stage 1 by ChatGPT from the raw artifacts. Agy only supplies machine evidence.

The Stage-1 commit message remains:
`audit(dean): map Round0 evidence to Mimic risk-head contract`
