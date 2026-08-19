# Stage 3 — train all five frozen seeds and freeze VALIDATION only

Scientific design remains `FINAL_ADAPTATION_SPEC_V1.md`. Do not change it.

Machine: Dean only.
Workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Branch: `experiment/dean-isaac-mimic-risk-offline-ablation-20260819`
Required pre-stage code/data commit: `50d2434039ff1311de3487565a6f7a9fa19104f6`
Required dataset freeze SHA256: `043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`
Required normalization SHA256: `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`

## ABSOLUTE RULES

- This stage may TRAIN on TRAIN and SCORE/CALIBRATE on VALIDATION.
- This stage MUST NOT load, score, summarize, inspect model predictions on, or evaluate the held-out TEST split.
- No OOD150/OOD400.
- No Isaac Sim.
- No SimVLA inference.
- No new data collection.
- Do not touch HARD1000 files/processes.
- Do not alter the frozen 75,603-row feature arrays.
- Do not alter split assignments, labels, normalization, candidate subset, feature definitions, model architecture, history length, loss, optimizer or hyperparameters.
- Do not select a primary seed by validation performance. Seed 0 is predeclared primary; seeds 1..4 are robustness repeats.

## 0. GPU / PROCESS PREFLIGHT

Before any training:

- inspect `nvidia-smi` and active GPU processes;
- inspect whether HARD1000 or another Isaac/SimVLA production process is currently using Dean's GPU;
- do NOT kill, pause, renice or modify any existing process.

If a HARD1000/Isaac/SimVLA production GPU job is active, STOP Stage 3 before training and return `GPU_PREFLIGHT: BUSY_ABORTED` with PID/process details.

If GPU is free, continue and return `GPU_PREFLIGHT: FREE`.

Training seeds must run SEQUENTIALLY, never concurrently.

## 1. EXACT final guard-message repair BEFORE training

In:
`implementation/evaluate.py`

There are three mismatch error-message f-strings whose dictionary references are missing quotes. Change ONLY these display expressions:

- `val_freeze[model_checkpoint_sha256]` -> `val_freeze['model_checkpoint_sha256']`
- `val_freeze[normalization_sha256]` -> `val_freeze['normalization_sha256']`
- `val_freeze[dataset_manifest_v2_sha256]` -> `val_freeze['dataset_manifest_v2_sha256']`

Do not change guard conditions or evaluation logic.

Add tests that deliberately pass each wrong asset/hash condition and verify a `RuntimeError` is raised rather than `NameError`.

Run the complete test suite. Require all tests pass before training.

Commit this tiny repair before training with message exactly:
`fix(dean): make held-out hash guards fail cleanly`

Push branch. Record commit SHA as `TRAINING_CODE_COMMIT`.

## 2. PRETRAIN FREEZE VERIFICATION

Before training, recompute SHA256 of:

- `$W/derived_datasets/isaac_mimic_h10_c0dyn_v1/dataset_manifest_v2.json`
- `$W/derived_datasets/isaac_mimic_h10_c0dyn_v1/normalization.json`
- all six heavy arrays listed by dataset_manifest_v2;
- `FINAL_ADAPTATION_SPEC_V1.md`;
- every implementation `.py` file after the tiny guard repair.

Hard require:
- dataset manifest v2 SHA = `043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`
- normalization SHA = `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`
- heavy arrays match the hashes recorded in manifest v2.

The evaluate.py repair is expected to change only evaluate.py's implementation hash; no data hash may change.

If any dataset/array/normalization hash differs: STOP. Do not train.

## 3. TRAINING — fixed five seeds

Derived dataset:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1`

Model root:
`$W/models/isaac_mimic_h10_c0dyn_v1`

Train exactly these seeds, sequentially:
`0 1 2 3 4`

Use production `implementation/train.py` with exactly the frozen constants:
- batch size 64
- 25 epochs
- AdamW
- lr 1e-3
- weight decay 1e-4
- gradient clip 1.0
- BCEWithLogitsLoss
- train-row pos_weight = 48985 / 3840 = 12.756510416666666
- train DataLoader deterministic generator seeded by the current run seed
- validation used only for epoch selection
- best epoch = highest validation row AUPRC
- exact tie -> earliest epoch because update occurs only on strictly greater AUPRC

Do not stop early. Every seed must complete all 25 epochs even if best epoch occurs earlier.

After EACH seed, mechanically verify:
- exactly 25 epoch checkpoints exist;
- `training_summary.json` exists;
- epoch log length = 25;
- summary seed matches directory seed;
- train pos/neg = 3840/48985;
- pos_weight exact within float tolerance;
- best_epoch in 1..25;
- best_val_auprc finite;
- `best_model.pt` exists;
- `best_model.pt` stored epoch equals summary best_epoch;
- checkpoint seed equals summary seed;
- checkpoint val_auprc equals summary best_val_auprc within 1e-12.

Compute SHA256 for each `best_model.pt` and `training_summary.json`.

If a seed fails structurally, STOP before validation calibration for that seed. Do not silently restart with changed settings.

## 4. FREEZE TRAINING IDENTITY BEFORE CALIBRATION

Create on Dean:
`$W/models/isaac_mimic_h10_c0dyn_v1/TRAINING_FREEZE.json`

It must include:
- experiment name;
- TRAINING_CODE_COMMIT;
- dataset_manifest_v2 SHA;
- normalization SHA;
- spec SHA;
- implementation file hashes;
- CUDA/Torch/device info;
- for seeds 0..4: best epoch, best val AUPRC, best_model SHA, training_summary SHA, all 25 epoch checkpoint filenames/hashes;
- statement `primary_seed=0_predeclared_before_test`;
- statement `no_test_scores_observed=true`.

SHA256 this freeze.

## 5. VALIDATION SCORING + CALIBRATION — all five seeds

Validation output root:
`$W/evaluations/isaac_mimic_h10_c0dyn_v1/validation`

For EACH seed 0..4, use ONLY that seed's frozen `best_model.pt` and run production validation scoring/calibration.

Pass:
- derived dataset root;
- seed's `best_model.pt`;
- seed's `training_summary.json`;
- exact `FINAL_ADAPTATION_SPEC_V1.md` path;
- output `validation/seed_<seed>`;
- Dean CUDA device.

This must create one:
`validation/seed_<seed>/FROZEN_VALIDATION_SELECTION.json`
per seed.

For each validation freeze mechanically verify:
- checkpoint SHA equals TRAINING_FREEZE seed checkpoint SHA;
- dataset manifest v2 SHA correct;
- normalization SHA correct;
- spec SHA correct;
- seed correct;
- selected epoch equals training summary best epoch;
- validation rows = 11410;
- validation episodes = 600;
- validation failure episodes = 14;
- successful validation episode maxima count = 586;
- row AUROC finite;
- row AUPRC finite;
- thresholds include exactly at least:
  - fixed_0.5
  - row_best_f1
  - conformal_alpha_0.05
  - conformal_alpha_0.10
  - conformal_alpha_0.15
  - empirical_q90
  - empirical_q95
  - empirical_q99
- primary threshold is `conformal_alpha_0.10` by predeclared protocol, regardless of which threshold looks best on validation.

Compute SHA256 for each validation freeze.

## 6. VALIDATION-ONLY robustness summary

Create:
`$W/evaluations/isaac_mimic_h10_c0dyn_v1/validation/VALIDATION_FREEZE_ALL_SEEDS.json`

Include for all five seeds:
- best epoch;
- best validation row AUROC/AUPRC;
- every calibrated threshold;
- validation episode metrics at each threshold;
- checkpoint/freeze hashes.

Also include aggregate mean/std across seeds for validation AUROC/AUPRC, clearly labeled validation-only.

DO NOT rank seeds and DO NOT alter primary seed 0.

Add:
- `primary_seed: 0`
- `primary_operating_point: conformal_alpha_0.10`
- `held_out_test_scored: false`
- `ood_scored: false`

SHA256 this all-seed validation freeze.

## 7. PROHIBITED TEST ACCESS CHECK

Before finishing Stage 3:

- verify no `HELD_OUT_TEST_RESULTS.json` exists under this experiment's evaluation root;
- verify no test score arrays/results were produced by Stage 3;
- do NOT delete a historical file if one unexpectedly exists; instead STOP and report contamination.

## 8. Git snapshot — SMALL METADATA ONLY

Copy only small metadata summaries into:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/training_snapshot/`

Include:
- `TRAINING_FREEZE.json`
- five `training_summary_seed_<seed>.json`
- five `FROZEN_VALIDATION_SELECTION_seed_<seed>.json`
- `VALIDATION_FREEZE_ALL_SEEDS.json`
- `STAGE3_SUMMARY.md`

Do NOT commit model checkpoints, `.npy` score arrays, or heavy data.

Commit message exactly:
`train(dean): freeze five-seed Mimic H10 training and validation`

Push branch.

## RETURN ONLY

GPU_PREFLIGHT:
status:
active_gpu_processes_before_training:

PRETRAIN_FREEZE:
dataset_manifest_v2_sha256:
normalization_sha256:
heavy_arrays_match:
training_code_commit:
tests_passed:
tests_total:

TRAINING:
seed0: best_epoch | best_val_auprc | checkpoint_sha256
seed1: best_epoch | best_val_auprc | checkpoint_sha256
seed2: best_epoch | best_val_auprc | checkpoint_sha256
seed3: best_epoch | best_val_auprc | checkpoint_sha256
seed4: best_epoch | best_val_auprc | checkpoint_sha256
training_freeze_sha256:
all_seeds_25_epochs_complete:

VALIDATION_FREEZE:
seed0: val_auroc | val_auprc | alpha010_threshold | freeze_sha256
seed1: val_auroc | val_auprc | alpha010_threshold | freeze_sha256
seed2: val_auroc | val_auprc | alpha010_threshold | freeze_sha256
seed3: val_auroc | val_auprc | alpha010_threshold | freeze_sha256
seed4: val_auroc | val_auprc | alpha010_threshold | freeze_sha256
all_seed_validation_freeze_sha256:
primary_seed:
primary_operating_point:

HELD_OUT_TEST_SCORED:
NO

OOD_SCORED:
NO

ISAAC_SIM_LAUNCHED:
NO

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
