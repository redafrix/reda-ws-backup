# 003 - OpenPI Pi0.5 DROID Checkpoint in Isaac

## Purpose

Run the official OpenPI `pi05_droid` checkpoint in the IsaacLab tabletop setup as a separate experiment from Pi0.5 LIBERO, so both can be rerun independently later.

## Why Separate From LIBERO

DROID and LIBERO use different OpenPI interfaces:

- Pi0.5 LIBERO uses `observation/image`, `observation/wrist_image`, and an 8D state.
- Pi0.5 DROID uses `observation/exterior_image_1_left`, `observation/wrist_image_left`, `observation/joint_position`, and `observation/gripper_position`.
- Pi0.5 DROID actions are treated as 7 joint velocity commands plus 1 gripper command, not LIBERO-style Cartesian deltas.

## Checkpoint And Server

Wrapper:

- `isaac_pi05_work/run_pi05_droid_server_bob.sh`

Known server config from wrapper:

- OpenPI root: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi`
- OpenPI env: `/home/rootalkhatib/pi05_openpi_20260623_env`
- checkpoint: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/openpi-assets/checkpoints/pi05_droid`
- port: `8006`
- policy config: `pi05_droid`

## Runtime Config

Main eval config:

- `isaac_pi05_work/configs/eval_pi05_droid_bob.yaml`

Important settings:

- `action_horizon: 15`
- `action_dim: 8`
- `observation_schema: droid`
- `replan_steps: 8`
- `droid_control_fps: 15.0`
- `joint_velocity_scale_rad_s: 1.0`
- no camera flip

## Implementation Details

Primary edited files:

- `isaac_pi05_work/src/franka_wrist_camera_scene/pi05/runtime.py`
- `isaac_pi05_work/src/franka_wrist_camera_scene/pi05/policy.py`
- `isaac_pi05_work/scripts/pi05_reaching_rollout.py`
- `isaac_pi05_work/scripts/pi05_pick_place_rollout.py`

Key adapter behavior:

- strict schema validation for `libero` and `droid`.
- DROID images resized/padded to `224x224 uint8`.
- DROID joint observation shape: `(7,)`.
- DROID gripper observation shape: `(1,)`.
- DROID output expected shape: `(15, 8)`.
- first 7 action dims are clipped to `[-1, 1]`, scaled as joint velocity, and integrated using `1 / droid_control_fps`.
- 8th action dim controls open/closed gripper threshold.
- DROID joint command wraps a `recorder_command` so episode recording still stores an end-effector pose/action target.

Important bug fixed:

- The rollout initially read `finger_opening_m` directly from `Pi05DroidJointCommand`.
- Correct path is `current_cmd.recorder_command.finger_opening_m`.
- This fix was applied to both reaching and pick-place rollout scripts.

## Rollout Configs

Reaching:

- `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_5ep.yaml`
- output dir on Bob: `data/raw/pi05_droid_reaching_5ep_collection_limit`
- `max_steps: 3600`
- `camera_width: 300`
- `camera_height: 300`
- `camera_fps: 15`
- `state_record_fps: 15`

Pick-place:

- `isaac_pi05_work/configs/eval_pi05_droid_pick_place_bob_5ep.yaml`
- output dir on Bob: `data/raw/pi05_droid_pick_place_5ep_collection_limit`
- `max_steps: 3800`
- `camera_width: 300`
- `camera_height: 300`
- `camera_fps: 15`
- `state_record_fps: 15`

Smoke / repair configs:

- `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_1ep_save_smoke.yaml`
- `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_ep4_plus_dummy_rerun.yaml`
- `isaac_pi05_work/configs/eval_pi05_droid_pick_place_bob_ep4_plus_dummy_rerun.yaml`

## Validation

Smoke validation:

- one 60-step reaching smoke saved a complete episode after fixing DROID gripper-command routing.

Full run:

- 5 reaching episodes completed.
- 5 pick-place episodes completed.
- all 10 were failures at max step limit.
- final episode media had the same last-writer flush problem as LIBERO, so episode 4 plus dummy episode 5 was rerun for both task groups.
- after repair, all 10 per-episode videos were readable and nonblank.

## Local Evidence

Current readable fast video:

- `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4`

Older video copies:

- `vids/old/pi05_droid_10_tests_agent_view_2x.mp4`
- `vids/old/pi05_droid_10_tests_agent_view_4x.mp4`

Video properties checked after final postprocessing:

- resolution: `300x300`
- duration: about `77.33` seconds for `4x_labeled`
- fps: `15`

