# Stage 5 — frozen offline OOD150 transfer

Agy is an operator only. The seen experiment is CLOSED. No scientific choice may change.

## Purpose

Evaluate the already-frozen Mimic-style Isaac monitor on the already-existing locked OOD150 trajectories, with ZERO retraining, ZERO recalibration and ZERO simulator/policy inference.

This is a **historical OOD transfer evaluation**, not a pristine never-touched project benchmark: OOD150 has been used previously elsewhere in the project for engineering/controller work. However, it was not used to train, select or calibrate `isaac_mimic_h10_c0dyn_v1`. This distinction must be preserved in all outputs.

## Canonical roots

Workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

OOD150 source:
`$W/outputs/final_locked_h10_ood150_seed20260728`

Seen derived dataset:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1`

Seen model root:
`$W/models/isaac_mimic_h10_c0dyn_v1`

Seen validation freeze root:
`$W/evaluations/isaac_mimic_h10_c0dyn_v1/validation`

OOD derived output:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1_ood150_frozen_transfer`

OOD evaluation output:
`$W/evaluations/isaac_mimic_h10_c0dyn_v1/ood150_frozen_transfer`

## Frozen identity

Primary model is irrevocably:
- seed: 0
- checkpoint SHA256: `4869526f636dc005b4cbcd85c8cfce1f307618fed9f81784f3fd3ee3c3180cf3`
- primary operating point: `conformal_alpha_0.10`
- threshold: `0.736110270023346`

Seen normalization SHA256:
`40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`

Seen dataset manifest v2 SHA256:
`043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`

Seen held-out freeze commit/reference must remain unchanged.

## Absolute prohibitions

- no training;
- no optimizer step;
- no checkpoint selection;
- no threshold selection;
- no threshold recalibration;
- no normalization fitting on OOD;
- no feature redesign;
- no candidate-subset change;
- no use of alternative fake X_d/V_d;
- no Isaac Sim launch;
- no SimVLA inference;
- no recollection;
- no online action selection/controller experiment;
- no OOD400;
- do not touch HARD1000;
- do not modify seen train/val/test artifacts;
- do not use OOD labels/scores to change any preprocessing or model setting.

## Stage 5A hard compatibility gate

Before any OOD scoring, inspect ALL 150 source episodes and their rows.

Require exactly:
- 150 episodes;
- 72 successes;
- 78 failures;
- strict 2 cm label contract;
- source is the canonical `final_locked_h10_ood150_seed20260728` run.

Stream every OOD risk row and report total query count.

Every accepted OOD query must contain the exact raw evidence required by the FROZEN seen materializer:
- `episode_id`
- `decision_index`
- `main_candidate_action_chunk_normalized`
- `main_candidate_action_chunk_env`
- `ace_candidate_chunks_normalized`
- `ace_candidate_chunks_env`
- `main_seed`
- `ace_candidate_seeds`
- `current.proprio`
- `history`
- `simvla_uncertainty_raw.initial_noise`
- `simvla_uncertainty_raw.final_action_normalized`
- `simvla_uncertainty_raw.update_vector_trace`
- source episode failure/success label

Require candidate shapes:
- main [10,7]
- >= 7 alternatives [10,7]

Require the same action semantics as the seen materializer. Verify source/manifests/code hashes; do not infer from shape alone.

### Exact C0 dynamics parity gate

Using the already-frozen production `c0_dynamics.py`, for every OOD row reconstruct C0 dynamics and require:

`initial_noise + sum(update_vector_trace.reshape(10,10,7), axis=0) == final_action_normalized`

with the same frozen max-abs tolerance `<=1e-5`.

If ANY required field/action binding/shape/parity condition fails:
- STOP;
- do not score OOD;
- return compatibility failure with first 20 offending episode/query IDs.

## Reuse production feature code — no reimplementation

If and only if compatibility passes, materialize OOD150 using the exact already-frozen production functions from:

`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/implementation/`

Specifically reuse:
- `action_adapter.py`
- `candidate_features.py`
- `c0_dynamics.py`
- feature order/constants from the frozen seen implementation

Do not copy formulas into a new independent implementation.

Candidate subset remains exactly:
`main + alternatives 1..7`

For every OOD query produce exactly:
- scalar37 [37]
- horizon10x6 [10,6]
- label
- episode_id
- decision_index

Require all finite.

Store raw OOD features and a manifest with hashes. Do NOT fit OOD normalization.

## Frozen normalization application

Load the seen normalization file whose SHA is frozen above.
Apply it exactly as in seen evaluation:
- scalar per-coordinate mean/std from seen TRAIN only;
- horizon per-channel mean/std from seen TRAIN only;
- same std floor semantics already encoded;
- same 8-query episode-local left-zero-padded windows.

No OOD statistic enters normalization.

## Frozen model scoring

After materialization/integrity gate passes, score all five already-frozen seeds as transfer robustness.

For each seed:
- use its exact `best_model.pt` from TRAINING_FREEZE;
- verify checkpoint SHA against TRAINING_FREEZE;
- load that seed's exact `FROZEN_VALIDATION_SELECTION.json`;
- verify validation-freeze/checkpoint/dataset/normalization binding;
- score OOD exactly once;
- apply ONLY thresholds already frozen from seen validation.

Primary result remains seed0 + `conformal_alpha_0.10`, regardless of any OOD result.

DO NOT select a seed or threshold based on OOD.

## Metrics

For each seed, threshold-independent:
- row AUROC
- row AUPRC

For each frozen threshold:
- successful OOD false alarms: count / 72 and percent
- failed OOD detection: count / 78 and percent
- Det@10: count / 78 and percent
- Det@25: count / 78 and percent
- Det@50: count / 78 and percent
- never detected: count / 78
- mean first-alarm fraction among detected failures

Primary output must emphasize exact integer denominators.

For seed0, report all frozen thresholds as supplementary, but primary is alpha=.10.

For seeds0..4 at alpha=.10, report mean/std robustness without changing primary seed.

## Important interpretation metadata

Every result package must contain:
- `evaluation_role = historical_ood_transfer_after_complete_seen_freeze`
- `used_for_mimic_training = false`
- `used_for_mimic_checkpoint_selection = false`
- `used_for_mimic_threshold_calibration = false`
- `previously_used_elsewhere_in_project = true`
- `not_pristine_global_holdout = true`

Do not claim this OOD150 is a pristine untouched benchmark.

## Comparison lock

DO NOT compare against TopK8 OOD150 in this stage unless an already-existing TopK8 OOD150 score artifact is found and exact membership + label/timing conventions can be proven without rerunning or recalibrating TopK8.

If such an artifact exists, only inventory it and record path/hash; do not generate deltas yet. ChatGPT will decide the comparison afterward.

## Git snapshot

Commit only small:
- compatibility audit JSON
- OOD dataset manifest/hashes
- seed result JSON snapshots
- final OOD150 freeze JSON
- summary MD

Do not commit heavy arrays or checkpoints.

Commit exactly:
`experiment(dean): freeze Mimic H10 historical OOD150 transfer`

Push branch.

## RETURN ONLY

COMPATIBILITY_GATE:
status:
source_root:
episodes:
success/failure:
rows:
required_fields_all_rows:
candidate_shapes_valid:
action_binding_match:
c0_recurrence_all_pass:
c0_recurrence_worst_max_abs:

OOD_MATERIALIZATION:
root:
rows:
all_finite:
scalar_shape:
horizon_shape:
seen_normalization_sha256:
ood_normalization_fit:
manifest_sha256:

PRIMARY_SEED0_ALPHA010:
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

ROBUSTNESS_ALPHA010:
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

SEED0_ALL_THRESHOLDS:
fixed_0.5:
conformal_alpha_0.05:
conformal_alpha_0.10:
conformal_alpha_0.15:
empirical_q90:
empirical_q95:
empirical_q99:
row_best_f1:

TOPK8_OOD_ARTIFACT_INVENTORY:
found:
path:
sha256:
exact_membership_proven_without_rerun:

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
