# Static Collection Design Inspection
Goal: identify the minimal safe patch points for static-object scripted collection.

## scene_selection

### simulations/simulate.py
- L100: `def get_env_cfg(sim_cfg, task, robot, object_metadata, scene_dir):`
- L122: `scenes = [f for f in os.listdir(scene_dir) if f.endswith(".usd")]`
- L125: `scene = random.choice(scenes)`
- L126: `usd_file = os.path.join(scene_dir, scene)`
- L129: `env_cfg.scene, os.path.join(scene_dir, usd_file)`
- L135: `scenes.remove(scene)`
- L138: `table = random.choice(tables)`
- L142: `robot_pose = random.choice([a for a in table["anchors"] if a["side"] == "long"])`
- L301: `_object = random.choice(object_candidates).copy()`
- L342: `_container = random.choice(container_candidates).copy()`
- L864: `def simulate(sim_cfg, task, robot, scene_dir, object_metadata, seed):`
- L873: `scene_dir,`
- L1246: `args.scene_dir,`
- L1333: `"--scene_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")`

### simulations/evaluate.py
- L49: `scene_dir,`
- L61: `cfg, num_envs, scene_dir, object_dir, tolerance, device, disable_fabric`
- L80: `cfg, num_envs, scene_dir, object_dir, tolerance, device, disable_fabric`
- L113: `scene_dir, os.path.basename(cfg["scene"]["house"]["spawn"]["usd_path"])`
- L117: `env_cfg.scene, os.path.join(scene_dir, scene_usd_path)`
- L441: `sim_cfg["scene_dir"],`
- L511: `"scene_dir": args.scene_dir,`
- L631: `"--scene_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")`

### simulations/configs/object_cfg.py
- L87: `verticle_angle = np.pi / 2 * np.random.choice([-1, 1])`

### utils/instruction_generator.py
- L21: `object_desc = random.choice(inst_metadata.get("objects", [""]))`
- L22: `container_desc = random.choice(inst_metadata.get("containers", [""]))`
- L27: `pick_action = random.choice(`
- L30: `place_action = random.choice(`

### scripts/create_scene_collision.py
- L308: `"--output_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")`

### scripts/replay_dataset_seq.py
- L95: `args.scene_dir,`
- L152: `"--scene_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")`

### scripts/translate_dataset_seq.py
- L248: `args.scene_dir,`
- L334: `"--scene_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")`

### scripts/create_usd_scenes.py
- L3: `# @File:   create_usd_scenes.py`

### scripts/fix_error_scenes.py
- L3: `# @File:   fix_error_scenes.py`
- L166: `def main(scene_dir, range=None):`
- L169: `usd_files = sorted([f for f in os.listdir(scene_dir) if f.endswith(".usd")])`
- L176: `usd_file = os.path.join(scene_dir, uf)`
- L235: `"--scene_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")`
- L240: `main(args.scene_dir, args.range)`

## object_selection

### simulations/simulate.py
- L38: `def get_object_metadata(object_dir, target_categories=[]):`
- L41: `object_sizes = _get_object_sizes(args.object_dir, target_categories)`
- L67: `def _get_object_sizes(object_dir, target_categories=None):`
- L71: `if target_categories and c not in target_categories:`
- L290: `object_categories = object_cfg["categories"]`
- L291: `if not object_categories:`
- L292: `object_categories = list(set([v["category"] for v in object_metadata.values()]))`
- L297: `if v["category"] in object_categories`
- L325: `container_categories = container_cfg["categories"]`
- L329: `if not container_categories:`
- L330: `container_categories = list(`
- L337: `if v["category"] in container_categories`
- L560: `"Using target object: %s" % os.path.basename(target_object["file_path"])`
- L601: `logging.info("Using container object: %s" % os.path.basename(o["file_path"]))`
- L1227: `object_categories = sim_cfg["scene"]["objects"]["categories"]`
- L1228: `container_categories = sim_cfg["scene"]["containers"].get("categories", [])`
- L1229: `object_metadata = get_object_metadata(`
- L1230: `args.object_dir, object_categories + container_categories`

## spawn_pose

### simulations/helpers.py
- L91: `object_position: torch.Tensor,`
- L102: `object_container_rela = object_position - container_position`
- L115: `object_lowest_z = object_position[:, 2] - torch.sum(`

### simulations/simulate.py
- L182: `os.path.basename(getattr(env_cfg.scene, o).spawn.usd_path),`
- L202: `os.path.basename(env_cfg.scene.container.spawn.usd_path),`
- L434: `object_position = np.array(`
- L447: `return {"pos": object_position, "quat": object_quat}`
- L455: `object_position = np.array(`
- L466: `random_position = tbl_ctr + random_ratio * (robot_position - tbl_ctr)`
- L467: `random_position[2] = object_z`
- L470: `object_direction = random_position - object_position`
- L479: `"pos": object_position,`
- L567: `configs.object_cfg.get_spawner_cfg(`
- L584: `configs.object_cfg.get_spawner_cfg(`
- L609: `configs.object_cfg.get_spawner_cfg(`
- L892: `os.path.basename(env_cfg.scene.container.spawn.usd_path),`
- L1042: `os.path.basename(scene_cfg["object"]["spawn"]["usd_path"][:-4])`
- L1043: `if "usd_path" in scene_cfg["object"]["spawn"]`

### simulations/evaluate.py
- L113: `scene_dir, os.path.basename(cfg["scene"]["house"]["spawn"]["usd_path"])`
- L124: `cfg["scene"]["robot"]["spawn"]["usd_path"]`
- L213: `"focal_length": v["spawn"]["focal_length"],`
- L214: `"focus_distance": v["spawn"]["focus_distance"],`
- L215: `"horizontal_aperture": v["spawn"]["horizontal_aperture"],`
- L217: `"near": v["spawn"]["clipping_range"][0],`
- L218: `"far": v["spawn"]["clipping_range"][1],`
- L236: `temperature=cfg["spawn"]["color_temperature"],`
- L237: `intensity=cfg["spawn"]["intensity"],`
- L255: `if "usd_path" in v["spawn"]:`
- L256: `usd_folder = os.path.basename(os.path.dirname(v["spawn"]["usd_path"]))`
- L258: `object_dir, usd_folder, os.path.basename(v["spawn"]["usd_path"])`
- L274: `configs.object_cfg.get_spawner_cfg(`
- L276: `v["spawn"]["mass_props"]["mass"],`
- L277: `v["spawn"]["rigid_props"]["angular_damping"],`
- L278: `v["spawn"]["semantic_tags"],`
- L371: `env.unwrapped.scene["robot"].cfg.spawn.usd_path`

### simulations/robots/piper.py
- L27: `spawn=sim_utils.UsdFileCfg(`
- L91: `AGILEX_PIPER_HIGH_PD_CFG.spawn.rigid_props.disable_gravity = True`

### simulations/robots/franka.py
- L26: `spawn=sim_utils.UsdFileCfg(`
- L88: `FRANKA_PANDA_HIGH_PD_CFG.spawn.rigid_props.disable_gravity = True`

### simulations/configs/event_cfg.py
- L58: `reset_object_position = EventTermCfg(`

### simulations/configs/scene_cfg.py
- L27: `from isaaclab.sim.spawners.from_files.from_files_cfg import GroundPlaneCfg, UsdFileCfg`
- L52: `spawn=sim_utils.DomeLightCfg(`
- L64: `spawn=GroundPlaneCfg(visible=False, color=(0.0, 0.0, 0.0)),`
- L86: `spawn=sim_utils.PinholeCameraCfg(`
- L117: `spawn=sim_utils.DistantLightCfg(`
- L168: `spawn=UsdFileCfg(usd_path=scene_asset_usd_file),`

### simulations/configs/termination_cfg.py
- L34: `object_position_w = object.data.root_pos_w`
- L37: `object_eef_dist = torch.norm(eef_position_w - object_position_w, dim=1)`
- L72: `object_position = helpers.get_robot_relative_position(`
- L81: `object_position,`
- L123: `object_position = helpers.get_robot_relative_position(`
- L126: `obj_dist = torch.norm(object_position)`

### simulations/configs/env_cfg.py
- L33: `object_pose = mdp.UniformPoseCommandCfg(`
- L38: `ranges=mdp.UniformPoseCommandCfg.Ranges(`
- L59: `object_position = ObservationTermCfg(`
- L60: `func=mdp.object_position_in_robot_root_frame`
- L62: `target_object_position = ObservationTermCfg(`

### simulations/configs/object_cfg.py
- L14: `from isaaclab.sim.spawners import SpawnerCfg`
- L15: `from isaaclab.sim.spawners.from_files.from_files_cfg import UsdFileCfg`
- L19: `prim_path: str, obj_cfg: dict, spawner_cfg: SpawnerCfg`
- L34: `spawn=spawner_cfg,`
- L38: `def get_spawner_cfg(`
- L45: `spawner_cfg = UsdFileCfg(`
- L65: `# spawner_cfg = sim_utils.SphereCfg(`
- L66: `spawner_cfg = sim_utils.CylinderCfg(`
- L75: `spawner_cfg.rigid_props.angular_damping = friction`
- L77: `spawner_cfg.semantic_tags = semantic_tags`
- L79: `return spawner_cfg`

### simulations/configs/robot_cfg.py
- L98: `cfg.spawn.semantic_tags = [("class", "ROBOT")]`

### simulations/state_machines/sm_utils.py
- L41: `object_position: torch.Tensor,`
- L48: `grasp_position = object_position.clone() + object_velocity * WAITING_TIME`

### policies/dynamicvla/modeling_dynamicvla.py
- L305: `is spawned to run the VLA model for streaming inference.`
- L328: `ctx = mp.get_context("spawn")`

### scripts/translate_dataset_seq.py
- L235: `args.sim_cfg_file, env_cfg["scene"]["robot"]["spawn"]["usd_path"]`

### scripts/create_lerobot_dataset.py
- L74: `"focal": v["spawn"]["focal_length"],`

## velocity_dynamic

### simulations/helpers.py
- L150: `# Generate additional direction tags`
- L152: `object_states = _get_direction_tags(`
- L257: `def _get_direction_tags(object_type, object_states, robot_quat):`
- L259: `"the %s moving in the robot's forward direction",`
- L260: `"the %s moving in the robot's forward-left direction",`
- L261: `"the %s moving in the robot's left direction",`
- L262: `"the %s moving in the robot's backward-left direction",`
- L263: `"the %s moving in the robot's backward direction",`
- L264: `"the %s moving in the robot's backward-right direction",`
- L265: `"the %s moving in the robot's right direction",`
- L266: `"the %s moving in the robot's forward-right direction",`
- L276: `idx = get_direction_index(state["lin_vel"], robot_quat)`
- L282: `def get_direction_index(linear_velocity, robot_quat=None, inverse=True):`

### simulations/simulate.py
- L311: `None if random_static else object_cfg.get("moving_speed", None),`
- L411: `moving_speed,`
- L415: `if moving_speed is None:`
- L423: `moving_speed,`
- L451: `object_range_bbox, object_z, moving_speed, friction, robot_position`
- L469: `assert moving_speed is not None and len(moving_speed) == 2`
- L470: `object_direction = random_position - object_position`
- L471: `object_velocity = (`
- L472: `object_direction`
- L473: `/ np.linalg.norm(object_direction)`
- L474: `* random.uniform(*moving_speed)`
- L476: `object_quat = configs.object_cfg.get_object_init_quat(object_velocity)`
- L481: `"lin_vel": object_velocity,`
- L806: `speed = torch.norm(objects_velocity, dim=-1)`
- L807: `fastest_index = torch.argmax(speed, dim=0).item()`
- L821: `"object_vel": ("curr_state", "object", "velocity"),`
- L1007: `def is_object_stopped(scene_cfg, object_velocity, n_steps=25):`
- L1008: `init_speed = np.linalg.norm(scene_cfg["object"]["init_state"]["lin_vel"])`
- L1010: `for i in range(min(n_steps, len(object_velocity))):`
- L1011: `if init_speed > 1e-2 and np.linalg.norm(object_velocity[i]) < 1e-2:`
- L1017: `def is_object_direction_changed(scene_cfg, object_velocity, n_steps=25):`
- L1020: `init_dir_idx = helpers.get_direction_index(init_velocity, robot_quat)`
- L1022: `for i in range(min(n_steps, len(object_velocity))):`
- L1023: `dir_idx = helpers.get_direction_index(object_velocity[i])`
- L1040: `object_vel = np.linalg.norm(scene_cfg["object"]["init_state"]["lin_vel"])`
- L1053: `"d" if object_vel > 1e-3 else "s",`
- L1083: `env_state, state_keys=["sm_state", "ee_pos", "object_pos", "object_vel"]`
- L1262: `if is_object_stopped(env_cfg["scene"], es["object_vel"]):`
- L1264: `if is_object_direction_changed(env_cfg["scene"], es["object_vel"]):`
- L1265: `# Remove direction tags`
- L1267: `t for t in object_tags["objects"] if not t.endswith("direction")`

### simulations/state_machines/sm_utils.py
- L34: `def is_object_static(object_velocity: torch.Tensor) -> torch.Tensor:`
- L36: `return torch.norm(object_velocity, dim=1) < STATIC_VELOCITY_THRESHOLD`
- L42: `object_velocity: torch.Tensor,`
- L48: `grasp_position = object_position.clone() + object_velocity * WAITING_TIME`
- L75: `object_velocity: torch.Tensor,`
- L89: `is_static = is_object_static(object_velocity)`
- L90: `grasp_direction = torch.zeros(batch_size, 2, device=device)`
- L112: `grasp_direction_static = torch.gather(`
- L115: `grasp_direction[is_static] = grasp_direction_static[is_static]`
- L118: `grasp_direction[~is_static] = object_velocity[~is_static, :2]`
- L121: `gsp_theta = torch.atan2(grasp_direction[:, 0], grasp_direction[:, 1])`
- L159: `offset: wp.vec3, threshold: wp.vec3, object_vel: wp.vec3`
- L161: `is_static = wp.length(object_vel) < 0.05`

### simulations/state_machines/place_sm.py
- L197: `object_vel_wp = wp.from_torch(curr_state["object"]["velocity"], wp.vec3)`
- L214: `object_vel_wp,`
- L253: `object_vel: wp.array(dtype=wp.vec3),`
- L326: `offset_object_ee, thres_object_ee, object_vel[tid]`
- L390: `offset_ee_target, thres_target_ee, object_vel[tid]`

### simulations/state_machines/pick_sm.py
- L164: `object_vel_wp = wp.from_torch(curr_state["object"]["velocity"], wp.vec3)`
- L178: `object_vel_wp,`
- L214: `object_vel: wp.array(dtype=wp.vec3),`
- L278: `offset_object_ee, thres_object_ee, object_vel[tid]`

### policies/dynamicvla/modeling_fastvlm.py
- L902: `# when using deepspeed + accelerate`
- L1064: `# when using deepspeed + accelerate`
- L1304: `# when using deepspeed + accelerate`
- L1352: `# when using deepspeed + accelerate`
- L1614: `# when using deepspeed + accelerate`

### utils/distributed.py
- L76: `# Increase the L2 fetch granularity for faster speed.`

### scripts/translate_dataset_seq.py
- L289: `sim.get_frames(env_state, ["ee_pos", "object_pos", "object_vel"]),`

### scripts/create_lerobot_dataset.py
- L194: `env_states["object_vel"][i],`
- L250: `["object_pos_", "object_rot_", "object_vel_"], rot_fmt`

## task_logic

### simulations/helpers.py
- L90: `def is_object_placed(`
- L209: `state["tags"][-1] = state["tags"][-1].replace("est", "er")`
- L250: `state["tags"][-1] = state["tags"][-1].replace("est", "er")`

### simulations/simulate.py
- L100: `def get_env_cfg(sim_cfg, task, robot, object_metadata, scene_dir):`
- L104: `import isaaclab_tasks`
- L114: `env_cfg = isaaclab_tasks.utils.parse_cfg.parse_env_cfg(`
- L173: `# Determine the objects to be used in the task`
- L175: `if task == "long-horizon":`
- L188: `# Modify task-specific parameters`
- L189: `env_cfg.episode_length_s = sim_cfg["tasks"][task]["episode_length"]`
- L212: `task, terimation_args`
- L225: `if task == "long-horizon":`
- L350: `# The container cannot be placed without occlusion`
- L632: `def get_state_machine(task_cfg, robot_cfg, sm_args={}):`
- L633: `state_machine = _get_class(task_cfg["sm"])`
- L794: `def get_next_object(scene_objects, scene, env_idx=None):`
- L864: `def simulate(sim_cfg, task, robot, scene_dir, object_metadata, seed):`
- L870: `task,`
- L906: `assert task in sim_cfg["tasks"], "Unknown task: %s." % task`
- L909: `sim_cfg["tasks"][task],`
- L930: `curr_object_idx = get_next_object(scene_objects, env.unwrapped.scene)`
- L950: `if task == "long-horizon":`
- L951: `object_placed = helpers.is_object_placed(`
- L957: `if object_placed.any():`
- L958: `for env_idx, op in enumerate(object_placed):`
- L963: `curr_object_idx[env_idx] = get_next_object(`
- L970: `"[Env%02d] Object %s placed. Next object: %s."`
- L993: `# Ignore the simulation if the task is not finished`
- L994: `# If in debug mode, save all simulation data even if the task is not finishedq`
- L1030: `def get_episode_name(task, robot, seed, scene_cfg):`
- L1050: `task,`
- L1181: `k = k.replace("_", " ").title()`
- L1187: `k = k.replace("Quat", "Rot")`
- L1244: `args.task,`
- L1271: `args.task, args.robot, seed, env_cfg["scene"]`
- L1282: `env_cfg["instruction"] = {"task": args.task, **object_tags}`
- L1341: `parser.add_argument("--task", default="pick")`

### simulations/evaluate.py
- L85: `import isaaclab_tasks`
- L96: `env_cfg = isaaclab_tasks.utils.parse_cfg.parse_env_cfg(`
- L151: `if "object_picked" in cfg:`
- L152: `task = "pick"`
- L153: `args = cfg["object_picked"]["params"]`
- L154: `elif "objects_placed" in cfg:`
- L155: `task = "place"`
- L156: `args = cfg["objects_placed"]["params"]`
- L157: `elif "object_placed" in cfg:`
- L158: `task = "place"`
- L159: `# Competible with single-object placement (legacy implementation)`
- L160: `args = cfg["object_placed"]["params"]`
- L184: `return configs.termination_cfg.get_termination_cfg(task, args)`
- L453: `# Randomize the task instruction before fixing the random seed`
- L461: `# Send the task instruction at the beginning of the simulation`
- L462: `obs_socket.send_pyobj({"task": instruction})`

### simulations/robots/piper.py
- L98: `This configuration is useful for task-space control using differential IK.`

### simulations/robots/franka.py
- L95: `This configuration is useful for task-space control using differential IK.`

### simulations/configs/scene_cfg.py
- L42: `# target object: placeholder. Can be replaced by calling `set_target_object``
- L211: `)  # Replace table height values in bbox`
- L230: `# z is replaced by the height of the table (generated in create_scene_collision.py)`

### simulations/configs/termination_cfg.py
- L16: `from isaaclab_tasks.manager_based.manipulation.lift import mdp`
- L21: `def is_object_picked(`
- L29: `assert len(objects) == 1, "Only single object picking is supported."`
- L47: `def are_objects_placed(`
- L58: `objects_placed = torch.ones(env.num_envs, dtype=torch.bool, device=env.device)`
- L78: `objects_placed = torch.logical_and(`
- L79: `objects_placed,`
- L80: `helpers.is_object_placed(`
- L93: `return torch.logical_and(objects_placed, eef_goal_dist < tolerance)`
- L135: `DONE_TERMS = ["object_picked", "objects_placed"]`
- L169: `"""Termination terms for the Pick task."""`
- L171: `object_picked = TerminationTermCfg(`
- L172: `func=is_object_picked,`
- L180: `"""Termination terms for the Pick task."""`
- L182: `objects_placed = TerminationTermCfg(`
- L183: `func=are_objects_placed,`
- L203: `def get_termination_cfg(task: str, args: dict = {}) -> TerminationsCfg:`
- L205: `if task == "pick":`
- L207: `done_term = cfg.object_picked`
- L208: `elif task in ["place", "long-horizon"]:`
- L210: `done_term = cfg.objects_placed`

### simulations/configs/env_cfg.py
- L26: `from isaaclab_tasks.manager_based.manipulation.lift import mdp`

### simulations/configs/robot_cfg.py
- L18: `from isaaclab_tasks.manager_based.manipulation.lift import mdp`
- L92: `cfg = FRANKA_PANDA_HIGH_PD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")`
- L94: `cfg = AGILEX_PIPER_HIGH_PD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")`

### simulations/state_machines/place_sm.py
- L3: `# @File:   place_sm.py`
- L28: `"""States for the place state machine."""`
- L58: `"""A simple state machine in a robot's task space to place and lift an object.`
- L73: `place_dist_thres: float = 0.1,`
- L96: `self.sm_is_placed = torch.full((num_envs,), 0, dtype=torch.int32, device=device)`
- L113: `self.place_dist_thres = place_dist_thres`
- L129: `self.sm_is_placed_wp = wp.from_torch(self.sm_is_placed, wp.int32)`
- L144: `def _get_place_pose(`
- L149: `place_position = container_position.clone()`
- L150: `place_position[:, 2] += 0.10`
- L151: `place_quat = self.final_eef_pose[:, 3:7]`
- L153: `return torch.cat([place_position, place_quat], dim=-1)`
- L181: `place_pose = self._get_place_pose(`
- L184: `object_placed = helpers.is_object_placed(`
- L198: `place_pose_wp = wp.from_torch(place_pose, wp.transform)`
- L201: `object_placed_wp = wp.from_torch(object_placed, wp.bool)`
- L210: `self.sm_is_placed_wp,`
- L217: `place_pose_wp,`
- L224: `object_placed_wp,`
- L249: `sm_is_placed: wp.array(dtype=int),`
- L256: `place_pose: wp.array(dtype=wp.transform),`
- L263: `object_placed: wp.array(dtype=bool),  # the object is placed`
- L366: `dist_ee_target = place_pose[tid][2] + (offset[tid][2] / 2.0) - ee_pose[tid][2]`
- L377: `des_ee_pose[tid] = wp.transform_multiply(offset[tid], place_pose[tid])`
- L384: `wp.transform_get_translation(place_pose[tid]),`
- L401: `place_pose[tid][0],`
- L402: `place_pose[tid][1],`
- L403: `place_pose[tid][2],`
- L415: `des_ee_pose[tid] = place_pose[tid]`
- L423: `des_ee_pose[tid] = place_pose[tid]`
- L428: `sm_is_placed[tid] = 0`
- L433: `is_object_placed = object_placed[tid]`
- L435: `if is_object_placed:`
- L436: `sm_is_placed[tid] = 0`
- L438: `sm_is_placed[tid] += 1`
- L440: `if sm_is_placed[tid] >= N_CHECK_PLACED_TIMES:`
- L445: `"TO_TARGET: is_placed: %d, %d\n", is_object_placed, sm_is_placed[tid]`

### simulations/state_machines/pick_sm.py
- L3: `# @File:   pick_sm.py`
- L26: `"""States for the pick state machine."""`
- L50: `"""A simple state machine in a robot's task space to pick and lift an object.`

### core/train.py
- L196: `# Fix: Remove the additional dimension for task`
- L197: `if isinstance(batch["task"], list) and isinstance(`
- L198: `batch["task"][0], (tuple, list)`
- L200: `batch["task"] = batch["task"][0]`

### core/test.py
- L69: `# Fix: Remove the additional dimension for task`
- L70: `if isinstance(batch["task"], list) and isinstance(`
- L71: `batch["task"][0], (tuple, list)`
- L73: `batch["task"] = batch["task"][0]`

### policies/dynamicvla/modeling_dynamicvla.py
- L99: `k = k.replace(old_key, new_key)`
- L386: `dummy_batch["task"] = ["dummy text input"]`
- L682: `tasks = batch["task"]`
- L683: `if isinstance(tasks, str):`
- L684: `tasks = [tasks]`
- L686: `if len(tasks) == 1:`
- L687: `tasks = [tasks[0] for _ in range(batch[OBS_STATE].shape[0])]`
- L689: `tasks = [task if task.endswith("\n") else f"{task}\n" for task in tasks]`
- L691: `tasks,`
- L772: `padded_tensor[:, :d] = tensor  # Efficient in-place copy`

### policies/dynamicvla/modeling_fastvlm.py
- L155: `_skip_keys_device_placement = "past_key_values"`

### utils/maya_controller.py
- L104: `send_message = "select -replace " + object_name + ";"`
- L124: `send_message = "select -replace " + object_name + ";"`
- L144: `send_message = "select -replace " + object_name + ";" + "move -relative "`
- L159: `send_message = "select -replace " + object_name + ";" + "rotate -relative "`

### utils/instruction_generator.py
- L20: `tmpl = InstructionGenerator._get_instruction_template(inst_metadata["task"])`
- L26: `def _get_instruction_template(task):`
- L27: `pick_action = random.choice(`
- L28: `["pick up", "grasp", "catch", "grab", "get hold of"]`
- L30: `place_action = random.choice(`
- L31: `["place on", "put on", "set on", "position on", "return to", "deposit in"]`
- L33: `if task == "pick":`
- L34: `return f"{pick_action} the {{object}}."`
- L35: `elif task in ["place", "long-horizon"]:`
- L36: `return f"{pick_action} the {{object}} and {place_action} the {{container}}."`
- L38: `raise ValueError(f"Unknown task: {task}")`

### utils/datasets.py
- L113: `│   └── tasks.jsonl`
- L303: `# Add task as a string`
- L304: `task_idx = episode["task_index"][frame_idx].item()`
- L305: `item["task"] = InstructionGenerator.generate_instruction(`
- L306: `self.meta.tasks[task_idx]`

### scripts/eval_libero_dataset.py
- L18: `import pickle`
- L33: `def get_libero_env(env_name, task_id, seed):`
- L39: `task_suite = benchmarks[env_name]()`
- L40: `assert task_id < task_suite.n_tasks`
- L41: `task = task_suite.get_task(task_id)`
- L46: `LIBERO_PATH, task.problem_folder, task.bddl_file`
- L54: `logging.info("Environment initialized with task: %s." % (task.name))`
- L55: `env.set_init_state(task_suite.get_task_init_states(task_id)[0])`
- L57: `return env, task.language`
- L91: `"task": instruction,`
- L120: `def get_episode_name(env_name, task_id, done):`
- L123: `task_id,`
- L129: `def main(vla_model, vla_weights, env_name, task_id, output_dir, seed, debug):`
- L143: `env, task_instruction = get_libero_env(env_name, task_id, seed)`
- L161: `get_observation(vla_model.config.input_features, obs, task_instruction),`
- L174: `os.path.join(output_dir, get_episode_name(env_name, task_id, done)),`
- L184: `% (env_name, task_id, datetime.datetime.now().strftime("%m%d-%H%M%S")),`
- L187: `pickle.dump(`
- L190: `"task": task_id,`
- L191: `"inst": task_instruction,`
- L222: `"--task",`
- L225: `help="The task ID in the LIBERO environment",`
- L243: `args.task,`

### scripts/update_usd_tex_loc.py
- L43: `new_texture_path = old_texture_path.replace(`
- L47: `# new_texture_path = new_texture_path.replace("/texture.png", ".png")`

### scripts/replay_dataset_seq.py
- L63: `# Replace the action with the next state`

### scripts/translate_dataset_seq.py
- L101: `# Replace the action with the next state`

### scripts/inference.py
- L15: `import pickle`
- L181: `if "task" in observation:`
- L182: `instruction = observation["task"]`
- L184: `"[Test%02d] Received new task: %s" % (n_tests, instruction.strip())`
- L195: `observation["task"] = instruction`
- L249: `pickle.dump({"vla": vla_cfg, "state": states, "action": actions}, fp)`
- L328: `k: torch.stack(v, dim=1) for k, v in tr_observations.items() if k != "task"`
- L330: `for k in ["task", "index", "dt_scale"]:`
- L361: `"task": [observation["task"]],`

### scripts/create_usd_objects.py
- L47: `"cmds.file('%s', i=True, type='OBJ')" % input_file_path.replace("\\", "/")`
- L57: `% output_file_path.replace("\\", "/")`

### scripts/create_libero_dataset.py
- L102: `task=step["language_instruction"].decode(),`

### scripts/create_usd_scenes.py
- L258: `% (furniture["model"].replace("\\", "/"), furniture_name)`
- L434: `output_dir, lf.replace(".json", ".usd")`
- L435: `).replace("\\", "/")`

### scripts/fix_error_scenes.py
- L58: `def replace_in_list(spec_list):`
- L59: `"""Replace paths in SdfTargetProxy or SdfConnectionsProxy"""`
- L74: `replace_in_list(spec.targetPathList)`
- L76: `replace_in_list(spec.connectionPathList)`

### scripts/create_lerobot_dataset.py
- L88: `parquet_path = episode_path.replace(".h5", ".parquet")`
- L92: `stat_path = episode_path.replace(".h5", ".stats")`
- L154: `video_path = episode_path.replace(".h5", ".%s.mp4" % k.split(".")[-1])`
- L316: `def get_task(instruction_metadata, dataset_tasks):`
- L317: `task_prompt = json.dumps(instruction_metadata)`
- L318: `if task_prompt in dataset_tasks:`
- L319: `task_index = dataset_tasks.index(task_prompt)`
- L321: `task_index = len(dataset_tasks)`
- L322: `dataset_tasks.append(task_prompt)`
- L324: `return task_index, task_prompt`
- L328: `input_dir, output_dir, dataset_info, episode_name, task_index`
- L345: `task_index,`
- L349: `input_dir, episode_name, episode_index, task_index, n_frames, dataset_info`
- L384: `task_index,`
- L398: `df["task_index"] = task_index`
- L404: `input_dir, episode_name, episode_index, task_index, n_frames, dataset_info`
- L417: `episode_stats["task_index"] = _get_dataset_stats(task_index, task_index, n_frames)`
- L432: `def get_dataset_info(dataset_info, episode_metadata, n_tasks):`
- L433: `dataset_info["total_tasks"] = n_tasks`
- L462: `("task_index", "int64"),`
- L536: `dataset_tasks = []`
- L553: `task_index, task_prompt = get_task(env_cfg["instruction"], dataset_tasks)`
- L555: `input_dir, output_dir, dataset_info, episode, task_index`
- L570: `{"episode_index": episode_index, "tasks": task_prompt, "length": length},`
- L581: `# Save dataset info and tasks`
- L583: `get_dataset_info(dataset_info, episode_metadata, len(dataset_tasks)),`
- L586: `for tid, task in enumerate(dataset_tasks):`
- L588: `{"task_index": tid, "task": task},`
- L589: `pathlib.Path(os.path.join(output_dir, "meta", "tasks.jsonl")),`

## instruction

### simulations/helpers.py
- L20: `for i in range(8):  # Support up to 8 background objects/containers`
- L140: `"objects",`
- L141: `"containers",`
- L158: `# Remove duplicate tags (causing confusion in instruction generation)`
- L196: `object_type.rstrip("s") if object_type == "objects" else state["category"]`
- L236: `if object_type == "objects"`
- L270: `object_type.rstrip("s") if object_type == "objects" else state["category"]`

### simulations/simulate.py
- L40: `# Get the sizes of all objects (for grasping)`
- L49: `"tags": [object_category],  # Default tag for instruction generation`
- L74: `objects = [`
- L77: `for o in objects:`
- L157: `# Determine the poses of objects and containers`
- L165: `# Dynamically add objects to the scene`
- L166: `env_cfg.scene = _set_up_scene_objects(env_cfg.scene, object_states["objects"])`
- L167: `# Dynamically add containers to the scene`
- L168: `if "containers" in object_states and object_states["containers"]:`
- L169: `env_cfg.scene = _set_up_scene_containers(`
- L170: `env_cfg.scene, object_states["containers"]`
- L173: `# Determine the objects to be used in the task`
- L174: `objects = []`
- L176: `objects = [key for key in vars(env_cfg.scene) if key.startswith("object")]`
- L178: `objects = ["object"]`
- L186: `for o in objects`
- L196: `"objects": objects,`
- L209: `sim_cfg["scene"]["objects"]["perturbation"]`
- L220: `["VELOCITY"] if k == "containers" else None,`
- L221: `sim_cfg["scene"]["objects"]["tag_thresholds"],`
- L226: `object_tags["objects"] = ["entire set of objects"]`
- L228: `logging.debug("Object tags: %s" % object_tags)`
- L229: `return env_cfg, object_tags, objects, object_sizes`
- L287: `object_states = {"objects": [], "containers": []}`
- L288: `# Generate the poses of objects (The first object is the target object)`
- L289: `object_cfg = sim_cfg["scene"]["objects"]`
- L300: `for oi in range(object_cfg["n_objects"]):`
- L315: `object_states["objects"].append(`
- L323: `# Generate the poses of containers (The first container is the target container)`
- L324: `container_cfg = sim_cfg["scene"]["containers"]`
- L339: `for _ in range(container_cfg["n_containers"]):`
- L356: `object_states["containers"].append(`
- L487: `container_size, object_range_bbox, random_orientation, existing_objects`
- L508: `# Check whether the container is occluding with existing objects/containers`
- L509: `for eo in existing_objects["objects"] + existing_objects["containers"]:`
- L550: `def _set_up_scene_objects(scene_cfg, object_states):`
- L556: `other_objects = object_states[1:]`
- L575: `# Add more objects to the scene`
- L576: `for i, o in enumerate(other_objects):`
- L595: `def _set_up_scene_containers(scene_cfg, container_states):`
- L794: `def get_next_object(scene_objects, scene, env_idx=None):`
- L796: `n_envs = len(scene_objects)`
- L798: `if len(scene_objects[i]) == 0 or (env_idx is not None and i != env_idx):`
- L802: `objects = scene_objects[i]`
- L803: `objects_velocity = torch.cat(`
- L804: `[scene[o].data.root_lin_vel_w[i : i + 1] for o in objects], dim=0`
- L806: `speed = torch.norm(objects_velocity, dim=-1)`
- L868: `env_cfg, object_tags, objects, object_sizes = get_env_cfg(`
- L876: `if not object_tags["objects"]:`
- L879: `sim_cfg["scene"]["containers"]["n_containers"] > 0`
- L880: `and not object_tags["containers"]`
- L929: `scene_objects = [copy.deepcopy(objects) for _ in range(env.unwrapped.num_envs)]`
- L930: `curr_object_idx = get_next_object(scene_objects, env.unwrapped.scene)`
- L931: `curr_object = [so[coi] for so, coi in zip(scene_objects, curr_object_idx)]`
- L959: `if not op or len(scene_objects[env_idx]) < 2:`
- L962: `scene_objects[env_idx].remove(curr_object[env_idx])`
- L964: `scene_objects, env.unwrapped.scene, env_idx`
- L967: `_next_object = scene_objects[env_idx][curr_object_idx[env_idx]]`
- L1031: `n_objects = len(`
- L1054: `n_objects,`
- L1226: `# Get metadata for the objects (size, description, orientation)`
- L1227: `object_categories = sim_cfg["scene"]["objects"]["categories"]`
- L1228: `container_categories = sim_cfg["scene"]["containers"].get("categories", [])`
- L1266: `object_tags["objects"] = [`
- L1267: `t for t in object_tags["objects"] if not t.endswith("direction")`
- L1282: `env_cfg["instruction"] = {"task": args.task, **object_tags}`
- L1336: `"--object_dir", default=os.path.join(PROJECT_HOME, os.pardir, "objects")`

### simulations/evaluate.py
- L31: `from utils.instruction_generator import InstructionGenerator`
- L143: `# Dynamically add objects / containers to scene`
- L144: `env_cfg.scene = _set_up_scene_objects(env_cfg.scene, cfg["scene"], object_dir)`
- L154: `elif "objects_placed" in cfg:`
- L156: `args = cfg["objects_placed"]["params"]`
- L161: `args["objects"] = ["object"]`
- L242: `def _set_up_scene_objects(scene_cfg, cfg, object_dir):`
- L453: `# Randomize the task instruction before fixing the random seed`
- L454: `instruction = InstructionGenerator.generate_instruction(env_cfg["instruction"])`
- L461: `# Send the task instruction at the beginning of the simulation`
- L462: `obs_socket.send_pyobj({"task": instruction})`
- L634: `"--object_dir", default=os.path.join(PROJECT_HOME, os.pardir, "objects")`

### simulations/configs/scene_cfg.py
- L43: `# more objects can be added to the scene by calling `add_object``

### simulations/configs/termination_cfg.py
- L25: `objects: list[str] = ["object"],`
- L29: `assert len(objects) == 1, "Only single object picking is supported."`
- L30: `object = env.scene[objects[0]]`
- L47: `def are_objects_placed(`
- L50: `objects: list[str],`
- L58: `objects_placed = torch.ones(env.num_envs, dtype=torch.bool, device=env.device)`
- L70: `for obj in objects:`
- L78: `objects_placed = torch.logical_and(`
- L79: `objects_placed,`
- L93: `return torch.logical_and(objects_placed, eef_goal_dist < tolerance)`
- L96: `def are_objects_dropped(`
- L99: `objects: list[str],`
- L102: `for obj in objects:`
- L111: `def are_objects_unreachable(`
- L114: `objects: list[str],`
- L121: `for obj in objects:`
- L135: `DONE_TERMS = ["object_picked", "objects_placed"]`
- L150: `func=are_objects_dropped,`
- L153: `"objects": ["object"],`
- L158: `#     func=are_objects_unreachable,`
- L161: `#         "objects": ["object"],`
- L182: `objects_placed = TerminationTermCfg(`
- L183: `func=are_objects_placed,`
- L186: `"objects": None,`
- L210: `done_term = cfg.objects_placed`

### simulations/state_machines/sm_utils.py
- L87: `# Consider the object quaternion to determine the grasp quaternion for static objects`

### utils/maya_controller.py
- L189: `def set_current_key_frame_for_objects(self, object_list):`
- L190: `"""Set keyframe for a list of objects`
- L274: `def get_all_objects(self):`
- L276: `Get all the objects from Maya scene`

### utils/instruction_generator.py
- L3: `# @File:   instruction_generator.py`
- L16: `def generate_instruction(inst_metadata):`
- L20: `tmpl = InstructionGenerator._get_instruction_template(inst_metadata["task"])`
- L21: `object_desc = random.choice(inst_metadata.get("objects", [""]))`
- L22: `container_desc = random.choice(inst_metadata.get("containers", [""]))`
- L26: `def _get_instruction_template(task):`

### utils/datasets.py
- L28: `from utils.instruction_generator import InstructionGenerator`
- L305: `item["task"] = InstructionGenerator.generate_instruction(`

### scripts/create_scene_collision.py
- L80: `def remove_table_objects(stage):`
- L137: `from isaacsim.core.api.objects.cuboid import DynamicCuboid`
- L266: `# Remove objects on tables`
- L267: `remove_table_objects(stage)`
- L284: `# Remove objects on tables`
- L285: `remove_table_objects(stage)`

### scripts/fix_lerobot_videos.py
- L108: `default="hzxie/dynamic_objects",`

### scripts/eval_libero_dataset.py
- L60: `def get_observation(cfg, obs, instruction):`
- L91: `"task": instruction,`
- L143: `env, task_instruction = get_libero_env(env_name, task_id, seed)`
- L161: `get_observation(vla_model.config.input_features, obs, task_instruction),`
- L191: `"inst": task_instruction,`

### scripts/replay_dataset_seq.py
- L91: `# Set up the instruction and environment`
- L155: `"--object_dir", default=os.path.join(PROJECT_HOME, os.pardir, "objects")`

### scripts/translate_dataset_seq.py
- L165: `n_exp_objects = len([k for k in scene_cfg.keys() if k.startswith(object_type)])`
- L174: `n_act_objects = len(`
- L181: `if n_act_objects < n_exp_objects:`
- L244: `# Set up the instruction and environment`
- L265: `and len(env_cfg["instruction"]["objects"]) != 0`
- L337: `"--object_dir", default=os.path.join(PROJECT_HOME, os.pardir, "objects")`

### scripts/inference.py
- L141: `instruction = None`
- L182: `instruction = observation["task"]`
- L184: `"[Test%02d] Received new task: %s" % (n_tests, instruction.strip())`
- L186: `# Reset the model with the new instruction`
- L194: `elif instruction is not None:`
- L195: `observation["task"] = instruction`

### scripts/create_object_collision.py
- L149: `"--output_dir", default=os.path.join(PROJECT_HOME, os.pardir, "objects")`

### scripts/create_usd_objects.py
- L3: `# @File:   create_usd_objects.py`

### scripts/create_libero_dataset.py
- L102: `task=step["language_instruction"].decode(),`

### scripts/create_usd_scenes.py
- L374: `n_objects = 0`
- L378: `n_objects += 1`
- L398: `maya_ctl, n_objects, dict(list(furniture.items()) + list(v.items()))`
- L405: `_add_mesh_to_scene(maya_ctl, n_objects, mesh, shader_name)`

### scripts/fix_error_scenes.py
- L22: `def contains_orphan_objects(stage):`
- L23: `orphan_objects = []`
- L28: `orphan_objects.append(prim)`
- L30: `return orphan_objects`
- L106: `def contains_floating_objects(stage):`
- L108: `floating_objects = []`
- L114: `# Detect floating objects (that are not lights)`
- L117: `floating_objects.append(prim)`
- L119: `floating_objects.append(dup_prim)`
- L121: `return floating_objects`
- L182: `orphan_objects = contains_orphan_objects(stage)`
- L183: `if orphan_objects:`
- L189: `for oo in orphan_objects:`
- L195: `floating_objects = contains_floating_objects(stage)`
- L196: `if floating_objects:`
- L198: `logging.info("Floating objects[%s] found in %s" % (floating_objects, uf))`
- L199: `for fo in floating_objects:`

### scripts/create_lerobot_dataset.py
- L316: `def get_task(instruction_metadata, dataset_tasks):`
- L317: `task_prompt = json.dumps(instruction_metadata)`
- L553: `task_index, task_prompt = get_task(env_cfg["instruction"], dataset_tasks)`
- L614: `default="hzxie/dynamic-objects",`

## quality_filters

### simulations/simulate.py
- L211: `env_cfg.terminations = configs.termination_cfg.get_termination_cfg(`
- L1007: `def is_object_stopped(scene_cfg, object_velocity, n_steps=25):`
- L1017: `def is_object_direction_changed(scene_cfg, object_velocity, n_steps=25):`
- L1262: `if is_object_stopped(env_cfg["scene"], es["object_vel"]):`
- L1264: `if is_object_direction_changed(env_cfg["scene"], es["object_vel"]):`

### simulations/evaluate.py
- L110: `env_cfg.terminations = _get_terimation_cfg(cfg["terminations"], tolerance, device)`
- L154: `elif "objects_placed" in cfg:`
- L156: `args = cfg["objects_placed"]["params"]`

### simulations/configs/termination_cfg.py
- L47: `def are_objects_placed(`
- L58: `objects_placed = torch.ones(env.num_envs, dtype=torch.bool, device=env.device)`
- L78: `objects_placed = torch.logical_and(`
- L79: `objects_placed,`
- L93: `return torch.logical_and(objects_placed, eef_goal_dist < tolerance)`
- L135: `DONE_TERMS = ["object_picked", "objects_placed"]`
- L149: `object_dropping = TerminationTermCfg(`
- L182: `objects_placed = TerminationTermCfg(`
- L183: `func=are_objects_placed,`
- L210: `done_term = cfg.objects_placed`
- L215: `if k in cfg.object_dropping.params:`
- L216: `cfg.object_dropping.params[k] = v`

### simulations/configs/env_cfg.py
- L133: `terminations: TerminationsCfg = MISSING`

### scripts/translate_dataset_seq.py
- L281: `"Cam Occluded: %s; Object Occluded: %s; Container Occluded: %s"`

## Required final answer from CLI

After inspection, write a section named `MINIMAL PATCH PLAN` with:
1. Exact files to modify later.
2. Exact functions to modify later.
3. Whether static-object behavior can be added with CLI flags, config file, or wrapper.
4. Whether baseline translation will remain compatible.
5. Risks.
6. Recommended first implementation step.
7. Things that should NOT be touched.

Do not modify files in this step.


# Manual Design Questions To Answer

Please answer these clearly:

## A. What does “dynamic object” mean in current code?
- Are objects given initial velocity?
- Are objects spawned in unstable positions?
- Are objects deliberately moved by scene events?
- Or are they just physics-enabled?

## B. Where should static behavior be enforced?
Candidate minimal controls:
- zero object linear/angular velocity at reset
- add settle frames before scripted control starts
- reject episodes where object moves before robot contact
- restrict sampled spawn pose to support/table anchors
- keep gravity and collisions enabled

## C. How to preserve original pipeline?
Preferred:
- create a copied dev script or config under `_dev/data_collection_mods/working_copies`
- keep original baseline untouched
- later produce a small patch file
- output same H5/JSON/MP4 keys

## D. What should be randomized?
- scene
- target object
- container/goal object
- support/table anchor
- object XY position
- object yaw
- instruction formulation

## E. What should be the first implementation?
Recommend the smallest version first:
- add static spawn/settle mode
- one task: place/franka
- headless
- n=3
- translate
- multicam check

# Design Analysis and Answers

## A. What does “dynamic object” mean in current code?
- **Are objects given initial velocity?** Yes. In `simulations/simulate.py` (line 471), the target object (the first object in the sequence, `oi == 0`) is assigned an initial linear velocity directionally mapped towards the center/robot and scaled by a value sampled from `moving_speed` in `sim_cfg.yaml`. This velocity is set on the rigid body via `lin_vel`.
- **Are objects spawned in unstable positions?** No. They are spawned at a valid table-height offset (calculated in `_get_object_z`), but with an initial linear velocity vector that slides them across the table.
- **Are objects deliberately moved by scene events?** No. They only slide due to the initial velocity, with contacts and gravity naturally acting on them.
- **Or are they just physics-enabled?** They are standard rigid bodies with physical materials (friction and restitution) enabled, which slide and eventually come to rest or interact with other objects/robot.

## B. Where should static behavior be enforced?
To collect clean static manipulation datasets:
- **Zero initial velocity**: Assign `object_velocity = [0.0, 0.0, 0.0]` for all objects. This can be done by configuring `moving_speed` to `[0.0, 0.0]` or overriding `lin_vel` in the code.
- **Settle frames**: We can allow the physics simulation to run for a short duration (e.g. 50-100 steps) at reset without the robot moving, letting objects drop and settle naturally onto the table surface.
- **Reject early movements**: Ensure the object remains stationary until the gripper contacts it.
- **Spawn height/anchors**: Keep them within standard reachable table bounds on table surfaces.
- **Physics settings**: Keep gravity, material properties, and collisions enabled.

## C. How to preserve original pipeline?
- **Develop in Sandbox**: All modifications will be done strictly under `_dev/data_collection_mods/working_copies/` using copies of the collection scripts.
- **No baseline changes**: The baseline repository under `dynamic-vla/` remains clean and untouched.
- **Identical schema**: Maintain the exact structure, keys, and data formats in the generated `.h5` and `.json` datasets. This ensures 100% compatibility with `translate_dataset_seq.py`.

## D. What should be randomized?
To ensure generalization, we will randomize:
- Table scene selection.
- Target object category and USD model.
- Container/goal category and USD model.
- Object spawn location (XY position) on the table.
- Object spawn yaw orientation.
- Support container positions.
- Instruction formulations.

## E. What should be the first implementation?
The first trial implementation will:
1. Configure `sim_cfg.yaml` in the sandbox with `moving_speed: [0.0, 0.0]`.
2. Run a small simulation matrix ($n=3$) for the `place` task on `franka` in headless mode.
3. Translate the datasets and verify them using the multicam video generator.

---

# MINIMAL PATCH PLAN

### 1. Exact files to modify later
- `_dev/data_collection_mods/working_copies/dynamic-vla/simulations/simulate.py`
- `_dev/data_collection_mods/working_copies/dynamic-vla/simulations/configs/sim_cfg.yaml`

### 2. Exact functions to modify later
- `_get_object_states` / `_get_dynamic_object_state` in `simulate.py`: Force `lin_vel` to `[0.0, 0.0, 0.0]` when a `--static` flag is set or configure it directly.
- `helpers.py`: Verify that direction tag generation correctly falls back to `"stationary <object>"` when velocity is zero.

### 3. Execution controls
Static-object behavior can be controlled via:
- Setting `moving_speed: [0.0, 0.0]` in `sim_cfg.yaml`.
- Adding a CLI flag `--static` to `simulate.py` to programmatically override velocities to zero.

### 4. Translation Compatibility
Yes, the baseline translation script (`translate_dataset_seq.py`) remains 100% compatible since H5 keys, frames, states, and scene files are structurally identical.

### 5. Risks
- Zero initial velocity might cause some objects to spawn slightly floating if the table surface height is not perfectly aligned with `_get_object_z`. We must ensure they have a few frames to settle onto the table before the robot moves.
- Setting target velocity to zero will cause the direction checker (`is_object_direction_changed`) to remove direction tags, which is expected and correct.

### 6. Recommended first implementation step
Edit `sim_cfg.yaml` and `simulate.py` in the dev sandbox to enforce static objects and test a run with $n=3$ in headless mode.

