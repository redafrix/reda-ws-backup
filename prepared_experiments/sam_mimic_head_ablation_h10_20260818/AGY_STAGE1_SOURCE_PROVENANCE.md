# Agy Stage 1 — source provenance only

This stage is mechanical. Do not design or modify the experiment.

Machine: Sam / PCROBOTUBUNTU05
Clean worktree: `/home/rootalkhatib/test/reda_ws_current_20260818`
Historical workspace: `/home/rootalkhatib/test/reda_ws`
Required branch: `experiment/sam-mimic-head-ablation-h10-20260818`

## Absolute prohibitions

Do not launch LIBERO, SimVLA, training, feature extraction, collection or evaluation.
Do not modify the historical Sam workspace.
Do not use the archived June collector as the implementation base.
Do not infer source provenance from filenames alone.
Do not summarize scientific results.

## Required source-tracing anchors

Use the final canonical promoted-SimVLA evidence, in this order:

1. `fiper_ws/cross_suite_official_ood_20260630`
2. final promoted training run `train_seen_goal_object_eval_goal_swap_100`
3. final promoted OOD run `eval_promoted_single_model_all_ood_20260701`
4. their manifests / results JSON / launch command / code-version fields / copied source snapshots
5. current repository scripts such as `fiper_ws/scripts/run_clean_temporal_nextgen_campaign_v2.py` only when the final artifacts prove they are part of the valid lineage

The goal is to find the exact latest corrected code used after earlier collection/training mistakes were fixed.

## Deliverables

Create under the new clean worktree only:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/source_snapshot/`

Copy verbatim every small source file that the final evidence identifies as authoritative for:

- Goal-Object H10 collection/runtime
- SimVLA policy inference / stochastic candidate generation
- action postprocessing / 7D LIBERO adapter
- environment reset / success detection
- dataset materialization / split handling
- promoted risk-head training
- promoted risk-head evaluation / threshold computation

Do not copy large datasets, checkpoints or outputs.

Create `SOURCE_PROVENANCE.json` containing raw factual fields only:

- canonical_evidence_root
- promoted_train_run_root
- promoted_ood_run_root
- collector_source_path
- collector_sha256
- collector_code_version_if_recorded
- policy_runtime_source_paths_and_sha256
- action_postprocess_source_path_and_sha256
- reset_success_source_path_and_sha256
- dataset_materializer_source_path_and_sha256
- trainer_source_path_and_sha256
- evaluator_source_path_and_sha256
- checkpoint_path
- checkpoint_sha256
- normalization_path
- normalization_sha256
- libero_pro_path
- libero_pro_git_head_if_available
- evidence_files_used_for_resolution (path + sha256)
- older_superseded_collectors_seen (paths only)
- provenance_complete true/false

## Hard source rule

If the final promoted evidence does not identify a trustworthy corrected collector/runtime source, set `provenance_complete=false` and STOP. Do not fall back to `archive/sam-local-preservation-20260818/fiper_ws/scripts/collect_simvla_official_goal_object_uncertainty_20260626.py` merely because it exists.

## Git

Only after provenance is complete:

- add `SOURCE_PROVENANCE.json`
- add the copied small source snapshot files
- commit message exactly:

`chore(sam): freeze corrected SimVLA source lineage for Mimic-head ablation`

- push branch `experiment/sam-mimic-head-ablation-h10-20260818`

## Return only

PROVENANCE_COMPLETE:
YES/NO

CANONICAL_EVIDENCE_ROOT:
<path>

PROMOTED_TRAIN_RUN:
<path>

PROMOTED_OOD_RUN:
<path>

COLLECTOR:
path:
sha256:
code_version:

POLICY_RUNTIME:
<paths + sha256>

ACTION_POSTPROCESS:
path:
sha256:

RESET_SUCCESS:
path:
sha256:

MATERIALIZER:
path:
sha256:

TRAINER:
path:
sha256:

EVALUATOR:
path:
sha256:

CHECKPOINT:
path:
sha256:

NORMALIZATION:
path:
sha256:

LIBERO_PRO:
path:
git_head:

SUPERSEDED_SOURCES_NOT_USED:
<paths>

COMMIT:
<sha or NONE>

No interpretation. Stop.
