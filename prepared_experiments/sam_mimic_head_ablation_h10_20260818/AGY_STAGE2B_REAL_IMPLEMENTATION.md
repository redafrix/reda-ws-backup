# Stage 2B — REAL collector implementation, no stubs

The previous commit `57e012251d63b4f148cb23388e24f7ca45808e1d` is REJECTED as an implementation milestone. It contains placeholder code (`pass`) and a speculative rotation adapter. Do not launch it.

Machine: Sam / PCROBOTUBUNTU05
Clean worktree: `/home/rootalkhatib/test/reda_ws_current_20260818`
Branch: `experiment/sam-mimic-head-ablation-h10-20260818`

## Absolute prohibitions

Do NOT launch a rollout.
Do NOT train.
Do NOT touch HARD1000.
Do NOT keep any `pass`, `...`, `TODO`, `FIXME`, `NotImplementedError`, placeholder/stub function, or comment such as "for static test passing" in executable collector/feature/adapter code.
Do NOT claim tests pass unless they exercise the real implementation.
Do NOT infer axis-angle from proprio conversion.
Do NOT use the old one-action `collect()` loop from `collect_fiper_uncertainty_receding_dean_v1.py`.
Do NOT silently switch back to 9 candidates.

## Authoritative runtime pieces

Use these frozen sources already in `source_snapshot/`:

1. `online_gate_micro_ablation_20260709.py`
   - source of truth for corrected query loop, separate nominal-candidate generation, deterministic seed semantics, and full true-H10 execution.

2. `collect_fiper_uncertainty_receding_dean_v1.py`
   - use ONLY its environment/model/reset/image/success/helper utilities.
   - DO NOT use its historical one-action receding `collect()` loop.

3. `action_hub.py`
   - source of truth for normalization/postprocess implementation.
   - note: its action-space documentation labels action[3:6] as delta Euler, while postprocess itself only unnormalizes. This alone is NOT sufficient to freeze the 3D->6D rotation mapping.

Final policy bindings remain:

- checkpoint: `/home/rootalkhatib/test/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors`
- checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- normalization: `/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json`
- SimVLA root: `/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified`
- LIBERO-PRO root: `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO`
- suite: ONLY `libero_goal_object`, task IDs 0..9
- execution horizon: 10
- max environment actions: 300

## A. First recover the FRIEND 10D rotation convention exactly

Before implementing the adapter, search the historical Sam workspaces for the friend's Mimic/W2A conversion code. Priority known location from prior audit:

`/home/rootalkhatib/test/reda_ws/fiper_ws/external/fiper/models/mimic.py`

Also search for functions/strings:

- `action_10d_to_7d`
- `rotation_6d`
- `rot6d`
- `matrix_to_rotation_6d`
- `rotation_6d_to_matrix`

Return and record the exact source path, SHA256, function name and exact 6D convention (which matrix rows/columns/order are serialized).

Then trace the actual LIBERO action controller path under the installed LIBERO-PRO/robosuite code to establish what environment action dimensions 3:6 mean at `env.step(action)`. Do not rely only on comments in `action_hub.py`.

Write:

`collector/ROTATION_ADAPTER_PROVENANCE.json`

with:

- simvla_env_rotation_representation
- simvla_controller_source_path + sha256 + function
- friend_10d_rotation_representation
- friend_converter_source_path + sha256 + function
- exact_forward_7d_to_10d_mapping
- exact_inverse_parity_mapping
- provenance_complete true/false

If provenance_complete=false, STOP. Do not implement a guessed adapter.

## B. Real collector implementation

Replace the rejected stub files with real code.

Primary file:

`collector/collect_goal_object_mimic_head_h10.py`

It must be a complete runnable collector, not a thin placeholder.

Required behavior per policy query:

1. observe current state
2. encode current agent + wrist images and language once
3. construct exactly 8 unique action seeds
4. generate candidate 0 ALONE, matching final SimVLA-only semantics
5. generate candidates 1..7 as the alternative batch from the same encoded state
6. capture true native-normalized SimVLA state `X_d` and vector field `V_d` at EVERY denoising step for all 8 candidates
7. combine candidates only for feature computation; do not regenerate candidate 0 in an 8-way batch
8. postprocess all final chunks with the frozen SimVLA action space
9. execute ONLY candidate 0
10. execute the FULL H10 chunk, action indices 0..9, stopping only on success/done/300-action budget
11. make the next policy query only after the chunk finishes or episode terminates

The collector must never use risk scores to modify execution.

## C. Denoising metrics

Implement real extraction from SimVLA flow dynamics, not from post-hoc fake arrays.

At denoising step d, from native normalized tensors:

- `X_d`: `[8,10,7]`, the pre-update action state supplied to the transformer at that step
- `V_d`: `[8,10,7]`, the velocity field returned for those same candidates and same step

Store the step number and these EXACT scalar metrics:

- `sample_pairwise_mse_mean`
- `sample_variance_max`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`

Pairwise quantities must EXCLUDE diagonal self-pairs. Average over unordered candidate pairs, then over action horizon/dimensions. Do not include zero self-distances, because doing so biases the metric downward.

Record 10 contiguous denoising records if the configured model uses 10 steps; assert actual count.

## D. 8 genuine candidates and feature-space storage

Final candidate tensor:

- native env: `[8,10,7]`
- friend monitor representation: `[8,10,10]`

The 10D conversion must follow the recovered friend convention exactly.

Store both forms, because the environment executes 7D and the risk-head feature extractor consumes the friend-compatible 10D representation.

Required NPZ arrays per query:

- `action_candidates_env_7d` float32 `[8,10,7]`
- `action_candidates_monitor_10d` float32 `[8,10,10]`
- optionally native normalized 7D chunks if needed for audit

## E. Feature contract

Implement the frozen Mimic-style Single-Head K1-without-ACE feature contract from `PROTOCOL.md`:

- 9 candidate-disagreement/action scalars
- 25 denoising summaries (5 traces x first,last,mean,max,last-first)
- 3 temporal/change scalars
= 37 scalars

H10 horizon tensor: `[10,6]`

The code must materialize both from real candidate arrays and real denoising traces.

No ACE, TopK8, V2W residual, task ID, timestep, reward or future observation may enter the neural features.

## F. Episode/split logic

Only official LIBERO-PRO Goal-Object tasks 0..9.

Fixed non-calibration collection:

- train: 500 episodes
- development: 200 episodes
- heldout_seen_test: 200 episodes

All episodes derived from the same `(task_id, init_state_idx)` must be assigned together; no reset-state leakage.

Calibration pool is collected separately from designated calibration init states until exactly 100 SUCCESSFUL calibration episodes are available. Failed calibration attempts remain logged but are not used to derive the success-only threshold.

Do not mix heldout_seen_test into model selection or calibration.

## G. Dataset records

Produce:

```
DATA_ROOT/
  queries.jsonl
  arrays/
  episode_summaries.jsonl
  collection_manifest.json
  split_manifest.json
  sha256sums.txt
```

Every query record must include:

- episode_key
- task_id
- init_state_idx
- rollout_seed
- query_index
- action_timestep_start
- actions_executed_from_chunk
- assignment
- candidate_seeds[8]
- arrays_path
- `w2a_denoising_step_metrics`
- eventual_failure_target after episode completion
- parent episode success/outcome
- instruction
- checkpoint SHA
- normalization SHA
- collector Git commit/code SHA

No absolute path is allowed as the only pointer to an NPZ; use dataset-relative paths.

## H. REAL tests — no rollout

Tests must import and execute the actual production functions.

Minimum required tests:

1. no-stub scan: recursively fail if executable collector modules contain `pass`, literal ellipsis placeholder, `NotImplementedError`, `TODO`, `FIXME`, or `for static test passing`
2. 7D->10D->7D rotation parity over identity + >=100 random small rotations according to exact friend converter convention
3. candidate seed uniqueness and deterministic reproducibility
4. candidate combine order preserves candidate0 and indices 1..7 exactly
5. pairwise metric unit test proving diagonal pairs are excluded
6. denoising trace reducer returns exactly 25 values in frozen order
7. full feature extractor returns exactly scalar `(37,)` and horizon `(10,6)` and finite values
8. split assignment has zero `(task_id,init_state_idx)` leakage
9. collector static AST test proves its execution loop can execute indices 0..9 rather than only `[0]`
10. manifest builder asserts suite exactly `libero_goal_object`, tasks exactly 0..9, H10, 8 candidates, 300 max actions

Tests using random fake arrays are allowed only for mathematical unit tests; they are not sufficient to claim candidate-generation or collector readiness.

## I. Static import/preflight only

From the Sam SimVLA environment, run imports and `--help` only. Do not load the GPU checkpoint yet if not necessary. Do not start an environment episode.

Run the complete production test suite.

## J. Git

Only if all above passes:

Commit message exactly:

`fix(sam): replace stub with real Goal-Object H10 Mimic-head collector`

Push branch.

## RETURN ONLY

ROTATION_PROVENANCE_COMPLETE:
YES/NO

SIMVLA_ENV_ROTATION:
representation:
source:
function:

FRIEND_10D_ROTATION:
representation:
source:
function:
ordering:

ADAPTER_PARITY:
passed:
random_cases:
max_roundtrip_error:

COLLECTOR_REAL_IMPLEMENTATION:
YES/NO
path:
sha256:
line_count:

STUB_SCAN:
passed:
violations:

TRUE_H10_STATIC_GATE:
passed:

CANDIDATES:
count:
main_separate:
alternatives:

DENOISING:
steps:
metrics_per_step:
pairwise_diagonal_excluded:

FEATURE_CONTRACT:
scalar_shape:
horizon_shape:

SPLIT_LEAKAGE_TEST:
passed:

TESTS:
passed:
count:

ROLLOUT_LAUNCHED:
NO

COMMIT:
<sha/NONE>

HARD1000_TOUCHED:
NO
