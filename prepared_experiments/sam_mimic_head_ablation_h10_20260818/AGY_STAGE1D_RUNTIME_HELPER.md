# Agy Stage 1D — freeze the exact helper imported by the final H10 runner

Purpose: complete source provenance before adapting any collector.

Machine roles:
- Dean old Bob disk: READ ONLY
- Sam clean worktree: writable only inside the prepared experiment folder

Do NOT launch LIBERO, SimVLA, training or evaluation.
Do NOT touch HARD1000.
Do NOT use the old June collector as a fallback.

## Verified final runner

Exact final H10 runner:

`/media/redafrix/My Passport1/reda_ws/fiper_ws/cross_suite_official_ood_20260630/scripts/online_gate_micro_ablation_20260709.py`

SHA256:

`c7ebe368d4b14272eceb063cf3bfbf198fd56475abc2bbbec66f7e86ae744351`

The runner itself hardcodes the collector directory and imports:

`collect_fiper_uncertainty_receding_dean_v1`

from historical path:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9`

On Dean the corresponding preserved root is expected under:

`/media/redafrix/My Passport1/reda_ws/asynchvla_ws/src/data_collection_stage9`

## 1. Locate exact imported helper

READ ONLY check:

`/media/redafrix/My Passport1/reda_ws/asynchvla_ws/src/data_collection_stage9/collect_fiper_uncertainty_receding_dean_v1.py`

If present, compute SHA256 and size.

Also identify every local project module imported by this helper that is required by the functions used by the final runner, especially:

- `ImagePreprocessor`
- `check_success`
- `load_state_stats`
- `make_env`
- `obs_images`
- `obs_to_proprio`
- `quat2axisangle`
- `reset_to_init`
- `setup_runtime`
- `sha256_file`

Do not include dependencies that are only used by unrelated standalone collection entry points unless imported runtime behavior requires them.

## 2. Verify that this helper is actually the one resolved by the final runner

Mechanically reproduce the runner path ordering using the preserved paths, without executing a rollout.

Resolve `importlib.util.find_spec("collect_fiper_uncertainty_receding_dean_v1")` under an equivalent `sys.path` ordering and return the resolved file.

Require the resolved file to equal the preserved helper path above.

## 3. Freeze helper and required small local dependencies

Copy bytes unchanged into:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/source_snapshot/`

At minimum copy:

- `collect_fiper_uncertainty_receding_dean_v1.py`

and any small local helper module required for the exact runtime functions used by the final runner.

Do not copy datasets/checkpoints/outputs/binaries.

Update `SOURCE_PROVENANCE_FINAL.json` with:

- `runtime_helper`
- `runtime_helper_sha256`
- `runtime_helper_resolved_by_final_runner: true/false`
- `runtime_helper_dependencies` list of `{path, sha256}`

## 4. Static semantic report

From the exact helper + final runner, report mechanically:

- official Goal-Object benchmark/suite identifier supported by helper
- number of candidate action dimensions
- `model.num_actions` used as H proposal length
- denoising-step implementation location
- image preprocessing shape/cameras
- reset/warmup behavior
- success-check function behavior
- whether the final runner generates nominal candidate 0 separately from alternative candidates
- whether final runner executes `execution_horizon` actions from the selected H10 chunk
- exact candidate seed-generation function name

No scientific interpretation.

## 5. Git

Commit only the provenance/helper snapshot changes on:

`experiment/sam-mimic-head-ablation-h10-20260818`

Commit message exactly:

`chore(sam): freeze final H10 runtime helper dependency`

Push.

## Return only

HELPER_FOUND:
YES/NO

HELPER:
path:
sha256:
size:
resolved_by_final_runner:

DEPENDENCIES:
<path + sha256>

STATIC_SEMANTICS:
official_goal_object_identifier:
action_dim:
proposal_horizon_source:
denoising_loop:
image_preprocess:
reset_warmup:
success_check:
main_generated_separately:
execution_horizon_loop:
seed_function:

SOURCE_PROVENANCE_UPDATED:
YES/NO

COMMIT:
<sha/NONE>

NO_ROLLOUT_LAUNCHED:
YES

HARD1000_TOUCHED:
NO
