# Complex Object Test Matrix Report

Goal:
After validating apple and fcan03, test more complex objects one by one.

Complexity types:
- small/heavy object
- concave cup/container
- tall cup/bottle-like object
- bowl/container-like shape
- rolling or unstable object

Rules:
- Always generate side-by-side MP4 videos after every run.
- Do not bulk integrate all objects.
- Use config-driven physics overrides only.
## Starting git state
object-integration-static-assets
2c8bfbbe19656baae0df607ba81caae8a3e30185
 M src/franka_wrist_camera_scene/collection/pick_place.py
 M src/franka_wrist_camera_scene/scene/tabletop.py
?? configs/first_object_test_can_fcan03.yaml
?? configs/object_sweeps/
?? scratch/

## Current diff before cleanup
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
## Complex candidates found
- cup/cup05 -> cup/cup05.usd
- cup/cup00 -> cup/cup00.usd
- cup/cup06 -> cup/cup06.usd
- bowl/bowl00 -> bowl/bowl00.usd
- bowl/bowl01 -> bowl/bowl01.usd
- plate/plate00 -> plate/plate00.usd
- kiwi/kiwi07 -> kiwi/kiwi07.usd

## Selected for this matrix
- cup/cup05 -> cup/cup05.usd
- cup/cup00 -> cup/cup00.usd
- cup/cup06 -> cup/cup06.usd
- bowl/bowl00 -> bowl/bowl00.usd
- bowl/bowl01 -> bowl/bowl01.usd
- plate/plate00 -> plate/plate00.usd

## Result complex_cup_cup05_default
- status: 0
- success: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup05_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_cup_cup05_default_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 448239 bytes

### log tail
```
Traceback (most recent call last):
    raise FileExistsError(f"Episode directory already exists: {episode_dir}")
FileExistsError: Episode directory already exists: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup05_default/000000
There was an error running python
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the cup and place it on the target area",
  "success": true,
  "num_steps": 1956,
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
  "object_category_id": "cup",
  "object_variant_id": "cup05",
  "object_label": "cup",
  "object_usd_path": "objects/cup/cup05.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_cup_cup00_default
- status: 0
- success: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup00_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_cup_cup00_default_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 448481 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup00_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup00_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the cup and place it on the target area",
  "success": true,
  "num_steps": 1956,
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
  "object_category_id": "cup",
  "object_variant_id": "cup00",
  "object_label": "cup",
  "object_usd_path": "objects/cup/cup00.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_cup_cup06_default
- status: 0
- success: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup06_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_cup_cup06_default_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 461120 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup06_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup06_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the cup and place it on the target area",
  "success": true,
  "num_steps": 1956,
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
  "object_category_id": "cup",
  "object_variant_id": "cup06",
  "object_label": "cup",
  "object_usd_path": "objects/cup/cup06.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_bowl_bowl00_default
- status: 0
- success: NO
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl00_default_000000_FAIL_agent_plus_wrist.mp4
- video_size: 418671 bytes

### log tail
```
[INFO] Episode 0 success: False
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the bowl and place it on the target area",
  "success": false,
  "num_steps": 1990,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 498,
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
  "object_category_id": "bowl",
  "object_variant_id": "bowl00",
  "object_label": "bowl",
  "object_usd_path": "objects/bowl/bowl00.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_bowl_bowl00_mass020_stiff150
- status: 0
- success: NO
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_mass020_stiff150
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl00_mass020_stiff150_000000_FAIL_agent_plus_wrist.mp4
- video_size: 418495 bytes

### log tail
```
[INFO] Episode 0 success: False
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_mass020_stiff150/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_mass020_stiff150/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the bowl and place it on the target area",
  "success": false,
  "num_steps": 1990,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 498,
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
  "object_category_id": "bowl",
  "object_variant_id": "bowl00",
  "object_label": "bowl",
  "object_usd_path": "objects/bowl/bowl00.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_bowl_bowl00_mass020_stiff220
- status: 0
- success: NO
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_mass020_stiff220
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl00_mass020_stiff220_000000_FAIL_agent_plus_wrist.mp4
- video_size: 418888 bytes

### log tail
```
[INFO] Episode 0 success: False
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_mass020_stiff220/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl00_mass020_stiff220/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the bowl and place it on the target area",
  "success": false,
  "num_steps": 1990,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 498,
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
  "object_category_id": "bowl",
  "object_variant_id": "bowl00",
  "object_label": "bowl",
  "object_usd_path": "objects/bowl/bowl00.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_bowl_bowl01_default
- status: 0
- success: NO
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl01_default_000000_FAIL_agent_plus_wrist.mp4
- video_size: 435911 bytes

### log tail
```
[INFO] Episode 0 success: False
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the bowl and place it on the target area",
  "success": false,
  "num_steps": 1983,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 496,
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
  "object_category_id": "bowl",
  "object_variant_id": "bowl01",
  "object_label": "bowl",
  "object_usd_path": "objects/bowl/bowl01.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_bowl_bowl01_mass020_stiff150
- status: 0
- success: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_mass020_stiff150
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl01_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 463053 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_mass020_stiff150/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_mass020_stiff150/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the bowl and place it on the target area",
  "success": true,
  "num_steps": 1980,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 495,
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
  "object_category_id": "bowl",
  "object_variant_id": "bowl01",
  "object_label": "bowl",
  "object_usd_path": "objects/bowl/bowl01.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_plate_plate00_default
- status: 0
- success: NO
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_plate_plate00_default_000000_FAIL_agent_plus_wrist.mp4
- video_size: 457822 bytes

### log tail
```
[INFO] Episode 0 success: False
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the plate and place it on the target area",
  "success": false,
  "num_steps": 1990,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 498,
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
  "object_category_id": "plate",
  "object_variant_id": "plate00",
  "object_label": "plate",
  "object_usd_path": "objects/plate/plate00.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result complex_plate_plate00_mass020_stiff150
- status: 0
- success: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_mass020_stiff150
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_plate_plate00_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 497260 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_mass020_stiff150/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_mass020_stiff150/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the plate and place it on the target area",
  "success": true,
  "num_steps": 1984,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 496,
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
  "object_category_id": "plate",
  "object_variant_id": "plate00",
  "object_label": "plate",
  "object_usd_path": "objects/plate/plate00.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```
Exporting successful run: complex_bowl_bowl01_mass020_stiff150
Exporting successful run: complex_cup_cup00_default
Exporting successful run: complex_cup_cup05_default
Exporting successful run: complex_cup_cup06_default
Exporting successful run: complex_plate_plate00_mass020_stiff150

## Complex object results table
| run | object | success | steps | frames |
|---|---|---:|---:|---:|
| complex_bowl_bowl00_default | bowl/bowl00 | False | 1990 | 498 |
| complex_bowl_bowl00_mass020_stiff150 | bowl/bowl00 | False | 1990 | 498 |
| complex_bowl_bowl00_mass020_stiff220 | bowl/bowl00 | False | 1990 | 498 |
| complex_bowl_bowl01_default | bowl/bowl01 | False | 1983 | 496 |
| complex_bowl_bowl01_mass020_stiff150 | bowl/bowl01 | True | 1980 | 495 |
| complex_cup_cup00_default | cup/cup00 | True | 1956 | 489 |
| complex_cup_cup05_default | cup/cup05 | True | 1956 | 489 |
| complex_cup_cup06_default | cup/cup06 | True | 1956 | 489 |
| complex_plate_plate00_default | plate/plate00 | False | 1990 | 498 |
| complex_plate_plate00_mass020_stiff150 | plate/plate00 | True | 1984 | 496 |

## Accepted successful runs
- complex_bowl_bowl01_mass020_stiff150 | bowl/bowl01
- complex_cup_cup00_default | cup/cup00
- complex_cup_cup05_default | cup/cup05
- complex_cup_cup06_default | cup/cup06
- complex_plate_plate00_mass020_stiff150 | plate/plate00

## Failed runs
- complex_bowl_bowl00_default | bowl/bowl00
- complex_bowl_bowl00_mass020_stiff150 | bowl/bowl00
- complex_bowl_bowl00_mass020_stiff220 | bowl/bowl00
- complex_bowl_bowl01_default | bowl/bowl01
- complex_plate_plate00_default | plate/plate00

# FINAL SUMMARY
- branch: object-integration-static-assets
- commit: d689baa6a4dab4f67aff31d811e95eb96dfd33c0
- apple_after_status: 0
- apple_after_success: YES
- videos_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos
- generated_video_count: 17
- generated_preview_count: 5
- patch_path: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/patches/complex_object_test_matrix.patch

## git status
?? configs/complex_object_tests/

## videos
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/apple_recheck_after_complex_objects_000000_SUCCESS_agent_plus_wrist.mp4 | 484945 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/apple_recheck_after_fcan03_patch_000000_SUCCESS_agent_plus_wrist.mp4 | 1279919 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/apple_recheck_after_fcan03_patch_000000_SUCCESS_agent_plus_wrist.preview.jpg | 96237 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl00_default_000000_FAIL_agent_plus_wrist.mp4 | 418671 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl00_mass020_stiff150_000000_FAIL_agent_plus_wrist.mp4 | 418495 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl00_mass020_stiff220_000000_FAIL_agent_plus_wrist.mp4 | 418888 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl01_default_000000_FAIL_agent_plus_wrist.mp4 | 435911 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_bowl_bowl01_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.mp4 | 463053 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_cup_cup00_default_000000_SUCCESS_agent_plus_wrist.mp4 | 448481 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_cup_cup05_default_000000_SUCCESS_agent_plus_wrist.mp4 | 448239 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_cup_cup06_default_000000_SUCCESS_agent_plus_wrist.mp4 | 461120 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_plate_plate00_default_000000_FAIL_agent_plus_wrist.mp4 | 457822 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/complex_plate_plate00_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.mp4 | 497260 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.mp4 | 1266948 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff150_000000_SUCCESS_agent_plus_wrist.preview.jpg | 93304 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff220_000000_SUCCESS_agent_plus_wrist.mp4 | 1249869 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass020_stiff220_000000_SUCCESS_agent_plus_wrist.preview.jpg | 95093 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass050_stiff300_000000_FAIL_agent_plus_wrist.mp4 | 1220213 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/fcan03_mass050_stiff300_000000_FAIL_agent_plus_wrist.preview.jpg | 89562 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/first_object_test_can_fcan03_000000_FAIL_agent_plus_wrist.mp4 | 1209684 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/first_object_test_can_fcan03_000000_FAIL_agent_plus_wrist.preview.jpg | 88831 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/first_object_test_can_fcan03_failed_agent_plus_wrist.mp4 | 446085 bytes
