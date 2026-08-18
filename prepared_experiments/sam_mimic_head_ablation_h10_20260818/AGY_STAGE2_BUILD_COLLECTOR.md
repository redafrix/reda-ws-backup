# Agy Stage 2 — build the new Goal-Object H10 Mimic-head collector

Machine: Sam / PCROBOTUBUNTU05
Clean worktree: `/home/rootalkhatib/test/reda_ws_current_20260818`
Branch: `experiment/sam-mimic-head-ablation-h10-20260818`

This stage builds code and runs STATIC/unit checks only. **Do not launch a rollout yet.**

## Authoritative sources already frozen

Use only these frozen snapshots for behavioral lineage:

- `source_snapshot/online_gate_micro_ablation_20260709.py`
  - exact final H10 runner
  - original SHA256 `c7ebe368d4b14272eceb063cf3bfbf198fd56475abc2bbbec66f7e86ae744351`
- `source_snapshot/collect_fiper_uncertainty_receding_dean_v1.py`
  - exact co-located helper
  - original SHA256 `faec71e7685ac17b33627d0beb4864d47851335c068527dc6af1c31e521ef9ea`
- `source_snapshot/action_hub.py`
- `source_snapshot/run_manifest.json`

The helper's historical `collect()` function is **NOT an acceptable rollout base** because it executes only `main_chunk_env[0]` and replans after one action. Reuse its setup/env/reset/image/success helpers only.

The new collector must use the final runner's full-H10 execution semantics.

## Friend-head source of truth

The user supplied `simvla_h10_risk_monitor_handoff` package. Its K1 contract is authoritative for the new risk-head inputs:

- proposal horizon 10
- commitment horizon 10
- action candidates `[8,10,10]`
- 37 scalar features + `10x6` horizon features
- Single-Head GRU Combined without ACE is the primary model
- no ACE, no V2W/K3, no proposal-overlap features
- exactly five genuine denoising-step metric traces

Do not alter the friend package in this stage.

# PART A — Sam asset parity gate

Before writing runtime-dependent code, resolve the exact final policy assets on Sam.

Required checkpoint model SHA256:

`3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`

Required normalization SHA256:

`5e4dcf9026271137e102f6f784d345f0f03c1fd9963b679631b110a16788149e`

Required final SimVLA source identity from provenance:

`1665bc69f14d648707963e4c94cd9899092a7dc0`

Search Sam first for existing matching assets. Do not assume the old `original_simvla_libero` checkpoint is equivalent.

Also verify the existing Sam LIBERO-PRO checkout can instantiate official `libero_goal_object` tasks `0..9` and that every task exposes at least 50 official init states.

If the exact checkpoint or exact SimVLA source is absent on Sam, STOP this stage and return which assets are missing. Do not silently use an older checkpoint/source and do not copy multi-GB assets during this stage.

# PART B — trace the actual 7D LIBERO rotation semantics

Do not trust comments such as `delta_euler` or prior audit prose by themselves.

Mechanically trace the actual local Sam call path from:

`env.step(action_7d)`

to the robosuite/LIBERO controller consuming action dimensions `3:6`.

Determine from executable source whether those three numbers are interpreted as:

- rotation vector / axis-angle increment,
- Euler increment,
- or another representation.

Record source paths, functions and relevant line ranges in:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/ACTION_SEMANTICS_AUDIT.json`

If the interpretation cannot be proven from code, STOP. Do not guess the 7D->10D adapter.

# PART C — implement deterministic 7D -> friend 10D adapter

Create:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/collector/action_adapter.py`

Input is **environment-space** SimVLA action chunk `[H,7]` after final `model.action_space.postprocess`.

Output `[H,10]`:

`[dx,dy,dz, rotation_6d(6), gripper]`

Rotation-6D follows the friend/Mimic convention: first two columns of the 3x3 rotation matrix, flattened in the exact order used by the supplied Mimic converter.

Use the proven local 3D rotation convention to form that incremental rotation matrix.

Add unit tests covering:

- identity/no-rotation
- small rotations around x/y/z
- random valid rotations
- finite output
- output shape `[10,10]` for H10 chunks
- orthogonality of the reconstructed first two rotation-matrix columns
- parity against the supplied Mimic 10D->7D conversion for rotations, within numerical tolerance, when applying the inverse convention

Do not alter translation or gripper values.

# PART D — implement exact eight-candidate generation wrapper

Create:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/collector/simvla_mimic_features.py`

The policy query must produce exactly **8 genuine candidates total**:

- candidate 0 = nominal/main SimVLA sample, generated ALONE
- candidates 1..7 = seven genuine stochastic alternatives generated in a second batch

This preserves the final H10 runner's correction that candidate 0 must not be generated inside the alternative batch.

All 8 seeds must be unique within a query.

Use the same deterministic seed-generation family as the final H10 runner. Do not use Python's process-randomized hash.

Return:

- `chunks_norm_7d [8,10,7] float32`
- `chunks_env_7d [8,10,7] float32`
- `chunks_monitor_10d [8,10,10] float32`
- ordered candidate seeds
- exact per-step denoising metrics described below

Assert the model's native action count is exactly 10 and denoising step count is exactly the configured value.

# PART E — genuine denoising metrics

The supplied friend package requires these five metrics for every denoising iteration:

1. `sample_pairwise_mse_mean`
2. `sample_variance_max`
3. `sample_variance_mean`
4. `sample_velocity_mse_mean`
5. `vector_field_l2_mean`

The friend handoff does not provide the original upstream collector implementation for these raw metrics. Therefore implement the direct mathematically analogous quantities on SimVLA's **native normalized iterative action-generation state**. Do not pretend they are byte-identical to Mimic; record the adaptation explicitly.

At denoising iteration `d`, let:

- `X_d` = current pre-update SimVLA denoising states for all 8 candidates, shape `[8,10,7]`
- `V_d` = transformer vector fields evaluated at `X_d`, shape `[8,10,7]`

Candidate 0 is evaluated in the one-sample call and candidates 1..7 in the seven-sample call, then their same-step tensors are concatenated before metrics are computed.

Use float64 for metric accumulation after detaching tensors.

Definitions:

- `sample_pairwise_mse_mean` = mean, over all unordered candidate pairs, of MSE between flattened `X_d` tensors.
- `sample_variance_mean` = mean of population variance of `X_d` across the candidate axis (`ddof=0`) over all H10/action elements.
- `sample_variance_max` = maximum of that same population-variance tensor.
- `sample_velocity_mse_mean` = mean, over all unordered candidate pairs, of MSE between flattened `V_d` tensors.
- `vector_field_l2_mean` = mean over candidates and H10 steps of the L2 norm of `V_d` across the 7 action dimensions.

Record one dictionary per denoising iteration with contiguous `denoising_step = 0..D-1`.

Also record in the collection manifest:

`denoising_metric_space = "simvla_native_normalized_7d_preupdate"`

`denoising_metric_adaptation = "direct analogous SimVLA flow-state/vector-field statistics; Mimic upstream raw collector unavailable in supplied handoff"`

Do NOT compute these metrics from final action chunks only.
Do NOT map old 49D uncertainty values into these names.

# PART F — exact W2A feature parity check

Do not manually reimplement the final 37+10x6 extractor differently from the friend package.

Vendor/copy the minimum friend K1 feature code into a small audit-only compatibility location OR import the supplied package if already available locally.

For each synthetic query built by unit tests, write `action_candidates [8,10,10]` and denoising rows, then call the supplied friend `extract_query_features()`.

Require:

- scalar shape `(37,)`
- horizon shape `(10,6)`
- all finite
- first-query `history_available=0`
- second-query `history_available=1`
- no ACE/V2W/overlap inputs

The collector itself should save raw 8x10x10 candidates + raw denoising-step metrics. Training should derive the 37+10x6 features using the friend package, rather than trusting precomputed collector features.

# PART G — build the new collector

Create:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/collector/collect_goal_object_mimic_head_h10.py`

Behavior:

- suite hard-locked to `libero_goal_object`
- task IDs hard-locked to `0..9`
- native H10 proposal
- **full H10 chunk execution** before the next policy query, exactly as in final `run_episode`
- candidate 0 always executed; no risk monitor/controller exists during collection
- max 300 environment actions per episode
- warmup/reset/success semantics from exact recovered helper/final runner
- same final uncertainty-enabled SimVLA checkpoint
- same final normalization
- exactly 8 candidates per query as defined above
- no ACE features
- no TopK8 scoring
- no risk-based action selection
- no image/state saving unless needed for debugging; default off to keep this collection compact

Use the split rules in `PROTOCOL_AMENDMENT_02_COLLECTION_COUNTS.md`.

Every episode receives a deterministic `episode_key` encoding assignment/task/init state/rollout seed index, but task ID itself must not become a neural risk feature.

Every query row stores at minimum:

- `episode_key`
- `query_index`
- `assignment`
- `task_id`
- `init_state_idx`
- `rollout_seed`
- `candidate_seeds[8]`
- `eventual_failure_target` backfilled after episode end
- `arrays_path`
- `w2a_denoising_step_metrics`
- instruction
- executed action count from that H10 chunk
- success-after-query flag for audit only
- checkpoint SHA
- normalization SHA
- collector Git SHA

NPZ per query contains at minimum:

`action_candidates` = monitor-space `float32 [8,10,10]`

Optionally preserve `action_candidates_env7d` and `action_candidates_norm7d` for audit if storage remains reasonable.

Dataset root layout:

```
DATA_ROOT/
  queries.jsonl
  arrays/
  episode_summaries.jsonl
  split_manifest.json
  collection_manifest.json
```

Do not create the final sha256sums file until the collection is frozen/completed.

# PART H — resume safety

The collector must support `--resume` without duplicating completed episode keys.

Before starting an episode, check `episode_summaries.jsonl` for completed keys.

Write query arrays/rows into a temporary per-episode staging directory/file and atomically finalize them only when the episode finishes, so a crash does not create a half-valid episode.

Errors are recorded separately and do not count as completed scientific episodes.

# PART I — tests in this stage only

Run STATIC/unit tests only. No environment rollout.

Required tests:

1. action-adapter unit tests
2. synthetic eight-candidate denoising metric tests with hand-computable arrays
3. friend feature-contract parity tests
4. split membership/count test
5. seed uniqueness/determinism test
6. collector import/CLI `--help`

Do not instantiate SimVLA or LIBERO in Stage 2 except lightweight registry/source inspection needed for Part A/B.

# Git

Commit only source/tests/docs, no outputs or large assets.

Commit message exactly:

`feat(sam): build corrected Goal-Object H10 Mimic-head collector`

Push the experiment branch.

# Return only

ASSET_PARITY:
checkpoint_found:
checkpoint_path:
checkpoint_sha_match:
normalization_path:
normalization_sha_match:
simvla_root:
simvla_git_head_match:
libero_pro_root:
goal_object_tasks_0_9:
init_states_min_per_task:

ROTATION_SEMANTICS:
representation:
source_path:
function:
line_range:

ADAPTER_TESTS:
passed:
count:

DENOISING_METRIC_TESTS:
passed:
count:
metric_space:

FRIEND_FEATURE_PARITY:
passed:
scalar_shape:
horizon_shape:

COLLECTOR:
path:
sha256:

STATIC_TESTS:
passed:
count:

ROLLOUT_LAUNCHED:
NO

COMMIT:
<sha/NONE>

HARD1000_TOUCHED:
NO
