# Stage 6 — Strict Mimic fidelity V2: build, train, freeze validation; NO TEST/OOD

Agy is an operator only. Scientific choices are frozen in `STRICT_MIMIC_FIDELITY_BASELINE_SPEC_V2.md`.

Machine: Dean only.
Workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Branch: `experiment/dean-isaac-mimic-risk-offline-ablation-20260819`

## Absolute rules

- Do not alter V1 artifacts/results.
- Do not optimize V2 based on V1 seen-test or OOD results.
- Do not invent replacement denoising features.
- Do not use candidate0 dynamics in V2 model inputs.
- Do not change candidate subset, action conversion, horizon formulas, temporal formulas, architecture, hyperparameters, split, seeds, calibration family, or primary seed.
- Do not score seen held-out test in this stage.
- Do not score OOD150/OOD400.
- Do not launch Isaac Sim.
- Do not run SimVLA inference.
- Do not recollect anything.
- Do not touch HARD1000.

## 1. V2 dataset construction

Source V1 derived dataset:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1`

Create new root:
`$W/derived_datasets/isaac_mimic_h10_strict_missingdyn_v2`

Use existing V1 frozen arrays only as a mechanically verified source for the exact available features:
- scalar dims 0..8 -> copy unchanged;
- scalar dims 9..33 -> set exactly 0.0 float32;
- scalar dims 34..36 -> copy unchanged;
- horizon10x6 -> copy unchanged;
- labels / episode_index / decision_index / split_index / episode_ids -> copy logically identically.

Do not use V1 candidate0 proxy dynamics in V2 inputs.

## 2. Required parity proof

Across all 75,603 rows require:
- V2 scalar[:,0:9] bitwise/float-exact equal to V1 scalar[:,0:9];
- V2 scalar[:,34:37] exact equal to V1 scalar[:,34:37];
- V2 horizon exact equal to V1 horizon;
- V2 scalar[:,9:34] == 0 for every value;
- labels exact;
- episode_index exact;
- decision_index exact;
- split_index exact;
- episode IDs exact.

If any mismatch: STOP.

Write `audit/STRICT_V2_AVAILABLE_FEATURE_PARITY.json` with all hashes/max diffs.

## 3. Strict V2 normalization

Fit from TRAIN only.

Scalar:
- available dims 0..8 and 34..36: mean/std from train, std floor 1e-6;
- disabled dims 9..33: mean exactly 0, std exactly 1.

Horizon:
- same train-only per-channel method as V1.

Require V2 normalized disabled channels remain exactly zero.

Write normalization and SHA256.

## 4. Dataset manifest

Write V2 manifest containing:
- experiment name `isaac_mimic_h10_strict_missingdyn_v2`;
- parent V1 dataset_manifest_v2 SHA `043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`;
- exact 75,603 / 4000 counts;
- exact split counts 52825/11410/11368 rows and 2800/600/600 episodes;
- failure episodes 64/14/14;
- explicit disabled channel indices 9..33;
- reason `UNAVAILABLE_CROSS_CANDIDATE_DENOISING_INTERNALS_NOT_REPLACED`;
- all heavy array hashes;
- normalization hash;
- spec file SHA;
- code commit/hash.

## 5. Model

Reuse the already-tested `MimicH10RiskMonitor` architecture unchanged.
Do not create a smaller scalar encoder.
Input remains 37D with 25 constant-zero channels.

## 6. Training

New model root:
`$W/models/isaac_mimic_h10_strict_missingdyn_v2/seed_<seed>`

New validation root:
`$W/evaluations/isaac_mimic_h10_strict_missingdyn_v2/validation/seed_<seed>`

Same frozen training protocol:
- seeds 0,1,2,3,4 sequentially;
- 25 epochs each;
- batch 64;
- AdamW lr1e-3 wd1e-4;
- grad clip1;
- dropout.1;
- train-only pos_weight;
- DataLoader explicitly seeded;
- checkpoint every epoch;
- select highest validation row AUPRC, earliest tie.

Seed 0 permanently primary. Never choose another seed as primary.

## 7. Validation calibration

For each seed freeze:
- row AUROC/AUPRC;
- conformal successful-episode-max alpha .05/.10/.15;
- primary alpha .10;
- fixed0.5;
- validation row best-F1;
- empirical q90/q95/q99.

Same corrected order statistic.

## 8. Leakage guard

Do not instantiate/test-score the held-out test split in Stage6.
No OOD load/scoring.

Create a V2 training freeze binding:
- V2 dataset manifest SHA;
- normalization SHA;
- all five checkpoint SHAs;
- all five validation freeze SHAs;
- primary seed0;
- primary alpha0.10;
- `held_out_test_observed_by_v2_training=false`;
- `ood_observed_by_v2_training=false`.

## 9. GPU sharing

Existing foreign GPU process may remain running. Use the already-approved Stage3B headroom policy; do not kill/signal foreign processes. If memory headroom fails, abort only V2 training.

## 10. Git

Commit small code/manifests/audits only. No heavy arrays/checkpoints.

Commit exactly:
`experiment(dean): train strict source-fidelity Mimic baseline v2`

## RETURN ONLY

STRICT_V2_DATASET:
root:
rows:
available_feature_parity:
disabled_channels_zero:
horizon_parity:
normalization_sha256:
dataset_manifest_sha256:

TRAINING:
seed0: <best_epoch | val_auprc | checkpoint_sha | 25/25>
seed1: <...>
seed2: <...>
seed3: <...>
seed4: <...>
all_seeds_complete:

VALIDATION_FREEZE:
seed0: <auroc | auprc | alpha010_threshold | freeze_sha>
seed1: <...>
seed2: <...>
seed3: <...>
seed4: <...>
primary_seed: 0
primary_operating_point: conformal_alpha_0.10
training_freeze_sha256:

HELD_OUT_TEST_SCORED:
NO

OOD_SCORED:
NO

NO_SIM_LAUNCHED:
YES

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
