# Restore Guide — Stage 4 Working Baseline

This checkpoint does not contain huge datasets/assets/videos.
It records the known-good state and paths.

## To return to this baseline mentally
Use:
- Workspace map: `/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/WORKSPACE_MAP.md`
- Git diff: `/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/PATCH_STAGE3_COMPATIBILITY.diff`
- Verified status: `/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/VERIFIED_STATUS.md`
- Dataset manifests:
  - `DATASETS_MANIFEST.tsv`
  - `TRANSLATED_DATASETS_MANIFEST.tsv`
  - `VIDEOS_MANIFEST.tsv`

## To restore the minimal repo compatibility patch
From:
`/home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla`

Apply:
```bash
git apply "/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/PATCH_STAGE3_COMPATIBILITY.diff"
```

## To compare current files with checkpoint copies
```bash
diff -u "/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/baseline_small_files/dynamic-vla/scripts/translate_dataset_seq.py" "/home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla/scripts/translate_dataset_seq.py"
diff -u "/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/baseline_small_files/dynamic-vla/scripts/replay_dataset_seq.py" "/home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla/scripts/replay_dataset_seq.py"
diff -u "/home/redafrix/tests/internship/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/baseline_small_files/dynamic-vla/simulations/simulate.py" "/home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla/simulations/simulate.py"
```

## Important future rule
Do not modify this baseline directly.
All future modifications must be done inside:
`/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods`

## Isaac launch rules for future work
- Always use headless mode by default.
- Always check/kill stale Isaac/Kit/Omniverse processes before launching.
- Never run two Isaac instances at the same time.
