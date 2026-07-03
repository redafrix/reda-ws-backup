# DynamicVLA Working Baseline Checkpoint — Stage 4

Date: 2026-06-11

This checkpoint marks the known-good working state of the DynamicVLA scripted data-collection pipeline.

Verified:
- Official assets present.
- Scripted raw collection works.
- Translation/replay works after minimal compatibility patch.
- Multicam videos generated and visually inspected.
- Headless execution is the preferred/default mode.
- Single Isaac instance rule must be respected before every future Isaac launch.

This checkpoint does not duplicate huge datasets/assets/videos.
It stores paths, manifests, diffs, checksums, and small copies of critical scripts/configs.

Do not modify this checkpoint.
Future experiments must happen in:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods
