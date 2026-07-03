# Static Collection V3 True Stable Spawn + Physics Gate Report

Goal:
Fix the real static spawn orientation path and add conservative physics-quality checks.

Problems:
- V2 did not truly force yaw-only/upright spawn.
- Some demos look physically invalid.
- Objects can roll too much or traverse bowls/containers.

V3 principles:
- Keep physics/gravity/collisions enabled.
- Remove intentional object velocity.
- Force stable yaw-only/upright spawn through the real object-state path.
- Do not broadly change friction/materials yet.
- Reject clearly bad physics episodes instead of hiding them.
## Before patch relevant code
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:158:    object_states = _get_object_states(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:284:def _get_object_states(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:302:        random_orientation = random.random() < object_cfg.get("prob_rnd_quat", 0.5)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:306:        random_friction = np.random.uniform(*object_cfg.get("friction", [0, 0]))
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:307:        _state = _get_object_state(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:312:            random_friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:313:            random_orientation,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:346:                random_orientation,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:407:def _get_object_state(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:412:    friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:413:    random_orientation,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:416:        object_state = _get_static_object_state(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:417:            object_range_bbox, object_z, random_orientation, friction
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:424:            friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:431:def _get_static_object_state(object_range_bbox, object_z, random_orientation, friction=0.0):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:445:    if random_orientation == "yaw_only":
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:450:        if random_orientation:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:451:            object_quat = configs.object_cfg.get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:455:    return {"pos": object_position, "quat": object_quat, "friction": friction}
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:459:    object_range_bbox, object_z, moving_speed, friction, robot_position
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:479:    object_velocity = (
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:484:    object_quat = configs.object_cfg.get_object_init_quat(object_velocity)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:489:        "lin_vel": object_velocity,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:490:        "friction": friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:495:    container_size, object_range_bbox, random_orientation, existing_objects
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:512:        if random_orientation:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:513:            container_quat = configs.object_cfg.get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:578:                friction=target_object.get("friction", 0.0),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:595:                    friction=o.get("friction", 0.0),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:666:    materials = target_object.root_physx_view.get_material_properties()
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:667:    materials[..., 0] = 0.9  # Static friction.
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:668:    materials[..., 1] = 1.0  # Dynamic friction.
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:669:    materials[..., 2] = 0.0  # Restitution
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:671:        materials, torch.arange(n_envs)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:829:        "object_vel": ("curr_state", "object", "velocity"),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1015:def is_object_stopped(scene_cfg, object_velocity, n_steps=25):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1018:    for i in range(min(n_steps, len(object_velocity))):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1019:        if init_speed > 1e-2 and np.linalg.norm(object_velocity[i]) < 1e-2:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1025:def is_object_direction_changed(scene_cfg, object_velocity, n_steps=25):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1030:    for i in range(min(n_steps, len(object_velocity))):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1031:        dir_idx = helpers.get_direction_index(object_velocity[i])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1038:def get_episode_name(task, robot, seed, scene_cfg):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1048:    object_vel = np.linalg.norm(scene_cfg["object"]["init_state"]["lin_vel"])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1061:        "d" if object_vel > 1e-3 else "s",
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1091:    env_state, state_keys=["sm_state", "ee_pos", "object_pos", "object_vel"]
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1227:    if getattr(args, "static_stable_spawn", False):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1229:        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["static_stable_spawn"] = True
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1230:        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["random_orientation"] = "yaw_only"
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1231:        orig_friction = sim_cfg.setdefault("scene", {}).setdefault("objects", {}).get("friction", [0.5, 1.5])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1232:        if isinstance(orig_friction, list):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1233:            f_val = max(orig_friction)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1235:            f_val = float(orig_friction)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1236:        sim_cfg["scene"]["objects"]["friction"] = [max(f_val, 3.0), max(f_val, 3.0)]
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1241:        logging.info("STATIC_STABLE_SPAWN_V2 enabled: static_objects=True, yaw-only/upright orientation, friction>=3.0, angular_damping>=2.0.")
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1303:            if is_object_stopped(env_cfg["scene"], es["object_vel"]):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1305:            if is_object_direction_changed(env_cfg["scene"], es["object_vel"]):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1311:            episode_name = get_episode_name(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1315:                "Saving episode %s with %d frames."
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1399:        "--static_stable_spawn",
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1402:        help="Static V2: prefer upright/stable spawn orientation and higher friction/damping for static manipulation data.",
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:41:    friction: float | None = None,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:74:    if friction is not None:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:75:        spawner_cfg.rigid_props.angular_damping = friction
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:82:def get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:47:def are_objects_placed(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:58:    objects_placed = torch.ones(env.num_envs, dtype=torch.bool, device=env.device)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:78:        objects_placed = torch.logical_and(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:79:            objects_placed,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:93:    return torch.logical_and(objects_placed, eef_goal_dist < tolerance)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:135:    DONE_TERMS = ["object_picked", "objects_placed"]
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:149:    object_dropping = TerminationTermCfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:182:    objects_placed = TerminationTermCfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:183:        func=are_objects_placed,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:210:        done_term = cfg.objects_placed
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:215:        if k in cfg.object_dropping.params:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/termination_cfg.py:216:            cfg.object_dropping.params[k] = v

## Friction/material decision
Current object_cfg.py maps argument named friction to angular_damping:
75:        spawner_cfg.rigid_props.angular_damping = friction

Current material friction seems set after spawn around:
672:    materials[..., 0] = 0.9  # Static friction.
673:    materials[..., 1] = 1.0  # Dynamic friction.

Decision: V3 does NOT modify friction/materials yet.
Reason: broad friction/material changes can hide bad collisions or break dynamics.
First fix stable orientation and add quality checks.
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
## Static V3 orientation + physics sanity inspection
h5_count 3
json_count 3
mp4_count 3

### place_franka_cup05s_O02_00000901_d4f8.h5
json_object_init_lin_vel [0.0, 0.0, 0.0]
json_object_init_quat [0.6974308345729846, 0.0, 0.0, 0.7166520989900401]
json_object_init_pos [-2.399934990053362, 3.5871833285240835, 0.4189150109887123]
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 300
quat_xy_abs_max_first_10 0.0002102374710375443
yaw_only_like_first_10 YES
object_vel_first_50_norms_min_mean_max 0.0 0.01716592162847519 0.10525907576084137
object_z_first80_z0_min_max_dzmin_dzmax_max_step 0.03999999165534973 0.03999999165534973 0.20794910192489624 0.0 0.1679491102695465 0.018741250038146973
PHYSICS_GATE_KEEP YES
PHYSICS_GATE_REASONS []

### place_franka_fcan03s_O02_00000902_dbb6.h5
json_object_init_lin_vel [0.0, 0.0, 0.0]
json_object_init_quat [0.8768533072618715, 0.0, 0.0, -0.4807580238996725]
json_object_init_pos [-0.4626486878735035, 3.4318221701405243, 0.7786903902888298]
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 114
quat_xy_abs_max_first_10 6.892880628583953e-05
yaw_only_like_first_10 YES
object_vel_first_50_norms_min_mean_max 0.0 0.005371379666030407 0.10394275188446045
object_z_first80_z0_min_max_dzmin_dzmax_max_step 0.05500000715255737 0.05500000715255737 0.18025361001491547 0.0 0.1252536028623581 0.015015900135040283
PHYSICS_GATE_KEEP YES
PHYSICS_GATE_REASONS []

### place_franka_kiwi07s_O02_00000900_4f2d.h5
json_object_init_lin_vel [0.0, 0.0, 0.0]
json_object_init_quat [0.9953270385584918, 0.0, 0.0, 0.09656130857844986]
json_object_init_pos [-3.5868423775403455, 2.4955966799693066, 0.7999299447983503]
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 118
quat_xy_abs_max_first_10 3.225108713422742e-08
yaw_only_like_first_10 YES
object_vel_first_50_norms_min_mean_max 0.0 1.4388506031082215e-07 1.5248093632180826e-07
object_z_first80_z0_min_max_dzmin_dzmax_max_step 0.029999971389770508 0.029999971389770508 0.19715255498886108 0.0 0.16715258359909058 0.019475877285003662
PHYSICS_GATE_KEEP YES
PHYSICS_GATE_REASONS []

## Static V3 translate result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/logs/static_v3_translate.log
2026-06-11 15:04:06 [[INFO] 2026-06-11 17:04:12,104 Recovering test environment from /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_fcan03s_O02_00000902_dbb6.json
2026-06-11 15:04:16 [16,657ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for i[DEBUG] 2026-06-11 17:04:34,109 Cam Occluded: False; Object Occluded: False; Container Occluded: False
[INFO] 2026-06-11 17:04:37,504 Recovering test environment from /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_kiwi07s_O02_00000900_4f2d.json
[INFO] Reward Manager:  [DEBUG] 2026-06-11 17:04:54,503 Cam Occluded: False; Object Occluded: False; Container Occluded: False

## Multicam video generation logs

### Video generation for place_franka_cup05s_O02_00000901_d4f8.h5
Command: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/isaaclab.sh -p /home/redafrix/tests/internship/isaac_dynamicVLA-test/tools/make_multicam_video.py --input /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_cup05s_O02_00000901_d4f8.h5 --output /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_cup05s_O02_00000901_d4f8_multicam.mp4 --fps 20
Stdout:

Stderr:
tabs: terminal type 'dumb' cannot reset tabs

### Video generation for place_franka_fcan03s_O02_00000902_dbb6.h5
Command: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/isaaclab.sh -p /home/redafrix/tests/internship/isaac_dynamicVLA-test/tools/make_multicam_video.py --input /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_fcan03s_O02_00000902_dbb6.h5 --output /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_fcan03s_O02_00000902_dbb6_multicam.mp4 --fps 20
Stdout:

Stderr:
tabs: terminal type 'dumb' cannot reset tabs

### Video generation for place_franka_kiwi07s_O02_00000900_4f2d.h5
Command: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/isaaclab.sh -p /home/redafrix/tests/internship/isaac_dynamicVLA-test/tools/make_multicam_video.py --input /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_kiwi07s_O02_00000900_4f2d.h5 --output /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_kiwi07s_O02_00000900_4f2d_multicam.mp4 --fps 20
Stdout:

Stderr:
tabs: terminal type 'dumb' cannot reset tabs

### Video generation for place_franka_cup05s_O02_00000901_d4f8-tr.h5
Command: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/isaaclab.sh -p /home/redafrix/tests/internship/isaac_dynamicVLA-test/tools/make_multicam_video.py --input /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_cup05s_O02_00000901_d4f8-tr.h5 --output /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_cup05s_O02_00000901_d4f8-tr_multicam.mp4 --fps 20
Stdout:

Stderr:
tabs: terminal type 'dumb' cannot reset tabs

### Video generation for place_franka_fcan03s_O02_00000902_dbb6-tr.h5
Command: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/isaaclab.sh -p /home/redafrix/tests/internship/isaac_dynamicVLA-test/tools/make_multicam_video.py --input /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_fcan03s_O02_00000902_dbb6-tr.h5 --output /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_fcan03s_O02_00000902_dbb6-tr_multicam.mp4 --fps 20
Stdout:

Stderr:
tabs: terminal type 'dumb' cannot reset tabs

### Video generation for place_franka_kiwi07s_O02_00000900_4f2d-tr.h5
Command: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/isaaclab.sh -p /home/redafrix/tests/internship/isaac_dynamicVLA-test/tools/make_multicam_video.py --input /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_kiwi07s_O02_00000900_4f2d-tr.h5 --output /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_kiwi07s_O02_00000900_4f2d-tr_multicam.mp4 --fps 20
Stdout:

Stderr:
tabs: terminal type 'dumb' cannot reset tabs

# FINAL STATIC V3 SUMMARY
- static repo: /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1
- experiment: /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate
- raw H5 count: 3
- raw JSON count: 3
- raw MP4 count: 3
- translated H5 count: 3
- translated JSON count: 3
- videos count: 6

## Raw files
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_cup05s_O02_00000901_d4f8.h5 | 144385635 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_cup05s_O02_00000901_d4f8.json | 37023 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_cup05s_O02_00000901_d4f8.mp4 | 1671939 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_fcan03s_O02_00000902_dbb6.h5 | 69931134 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_fcan03s_O02_00000902_dbb6.json | 37135 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_fcan03s_O02_00000902_dbb6.mp4 | 632139 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_kiwi07s_O02_00000900_4f2d.h5 | 59192181 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_kiwi07s_O02_00000900_4f2d.json | 37052 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_kiwi07s_O02_00000900_4f2d.mp4 | 520181 bytes

## Translated files
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_cup05s_O02_00000901_d4f8-FAIL.mp4 | 1627972 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_cup05s_O02_00000901_d4f8-tr.h5 | 145618077 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_cup05s_O02_00000901_d4f8-tr.json | 37010 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_fcan03s_O02_00000902_dbb6-SUCCESS.mp4 | 657291 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_fcan03s_O02_00000902_dbb6-tr.h5 | 69633129 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_fcan03s_O02_00000902_dbb6-tr.json | 37122 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_kiwi07s_O02_00000900_4f2d-FAIL.mp4 | 521368 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_kiwi07s_O02_00000900_4f2d-tr.h5 | 59454055 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_kiwi07s_O02_00000900_4f2d-tr.json | 37039 bytes

## Videos
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_cup05s_O02_00000901_d4f8-tr_multicam.mp4 | 7616181 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_cup05s_O02_00000901_d4f8_multicam.mp4 | 7650225 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_fcan03s_O02_00000902_dbb6-tr_multicam.mp4 | 3260834 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_fcan03s_O02_00000902_dbb6_multicam.mp4 | 3134924 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_kiwi07s_O02_00000900_4f2d-tr_multicam.mp4 | 2783105 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/videos/place_franka_kiwi07s_O02_00000900_4f2d_multicam.mp4 | 2752838 bytes

## Patch path
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/patches/static_true_stable_physics_gate_v3_simulate.patch

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  261G   26G  92% /
