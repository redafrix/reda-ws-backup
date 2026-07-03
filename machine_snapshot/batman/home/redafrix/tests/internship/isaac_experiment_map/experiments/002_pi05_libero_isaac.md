# 002 - OpenPI Pi0.5 LIBERO Checkpoint in Isaac

## Purpose

Run the official OpenPI `pi05_libero` checkpoint in the IsaacLab tabletop setup using the same 10-test task structure:

- 5 reaching episodes.
- 5 pick-place episodes.

## Checkpoint And Server

Wrapper:

- `isaac_pi05_work/run_pi05_libero_server_bob.sh`

Known server config from wrapper:

- OpenPI root: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi`
- OpenPI env: `/home/rootalkhatib/pi05_openpi_20260623_env`
- checkpoint: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/pi05_libero`
- port: `8005`
- policy config: `pi05_libero`

## Runtime Config

Main eval config:

- `isaac_pi05_work/configs/eval_pi05_libero_bob.yaml`

Important settings:

- `action_horizon: 10`
- `action_dim: 7`
- `replan_steps: 10`
- `translation_scale_m: 0.05`
- `rotation_scale_rad: 0.5`
- no camera flip

## Rollout Configs

Reaching:

- `isaac_pi05_work/configs/eval_pi05_reaching_bob_5ep.yaml`
- output dir on Bob: `data/raw/pi05_libero_reaching_5ep_collection_limit`
- `max_steps: 3600`
- `camera_width: 300`
- `camera_height: 300`
- `camera_fps: 20`
- `state_record_fps: 20`

Pick-place:

- `isaac_pi05_work/configs/eval_pi05_pick_place_bob_5ep.yaml`
- output dir on Bob: `data/raw/pi05_libero_pick_place_5ep_collection_limit`
- `max_steps: 3800`
- `camera_width: 300`
- `camera_height: 300`
- `camera_fps: 20`
- `state_record_fps: 20`

Smoke / repair configs:

- `isaac_pi05_work/configs/eval_pi05_reaching_bob_1ep_save_smoke.yaml`
- `isaac_pi05_work/configs/eval_pi05_reaching_bob_1ep_smoke.yaml`
- `isaac_pi05_work/configs/eval_pi05_reaching_bob_ep4_rerun.yaml`
- `isaac_pi05_work/configs/eval_pi05_reaching_bob_ep4_plus_dummy_rerun.yaml`
- `isaac_pi05_work/configs/eval_pi05_pick_place_bob_ep4_rerun.yaml`
- `isaac_pi05_work/configs/eval_pi05_pick_place_bob_ep4_plus_dummy_rerun.yaml`

## Result

All 10 rollout tests completed and all were failures at the configured collection-length limit:

- reaching failures at `3600` steps.
- pick-place failures at `3800` steps.

The final episode media writer showed a last-episode flush/corruption issue. The fix was to rerun episode 4 plus a disposable episode 5, then delete episode 5 and rebuild the combined video.

## Local Evidence

Current readable fast video:

- `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4`

Older video copies:

- `vids/old/pi05_libero_10_tests_agent_view_2x.mp4`
- `vids/old/pi05_libero_10_tests_agent_view_4x.mp4`

Video properties checked after final postprocessing:

- resolution: `300x300`
- duration: about `77.25` seconds for `4x_labeled`
- fps: `20`

