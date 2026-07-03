# First New Object Test Report

Goal:
Test exactly one non-baseline object variant using the already-working deterministic apple pipeline.

Candidate priority:
1. fcan03
2. kiwi07
3. cup05

No bulk object integration yet.
## Git state
object-integration-static-assets
2c8bfbbe19656baae0df607ba81caae8a3e30185

## Object catalog files
-rw-rw-r-- 1 redafrix redafrix  13K Jun 12 10:18 configs/object_catalog.generated.yaml
-rw-rw-r-- 1 redafrix redafrix 1.2K Jun 12 09:46 configs/object_catalog.yaml

## Candidate search
configs/object_catalog.yaml:27:      - id: fcan01
configs/object_catalog.yaml:28:        usd_path: can/fcan01.usd
configs/object_catalog.yaml:30:  - id: cup
configs/object_catalog.yaml:31:    label: cup
configs/object_catalog.yaml:36:      - id: cup00
configs/object_catalog.yaml:37:        usd_path: cup/cup00.usd
configs/object_catalog.yaml:38:      - id: cup01
configs/object_catalog.yaml:39:        usd_path: cup/cup01.usd
configs/object_catalog.generated.yaml:221:  - id: can03
configs/object_catalog.generated.yaml:222:    usd_path: can/can03.usd
configs/object_catalog.generated.yaml:233:  - id: fcan01
configs/object_catalog.generated.yaml:234:    usd_path: can/fcan01.usd
configs/object_catalog.generated.yaml:235:  - id: fcan03
configs/object_catalog.generated.yaml:236:    usd_path: can/fcan03.usd
configs/object_catalog.generated.yaml:237:  - id: fcan04
configs/object_catalog.generated.yaml:238:    usd_path: can/fcan04.usd
configs/object_catalog.generated.yaml:239:  - id: fcan05
configs/object_catalog.generated.yaml:240:    usd_path: can/fcan05.usd
configs/object_catalog.generated.yaml:241:  - id: fcan08
configs/object_catalog.generated.yaml:242:    usd_path: can/fcan08.usd
configs/object_catalog.generated.yaml:243:  - id: fcan11
configs/object_catalog.generated.yaml:244:    usd_path: can/fcan11.usd
configs/object_catalog.generated.yaml:245:  - id: fcan15
configs/object_catalog.generated.yaml:246:    usd_path: can/fcan15.usd
configs/object_catalog.generated.yaml:247:  - id: fcan17
configs/object_catalog.generated.yaml:248:    usd_path: can/fcan17.usd
configs/object_catalog.generated.yaml:249:  - id: fcan18
configs/object_catalog.generated.yaml:250:    usd_path: can/fcan18.usd
configs/object_catalog.generated.yaml:251:- id: cup
configs/object_catalog.generated.yaml:252:  label: cup
configs/object_catalog.generated.yaml:259:  - id: cup00
configs/object_catalog.generated.yaml:260:    usd_path: cup/cup00.usd
configs/object_catalog.generated.yaml:261:  - id: cup01
configs/object_catalog.generated.yaml:262:    usd_path: cup/cup01.usd
configs/object_catalog.generated.yaml:263:  - id: cup02
configs/object_catalog.generated.yaml:264:    usd_path: cup/cup02.usd
configs/object_catalog.generated.yaml:265:  - id: cup03
configs/object_catalog.generated.yaml:266:    usd_path: cup/cup03.usd
configs/object_catalog.generated.yaml:267:  - id: cup04
configs/object_catalog.generated.yaml:268:    usd_path: cup/cup04.usd
configs/object_catalog.generated.yaml:269:  - id: cup05
configs/object_catalog.generated.yaml:270:    usd_path: cup/cup05.usd
configs/object_catalog.generated.yaml:271:  - id: cup06
configs/object_catalog.generated.yaml:272:    usd_path: cup/cup06.usd
configs/object_catalog.generated.yaml:273:  - id: cup07
configs/object_catalog.generated.yaml:274:    usd_path: cup/cup07.usd
configs/object_catalog.generated.yaml:275:  - id: cup08
configs/object_catalog.generated.yaml:276:    usd_path: cup/cup08.usd
configs/object_catalog.generated.yaml:277:  - id: cup09
configs/object_catalog.generated.yaml:278:    usd_path: cup/cup09.usd
configs/object_catalog.generated.yaml:309:- id: kiwi
configs/object_catalog.generated.yaml:310:  label: kiwi
configs/object_catalog.generated.yaml:317:  - id: kiwi00
configs/object_catalog.generated.yaml:318:    usd_path: kiwi/kiwi00.usd
configs/object_catalog.generated.yaml:319:  - id: kiwi05
configs/object_catalog.generated.yaml:320:    usd_path: kiwi/kiwi05.usd
configs/object_catalog.generated.yaml:321:  - id: kiwi07
configs/object_catalog.generated.yaml:322:    usd_path: kiwi/kiwi07.usd
configs/object_catalog.generated.yaml:613:- id: unseen_cup
configs/object_catalog.generated.yaml:614:  label: cup
configs/object_catalog.generated.yaml:621:  - id: cup99
configs/object_catalog.generated.yaml:622:    usd_path: unseen/cup99.usd
objects/metadata.json:714:    "can03.usd": {
objects/metadata.json:760:    "fcan01.usd": {
objects/metadata.json:765:    "fcan03.usd": {
objects/metadata.json:773:    "fcan04.usd": {
objects/metadata.json:781:    "fcan05.usd": {
objects/metadata.json:789:    "fcan08.usd": {
objects/metadata.json:797:    "fcan11.usd": {
objects/metadata.json:805:    "fcan15.usd": {
objects/metadata.json:813:    "fcan17.usd": {
objects/metadata.json:821:    "fcan18.usd": {
objects/metadata.json:827:    "cup00.usd": {
objects/metadata.json:829:            "cup",
objects/metadata.json:830:            "tall cup",
objects/metadata.json:831:            "cone-shaped cup",
objects/metadata.json:832:            "tall cone-shaped cup"
objects/metadata.json:835:    "cup01.usd": {
objects/metadata.json:837:            "cup",
objects/metadata.json:838:            "yellow cup",
objects/metadata.json:839:            "tall cup",
objects/metadata.json:840:            "cup with red flower",
objects/metadata.json:841:            "yellow tall cup",
objects/metadata.json:842:            "yellow cup with red flower",
objects/metadata.json:843:            "tall cup with red flower",
objects/metadata.json:844:            "yellow tall cup with red flower"
objects/metadata.json:847:    "cup02.usd": {
objects/metadata.json:849:            "cup",
objects/metadata.json:850:            "yellow cup",
objects/metadata.json:851:            "tall cup",
objects/metadata.json:852:            "cup with red watermelon",
objects/metadata.json:853:            "yellow tall cup",
objects/metadata.json:854:            "yellow cup with red watermelon",
objects/metadata.json:855:            "tall cup with red watermelon",
objects/metadata.json:856:            "yellow tall cup with red watermelon"
objects/metadata.json:859:    "cup03.usd": {
objects/metadata.json:861:            "cup",
objects/metadata.json:862:            "blue cup",
objects/metadata.json:863:            "tall cup",
objects/metadata.json:864:            "cup with NTU Singapore logo",
objects/metadata.json:865:            "blue tall cup",
objects/metadata.json:866:            "blue cup with NTU Singapore logo",
objects/metadata.json:867:            "tall cup with NTU Singapore logo",
objects/metadata.json:868:            "blue tall cup with NTU Singapore logo"
objects/metadata.json:871:    "cup04.usd": {
objects/metadata.json:873:            "cup",
objects/metadata.json:874:            "red cup",
objects/metadata.json:875:            "tall cup",
objects/metadata.json:876:            "cup with MMLab at NTU logo",
objects/metadata.json:877:            "red tall cup",
objects/metadata.json:878:            "red cup with MMLab at NTU logo",
objects/metadata.json:879:            "tall cup with MMLab at NTU logo",
objects/metadata.json:880:            "red tall cup with MMLab at NTU logo"
objects/metadata.json:883:    "cup05.usd": {
objects/metadata.json:885:            "cup",
objects/metadata.json:886:            "white cup",
objects/metadata.json:887:            "short cup",
objects/metadata.json:888:            "white short cup"
objects/metadata.json:891:    "cup06.usd": {
objects/metadata.json:893:            "cup",
objects/metadata.json:894:            "white cup",
objects/metadata.json:895:            "tall cup",
objects/metadata.json:896:            "white tall cup"
objects/metadata.json:899:    "cup07.usd": {
objects/metadata.json:901:            "cup",
objects/metadata.json:902:            "yellow cup",
objects/metadata.json:903:            "tall cup",
objects/metadata.json:904:            "yellow tall cup"
objects/metadata.json:907:    "cup08.usd": {
objects/metadata.json:909:            "cup",
objects/metadata.json:910:            "red cup",
objects/metadata.json:911:            "tall cup",
objects/metadata.json:912:            "red tall cup"
objects/metadata.json:915:    "cup09.usd": {
objects/metadata.json:917:            "cup",
objects/metadata.json:918:            "black cup",
objects/metadata.json:919:            "tall cup",
objects/metadata.json:920:            "black tall cup"
objects/metadata.json:992:    "kiwi07.usd": {
objects/metadata.json:994:            "kiwi",
objects/metadata.json:995:            "light-green kiwi"
objects/kiwi/kiwi05.usd:24:            string authoring_layer = "./kiwi_5.usd"
objects/kiwi/kiwi05.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\kiwi\\kiwi05.usd
objects/kiwi/kiwi05.usd:121:                    asset inputs:file = @./texture/kiwi05.jpg@ (
objects/kiwi/kiwi07.usd:24:            string authoring_layer = "./kiwi_7.usd"
objects/kiwi/kiwi07.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\kiwi\\kiwi07.usd
objects/kiwi/kiwi07.usd:119:                    asset inputs:file = @./texture/kiwi07.jpg@ (
objects/kiwi/kiwi00.usd:24:            string authoring_layer = "./kiwi_0.usd"
objects/kiwi/kiwi00.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\kiwi\\kiwi00.usd
objects/kiwi/kiwi00.usd:121:                    asset inputs:file = @./texture/kiwi00.jpg@ (
objects/can/fcan15.usd:24:            string authoring_layer = "./fcan15.usd"
objects/can/fcan15.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan15.usd
objects/can/can03.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\can03.usd
objects/can/can03.usd:119:                    asset inputs:file = @./texture/can03.jpg@ (
objects/can/fcan18.usd:24:            string authoring_layer = "./fcan18.usd"
objects/can/fcan18.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan18.usd
objects/can/fcan11.usd:24:            string authoring_layer = "./fcan11.usd"
objects/can/fcan11.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan11.usd
objects/can/fcan03.usd:24:            string authoring_layer = "./fcan03.usd"
objects/can/fcan03.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan03.usd
objects/can/fcan04.usd:24:            string authoring_layer = "./fcan04.usd"
objects/can/fcan04.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan04.usd
objects/can/fcan05.usd:24:            string authoring_layer = "./fcan05.usd"
objects/can/fcan05.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan05.usd
objects/can/fcan17.usd:24:            string authoring_layer = "./fcan17.usd"
objects/can/fcan17.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan17.usd
objects/can/fcan01.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan01.usd
objects/can/fcan08.usd:24:            string authoring_layer = "./fcan08.usd"
objects/can/fcan08.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\can\\fcan08.usd
objects/cup/cup01.usd:24:            string authoring_layer = "./cup01.usd"
objects/cup/cup01.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup01.usd
objects/cup/cup01.usd:119:                    asset inputs:file = @./texture/cup01.jpg@ (
objects/cup/cup09.usd:24:            string authoring_layer = "./cup04.usd"
objects/cup/cup09.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup09.usd
objects/cup/cup08.usd:24:            string authoring_layer = "./cup08.usd"
objects/cup/cup08.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup08.usd
objects/cup/cup06.usd:24:            string authoring_layer = "./cup06.usd"
objects/cup/cup06.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup06.usd
objects/cup/cup02.usd:24:            string authoring_layer = "./cup02.usd"
objects/cup/cup02.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup02.usd
objects/cup/cup02.usd:119:                    asset inputs:file = @./texture/cup02.jpg@ (
objects/cup/cup03.usd:24:            string authoring_layer = "./cup03.usd"
objects/cup/cup03.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup03.usd
objects/cup/cup03.usd:119:                    asset inputs:file = @./texture/cup03.jpg@ (
objects/cup/cup05.usd:24:            string authoring_layer = "./cup00.usd"
objects/cup/cup05.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup05.usd
objects/cup/cup07.usd:24:            string authoring_layer = "./cup03.usd"
objects/cup/cup07.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup07.usd
objects/cup/cup04.usd:24:            string authoring_layer = "./cup04.usd"
objects/cup/cup04.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup04.usd
objects/cup/cup04.usd:119:                    asset inputs:file = @./texture/cup04.jpg@ (
objects/cup/cup00.usd:24:            string authoring_layer = "./cup00.usd"
objects/cup/cup00.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup00.usd
objects/tree.md:172:│   │   ├── can03.jpg
objects/tree.md:189:│   ├── can03.usd
objects/tree.md:195:│   ├── fcan01.usd
objects/tree.md:196:│   ├── fcan03.usd
objects/tree.md:197:│   ├── fcan04.usd
objects/tree.md:198:│   ├── fcan05.usd
objects/tree.md:199:│   ├── fcan08.usd
objects/tree.md:200:│   ├── fcan11.usd
objects/tree.md:201:│   ├── fcan15.usd
objects/tree.md:202:│   ├── fcan17.usd
objects/tree.md:203:│   └── fcan18.usd
objects/tree.md:204:├── cup
objects/tree.md:206:│   │   ├── cup01.jpg
objects/tree.md:207:│   │   ├── cup02.jpg
objects/tree.md:208:│   │   ├── cup03.jpg
objects/tree.md:209:│   │   └── cup04.jpg
objects/tree.md:210:│   ├── cup00.usd
objects/tree.md:211:│   ├── cup01.usd
objects/tree.md:212:│   ├── cup02.usd
objects/tree.md:213:│   ├── cup03.usd
objects/tree.md:214:│   ├── cup04.usd
objects/tree.md:215:│   ├── cup05.usd
objects/tree.md:216:│   ├── cup06.usd
objects/tree.md:217:│   ├── cup07.usd
objects/tree.md:218:│   ├── cup08.usd
objects/tree.md:219:│   └── cup09.usd
objects/tree.md:242:├── kiwi
objects/tree.md:244:│   │   ├── kiwi00.jpg
objects/tree.md:245:│   │   ├── kiwi05.jpg
objects/tree.md:246:│   │   └── kiwi07.jpg
objects/tree.md:247:│   ├── kiwi00.usd
objects/tree.md:248:│   ├── kiwi05.usd
objects/tree.md:249:│   └── kiwi07.usd
objects/tree.md:447:│   │   ├── cup99.jpg
objects/tree.md:451:│   ├── cup99.usd
objects/unseen/cup99.usd:24:            string authoring_layer = "./cup99.usd"
objects/unseen/cup99.usd:33:Generated from Composed Stage of root layer D:\\Projects\\DynamicVLA\\objects-new\\objects-new\\cup\\cup04.usd
objects/unseen/cup99.usd:119:                    asset inputs:file = @./texture/cup99.jpg@ (
Could not select a candidate automatically. Stop and report.
USING_CATALOG configs/object_catalog.generated.yaml
TOTAL_VARIANTS 211
SELECTED_CATEGORY_ID can
SELECTED_LABEL can
SELECTED_VARIANT_ID fcan03
SELECTED_USD_PATH can/fcan03.usd
SELECTED_CATEGORY_ID=can
SELECTED_LABEL=can
SELECTED_VARIANT_ID=fcan03
SELECTED_USD_PATH=can/fcan03.usd

## Created config
configs/first_object_test_can_fcan03.yaml
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
## meta.json
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
## Post-processing logs

### first_object_test_can_fcan03_export_ila.log
[INFO] Saved ILA manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03_ila/manifest.json

### first_object_test_can_fcan03_inspect_collection.log
collection: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03
episodes: 1
success: 0/1

episode_id success  meta_steps traj_steps meta_cam  traj_cam  depth  object_variant       light                   
000000     false    1959       1959       490       490       true   fcan03               1145.7 (0.90, 0.90, 0.90)

success by pose variant:
object_pos_local           place_pos_local            success 
(0.58, -0.16, 1.08)        (0.55, 0.22, 1.08)         0/1       

### first_object_test_can_fcan03_inspect_episode.log
metadata:
  episode_id: 0
  task_name: pick_place
  instruction: pick up the can and place it on the target area
  success: False
  num_steps: 1959
  sim_dt: 0.008333333333333333
  seed: 123
  record_cameras: True
  record_depth: True
  num_camera_frames: 490
  object_pos_local: [0.58, -0.16, 1.08]
  place_pos_local: [0.55, 0.22, 1.08]
  object_xy_offset: [0.0, 0.0]
  place_xy_offset: [0.0, 0.0]
  object_category_id: can
  object_variant_id: fcan03
  object_label: can
  object_usd_path: objects/can/fcan03.usd
  light_intensity: 1145.6593828734322
  light_color: [0.9, 0.9, 0.9]

trajectory.npz:
  timestamps_s                 (1959,)                  float32
  joint_pos                    (1959, 1, 9)             float32
  joint_vel                    (1959, 1, 9)             float32
  ee_pos_w                     (1959, 1, 3)             float32
  object_pos_w                 (1959, 1, 3)             float32
  action_target_pos_w          (1959, 1, 3)             float32
  action_target_quat_w         (1959, 1, 4)             float32
  action_finger_opening_m      (1959,)                  float64
  camera_step_indices          (490,)                   int64
  camera_timestamps_s          (490,)                   float32
  agent_rgb                    (490, 128, 128, 3)       uint8
  wrist_rgb                    (490, 128, 128, 3)       uint8
  agent_depth                  (490, 128, 128)          float32
  wrist_depth                  (490, 128, 128)          float32

### first_object_test_can_fcan03_inspect_ila.log
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/scripts/inspect_ila_dataset.py", line 13, in <module>
    from franka_wrist_camera_scene.datasets.ila import ILADataset
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/datasets/ila.py", line 9, in <module>
    import torch
ModuleNotFoundError: No module named 'torch'

### first_object_test_can_fcan03_visualize.log
[INFO] Saved episode visualization to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03_preview.png

## Preview/output files
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03/000000/meta.json | 720 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03/000000/trajectory.npz | 37113829 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03_ila/episodes/000000.npz | 36960660 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03_ila/manifest.json | 1282 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03/manifest.json | 935 bytes
-rw-rw-r-- 1 redafrix redafrix 340K Jun 12 14:15 /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03_preview.png

# FINAL SUMMARY
- branch: object-integration-static-assets
- commit: 2c8bfbbe19656baae0df607ba81caae8a3e30185
- selected_category_id: can
- selected_variant_id: fcan03
- selected_usd_path: can/fcan03.usd
- collect_status: 0
- success: NO
- committed_config: NO
- config: configs/first_object_test_can_fcan03.yaml
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/first_object_test_can_fcan03
- patch: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/patches/first_object_test_can_fcan03.patch

## AUTOMATIC EPISODE VIDEOS & PREVIEWS
- **generated_video_count**: 2
- **generated_preview_count**: 2
- **failed_video_generation_count**: 0
- **all video/preview paths**:
  - Video 1 (fcan03): [first_object_test_can_fcan03_000000_FAIL_agent_plus_wrist.mp4](file:///home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/first_object_test_can_fcan03_000000_FAIL_agent_plus_wrist.mp4)
  - Preview 1 (fcan03): [first_object_test_can_fcan03_000000_FAIL_agent_plus_wrist.preview.jpg](file:///home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/first_object_test_can_fcan03_000000_FAIL_agent_plus_wrist.preview.jpg)
  - Video 2 (apple): [apple_recheck_after_fcan03_patch_000000_SUCCESS_agent_plus_wrist.mp4](file:///home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/apple_recheck_after_fcan03_patch_000000_SUCCESS_agent_plus_wrist.mp4)
  - Preview 2 (apple): [apple_recheck_after_fcan03_patch_000000_SUCCESS_agent_plus_wrist.preview.jpg](file:///home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/apple_recheck_after_fcan03_patch_000000_SUCCESS_agent_plus_wrist.preview.jpg)

## PHYSICS & SLIP FAILURE ANALYSIS

We observed that the `fcan03` collection episode completed, but failed with `success: False` because the object slipped out of the gripper during the lift phase. Below is our detailed physical analysis:

1. **Object Dimensions & Bounding Boxes:**
   - `apple01` extent in USD: `[(-0.5, -0.476, -0.487), (0.5, 0.476, 0.487)]` -> Z-height is `0.975` units. At scale `0.0595`, simulated diameter is ~`5.8` cm.
   - `fcan03` extent in USD: `[(-0.316, -0.316, -0.5), (0.316, 0.316, 0.5)]` -> Z-height is `1.0` units. At scale `0.0595`, simulated diameter is ~`3.76` cm and height is ~`5.95` cm.
   - When the end-effector lifts to `z = 1.206` (TCP at `1.106`), the bottom of the fingers still overlaps with the top of the can (at `z = 1.109`), which keeps the gripper in contact with the can as it slides out. Once the gripper clears the top of the can at `z = 1.306`, the fingers snap shut to `0.0002` m.

2. **Mass Discrepancy & Gripping Forces:**
   - `apple01` mass in the simulator is **`0.20 kg`**. When grasped, the finger width is `0.0594` m (joints at `0.0297` m). The squeezing force is `stiffness * joint_error = 150.0 * 0.0297 = 4.455` N. With a standard friction coefficient of `0.5`, the max friction force is `2 * 0.5 * 4.455 = 4.455` N, which easily overcomes the `1.962` N gravity force.
   - `fcan03` mass in the simulator is **`0.50 kg`**. When grasped, the finger width is `0.0393` m (joints at `0.0195` m). The squeezing force is `150.0 * 0.0195 = 2.925` N. The max friction force is `2 * 0.5 * 2.925 = 2.925` N, which is **less** than the `4.905` N gravity force on the can.
   - Therefore, the can slips through the fingers due to insufficient squeezing force under the baseline gripper stiffness of `150.0`.

## RECOMMENDATION & NEXT STEPS
To support heavier static objects like `fcan03` (0.50 kg) and other static objects in bulk integration, we recommend either:
1. Increasing the gripper finger stiffness in `src/franka_wrist_camera_scene/scene/tabletop.py` from `150.0` to `300.0` or higher to increase squeezing force.
2. Sparing or scaling down the masses of heavier static objects in the simulation config.

## git status
?? configs/first_object_test_can_fcan03.yaml


