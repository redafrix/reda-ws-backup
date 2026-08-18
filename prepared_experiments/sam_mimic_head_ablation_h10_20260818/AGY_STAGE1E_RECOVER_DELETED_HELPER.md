# Agy Stage 1E — recover deleted final H10 helper exactly

Purpose: recover the exact bytes of the helper imported by the final corrected H10 runner before reconstructing or adapting any runtime code.

Known final runner:
`prepared_experiments/sam_mimic_head_ablation_h10_20260818/source_snapshot/online_gate_micro_ablation_20260709.py`

Known import target:
`collect_fiper_uncertainty_receding_dean_v1.py`

Historical path embedded in final runner:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/collect_fiper_uncertainty_receding_dean_v1.py`

Current old-Bob disk root on Dean:
`/media/redafrix/My Passport1/reda_ws`

## Absolute prohibitions

- Do not launch LIBERO or SimVLA.
- Do not train.
- Do not modify Dean/HARD1000.
- Do not reconstruct the helper yet.
- Do not substitute a similarly named script.
- Do not trust filename dates as proof of lineage.
- Do not use `git fsck --lost-found` because it writes files.
- Do not change the old Bob disk.

## 1. Working-tree and filesystem search

READ ONLY search the following roots for the exact basename and for unique imported symbols:

- `/media/redafrix/My Passport1/reda_ws`
- `/media/redafrix/My Passport/reda_ws` if present
- `/home/redafrix/tests/internship`
- Sam historical workspace `/home/rootalkhatib/test/reda_ws`
- Sam clean workspace `/home/rootalkhatib/test/reda_ws_current_20260818`

Search exact basename:
`collect_fiper_uncertainty_receding_dean_v1.py`

Also search text content containing ALL or several of these symbols:
`DEAN_CKPT_60K`, `DEAN_LIBERO_PRO_ROOT`, `DEAN_NORM_STATS`, `DEAN_SIMVLA_ROOT`, `DEAN_SMOLVLM_CACHE`, `UNCERTAINTY_49D_KEYS`, `ImagePreprocessor`, `check_success`, `load_state_stats`, `make_env`, `obs_images`, `obs_to_proprio`, `quat2axisangle`, `reset_to_init`, `setup_runtime`, `sha256_file`.

For every candidate file return path, size, SHA256, and exact set of matching symbols.

## 2. Search old Bob Git history by path

Find the Git repository root corresponding to `/media/redafrix/My Passport1/reda_ws`.

READ ONLY run equivalent Git queries:

- `git log --all --full-history --name-status -- asynchvla_ws/src/data_collection_stage9/collect_fiper_uncertainty_receding_dean_v1.py`
- `git rev-list --all --objects | grep -F 'collect_fiper_uncertainty_receding_dean_v1.py'`
- search all refs for any object/path under `asynchvla_ws/src/data_collection_stage9/`

If the path exists in any commit/tree, extract it with `git show <commit>:<path>` to `/tmp` ONLY, compute SHA256 and size, and compare its imported/exported symbols against the final runner expectations.

Do not checkout or reset any branch.

## 3. Search unreachable Git objects read-only

If normal refs fail, run `git fsck --unreachable --no-reflogs` WITHOUT `--lost-found`.

Inspect unreachable blob objects <= 1 MB by streaming them with `git cat-file blob <sha>` and searching for the distinctive symbol set above.

Do not write recovered blobs anywhere except `/tmp` after a positive content match.

For each positive blob return Git object SHA, content SHA256, size and matching symbols.

## 4. Search archives/backups on preserved disks

READ ONLY identify archive files under the old Bob/Dean workspace whose names or directories plausibly contain source backups:

extensions: `.zip`, `.tar`, `.tar.gz`, `.tgz`, `.7z`

Do not extract large archives wholesale.
Use archive listing first.
Search listings for:

- `collect_fiper_uncertainty_receding_dean_v1.py`
- `data_collection_stage9`

If found, extract ONLY the matching small source file to `/tmp`, hash it, and report archive path + member path + SHA256.

## 5. Search shell history / logs / manifests for copy provenance

READ ONLY search small text/log/manifest files under the old Bob workspace and current experiment catalog for references to:

`collect_fiper_uncertainty_receding_dean_v1.py`

Return context showing whether the helper was copied, generated, renamed or sourced from another machine/repo. Do not infer beyond literal evidence.

## 6. Exact-match acceptance rule

A recovered file is accepted as the authoritative helper only if:

1. it contains the symbols imported by the final runner;
2. its constants resolve the same checkpoint / SimVLA root / normalization family as the final H10 run, or the historical mount-path equivalent;
3. its runtime semantics are compatible with the final runner’s H10 execution path;
4. there is direct provenance evidence tying it to the old Bob/final H10 workspace.

Do not accept a merely similar helper.

## 7. If exact helper is recovered

Copy its bytes unchanged into:

`prepared_experiments/sam_mimic_head_ablation_h10_20260818/source_snapshot/collect_fiper_uncertainty_receding_dean_v1.py`

Update `SOURCE_PROVENANCE_FINAL.json` with:

- helper_source_kind: working_tree / git_history / unreachable_blob / archive
- original_location_or_object
- helper_sha256
- helper_size
- direct_provenance_evidence

Then commit and push with exact message:

`chore(sam): recover exact final H10 runtime helper`

## 8. If exact helper is NOT recovered

Do not reconstruct it in this stage.
Create no runtime code.
Return `HELPER_EXACT_RECOVERY=NO` and stop.

## Return only

HELPER_EXACT_RECOVERY:
YES/NO

WORKING_TREE_MATCHES:
<path | sha256 | size | symbols, or NONE>

GIT_HISTORY_MATCHES:
<commit/object/path | sha256 | size | symbols, or NONE>

UNREACHABLE_BLOB_MATCHES:
<object | sha256 | size | symbols, or NONE>

ARCHIVE_MATCHES:
<archive | member | sha256 | size, or NONE>

PROVENANCE_REFERENCES:
<literal references, or NONE>

ACCEPTED_HELPER:
path/source:
sha256:
size:
source_kind:

SOURCE_PROVENANCE_UPDATED:
YES/NO

COMMIT:
<sha/NONE>

NO_ROLLOUT_LAUNCHED:
YES

HARD1000_TOUCHED:
NO
