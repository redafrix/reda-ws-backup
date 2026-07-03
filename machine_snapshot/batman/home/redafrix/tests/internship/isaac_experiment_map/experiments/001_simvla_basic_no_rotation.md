# 001 - SimVLA Basic Isaac No-Rotation Tests

## Purpose

Test the basic SimVLA checkpoint in Isaac using the same deployment task families as the real data-collection scripts: reaching and pick-place.

## Camera Decision

No camera flip was used for the Isaac deployment. The conclusion used for this run was:

- SimVLA wants normal-looking visual input.
- LIBERO needs image flipping because LIBERO observations arrive inverted.
- IsaacLab cameras in this setup are already correct, so flipping would be wrong.

## Episode Setup

The local summary file records 10 episodes:

- 5 reaching episodes.
- 5 pick-place episodes.
- All episodes were marked `success: false`.
- Each summary entry has `134` frames, `6.7` source seconds, and `3.35` seconds after the 2x summary-video speedup.

## Episode List

| Index | Episode | Task | Instruction | Success | Local Summary Root |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | reaching | reach the avocado | false | `data/raw/simvla_paper_reaching_5ep_no_rotation_800/000000` |
| 2 | 1 | reaching | reach the bowl | false | `data/raw/simvla_paper_reaching_5ep_no_rotation_800/000001` |
| 3 | 2 | reaching | reach the basket | false | `data/raw/simvla_paper_reaching_5ep_no_rotation_800/000002` |
| 4 | 3 | reaching | reach the onion | false | `data/raw/simvla_paper_reaching_5ep_no_rotation_800/000003` |
| 5 | 4 | reaching | reach the onion | false | `data/raw/simvla_paper_reaching_5ep_no_rotation_800/000004` |
| 6 | 0 | pick_place | pick up the can and place it in the tray | false | `data/raw/simvla_paper_pick_place_5ep_no_rotation_800/000000` |
| 7 | 1 | pick_place | pick up the can and place it in the basket | false | `data/raw/simvla_paper_pick_place_5ep_no_rotation_800/000001` |
| 8 | 2 | pick_place | pick up the onion and place it in the tray | false | `data/raw/simvla_paper_pick_place_5ep_no_rotation_800/000002` |
| 9 | 3 | pick_place | pick up the onion and place it in the tray | false | `data/raw/simvla_paper_pick_place_5ep_no_rotation_800/000003` |
| 10 | 4 | pick_place | pick up the kiwi and place it in the basket | false | `data/raw/simvla_paper_pick_place_5ep_no_rotation_800/000004` |

## Local Evidence

- Summary: `vids/simvla_basic_10_tests_agent_view_2x_no_rotation_summary.json`
- Original combined video currently archived under: `vids/old/simvla_basic_10_tests_agent_view_2x_no_rotation.mp4`
- Camera-rotation smoke videos:
  - `vids/simvla_paper_reaching_dense_smoke_no_rotation_videos/simvla_agent_input_no_rotation.mp4`
  - `vids/simvla_paper_reaching_dense_smoke_no_rotation_videos/simvla_wrist_input_no_rotation.mp4`
  - `vids/simvla_paper_reaching_dense_smoke_no_rotation_videos/simvla_rotation_decision_grid.mp4`
  - older rotate-180 comparison folder: `vids/simvla_paper_reaching_dense_smoke_videos/`

## Notes

The summary roots are remote/run-relative paths and may not exist locally now. This map preserves the intended locations and the local summary evidence.

