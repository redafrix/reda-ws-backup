# DynamicVLA Scripted Data Collection Stage 2 Report

Goal:
Validate the first generated episode, then run a small official DynamicVLA scripted data-collection batch using the repo's own scripts with minimal modifications.

No training, no inference server, no evaluation server, no fake scenes, no repo patches unless explicitly reported as unavoidable.

## Start
Thu Jun 11 11:28:08 AM CEST 2026
ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
/home/redafrix/tests/internship/isaac_dynamicVLA-test

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  256G   31G  90% /

## Workspace check
total 88K
drwxrwxr-x  9 redafrix redafrix 4.0K Jun 11 11:07 .
drwxrwxr-x 15 redafrix redafrix 4.0K Jun 10 16:23 ..
drwxrwxr-x  4 redafrix redafrix 4.0K Jun 11 11:07 assets_staging
-rw-rw-r--  1 redafrix redafrix 1.2K Jun 11 10:09 cleanup_and_prepare.py
drwxrwxr-x  2 redafrix redafrix 4.0K Jun 11 11:12 datasets
-rw-rw-r--  1 redafrix redafrix 1.7K Jun 11 09:31 DOM_Part2.zip
drwxrwxr-x  2 redafrix redafrix 4.0K Jun 11 11:06 downloads
drwxrwxr-x  9 redafrix redafrix 4.0K Jun 11 11:06 dynamic-vla
-rw-rw-r--  1 redafrix redafrix  850 Jun 11 10:09 extract_links.py
-rw-rw-r--  1 redafrix redafrix 8.7K Jun 11 10:48 inventory_audit.py
drwxrwxr-x 11 redafrix redafrix 4.0K Jun 11 11:06 IsaacLab
lrwxrwxrwx  1 redafrix redafrix   23 Jun 11 11:03 isaacsim -> /home/redafrix/isaacsim
drwxrwxr-x  2 redafrix redafrix 4.0K Jun 11 11:07 logs
lrwxrwxrwx  1 redafrix redafrix   76 Jun 11 11:06 objects -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/objects
-rw-rw-r--  1 redafrix redafrix  215 Jun 11 10:11 read_readme.py
drwxrwxr-x  2 redafrix redafrix 4.0K Jun 11 11:28 reports
lrwxrwxrwx  1 redafrix redafrix   84 Jun 11 11:07 scenes -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes
-rw-rw-r--  1 redafrix redafrix  737 Jun 10 18:37 test_download
lrwxrwxrwx  1 redafrix redafrix   91 Jun 11 11:07 test-envs.txt -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt
lrwxrwxrwx  1 redafrix redafrix   83 Jun 11 11:07 tests -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests
-rw-rw-r--  1 redafrix redafrix  628 Jun 11 10:22 write_report.py

## Symlinks
lrwxrwxrwx 1 redafrix redafrix 62 Jun 11 11:06 IsaacLab/_isaac_sim -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim
lrwxrwxrwx 1 redafrix redafrix 23 Jun 11 11:03 isaacsim -> /home/redafrix/isaacsim
lrwxrwxrwx 1 redafrix redafrix 76 Jun 11 11:06 objects -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/objects
lrwxrwxrwx 1 redafrix redafrix 84 Jun 11 11:07 scenes -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes
lrwxrwxrwx 1 redafrix redafrix 91 Jun 11 11:07 test-envs.txt -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt
lrwxrwxrwx 1 redafrix redafrix 83 Jun 11 11:07 tests -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests

## Counts
- object USD count: 211
- scene USD count: 81
- test JSON count: 90
- test-envs.txt size: 91

## DynamicVLA git status
a27a06d2ca74d0e987a5e552e01013073e93cfd8

## Existing generated dataset files
datasets/place_franka_tomato02d_O02_00000042_e954.h5 | 114687874 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.json | 37328 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.mp4 | 1164912 bytes

[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
## Deep validation of existing generated outputs
h5_count: 1
json_count: 1
mp4_count: 1

### H5: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.h5 size= 114687874
top_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
DATASET action shape= (204, 8) dtype= float32
DATASET ee_pos shape= (204, 3) dtype= float32
DATASET ee_quat shape= (204, 4) dtype= float32
DATASET joints shape= (204, 9) dtype= float32
DATASET object_pos shape= (204, 3) dtype= float32
DATASET object_quat shape= (204, 4) dtype= float32
DATASET object_vel shape= (204, 3) dtype= float32
DATASET opst_cam_rgb shape= (204, 360, 480, 3) dtype= uint8
DATASET opst_cam_seg shape= (204, 360, 480, 1) dtype= uint8
DATASET side_cam_rgb shape= (204, 360, 480, 3) dtype= uint8
DATASET side_cam_seg shape= (204, 360, 480, 1) dtype= uint8
DATASET sm_state shape= (204,) dtype= int32
DATASET wrist_cam_rgb shape= (204, 360, 480, 3) dtype= uint8
DATASET wrist_cam_seg shape= (204, 360, 480, 1) dtype= uint8

### JSON: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.json size= 37328
top_keys: ['viewer', 'sim', 'ui_window_class_type', 'seed', 'decimation', 'scene', 'recorders', 'observations', 'actions', 'events', 'rerender_on_reset', 'wait_for_textures', 'xr', 'teleop_devices', 'export_io_descriptors', 'io_descriptors_output_dir', 'is_finite_horizon', 'episode_length_s', 'rewards', 'terminations', 'curriculum', 'commands', 'instruction']
instruction: {'task': 'place', 'objects': ['red tomato', 'red round tomato', 'round tomato', 'tomato'], 'containers': ['bowl with cyan patterns', 'ceramic bowl with cyan patterns', 'bowl', 'deep bowl', 'ceramic bowl', 'ceramic deep bowl with cyan patterns', 'deep bowl with cyan patterns', 'ceramic deep bowl']}
seed: 42

### MP4: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.mp4 size= 1164912

## Existing simulate logs important lines
### logs/simulate_place_franka_dom_test_n1.log


## Isaac process check before cleanup
redafrix    3602    2707  0 09:18 ?        00:00:00 server --sh -n /run/user/1000/.flatpak-helper/pkcs11-flatpak-3589 --provider p11-kit-trust.so pkcs11:model=p11-kit-trust?write-protected=yes


## simulate.py place/franka n=3 result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/simulate_place_franka_official_n3_stage2.log

Important lines:
[DEBUG] 2026-06-11 11:28:23,030 Using selector: EpollSelector
[DEBUG] 2026-06-11 11:28:27,628 Defining data type 'any' as 'Any'
[DEBUG] 2026-06-11 11:28:27,628 Defining data type 'bool' as 'Bool' and array 'BoolArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'bundle' as 'Bundle'
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'colord[3]' as 'Color3d' and array 'Color3dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'colorf[3]' as 'Color3f' and array 'Color3fArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'colorh[3]' as 'Color3h' and array 'Color3hArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'colord[4]' as 'Color4d' and array 'Color4dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'colorf[4]' as 'Color4f' and array 'Color4fArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'colorh[4]' as 'Color4h' and array 'Color4hArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'double' as 'Double' and array 'DoubleArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'double[2]' as 'Double2' and array 'Double2Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'double[3]' as 'Double3' and array 'Double3Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'double[4]' as 'Double4' and array 'Double4Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'execution' as 'Execution'
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'float' as 'Float' and array 'FloatArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'float[2]' as 'Float2' and array 'Float2Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'float[3]' as 'Float3' and array 'Float3Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'float[4]' as 'Float4' and array 'Float4Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'frame[4]' as 'Frame' and array 'FrameArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'half' as 'Half' and array 'HalfArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'half[2]' as 'Half2' and array 'Half2Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'half[3]' as 'Half3' and array 'Half3Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'half[4]' as 'Half4' and array 'Half4Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'int' as 'Int' and array 'IntArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'int[2]' as 'Int2' and array 'Int2Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'int[3]' as 'Int3' and array 'Int3Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'int[4]' as 'Int4' and array 'Int4Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'int64' as 'Int64' and array 'Int64Array
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'matrixd[2]' as 'Matrix2d' and array 'Matrix2dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'matrixd[3]' as 'Matrix3d' and array 'Matrix3dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'matrixd[4]' as 'Matrix4d' and array 'Matrix4dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'normald[3]' as 'Normal3d' and array 'Normal3dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'normalf[3]' as 'Normal3f' and array 'Normal3fArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'normalh[3]' as 'Normal3h' and array 'Normal3hArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'objectId' as 'ObjectId' and array 'ObjectIdArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'path' as 'Path'
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'pointd[3]' as 'Point3d' and array 'Point3dArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'pointf[3]' as 'Point3f' and array 'Point3fArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'pointh[3]' as 'Point3h' and array 'Point3hArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'quatd[4]' as 'Quatd' and array 'QuatdArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'quatf[4]' as 'Quatf' and array 'QuatfArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'quath[4]' as 'Quath' and array 'QuathArray
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'string' as 'String'
[DEBUG] 2026-06-11 11:28:27,629 Defining data type 'target' as 'Target'
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'texcoordd[2]' as 'TexCoord2d' and array 'TexCoord2dArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'texcoordf[2]' as 'TexCoord2f' and array 'TexCoord2fArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'texcoordh[2]' as 'TexCoord2h' and array 'TexCoord2hArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'texcoordd[3]' as 'TexCoord3d' and array 'TexCoord3dArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'texcoordf[3]' as 'TexCoord3f' and array 'TexCoord3fArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'texcoordh[3]' as 'TexCoord3h' and array 'TexCoord3hArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'timecode' as 'Timecode' and array 'TimecodeArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'token' as 'Token' and array 'TokenArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'uchar' as 'UChar' and array 'UCharArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'uint' as 'UInt' and array 'UIntArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'uint64' as 'UInt64' and array 'UInt64Array
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'vectord[3]' as 'Vector3d' and array 'Vector3dArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'vectorf[3]' as 'Vector3f' and array 'Vector3fArray
[DEBUG] 2026-06-11 11:28:27,630 Defining data type 'vectorh[3]' as 'Vector3h' and array 'Vector3hArray
2026-06-11 09:28:22 [2ms] [Warning] [omni.ext.plugin] [ext: rendering_modes] Extensions config 'extension.toml' doesn't exist '/home/redafrix/isaac_franka_env_probe/IsaacLab/apps/isaacsim_4_5/rendering_modes' or '/home/redafrix/isaac_franka_env_probe/IsaacLab/apps/isaacsim_4_5/rendering_modes/config'
2026-06-11 09:28:29 [6,517ms] [Warning] [omni.kit.menu.utils.app_menu] add_menu_items: menu [<MenuItemDescription name:'New'>, <MenuItemDescription name:'Open'>, <MenuItemDescription name:'Re-open with New Edit Layer'>, <MenuItemDescription name:'Save'>, <MenuItemDescription name:'Save With[DEBUG] 2026-06-11 11:28:29,749 matplotlib data path: /home/redafrix/isaacsim/exts/omni.isaac.core_archive/pip_prebundle/matplotlib/mpl-data
[DEBUG] 2026-06-11 11:28:29,754 CONFIGDIR=/home/redafrix/.config/matplotlib
[DEBUG] 2026-06-11 11:28:29,756 interactive is False
[DEBUG] 2026-06-11 11:28:29,756 platform is linux
[DEBUG] 2026-06-11 11:28:29,908 CACHEDIR=/home/redafrix/.cache/matplotlib
[DEBUG] 2026-06-11 11:28:29,910 Using fontManager instance from /home/redafrix/.cache/matplotlib/fontlist-v330.json
2026-06-11 09:28:31 [8,884ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults/sceneDb/ambientLightIntensity'
2026-06-11 09:28:31 [9,008ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 7508933632
2026-06-11 09:28:31 [9,008ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid false, within: false
2026-06-11 09:28:31 [9,008ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : decrement: 167690, decrement size: 7433845248
2026-06-11 09:28:31 [9,008ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : New limit 9574251 (slope: 447, intercept: 13179904)
2026-06-11 09:28:31 [9,008ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 4287216384
2026-06-11 09:28:31 [9,008ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid true, within: true
2026-06-11 09:28:43 [20,655ms] [Warning] [carb] Client rtx.scenedb.plugin has acquired [carb::settings::ISettings v1.0] 100 times. Consider accessing this interface with carb::getCachedInterface() (Performance warning)
2026-06-11 09:33:08[WARNING] 2026-06-11 11:33:10,103 Metadata found for unknown object tray00.usd.
[WARNING] 2026-06-11 11:33:10,104 Metadata found for unknown object tray01.usd.
[WARNING] 2026-06-11 11:33:10,104 Metadata found for unknown object tray02.usd.
[WARNING] 2026-06-11 11:33:10,104 Metadata found for unknown object tray03.usd.
[INFO] 2026-06-11 11:33:10,129 Loading scene from /home/redafrix/tests/internship/isaac_dynamicVLA-test/scenes/e249a0e2-e0ef-4af4-81ab-945e6973e53f.usd
[DEBUG] 2026-06-11 11:33:11,224 [Table_00004] Anchor [ 0.4720019  -1.36076364  0.52993369] collides with Chair_00037
[DEBUG] 2026-06-11 11:33:11,225 [Table_00004] Anchor [ 0.4720019  -0.75226959  0.52993369] collides with Chair_00038
[DEBUG] 2026-06-11 11:33:11,231 [Table_00004] Anchor [ 1.80778896 -1.05651662  0.52993369] collides with WallInner_00087
[DEBUG] 2026-06-11 11:33:11,251 [Coffee_Table_00022] Camera side_cam of [ 0.18097    -4.13325196  0.29950136] collides with Sofa_00041
[INFO] 2026-06-11 11:33:12,346 Using target object: orange05.usd
[INFO] 2026-06-11 11:33:12,347 Using container object: box12.usd
[DEBUG] 2026-06-11 11:33:12,380 Object tags: {'objects': ['orange', 'yellow orange'], 'containers': ['box', 'plastic box', 'white box', 'white box with Tencent Logo', 'box with Tencent Logo']}
2026-06-11 09:33:10 [287,392ms] [Warning] [root] Metadata found for unknown object tray00.usd.
2026-06-11 09:33:10 [287,392ms] [Warning] [root] Metadata found for unknown object tray01.usd.
2026-06-11 09:33:10 [287,392ms] [Warning] [root] Metadata found for unknown object tray02.usd.
2026-06-11 09:33:10 [287,392ms] [Warning] [root] Metadata found for unknown object tray03.usd.
[INFO] 2026-06-11 11:33:42,269 Loading scene from /home/redafrix/tests/internship/isaac_dynamicVLA-test/scenes/d0615bd5-c5af-474b-a2bf-c434fcfaf74c.usd
[DEBUG] 2026-06-11 11:33:43,542 [Table_00143] Anchor [2.37960985 4.62234506 0.74934268] collides with WallInner_00169
[DEBUG] 2026-06-11 11:33:43,580 [Coffee_Table_00149] Camera side_cam of [ 2.26278    -0.18545798  0.38398743] collides with Sofa_00142
[INFO] 2026-06-11 11:33:44,757 Using target object: fcan17.usd
[INFO] 2026-06-11 11:33:44,758 Using container object: box08.usd
[DEBUG] 2026-06-11 11:33:44,761 Object tags: {'objects': ['yellow and red food can with golden bull logo', 'food can', 'yellow and red food can', 'food can with golden bull logo'], 'containers': ['box with MMLab At NTU words', 'box', 'plastic box', 'red box with MMLab At NTU words', 'red box']}
2026-06-11 09:33:15 [293,288ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:33:16 [293,313ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:33:16 [293,331ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:33:19 [296,894ms] [Warning] [rtx.postprocessing.plugin] DLSS increasing input dimensions: Render resolution of (278, 209) is below minimal input resolution of 300.
2026-06-11 09:33:45 [322,750ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:33:45 [322,777ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:33:45 [322,794ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:33:46 [323,340ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,340ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_001!
2026-06-11 09:33:46 [323,341ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,341ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_002!
2026-06-11 09:33:46 [323,342ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,342ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_003!
2026-06-11 09:33:46 [323,349ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,349ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_glass_001!
2026-06-11 09:33:46 [323,372ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,372ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_005!
2026-06-11 09:33:46 [323,374ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,374ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_006!
2026-06-11 09:33:46 [323,375ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,375ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_007!
2026-06-11 09:33:46 [323,376ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,376ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_008!
2026-06-11 09:33:46 [323,379ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,379ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_glass_002!
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_010!
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_001!
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_002!
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_003!
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,380ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_glass_001!
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_005!
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_006!
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_007!
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_008!
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_glass_002!
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,381ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_010!
2026-06-11 09:33:46 [323,397ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,397ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00163/Lighting_00161_solid_001!
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00163/Lighting_00161_glass_001!
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00165/Lighting_00164_solid_001!
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00165/Lighting_00164_glass_001!
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00167/Lighting_00166_solid_001!
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL., FILE /builds/omniverse/physics/physx/source/physx/src/NpFactory.cpp, LINE 810
2026-06-11 09:33:46 [323,399ms] [Error] [omni.physx.plugin] PhysX Shape failed to be created on a prim: /World/envs/env_0/House/furniture/Lighting_00167/Lighting_00166_glass_001!
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_glass_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_glass_002)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_002)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_003)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_005)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_006)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_007)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_008)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00160/Lighting_00159_solid_010)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_glass_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_glass_002)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_002)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_003)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_005)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_006)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_007)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_008)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00162/Lighting_00161_solid_010)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00163/Lighting_00161_glass_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00163/Lighting_00161_solid_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00165/Lighting_00164_glass_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00165/Lighting_00164_solid_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00167/Lighting_00166_glass_001)
2026-06-11 09:33:46 [323,476ms] [Error] [omni.physx.plugin] Static body transformation not valid, prim (/World/envs/env_0/House/furniture/Lighting_00167/Lighting_00166_solid_001)
[INFO][AppLauncher]: Loading experience file: /home/redafrix/isaac_franka_env_probe/IsaacLab/apps/isaacsim_4_5/isaaclab.python.rendering.kit
	Rendering step-size   : 0.04
[INFO]: Time taken for scene creation : 2.254887 seconds
[INFO]: Scene manager:  <class InteractiveScene>
|   0   | object_pose | UniformPoseCommand |
|    1    | reset_object_position      |
|    2     | object_position                     |   (3,)   |
|    3     | target_object_position              |   (7,)   |
|   1   | object_dropping    |   True   |
|   2   | objects_placed     |  False   |
|   0   | reaching_object                   |     1.0 |
|   1   | lifting_object                    |    15.0 |
|   2   | object_goal_tracking              |    16.0 |
|   3   | object_goal_tracking_fine_grained |     5.0 |
	Rendering step-size   : 0.04
[INFO]: Time taken for scene creation : 0.607986 seconds
[INFO]: Scene manager:  <class InteractiveScene>
|   0   | object_pose | UniformPoseCommand |
|    1    | reset_object_position      |
|    2     | object_position                     |   (3,)   |
|    3     | target_object_position              |   (7,)   |
|   1   | object_dropping    |   True   |
|   2   | objects_placed     |  False   |
[INFO] Reward Manager:  [INFO] 2026-06-11 11:34:00,580 Saving episode place_franka_fcan17d_O02_00000101_fb10 with 118 frames.
[DEBUG] 2026-06-11 11:34:05,479 {'objects': ['yellow and red food can with golden bull logo', 'food can', 'yellow and red food can', 'food can with golden bull logo'], 'containers': ['box with MMLab At NTU words', 'box', 'plastic box', 'red box with MMLab At NTU words', 'red box']}
[INFO] 2026-06-11 11:34:05,484 Loading scene from /home/redafrix/tests/internship/isaac_dynamicVLA-test/scenes/e249a0e2-e0ef-4af4-81ab-945e6973e53f.usd
[DEBUG] 2026-06-11 11:34:06,796 [Table_00004] Anchor [ 0.4720019  -1.36076364  0.52993369] collides with Chair_00037
[DEBUG] 2026-06-11 11:34:06,797 [Table_00004] Anchor [ 0.4720019  -0.75226959  0.52993369] collides with Chair_00038
[DEBUG] 2026-06-11 11:34:06,806 [Table_00004] Anchor [ 1.80778896 -1.05651662  0.52993369] collides with WallInner_00087
[DEBUG] 2026-06-11 11:34:06,830 [Coffee_Table_00022] Camera side_cam of [ 0.18097    -4.13325196  0.29950136] collides with Sofa_00041
[INFO] 2026-06-11 11:34:07,993 Using target object: lemon08.usd
[INFO] 2026-06-11 11:34:07,994 Using container object: box10.usd
[DEBUG] 2026-06-11 11:34:07,997 Object tags: {'objects': ['lemon'], 'containers': ['white box with Google Logo', 'box', 'plastic box', 'white box', 'box with Google Logo']}
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:33:47 [324,822ms] [Warning] [omni.kit.notification_manager.manager] PhysX error: Supplied PxGeometry is not valid. Shape creation method returns NULL.
2026-06-11 09:34:08 [346,044ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:34:08 [346,069ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:34:08 [346,086ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.

## Dataset outputs after n=3
datasets/place_franka_fcan17d_O02_00000101_fb10.h5 | 51426904 bytes
datasets/place_franka_fcan17d_O02_00000101_fb10.json | 37183 bytes
datasets/place_franka_fcan17d_O02_00000101_fb10.mp4 | 597229 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.h5 | 114687874 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.json | 37328 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.mp4 | 1164912 bytes

Counts:
- H5: 2
- JSON: 2
- MP4: 2

Disk:
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  256G   31G  90% /
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
## Deep validation of existing generated outputs
h5_count: 2
json_count: 2
mp4_count: 2

### H5: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_fcan17d_O02_00000101_fb10.h5 size= 51426904
top_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
DATASET action shape= (118, 8) dtype= float32
DATASET ee_pos shape= (118, 3) dtype= float32
DATASET ee_quat shape= (118, 4) dtype= float32
DATASET joints shape= (118, 9) dtype= float32
DATASET object_pos shape= (118, 3) dtype= float32
DATASET object_quat shape= (118, 4) dtype= float32
DATASET object_vel shape= (118, 3) dtype= float32
DATASET opst_cam_rgb shape= (118, 360, 480, 3) dtype= uint8
DATASET opst_cam_seg shape= (118, 360, 480, 1) dtype= uint8
DATASET side_cam_rgb shape= (118, 360, 480, 3) dtype= uint8
DATASET side_cam_seg shape= (118, 360, 480, 1) dtype= uint8
DATASET sm_state shape= (118,) dtype= int32
DATASET wrist_cam_rgb shape= (118, 360, 480, 3) dtype= uint8
DATASET wrist_cam_seg shape= (118, 360, 480, 1) dtype= uint8

### H5: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.h5 size= 114687874
top_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
DATASET action shape= (204, 8) dtype= float32
DATASET ee_pos shape= (204, 3) dtype= float32
DATASET ee_quat shape= (204, 4) dtype= float32
DATASET joints shape= (204, 9) dtype= float32
DATASET object_pos shape= (204, 3) dtype= float32
DATASET object_quat shape= (204, 4) dtype= float32
DATASET object_vel shape= (204, 3) dtype= float32
DATASET opst_cam_rgb shape= (204, 360, 480, 3) dtype= uint8
DATASET opst_cam_seg shape= (204, 360, 480, 1) dtype= uint8
DATASET side_cam_rgb shape= (204, 360, 480, 3) dtype= uint8
DATASET side_cam_seg shape= (204, 360, 480, 1) dtype= uint8
DATASET sm_state shape= (204,) dtype= int32
DATASET wrist_cam_rgb shape= (204, 360, 480, 3) dtype= uint8
DATASET wrist_cam_seg shape= (204, 360, 480, 1) dtype= uint8

### JSON: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_fcan17d_O02_00000101_fb10.json size= 37183
top_keys: ['viewer', 'sim', 'ui_window_class_type', 'seed', 'decimation', 'scene', 'recorders', 'observations', 'actions', 'events', 'rerender_on_reset', 'wait_for_textures', 'xr', 'teleop_devices', 'export_io_descriptors', 'io_descriptors_output_dir', 'is_finite_horizon', 'episode_length_s', 'rewards', 'terminations', 'curriculum', 'commands', 'instruction']
instruction: {'task': 'place', 'objects': ['yellow and red food can with golden bull logo', 'food can', 'yellow and red food can', 'food can with golden bull logo'], 'containers': ['box with MMLab At NTU words', 'box', 'plastic box', 'red box with MMLab At NTU words', 'red box']}
seed: 101

### JSON: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.json size= 37328
top_keys: ['viewer', 'sim', 'ui_window_class_type', 'seed', 'decimation', 'scene', 'recorders', 'observations', 'actions', 'events', 'rerender_on_reset', 'wait_for_textures', 'xr', 'teleop_devices', 'export_io_descriptors', 'io_descriptors_output_dir', 'is_finite_horizon', 'episode_length_s', 'rewards', 'terminations', 'curriculum', 'commands', 'instruction']
instruction: {'task': 'place', 'objects': ['red tomato', 'red round tomato', 'round tomato', 'tomato'], 'containers': ['bowl with cyan patterns', 'ceramic bowl with cyan patterns', 'bowl', 'deep bowl', 'ceramic bowl', 'ceramic deep bowl with cyan patterns', 'deep bowl with cyan patterns', 'ceramic deep bowl']}
seed: 42

### MP4: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_fcan17d_O02_00000101_fb10.mp4 size= 597229

### MP4: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.mp4 size= 1164912
Skipping pick: place n=3 did not pass cleanly (H5 count is 2, bad log matches: ).
Preparing translate_dataset_seq.py on generated raw datasets.

## Process check before translate_dataset_seq.py


## translate_dataset_seq.py result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/translate_dataset_seq_stage2.log
2026-06-11 09:35:02 [[INFO] 2026-06-11 11:37:51,515 Recovering test environment from /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_fcan17d_O02_00000101_fb10.json
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla/scripts/translate_dataset_seq.py", line 366, in <module>
  File "/home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla/scripts/translate_dataset_seq.py", line 245, in main
TypeError: get_test_env() takes 9 positional arguments but 10 were given

# FINAL SUMMARY
- workspace: /home/redafrix/tests/internship/isaac_dynamicVLA-test
- object USD count: 211
- scene USD count: 81
- test JSON count: 90
- test-envs.txt size: 91
- raw H5 count: 2
- raw JSON count: 2
- raw MP4 count: 2
- translated output files: 0

## Raw dataset files
datasets/place_franka_fcan17d_O02_00000101_fb10.h5 | 51426904 bytes
datasets/place_franka_fcan17d_O02_00000101_fb10.json | 37183 bytes
datasets/place_franka_fcan17d_O02_00000101_fb10.mp4 | 597229 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.h5 | 114687874 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.json | 37328 bytes
datasets/place_franka_tomato02d_O02_00000042_e954.mp4 | 1164912 bytes

## Translated dataset files

## Logs
logs/dom_test_ready_flag.txt | 4 bytes
logs/simulate_place_franka_dom_test_n1.log | 245160 bytes
logs/simulate_place_franka_official_n3_stage2.log | 283176 bytes
logs/translate_dataset_seq_stage2.log | 14502 bytes

## Git diff

## Final disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  256G   31G  90% /
