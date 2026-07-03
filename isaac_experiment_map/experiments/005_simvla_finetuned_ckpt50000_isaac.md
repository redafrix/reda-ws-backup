# 005 - SimVLA Fine-Tuned ckpt-50000 Isaac No-Rotation Tests

## Purpose

Deploy the user fine-tuned SimVLA checkpoint in Isaac using the same task sequence and no-rotation camera convention as the old/basic SimVLA run.

## Source Checkpoint

Local zip provided by the user:

- `/home/redafrix/Downloads/ckpt-50000 (1).zip`

Transferred to Bob:

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_finetuned_isaac_20260703/ckpt-50000-finetuned-20260703.zip`

Unpacked raw checkpoint on Bob:

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_finetuned_isaac_20260703/ckpt-50000-finetuned`

Runtime-adapted checkpoint on Bob:

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_finetuned_isaac_20260703/ckpt-50000-finetuned-action-decoder`

## Checkpoint Adaptation

The zip checkpoint used `transformer.velocity_head.*` and `transformer.logvar_head.*` keys. The Bob SimVLA runtime expects `transformer.action_decoder.*`.

For deployment, `velocity_head.weight/bias` were copied to `action_decoder.weight/bias`, and the unused `logvar_head.*` tensors were removed. Tensor shapes matched the old SimVLA action decoder:

- action dimension: `7`
- hidden dimension: `1024`

The original zip and raw unpacked checkpoint were preserved.

## Runtime Config

Main eval config on Bob:

- `configs/eval_simvla_finetuned_ckpt50000_bob_no_rotation.yaml`

Important settings:

- `image_rotation: none`
- `action_mode: libero_joint`
- `num_actions: 10`
- `inference_steps: 10`
- `predict_uncertainty: false`
- `replan_steps: 5`

## Rollout Configs

Reaching:

- `configs/eval_simvla_finetuned_reaching_bob_5ep_no_rotation_800.yaml`
- output dir on Bob: `data/raw/simvla_finetuned_ckpt50000_reaching_5ep_no_rotation_800`
- `max_steps: 800`
- `camera_fps: 20`
- `state_record_fps: 20`

Pick-place:

- `configs/eval_simvla_finetuned_pick_place_bob_5ep_no_rotation_800.yaml`
- output dir on Bob: `data/raw/simvla_finetuned_ckpt50000_pick_place_5ep_no_rotation_800`
- `max_steps: 800`
- `camera_fps: 20`
- `state_record_fps: 20`

## Result

All 10 rollout tests completed and all were failures at the configured 800-step limit:

- 5 reaching failures.
- 5 pick-place failures.

No image flip or rotation was applied. This matches the Isaac camera decision used for the old/basic SimVLA run.

## Local Evidence

Current readable fast video:

- `vids/simvla_finetuned_ckpt50000_10_tests_agent_view_4x_labeled.mp4`

Video summary:

- `vids/simvla_finetuned_ckpt50000_10_tests_agent_view_4x_labeled.json`

Checked properties:

- resolution: `640x480`
- duration: `17.0` seconds
- fps: `20`
- frames: `340`

## Video Builder

Script added locally and copied to Bob for this run:

- `scripts/generated/create_simvla_ft_labeled_video_20260703.py`

Remote copy used for rendering:

- `scripts/create_simvla_ft_labeled_video_20260703.py`
