# Verified Pipeline Status

Known-good baseline status:

## Setup
- Workspace: /home/redafrix/tests/internship/isaac_dynamicVLA-test
- Isaac Sim symlink: /home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim
- Isaac Lab: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab
- DynamicVLA repo: /home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla

## Verified pipeline
- Raw scripted data collection works using DynamicVLA `simulations/simulate.py`.
- Translation works using DynamicVLA `scripts/translate_dataset_seq.py`.
- Headless mode is verified and preferred.
- Multicam videos from H5 data were generated successfully.

## Stage 3 minimal compatibility patch
The repo needed a tiny compatibility patch:
- remove extra `args.timeout` from `get_test_env(...)` call in:
  - `scripts/translate_dataset_seq.py`
  - `scripts/replay_dataset_seq.py`

## Stage 4 controlled validation
- Raw H5 count: 10
- Translated H5 count: 9
- Multicam MP4 count: 20

## Important warning
This checkpoint is the working baseline.
Do not modify it directly.
Future experiments must happen under:
`/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods`
