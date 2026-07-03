# fcan03 Fix Sweep Report

Goal:
Diagnose and minimally fix why `can/fcan03` slips/fails while baseline apple succeeds.

Rules:
- No bulk object integration.
- No global physics change unless tested against apple.
- No commit unless a fix succeeds and apple still succeeds.
## Git state
object-integration-static-assets
2c8bfbbe19656baae0df607ba81caae8a3e30185
 M src/franka_wrist_camera_scene/collection/pick_place.py
 M src/franka_wrist_camera_scene/scene/tabletop.py
?? configs/first_object_test_can_fcan03.yaml
?? configs/object_sweeps/
?? scratch/
?? src/franka_wrist_camera_scene/collection/pick_place.py.bak_fcan03_sweep
?? src/franka_wrist_camera_scene/scene/tabletop.py.bak_fcan03_sweep

## Existing fcan03 failed output
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03/000000/meta.json | 720 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03/000000/trajectory.npz | 37113829 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03/manifest.json | 935 bytes

## Existing fcan03 meta
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the can and place it on the target area",
  "success": false,
  "num_steps": 1959,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 490,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "can",
  "object_variant_id": "fcan03",
  "object_label": "can",
  "object_usd_path": "objects/can/fcan03.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
## Existing fcan03 config
output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03
start_episode_id: 0
num_episodes: 1
max_steps: 2400
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 123

target_object:
  catalog_config: object_catalog.generated.yaml
  category_id: can
  variant_id: fcan03

pose_randomization:
  object_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]
  place_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]

lighting_randomization:
  dome_light_intensity_range: [650.0, 1200.0]
  dome_light_color_options:
    - [0.90, 0.90, 0.90]
    - [1.00, 0.92, 0.84]
    - [0.82, 0.88, 1.00]
RUNNING fcan03_mass020_stiff150

## Result fcan03_mass020_stiff150
status=0
2026-06-12 12:40:18 [2,746ms] [Warning] [gpu.foundation.plugin] Detected IOMMU is enabled. Running CUDA peer-to-peer bandwidth and latency validation.
[INFO][AppLauncher]: Using device: cuda:0
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150/manifest.json

outputs:
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150/000000/meta.json | 719 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150/000000/trajectory.npz | 39839854 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150/manifest.json | 934 bytes

meta:
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the can and place it on the target area",
  "success": true,
  "num_steps": 1926,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 482,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "can",
  "object_variant_id": "fcan03",
  "object_label": "can",
  "object_usd_path": "objects/can/fcan03.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}Video generated successfully at: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.mp4
Preview contact sheet generated at: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.preview.jpg
RUNNING fcan03_mass020_stiff220

## Result fcan03_mass020_stiff220
status=0
2026-06-12 12:47:02 [2,783ms] [Warning] [gpu.foundation.plugin] Detected IOMMU is enabled. Running CUDA peer-to-peer bandwidth and latency validation.
[INFO][AppLauncher]: Using device: cuda:0
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220/manifest.json

outputs:
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220/000000/meta.json | 719 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220/000000/trajectory.npz | 39999914 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220/manifest.json | 934 bytes

meta:
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the can and place it on the target area",
  "success": true,
  "num_steps": 1955,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 489,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "can",
  "object_variant_id": "fcan03",
  "object_label": "can",
  "object_usd_path": "objects/can/fcan03.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}Video generated successfully at: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff220_000000_SUCCESS_agent_plus_wrist.mp4
Preview contact sheet generated at: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff220_000000_SUCCESS_agent_plus_wrist.preview.jpg
RUNNING fcan03_mass050_stiff300

## Result fcan03_mass050_stiff300
status=0
2026-06-12 12:48:51 [1,089ms] [Warning] [gpu.foundation.plugin] Detected IOMMU is enabled. Running CUDA peer-to-peer bandwidth and latency validation.
[INFO][AppLauncher]: Using device: cuda:0
[INFO] Episode 0 success: False
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass050_stiff300/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass050_stiff300/manifest.json

outputs:
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass050_stiff300/000000/meta.json | 720 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass050_stiff300/000000/trajectory.npz | 38105386 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass050_stiff300/manifest.json | 935 bytes

meta:
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the can and place it on the target area",
  "success": false,
  "num_steps": 1957,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 490,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "can",
  "object_variant_id": "fcan03",
  "object_label": "can",
  "object_usd_path": "objects/can/fcan03.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}Video generated successfully at: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass050_stiff300_000000_FAIL_agent_plus_wrist.mp4
Preview contact sheet generated at: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass050_stiff300_000000_FAIL_agent_plus_wrist.preview.jpg
Post-processing successful sweep: fcan03_mass020_stiff150
Post-processing successful sweep: fcan03_mass020_stiff220

# FINAL SUMMARY
- branch: object-integration-static-assets
- commit_start: 2c8bfbbe19656baae0df607ba81caae8a3e30185
- apple_recheck_status: 0
- apple_recheck_success: YES
- successful_fcan03_sweeps: fcan03_mass020_stiff150,fcan03_mass020_stiff220

## Current diff
 .../collection/pick_place.py                        |  1 +
 src/franka_wrist_camera_scene/scene/tabletop.py     | 21 ++++++++++++++++++++-
 2 files changed, 21 insertions(+), 1 deletion(-)
diff --git a/src/franka_wrist_camera_scene/collection/pick_place.py b/src/franka_wrist_camera_scene/collection/pick_place.py
index 3eda5cc..80b2244 100644
--- a/src/franka_wrist_camera_scene/collection/pick_place.py
+++ b/src/franka_wrist_camera_scene/collection/pick_place.py
@@ -181,6 +181,7 @@ def collect_pick_place_dataset(
             object_context=object_context,
             num_envs=1,
             env_spacing=2.5,
+            physics_overrides=collection_cfg.get("physics_overrides", {}),
         )
     )
     robot: Articulation = scene["robot"]
diff --git a/src/franka_wrist_camera_scene/scene/tabletop.py b/src/franka_wrist_camera_scene/scene/tabletop.py
index 0a4d267..7b97b17 100644
--- a/src/franka_wrist_camera_scene/scene/tabletop.py
+++ b/src/franka_wrist_camera_scene/scene/tabletop.py
@@ -113,12 +113,31 @@ def make_tabletop_scene_cfg(
     object_context: CatalogObjectContext,
     num_envs: int = 1,
     env_spacing: float = 2.5,
+    physics_overrides: dict | None = None,
 ) -> TabletopFrankaSceneCfg:
     """Create a tabletop scene configuration with the specified target object."""
     scene_cfg = TabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
     scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
-    # Modify gripper finger actuator stiffness/damping to prevent force explosion
+
+    # Baseline local Isaac 4.5 stabilization defaults.
     if "panda_hand" in scene_cfg.robot.actuators:
         scene_cfg.robot.actuators["panda_hand"].stiffness = 150.0
         scene_cfg.robot.actuators["panda_hand"].damping = 15.0
+
+    # Optional per-run physics overrides for controlled object testing.
+    # These are intentionally config-driven so failed experiments do not require global changes.
+    physics_overrides = physics_overrides or {}
+    if "target_mass" in physics_overrides:
+        if scene_cfg.target_cube.spawn.mass_props is None:
+            scene_cfg.target_cube.spawn.mass_props = sim_utils.schemas.MassPropertiesCfg()
+        scene_cfg.target_cube.spawn.mass_props.mass = float(physics_overrides["target_mass"])
+    if "target_linear_damping" in physics_overrides:
+        scene_cfg.target_cube.spawn.rigid_props.linear_damping = float(physics_overrides["target_linear_damping"])
+    if "target_angular_damping" in physics_overrides:
+        scene_cfg.target_cube.spawn.rigid_props.angular_damping = float(physics_overrides["target_angular_damping"])
+    if "gripper_stiffness" in physics_overrides and "panda_hand" in scene_cfg.robot.actuators:
+        scene_cfg.robot.actuators["panda_hand"].stiffness = float(physics_overrides["gripper_stiffness"])
+    if "gripper_damping" in physics_overrides and "panda_hand" in scene_cfg.robot.actuators:
+        scene_cfg.robot.actuators["panda_hand"].damping = float(physics_overrides["gripper_damping"])
+
     return scene_cfg

## Git status
 M src/franka_wrist_camera_scene/collection/pick_place.py
 M src/franka_wrist_camera_scene/scene/tabletop.py
?? configs/first_object_test_can_fcan03.yaml
?? configs/object_sweeps/
?? scratch/
