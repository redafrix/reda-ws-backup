# LIBERO-PRO `libero_goal_object` Reproduction Bundle (2026-06-05)

This bundle captures the exact environment and episode identities represented by:

- `source_manifests/libero_goal_object_exact_trials0to9_40to49_eval_seed0_20260605.csv`
- `source_manifests/libero_goal_object_exact_trials0to9_40to49_eval_seed0_20260605.json`

It is for reproducing the same LIBERO-PRO `libero_goal_object` episode environments on another machine, so another policy or VLA model can be evaluated on the same tasks and initial states.

## What Was Copied

The bundle contains:

- the two source reproduction manifests;
- both original `collection_protocol.json` files from the completed `goal_object_t0to9` and `goal_object_t40to49` rollout directories;
- the exact 10 BDDL files for `libero_goal_object` task IDs 0-9;
- the exact 10 `.pruned_init` files for those tasks;
- minimal source code showing benchmark registration, task-id mapping, object-substitution generation, prompt selection, evaluator seeding, initial-state selection, and environment reset;
- generated verification tables and provenance metadata.

No model checkpoints, datasets, videos, or rollout arrays are included.

## Original Sources

The local source tree used by the collection was:

```text
/home/utilisateur/worldmodel/LIBERO-PRO
```

The evaluator and launch scripts came from:

```text
/home/utilisateur/worldmodel/mimic-video/eval/libero/run.py
/home/utilisateur/worldmodel/mimic-video/scripts/run_libero_goal_ood_full_uncertainty_collection.sh
/home/utilisateur/worldmodel/mimic-video/scripts/launch_pro_goal_multi_ood_calibrated_100x100.sh
```

The source tree does not contain `.git` metadata on this machine. Therefore the Git commit, dirty status, and remote URL cannot be recovered. Exact byte hashes are recorded for all copied source files, BDDL files, and init files.

## Episode-Generation Contract

Use:

```text
LIBERO implementation: LIBERO-PRO
suite: libero_goal_object
perturbation family: object_substitution_ood
task IDs: 0,1,2,3,4,5,6,7,8,9
initial_state_indices: 0,1,2,3,4,5,6,7,8,9,40,41,42,43,44,45,46,47,48,49
eval_seed: 0
prompt_source: bddl_language
```

The original collection used two independent evaluator invocations:

1. `TRIAL_START_INDEX=0`, `NUM_TRIALS_PER_TASK=10`, `SEED=0`
2. `TRIAL_START_INDEX=40`, `NUM_TRIALS_PER_TASK=10`, `SEED=0`

For stochastic policies, reset the evaluator seed to `0` at the start of each of these two windows. Within each window, the order is task ID ascending, then initial-state index ascending.

The exact episode identity is:

```text
(libero_impl, task_suite_name, task_id, initial_state_index, eval_seed)
```

The file `verification/episode_identity_table.csv` has exactly 200 rows in the order used by the original completed runs.

## Prompt Contract

The collection used `prompt_source=bddl_language`. The prompt is obtained from each BDDL file's `(:language ...)` field. Some raw LIBERO registration language strings are derived from filenames and differ slightly from the BDDL language, for example "drawer" versus "layer of the drawer". For this bundle, BDDL language is the authority because that is what the evaluator passed to the policy.

## What Is Guaranteed Identical

This bundle is intended to guarantee:

- same task suite and task IDs;
- same BDDL bytes;
- same object-substitution OOD assets already materialized in those BDDL files;
- same `.pruned_init` bytes;
- same initial-state indices;
- same evaluator-level seed contract;
- same BDDL language prompts;
- same task and episode ordering.

## What Is Not Covered

This bundle intentionally does not guarantee policy-dependent behavior such as:

- model weights or checkpoints;
- diffusion horizon or replanning frequency;
- action execution horizon, e.g. executing 14 actions versus replanning every action;
- GPU nondeterminism inside a policy;
- success/failure parity for a different model.

The reference world-model success labels are present only as provenance in the source manifests. They must not be used to select or filter episodes for a new model comparison.

## Verification

From the bundle root, run:

```bash
python verification/verify_bundle.py
```

The verifier checks SHA-256 hashes, 200 unique episode identities, task IDs 0-9, state indices 0-9 and 40-49 for every task, eval seed 0, BDDL/init presence, init-state counts, prompt agreement with BDDL language, and missing references.
