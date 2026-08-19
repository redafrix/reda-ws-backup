# Stage 5B — REPAIR invalid OOD150 transfer feature space

## Status of previous Stage 5

Commit `e098edbd1e2c93b3e61154c7b8aacba7a1081cb3` OOD150 scientific results are **INVALID** and must not be interpreted or compared.

Fatal reason:

The frozen SEEN materializer used final-candidate ENVIRONMENT action chunks:
- `main_candidate_action_chunk_env`
- `ace_candidate_chunks_env[:7]`
then `isaac_7d_to_mimic_10d(...)` for the 9 disagreement scalars and 10x6 horizon tensor.

The Stage 5 OOD code instead used:
- `main_candidate_action_chunk_normalized`
- `ace_candidate_chunks_normalized`
for these features.

Therefore Stage 5 OOD features were not in the training feature space.

Also `action_binding_match` was hard-coded True rather than proven.

Agy is a machine operator/coder only. Do not reinterpret the experiment.

## Absolute rules

- DO NOT change any seen dataset/model/checkpoint/threshold/result.
- DO NOT retrain.
- DO NOT recalibrate.
- DO NOT change candidate subset.
- DO NOT change normalization.
- DO NOT launch Isaac.
- DO NOT run SimVLA inference.
- DO NOT recollect.
- DO NOT touch HARD1000 or OOD400.
- The previous invalid OOD results must remain preserved for forensic history but must be clearly marked INVALID.

## 1. First write an invalidation marker

Create:

`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/ood150_snapshot/STAGE5_INVALIDATION.json`

It must include:
- invalid_commit = `e098edbd1e2c93b3e61154c7b8aacba7a1081cb3`
- invalid_reason = final-candidate disagreement/horizon features were computed from normalized action chunks instead of env action chunks
- invalid_results_must_not_be_cited = true
- invalid primary reported FA = 72/72
- invalid primary reported Det = 78/78

Do not delete old files.

## 2. Prove exact SEEN feature-space contract from frozen production source

Use the exact production materializer at commit `5a383dd319504f40fdcadc531ca665797a537d76`:

`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/implementation/materialize.py`

The relevant frozen sequence is:

```python
main_env = np.asarray(row["main_candidate_action_chunk_env"], dtype=np.float32)[None, :, :]
ace_env = np.asarray(row["ace_candidate_chunks_env"], dtype=np.float32)[:7, :, :]
c8_env = np.concatenate([main_env, ace_env], axis=0)
c8_10d = isaac_7d_to_mimic_10d(c8_env)
disagree_9, horizon_10x6 = compute_disagreement_and_horizon_features(c8_10d)
```

C0 dynamics continue to use:
- `simvla_uncertainty_raw.initial_noise`
- `simvla_uncertainty_raw.update_vector_trace`
- `simvla_uncertainty_raw.final_action_normalized`

Do not alter these spaces.

## 3. Build a parity-tested shared row featurizer for transfer only

Repair `implementation/stage5_ood_transfer.py` so OOD rows use the exact frozen SEEN feature-space sequence above.

Before touching OOD scores, run a deterministic parity test on at least 1000 SEEN query rows sampled deterministically across train/validation/test episodes.

For each selected seen query:
- recompute scalar37 and horizon10x6 with the repaired Stage5 row featurizer;
- compare to the already-frozen seen arrays in `$W/derived_datasets/isaac_mimic_h10_c0dyn_v1` at the exact corresponding row;
- require exact array equality if operations are byte-identical; otherwise require max_abs <= 1e-7 and explain dtype source;
- record worst scalar max_abs and horizon max_abs.

If parity fails: STOP. Do not materialize or score OOD.

Create:
`ood150_snapshot/SEEN_FEATURIZER_PARITY.json`

## 4. OOD150 compatibility gate must include ENV fields

Across ALL 5,887 OOD rows require:
- `main_candidate_action_chunk_env` shape [10,7]
- `ace_candidate_chunks_env` with >=7 alternatives each [10,7]
- `main_candidate_action_chunk_normalized` shape [10,7]
- `ace_candidate_chunks_normalized` with >=7 alternatives [10,7]
- `simvla_uncertainty_raw.initial_noise`
- `simvla_uncertainty_raw.update_vector_trace`
- `simvla_uncertainty_raw.final_action_normalized`
- contiguous `decision_index`
- episode labels/outcomes exactly 72 success / 78 failure

The disagreement/horizon branch MUST use ENV chunks only.
The C0 dynamics branch MUST use normalized internal diffusion evidence only.

## 5. Real action-binding proof

Do NOT hard-code `action_binding_match=True`.

Mechanically locate the OOD150 run/collector manifest and provenance for:
`$W/outputs/final_locked_h10_ood150_seed20260728`

Compare the actual OOD action/controller semantics/source binding against the frozen SEEN action binding artifact:

`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/source_provenance/ROUND0_ACTION_BINDING.json`

Return exact paths and SHA256 values.

If the historical OOD manifest does not cryptographically record controller source SHA, prove equivalence using the collector/runtime source/config hashes actually recorded and the same controller source path. Do not assert YES without evidence.

Create:
`ood150_snapshot/OOD150_ACTION_BINDING_PROOF.json`

If exact semantic binding cannot be proven: STOP before scoring.

## 6. Rematerialize into NEW corrected root

Do NOT overwrite the invalid Stage5 derived root.

Corrected root:

`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1_ood150_frozen_transfer_v2`

Requirements:
- 150 episodes
- 5887 rows
- scalar [5887,37]
- horizon [5887,10,6]
- all finite
- candidate subset main + alt1..7
- C0 recurrence parity all pass with worst <=1e-5
- no OOD-fitted normalization
- record every heavy array SHA256
- record exact repaired featurizer source SHA256
- record seen normalization SHA `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`

## 7. Score only after all gates pass

Use already-frozen checkpoints exactly:
- seed0 `4869526f636dc005b4cbcd85c8cfce1f307618fed9f81784f3fd3ee3c3180cf3`
- seed1 `9328a8102060bb46414b8f8bd3f71eedd61f4ce93949822dfe2138d4b9a40590`
- seed2 `199a17c2a34c56f4807869f2aa8cc556ba43a39c2bb000719612971ab1ccb693`
- seed3 `f745aa5392918b56135710e7cdb05e2a15c9bc19e9cd03284e5c9885fcfb20a8`
- seed4 `15825ca05155b6ba1248b5542454ae33bd210d77cf86522ceb28e28567d90cb7`

Use each seed's existing `FROZEN_VALIDATION_SELECTION.json` thresholds unchanged.

Primary remains:
- seed0
- `conformal_alpha_0.10`
- threshold `0.736110270023346`

Do not choose from OOD results.

## 8. TopK8 OOD comparison

Only after corrected Mimic OOD results are frozen:
- inventory the already-existing TopK8 OOD150 result artifact;
- prove exact 150-episode membership using source episode IDs / locked manifest;
- do not rerun TopK8;
- compare threshold-independent AUROC/AUPRC directly if row membership/labels match;
- for thresholded results, label calibration rules explicitly; do not claim matched calibration unless the same calibration rule is actually used.

## 9. Outputs

Commit small files only:
- repaired `implementation/stage5_ood_transfer.py`
- tests
- `ood150_snapshot/STAGE5_INVALIDATION.json`
- `ood150_snapshot/SEEN_FEATURIZER_PARITY.json`
- `ood150_snapshot/OOD150_ACTION_BINDING_PROOF.json`
- `ood150_snapshot/OOD150_COMPATIBILITY_V2.json`
- `ood150_snapshot/OOD150_DATASET_MANIFEST_V2.json`
- five corrected result JSON snapshots
- `ood150_snapshot/OOD150_TRANSFER_FREEZE_V2.json`
- optional corrected TopK8 comparison JSON only if exact membership proven

Commit exactly:

`fix(dean): repair OOD150 transfer to exact seen feature space`

## RETURN ONLY

PREVIOUS_STAGE5:
status: INVALID
reason:

SEEN_FEATURIZER_PARITY:
rows_checked:
scalar_worst_max_abs:
horizon_worst_max_abs:
passed:

ACTION_BINDING:
status:
ood_manifest_path:
ood_manifest_sha256:
seen_binding_sha256:
evidence:

COMPATIBILITY_V2:
status:
episodes:
rows:
success/failure:
env_fields_all_rows:
normalized_internal_fields_all_rows:
candidate_shapes_valid:
c0_recurrence_all_pass:
c0_recurrence_worst_max_abs:

OOD_MATERIALIZATION_V2:
root:
rows:
scalar_shape:
horizon_shape:
all_finite:
seen_normalization_sha256:
ood_normalization_fit:
manifest_sha256:

PRIMARY_SEED0_ALPHA010_V2:
threshold:
row_auroc:
row_auprc:
success_false_alarms:
failure_detection:
det10:
det25:
det50:
never_detected:
mean_first_alarm_fraction:

ROBUSTNESS_ALPHA010_V2:
seed0:
seed1:
seed2:
seed3:
seed4:
mean_std_auroc:
mean_std_auprc:
mean_std_fa_percent:
mean_std_failure_detection_percent:
mean_std_det25_percent:
mean_std_det50_percent:

TOPK8_OOD150_COMPARISON:
membership_exact_match:
threshold_independent_comparison:
thresholded_comparison_note:

NO_TRAINING:
YES

NO_RECALIBRATION:
YES

NO_SIM_LAUNCHED:
YES

HARD1000_TOUCHED:
NO

OOD400_TOUCHED:
NO

COMMIT:
<sha or NONE>
