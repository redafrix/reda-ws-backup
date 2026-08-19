# 005 - xVLA LIBERO Checkpoint in Isaac

## Purpose

Run the official LeRobot `lerobot/xvla-libero` checkpoint in the IsaacLab tabletop setup using the same reaching and pick-place task families as the collection rollouts.

## Status

Implementation repaired and smoke-validated on Bob on 2026-07-06.

The earlier Agy/Gemini session summary that claimed a full 5 reaching + 5 pick-place run was not reliable. Bob did not contain the claimed pick-place raw output folder, and the implementation it left behind mixed manual preprocessing, `json_numpy`, and delta-style action decoding that did not match the official LeRobot xVLA path.

## Checkpoint And Server

Policy server:
- Remote repo: `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab`
- Script: `scripts/xvla_server.py`
- Wrapper: `./run_xvla_server_bob.sh`
- Python env: `/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0`
- Model ID: `lerobot/xvla-libero`
- Port: `8007`

Current server session used for validation:
- tmux: `xvla_fixed_server_20260706`
- log: `logs_xvla_fixed_server_20260706.log`

## Correct Adapter Behavior

The fixed server uses the installed LeRobot xVLA processors instead of manually recreating the data path:
- `LiberoProcessorStep`
- `TokenizerProcessorStep` with Hub-compatible `tokenizer_max_length=50`
- `XVLAImageToFloatProcessorStep`
- `XVLAImageNetNormalizeProcessorStep`
- `XVLAAddDomainIdProcessorStep(domain_id=3)`
- `DeviceProcessorStep`
- `NormalizerProcessorStep`
- postprocess with `UnnormalizerProcessorStep` and `XVLARotation6DToAxisAngleProcessorStep`

The rollout client sends plain JSON lists. It does not use `json_numpy`, because monkey-patching JSON broke Isaac/NumPy/Scipy imports.

The server builds the LIBERO-style robot state expected by LeRobot:
- `observation.robot_state.eef.pos`
- `observation.robot_state.eef.mat`

State is converted from Isaac world frame into robot-base frame before xVLA. The postprocessed absolute LIBERO action is converted back into Isaac world-frame `PolicyCommand` targets.

Camera handling:
- Isaac camera frames are already visually upright.
- LeRobot's `LiberoProcessorStep` flips only `observation.images.image` for LIBERO.
- To keep the net xVLA input upright for Isaac, the server pre-compensates the agent camera by 180 degrees before `LiberoProcessorStep`.
- Wrist camera is not pre-rotated.

## Runtime Configs

Main eval configs:
- `configs/eval_xvla_libero_bob.yaml`
- `configs/eval_xvla_reaching_bob_5ep.yaml`
- `configs/eval_xvla_pick_place_bob_5ep.yaml`

Wrappers:
- `./run_xvla_reaching_rollout.sh`
- `./run_xvla_pick_place_rollout.sh`

## Validation Evidence

Server health:
- `GET /health` returned status `ok`
- model: `lerobot/xvla-libero`
- device: `cuda`
- `uses_lerobot_processors: true`
- `precompensate_agent_rotation: true`

Synthetic server request:
- `POST /reset` succeeded
- `POST /step` succeeded and returned plain JSON with `target_pos_w`, `target_quat_wxyz`, `gripper_action`, and `finger_opening_m`

Isaac smoke rollouts:
- Reaching smoke output: `data/raw/xvla_libero_reaching_1ep_smoke_fixed/000000`
- Pick-place smoke output: `data/raw/xvla_libero_pick_place_1ep_smoke_fixed/000000`
- Both produced `agent_camera.mp4`, `rgb.npz`, `trajectory.npz`, `meta.json`, and `failure.json`
- Both reached successful server `/step` calls and stopped as task failures, not integration crashes

Smoke commands used on Bob:

```bash
cd /home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab
./run_xvla_reaching_rollout.sh --rollout_config /tmp/eval_xvla_reaching_fixed_1ep_smoke.yaml --headless --device cpu --rendering_mode performance
./run_xvla_pick_place_rollout.sh --rollout_config /tmp/eval_xvla_pick_place_fixed_1ep_smoke.yaml --headless --device cpu --rendering_mode performance
```

## Notes For Future Full Runs

Use the repaired server and wrappers above. Do not reuse the old manual xVLA action decoder, do not add `json_numpy.patch()` to Isaac rollout scripts, and do not interpret the old 5+5 Agy summary as validated evidence.
