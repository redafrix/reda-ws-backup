# Static Collection V1 Report

Goal:
Minimal static-object adaptation of DynamicVLA scripted data collection.

Static means:
- object is physics-enabled
- gravity/contact remain enabled
- no initial sliding velocity before robot interaction
- scripted robot controller remains original
- output schema remains compatible

## Static repo path
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1

## Relevant moving_speed lines
simulations/simulate.py:100:def get_env_cfg(sim_cfg, task, robot, object_metadata, scene_dir):
simulations/simulate.py:303:        random_static = (
simulations/simulate.py:311:            None if random_static else object_cfg.get("moving_speed", None),
simulations/simulate.py:411:    moving_speed,
simulations/simulate.py:415:    if moving_speed is None:
simulations/simulate.py:416:        object_state = _get_static_object_state(
simulations/simulate.py:420:        object_state = _get_dynamic_object_state(
simulations/simulate.py:423:            moving_speed,
simulations/simulate.py:431:def _get_static_object_state(object_range_bbox, object_z, random_orientation):
simulations/simulate.py:450:def _get_dynamic_object_state(
simulations/simulate.py:451:    object_range_bbox, object_z, moving_speed, friction, robot_position
simulations/simulate.py:469:    assert moving_speed is not None and len(moving_speed) == 2
simulations/simulate.py:474:        * random.uniform(*moving_speed)
simulations/simulate.py:481:        "lin_vel": object_velocity,
simulations/simulate.py:513:                    eo["pos"], eo["size"], eo["quat"], eo.get("lin_vel", None)
simulations/simulate.py:525:def _get_object_bbox(position, size, quat, lin_vel=None):
simulations/simulate.py:696:        # object_root_lin_vel_w = _get_merged_object_state(object_state, "root_lin_vel_w")
simulations/simulate.py:705:                object_state.root_lin_vel_w, robot_quat
simulations/simulate.py:804:            [scene[o].data.root_lin_vel_w[i : i + 1] for o in objects], dim=0
simulations/simulate.py:1008:    init_speed = np.linalg.norm(scene_cfg["object"]["init_state"]["lin_vel"])
simulations/simulate.py:1019:    init_velocity = scene_cfg["object"]["init_state"]["lin_vel"]
simulations/simulate.py:1040:    object_vel = np.linalg.norm(scene_cfg["object"]["init_state"]["lin_vel"])
simulations/simulate.py:1312:    parser.add_argument(
simulations/simulate.py:1318:    parser.add_argument(
simulations/simulate.py:1321:    parser.add_argument(
simulations/simulate.py:1331:    parser.add_argument("--robot", default="franka")
simulations/simulate.py:1332:    parser.add_argument(
simulations/simulate.py:1335:    parser.add_argument(
simulations/simulate.py:1338:    parser.add_argument(
simulations/simulate.py:1341:    parser.add_argument("--task", default="pick")
simulations/simulate.py:1342:    parser.add_argument(
simulations/simulate.py:1347:    parser.add_argument("--debug", action="store_true", default=False)
simulations/simulate.py:1348:    parser.add_argument("--disable_sm", action="store_true", default=False)
simulations/simulate.py:1349:    parser.add_argument("--path_tracing", action="store_true", default=False)
simulations/simulate.py:1350:    parser.add_argument("--seed", type=int, default=None)
simulations/simulate.py:1351:    parser.add_argument("-n", "--n_simulations", type=int, default=10_000)
simulations/configs/sim_cfg.yaml:16:    moving_speed: [0.15, 0.75] # range of speed for moving objects, generated uniformly random
simulations/configs/sim_cfg.yaml:17:    # moving_speed: [0.05, 0.25]
simulations/configs/object_cfg.py:24:    if "lin_vel" in obj_cfg:
simulations/configs/object_cfg.py:25:        init_state.lin_vel = obj_cfg["lin_vel"]
simulations/configs/object_cfg.py:83:    init_lin_vel: list[float], upright=False, perturbation=None
simulations/configs/object_cfg.py:86:    lin_vel_angle = np.arctan2(init_lin_vel[1], init_lin_vel[0])
simulations/configs/object_cfg.py:89:        lin_vel_angle += np.deg2rad(perturbation)
simulations/configs/object_cfg.py:97:            lin_vel_angle,

## Current simulate.py git-less checksum
02dce8ecdd1bd1f5aba48c72f53cb15f946bbe6db182beb5ab86c924132c88fd  simulations/simulate.py

## Diff after static patch
--- simulations/simulate.py.bak_static_v1	2026-06-11 15:44:31.903353664 +0200
+++ simulations/simulate.py	2026-06-11 15:44:31.925353975 +0200
@@ -1211,6 +1211,18 @@
 def main(args):
     with open(args.sim_cfg_file) as fp:
         sim_cfg = yaml.load(fp, Loader=yaml.FullLoader)
+    # STATIC_OBJECTS_V1_PATCH:
+    # Keep the original scripted collector and physics, but remove the intentional
+    # initial object velocity used for dynamic-object data.
+    if getattr(args, "static_objects", False):
+        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["moving_speed"] = None
+        perturb = sim_cfg.setdefault("scene", {}).setdefault("objects", {}).get("perturbation", [])
+        if isinstance(perturb, list):
+            sim_cfg["scene"]["objects"]["perturbation"] = [
+                p for p in perturb if str(p).upper() != "VELOCITY"
+            ]
+        logging.info("STATIC_OBJECTS_V1 enabled: objects keep physics/gravity but initial moving_speed is disabled.")
+
 
     sim_cfg.update(
         {
@@ -1348,6 +1360,12 @@
     parser.add_argument("--disable_sm", action="store_true", default=False)
     parser.add_argument("--path_tracing", action="store_true", default=False)
     parser.add_argument("--seed", type=int, default=None)
+    parser.add_argument(
+        "--static_objects",
+        action="store_true",
+        default=False,
+        help="Static-object data collection: keep physics/gravity, but disable initial object velocity by forcing moving_speed=None.",
+    )
     parser.add_argument("-n", "--n_simulations", type=int, default=10_000)
     args = parser.parse_args(script_args)
     # Copy the shared parameters from isaaclab_args to args

## Check static flag exists
1214:    # STATIC_OBJECTS_V1_PATCH:
1217:    if getattr(args, "static_objects", False):
1224:        logging.info("STATIC_OBJECTS_V1 enabled: objects keep physics/gravity but initial moving_speed is disabled.")
1364:        "--static_objects",

## Experiment symlinks
lrwxrwxrwx 1 redafrix redafrix 105 Jun 11 15:44 /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/datasets -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw
lrwxrwxrwx 1 redafrix redafrix 112 Jun 11 15:44 /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/datasets-tr -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
## Static V1 raw inspection
h5_count 3
json_count 3
mp4_count 3

### place_franka_apple12s_O02_00000700_b4c3.h5
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 115
object_vel_first_25_norms_min_mean_max 0.0 0.012273618020117283 0.03716529533267021
object_vel_first_10 [[0.0, 0.0, 0.0], [-0.0005139054264873266, -0.0026778639294207096, 5.7625795307103544e-05], [0.0022531934082508087, 0.011737192049622536, -0.0006646193214692175], [0.0032283347100019455, 0.016813959926366806, -0.0010012993589043617], [0.001008546445518732, 0.005241595208644867, 0.0002381825470365584], [-0.0007890136912465096, -0.00413843709975481, 0.0003024125180672854], [0.0002559019485488534, 0.001287293853238225, -0.0002672906266525388], [0.0025063185021281242, 0.0129740284755826, -0.0009188249241560698], [0.0022604037076234818, 0.011638102121651173, -0.0007300662691704929], [0.00027651875279843807, 0.0012041877489537, -9.44273269851692e-05]]
wrist_cam_rgb (115, 360, 480, 3) uint8
side_cam_rgb (115, 360, 480, 3) uint8
opst_cam_rgb (115, 360, 480, 3) uint8

### place_franka_peach06s_O02_00000702_c698.h5
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 113
object_vel_first_25_norms_min_mean_max 0.0 7.155352754750766e-09 7.453591521766612e-09
object_vel_first_10 [[0.0, 0.0, 0.0], [-2.2842602809269863e-11, -1.8272316992806736e-10, -7.450580596923828e-09], [-2.6279409204299498e-11, -2.1021229201778624e-10, -7.450580596923828e-09], [-2.626319994813997e-11, -2.1008794703902822e-10, -7.450566386069113e-09], [-2.6239219130808067e-11, -2.098889950730154e-10, -7.450566386069113e-09], [-2.621634853650079e-11, -2.0969714853436017e-10, -7.450566386069113e-09], [-2.6193255897588585e-11, -2.0951596013674134e-10, -7.450566386069113e-09], [-2.6168164857232057e-11, -2.0932056088440731e-10, -7.450566386069113e-09], [-2.614529426292478e-11, -2.0912160891839449e-10, -7.450566386069113e-09], [-2.612109140098795e-11, -2.0892976237973926e-10, -7.450566386069113e-09]]
wrist_cam_rgb (113, 360, 480, 3) uint8
side_cam_rgb (113, 360, 480, 3) uint8
opst_cam_rgb (113, 360, 480, 3) uint8

### place_franka_tangerine04s_O02_00000701_0b41.h5
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 300
object_vel_first_25_norms_min_mean_max 0.0 0.009369566105306149 0.03171965852379799
object_vel_first_10 [[0.0, 0.0, 0.0], [0.0009444181923754513, -0.001320857205428183, 2.5550723421474686e-06], [-0.007451403886079788, 0.010419138707220554, -0.0007323800818994641], [-0.009307927452027798, 0.013016881421208382, -0.0009689381113275886], [-0.0030872703064233065, 0.004318649414926767, 0.0002271333651151508], [0.0020103338174521923, -0.0028075079899281263, -0.0001220177291543223], [0.0004601955588441342, -0.0006382747087627649, -8.891147444956005e-05], [-0.006563223898410797, 0.00918545387685299, -0.0008566827746108174], [-0.007331183645874262, 0.010266204364597797, -0.0008136790711432695], [-0.0015772075857967138, 0.002230175770819187, -0.00021570468379650265]]
wrist_cam_rgb (300, 360, 480, 3) uint8
side_cam_rgb (300, 360, 480, 3) uint8
opst_cam_rgb (300, 360, 480, 3) uint8

JSON place_franka_apple12s_O02_00000700_b4c3.json
instruction {'task': 'place', 'objects': ['round apple', 'apple', 'red apple', 'red round apple'], 'containers': ['box', 'box with Tesla Logo', 'white box', 'white box with Tesla Logo', 'plastic box']}
json_object_init_lin_vel [0.0, 0.0, 0.0]

JSON place_franka_peach06s_O02_00000702_c698.json
instruction {'task': 'place', 'objects': ['white peach', 'peach'], 'containers': ['box', 'black box with Apple Logo', 'plastic box', 'black box', 'box with Apple Logo']}
json_object_init_lin_vel [0.0, 0.0, 0.0]

JSON place_franka_tangerine04s_O02_00000701_0b41.json
instruction {'task': 'place', 'objects': ['tangerine'], 'containers': ['woven mat', 'woven mat with natural rattan texture', 'woven rattan mat', 'square woven mat', 'square mat with straw texture texture']}
json_object_init_lin_vel [0.0, 0.0, 0.0]

# FINAL STATIC V1 SUMMARY
- static repo: /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1
- experiment: /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1
- raw H5 count: 3
- raw JSON count: 3
- raw MP4 count: 3
- translated H5 count: 3
- translated JSON count: 3
- videos count: 6

## Raw files
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_apple12s_O02_00000700_b4c3.h5 | 52146661 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_apple12s_O02_00000700_b4c3.json | 37127 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_apple12s_O02_00000700_b4c3.mp4 | 556427 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_peach06s_O02_00000702_c698.h5 | 56006197 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_peach06s_O02_00000702_c698.json | 36971 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_peach06s_O02_00000702_c698.mp4 | 500002 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_tangerine04s_O02_00000701_0b41.h5 | 139120172 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_tangerine04s_O02_00000701_0b41.json | 37139 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_tangerine04s_O02_00000701_0b41.mp4 | 1538307 bytes

## Translated files
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_apple12s_O02_00000700_b4c3-FAIL.mp4 | 584715 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_apple12s_O02_00000700_b4c3-tr.h5 | 52461195 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_apple12s_O02_00000700_b4c3-tr.json | 37114 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_peach06s_O02_00000702_c698-SUCCESS.mp4 | 517928 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_peach06s_O02_00000702_c698-tr.h5 | 55968787 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_peach06s_O02_00000702_c698-tr.json | 36958 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_tangerine04s_O02_00000701_0b41-FAIL.mp4 | 1523502 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_tangerine04s_O02_00000701_0b41-tr.h5 | 139809109 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_tangerine04s_O02_00000701_0b41-tr.json | 37126 bytes

## Videos
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/videos/place_franka_apple12s_O02_00000700_b4c3_multicam.mp4 | 2672452 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/videos/place_franka_apple12s_O02_00000700_b4c3-tr_multicam.mp4 | 2796131 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/videos/place_franka_peach06s_O02_00000702_c698_multicam.mp4 | 2560355 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/videos/place_franka_peach06s_O02_00000702_c698-tr_multicam.mp4 | 2644593 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/videos/place_franka_tangerine04s_O02_00000701_0b41_multicam.mp4 | 8319233 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/videos/place_franka_tangerine04s_O02_00000701_0b41-tr_multicam.mp4 | 8388936 bytes

## Dev patch
--- /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py.bak_static_v1	2026-06-11 15:44:31.903353664 +0200
+++ /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py	2026-06-11 15:44:31.925353975 +0200
@@ -1211,6 +1211,18 @@
 def main(args):
     with open(args.sim_cfg_file) as fp:
         sim_cfg = yaml.load(fp, Loader=yaml.FullLoader)
+    # STATIC_OBJECTS_V1_PATCH:
+    # Keep the original scripted collector and physics, but remove the intentional
+    # initial object velocity used for dynamic-object data.
+    if getattr(args, "static_objects", False):
+        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["moving_speed"] = None
+        perturb = sim_cfg.setdefault("scene", {}).setdefault("objects", {}).get("perturbation", [])
+        if isinstance(perturb, list):
+            sim_cfg["scene"]["objects"]["perturbation"] = [
+                p for p in perturb if str(p).upper() != "VELOCITY"
+            ]
+        logging.info("STATIC_OBJECTS_V1 enabled: objects keep physics/gravity but initial moving_speed is disabled.")
+
 
     sim_cfg.update(
         {
@@ -1348,6 +1360,12 @@
     parser.add_argument("--disable_sm", action="store_true", default=False)
     parser.add_argument("--path_tracing", action="store_true", default=False)
     parser.add_argument("--seed", type=int, default=None)
+    parser.add_argument(
+        "--static_objects",
+        action="store_true",
+        default=False,
+        help="Static-object data collection: keep physics/gravity, but disable initial object velocity by forcing moving_speed=None.",
+    )
     parser.add_argument("-n", "--n_simulations", type=int, default=10_000)
     args = parser.parse_args(script_args)
     # Copy the shared parameters from isaaclab_args to args

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  259G   28G  91% /
