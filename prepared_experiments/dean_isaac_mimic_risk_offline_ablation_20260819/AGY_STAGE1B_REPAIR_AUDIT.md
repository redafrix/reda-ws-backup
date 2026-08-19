# Stage 1B — repair the audit, raw evidence only

The previous audit commit `b93b09b41a7bc1ffc80e25953105783804c23e49` is NOT accepted as the final evidence basis.

Two defects must be repaired:

1. `FRIEND_HEAD_SOURCE_AUDIT.json` incorrectly used this experiment's own `PROTOCOL.md` as the authoritative friend source.
2. `ROUND0_SCHEMA_CENSUS.json` reports `total_rows=75603` while core raw-row fields show `rows_present=1876`, so the claimed full-corpus census is not internally valid.

Agy is an operator only. Do not make experiment-design decisions.

## A. Full-corpus Round0 census must really cover 75,603 rows

Read every committed `risk_rows.jsonl.zst` row belonging to accepted Round0:

`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730`

Use the canonical episode/audit membership to exclude infrastructure errors/quarantine exactly as the frozen dataset does.

Produce these hard counters:

- number of episode row files opened;
- number of rows decompressed per episode;
- sum of rows read;
- number of rows accepted into frozen Round0;
- number of rows excluded and exact exclusion reason;

Require accepted total == 75,603.

For these REQUIRED fields, report presence count over the accepted 75,603 rows:

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
- `simvla_uncertainty_49d`
- `simvla_uncertainty_delta_49d`
- `simvla_uncertainty_raw`
- episode label/outcome field used by frozen materializer

If any field is legitimately absent from some accepted rows, report exact count and the exact episode/query IDs for the first 20 absences. Do not hide it by sampling.

## B. Candidate0 raw dynamics: exact shapes and reconstructibility

Across all accepted rows with `simvla_uncertainty_raw`, mechanically report shapes/lengths for each of these keys when present:

- `initial_noise`
- `final_action_normalized`
- `denoise_mean_trace`
- `velocity_norm_trace`
- `update_norm_trace`
- `update_vector_trace`
- `path_variance`
- `last_step_variance`
- `uncertainty_parameterization`

For `update_vector_trace`, establish the exact tensor/list shape and the writer source code.

Then answer these factual reconstruction questions ONLY:

1. Given `initial_noise`, ordered `update_vector_trace`, and the collector's integration `dt`, can candidate0 pre-update states X_d be reconstructed exactly? YES/NO, with the exact recurrence from code.
2. Given `update_vector_trace` and fixed `dt`, can candidate0 V_d be reconstructed exactly? YES/NO, with the exact recurrence from code.
3. Is `dt` constant and source-backed for every Round0 query? YES/NO.

Do not extrapolate this reconstruction to alternative candidates.

## C. Alternative candidates: initial-noise reproducibility audit

The rows contain alternative candidate seeds. Locate the exact Round0 seed/noise-generation function in the collector source.

Mechanically determine whether, WITHOUT policy inference, the exact initial Gaussian noise tensor for alternatives 1..8 can be regenerated from each stored seed.

Return:

- generator library/type;
- device dependence;
- tensor shape;
- dtype;
- seed transform/modulo if any;
- exact code path;
- deterministic regeneration possible on Dean: YES/NO.

Do NOT claim any intermediate alternative X_d/V_d is recoverable from this.

## D. Recover the ORIGINAL friend/Mimic/W2A risk-head source on Dean

Do not use `PROTOCOL.md` or `MIMIC_H10_HANDOFF_CONTRACT.md` as a discovered friend source. Those are experiment documents.

Search the old Bob disk and Dean project trees exhaustively for SMALL source/config/text files.

Known historical clue from earlier source recovery:

`wm_collected/wm_collected/wm_methodology_source/eval/libero/run.py`

Search sibling/parent trees around any `wm_collected`, `wm_methodology_source`, `mimic`, `W2A`, `V2W`, `risk`, `monitor` directories.

Priority roots:

- `/media/redafrix/My Passport1/reda_ws`
- `/media/redafrix/My Passport/reda_ws` if mounted
- `/home/redafrix/tests/internship`
- `/mnt/ai/projects`

Search file CONTENT for all of:

- `74`
- `16`
- `RiskHead`
- `risk_head`
- `GRU`
- `w2a`
- `W2A`
- `episode_max`
- `conformal`
- `sample_pairwise_mse_mean`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`
- `candidate_centrality`
- `plan_overlap`
- `receding`

Also search for filenames matching:

- `*risk*.py`
- `*monitor*.py`
- `*uncert*.py`
- `*feature*.py`
- `*train*.py`
- `*dataset*.py`
- `*mimic*.py`

Do not stop at the first result.

For every plausible ORIGINAL friend/W2A source file, return:

- absolute path;
- SHA256;
- size;
- relevant class/function names;
- imports of sibling source files;
- whether it is executable source, config, generated report, or paper text.

Copy only small ORIGINAL source/config files into:

`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/friend_source_snapshot/`

Preserve bytes. Do not copy weights/datasets.

## E. If original source exists, extract contract mechanically

From original executable source only, report:

- exact selected K1 class/model name;
- temporal history length;
- GRU layer count;
- GRU hidden size;
- static branch dimensions;
- fusion dimensions;
- exact ordered static feature names and count;
- exact temporal token names/channels, shape and count;
- candidate count;
- candidate0 semantics;
- exact formulas for candidate variance/pairwise disagreement/plan overlap/denoising dynamics;
- loss;
- sampling/class weighting;
- optimizer/lr/epochs/batch if encoded;
- normalization;
- checkpoint-selection metric;
- episode-level calibration formula/alpha values.

Do not reconcile discrepancies with the paper or handoff. Return source facts.

## F. If original source cannot be found

Return `ORIGINAL_FRIEND_SOURCE_FOUND=NO`.

Do NOT call our experiment docs authoritative friend source.

The fallback source is already frozen separately as:

`MIMIC_H10_HANDOFF_CONTRACT.md`

ChatGPT, not Agy, will decide whether to use that fallback.

## G. No implementation/training

Do not write the materializer, feature code, model, trainer or evaluator yet.
Do not launch Isaac.
Do not run SimVLA.
Do not touch HARD1000/OOD150/OOD400.

## Output

Create/replace only repaired small audit files:

- `audit/ROUND0_FULL_CORPUS_CENSUS_V2.json`
- `audit/CANDIDATE0_RECONSTRUCTIBILITY_V2.json`
- `audit/ALTERNATIVE_INITIAL_NOISE_AUDIT.json`
- `audit/ORIGINAL_FRIEND_SOURCE_SEARCH.json`
- `audit/ORIGINAL_FRIEND_CONTRACT.json` if source exists
- `audit/STAGE1B_SUMMARY.md`

Commit exactly:

`audit(dean): repair full Round0 census and recover original Mimic source`

Push branch.

## RETURN ONLY

FULL_CORPUS:
row_files_opened:
rows_streamed:
rows_accepted:
rows_excluded:
required_field_presence_counts:

CANDIDATE0_RECONSTRUCTION:
initial_noise_shape:
update_vector_trace_shape:
dt:
Xd_exactly_reconstructible:
Vd_exactly_reconstructible:
source_path:
function:

ALTERNATIVE_INITIAL_NOISE:
exactly_regenerable_from_seed:
generator:
shape:
dtype:
source_path:
function:

ORIGINAL_FRIEND_SOURCE_FOUND:
YES/NO

ORIGINAL_FRIEND_SOURCE_FILES:
<path | sha256 | class/functions for each, or NONE>

ORIGINAL_K1_CONTRACT:
history_length:
gru_layers:
gru_hidden:
static_feature_count:
static_feature_names_source:
temporal_token_shape:
temporal_token_names_source:
candidate_count:
loss:
calibration:

NO_SIM_LAUNCHED:
YES

NO_TRAINING:
YES

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
