# 004 - Combined Video Speed And Task Labels

## Purpose

Create compact videos that are easy to inspect quickly and have readable task labels.

## Outputs

Current final videos:

- `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4`
- `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4`

Older unlabeled/intermediate copies:

- `vids/old/pi05_droid_10_tests_agent_view_2x.mp4`
- `vids/old/pi05_droid_10_tests_agent_view_4x.mp4`
- `vids/old/pi05_libero_10_tests_agent_view_2x.mp4`
- `vids/old/pi05_libero_10_tests_agent_view_4x.mp4`
- `vids/old/simvla_basic_10_tests_agent_view_2x_no_rotation.mp4`

## Speed

The final labeled videos are approximately half the duration of the previous `2x` videos:

- DROID `4x_labeled`: about `77.33` seconds.
- LIBERO `4x_labeled`: about `77.25` seconds.

## Label Fix

The first labeled attempt used a single-line label, but at `300x300` it clipped long pick-place text. The corrected final videos use:

- full-width black top banner.
- two-line label.
- first line: task index and task type.
- second line: object/target instruction, for example `can to tray`.

Visual spot checks were made on extracted frames around the pick-place segment to confirm labels fit and are readable.

## Rebuild Method

The fast labeled videos were produced from existing `4x` MP4s with `ffmpeg` drawbox/drawtext overlays. No raw experiment folders were modified.

