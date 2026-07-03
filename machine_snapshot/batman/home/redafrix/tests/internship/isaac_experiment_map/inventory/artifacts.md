# Isaac Artifact Inventory

This inventory lists known local artifacts for the recent Isaac work. Paths are relative to `/home/redafrix/tests/internship` unless absolute.

## Final Local Videos

| Path | Meaning |
| --- | --- |
| `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4` | Final readable fast DROID combined video |
| `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4` | Final readable fast LIBERO combined video |

## Archived / Older Local Videos

| Path | Meaning |
| --- | --- |
| `vids/old/pi05_droid_10_tests_agent_view_2x.mp4` | Older DROID combined video |
| `vids/old/pi05_droid_10_tests_agent_view_4x.mp4` | Older DROID faster unlabeled video |
| `vids/old/pi05_libero_10_tests_agent_view_2x.mp4` | Older LIBERO combined video |
| `vids/old/pi05_libero_10_tests_agent_view_4x.mp4` | Older LIBERO faster unlabeled video |
| `vids/old/simvla_basic_10_tests_agent_view_2x_no_rotation.mp4` | SimVLA basic no-rotation combined video |

## SimVLA Local Evidence

| Path | Meaning |
| --- | --- |
| `vids/simvla_basic_10_tests_agent_view_2x_no_rotation_summary.json` | Summary for SimVLA 10-test Isaac run |
| `vids/simvla_paper_reaching_dense_smoke_no_rotation_videos/` | no-rotation camera input smoke videos |
| `vids/simvla_paper_reaching_dense_smoke_videos/` | rotate-180 camera comparison smoke videos |

## Pi0.5 Configs

| Path | Meaning |
| --- | --- |
| `isaac_pi05_work/configs/eval_pi05_libero_bob.yaml` | LIBERO policy server/client shape config |
| `isaac_pi05_work/configs/eval_pi05_reaching_bob_5ep.yaml` | LIBERO reaching 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_pick_place_bob_5ep.yaml` | LIBERO pick-place 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_reaching_bob_ep4_plus_dummy_rerun.yaml` | LIBERO reaching repair config |
| `isaac_pi05_work/configs/eval_pi05_pick_place_bob_ep4_plus_dummy_rerun.yaml` | LIBERO pick-place repair config |
| `isaac_pi05_work/configs/eval_pi05_droid_bob.yaml` | DROID policy server/client shape config |
| `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_5ep.yaml` | DROID reaching 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_droid_pick_place_bob_5ep.yaml` | DROID pick-place 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_ep4_plus_dummy_rerun.yaml` | DROID reaching repair config |
| `isaac_pi05_work/configs/eval_pi05_droid_pick_place_bob_ep4_plus_dummy_rerun.yaml` | DROID pick-place repair config |

## Pi0.5 Scripts

| Path | Meaning |
| --- | --- |
| `isaac_pi05_work/run_pi05_libero_server_bob.sh` | starts OpenPI `pi05_libero` server on Bob |
| `isaac_pi05_work/run_pi05_droid_server_bob.sh` | starts OpenPI `pi05_droid` server on Bob |
| `isaac_pi05_work/run_pi05_reaching_rollout.sh` | LIBERO reaching rollout wrapper |
| `isaac_pi05_work/run_pi05_pick_place_rollout.sh` | LIBERO pick-place rollout wrapper |
| `isaac_pi05_work/run_pi05_droid_reaching_rollout.sh` | DROID reaching rollout wrapper |
| `isaac_pi05_work/run_pi05_droid_pick_place_rollout.sh` | DROID pick-place rollout wrapper |
| `isaac_pi05_work/scripts/pi05_reaching_rollout.py` | shared reaching rollout implementation |
| `isaac_pi05_work/scripts/pi05_pick_place_rollout.py` | shared pick-place rollout implementation |
| `isaac_pi05_work/scripts/create_pi05_combined_agent_video.py` | combined video builder from raw episode folders |

## Remote Raw Output Paths

These paths were used on Bob and are recorded here for rerun/reference. They may not exist locally.

| Path | Meaning |
| --- | --- |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_libero_reaching_5ep_collection_limit` | LIBERO reaching raw episodes |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_libero_pick_place_5ep_collection_limit` | LIBERO pick-place raw episodes |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_droid_reaching_5ep_collection_limit` | DROID reaching raw episodes |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_droid_pick_place_5ep_collection_limit` | DROID pick-place raw episodes |

