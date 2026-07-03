# Static Collection V2 Stable Spawn Report

Goal: reduce rolling/sliding by fixing static spawn orientation and friction with minimal changes.

## Repo
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1

## Relevant orientation/friction code
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:302:        random_orientation = random.random() < object_cfg.get("prob_rnd_quat", 0.5)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:306:        random_friction = np.random.uniform(*object_cfg.get("friction", [0, 0]))
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:311:            None if random_static else object_cfg.get("moving_speed", None),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:312:            random_friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:313:            random_orientation,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:346:                random_orientation,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:411:    moving_speed,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:412:    friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:413:    random_orientation,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:415:    if moving_speed is None:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:416:        object_state = _get_static_object_state(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:417:            object_range_bbox, object_z, random_orientation
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:420:        object_state = _get_dynamic_object_state(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:423:            moving_speed,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:424:            friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:431:def _get_static_object_state(object_range_bbox, object_z, random_orientation):
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:442:    if random_orientation:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:443:        object_quat = configs.object_cfg.get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:450:def _get_dynamic_object_state(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:451:    object_range_bbox, object_z, moving_speed, friction, robot_position
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:469:    assert moving_speed is not None and len(moving_speed) == 2
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:474:        * random.uniform(*moving_speed)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:476:    object_quat = configs.object_cfg.get_object_init_quat(object_velocity)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:482:        "friction": friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:487:    container_size, object_range_bbox, random_orientation, existing_objects
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:504:        if random_orientation:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:505:            container_quat = configs.object_cfg.get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:567:            configs.object_cfg.get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:570:                friction=target_object.get("friction", 0.0),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:584:                configs.object_cfg.get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:587:                    friction=o.get("friction", 0.0),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:609:                configs.object_cfg.get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:659:    materials[..., 0] = 0.9  # Static friction.
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:660:    materials[..., 1] = 1.0  # Dynamic friction.
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1218:        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["moving_speed"] = None
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1224:        logging.info("STATIC_OBJECTS_V1 enabled: objects keep physics/gravity but initial moving_speed is disabled.")
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1367:        help="Static-object data collection: keep physics/gravity, but disable initial object velocity by forcing moving_speed=None.",
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:38:def get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:41:    friction: float | None = None,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:47:            rigid_props=sim_utils.RigidBodyPropertiesCfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:55:            mass_props=sim_utils.MassPropertiesCfg(mass=mass),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:69:            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:70:            mass_props=sim_utils.MassPropertiesCfg(mass=mass),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:74:    if friction is not None:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:75:        spawner_cfg.rigid_props.angular_damping = friction
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:82:def get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:86:    lin_vel_angle = np.arctan2(init_lin_vel[1], init_lin_vel[0])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:87:    verticle_angle = np.pi / 2 * np.random.choice([-1, 1])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:89:        lin_vel_angle += np.deg2rad(perturbation)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:90:        verticle_angle += np.deg2rad(perturbation)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:95:            0 if upright else verticle_angle,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:97:            lin_vel_angle,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/sim_cfg.yaml:16:    moving_speed: [0.15, 0.75] # range of speed for moving objects, generated uniformly random
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/sim_cfg.yaml:17:    # moving_speed: [0.05, 0.25]
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/sim_cfg.yaml:18:    friction: [0.5, 1.5] # range of friction for objects, generated uniformly random
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/sim_cfg.yaml:16:    moving_speed: [0.15, 0.75] # range of speed for moving objects, generated uniformly random
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/sim_cfg.yaml:17:    # moving_speed: [0.05, 0.25]
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/sim_cfg.yaml:18:    friction: [0.5, 1.5] # range of friction for objects, generated uniformly random
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/env_cfg.py:148:        self.sim.physx.friction_correlation_distance = 0.00625
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:38:def get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:41:    friction: float | None = None,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:47:            rigid_props=sim_utils.RigidBodyPropertiesCfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:55:            mass_props=sim_utils.MassPropertiesCfg(mass=mass),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:69:            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:70:            mass_props=sim_utils.MassPropertiesCfg(mass=mass),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:74:    if friction is not None:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:75:        spawner_cfg.rigid_props.angular_damping = friction
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:82:def get_object_init_quat(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:86:    lin_vel_angle = np.arctan2(init_lin_vel[1], init_lin_vel[0])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:87:    verticle_angle = np.pi / 2 * np.random.choice([-1, 1])
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:89:        lin_vel_angle += np.deg2rad(perturbation)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:90:        verticle_angle += np.deg2rad(perturbation)
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:95:            0 if upright else verticle_angle,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:97:            lin_vel_angle,

## object_cfg.py
     1	# -*- coding: utf-8 -*-
     2	#
     3	# @File:   object_cfg.py
     4	# @Author: Haozhe Xie
     5	# @Date:   2025-04-16 14:38:58
     6	# @Last Modified by: Haozhe Xie
     7	# @Last Modified at: 2025-11-06 09:38:17
     8	# @Email:  root@haozhexie.com
     9	
    10	import isaaclab.sim as sim_utils
    11	import numpy as np
    12	import scipy.spatial.transform
    13	from isaaclab.assets import DeformableObjectCfg, RigidObjectCfg
    14	from isaaclab.sim.spawners import SpawnerCfg
    15	from isaaclab.sim.spawners.from_files.from_files_cfg import UsdFileCfg
    16	
    17	
    18	def get_object_cfg(
    19	    prim_path: str, obj_cfg: dict, spawner_cfg: SpawnerCfg
    20	) -> RigidObjectCfg | DeformableObjectCfg:
    21	    assert prim_path.startswith("/")
    22	
    23	    init_state = RigidObjectCfg.InitialStateCfg(pos=obj_cfg["pos"])
    24	    if "lin_vel" in obj_cfg:
    25	        init_state.lin_vel = obj_cfg["lin_vel"]
    26	    if "ang_vel" in obj_cfg:
    27	        init_state.ang_vel = obj_cfg["ang_vel"]
    28	    if "quat" in obj_cfg:
    29	        init_state.rot = obj_cfg["quat"]
    30	
    31	    return RigidObjectCfg(
    32	        prim_path="{ENV_REGEX_NS}%s" % prim_path,
    33	        init_state=init_state,
    34	        spawn=spawner_cfg,
    35	    )
    36	
    37	
    38	def get_spawner_cfg(
    39	    file_path: str = None,
    40	    mass: int = 0.05,
    41	    friction: float | None = None,
    42	    semantic_tags=None,
    43	) -> SpawnerCfg:
    44	    if file_path is not None:
    45	        spawner_cfg = UsdFileCfg(
    46	            usd_path=file_path,
    47	            rigid_props=sim_utils.RigidBodyPropertiesCfg(
    48	                solver_position_iteration_count=16,
    49	                solver_velocity_iteration_count=1,
    50	                max_angular_velocity=1000.0,
    51	                max_linear_velocity=1000.0,
    52	                max_depenetration_velocity=5.0,
    53	                disable_gravity=False,
    54	            ),
    55	            mass_props=sim_utils.MassPropertiesCfg(mass=mass),
    56	            collision_props=sim_utils.CollisionPropertiesCfg(
    57	                collision_enabled=True,
    58	                contact_offset=0.01,
    59	                rest_offset=0.0,
    60	                min_torsional_patch_radius=0.01,
    61	                torsional_patch_radius=0.01,
    62	            ),
    63	        )
    64	    else:
    65	        # spawner_cfg = sim_utils.SphereCfg(
    66	        spawner_cfg = sim_utils.CylinderCfg(
    67	            radius=0.03,
    68	            height=0.1,
    69	            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
    70	            mass_props=sim_utils.MassPropertiesCfg(mass=mass),
    71	            collision_props=sim_utils.CollisionPropertiesCfg(),
    72	            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 1.0, 0.0)),
    73	        )
    74	    if friction is not None:
    75	        spawner_cfg.rigid_props.angular_damping = friction
    76	    if semantic_tags is not None:
    77	        spawner_cfg.semantic_tags = semantic_tags
    78	
    79	    return spawner_cfg
    80	
    81	
    82	def get_object_init_quat(
    83	    init_lin_vel: list[float], upright=False, perturbation=None
    84	) -> list[float]:
    85	
    86	    lin_vel_angle = np.arctan2(init_lin_vel[1], init_lin_vel[0])
    87	    verticle_angle = np.pi / 2 * np.random.choice([-1, 1])
    88	    if perturbation is not None:
    89	        lin_vel_angle += np.deg2rad(perturbation)
    90	        verticle_angle += np.deg2rad(perturbation)
    91	
    92	    quat = scipy.spatial.transform.Rotation.from_euler(
    93	        "xyz",
    94	        [
    95	            0 if upright else verticle_angle,
    96	            0,
    97	            lin_vel_angle,
    98	        ],
    99	    ).as_quat()
   100	    return quat[[3, 0, 1, 2]]

## simulate.py object state sections
   280	        "intensity": light_intensity,
   281	    }
   282	
   283	
   284	def _get_object_states(
   285	    sim_cfg, robot_pose, table_bbox, object_metadata, robot_reach_dist
   286	):
   287	    object_states = {"objects": [], "containers": []}
   288	    # Generate the poses of objects (The first object is the target object)
   289	    object_cfg = sim_cfg["scene"]["objects"]
   290	    object_categories = object_cfg["categories"]
   291	    if not object_categories:
   292	        object_categories = list(set([v["category"] for v in object_metadata.values()]))
   293	
   294	    object_candidates = [
   295	        copy.deepcopy(v)
   296	        for v in object_metadata.values()
   297	        if v["category"] in object_categories
   298	    ]
   299	    object_range_bbox = _get_object_range_bbox(table_bbox)
   300	    for oi in range(object_cfg["n_objects"]):
   301	        _object = random.choice(object_candidates).copy()
   302	        random_orientation = random.random() < object_cfg.get("prob_rnd_quat", 0.5)
   303	        random_static = (
   304	            random.random() < object_cfg.get("prob_static", 0.5) if oi != 0 else False
   305	        )  # The first object is always dynamic
   306	        random_friction = np.random.uniform(*object_cfg.get("friction", [0, 0]))
   307	        _state = _get_object_state(
   308	            _get_object_z(object_range_bbox.max[2], _object["size"]),
   309	            robot_pose["pos"],
   310	            object_range_bbox,
   311	            None if random_static else object_cfg.get("moving_speed", None),
   312	            random_friction,
   313	            random_orientation,
   314	        )
   315	        object_states["objects"].append(
   316	            {
   317	                **_object,
   318	                **_state,
   319	                "mass": object_cfg.get("mass", 0.05),
   320	            }
   321	        )
   322	
   323	    # Generate the poses of containers (The first container is the target container)
   324	    container_cfg = sim_cfg["scene"]["containers"]
   325	    container_categories = container_cfg["categories"]
   326	    cntr_range_bbox = _get_object_range_bbox(
   327	        table_bbox, robot_pose["pos"], robot_reach_dist
   328	    )
   329	    if not container_categories:
   330	        container_categories = list(
   331	            set([v["category"] for v in object_metadata.values()])
   332	        )
   333	
   334	    container_candidates = [
   335	        copy.deepcopy(v)
   336	        for v in object_metadata.values()
   337	        if v["category"] in container_categories
   338	    ]
   339	    for _ in range(container_cfg["n_containers"]):
   340	        _state = None
   341	        while _state is None and container_candidates:
   342	            _container = random.choice(container_candidates).copy()
   343	            _state = _get_container_state(
   344	                _container["size"],
   345	                cntr_range_bbox,
   346	                random_orientation,
   347	                object_states,
   348	            )
   349	            if _state is None:
   350	                # The container cannot be placed without occlusion
   351	                container_candidates.remove(_container)
   352	
   353	        # Remove from the candidates to avoid duplication
   354	        if _state is not None:
   355	            container_candidates.remove(_container)
   356	            object_states["containers"].append(
   357	                {
   358	                    **_container,
   359	                    **_state,
   360	                    "mass": container_cfg.get("mass", 0.1),
   361	                }
   362	            )
   363	
   364	    return object_states
   365	
   366	
   367	def _get_object_range_bbox(table_bbox, robot_position=None, robot_reach_dist=None):
   368	    from pxr import Gf
   369	
   370	    object_range_min_0 = table_bbox.min[0] * 3 / 4 + table_bbox.max[0] / 4
   371	    object_range_max_0 = table_bbox.min[0] / 4 + table_bbox.max[0] * 3 / 4
   372	    object_range_min_1 = table_bbox.min[1] * 3 / 4 + table_bbox.max[1] / 4
   373	    object_range_max_1 = table_bbox.min[1] / 4 + table_bbox.max[1] * 3 / 4
   374	    table_z = table_bbox.max[2]
   375	    object_valid_range = Gf.Range3d(
   376	        Gf.Vec3d(object_range_min_0, object_range_min_1, table_z),
   377	        Gf.Vec3d(object_range_max_0, object_range_max_1, table_z),
   378	    )
   379	    if robot_position is None and robot_reach_dist is None:
   380	        return object_valid_range
   381	    else:
   382	        # Consider whether the object is within the robot reach
   383	        robot_reach_bbox = Gf.Range3d(
   384	            Gf.Vec3d(
   385	                robot_position[0] - robot_reach_dist,
   386	                table_bbox.min[1] - robot_reach_dist,
   387	                table_z,
   388	            ),
   389	            Gf.Vec3d(
   390	                robot_position[0] + robot_reach_dist,
   391	                table_bbox.min[1] + robot_reach_dist,
   392	                table_z,
   393	            ),
   394	        )
   395	        return robot_reach_bbox.IntersectWith(object_valid_range)
   396	
   397	
   398	def _get_object_z(table_z, object_size=None):
   399	    PADDING = 0.02
   400	    return (
   401	        table_z + np.max(object_size) / 2
   402	        if object_size is not None
   403	        else table_z + PADDING
   404	    )
   405	
   406	
   407	def _get_object_state(
   408	    object_z,
   409	    robot_position,
   410	    object_range_bbox,
   411	    moving_speed,
   412	    friction,
   413	    random_orientation,
   414	):
   415	    if moving_speed is None:
   416	        object_state = _get_static_object_state(
   417	            object_range_bbox, object_z, random_orientation
   418	        )
   419	    else:
   420	        object_state = _get_dynamic_object_state(
   421	            object_range_bbox,
   422	            object_z,
   423	            moving_speed,
   424	            friction,
   425	            robot_position,
   426	        )
   427	
   428	    return object_state
   429	
   430	
   431	def _get_static_object_state(object_range_bbox, object_z, random_orientation):
   432	    import configs.object_cfg
   433	
   434	    object_position = np.array(
   435	        [
   436	            random.uniform(object_range_bbox.min[0], object_range_bbox.max[0]),
   437	            random.uniform(object_range_bbox.min[1], object_range_bbox.max[1]),
   438	            object_z,
   439	        ]
   440	    )
   441	    object_quat = np.array([1.0, 0.0, 0.0, 0.0])
   442	    if random_orientation:
   443	        object_quat = configs.object_cfg.get_object_init_quat(
   444	            np.random.uniform(-0.1, 0.1, size=3)
   445	        )
   446	
   447	    return {"pos": object_position, "quat": object_quat}
   448	
   449	
   450	def _get_dynamic_object_state(
   451	    object_range_bbox, object_z, moving_speed, friction, robot_position
   452	):
   453	    import configs.object_cfg
   454	
   455	    object_position = np.array(
   456	        [
   457	            random.uniform(object_range_bbox.min[0], object_range_bbox.max[0]),
   458	            random.uniform(object_range_bbox.min[1], object_range_bbox.max[1]),
   459	            object_z,
   460	        ]
   461	    )
   462	    assert robot_position is not None
   463	    # Generate a random position between the table center and the robot arm
   464	    tbl_ctr = (object_range_bbox.min + object_range_bbox.max) / 2.0
   465	    random_ratio = random.uniform(-0.5, 0.5)
   466	    random_position = tbl_ctr + random_ratio * (robot_position - tbl_ctr)
   467	    random_position[2] = object_z
   468	    # Determine the linear velocity of the object
   469	    assert moving_speed is not None and len(moving_speed) == 2
   470	    object_direction = random_position - object_position
   471	    object_velocity = (
   472	        object_direction
   473	        / np.linalg.norm(object_direction)
   474	        * random.uniform(*moving_speed)
   475	    )
   476	    object_quat = configs.object_cfg.get_object_init_quat(object_velocity)
   477	
   478	    return {
   479	        "pos": object_position,
   480	        "quat": object_quat,
   481	        "lin_vel": object_velocity,
   482	        "friction": friction,
   483	    }
   484	
   485	
   486	def _get_container_state(
   487	    container_size, object_range_bbox, random_orientation, existing_objects
   488	):
   489	    import configs.object_cfg
   490	
   491	    N_MAX_TRIES = 100
   492	    n_tries = 0
   493	    container_position = None
   494	    while container_position is None and n_tries < N_MAX_TRIES:
   495	        n_tries += 1
   496	        container_position = np.array(
   497	            [
   498	                random.uniform(object_range_bbox.min[0], object_range_bbox.max[0]),
   499	                random.uniform(object_range_bbox.min[1], object_range_bbox.max[1]),
   500	                _get_object_z(object_range_bbox.max[2], container_size),
   501	            ]
   502	        )
   503	        container_quat = np.array([1.0, 0.0, 0.0, 0.0])
   504	        if random_orientation:
   505	            container_quat = configs.object_cfg.get_object_init_quat(
   506	                np.random.uniform(-0.1, 0.1, size=3), upright=True
   507	            )
   508	        # Check whether the container is occluding with existing objects/containers
   509	        for eo in existing_objects["objects"] + existing_objects["containers"]:
   510	            if _is_bbox_overlap(
   511	                _get_object_bbox(container_position, container_size, container_quat),
   512	                _get_object_bbox(
   513	                    eo["pos"], eo["size"], eo["quat"], eo.get("lin_vel", None)
   514	                ),
   515	            ):
   516	                container_position = None
   517	                break
   518	
   519	    if container_position is not None:
   520	        return {"pos": container_position, "quat": container_quat}
   521	    else:
   522	        return None
   523	
   524	
   525	def _get_object_bbox(position, size, quat, lin_vel=None):
   526	    # TODO: Consider the velocity of the object
   527	    dx, dy, dz = size / 2.0
   528	    corners = np.array(
   529	        [
   530	            [-dx, -dy, -dz],

## sim_cfg.yaml
     1	scene:
     2	  cameras: # Configure camera position and pose
     3	    - name: "opst_cam"
     4	      position: [1, 0, 0.6]
     5	      rotation: [0, 60, 90]
     6	      prim_path: "/Robot/OppositeCamera"
     7	    - name: "side_cam"
     8	      position: [0.5, 1, 0.35]
     9	      rotation: [-90, 0, 180]
    10	      prim_path: "/Robot/SideCamera"
    11	  objects: # Configure object
    12	    n_objects: 1 # number of objects in simulation
    13	    mass: 0.05 # mass of object
    14	    prob_rnd_quat: 0.85 # probability of object having random orientation. Otherwise it will have default orientation.
    15	    prob_static: 0.5 # probability of object being static. Otherwise it will be moving.
    16	    moving_speed: [0.15, 0.75] # range of speed for moving objects, generated uniformly random
    17	    # moving_speed: [0.05, 0.25]
    18	    friction: [0.5, 1.5] # range of friction for objects, generated uniformly random
    19	    perturbation: # configure perturbation for objects. Delete this if you don't intend to introduce perturbation for objects.
    20	      # force: [0.001, 0.005]
    21	      # torque: [0.0005, 0.0025]
    22	    tag_thresholds: # configure thresholds for tag generation. If the value difference between two objects is less than the threshold, the value is considered same, thus also the rank.
    23	      height: 0.1
    24	      area: 0.1
    25	      volume: 0.1
    26	      position_from_left: 0.1
    27	      position_from_bottom: 0.1
    28	      distance_from_robot: 0.3
    29	      velocity: 0.2
    30	    categories: # configure available categories of objects. All objects are randomly selected from available items whose category is in this list. Must exist in the objects directory.
    31	      - apple
    32	      - avocado
    33	      - beer
    34	      - bottle
    35	      - can
    36	      - cup
    37	      - egg
    38	      - kiwi
    39	      - lemon
    40	      - lime
    41	      - onion
    42	      - orange
    43	      - peach
    44	      - potato
    45	      - tangerine
    46	      - tomato
    47	      # - unseen
    48	  containers: # Configure containers
    49	    n_containers: 1 # number of containers
    50	    mass: 0.1 # mass of container
    51	    categories: # configure available categories of containers. Must exist in the objects directory.
    52	      - bowl
    53	      - box
    54	      - plate
    55	      - placemat
    56	      - tray
    57	
    58	camera:
    59	  width: 480
    60	  height: 360
    61	  fps: 25
    62	  focal_length: 2.3
    63	  focus_distance: 400
    64	  horizontal_aperture: 4.6
    65	  clip:
    66	    near: 0.01
    67	    far: 10000
    68	  data_types:
    69	    - rgb
    70	    - semantic_segmentation
    71	    # - depth
    72	
    73	lighting:  # lighting configuration, config for each scene is selected randomly in the respective range.
    74	  temperature: [4000, 8000]
    75	  intensity: [150, 750]
    76	  position:
    77	    x: [-50, 50]
    78	    y: [-50, 50]
    79	    z: [10, 20]
    80	
    81	tasks: # configure task behaviour
    82	  pick:
    83	    sm: "state_machines.pick_sm.PickStateMachine" # selects the state machine to run when generating scenes executing the respective task
    84	    episode_length: 10 # max episode length, terminating with failure if exceeded
    85	  place:
    86	    sm: "state_machines.place_sm.PlaceStateMachine"
    87	    episode_length: 12
    88	  long-horizon:
    89	    sm: "state_machines.place_sm.PlaceStateMachine"
    90	    episode_length: 20
    91	
    92	robots: # configure robots in simulation
    93	  franka:
    94	    init_pose: [0.465906, 0.0, 0.382970, 0.008583, 0.921765, 0.020404, 0.387116]
    95	    final_pose: [0.3, 0, 0.3, -1, 0, 0, 0]
    96	    gripper_length: 0.045
    97	    max_reach_dist: 0.75
    98	  piper:
    99	    init_pose: [0.373, 0.0, 0.271, 0.0, 0.9739, 0.0, 0.227]
   100	    final_pose: [0.373, 0.0, 0.271, -1, 0, 0, 0]
   101	    gripper_length: 0.09
   102	    max_reach_dist: 0.55

## Verify friction/damping path
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:575:            configs.object_cfg.get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:592:                configs.object_cfg.get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:617:                configs.object_cfg.get_spawner_cfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/evaluate.py:274:            configs.object_cfg.get_spawner_cfg(

/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:41:    friction: float | None = None,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:47:            rigid_props=sim_utils.RigidBodyPropertiesCfg(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:69:            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:74:    if friction is not None:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/configs/object_cfg.py:75:        spawner_cfg.rigid_props.angular_damping = friction
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:306:        random_friction = np.random.uniform(*object_cfg.get("friction", [0, 0]))
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:312:            random_friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:412:    friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:424:            friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:459:    object_range_bbox, object_z, moving_speed, friction, robot_position
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:490:        "friction": friction,
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:578:                friction=target_object.get("friction", 0.0),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:595:                    friction=o.get("friction", 0.0),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:667:    materials[..., 0] = 0.9  # Static friction.
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:668:    materials[..., 1] = 1.0  # Dynamic friction.
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1231:        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["friction"] = max(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1232:            float(sim_cfg.setdefault("scene", {}).setdefault("objects", {}).get("friction", 1.0)),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1235:        sim_cfg.setdefault("scene", {}).setdefault("objects", {})["angular_damping"] = max(
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1236:            float(sim_cfg.setdefault("scene", {}).setdefault("objects", {}).get("angular_damping", 0.05)),
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1239:        logging.info("STATIC_STABLE_SPAWN_V2 enabled: static_objects=True, yaw-only/upright orientation, friction>=3.0, angular_damping>=2.0.")
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1/simulations/simulate.py:1400:        help="Static V2: prefer upright/stable spawn orientation and higher friction/damping for static manipulation data.",
tabs: terminal type 'dumb' cannot reset tabs
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
## Static V2 raw inspection
h5_count 0
json_count 0
mp4_count 0
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
## Static V2 raw inspection
h5_count 3
json_count 3
mp4_count 3

### place_franka_apple07s_O02_00000800_b329.h5
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 261
object_vel_first_50_norms_min_mean_max 0.0 0.029577704146504402 0.061166852712631226
object_vel_first_10 [[0.0, 0.0, 0.0], [0.0012251940788701177, 0.001551743596792221, 1.984514165087603e-05], [-0.007707627490162849, -0.009762299247086048, -0.0006840823334641755], [-0.01018095389008522, -0.012896605767309666, -0.0009653551387600601], [-0.002546497853472829, -0.003228392917662859, 0.00019199911912437528], [0.0027999295853078365, 0.003541652113199234, 0.00029889208963140845], [-0.002277481835335493, -0.0028928755782544613, -0.00041127530857920647], [-0.008548756130039692, -0.010842543095350266, -0.0009131890838034451], [-0.006311303004622459, -0.008019340224564075, -0.0006335971993394196], [-0.00035636097891256213, -0.000493667961563915, -5.2178384066792205e-05]]
object_quat_first_3 [[-0.6679922342300415, 0.6679922342300415, -0.23191885650157928, 0.23191885650157928], [-0.6632369160652161, 0.6727133393287659, -0.2335585653781891, 0.23026862740516663], [-0.6636195778846741, 0.6723382472991943, -0.23342427611351013, 0.23039764165878296]]

### place_franka_avocado06s_O02_00000801_e89a.h5
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 189
object_vel_first_50_norms_min_mean_max 0.0 0.06739619374275208 0.849949061870575
object_vel_first_10 [[0.0, 0.0, 0.0], [-0.0031825988553464413, -0.016135457903146744, -0.003389089135453105], [-9.418884292244911e-05, -0.0006538574234582484, -0.0006345846923068166], [-4.362053005024791e-05, -0.0003418916021473706, -0.0008925205911509693], [-4.0163493395084515e-05, -0.0004335633711889386, -0.0009291936876252294], [-1.988679059650167e-06, -0.00044668567716144025, -0.0009294143528677523], [7.008692773524672e-05, -0.0004600925312843174, -0.0009293361217714846], [0.0002012552140513435, -0.0004822984919883311, -0.0009288970031775534], [0.00043856140109710395, -0.0005284237558953464, -0.0009297232027165592], [0.0008709746762178838, -0.0006061929743736982, -0.0009299226221628487]]
object_quat_first_3 [[0.06468921899795532, 0.06468920409679413, 0.7041415572166443, 0.7041415572166443], [0.06465780735015869, 0.06467145681381226, 0.7043578028678894, 0.7039297223091125], [0.06466269493103027, 0.06467707455158234, 0.7042379379272461, 0.7040486335754395]]

### place_franka_potato14s_O02_00000802_103e.h5
keys ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
frames 120
object_vel_first_50_norms_min_mean_max 0.0 0.03343089669942856 0.39239999651908875
object_vel_first_10 [[0.0, 0.0, 0.0], [-4.349445248408301e-09, 9.697997072066755e-09, -0.39239999651908875], [-0.0003149212570860982, -0.0017393745947629213, -0.0003414451493881643], [-8.40873399283737e-05, -0.00044054698082618415, -0.0001476062461733818], [-9.156731539405882e-05, -0.0004699449928011745, -0.00016171766037587076], [-9.704288095235825e-05, -0.00046882237074896693, -0.00016141591186169535], [-0.00010715308599174023, -0.0004675269010476768, -0.0001613414060557261], [-0.0001256850955542177, -0.000464852899312973, -0.00016137493366841227], [-0.00015926844207569957, -0.00046003895113244653, -0.00016138610953930765], [-0.000220176501898095, -0.00045148737262934446, -0.0001612929772818461]]
object_quat_first_3 [[-0.050266195088624954, -0.05026615783572197, -0.7053178548812866, -0.7053178548812866], [-0.050266195088624954, -0.0502660907804966, -0.7053177952766418, -0.7053177952766418], [-0.050260983407497406, -0.050255920737981796, -0.70533287525177, -0.7053036689758301]]

JSON place_franka_apple07s_O02_00000800_b329.json
instruction {'task': 'place', 'objects': ['round apple', 'red apple', 'red round apple', 'apple'], 'containers': ['ceramic bowl with enameled gold rim', 'ceramic bowl', 'bowl', 'bowl with enameled gold rim']}
json_object_init_pos [2.5768947958306354, -1.6686328650230513, 0.35023022815585136]
json_object_init_quat None
json_object_init_lin_vel [0.0, 0.0, 0.0]

JSON place_franka_avocado06s_O02_00000801_e89a.json
instruction {'task': 'place', 'objects': ['green pear-shaped long avocado', 'pear-shaped long avocado', 'avocado', 'green avocado'], 'containers': ['white tray', 'white tray with Don Don Donki logo', 'tray with Don Don Donki logo', 'tray']}
json_object_init_pos [2.2040987638253595, -2.307736946698648, 0.41179512068629265]
json_object_init_quat None
json_object_init_lin_vel [0.0, 0.0, 0.0]

JSON place_franka_potato14s_O02_00000802_103e.json
instruction {'task': 'place', 'objects': ['long potato', 'long pitted potato', 'light color long pitted potato', 'pitted potato', 'potato', 'light color long potato', 'light color potato', 'light color pitted potato'], 'containers': ['white tray', 'white tray with NTU logo', 'tray with NTU logo', 'tray']}
json_object_init_pos [1.3213118425911994, 0.44960560511330294, 0.4491993375122547]
json_object_init_quat None
json_object_init_lin_vel [0.0, 0.0, 0.0]

# FINAL STATIC V2 SUMMARY
- static repo: /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/repos/dynamic-vla-static-v1
- experiment: /home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn
- raw H5 count: 3
- raw JSON count: 3
- raw MP4 count: 3
- translated H5 count: 3
- translated JSON count: 3
- videos count: 6

## Raw files
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_apple07s_O02_00000800_b329.h5 | 131394691 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_apple07s_O02_00000800_b329.json | 37123 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_apple07s_O02_00000800_b329.mp4 | 1295193 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_avocado06s_O02_00000801_e89a.h5 | 91224329 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_avocado06s_O02_00000801_e89a.json | 37141 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_avocado06s_O02_00000801_e89a.mp4 | 1015096 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_potato14s_O02_00000802_103e.h5 | 62732017 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_potato14s_O02_00000802_103e.json | 37252 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_potato14s_O02_00000802_103e.mp4 | 587040 bytes

## Translated files
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_apple07s_O02_00000800_b329-FAIL.mp4 | 1178213 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_apple07s_O02_00000800_b329-tr.h5 | 129607415 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_apple07s_O02_00000800_b329-tr.json | 37110 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_avocado06s_O02_00000801_e89a-FAIL.mp4 | 921663 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_avocado06s_O02_00000801_e89a-tr.h5 | 89816444 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_avocado06s_O02_00000801_e89a-tr.json | 37128 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_potato14s_O02_00000802_103e-SUCCESS.mp4 | 619286 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_potato14s_O02_00000802_103e-tr.h5 | 61969366 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_potato14s_O02_00000802_103e-tr.json | 37239 bytes

## Videos
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/videos/place_franka_apple07s_O02_00000800_b329_multicam.mp4 | 6418512 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/videos/place_franka_apple07s_O02_00000800_b329-tr_multicam.mp4 | 6089113 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/videos/place_franka_avocado06s_O02_00000801_e89a_multicam.mp4 | 5031935 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/videos/place_franka_avocado06s_O02_00000801_e89a-tr_multicam.mp4 | 4759248 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/videos/place_franka_potato14s_O02_00000802_103e_multicam.mp4 | 3036760 bytes
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/videos/place_franka_potato14s_O02_00000802_103e-tr_multicam.mp4 | 3051310 bytes

## Patch path
/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/patches/static_stable_spawn_v2_simulate.patch

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  260G   27G  91% /
