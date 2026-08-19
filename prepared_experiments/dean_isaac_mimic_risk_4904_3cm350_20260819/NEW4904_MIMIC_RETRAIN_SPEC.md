# NEW4904 Mimic Risk-Head Retrain Specification

## 0. Scientific role

This is a NEW experiment. It supersedes the old Round0-4000 Mimic training dataset for future main-line Isaac comparisons.

Source dataset identity is frozen by NAME and expected census:

- dataset name: `isaac_seen4904_h10_3cm350_exact_v1`
- episodes: 4904
- success episodes: 4387
- failure episodes: 517
- query rows: 96813
- execution horizon: H10
- success label semantics: first reach `<= 0.030 m` within the first 350 control ticks at 30 Hz
- dwell requirement: none

The current main comparison model is:

`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`

The Mimic-style baseline MUST use the exact same frozen train/validation/test episode split as that main TopK8 model. No new random split is allowed.

The old Round0-4000 dataset, its split, labels, normalization and derived arrays MUST NOT be used as source data for this retraining. Old code modules may be reused only when their semantics are independently source-compatible.

## 1. New experiment identity

Experiment name:

`isaac_mimic_h10_strict_3cm350_seen4904_v3`

Derived dataset root:

`$W/derived_datasets/isaac_mimic_h10_strict_3cm350_seen4904_v3`

Model root:

`$W/models/isaac_mimic_h10_strict_3cm350_seen4904_v3`

Validation root:

`$W/evaluations/isaac_mimic_h10_strict_3cm350_seen4904_v3/validation`

No held-out test scoring is permitted in the build/train/validate stage.

## 2. Source-resolution gate

A mechanical audit MUST first locate exactly one dataset root corresponding to `isaac_seen4904_h10_3cm350_exact_v1` under the canonical Dean workspace.

It MUST prove from manifests / split metadata / row or episode metadata:

- 4904 unique episodes
- 4387 success and 517 failure episodes
- 96813 total query rows
- H10 action chunks
- label semantics are the exact 3 cm / 350-control-tick / 30 Hz / no-dwell protocol
- all rows map unambiguously to a parent episode
- exact train/validation/test membership can be recovered from the frozen source used by `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`

If any of these cannot be proved, STOP before materialization or training.

The split counts and split failure counts are NOT to be guessed or recreated. They are to be read mechanically from the frozen split artifact and written into the new manifest.

## 3. Candidate contract

Portable Mimic H10 requires exactly 8 stochastic final candidates.

If the new dataset retains main + >=7 alternatives, use exactly:

`[main, alternative1, alternative2, alternative3, alternative4, alternative5, alternative6, alternative7]`

in stored order.

Do not choose candidates by score, distance, outcome or risk. Any additional stored alternative is audit-only.

For final-candidate disagreement/horizon features, use ENVIRONMENT action chunks, not normalized chunks.

Expected Isaac action semantics remain 7D controller actions transformed to the source-backed Mimic 10D representation `[translation3, rotation6d6, gripper1]` using the already verified action adapter ONLY if the new dataset controller/action binding is proven identical. If the action binding differs, STOP and report; do not guess a conversion.

## 4. Exact available Mimic features

### 4.1 Nine candidate-disagreement scalars

Use the same exact source-backed definitions already frozen for the prior strict Mimic baseline:

1. action variance mean
2. action variance max
3. mean pairwise MSE over 28 unordered pairs
4. first-candidate vs candidate-mean MSE
5. endpoint position spread mean
6. endpoint position spread max
7. position variance mean
8. rotation variance mean
9. gripper variance mean

All are computed from the 8 retained final ENV candidates after exact 7D->10D conversion.

### 4.2 H10 horizon tensor `[10,6]`

Per proposal index:

1. position variance mean
2. position variance max
3. rotation variance mean
4. gripper variance
5. cumulative position spread mean
6. cumulative position spread max

Use exactly the existing frozen formulas; no redesign.

### 4.3 Three temporal-change scalars

1. `history_available`
2. absolute change in action-variance mean from previous query
3. absolute change in endpoint-spread mean from previous query

First query values are `[0,0,0]`.

## 5. The 25 denoising-dynamics channels: strict fidelity rule

The portable handoff expects five genuine cross-candidate denoising traces, each summarized by first / last / mean / max / last-minus-first = 25 scalars.

For this NEW dataset, perform a full-field audit before deciding availability.

### EXACT mode

Use the 25 channels ONLY if the new dataset directly stores, for every accepted row, the genuine source-compatible five cross-candidate trace series with unambiguous semantics matching the portable handoff:

- `sample_pairwise_mse_mean`
- `sample_variance_max`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`

The trace ordering and denoising-step axis must be proven from collector/source code. Do not infer formulas from names.

If this proof passes, summarize each genuine trace as first / last / mean / max / last-minus-first and use them in scalar dims 9..33.

### STRICT-MISSING mode

If those exact five genuine cross-candidate traces are not directly retained/proven for every row, then scalar dims 9..33 are EXACT ZERO for every row.

For disabled channels normalization is fixed to mean 0 and std 1.

PROHIBITED substitutes:

- candidate0-only dynamics
- candidate0 Xd/Vd proxies
- alternative-trajectory fabrication
- interpolation
- final-chunk approximations
- learned imputation
- reconstruction from insufficient fields
- guessed formulas for the five handoff traces

This decision is based only on source-field availability, never on validation/test performance.

## 6. Scalar layout

Always preserve the 37D Mimic input shape:

- dims 0..8 = exact nine final-candidate disagreement features
- dims 9..33 = exact genuine five-trace summaries if EXACT mode, otherwise all zeros
- dims 34..36 = exact temporal-change features

Record `dynamics_mode = EXACT` or `STRICT_MISSING` in the dataset manifest with source evidence.

## 7. Temporal window and model

Temporal query window = exactly 8 query records ending at current query.

Normalize available features first, then left-zero-pad startup history. No mask.

Architecture remains the portable Mimic H10 model:

- scalar branch: `37 -> Linear128 -> LayerNorm -> GELU -> Dropout0.1`
- horizon projection: `6 -> 128` + learned H10 positional embeddings
- TransformerEncoder: 2 layers, 4 heads, FFN 512, dropout 0.1
- mean pool horizon -> 128
- concat scalar+horizon -> 256
- query encoder: `256 -> 128 -> 64`, GELU/dropout as previously frozen
- temporal GRU: input64, hidden128, 1 layer, batch_first
- final hidden -> Linear1 risk logit

Target = parent episode failure under the NEW exact 3cm350 label.

No task ID, timestep/progress, reward, future observation, scene ID, target identity, episode length or outcome-derived quantity enters the input.

## 8. Normalization and split

Fit normalization from NEW4904 TRAIN split only.

- scalar active dimensions: per-coordinate train mean/std, std floor 1e-6
- disabled dynamics dimensions, when STRICT_MISSING: mean 0, std 1
- horizon: per-channel train mean/std across train rows and all 10 horizon positions, std floor 1e-6

Use the exact NEW4904 TopK8 split membership. No resplitting.

The final manifest must report per split:

- episode count
- success episode count
- failure episode count
- row count
- row positive/negative counts

## 9. Training

Use the same portable Mimic training recipe, from scratch on NEW4904 only:

- seeds: 0,1,2,3,4
- epochs: 25 each
- batch size: 64
- optimizer: AdamW
- learning rate: 1e-3
- weight decay: 1e-4
- gradient clip norm: 1.0
- dropout: 0.1
- BCEWithLogitsLoss
- `pos_weight = N_negative_train_rows / N_positive_train_rows` computed from NEW4904 train rows only
- every train query appears once per epoch
- deterministic DataLoader generator seeded per run
- checkpoint every epoch
- choose highest validation row AUPRC, earliest epoch on exact tie
- seed0 remains primary regardless other seed validation scores

No checkpoint/seed selection from held-out test or OOD.

## 10. Validation calibration only

For each selected checkpoint, score NEW4904 validation only.

Calibrate successful-episode-max conformal thresholds using the corrected order statistic for alpha 0.05, 0.10, 0.15; alpha 0.10 is primary.

Also record supplemental:

- fixed 0.5
- validation row best-F1
- successful-episode-max empirical q90/q95/q99

Do not access held-out test scores in this stage.

## 11. Required anti-leakage / provenance freeze

Before training:

- hash source dataset manifest
- hash source split assignment artifact
- hash new dataset arrays
- hash normalization
- bind source action/controller semantics
- bind candidate subset
- bind dynamics mode and evidence

After training:

- hash every selected checkpoint
- hash every validation freeze
- record all 25 epoch logs for all five seeds
- freeze `primary_seed=0`, `primary_operating_point=conformal_alpha_0.10`

## 12. Hard exclusions

Do NOT:

- use old Round0 arrays, labels, split or normalization
- copy old Mimic V1/V2 scalar arrays into this experiment
- tune against previous seen/OOD results
- score NEW4904 held-out test in this stage
- score OOD150/OOD400
- touch HARD1000
- recollect
- launch Isaac Sim
- run SimVLA inference
- kill or modify unrelated running GPU jobs

The sole goal of this stage is: build a fresh Mimic-compatible derived dataset from the new exact Seen4904 dataset, train five fresh Mimic risk heads, and freeze validation selections/thresholds.