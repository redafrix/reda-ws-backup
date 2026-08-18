# Isaac Sim Experiment Map

Created: 2026-07-03
Updated: 2026-08-18

This folder is a documentation map for the Isaac Sim / IsaacLab experiments we have run together in this workspace. It does not contain raw rollout data and does not move, rename, or perturb the existing experiment folders.

## Scope

Included here:

- SimVLA basic checkpoint Isaac deployment tests.
- Camera-rotation / no-flip validation for Isaac camera inputs.
- OpenPI Pi0.5 LIBERO checkpoint Isaac deployment tests.
- OpenPI Pi0.5 DROID checkpoint Isaac deployment tests.
- Local combined-video postprocessing and readable task-label fixes.
- Corrected true-H10 SimVLA risk-detector Seen4000, locked OOD150 offline evaluation, definitive active OOD150 controller, and HARD1000 continuation state.

Not included as primary Isaac experiments:

- Older non-Isaac LIBERO-only Stage 5/7/9 uncertainty work, except where it explains checkpoints, preprocessing, or decisions reused for Isaac.
- Remote raw rollout folders on Bob that are not currently copied into this local workspace. Those are referenced by path when known.

## Quick Index

| Experiment | Status | Main Local Evidence | Details |
| --- | --- | --- | --- |
| **Corrected true-H10 SimVLA risk campaign** | **Audited final OOD150; HARD1000 active** | `prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/FINAL_RESULT.json` | [FINAL_ISAAC_RESULTS_20260818.md](FINAL_ISAAC_RESULTS_20260818.md) |
| SimVLA basic, Isaac no-rotation 10 tests | Completed, all failed | `vids/old/simvla_basic_10_tests_agent_view_2x_no_rotation.mp4`; summary JSON still local | [experiments/001_simvla_basic_no_rotation.md](experiments/001_simvla_basic_no_rotation.md) |
| Pi0.5 LIBERO, Isaac 5 reaching + 5 pick-place | Completed, all failed | `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4`; configs under `isaac_pi05_work/configs/` | [experiments/002_pi05_libero_isaac.md](experiments/002_pi05_libero_isaac.md) |
| Pi0.5 DROID, Isaac 5 reaching + 5 pick-place | Completed, all failed | `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4`; DROID configs/scripts under `isaac_pi05_work/` | [experiments/003_pi05_droid_isaac.md](experiments/003_pi05_droid_isaac.md) |
| Combined video speed + readable task labels | Completed | `*_4x_labeled.mp4` files in `vids/` | [experiments/004_video_outputs_and_labels.md](experiments/004_video_outputs_and_labels.md) |

## Corrected True-H10 Headline Numbers

- Seen4000: 4000 episodes, 3908 success / 92 failure, 75,603 decisions.
- V1 validation AUROC/AUPRC: 0.93449 / 0.84945.
- Locked historical OOD150 detector: AUROC/AUPRC 0.91655 / 0.98003; 72 success / 78 failure membership.
- Definitive active OOD150: **75/150** vs historical **72/150**, with **11 rescues / 8 regressions**.
- Active controller: 57 real replacements in 36/150 episodes, 0 selection mismatches, 0 execution mismatches.
- HARD1000 resumed safely from 249 and is ongoing; intermediate counts are not final results.

See [FINAL_ISAAC_RESULTS_20260818.md](FINAL_ISAAC_RESULTS_20260818.md) for provenance and interpretation boundaries.

## Shared Task Sequence

The 10-test Isaac evaluation sequence used by the earlier combined videos is:

| Index | Task Type | Instruction |
| --- | --- | --- |
| 1 | reaching | reach the avocado |
| 2 | reaching | reach the bowl |
| 3 | reaching | reach the basket |
| 4 | reaching | reach the onion |
| 5 | reaching | reach the onion |
| 6 | pick_place | pick up the can and place it in the tray |
| 7 | pick_place | pick up the can and place it in the basket |
| 8 | pick_place | pick up the onion and place it in the tray |
| 9 | pick_place | pick up the onion and place it in the tray |
| 10 | pick_place | pick up the kiwi and place it in the basket |

## Important Decisions

- No image flipping is used for Isaac camera inputs. IsaacLab camera images are already upright for these deployment tests.
- LIBERO camera flipping is treated as a LIBERO-specific correction because LIBERO observations are inverted relative to normal visual input.
- Reaching failure limit follows the collection config: `3600` steps for the earlier deployment tests. The corrected true-H10 risk workspace uses its own frozen 2400-step contract and must not be mixed with those older tests.
- Pick-place failure limit follows the collection config: `3800` steps in the earlier deployment tests.
- Pi0.5 DROID is handled separately from Pi0.5 LIBERO because DROID expects a different observation schema and joint-space action convention.
- Episode-4-plus-dummy rerun configs exist because the final episode media writer can leave the last episode MP4/rgb incomplete on shutdown; rerunning episode 4 plus disposable episode 5 forces episode 4 to flush.
- For the corrected true-H10 campaign, the V1 model is a main/current-proposal risk detector with multi-sample disagreement context; do not describe it as trained on nine independently supervised candidate outcomes.
- The definitive online cap `C=0.9` is engineering-development-informed from preserved live OOD-development decisions, so the final OOD150 run is not a pristine untouched tuning holdout.

## Files In This Map

- [FINAL_ISAAC_RESULTS_20260818.md](FINAL_ISAAC_RESULTS_20260818.md)
- [experiments/001_simvla_basic_no_rotation.md](experiments/001_simvla_basic_no_rotation.md)
- [experiments/002_pi05_libero_isaac.md](experiments/002_pi05_libero_isaac.md)
- [experiments/003_pi05_droid_isaac.md](experiments/003_pi05_droid_isaac.md)
- [experiments/004_video_outputs_and_labels.md](experiments/004_video_outputs_and_labels.md)
- [inventory/artifacts.md](inventory/artifacts.md)
- [inventory/experiment_index.json](inventory/experiment_index.json)
- [rerun_notes.md](rerun_notes.md)
