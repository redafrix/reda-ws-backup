# Successful Episode Video Report

Goal:
Create MP4 videos from already-recorded successful episodes.

No Isaac launch.
No new collection.
No repo modification.
## Successful/priority episodes found
- /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple/000000
  success=True object=apple/apple01 frames=488 steps=1952
- /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_recheck/000000
  success=True object=apple/apple01 frames=488 steps=1952

EPISODE_LIST=/tmp/success_episode_paths.txt
Generating video for: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple/000000
Output: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.mp4

## Video result for /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple/000000
- status: 0
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.mp4
- log: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_video.log
- size: 467722 bytes

### log tail
episode: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple/000000
npz keys: ['timestamps_s', 'joint_pos', 'joint_vel', 'ee_pos_w', 'object_pos_w', 'action_target_pos_w', 'action_target_quat_w', 'action_finger_opening_m', 'camera_step_indices', 'camera_timestamps_s', 'agent_rgb', 'wrist_rgb', 'agent_depth', 'wrist_depth']
rgb_keys: ['agent_rgb', 'wrist_rgb']
selected_agent_key: agent_rgb
selected_wrist_key: wrist_rgb
saved: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.mp4
frames: 488
shape: (128, 256, 3)
Generating video for: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_recheck/000000
Output: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.mp4

## Video result for /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_recheck/000000
- status: 0
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.mp4
- log: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_video.log
- size: 467625 bytes

### log tail
episode: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_recheck/000000
npz keys: ['timestamps_s', 'joint_pos', 'joint_vel', 'ee_pos_w', 'object_pos_w', 'action_target_pos_w', 'action_target_quat_w', 'action_finger_opening_m', 'camera_step_indices', 'camera_timestamps_s', 'agent_rgb', 'wrist_rgb', 'agent_depth', 'wrist_depth']
rgb_keys: ['agent_rgb', 'wrist_rgb']
selected_agent_key: agent_rgb
selected_wrist_key: wrist_rgb
saved: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.mp4
frames: 488
shape: (128, 256, 3)
## Creating preview contact sheets
preview_failed: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.mp4 ModuleNotFoundError("No module named 'imageio'")
preview_failed: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.mp4 ModuleNotFoundError("No module named 'imageio'")
## Creating preview contact sheets (using cv2)
preview: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.preview.jpg
preview: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.preview.jpg

# FINAL SUMMARY
- videos_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos
- report: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/SUCCESS_EPISODE_VIDEO_REPORT.md

## Videos
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.mp4 | 467722 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.mp4 | 467625 bytes

## Preview images
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_000000_agent_plus_wrist.preview.jpg | 50223 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/success_videos/baseline_reachable_apple_recheck_000000_agent_plus_wrist.preview.jpg | 50203 bytes

## Episode list used
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple/000000
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_recheck/000000
