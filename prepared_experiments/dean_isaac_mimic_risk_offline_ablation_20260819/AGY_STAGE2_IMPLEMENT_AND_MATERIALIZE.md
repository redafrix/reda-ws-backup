# Stage 2 — implement EXACT frozen adaptation and materialize; NO TRAINING

Agy is an operator/coder. The scientific design is frozen in `FINAL_ADAPTATION_SPEC_V1.md` and must not be changed.

Machine: Dean only.
Workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Branch: `experiment/dean-isaac-mimic-risk-offline-ablation-20260819`

## Absolute rules

- Read `FINAL_ADAPTATION_SPEC_V1.md` first and implement it literally.
- Do not redesign features.
- Do not replace candidate subset.
- Do not change architecture/hyperparameters/calibration.
- Do not train yet.
- Do not score validation/test yet except deterministic unit-test fixtures.
- Do not launch Isaac Sim.
- Do not run SimVLA inference.
- Do not touch HARD1000, OOD150 or OOD400.
- Do not modify original Round0 or the existing frozen TopK8 dataset.
- No `pass`, TODO, FIXME, ellipsis placeholders or fake tests.

## 1. Action adapter provenance gate

Before writing the materializer, mechanically resolve BOTH sides of the 7D->10D conversion.

### Isaac side
Trace the exact 7D action semantics used by accepted Round0 all the way from SimVLA output to the Isaac controller/environment.

Inspect canonical sources under `$W`, especially:
- `src/risk_collection/runtime_policy.py`
- `src/risk_collection/adapter.py`
- collector/runtime scripts
- the Isaac task/controller config actually bound by Round0 manifest

Resolve and record:
- dimensions 0:3 meaning and units
- dimensions 3:6 representation, axis/order and units
- dimension 6 meaning/range
- whether `main_candidate_action_chunk_env` is before or after any scaling/clipping

### Mimic side
Inspect exact already-located source:
`/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/mimic_video/geometry.py`

Resolve:
- exact 10D layout
- exact 6D rotation representation
- exact row/column serialization
- exact 10D->7D function
- any 7D->10D inverse already present

Create:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/source_provenance/ACTION_ADAPTER_PROVENANCE.json`

Include absolute paths + SHA256 + functions + exact formulas.

Implement round-trip tests over identity + >=1000 deterministic random small rotation commands in the actual Round0 action range.

Require max round-trip error <= source-appropriate tolerance documented in the provenance JSON.

If exact mapping cannot be proven: STOP. Do not materialize.

## 2. Production code layout

Create small source files under:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/implementation/`

Required:
- `action_adapter.py`
- `candidate_features.py`
- `c0_dynamics.py`
- `materialize.py`
- `dataset.py`
- `model.py`
- `train.py`
- `evaluate.py`
- `calibration.py`
- `metrics.py`
- `constants.py`

Tests under:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/tests/`

No simulator imports should be needed for materialization/training.

## 3. Materializer implementation

Implement exactly `FINAL_ADAPTATION_SPEC_V1.md`.

Source raw rows: all 75,603 accepted Round0 rows.
Split assignment: reuse frozen split assignments byte-for-byte/logically exactly.
Candidate subset: main + first seven stored alternatives.

For every query:
- exact 8-candidate env tensor -> source-backed 10D monitor conversion
- scalar 9 disagreement
- horizon 10x6
- exact candidate0 X_d/V_d reconstruction
- exact five C0 proxy traces
- 25 trace summaries
- three temporal-change values
- scalar37
- source label

### Mandatory candidate0 recurrence parity

For all 75,603 rows:
rebuild `X10_from_updates` and compare to stored `final_action_normalized`.

Hard default tolerance max_abs <= 1e-5.
If ANY row violates it, STOP materialization and return the worst rows; do not relax tolerance yourself.

### Finite checks

No NaN/Inf in scalar37 or horizon10x6.

### Shape checks

Every row:
- scalar37 shape [37]
- horizon shape [10,6]
- label scalar {0,1}

## 4. Train-only normalization

After raw features are materialized:
- fit scalar mean/std from TRAIN rows only, 37D
- fit horizon per-channel mean/std from TRAIN rows/all H positions only, 6D
- floor std at 1e-6

Store raw and normalization separately; do not overwrite raw arrays.

Write normalization SHA256.

## 5. Derived dataset root

Create heavy derived data only at:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1`

Suggested portable structure:
- `raw/scalar37.npy`
- `raw/horizon10x6.npy`
- `labels.npy`
- `episode_index.npy`
- `decision_index.npy`
- `split_index.npy` or split row index files
- `episode_ids.json`
- `normalization.json`
- `dataset_manifest.json`
- `source_hashes.json`
- `audit/c0_reconstruction_parity.json`
- `audit/feature_ranges.json`

Do not put heavy arrays in Git.

Manifest MUST record:
- source Round0 root
- source dataset/split manifest SHA256
- accepted row count 75603
- candidate subset declaration
- action adapter provenance SHA
- feature order all 37 names
- horizon channel order all 6 names
- C0 proxy trace definitions
- train/val/test episode and row counts
- train row label counts and computed future `pos_weight`
- source code Git commit/SHAs

## 6. Model/trainer/evaluator code

Implement the exact architecture and fixed training constants in `FINAL_ADAPTATION_SPEC_V1.md`, but DO NOT RUN TRAINING in Stage 2.

`train.py` must support seed 0..4, fixed 25 epochs, checkpoint each epoch, select highest validation row AUPRC with earliest-epoch tie break.

`evaluate.py` must be able to compute row AUROC/AUPRC and episode metrics but MUST refuse held-out test evaluation unless a `FROZEN_VALIDATION_SELECTION.json` file exists. This is a leakage guard.

`calibration.py` must implement corrected episode-max conformal threshold exactly:
`k=min(n,ceil((n+1)*(1-alpha)))` using 1-indexed order statistic semantics.

Required alpha list fixed: [0.05, 0.10, 0.15].

## 7. Mandatory tests

Tests must exercise production functions.

At minimum:
1. no-stub scan over implementation directory
2. action adapter source parity / round-trip >=1000 cases
3. candidate subset exact ordering main + alt1..7
4. pairwise MSE uses exactly 28 unordered off-diagonal pairs
5. endpoint cumulative translation test with hand-computable fixture
6. scalar9 exact fixture
7. horizon10x6 exact fixture
8. C0 X_d recurrence fixture
9. C0 V_d = U/dt fixture with dt=-0.1
10. C0 five proxy traces fixture
11. 25-summary exact order fixture
12. scalar37 exact order/shape fixture
13. temporal q=0 zeros and q>0 absolute deltas
14. 8-query left-zero-padded window construction
15. model shape test: batch -> one logit/window
16. normalization fits train only; test mutation cannot change normalization hash
17. split identity/count test exactly 2800/600/600 episodes and 52825/11410/11368 rows
18. no forbidden metadata input test (task/timestep/reward/scene/outcome IDs absent from model tensors)
19. calibration order-statistic tests for alpha .05/.10/.15
20. evaluator test-lock refuses held-out test before freeze marker

## 8. Full materialization

Only after all unit/static tests pass:
run the complete 75,603-row materializer on Dean.

This is offline CPU/GPU tensor processing only. No simulator.

After materialization run a full integrity audit:
- 75603 rows exactly
- no missing source rows
- no duplicate (episode_id, decision_index)
- split counts exact
- all finite
- recurrence parity all pass
- feature order hashes frozen

Do NOT train.

## 9. Git

Commit only small code/tests/manifests/audit summaries; never heavy arrays.

Commit message exactly:
`feat(dean): implement and materialize frozen Isaac Mimic H10 adaptation`

Push branch.

## RETURN ONLY

ACTION_ADAPTER:
isaac_7d_semantics:
isaac_source:
mimic_10d_semantics:
mimic_source:
roundtrip_tests:
max_error:
provenance_complete:

IMPLEMENTATION:
files:
no_stub_scan:
unit_tests_passed:
unit_tests_total:

MATERIALIZATION:
root:
rows:
train_rows:
val_rows:
test_rows:
train_positive_rows:
train_negative_rows:
pos_weight:
all_finite:
recurrence_parity_passed:
recurrence_worst_max_abs:
normalization_sha256:
dataset_manifest_sha256:

TRAINING_RUN:
NO

TEST_EVAL_RUN:
NO

ISAAC_SIM_LAUNCHED:
NO

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
