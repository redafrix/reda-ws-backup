# Corrupted Action Evaluation

## Purpose
Evaluate RND/ACE/FIPER robust response to corrupted actions in real-time.

## Logic
- No training or calibration happens here.
- Source dataset: `00_global_main/success_test_id`
- Corruptions applied at chunk level: zero, random_uniform, shuffled, reversed, scaled, gripper_flipped, repeated, gaussian noise.
