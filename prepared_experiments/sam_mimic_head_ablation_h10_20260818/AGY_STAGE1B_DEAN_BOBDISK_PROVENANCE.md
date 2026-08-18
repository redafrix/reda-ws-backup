# Agy Stage 1B — resolve final SimVLA lineage from Dean-mounted Bob disk

The previous Stage 1 stopped correctly because the canonical final paper workspace is not stored on Sam. Historical paths embedded in the final artifacts use `/media/rootalkhatib/My Passport/reda_ws/...`, which was Bob's mount path. The old Bob disk is now mounted on Dean under `/media/redafrix/My Passport` and/or `/media/redafrix/My Passport1`.

## Hard restrictions

- READ ONLY on Dean and both mounted disks.
- DO NOT stop/pause/restart/touch HARD1000.
- DO NOT launch Isaac, LIBERO, SimVLA, training or evaluation.
- DO NOT modify the old Bob disk.
- DO NOT assume `/media/rootalkhatib/...` exists on Dean; translate historical paths only after verifying actual current mount contents.
- DO NOT use the archived June collector as a fallback.

## Independent anchors already established from final raw evidence

The final promoted evidence root is `fiper_ws/cross_suite_official_ood_20260630`.

The final promoted training result identifies source data:
`fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`

The final H10 online run manifests identify the SimVLA uncertainty policy checkpoint historically as:
`fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
with expected `model.safetensors` SHA256:
`3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`

They identify:
- execution_horizon = 10
- SimVLA source root historically `intern_ship_ws/simvla/code/SimVLA_modified`
- normalization historically `intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json`
- SmolVLM snapshot ending `a7da5b986cb59b408707209984f360a5f4ad7e47`

These are validation anchors, not permission to skip source tracing.

## 1. Resolve current Dean mount

On Dean, read only:

`findmnt`
`lsblk -f`

Check exact candidates:

`/media/redafrix/My Passport/reda_ws`
`/media/redafrix/My Passport1/reda_ws`

Find which contains:

`fiper_ws/cross_suite_official_ood_20260630`

Return the exact canonical current path. If both contain it, compute SHA256 for a small immutable anchor such as:

`experiments/train_seen_goal_object_eval_goal_swap_100/results.json`

and report whether the copies are identical.

## 2. Verify final evidence anchors

From the resolved root, verify existence + SHA256 of:

- `experiments/train_seen_goal_object_eval_goal_swap_100/results.json`
- `experiments/train_seen_goal_object_eval_goal_swap_100/normalization.json`
- `experiments/train_seen_goal_object_eval_goal_swap_100/split_episode_ids.json`
- `experiments/eval_promoted_single_model_all_ood_20260701/results.json`
- `models/simvla_h10_topk8_official_goal_object_seen_main_20260701/`
- `source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`

Do not hash the huge JSONL if it is expensive; report size and existing sidecar hash if present.

## 3. Verify actual policy checkpoint

Resolve current path corresponding to historical:

`fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors`

Compute SHA256 and require:

`3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`

If it does not match, STOP and report mismatch.

Also inspect its config files only to verify native H10 / uncertainty-head identity.

## 4. Resolve exact current SimVLA runtime

Resolve current path corresponding to:

`intern_ship_ws/simvla/code/SimVLA_modified`

Record git HEAD if it is a repository; otherwise hash all small Python source files directly involved in:

- model loading
- stochastic flow sampling
- action postprocess
- LIBERO environment adapter

Find the exact function that maps normalized policy action to the 7D LIBERO action and record source path + SHA256.

Verify the normalization file:

`intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json`

Compute SHA256.

## 5. Locate the corrected/latest H10 collection implementation

This is the key task.

Search the resolved old-Bob workspace AND its Git history/source snapshots for the scripts used after the H1/receding mistakes were corrected and that implement the final H10 semantics:

- one policy query generates an H10 main chunk
- stochastic alternatives generated from same observation
- full 10-action prefix executed before next query, except success/done/budget termination
- 300-action LIBERO budget for the matched VLA runs

Use evidence in final run manifests, configs, source snapshots, shell launchers, timestamps and Git history to establish lineage.

Candidate files may include realtime-deployment / online-H10 scripts and later corrected collectors. Do NOT choose based on filename recency alone.

For every candidate, return:
path
sha256
mtime
git commit if available
why it is linked or not linked to final evidence

Select one `authoritative_h10_runtime_source` only if final evidence establishes it.

## 6. Locate final promoted trainer/evaluator lineage

Trace the code that produced:

`train_seen_goal_object_eval_goal_swap_100`

and the promoted model:

`simvla_h10_topk8_official_goal_object_seen_main_20260701`

Then trace the code used by:

`eval_promoted_single_model_all_ood_20260701`

Record source files + SHA256 and any launch command or copied source snapshot.

Use `run_clean_temporal_nextgen_campaign_v2.py` only if the evidence proves it belongs to this lineage; do not assume that merely because it is newer.

## 7. Copy only small authoritative sources into experiment branch

If and only if provenance is complete:

Copy the authoritative small source files, manifests and configs from Dean/old-Bob disk to Sam's clean worktree under:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/source_snapshot/`

Do not copy datasets/checkpoints/large logs.

Create `SOURCE_PROVENANCE.json` with exact current and historical paths, hashes and evidence chain.

Commit/push on:
`experiment/sam-mimic-head-ablation-h10-20260818`

Commit message exactly:
`chore(sam): freeze final H10 SimVLA lineage from Bob archive`

## Return only

PROVENANCE_COMPLETE:
YES/NO

DEAN_MOUNT_RESOLVED:
<path>

SECOND_COPY_IF_ANY:
<path/NONE>
identical:

FINAL_EVIDENCE_ROOT:
<path>

SOURCE_DATA:
<path>

POLICY_CHECKPOINT:
path:
sha256:
expected_sha_match:

SIMVLA_ROOT:
path:
git_head:

NORMALIZATION:
path:
sha256:

ACTION_POSTPROCESS:
path:
function:
sha256:

AUTHORITATIVE_H10_RUNTIME_SOURCE:
path:
sha256:
evidence_link:

TRAINER:
path:
sha256:
evidence_link:

EVALUATOR:
path:
sha256:
evidence_link:

SUPERSEDED_NOT_USED:
<paths>

COMMIT:
<sha/NONE>

HARD1000_TOUCHED:
NO

No interpretation. Stop.
