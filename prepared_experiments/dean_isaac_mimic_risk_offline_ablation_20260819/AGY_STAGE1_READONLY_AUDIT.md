# Stage 1 — Dean read-only audit for Mimic-style Isaac risk-head ablation

This stage is mechanical evidence recovery only.

Machine: Dean
Workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Branch: `experiment/dean-isaac-mimic-risk-offline-ablation-20260819`

## ABSOLUTE PROHIBITIONS

DO NOT:
- launch Isaac Sim;
- step an environment;
- collect or recollect any episode;
- run SimVLA inference;
- train a risk model;
- materialize a full new dataset;
- alter Round0;
- alter HARD1000;
- alter OOD150/OOD400;
- reuse anything from invalid commit `70327b4b31bde35c01fda29a807f9100b5295a62`;
- copy candidate0 denoising evidence into alternative candidate slots;
- invent feature mappings.

Read small files and stream/decompress raw rows only as needed.

## 1. VERIFY CANONICAL ROUND0 AND FROZEN SPLIT

Verify exact roots:

`W=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

`$W/outputs/final_seen_h10_round_000_seed20260730`

`$W/frozen_datasets/isaac_seen_h10_topk8_v1`

Mechanically report:

- committed episode count;
- success/failure counts;
- total query-row count;
- split episode counts train/validation/test;
- split row counts;
- split failure counts;
- SHA256 of dataset manifest, split assignments and normalization.

Expected reference only, NOT a substitute for measurement:
4000 episodes, 3908/92 outcomes, 2800/600/600 episodes, 75603 rows.

## 2. FULL RAW SCHEMA CENSUS

Across ALL committed Round0 episodes, stream every `risk_rows.jsonl.zst` row and produce a key/path census without modifying source files.

For every leaf key/path report:

- rows_present;
- observed Python/JSON types;
- observed array/list shapes where applicable;
- minimum/maximum length where variable;
- NaN/Inf count for numeric content when practical.

Specifically identify exact paths/shapes for:

- main candidate normalized H10 chunk;
- main candidate environment H10 chunk;
- all alternative candidate normalized chunks;
- all alternative candidate environment chunks;
- main seed;
- alternative seeds;
- current proprio;
- history;
- existing 49-D uncertainty vector/map;
- `simvla_uncertainty_raw` or equivalent;
- parent episode outcome/label;
- query/decision index;
- executed action/chunk information;
- any saved simulator state / robot state / image / latent / VLM feature pointer if present.

Do not assume LIBERO field names. Report actual Isaac field paths.

## 3. CANDIDATE CONTRACT AUDIT

Across all rows verify:

- candidate0 final chunk shape;
- alternative final chunk count and shape;
- total candidate count;
- seed uniqueness within query;
- any missing candidate rows;
- whether candidate0 is present separately from alternatives;
- normalized versus environment/action-space representations.

Return violations and counts.

## 4. CANDIDATE0 DENOISING/DYNAMICS CENSUS

Inspect every distinct leaf/key inside the candidate0 raw uncertainty/dynamics record.

For each key report:

- exact name;
- scalar/list/array;
- shape/trace length;
- presence count;
- short mechanical description only if source code gives semantics;
- source-code function/path responsible for writing it if traceable.

Explicitly search for raw or summarized forms of:

- denoising variance traces;
- path variance;
- last-step variance;
- velocity norms;
- update norms;
- update vectors;
- update oscillation;
- direction flips;
- initial/final denoising values;
- denoising slope/spike;
- sample/final-action variance;
- sample pairwise distances;
- any X_d trajectory;
- any V_d/vector-field trajectory.

State mechanically whether full per-step candidate0 X_d exists: YES/NO.
State mechanically whether full per-step candidate0 V_d exists: YES/NO.

## 5. ALTERNATIVE-CANDIDATE DYNAMICS AUDIT

Search all Round0 rows and sidecars for candidate-specific denoising evidence for alternatives 1..8.

Report separately whether any of these exist for alternatives:

- per-step X_d;
- per-step V_d;
- per-step predicted variance;
- per-step update vectors;
- summarized uncertainty/raw trace per candidate.

If absent, say absent. Do not infer from seeds/final chunks.

## 6. FRIEND / MIMIC RISK-HEAD SOURCE RECOVERY ON DEAN

Search READ ONLY for small source/handoff files under these likely roots:

- `/mnt/ai/projects`
- `/home/redafrix/tests/internship`
- `/media/redafrix/My Passport1/reda_ws`
- other already-mounted project roots on Dean

Search filenames/content for:

- `mimic`
- `RiskHead`
- `risk_input`
- `z_t.detach`
- `w2a`
- `SingleHead`
- `Single-Head`
- `K1`
- `Combined without ACE`
- `w2a_denoising_step_metrics`
- `sample_pairwise_mse_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`
- `74`
- `GRU`
- `conformal`

Only inspect small code/config/text/checkpoint-metadata files. Do not copy heavy weights.

For every plausible friend-head source return path + SHA256 + why it is relevant.

Then resolve the authoritative friend contract by source priority:

A. actual friend executable source;
B. explicit handoff source/config;
C. paper-level K1 description only if A/B unavailable.

Return exact source-backed:

- candidate count;
- action representation/dimension if relevant;
- temporal history length;
- risk architecture layers/widths;
- static feature count and ordered feature names if present;
- temporal/horizon token shape and ordered channels if present;
- denoising metrics and exact formulas if source gives them;
- target semantics;
- loss/class weighting;
- training hyperparameters if present;
- threshold/calibration rule.

If different source artifacts disagree, DO NOT reconcile. Return the conflict verbatim by source.

## 7. FEATURE AVAILABILITY MATRIX

Construct a factual matrix mapping every recovered friend feature/input to one of:

- EXACT_SAVED
- EXACT_RECONSTRUCTIBLE
- PROXY_FROM_CANDIDATE0
- UNAVAILABLE

For EXACT_RECONSTRUCTIBLE state the precise retained source fields and deterministic formula.

For PROXY_FROM_CANDIDATE0 state:

- the friend quantity being approximated;
- the candidate0-only retained quantity proposed as proxy;
- why it is not exact.

Do not decide to use a proxy merely because one exists. This stage only maps feasibility.

For UNAVAILABLE state the exact missing evidence.

## 8. EXACT FINAL-CANDIDATE RECONSTRUCTIONS ON A TINY SAMPLE

For exactly 20 deterministic query rows spanning success/failure and train/validation/test, compute ONLY quantities derivable from retained FINAL candidate chunks, such as:

- coordinate variance mean/max across a candidate subset;
- off-diagonal candidate pairwise chunk MSE;
- candidate0-versus-candidate-mean MSE;
- per-H10-index coordinate variance;
- endpoint spread;
- translation/rotation/gripper-group dispersion if dimensions have source-backed semantics.

Do not run any model.
Do not write into source dataset directories.

Save only a small JSON audit under:

`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/audit/`

with source episode/query IDs and computed values.

## 9. REINFERENCE / STATE-RESTORE POSSIBILITY — AUDIT ONLY

Without launching Isaac, determine whether Round0 retained enough information to restore an exact query state and observation later.

Report presence/absence of:

- full simulator snapshot at every query;
- robot state;
- target/clutter poses;
- camera state/config identity;
- RGB observations;
- policy seeds;
- instruction;
- deterministic scene identity.

Return one of:

- EXACT_REINFERENCE_POSSIBLE_FROM_RETAINED_STATE
- APPROXIMATE_REPLAY_ONLY
- NOT_PRACTICALLY_RECONSTRUCTIBLE

with missing inputs. Do not actually reinfer.

## 10. INVALIDATION CHECK

Find the corrective evidence corresponding to commit `86f5baf3` and the blacklisted `70327b4b31bde35c01fda29a807f9100b5295a62` workflow if present locally/GitHub-derived notes are already in workspace.

Verify that no proposed Stage-1 reconstruction depends on reusing candidate0 trace for alternatives.

## OUTPUT FILES

Create only small audit artifacts in the experiment branch/worktree:

- `audit/ROUND0_SCHEMA_CENSUS.json`
- `audit/CANDIDATE_DYNAMICS_CENSUS.json`
- `audit/FRIEND_HEAD_SOURCE_AUDIT.json`
- `audit/FEATURE_AVAILABILITY_MATRIX.json`
- `audit/FINAL_CHUNK_20ROW_CHECK.json`
- `audit/REINFERENCE_FEASIBILITY.json`
- `audit/STAGE1_SUMMARY.md`

Do not include heavy raw data.

Commit only if the audit is complete.

Commit message exactly:

`audit(dean): map Round0 evidence to Mimic risk-head contract`

Push branch.

## RETURN ONLY

ROUND0:
episodes:
success:
failure:
rows:
train_eps/train_rows:
val_eps/val_rows:
test_eps/test_rows:

CANDIDATES:
main_shape:
alternative_count:
alternative_shape:
total_candidates:
seed_violations:

CANDIDATE0_DYNAMICS:
full_Xd_saved:
full_Vd_saved:
raw_keys_count:
trace_keys:
summary_keys:

ALTERNATIVE_DYNAMICS:
Xd_saved:
Vd_saved:
variance_trace_saved:
raw_uncertainty_saved:

FRIEND_HEAD:
authoritative_source_kind:
path:
sha256:
architecture:
history_length:
static_features:
temporal_tokens:
candidate_count:
calibration:

FEATURE_MATRIX:
exact_saved_count:
exact_reconstructible_count:
proxy_count:
unavailable_count:

REINFERENCE:
status:
missing:

NO_COLLECTION:
YES

NO_SIM_LAUNCHED:
YES

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
