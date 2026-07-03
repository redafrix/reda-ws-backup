# 006 - SimVLA Fine-Tuned ckpt-50000 Isaac 5000-Step Tests

## Purpose

Deploy the user fine-tuned SimVLA checkpoint in Isaac using the same task sequence and no-rotation camera convention as the old/basic SimVLA run, but with an extended step limit of 5,000 steps per episode.

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

- `configs/eval_simvla_finetuned_reaching_bob_5ep_no_rotation_5000.yaml`
- output dir on Bob: `data/raw/simvla_finetuned_ckpt50000_reaching_5ep_no_rotation_5000`
- `max_steps: 5000`
- `camera_fps: 20`
- `state_record_fps: 20`

Pick-place:

- `configs/eval_simvla_finetuned_pick_place_bob_5ep_no_rotation_5000.yaml`
- output dir on Bob: `data/raw/simvla_finetuned_ckpt50000_pick_place_5ep_no_rotation_5000`
- `max_steps: 5000`
- `camera_fps: 20`
- `state_record_fps: 20`

## Result

Out of 10 rollout tests, 1 succeeded and 9 failed at the 5,000-step limit:

- **Reaching:** 5 failures (all 5 ran for 5,000 steps).
- **Pick-place:** 1 success, 4 failures.
  - Episode 3 ("pick up the onion and place it in the tray") was a **Success** (completed in 2,530 steps).
  - Episodes 0, 1, 2, 4 failed at the 5,000-step limit.

No image flip or rotation was applied.

## Local Evidence

Current readable fast video:

- `vids/simvla_finetuned_ckpt50000_10_tests_agent_view_4x_labeled_5000.mp4`

Video summary:

- `vids/simvla_finetuned_ckpt50000_10_tests_agent_view_4x_labeled_5000.json`

Checked properties:

- resolution: `640x480`
- duration: `99.35` seconds
- fps: `20`
- frames: `1987`

## Video Builder

Script added locally and copied to Bob:

- `scripts/generated/create_simvla_ft_labeled_video_20260703.py`

Remote copy used for rendering:

- `scripts/create_simvla_ft_labeled_video_20260703.py`
