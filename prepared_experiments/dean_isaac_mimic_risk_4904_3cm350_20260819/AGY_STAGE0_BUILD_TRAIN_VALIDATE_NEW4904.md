# AGY Stage 0 — Mechanical Build / Train / Validate on NEW Seen4904

Agy is mechanical only. Do not make scientific choices.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Git branch:
`experiment/dean-isaac-mimic-risk-4904-3cm350-20260819`

Read first:
`prepared_experiments/dean_isaac_mimic_risk_4904_3cm350_20260819/NEW4904_MIMIC_RETRAIN_SPEC.md`

## A. Resolve and freeze the NEW source dataset

1. Locate exactly one directory under the canonical workspace whose dataset identity is `isaac_seen4904_h10_3cm350_exact_v1`.
2. Locate the frozen source/split artifacts used by model identity `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`.
3. Do not guess locations. Search mechanically by exact name if necessary.
4. Compute SHA256 for source dataset manifest and split assignment artifact.
5. Prove:
   - 4904 unique episodes
   - 4387 success
   - 517 failure
   - 96813 query rows
   - H10
   - exact label protocol first `<=0.030m` within 350 control ticks at 30Hz, no dwell
   - exact split membership from the main TopK8 source
6. Report exact train/validation/test episode, success/failure episode, row, positive-row and negative-row counts.
7. If any expected census/protocol/split proof fails, STOP before materialization.

## B. Full schema census

Stream every one of the 96813 query rows. Record presence/shape counts for:

- episode ID
- decision/query index
- parent risk label
- main ENV H10 action chunk
- alternative ENV H10 chunks
- main normalized H10 action chunk
- alternative normalized H10 chunks
- any raw/internal denoising object
- the exact five handoff trace names:
  - sample_pairwise_mse_mean
  - sample_variance_max
  - sample_variance_mean
  - sample_velocity_mse_mean
  - vector_field_l2_mean
- any per-candidate denoising trajectories/traces
- history/proprio fields

Do not infer absent fields.

Determine `dynamics_mode` mechanically:

- `EXACT` only if all 96813 accepted rows directly contain all five genuine source-compatible cross-candidate trace series and their semantics/order are proven by collector/source code.
- otherwise `STRICT_MISSING`.

If `STRICT_MISSING`, dims 9..33 MUST be zeros. Do not use any C0 proxy.

## C. Action binding

Prove the NEW dataset action/controller binding from its own run/source manifests.

If byte/semantic binding is identical to the previously verified Isaac 7D action semantics, reuse the existing source-backed `isaac_7d_to_mimic_10d` adapter.

If it differs, STOP and report. Do not invent a conversion.

## D. Materialize fresh Mimic dataset

Create:
`$W/derived_datasets/isaac_mimic_h10_strict_3cm350_seen4904_v3`

Do not copy old derived arrays.

For every NEW4904 row, freshly compute:

- scalar dims 0..8: exact 8-candidate final-ENV disagreement features from main + alternatives1..7
- scalar dims 9..33:
  - EXACT mode: exact summaries of the five direct genuine handoff trace series
  - STRICT_MISSING mode: exactly 0.0
- scalar dims 34..36: exact temporal-change features from the immediately preceding query of the same episode
- horizon `[10,6]`: exact 8-candidate final-ENV H10 features
- parent failure label from NEW4904 exact 3cm350 protocol
- episode index
- decision index
- split index from frozen NEW4904 TopK8 split

Required scalar shape `(96813,37)`.
Required horizon shape `(96813,10,6)`.
All finite.

Fit normalization from NEW4904 TRAIN rows only.
In STRICT_MISSING mode, disabled dims normalization must be mean 0/std 1 exactly.

Write dataset manifest containing:

- source manifest SHA
- source split SHA
- source model/split identity
- all split counts
- candidate subset
- action binding proof SHA
- dynamics mode + evidence
- heavy array SHA256s
- normalization SHA256
- explicit statement old Round0 data not used

## E. Implementation fidelity

Reuse the already frozen Mimic architecture/modules only where semantics are unchanged.

Architecture and hyperparameters are exactly those in NEW4904_MIMIC_RETRAIN_SPEC.md.

Do not add features, masks, task IDs, timestep/progress, episode length, target identity, scene IDs or any outcome-derived input.

Add tests proving at minimum:

1. source census exact
2. split membership exact
3. 8-candidate subset exact and deterministic
4. scalar shape 37
5. horizon shape 10x6
6. dynamics mode rule obeyed
7. if STRICT_MISSING, dims9..33 exact zero before/after normalization
8. no old Round0 array path imported
9. train-only normalization
10. 8-query left-zero-padded window
11. held-out split inaccessible to training/calibration path

## F. GPU safety

Do not kill, pause, signal, renice or modify any foreign process.

If another CUDA job is active:

1. sample free VRAM/utilization for 60 seconds;
2. run one throwaway exact batch-64 forward/backward/AdamW step for this NEW model to measure peak reserved VRAM;
3. training may proceed in parallel only if:

`min_free_vram_60s_mib >= probe_peak_reserved_mib + 6144`

4. during training, sample free VRAM every 30 seconds;
5. if free VRAM drops below 3072 MiB, stop only this Mimic training process and report `HEADROOM_ABORTED`.

Do not touch foreign processes.

## G. Train five fresh seeds

Train seeds sequentially: 0,1,2,3,4.

For every seed:

- start from fresh random initialization
- 25/25 epochs
- batch64
- AdamW lr1e-3 wd1e-4
- grad clip1.0
- dropout0.1
- weighted BCE using NEW4904 train-row class counts
- deterministic seeded DataLoader
- checkpoint every epoch
- select max validation row AUPRC, earliest tie

Do not resume from old 4000-dataset Mimic checkpoints.
Do not initialize from old Mimic weights.

## H. Validation freeze

For every selected seed checkpoint:

- score validation only
- row AUROC/AUPRC
- compute successful-episode maxima
- freeze conformal alpha 0.05/0.10/0.15 using corrected order statistic
- alpha0.10 primary
- supplemental fixed0.5 / row-best-F1 / q90/q95/q99
- report validation episode alarm/detection counts

Freeze:

- every checkpoint SHA
- every validation-freeze SHA
- all 25 epoch logs per seed
- dataset manifest SHA
- normalization SHA
- source dataset/split SHA
- primary seed0 + alpha0.10 before held-out test

## I. ABSOLUTE STOP after validation

DO NOT score:

- NEW4904 held-out test
- OOD150
- OOD400
- HARD1000

DO NOT launch Isaac Sim.
DO NOT run SimVLA inference.
DO NOT recollect.

Commit only code/small metadata/audits; do not commit heavy arrays or model checkpoints.

## Required return block

Return ONLY:

```text
NEW4904_SOURCE_GATE:
  status: PASSED|FAILED
  dataset_root: ...
  source_manifest_sha256: ...
  split_artifact_path: ...
  split_artifact_sha256: ...
  protocol: ...
  episodes: ...
  success/failure: ...
  rows: ...
  train: <episodes> eps | <success>/<failure> | <rows> rows | <pos>/<neg> rows
  validation: <episodes> eps | <success>/<failure> | <rows> rows | <pos>/<neg> rows
  heldout_test: <episodes> eps | <success>/<failure> | <rows> rows | <pos>/<neg> rows

SCHEMA_AUDIT:
  all_96813_rows_streamed: YES|NO
  main_env_shape: ...
  alt_env_shape: ...
  candidate_subset: ...
  genuine_five_cross_candidate_traces_all_rows: YES|NO
  dynamics_mode: EXACT|STRICT_MISSING
  action_binding: PROVEN|FAILED

DERIVED_MIMIC_DATASET:
  root: ...
  rows: ...
  scalar_shape: ...
  horizon_shape: ...
  disabled_channels_zero_if_applicable: YES|N/A
  all_finite: YES|NO
  normalization_sha256: ...
  dataset_manifest_sha256: ...
  old_round0_arrays_used: NO

TRAINING:
  seed0: <best_epoch> | <best_val_auprc> | <checkpoint_sha256> | 25/25
  seed1: ...
  seed2: ...
  seed3: ...
  seed4: ...
  all_seeds_complete: YES|NO
  training_freeze_sha256: ...

VALIDATION_FREEZE:
  seed0: <val_auroc> | <val_auprc> | <alpha010_threshold> | <freeze_sha256>
  seed1: ...
  seed2: ...
  seed3: ...
  seed4: ...
  primary_seed: 0
  primary_operating_point: conformal_alpha_0.10
  all_seed_validation_freeze_sha256: ...

GPU_GUARD:
  foreign_processes_signaled: NO
  headroom_status: PASSED|NOT_NEEDED|HEADROOM_ABORTED
  minimum_free_vram_seen_mib: ...

HELD_OUT_TEST_SCORED:
  NO
OOD_SCORED:
  NO
ISAAC_SIM_LAUNCHED:
  NO
HARD1000_TOUCHED:
  NO

COMMIT:
  <sha>
```