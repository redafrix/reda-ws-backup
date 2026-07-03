# Smart Object/Receptacle Preflight and Physics Profiles

Goal:
Make collection reject physically impossible objects and pairs before simulation, require a real receptacle for every episode, and stabilize slippery objects using object-specific physics profiles.

No target-area dataset episodes.
No global gripper modifications.
No large-scale collection.

## Starting repository state
- branch: object-integration-static-assets
- commit: d42c7cd8e8c37e00047a46cb6578e237cd3268b4
- status:

Log:
d42c7cd (HEAD -> object-integration-static-assets, tag: checkpoint/readiness-validated-20260615, origin/object-integration-static-assets) feat(readiness): cache catalog/geometry lookup and fix clutter_02 layout sampling
6a3c181 (tag: checkpoint/robustness-verified-20260615) fix(configs): adjust fcan03 grasp depth and target mass to prevent slip in tray placement
e448c6a Fix placement success metadata and validate diverse receptacle tasks
07dab83 (tag: checkpoint/upstream-master-integrated-20260615, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
43da87b feat: add geometry-aware deterministic table clutter
4a65eac (backup/object-integration-before-master-20260615_093855, backup/object-integration-before-finalized-master-20260615_104358) Add true receptacle-goal metadata, instruction generation, success mode, and exit watchdog
8cc8080 feat: use receptacle bottom clearance for placement release height
286fa2b fix: make receptacle placement success geometry-aware
6e2cb86 feat: add sampled placement receptacle target
441bebd Implement config-driven receptacle-goal mode for pick-place and add verified configs
ce9fc15 fix: stop simulation before scene prim teardown
src/franka_wrist_camera_scene/objects/geometry.py:1:"""Planar geometry inference for USD object assets."""
src/franka_wrist_camera_scene/objects/geometry.py:17:    local_bbox_min: tuple[float, float, float]
src/franka_wrist_camera_scene/objects/geometry.py:18:    local_bbox_max: tuple[float, float, float]
src/franka_wrist_camera_scene/objects/geometry.py:19:    local_bbox_size: tuple[float, float, float]
src/franka_wrist_camera_scene/objects/geometry.py:34:    geometry: PlanarGeometry
src/franka_wrist_camera_scene/objects/geometry.py:90:def infer_planar_geometry_from_usd(
src/franka_wrist_camera_scene/objects/geometry.py:94:    """Infer local planar object geometry from USD mesh vertices."""
src/franka_wrist_camera_scene/objects/geometry.py:103:    bbox_size = max_xyz - min_xyz
src/franka_wrist_camera_scene/objects/geometry.py:133:        raise RuntimeError(f"Degenerate planar geometry for USD file: {usd_path}")
src/franka_wrist_camera_scene/objects/geometry.py:139:        local_bbox_min=tuple(float(value) for value in min_xyz),
src/franka_wrist_camera_scene/objects/geometry.py:140:        local_bbox_max=tuple(float(value) for value in max_xyz),
src/franka_wrist_camera_scene/objects/geometry.py:141:        local_bbox_size=tuple(float(value) for value in bbox_size),
src/franka_wrist_camera_scene/objects/geometry.py:152:def generate_object_geometry_records(
src/franka_wrist_camera_scene/objects/geometry.py:156:    """Generate planar geometry records for every variant in an object catalog."""
src/franka_wrist_camera_scene/objects/geometry.py:161:            geometry = infer_planar_geometry_from_usd(
src/franka_wrist_camera_scene/objects/geometry.py:171:                    geometry=geometry,
src/franka_wrist_camera_scene/objects/geometry.py:182:def _geometry_to_dict(geometry: PlanarGeometry) -> dict:
src/franka_wrist_camera_scene/objects/geometry.py:184:        "local_bbox_min": _rounded_list(geometry.local_bbox_min),
src/franka_wrist_camera_scene/objects/geometry.py:185:        "local_bbox_max": _rounded_list(geometry.local_bbox_max),
src/franka_wrist_camera_scene/objects/geometry.py:186:        "local_bbox_size": _rounded_list(geometry.local_bbox_size),
src/franka_wrist_camera_scene/objects/geometry.py:187:        "planar_centroid_local": _rounded_list(geometry.planar_centroid_local),
src/franka_wrist_camera_scene/objects/geometry.py:189:            _rounded_list(geometry.planar_major_axis_local)
src/franka_wrist_camera_scene/objects/geometry.py:190:            if geometry.planar_major_axis_local is not None
src/franka_wrist_camera_scene/objects/geometry.py:194:            _rounded_list(geometry.planar_minor_axis_local)
src/franka_wrist_camera_scene/objects/geometry.py:195:            if geometry.planar_minor_axis_local is not None
src/franka_wrist_camera_scene/objects/geometry.py:198:        "planar_extent_major": round(geometry.planar_extent_major, 6),
src/franka_wrist_camera_scene/objects/geometry.py:199:        "planar_extent_minor": round(geometry.planar_extent_minor, 6),
src/franka_wrist_camera_scene/objects/geometry.py:200:        "planar_aspect_ratio": round(geometry.planar_aspect_ratio, 6),
src/franka_wrist_camera_scene/objects/geometry.py:201:        "yaw_relevant": geometry.yaw_relevant,
src/franka_wrist_camera_scene/objects/geometry.py:205:def write_object_geometry(
src/franka_wrist_camera_scene/objects/geometry.py:210:    """Generate and write planar geometry metadata for a USD object catalog."""
src/franka_wrist_camera_scene/objects/geometry.py:212:    records = generate_object_geometry_records(
src/franka_wrist_camera_scene/objects/geometry.py:226:                **_geometry_to_dict(record.geometry),
src/franka_wrist_camera_scene/objects/selection.py:1:"""Deterministic object selection helpers."""
src/franka_wrist_camera_scene/objects/geometry_registry.py:1:"""Lookup utilities for generated object geometry metadata."""
src/franka_wrist_camera_scene/objects/geometry_registry.py:15:    """Planar geometry in the authored USD object coordinate frame."""
src/franka_wrist_camera_scene/objects/geometry_registry.py:18:    local_bbox_min: tuple[float, float, float]
src/franka_wrist_camera_scene/objects/geometry_registry.py:19:    local_bbox_max: tuple[float, float, float]
src/franka_wrist_camera_scene/objects/geometry_registry.py:20:    local_bbox_size: tuple[float, float, float]
src/franka_wrist_camera_scene/objects/geometry_registry.py:51:def load_object_geometry_registry(
src/franka_wrist_camera_scene/objects/geometry_registry.py:52:    geometry_config: str = "object_geometry.generated.yaml",
src/franka_wrist_camera_scene/objects/geometry_registry.py:54:    path = REPO_ROOT / "configs" / geometry_config
src/franka_wrist_camera_scene/objects/geometry_registry.py:58:        raise ValueError(f"Unsupported object geometry format_version: {data['format_version']}")
src/franka_wrist_camera_scene/objects/geometry_registry.py:65:            raise ValueError(f"Duplicate object geometry record: {key}")
src/franka_wrist_camera_scene/objects/geometry_registry.py:69:            local_bbox_min=_tuple3(record["local_bbox_min"]),
src/franka_wrist_camera_scene/objects/geometry_registry.py:70:            local_bbox_max=_tuple3(record["local_bbox_max"]),
src/franka_wrist_camera_scene/objects/geometry_registry.py:71:            local_bbox_size=_tuple3(record["local_bbox_size"]),
src/franka_wrist_camera_scene/objects/geometry_registry.py:87:def get_object_geometry(
src/franka_wrist_camera_scene/objects/geometry_registry.py:94:        raise KeyError(f"Missing object geometry record for {category_id}/{variant_id}")
src/franka_wrist_camera_scene/objects/__init__.py:1:"""USD object catalog and selection utilities."""
src/franka_wrist_camera_scene/collection/reaching.py:14:from franka_wrist_camera_scene.control.gripper import GripperController
src/franka_wrist_camera_scene/collection/reaching.py:39:    gripper: GripperController,
src/franka_wrist_camera_scene/collection/reaching.py:110:        # 3. Update and apply gripper command
src/franka_wrist_camera_scene/collection/reaching.py:111:        gripper.set_width(cmd.finger_opening_m)
src/franka_wrist_camera_scene/collection/reaching.py:112:        gripper.apply(robot)
src/franka_wrist_camera_scene/collection/reaching.py:199:        gripper = None
src/franka_wrist_camera_scene/collection/reaching.py:207:                geometry_config=target_object_cfg["geometry_config"],
src/franka_wrist_camera_scene/collection/reaching.py:228:            gripper = GripperController()
src/franka_wrist_camera_scene/collection/reaching.py:233:            gripper.bind(scene, robot)
src/franka_wrist_camera_scene/collection/reaching.py:265:                gripper=gripper,
src/franka_wrist_camera_scene/collection/reaching.py:281:                object_yaw_relevant=object_context.geometry.yaw_relevant,
src/franka_wrist_camera_scene/collection/reaching.py:282:                object_planar_aspect_ratio=object_context.geometry.planar_aspect_ratio,
src/franka_wrist_camera_scene/collection/reaching.py:283:                object_planar_minor_axis_local=object_context.geometry.planar_minor_axis_local,
src/franka_wrist_camera_scene/collection/reaching.py:284:                object_planar_major_axis_local=object_context.geometry.planar_major_axis_local,
src/franka_wrist_camera_scene/collection/reaching.py:290:            del scene, robot, ik, gripper, policy
src/franka_wrist_camera_scene/collection/pick_place.py:16:from franka_wrist_camera_scene.control.gripper import GripperController
src/franka_wrist_camera_scene/collection/pick_place.py:28:from franka_wrist_camera_scene.tasks.placement_geometry import object_root_pose_on_support
src/franka_wrist_camera_scene/collection/pick_place.py:41:        geometry_config=sampling_cfg["geometry_config"],
src/franka_wrist_camera_scene/collection/pick_place.py:61:    gripper: GripperController,
src/franka_wrist_camera_scene/collection/pick_place.py:83:    placement_target_category_id: str | None = None,
src/franka_wrist_camera_scene/collection/pick_place.py:84:    placement_target_variant_id: str | None = None,
src/franka_wrist_camera_scene/collection/pick_place.py:85:    placement_target_label: str | None = None,
src/franka_wrist_camera_scene/collection/pick_place.py:86:    placement_target_usd_path: str | None = None,
src/franka_wrist_camera_scene/collection/pick_place.py:87:    placement_target_grasp_strategy: str | None = None,
src/franka_wrist_camera_scene/collection/pick_place.py:88:    placement_target_pos_local: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/collection/pick_place.py:126:        placement_target_category_id=placement_target_category_id,
src/franka_wrist_camera_scene/collection/pick_place.py:127:        placement_target_variant_id=placement_target_variant_id,
src/franka_wrist_camera_scene/collection/pick_place.py:128:        placement_target_label=placement_target_label,
src/franka_wrist_camera_scene/collection/pick_place.py:129:        placement_target_usd_path=placement_target_usd_path,
src/franka_wrist_camera_scene/collection/pick_place.py:130:        placement_target_grasp_strategy=placement_target_grasp_strategy,
src/franka_wrist_camera_scene/collection/pick_place.py:131:        placement_target_pos_local=placement_target_pos_local,
src/franka_wrist_camera_scene/collection/pick_place.py:134:        goal_type=getattr(policy.spec, "goal_type", "target_area"),
src/franka_wrist_camera_scene/collection/pick_place.py:135:        success_metric=getattr(policy.spec, "success_metric", "target_area_center"),
src/franka_wrist_camera_scene/collection/pick_place.py:166:        # 3. Update and apply gripper command
src/franka_wrist_camera_scene/collection/pick_place.py:167:        gripper.set_width(cmd.finger_opening_m)
src/franka_wrist_camera_scene/collection/pick_place.py:168:        gripper.apply(robot)
src/franka_wrist_camera_scene/collection/pick_place.py:230:    placement_target_cfg = collection_cfg.get("placement_target")
src/franka_wrist_camera_scene/collection/pick_place.py:256:        gripper = None
src/franka_wrist_camera_scene/collection/pick_place.py:265:            if placement_target_cfg is not None:
src/franka_wrist_camera_scene/collection/pick_place.py:266:                placement_context = _load_collection_object_context(placement_target_cfg, placement_rng)
src/franka_wrist_camera_scene/collection/pick_place.py:292:                    object_bbox_min_z=placement_context.geometry.local_bbox_min[2],
src/franka_wrist_camera_scene/collection/pick_place.py:299:                object_context.geometry.planar_minor_axis_local
src/franka_wrist_camera_scene/collection/pick_place.py:300:                if object_context.geometry.yaw_relevant
src/franka_wrist_camera_scene/collection/pick_place.py:309:                object_local_bbox_min=object_context.geometry.local_bbox_min,
src/franka_wrist_camera_scene/collection/pick_place.py:310:                object_local_bbox_max=object_context.geometry.local_bbox_max,
src/franka_wrist_camera_scene/collection/pick_place.py:311:                placement_target_pos_local=placement_receptacle_pos_local,
src/franka_wrist_camera_scene/collection/pick_place.py:312:                placement_target_local_bbox_min=placement_context.geometry.local_bbox_min if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:313:                placement_target_local_bbox_max=placement_context.geometry.local_bbox_max if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:330:                    placement_target_context=placement_context,
src/franka_wrist_camera_scene/collection/pick_place.py:331:                    placement_target_xy=placement_xy,
src/franka_wrist_camera_scene/collection/pick_place.py:345:                    "local_bbox_min": list(clutter_spec.context.geometry.local_bbox_min),
src/franka_wrist_camera_scene/collection/pick_place.py:346:                    "local_bbox_max": list(clutter_spec.context.geometry.local_bbox_max),
src/franka_wrist_camera_scene/collection/pick_place.py:360:                    physics_overrides=collection_cfg.get("physics_overrides", {}),
src/franka_wrist_camera_scene/collection/pick_place.py:366:            gripper = GripperController()
src/franka_wrist_camera_scene/collection/pick_place.py:371:            gripper.bind(scene, robot)
src/franka_wrist_camera_scene/collection/pick_place.py:387:                gripper=gripper,
src/franka_wrist_camera_scene/collection/pick_place.py:404:                object_yaw_relevant=object_context.geometry.yaw_relevant,
src/franka_wrist_camera_scene/collection/pick_place.py:405:                object_planar_aspect_ratio=object_context.geometry.planar_aspect_ratio,
src/franka_wrist_camera_scene/collection/pick_place.py:406:                object_planar_minor_axis_local=object_context.geometry.planar_minor_axis_local,
src/franka_wrist_camera_scene/collection/pick_place.py:407:                object_planar_major_axis_local=object_context.geometry.planar_major_axis_local,
src/franka_wrist_camera_scene/collection/pick_place.py:409:                placement_target_category_id=placement_context.category_id if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:410:                placement_target_variant_id=placement_context.variant_id if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:411:                placement_target_label=placement_context.label if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:412:                placement_target_usd_path=placement_usd_path,
src/franka_wrist_camera_scene/collection/pick_place.py:413:                placement_target_grasp_strategy=placement_context.grasp_strategy if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:414:                placement_target_pos_local=placement_receptacle_pos_local,
src/franka_wrist_camera_scene/collection/pick_place.py:421:            del scene, robot, ik, gripper, policy
src/franka_wrist_camera_scene/episode/recorder.py:44:    placement_target_category_id: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:45:    placement_target_variant_id: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:46:    placement_target_label: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:47:    placement_target_usd_path: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:48:    placement_target_grasp_strategy: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:49:    placement_target_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/recorder.py:183:            placement_target_category_id=self.placement_target_category_id,
src/franka_wrist_camera_scene/episode/recorder.py:184:            placement_target_variant_id=self.placement_target_variant_id,
src/franka_wrist_camera_scene/episode/recorder.py:185:            placement_target_label=self.placement_target_label,
src/franka_wrist_camera_scene/episode/recorder.py:186:            placement_target_usd_path=self.placement_target_usd_path,
src/franka_wrist_camera_scene/episode/recorder.py:187:            placement_target_grasp_strategy=self.placement_target_grasp_strategy,
src/franka_wrist_camera_scene/episode/recorder.py:188:            placement_target_pos_local=self.placement_target_pos_local,
src/franka_wrist_camera_scene/episode/success.py:13:def receptacle_xy_radius_from_bbox(
src/franka_wrist_camera_scene/episode/success.py:14:    bbox_min: tuple[float, float, float],
src/franka_wrist_camera_scene/episode/success.py:15:    bbox_max: tuple[float, float, float],
src/franka_wrist_camera_scene/episode/success.py:18:    size_x = float(bbox_max[0]) - float(bbox_min[0])
src/franka_wrist_camera_scene/episode/success.py:19:    size_y = float(bbox_max[1]) - float(bbox_min[1])
src/franka_wrist_camera_scene/episode/success.py:48:    if getattr(spec, "goal_type", "target_area") == "receptacle":
src/franka_wrist_camera_scene/episode/success.py:54:    if spec.placement_target_pos_local is not None:
src/franka_wrist_camera_scene/episode/success.py:56:            spec.object_local_bbox_min is None
src/franka_wrist_camera_scene/episode/success.py:57:            or spec.placement_target_local_bbox_min is None
src/franka_wrist_camera_scene/episode/success.py:58:            or spec.placement_target_local_bbox_max is None
src/franka_wrist_camera_scene/episode/success.py:60:            raise RuntimeError("Receptacle placement success requires object and placement target geometry.")
src/franka_wrist_camera_scene/episode/success.py:62:        receptacle_pos_local = torch.tensor(spec.placement_target_pos_local, device=obj_pos_w.device).view(1, 3)
src/franka_wrist_camera_scene/episode/success.py:66:        xy_threshold = receptacle_xy_radius_from_bbox(
src/franka_wrist_camera_scene/episode/success.py:67:            bbox_min=spec.placement_target_local_bbox_min,
src/franka_wrist_camera_scene/episode/success.py:68:            bbox_max=spec.placement_target_local_bbox_max,
src/franka_wrist_camera_scene/episode/success.py:72:        object_bottom_z = obj_pos_w[:, 2] + float(spec.object_local_bbox_min[2])
src/franka_wrist_camera_scene/episode/success.py:73:        receptacle_top_z = receptacle_pos_w[:, 2] + float(spec.placement_target_local_bbox_max[2])
src/franka_wrist_camera_scene/episode/success.py:74:        receptacle_bottom_z = receptacle_pos_w[:, 2] + float(spec.placement_target_local_bbox_min[2])
src/franka_wrist_camera_scene/episode/schema.py:38:    placement_target_category_id: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:39:    placement_target_variant_id: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:40:    placement_target_label: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:41:    placement_target_usd_path: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:42:    placement_target_grasp_strategy: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:43:    placement_target_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/manifest.py:32:    placement_target_category_id: str | None
src/franka_wrist_camera_scene/episode/manifest.py:33:    placement_target_variant_id: str | None
src/franka_wrist_camera_scene/episode/manifest.py:34:    placement_target_label: str | None
src/franka_wrist_camera_scene/episode/manifest.py:35:    placement_target_usd_path: str | None
src/franka_wrist_camera_scene/episode/manifest.py:36:    placement_target_grasp_strategy: str | None
src/franka_wrist_camera_scene/episode/manifest.py:37:    placement_target_pos_local: tuple[float, float, float] | None
src/franka_wrist_camera_scene/episode/manifest.py:107:                placement_target_category_id=meta.get("placement_target_category_id"),
src/franka_wrist_camera_scene/episode/manifest.py:108:                placement_target_variant_id=meta.get("placement_target_variant_id"),
src/franka_wrist_camera_scene/episode/manifest.py:109:                placement_target_label=meta.get("placement_target_label"),
src/franka_wrist_camera_scene/episode/manifest.py:110:                placement_target_usd_path=meta.get("placement_target_usd_path"),
src/franka_wrist_camera_scene/episode/manifest.py:111:                placement_target_grasp_strategy=meta.get("placement_target_grasp_strategy"),
src/franka_wrist_camera_scene/episode/manifest.py:112:                placement_target_pos_local=(
src/franka_wrist_camera_scene/episode/manifest.py:113:                    tuple(meta["placement_target_pos_local"])
src/franka_wrist_camera_scene/episode/manifest.py:114:                    if meta.get("placement_target_pos_local") is not None
src/franka_wrist_camera_scene/scene/clutter.py:14:from franka_wrist_camera_scene.tasks.placement_geometry import object_root_pose_on_support
src/franka_wrist_camera_scene/scene/clutter.py:59:    bbox_min: tuple[float, float, float],
src/franka_wrist_camera_scene/scene/clutter.py:60:    bbox_max: tuple[float, float, float],
src/franka_wrist_camera_scene/scene/clutter.py:66:    size_x = float(bbox_max[0]) - float(bbox_min[0])
src/franka_wrist_camera_scene/scene/clutter.py:67:    size_y = float(bbox_max[1]) - float(bbox_min[1])
src/franka_wrist_camera_scene/scene/clutter.py:70:        raise ValueError(f"Invalid planar bbox size: size_x={size_x}, size_y={size_y}")
src/franka_wrist_camera_scene/scene/clutter.py:169:        bbox_min=context.geometry.local_bbox_min,
src/franka_wrist_camera_scene/scene/clutter.py:170:        bbox_max=context.geometry.local_bbox_max,
src/franka_wrist_camera_scene/scene/clutter.py:190:            geometry_config=clutter_cfg["geometry_config"],
src/franka_wrist_camera_scene/scene/clutter.py:217:    placement_target_context: CatalogObjectContext | None,
src/franka_wrist_camera_scene/scene/clutter.py:218:    placement_target_xy: tuple[float, float] | None,
src/franka_wrist_camera_scene/scene/clutter.py:237:    if placement_target_context is not None and placement_target_xy is not None:
src/franka_wrist_camera_scene/scene/clutter.py:240:                xy=placement_target_xy,
src/franka_wrist_camera_scene/scene/clutter.py:242:                    placement_target_context,
src/franka_wrist_camera_scene/scene/clutter.py:243:                    margin_m=float(clutter_cfg["placement_target_margin_m"]),
src/franka_wrist_camera_scene/scene/clutter.py:247:    elif placement_target_xy is not None:
src/franka_wrist_camera_scene/scene/clutter.py:250:                xy=placement_target_xy,
src/franka_wrist_camera_scene/scene/clutter.py:253:                    margin_m=float(clutter_cfg["placement_target_margin_m"]),
src/franka_wrist_camera_scene/scene/clutter.py:294:            object_bbox_min_z=context.geometry.local_bbox_min[2],
src/franka_wrist_camera_scene/scene/clutter.py:317:    placement_target_context: CatalogObjectContext | None,
src/franka_wrist_camera_scene/scene/clutter.py:318:    placement_target_xy: tuple[float, float] | None,
src/franka_wrist_camera_scene/scene/clutter.py:346:                placement_target_context=placement_target_context,
src/franka_wrist_camera_scene/scene/clutter.py:347:                placement_target_xy=placement_target_xy,
src/franka_wrist_camera_scene/scene/tabletop.py:47:            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.55, 0.42, 0.30)),
src/franka_wrist_camera_scene/scene/tabletop.py:151:    physics_overrides: dict | None = None,
src/franka_wrist_camera_scene/scene/tabletop.py:188:    physics_overrides = physics_overrides or {}
src/franka_wrist_camera_scene/scene/tabletop.py:189:    if "target_mass" in physics_overrides:
src/franka_wrist_camera_scene/scene/tabletop.py:190:        if scene_cfg.target_cube.spawn.mass_props is None:
src/franka_wrist_camera_scene/scene/tabletop.py:191:            scene_cfg.target_cube.spawn.mass_props = sim_utils.schemas.MassPropertiesCfg()
src/franka_wrist_camera_scene/scene/tabletop.py:192:        scene_cfg.target_cube.spawn.mass_props.mass = float(physics_overrides["target_mass"])
src/franka_wrist_camera_scene/scene/tabletop.py:193:    if "target_linear_damping" in physics_overrides:
src/franka_wrist_camera_scene/scene/tabletop.py:194:        scene_cfg.target_cube.spawn.rigid_props.linear_damping = float(physics_overrides["target_linear_damping"])
src/franka_wrist_camera_scene/scene/tabletop.py:195:    if "target_angular_damping" in physics_overrides:
src/franka_wrist_camera_scene/scene/tabletop.py:196:        scene_cfg.target_cube.spawn.rigid_props.angular_damping = float(physics_overrides["target_angular_damping"])
src/franka_wrist_camera_scene/scene/tabletop.py:197:    if "gripper_stiffness" in physics_overrides and "panda_hand" in scene_cfg.robot.actuators:
src/franka_wrist_camera_scene/scene/tabletop.py:198:        scene_cfg.robot.actuators["panda_hand"].stiffness = float(physics_overrides["gripper_stiffness"])
src/franka_wrist_camera_scene/scene/tabletop.py:199:    if "gripper_damping" in physics_overrides and "panda_hand" in scene_cfg.robot.actuators:
src/franka_wrist_camera_scene/scene/tabletop.py:200:        scene_cfg.robot.actuators["panda_hand"].damping = float(physics_overrides["gripper_damping"])
src/franka_wrist_camera_scene/scene/tabletop.py:212:    physics_overrides: dict | None = None,
src/franka_wrist_camera_scene/scene/tabletop.py:262:    physics_overrides = physics_overrides or {}
src/franka_wrist_camera_scene/scene/tabletop.py:263:    if "target_mass" in physics_overrides:
src/franka_wrist_camera_scene/scene/tabletop.py:264:        if scene_cfg.target_cube.spawn.mass_props is None:
src/franka_wrist_camera_scene/scene/tabletop.py:265:            scene_cfg.target_cube.spawn.mass_props = sim_utils.schemas.MassPropertiesCfg()
src/franka_wrist_camera_scene/scene/tabletop.py:266:        scene_cfg.target_cube.spawn.mass_props.mass = float(physics_overrides["target_mass"])
src/franka_wrist_camera_scene/scene/tabletop.py:267:    if "target_linear_damping" in physics_overrides:
src/franka_wrist_camera_scene/scene/tabletop.py:268:        scene_cfg.target_cube.spawn.rigid_props.linear_damping = float(physics_overrides["target_linear_damping"])
src/franka_wrist_camera_scene/scene/tabletop.py:269:    if "target_angular_damping" in physics_overrides:
src/franka_wrist_camera_scene/scene/tabletop.py:270:        scene_cfg.target_cube.spawn.rigid_props.angular_damping = float(physics_overrides["target_angular_damping"])
src/franka_wrist_camera_scene/scene/tabletop.py:271:    if "gripper_stiffness" in physics_overrides and "panda_hand" in scene_cfg.robot.actuators:
src/franka_wrist_camera_scene/scene/tabletop.py:272:        scene_cfg.robot.actuators["panda_hand"].stiffness = float(physics_overrides["gripper_stiffness"])
src/franka_wrist_camera_scene/scene/tabletop.py:273:    if "gripper_damping" in physics_overrides and "panda_hand" in scene_cfg.robot.actuators:
src/franka_wrist_camera_scene/scene/tabletop.py:274:        scene_cfg.robot.actuators["panda_hand"].damping = float(physics_overrides["gripper_damping"])
src/franka_wrist_camera_scene/scene/object_context.py:8:from franka_wrist_camera_scene.objects.geometry_registry import (
src/franka_wrist_camera_scene/scene/object_context.py:11:    get_object_geometry,
src/franka_wrist_camera_scene/scene/object_context.py:12:    load_object_geometry_registry,
src/franka_wrist_camera_scene/scene/object_context.py:14:from franka_wrist_camera_scene.objects.selection import sample_catalog_object, variant_grasp_strategy
src/franka_wrist_camera_scene/scene/object_context.py:24:    geometry: ObjectPlanarGeometry
src/franka_wrist_camera_scene/scene/object_context.py:27:def _validate_geometry_catalog_config(
src/franka_wrist_camera_scene/scene/object_context.py:29:    geometry_config: str,
src/franka_wrist_camera_scene/scene/object_context.py:34:            f"Geometry config {geometry_config} was generated for "
src/franka_wrist_camera_scene/scene/object_context.py:39:def _validate_geometry_usd_path(
src/franka_wrist_camera_scene/scene/object_context.py:42:    geometry: ObjectPlanarGeometry,
src/franka_wrist_camera_scene/scene/object_context.py:46:    if geometry.usd_path != catalog_relative_usd_path:
src/franka_wrist_camera_scene/scene/object_context.py:50:            f"geometry={geometry.usd_path}"
src/franka_wrist_camera_scene/scene/object_context.py:56:    geometry_config: str,
src/franka_wrist_camera_scene/scene/object_context.py:66:    geometry_registry = load_object_geometry_registry(geometry_config)
src/franka_wrist_camera_scene/scene/object_context.py:67:    _validate_geometry_catalog_config(
src/franka_wrist_camera_scene/scene/object_context.py:68:        registry=geometry_registry,
src/franka_wrist_camera_scene/scene/object_context.py:69:        geometry_config=geometry_config,
src/franka_wrist_camera_scene/scene/object_context.py:82:    geometry = get_object_geometry(
src/franka_wrist_camera_scene/scene/object_context.py:83:        registry=geometry_registry,
src/franka_wrist_camera_scene/scene/object_context.py:87:    _validate_geometry_usd_path(
src/franka_wrist_camera_scene/scene/object_context.py:90:        geometry=geometry,
src/franka_wrist_camera_scene/scene/object_context.py:100:        geometry=geometry,
src/franka_wrist_camera_scene/settings.py:20:# WXYZ quaternion used by Isaac Lab to orient the gripper toward the table.
src/franka_wrist_camera_scene/debug/visualization.py:31:                        visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.0, 0.65, 1.0)),
src/franka_wrist_camera_scene/debug/visualization.py:42:                        visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 0.55, 0.0)),
src/franka_wrist_camera_scene/policies/reaching_scripted.py:68:        finger_opening = self.spec.open_finger_m
src/franka_wrist_camera_scene/policies/circle_policy.py:16:    def __init__(self, cfg: CircleTrajectoryCfg, gripper_width: float = 0.035):
src/franka_wrist_camera_scene/policies/circle_policy.py:18:        self.gripper_width = gripper_width
src/franka_wrist_camera_scene/policies/circle_policy.py:28:        """Compute the next target end-effector pose and gripper width."""
src/franka_wrist_camera_scene/policies/circle_policy.py:36:            finger_opening_m=self.gripper_width,
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:10:from ..control.grasp_orientation import downward_gripper_quat_for_closing_axis
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:12:from ..tasks.placement_geometry import object_root_z_on_support
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:37:        if self.spec.object_local_bbox_min is None:
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:38:            raise RuntimeError("Pick-place requires object bbox metadata for placement height.")
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:43:            object_bbox_min_z=float(self.spec.object_local_bbox_min[2]),
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:50:            self.spec.object_local_bbox_min is None
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:51:            or self.spec.placement_target_local_bbox_min is None
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:53:            raise RuntimeError("Receptacle placement requires object and placement target geometry.")
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:56:        receptacle_bottom_z = receptacle_root_w[:, 2] + float(self.spec.placement_target_local_bbox_min[2])
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:59:            - float(self.spec.object_local_bbox_min[2])
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:65:        if self.spec.object_local_bbox_min is None or self.spec.object_local_bbox_max is None:
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:66:            raise RuntimeError("Pick-place requires object bbox metadata for top grasp targeting.")
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:68:        bbox_max_z = float(self.spec.object_local_bbox_max[2])
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:71:        grasp_tcp[:, 2] = obj_pos_w[:, 2] + bbox_max_z - self.spec.top_grasp_depth_m
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:90:            self.quat_wxyz = downward_gripper_quat_for_closing_axis(
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:142:            if self.spec.placement_target_pos_local is None:
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:145:                receptacle_local = torch.tensor(self.spec.placement_target_pos_local, device=self._device)
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:165:        finger_opening = self.spec.open_finger_m
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:223:            finger_opening = self.spec.open_finger_m
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:229:            finger_opening = self.spec.open_finger_m
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:246:            finger_opening = self.spec.open_finger_m
src/franka_wrist_camera_scene/tasks/reaching.py:22:    open_finger_m: float = 0.04
src/franka_wrist_camera_scene/tasks/reaching.py:51:        open_finger_m=base_spec.open_finger_m,
src/franka_wrist_camera_scene/tasks/placement_geometry.py:8:    object_bbox_min_z: float,
src/franka_wrist_camera_scene/tasks/placement_geometry.py:11:    return support_surface_z - object_bbox_min_z + bottom_clearance_m
src/franka_wrist_camera_scene/tasks/placement_geometry.py:17:    object_bbox_min_z: float,
src/franka_wrist_camera_scene/tasks/placement_geometry.py:25:            object_bbox_min_z=object_bbox_min_z,
src/franka_wrist_camera_scene/tasks/pick_place.py:7:from .placement_geometry import object_root_pose_on_support, object_root_z_on_support
src/franka_wrist_camera_scene/tasks/pick_place.py:17:    goal_type: str = "target_area"
src/franka_wrist_camera_scene/tasks/pick_place.py:18:    success_metric: str = "target_area_center"
src/franka_wrist_camera_scene/tasks/pick_place.py:34:    object_local_bbox_min: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:35:    object_local_bbox_max: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:36:    placement_target_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:37:    placement_target_local_bbox_min: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:38:    placement_target_local_bbox_max: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:49:    open_finger_m: float = 0.04
src/franka_wrist_camera_scene/tasks/pick_place.py:74:    object_local_bbox_min: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:75:    object_local_bbox_max: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:76:    placement_target_pos_local: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:77:    placement_target_local_bbox_min: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:78:    placement_target_local_bbox_max: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:81:    resolved_bbox_min = (
src/franka_wrist_camera_scene/tasks/pick_place.py:82:        object_local_bbox_min
src/franka_wrist_camera_scene/tasks/pick_place.py:83:        if object_local_bbox_min is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:84:        else base_spec.object_local_bbox_min
src/franka_wrist_camera_scene/tasks/pick_place.py:86:    resolved_bbox_max = (
src/franka_wrist_camera_scene/tasks/pick_place.py:87:        object_local_bbox_max
src/franka_wrist_camera_scene/tasks/pick_place.py:88:        if object_local_bbox_max is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:89:        else base_spec.object_local_bbox_max
src/franka_wrist_camera_scene/tasks/pick_place.py:91:    if resolved_bbox_min is None or resolved_bbox_max is None:
src/franka_wrist_camera_scene/tasks/pick_place.py:92:        raise ValueError("Pick-place episode specs require object bbox metadata.")
src/franka_wrist_camera_scene/tasks/pick_place.py:94:    resolved_placement_bbox_min = (
src/franka_wrist_camera_scene/tasks/pick_place.py:95:        placement_target_local_bbox_min
src/franka_wrist_camera_scene/tasks/pick_place.py:96:        if placement_target_local_bbox_min is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:97:        else base_spec.placement_target_local_bbox_min
src/franka_wrist_camera_scene/tasks/pick_place.py:99:    resolved_placement_bbox_max = (
src/franka_wrist_camera_scene/tasks/pick_place.py:100:        placement_target_local_bbox_max
src/franka_wrist_camera_scene/tasks/pick_place.py:101:        if placement_target_local_bbox_max is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:102:        else base_spec.placement_target_local_bbox_max
src/franka_wrist_camera_scene/tasks/pick_place.py:105:        placement_target_pos_local
src/franka_wrist_camera_scene/tasks/pick_place.py:106:        if placement_target_pos_local is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:107:        else base_spec.placement_target_pos_local
src/franka_wrist_camera_scene/tasks/pick_place.py:111:        or resolved_placement_bbox_min is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:112:        or resolved_placement_bbox_max is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:117:        or resolved_placement_bbox_min is None
src/franka_wrist_camera_scene/tasks/pick_place.py:118:        or resolved_placement_bbox_max is None
src/franka_wrist_camera_scene/tasks/pick_place.py:122:            "Receptacle pick-place episode specs require placement target pose, bbox metadata, and label."
src/franka_wrist_camera_scene/tasks/pick_place.py:136:        object_bbox_min_z=resolved_bbox_min[2],
src/franka_wrist_camera_scene/tasks/pick_place.py:143:            object_bbox_min_z=resolved_bbox_min[2],
src/franka_wrist_camera_scene/tasks/pick_place.py:153:                object_bbox_min_z=resolved_bbox_min[2],
src/franka_wrist_camera_scene/tasks/pick_place.py:177:        object_local_bbox_min=resolved_bbox_min,
src/franka_wrist_camera_scene/tasks/pick_place.py:178:        object_local_bbox_max=resolved_bbox_max,
src/franka_wrist_camera_scene/tasks/pick_place.py:179:        placement_target_pos_local=resolved_placement_pos,
src/franka_wrist_camera_scene/tasks/pick_place.py:180:        placement_target_local_bbox_min=resolved_placement_bbox_min,
src/franka_wrist_camera_scene/tasks/pick_place.py:181:        placement_target_local_bbox_max=resolved_placement_bbox_max,
src/franka_wrist_camera_scene/export/ila.py:71:        "placement_target_category_id": meta.get("placement_target_category_id"),
src/franka_wrist_camera_scene/export/ila.py:72:        "placement_target_variant_id": meta.get("placement_target_variant_id"),
src/franka_wrist_camera_scene/export/ila.py:73:        "placement_target_label": meta.get("placement_target_label"),
src/franka_wrist_camera_scene/export/ila.py:74:        "placement_target_usd_path": meta.get("placement_target_usd_path"),
src/franka_wrist_camera_scene/export/ila.py:75:        "placement_target_grasp_strategy": meta.get("placement_target_grasp_strategy"),
src/franka_wrist_camera_scene/export/ila.py:76:        "placement_target_pos_local": meta.get("placement_target_pos_local"),
src/franka_wrist_camera_scene/export/ila.py:105:        "action_space": "relative_cartesian_target_plus_gripper",
src/franka_wrist_camera_scene/control/gripper.py:11:    """Robot gripper controller for setting parallel finger widths."""
src/franka_wrist_camera_scene/control/gripper.py:27:        """Set target gripper width."""
src/franka_wrist_camera_scene/control/grasp_orientation.py:42:def downward_gripper_quat_for_closing_axis(
src/franka_wrist_camera_scene/control/grasp_orientation.py:46:    """Return downward gripper orientation with jaws closing along a planar axis."""
src/franka_wrist_camera_scene/control/__init__.py:1:"""Robot control interfaces, IK solver, gripper commands, and motion primitives."""
scripts/inspect_target_sampling.py:14:from franka_wrist_camera_scene.objects.geometry_registry import (
scripts/inspect_target_sampling.py:15:    get_object_geometry,
scripts/inspect_target_sampling.py:16:    load_object_geometry_registry,
scripts/inspect_target_sampling.py:18:from franka_wrist_camera_scene.objects.selection import (
scripts/inspect_target_sampling.py:32:        choices=("target_object", "placement_target", "clutter"),
scripts/inspect_target_sampling.py:44:    geometry_config = str(sampling_cfg["geometry_config"])
scripts/inspect_target_sampling.py:46:    geometry_registry = load_object_geometry_registry(geometry_config)
scripts/inspect_target_sampling.py:47:    if geometry_registry.catalog_config != catalog_config:
scripts/inspect_target_sampling.py:49:            f"Geometry config {geometry_config} was generated for "
scripts/inspect_target_sampling.py:50:            f"{geometry_registry.catalog_config}, not {catalog_config}."
scripts/inspect_target_sampling.py:98:            geometry = get_object_geometry(geometry_registry, category.id, variant.id)
scripts/inspect_target_sampling.py:100:            if geometry.usd_path != usd_path:
scripts/inspect_target_sampling.py:103:                    f"catalog={usd_path}, geometry={geometry.usd_path}"
scripts/inspect_target_sampling.py:105:            if args.only_yaw_relevant and not geometry.yaw_relevant:
scripts/inspect_target_sampling.py:114:                f"{str(geometry.yaw_relevant).lower():<6} "
scripts/inspect_target_sampling.py:115:                f"{geometry.planar_aspect_ratio:<8.3f} "
scripts/inspect_collection.py:53:        "placement_target_category_id": meta.get("placement_target_category_id"),
scripts/inspect_collection.py:54:        "placement_target_variant_id": meta.get("placement_target_variant_id"),
scripts/inspect_collection.py:55:        "placement_target_label": meta.get("placement_target_label"),
scripts/inspect_collection.py:56:        "placement_target_usd_path": meta.get("placement_target_usd_path"),
scripts/inspect_collection.py:57:        "placement_target_grasp_strategy": meta.get("placement_target_grasp_strategy"),
scripts/inspect_collection.py:58:        "placement_target_pos_local": (
scripts/inspect_collection.py:59:            tuple(meta["placement_target_pos_local"])
scripts/inspect_collection.py:60:            if meta.get("placement_target_pos_local") is not None
scripts/inspect_collection.py:105:        f"{'grasp_axis':<20} {'light':<24} {'clutter':<40}"
scripts/inspect_collection.py:113:        placement_variant_id = item.get("placement_target_variant_id", "none") or "none"
scripts/inspect_collection.py:114:        placement_label = item.get("placement_target_label", "none") or "none"
scripts/inspect_collection.py:125:        grasp_axis = item["grasp_closing_axis_xy"]
scripts/inspect_collection.py:126:        grasp_axis_str = str(grasp_axis) if grasp_axis is not None else "none"
scripts/inspect_collection.py:134:            f"{minor_axis_str:<20} {grasp_axis_str:<20} {light_str:<24} {clutter_summary:<40}"
scripts/inspect_collection.py:142:    placement_target_pos_local = summary["placement_target_pos_local"]
scripts/inspect_collection.py:147:            tuple(round(float(x), 4) for x in placement_target_pos_local)
scripts/inspect_collection.py:148:            if placement_target_pos_local is not None
scripts/collect.py:41:def preflight_collection_output(collection_cfg: dict) -> None:
scripts/collect.py:62:    preflight_collection_output(collection_cfg)
scripts/generate_object_geometry.py:2:"""Generate planar geometry metadata for USD catalog objects."""
scripts/generate_object_geometry.py:19:    parser = argparse.ArgumentParser(description="Generate USD object planar geometry metadata.")
scripts/generate_object_geometry.py:29:        default=REPO_ROOT / "configs" / "object_geometry.generated.yaml",
scripts/generate_object_geometry.py:30:        help="Output geometry YAML path.",
scripts/generate_object_geometry.py:48:    from franka_wrist_camera_scene.objects.geometry import write_object_geometry
scripts/generate_object_geometry.py:50:    output_path = write_object_geometry(
scripts/generate_object_geometry.py:55:    print(f"[INFO] Saved object geometry metadata to: {output_path}", flush=True)
scripts/inspect_object_geometry.py:2:"""Inspect generated USD object planar geometry metadata."""
scripts/inspect_object_geometry.py:19:    parser = argparse.ArgumentParser(description="Inspect generated object geometry metadata.")
scripts/inspect_object_geometry.py:21:        "--geometry-config",
scripts/inspect_object_geometry.py:23:        default=REPO_ROOT / "configs" / "object_geometry.generated.yaml",
scripts/inspect_object_geometry.py:30:    data = yaml.safe_load(args.geometry_config.read_text(encoding="utf-8"))
scripts/inspect_object_geometry.py:35:    print(f"geometry_config: {args.geometry_config}")
scripts/visualize_ila_episode.py:44:        gripper = episode["action_finger_opening_m"]
scripts/visualize_ila_episode.py:70:        gripper_ax = fig.add_subplot(grid[3, :])
scripts/visualize_ila_episode.py:71:        gripper_ax.plot(timestamps, gripper)
scripts/visualize_ila_episode.py:72:        gripper_ax.set_ylabel("gripper opening [m]")
scripts/visualize_ila_episode.py:73:        gripper_ax.set_xlabel("time [s]")
scripts/debug_scene.py:67:from franka_wrist_camera_scene.control.gripper import GripperController
scripts/debug_scene.py:79:from franka_wrist_camera_scene.tasks.placement_geometry import object_root_pose_on_support
scripts/debug_scene.py:101:    gripper: GripperController,
scripts/debug_scene.py:137:        # 3. Update and apply gripper command
scripts/debug_scene.py:138:        gripper.set_width(cmd.finger_opening_m)
scripts/debug_scene.py:139:        gripper.apply(robot)
scripts/debug_scene.py:197:        geometry_config=target_object_cfg["geometry_config"],
scripts/debug_scene.py:235:        placement_target_cfg = collection_cfg["placement_target"]
scripts/debug_scene.py:238:            catalog_config=placement_target_cfg["catalog_config"],
scripts/debug_scene.py:239:            geometry_config=placement_target_cfg["geometry_config"],
scripts/debug_scene.py:240:            category_id=placement_target_cfg["category_id"],
scripts/debug_scene.py:241:            variant_id=placement_target_cfg["variant_id"],
scripts/debug_scene.py:242:            split=placement_target_cfg["split"],
scripts/debug_scene.py:243:            role=placement_target_cfg["role"],
scripts/debug_scene.py:244:            required_affordances=tuple(placement_target_cfg["required_affordances"]),
scripts/debug_scene.py:245:            required_grasp_strategy=placement_target_cfg["required_grasp_strategy"],
scripts/debug_scene.py:252:            object_bbox_min_z=placement_context.geometry.local_bbox_min[2],
scripts/debug_scene.py:256:            object_context.geometry.planar_minor_axis_local
scripts/debug_scene.py:257:            if object_context.geometry.yaw_relevant
scripts/debug_scene.py:266:            object_local_bbox_min=object_context.geometry.local_bbox_min,
scripts/debug_scene.py:267:            object_local_bbox_max=object_context.geometry.local_bbox_max,
scripts/debug_scene.py:268:            placement_target_pos_local=placement_receptacle_pos_local,
scripts/debug_scene.py:269:            placement_target_local_bbox_min=placement_context.geometry.local_bbox_min,
scripts/debug_scene.py:270:            placement_target_local_bbox_max=placement_context.geometry.local_bbox_max,
scripts/debug_scene.py:281:            placement_target_context=placement_context,
scripts/debug_scene.py:282:            placement_target_xy=(
scripts/debug_scene.py:301:    gripper = GripperController()
scripts/debug_scene.py:307:    gripper.bind(scene, robot)
scripts/debug_scene.py:323:        gripper,
configs/object_tests/fcan03_mass020_stiff150.yaml:1:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150
configs/object_tests/fcan03_mass020_stiff150.yaml:18:physics_overrides:
configs/object_tests/fcan03_mass020_stiff150.yaml:19:  target_mass: 0.20
configs/object_tests/fcan03_mass020_stiff150.yaml:20:  gripper_stiffness: 150.0
configs/object_tests/fcan03_mass020_stiff150.yaml:21:  gripper_damping: 15.0
configs/fcan03_diagnosis/fcan03_diag_A_default.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_A_default.yaml:25:placement_target:
configs/fcan03_diagnosis/fcan03_diag_A_default.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_D_mass_override.yaml:2:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_diag_D_mass_override
configs/fcan03_diagnosis/fcan03_diag_D_mass_override.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_D_mass_override.yaml:25:placement_target:
configs/fcan03_diagnosis/fcan03_diag_D_mass_override.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_D_mass_override.yaml:35:physics_overrides:
configs/fcan03_diagnosis/fcan03_diag_D_mass_override.yaml:36:  target_mass: 0.15
configs/fcan03_diagnosis/fcan03_diag_B_deeper_grasp.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_B_deeper_grasp.yaml:25:placement_target:
configs/fcan03_diagnosis/fcan03_diag_B_deeper_grasp.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_C_moderate_depth.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/fcan03_diagnosis/fcan03_diag_C_moderate_depth.yaml:25:placement_target:
configs/fcan03_diagnosis/fcan03_diag_C_moderate_depth.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/upstream_sampled_receptacle_smoke.yaml:16:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/upstream_sampled_receptacle_smoke.yaml:24:placement_target:
configs/local_isaac45/upstream_sampled_receptacle_smoke.yaml:26:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/baseline_reachable_apple_integrated.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/fcan03_mass020_integrated.yaml:2:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_integrated
configs/local_isaac45/fcan03_mass020_integrated.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/fcan03_mass020_integrated.yaml:25:physics_overrides:
configs/local_isaac45/fcan03_mass020_integrated.yaml:26:  target_mass: 0.20
configs/local_isaac45/fcan03_mass020_integrated.yaml:27:  gripper_stiffness: 150.0
configs/local_isaac45/fcan03_mass020_integrated.yaml:28:  gripper_damping: 15.0
configs/local_isaac45/receptacle_tray_tray04_apple01_integrated.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/receptacle_tray_tray04_apple01_integrated.yaml:25:placement_target:
configs/local_isaac45/receptacle_tray_tray04_apple01_integrated.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/cup05_integrated.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/upstream_clutter_smoke.yaml:16:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/upstream_clutter_smoke.yaml:24:placement_target:
configs/local_isaac45/upstream_clutter_smoke.yaml:26:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/upstream_clutter_smoke.yaml:36:  geometry_config: object_geometry.generated.yaml
configs/local_isaac45/upstream_clutter_smoke.yaml:46:  placement_target_margin_m: 0.035
configs/collection_reaching_smoke.yaml:16:  geometry_config: object_geometry.generated.yaml
configs/accepted_object_tests/complex_plate_plate00_mass020_stiff150.yaml:1:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_mass020_stiff150
configs/accepted_object_tests/complex_plate_plate00_mass020_stiff150.yaml:18:physics_overrides:
configs/accepted_object_tests/complex_plate_plate00_mass020_stiff150.yaml:19:  target_mass: 0.2
configs/accepted_object_tests/complex_plate_plate00_mass020_stiff150.yaml:20:  gripper_stiffness: 150.0
configs/accepted_object_tests/complex_plate_plate00_mass020_stiff150.yaml:21:  gripper_damping: 15.0
configs/accepted_object_tests/fcan03_mass020_stiff150.yaml:1:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150
configs/accepted_object_tests/fcan03_mass020_stiff150.yaml:18:physics_overrides:
configs/accepted_object_tests/fcan03_mass020_stiff150.yaml:19:  target_mass: 0.20
configs/accepted_object_tests/fcan03_mass020_stiff150.yaml:20:  gripper_stiffness: 150.0
configs/accepted_object_tests/fcan03_mass020_stiff150.yaml:21:  gripper_damping: 15.0
configs/accepted_object_tests/complex_bowl_bowl01_mass020_stiff150.yaml:1:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_mass020_stiff150
configs/accepted_object_tests/complex_bowl_bowl01_mass020_stiff150.yaml:18:physics_overrides:
configs/accepted_object_tests/complex_bowl_bowl01_mass020_stiff150.yaml:19:  target_mass: 0.2
configs/accepted_object_tests/complex_bowl_bowl01_mass020_stiff150.yaml:20:  gripper_stiffness: 150.0
configs/accepted_object_tests/complex_bowl_bowl01_mass020_stiff150.yaml:21:  gripper_damping: 15.0
configs/diversity_validation/pair2_avocado_bowl.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair2_avocado_bowl.yaml:25:placement_target:
configs/diversity_validation/pair2_avocado_bowl.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair1_apple_bowl.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair1_apple_bowl.yaml:25:placement_target:
configs/diversity_validation/pair1_apple_bowl.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair6_beer_box.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair6_beer_box.yaml:25:placement_target:
configs/diversity_validation/pair6_beer_box.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair5_kiwi_bowl.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair5_kiwi_bowl.yaml:25:placement_target:
configs/diversity_validation/pair5_kiwi_bowl.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair4_box_bowl.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair4_box_bowl.yaml:25:placement_target:
configs/diversity_validation/pair4_box_bowl.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair3_can_tray.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair3_can_tray.yaml:25:placement_target:
configs/diversity_validation/pair3_can_tray.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/diversity_validation/pair3_can_tray.yaml:35:physics_overrides:
configs/diversity_validation/pair3_can_tray.yaml:36:  target_mass: 0.15
configs/diversity_validation/pair3_can_tray.yaml:37:  gripper_stiffness: 150.0
configs/diversity_validation/pair3_can_tray.yaml:38:  gripper_damping: 15.0
configs/final_readiness_validation/fcan03_verification_seed602.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed602.yaml:25:placement_target:
configs/final_readiness_validation/fcan03_verification_seed602.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed602.yaml:35:physics_overrides:
configs/final_readiness_validation/fcan03_verification_seed602.yaml:36:  target_mass: 0.15
configs/final_readiness_validation/fcan03_verification_seed602.yaml:37:  gripper_stiffness: 150.0
configs/final_readiness_validation/fcan03_verification_seed602.yaml:38:  gripper_damping: 15.0
configs/final_readiness_validation/fcan03_verification_seed604.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed604.yaml:25:placement_target:
configs/final_readiness_validation/fcan03_verification_seed604.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed604.yaml:35:physics_overrides:
configs/final_readiness_validation/fcan03_verification_seed604.yaml:36:  target_mass: 0.15
configs/final_readiness_validation/fcan03_verification_seed604.yaml:37:  gripper_stiffness: 150.0
configs/final_readiness_validation/fcan03_verification_seed604.yaml:38:  gripper_damping: 15.0
configs/final_readiness_validation/hard_05_potato00_into_bowl10_seed705.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_05_potato00_into_bowl10_seed705.yaml:25:placement_target:
configs/final_readiness_validation/hard_05_potato00_into_bowl10_seed705.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_02_lime_box_seed802.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_02_lime_box_seed802.yaml:25:placement_target:
configs/final_readiness_validation/clutter_02_lime_box_seed802.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_02_lime_box_seed802.yaml:37:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_02_lime_box_seed802.yaml:47:  placement_target_margin_m: 0.035
configs/final_readiness_validation/clutter_01_avocado_bowl_seed801.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_01_avocado_bowl_seed801.yaml:25:placement_target:
configs/final_readiness_validation/clutter_01_avocado_bowl_seed801.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_01_avocado_bowl_seed801.yaml:37:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_01_avocado_bowl_seed801.yaml:47:  placement_target_margin_m: 0.035
configs/final_readiness_validation/hard_06_wbottle01_into_bowl07_seed706.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_06_wbottle01_into_bowl07_seed706.yaml:25:placement_target:
configs/final_readiness_validation/hard_06_wbottle01_into_bowl07_seed706.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed605.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed605.yaml:25:placement_target:
configs/final_readiness_validation/fcan03_verification_seed605.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed605.yaml:35:physics_overrides:
configs/final_readiness_validation/fcan03_verification_seed605.yaml:36:  target_mass: 0.15
configs/final_readiness_validation/fcan03_verification_seed605.yaml:37:  gripper_stiffness: 150.0
configs/final_readiness_validation/fcan03_verification_seed605.yaml:38:  gripper_damping: 15.0
configs/final_readiness_validation/hard_01_beer00_into_bowl01_seed701.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_01_beer00_into_bowl01_seed701.yaml:25:placement_target:
configs/final_readiness_validation/hard_01_beer00_into_bowl01_seed701.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed601.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed601.yaml:25:placement_target:
configs/final_readiness_validation/fcan03_verification_seed601.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed601.yaml:35:physics_overrides:
configs/final_readiness_validation/fcan03_verification_seed601.yaml:36:  target_mass: 0.15
configs/final_readiness_validation/fcan03_verification_seed601.yaml:37:  gripper_stiffness: 150.0
configs/final_readiness_validation/fcan03_verification_seed601.yaml:38:  gripper_damping: 15.0
configs/final_readiness_validation/hard_04_egg03_into_box00_seed704.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_04_egg03_into_box00_seed704.yaml:25:placement_target:
configs/final_readiness_validation/hard_04_egg03_into_box00_seed704.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed603.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed603.yaml:25:placement_target:
configs/final_readiness_validation/fcan03_verification_seed603.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/fcan03_verification_seed603.yaml:35:physics_overrides:
configs/final_readiness_validation/fcan03_verification_seed603.yaml:36:  target_mass: 0.15
configs/final_readiness_validation/fcan03_verification_seed603.yaml:37:  gripper_stiffness: 150.0
configs/final_readiness_validation/fcan03_verification_seed603.yaml:38:  gripper_damping: 15.0
configs/final_readiness_validation/clutter_01_avocado_bowl_3episodes.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_01_avocado_bowl_3episodes.yaml:25:placement_target:
configs/final_readiness_validation/clutter_01_avocado_bowl_3episodes.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_01_avocado_bowl_3episodes.yaml:37:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/clutter_01_avocado_bowl_3episodes.yaml:47:  placement_target_margin_m: 0.035
configs/final_readiness_validation/hard_02_box01_into_bowl08_seed702.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_02_box01_into_bowl08_seed702.yaml:25:placement_target:
configs/final_readiness_validation/hard_02_box01_into_bowl08_seed702.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_03_tangerine06_into_tray04_seed703.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/hard_03_tangerine06_into_tray04_seed703.yaml:25:placement_target:
configs/final_readiness_validation/hard_03_tangerine06_into_tray04_seed703.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/final_readiness_validation/apple_regression_final.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_11_kiwi00_into_bowl10_seed302.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_11_kiwi00_into_bowl10_seed302.yaml:25:placement_target:
configs/robustness_validation/robust_11_kiwi00_into_bowl10_seed302.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_apple_bowl.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_apple_bowl.yaml:25:placement_target:
configs/robustness_validation/clutter_apple_bowl.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_apple_bowl.yaml:37:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_apple_bowl.yaml:47:  placement_target_margin_m: 0.035
configs/robustness_validation/robust_09_onion00_into_bowl07_seed303.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_09_onion00_into_bowl07_seed303.yaml:25:placement_target:
configs/robustness_validation/robust_09_onion00_into_bowl07_seed303.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_14_lime00_into_box00_seed302.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_14_lime00_into_box00_seed302.yaml:25:placement_target:
configs/robustness_validation/robust_14_lime00_into_box00_seed302.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_12_kiwi00_into_bowl10_seed303.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_12_kiwi00_into_bowl10_seed303.yaml:25:placement_target:
configs/robustness_validation/robust_12_kiwi00_into_bowl10_seed303.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_03_apple01_into_bowl08_seed303.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_03_apple01_into_bowl08_seed303.yaml:25:placement_target:
configs/robustness_validation/robust_03_apple01_into_bowl08_seed303.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_05_avocado02_into_bowl01_seed302.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_05_avocado02_into_bowl01_seed302.yaml:25:placement_target:
configs/robustness_validation/robust_05_avocado02_into_bowl01_seed302.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_06_avocado02_into_bowl01_seed303.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_06_avocado02_into_bowl01_seed303.yaml:25:placement_target:
configs/robustness_validation/robust_06_avocado02_into_bowl01_seed303.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_10_kiwi00_into_bowl10_seed301.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_10_kiwi00_into_bowl10_seed301.yaml:25:placement_target:
configs/robustness_validation/robust_10_kiwi00_into_bowl10_seed301.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_08_onion00_into_bowl07_seed302.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_08_onion00_into_bowl07_seed302.yaml:25:placement_target:
configs/robustness_validation/robust_08_onion00_into_bowl07_seed302.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_13_lime00_into_box00_seed301.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_13_lime00_into_box00_seed301.yaml:25:placement_target:
configs/robustness_validation/robust_13_lime00_into_box00_seed301.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_15_lime00_into_box00_seed303.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_15_lime00_into_box00_seed303.yaml:25:placement_target:
configs/robustness_validation/robust_15_lime00_into_box00_seed303.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_lime_box.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_lime_box.yaml:25:placement_target:
configs/robustness_validation/clutter_lime_box.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_lime_box.yaml:37:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/clutter_lime_box.yaml:47:  placement_target_margin_m: 0.035
configs/robustness_validation/robust_04_avocado02_into_bowl01_seed301.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_04_avocado02_into_bowl01_seed301.yaml:25:placement_target:
configs/robustness_validation/robust_04_avocado02_into_bowl01_seed301.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_07_onion00_into_bowl07_seed301.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_07_onion00_into_bowl07_seed301.yaml:25:placement_target:
configs/robustness_validation/robust_07_onion00_into_bowl07_seed301.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_01_apple01_into_bowl08_seed301.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_01_apple01_into_bowl08_seed301.yaml:25:placement_target:
configs/robustness_validation/robust_01_apple01_into_bowl08_seed301.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/apple_regression_final.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_02_apple01_into_bowl08_seed302.yaml:17:  geometry_config: object_geometry.generated.yaml
configs/robustness_validation/robust_02_apple01_into_bowl08_seed302.yaml:25:placement_target:
configs/robustness_validation/robust_02_apple01_into_bowl08_seed302.yaml:27:  geometry_config: object_geometry.generated.yaml
configs/object_geometry.generated.yaml:8:  local_bbox_min:
configs/object_geometry.generated.yaml:12:  local_bbox_max:
configs/object_geometry.generated.yaml:16:  local_bbox_size:
configs/object_geometry.generated.yaml:32:  local_bbox_min:
configs/object_geometry.generated.yaml:36:  local_bbox_max:
configs/object_geometry.generated.yaml:40:  local_bbox_size:
configs/object_geometry.generated.yaml:56:  local_bbox_min:
configs/object_geometry.generated.yaml:60:  local_bbox_max:
configs/object_geometry.generated.yaml:64:  local_bbox_size:
configs/object_geometry.generated.yaml:80:  local_bbox_min:
configs/object_geometry.generated.yaml:84:  local_bbox_max:
configs/object_geometry.generated.yaml:88:  local_bbox_size:
configs/object_geometry.generated.yaml:104:  local_bbox_min:
configs/object_geometry.generated.yaml:108:  local_bbox_max:
configs/object_geometry.generated.yaml:112:  local_bbox_size:
configs/object_geometry.generated.yaml:128:  local_bbox_min:
configs/object_geometry.generated.yaml:132:  local_bbox_max:
configs/object_geometry.generated.yaml:136:  local_bbox_size:
configs/object_geometry.generated.yaml:152:  local_bbox_min:
configs/object_geometry.generated.yaml:156:  local_bbox_max:
configs/object_geometry.generated.yaml:160:  local_bbox_size:
configs/object_geometry.generated.yaml:176:  local_bbox_min:
configs/object_geometry.generated.yaml:180:  local_bbox_max:
configs/object_geometry.generated.yaml:184:  local_bbox_size:
configs/object_geometry.generated.yaml:200:  local_bbox_min:
configs/object_geometry.generated.yaml:204:  local_bbox_max:
configs/object_geometry.generated.yaml:208:  local_bbox_size:
configs/object_geometry.generated.yaml:224:  local_bbox_min:
configs/object_geometry.generated.yaml:228:  local_bbox_max:
configs/object_geometry.generated.yaml:232:  local_bbox_size:
configs/object_geometry.generated.yaml:248:  local_bbox_min:
configs/object_geometry.generated.yaml:252:  local_bbox_max:
configs/object_geometry.generated.yaml:256:  local_bbox_size:
configs/object_geometry.generated.yaml:272:  local_bbox_min:
configs/object_geometry.generated.yaml:276:  local_bbox_max:
configs/object_geometry.generated.yaml:280:  local_bbox_size:
configs/object_geometry.generated.yaml:296:  local_bbox_min:
configs/object_geometry.generated.yaml:300:  local_bbox_max:
configs/object_geometry.generated.yaml:304:  local_bbox_size:
configs/object_geometry.generated.yaml:320:  local_bbox_min:
configs/object_geometry.generated.yaml:324:  local_bbox_max:
configs/object_geometry.generated.yaml:328:  local_bbox_size:
configs/object_geometry.generated.yaml:344:  local_bbox_min:
configs/object_geometry.generated.yaml:348:  local_bbox_max:
configs/object_geometry.generated.yaml:352:  local_bbox_size:
configs/object_geometry.generated.yaml:368:  local_bbox_min:
configs/object_geometry.generated.yaml:372:  local_bbox_max:
configs/object_geometry.generated.yaml:376:  local_bbox_size:
configs/object_geometry.generated.yaml:392:  local_bbox_min:
configs/object_geometry.generated.yaml:396:  local_bbox_max:
configs/object_geometry.generated.yaml:400:  local_bbox_size:
configs/object_geometry.generated.yaml:416:  local_bbox_min:
configs/object_geometry.generated.yaml:420:  local_bbox_max:
configs/object_geometry.generated.yaml:424:  local_bbox_size:
configs/object_geometry.generated.yaml:440:  local_bbox_min:
configs/object_geometry.generated.yaml:444:  local_bbox_max:
configs/object_geometry.generated.yaml:448:  local_bbox_size:
configs/object_geometry.generated.yaml:464:  local_bbox_min:
configs/object_geometry.generated.yaml:468:  local_bbox_max:
configs/object_geometry.generated.yaml:472:  local_bbox_size:
configs/object_geometry.generated.yaml:488:  local_bbox_min:
configs/object_geometry.generated.yaml:492:  local_bbox_max:
configs/object_geometry.generated.yaml:496:  local_bbox_size:
configs/object_geometry.generated.yaml:512:  local_bbox_min:
configs/object_geometry.generated.yaml:516:  local_bbox_max:
configs/object_geometry.generated.yaml:520:  local_bbox_size:
configs/object_geometry.generated.yaml:536:  local_bbox_min:
configs/object_geometry.generated.yaml:540:  local_bbox_max:
configs/object_geometry.generated.yaml:544:  local_bbox_size:
configs/object_geometry.generated.yaml:560:  local_bbox_min:
configs/object_geometry.generated.yaml:564:  local_bbox_max:
configs/object_geometry.generated.yaml:568:  local_bbox_size:
configs/object_geometry.generated.yaml:584:  local_bbox_min:
configs/object_geometry.generated.yaml:588:  local_bbox_max:
configs/object_geometry.generated.yaml:592:  local_bbox_size:
configs/object_geometry.generated.yaml:608:  local_bbox_min:
configs/object_geometry.generated.yaml:612:  local_bbox_max:
configs/object_geometry.generated.yaml:616:  local_bbox_size:
configs/object_geometry.generated.yaml:632:  local_bbox_min:
configs/object_geometry.generated.yaml:636:  local_bbox_max:
configs/object_geometry.generated.yaml:640:  local_bbox_size:
configs/object_geometry.generated.yaml:656:  local_bbox_min:
configs/object_geometry.generated.yaml:660:  local_bbox_max:
configs/object_geometry.generated.yaml:664:  local_bbox_size:
configs/object_geometry.generated.yaml:680:  local_bbox_min:
configs/object_geometry.generated.yaml:684:  local_bbox_max:
configs/object_geometry.generated.yaml:688:  local_bbox_size:
configs/object_geometry.generated.yaml:704:  local_bbox_min:
configs/object_geometry.generated.yaml:708:  local_bbox_max:
configs/object_geometry.generated.yaml:712:  local_bbox_size:
configs/object_geometry.generated.yaml:728:  local_bbox_min:
configs/object_geometry.generated.yaml:732:  local_bbox_max:
configs/object_geometry.generated.yaml:736:  local_bbox_size:
configs/object_geometry.generated.yaml:752:  local_bbox_min:
configs/object_geometry.generated.yaml:756:  local_bbox_max:
configs/object_geometry.generated.yaml:760:  local_bbox_size:
configs/object_geometry.generated.yaml:776:  local_bbox_min:
configs/object_geometry.generated.yaml:780:  local_bbox_max:
configs/object_geometry.generated.yaml:784:  local_bbox_size:
configs/object_geometry.generated.yaml:800:  local_bbox_min:
configs/object_geometry.generated.yaml:804:  local_bbox_max:
configs/object_geometry.generated.yaml:808:  local_bbox_size:
configs/object_geometry.generated.yaml:824:  local_bbox_min:
configs/object_geometry.generated.yaml:828:  local_bbox_max:
configs/object_geometry.generated.yaml:832:  local_bbox_size:
configs/object_geometry.generated.yaml:848:  local_bbox_min:
configs/object_geometry.generated.yaml:852:  local_bbox_max:
configs/object_geometry.generated.yaml:856:  local_bbox_size:
configs/object_geometry.generated.yaml:872:  local_bbox_min:
configs/object_geometry.generated.yaml:876:  local_bbox_max:
configs/object_geometry.generated.yaml:880:  local_bbox_size:
configs/object_geometry.generated.yaml:896:  local_bbox_min:
configs/object_geometry.generated.yaml:900:  local_bbox_max:
configs/object_geometry.generated.yaml:904:  local_bbox_size:
configs/object_geometry.generated.yaml:920:  local_bbox_min:
configs/object_geometry.generated.yaml:924:  local_bbox_max:
configs/object_geometry.generated.yaml:928:  local_bbox_size:
configs/object_geometry.generated.yaml:944:  local_bbox_min:
configs/object_geometry.generated.yaml:948:  local_bbox_max:
configs/object_geometry.generated.yaml:952:  local_bbox_size:
configs/object_geometry.generated.yaml:968:  local_bbox_min:
configs/object_geometry.generated.yaml:972:  local_bbox_max:
configs/object_geometry.generated.yaml:976:  local_bbox_size:
configs/object_geometry.generated.yaml:992:  local_bbox_min:
configs/object_geometry.generated.yaml:996:  local_bbox_max:
configs/object_geometry.generated.yaml:1000:  local_bbox_size:
configs/object_geometry.generated.yaml:1016:  local_bbox_min:
configs/object_geometry.generated.yaml:1020:  local_bbox_max:
configs/object_geometry.generated.yaml:1024:  local_bbox_size:
configs/object_geometry.generated.yaml:1040:  local_bbox_min:
configs/object_geometry.generated.yaml:1044:  local_bbox_max:
configs/object_geometry.generated.yaml:1048:  local_bbox_size:
configs/object_geometry.generated.yaml:1064:  local_bbox_min:
configs/object_geometry.generated.yaml:1068:  local_bbox_max:
configs/object_geometry.generated.yaml:1072:  local_bbox_size:
configs/object_geometry.generated.yaml:1088:  local_bbox_min:
configs/object_geometry.generated.yaml:1092:  local_bbox_max:
configs/object_geometry.generated.yaml:1096:  local_bbox_size:
configs/object_geometry.generated.yaml:1112:  local_bbox_min:
configs/object_geometry.generated.yaml:1116:  local_bbox_max:
configs/object_geometry.generated.yaml:1120:  local_bbox_size:
configs/object_geometry.generated.yaml:1136:  local_bbox_min:
configs/object_geometry.generated.yaml:1140:  local_bbox_max:
configs/object_geometry.generated.yaml:1144:  local_bbox_size:
configs/object_geometry.generated.yaml:1160:  local_bbox_min:
configs/object_geometry.generated.yaml:1164:  local_bbox_max:
configs/object_geometry.generated.yaml:1168:  local_bbox_size:
configs/object_geometry.generated.yaml:1184:  local_bbox_min:
configs/object_geometry.generated.yaml:1188:  local_bbox_max:
configs/object_geometry.generated.yaml:1192:  local_bbox_size:
configs/object_geometry.generated.yaml:1208:  local_bbox_min:
configs/object_geometry.generated.yaml:1212:  local_bbox_max:
configs/object_geometry.generated.yaml:1216:  local_bbox_size:
configs/object_geometry.generated.yaml:1232:  local_bbox_min:
configs/object_geometry.generated.yaml:1236:  local_bbox_max:
configs/object_geometry.generated.yaml:1240:  local_bbox_size:
configs/object_geometry.generated.yaml:1256:  local_bbox_min:
configs/object_geometry.generated.yaml:1260:  local_bbox_max:
configs/object_geometry.generated.yaml:1264:  local_bbox_size:
configs/object_geometry.generated.yaml:1280:  local_bbox_min:
configs/object_geometry.generated.yaml:1284:  local_bbox_max:
configs/object_geometry.generated.yaml:1288:  local_bbox_size:
configs/object_geometry.generated.yaml:1304:  local_bbox_min:
configs/object_geometry.generated.yaml:1308:  local_bbox_max:
configs/object_geometry.generated.yaml:1312:  local_bbox_size:
configs/object_geometry.generated.yaml:1328:  local_bbox_min:
configs/object_geometry.generated.yaml:1332:  local_bbox_max:
configs/object_geometry.generated.yaml:1336:  local_bbox_size:
configs/object_geometry.generated.yaml:1352:  local_bbox_min:
configs/object_geometry.generated.yaml:1356:  local_bbox_max:
configs/object_geometry.generated.yaml:1360:  local_bbox_size:
configs/object_geometry.generated.yaml:1376:  local_bbox_min:
configs/object_geometry.generated.yaml:1380:  local_bbox_max:
configs/object_geometry.generated.yaml:1384:  local_bbox_size:
configs/object_geometry.generated.yaml:1400:  local_bbox_min:
configs/object_geometry.generated.yaml:1404:  local_bbox_max:
configs/object_geometry.generated.yaml:1408:  local_bbox_size:
configs/object_geometry.generated.yaml:1424:  local_bbox_min:
configs/object_geometry.generated.yaml:1428:  local_bbox_max:
configs/object_geometry.generated.yaml:1432:  local_bbox_size:
configs/object_geometry.generated.yaml:1448:  local_bbox_min:
configs/object_geometry.generated.yaml:1452:  local_bbox_max:
configs/object_geometry.generated.yaml:1456:  local_bbox_size:
configs/object_geometry.generated.yaml:1472:  local_bbox_min:
configs/object_geometry.generated.yaml:1476:  local_bbox_max:
configs/object_geometry.generated.yaml:1480:  local_bbox_size:
configs/object_geometry.generated.yaml:1496:  local_bbox_min:
configs/object_geometry.generated.yaml:1500:  local_bbox_max:
configs/object_geometry.generated.yaml:1504:  local_bbox_size:
configs/object_geometry.generated.yaml:1520:  local_bbox_min:
configs/object_geometry.generated.yaml:1524:  local_bbox_max:
configs/object_geometry.generated.yaml:1528:  local_bbox_size:
configs/object_geometry.generated.yaml:1544:  local_bbox_min:
configs/object_geometry.generated.yaml:1548:  local_bbox_max:
configs/object_geometry.generated.yaml:1552:  local_bbox_size:
configs/object_geometry.generated.yaml:1572:  local_bbox_min:
configs/object_geometry.generated.yaml:1576:  local_bbox_max:
configs/object_geometry.generated.yaml:1580:  local_bbox_size:
configs/object_geometry.generated.yaml:1600:  local_bbox_min:
configs/object_geometry.generated.yaml:1604:  local_bbox_max:
configs/object_geometry.generated.yaml:1608:  local_bbox_size:
configs/object_geometry.generated.yaml:1628:  local_bbox_min:
configs/object_geometry.generated.yaml:1632:  local_bbox_max:
configs/object_geometry.generated.yaml:1636:  local_bbox_size:
configs/object_geometry.generated.yaml:1656:  local_bbox_min:
configs/object_geometry.generated.yaml:1660:  local_bbox_max:
configs/object_geometry.generated.yaml:1664:  local_bbox_size:
configs/object_geometry.generated.yaml:1684:  local_bbox_min:
configs/object_geometry.generated.yaml:1688:  local_bbox_max:
configs/object_geometry.generated.yaml:1692:  local_bbox_size:
configs/object_geometry.generated.yaml:1712:  local_bbox_min:
configs/object_geometry.generated.yaml:1716:  local_bbox_max:
configs/object_geometry.generated.yaml:1720:  local_bbox_size:
configs/object_geometry.generated.yaml:1740:  local_bbox_min:
configs/object_geometry.generated.yaml:1744:  local_bbox_max:
configs/object_geometry.generated.yaml:1748:  local_bbox_size:
configs/object_geometry.generated.yaml:1768:  local_bbox_min:
configs/object_geometry.generated.yaml:1772:  local_bbox_max:
configs/object_geometry.generated.yaml:1776:  local_bbox_size:
configs/object_geometry.generated.yaml:1796:  local_bbox_min:
configs/object_geometry.generated.yaml:1800:  local_bbox_max:
configs/object_geometry.generated.yaml:1804:  local_bbox_size:
configs/object_geometry.generated.yaml:1824:  local_bbox_min:
configs/object_geometry.generated.yaml:1828:  local_bbox_max:
configs/object_geometry.generated.yaml:1832:  local_bbox_size:
configs/object_geometry.generated.yaml:1852:  local_bbox_min:
configs/object_geometry.generated.yaml:1856:  local_bbox_max:
configs/object_geometry.generated.yaml:1860:  local_bbox_size:
configs/object_geometry.generated.yaml:1880:  local_bbox_min:
configs/object_geometry.generated.yaml:1884:  local_bbox_max:
configs/object_geometry.generated.yaml:1888:  local_bbox_size:
configs/object_geometry.generated.yaml:1908:  local_bbox_min:
configs/object_geometry.generated.yaml:1912:  local_bbox_max:
configs/object_geometry.generated.yaml:1916:  local_bbox_size:
configs/object_geometry.generated.yaml:1936:  local_bbox_min:
configs/object_geometry.generated.yaml:1940:  local_bbox_max:
configs/object_geometry.generated.yaml:1944:  local_bbox_size:
configs/object_geometry.generated.yaml:1964:  local_bbox_min:
configs/object_geometry.generated.yaml:1968:  local_bbox_max:
configs/object_geometry.generated.yaml:1972:  local_bbox_size:
configs/object_geometry.generated.yaml:1988:  local_bbox_min:
configs/object_geometry.generated.yaml:1992:  local_bbox_max:
configs/object_geometry.generated.yaml:1996:  local_bbox_size:
configs/object_geometry.generated.yaml:2012:  local_bbox_min:
configs/object_geometry.generated.yaml:2016:  local_bbox_max:
configs/object_geometry.generated.yaml:2020:  local_bbox_size:
configs/object_geometry.generated.yaml:2036:  local_bbox_min:
configs/object_geometry.generated.yaml:2040:  local_bbox_max:
configs/object_geometry.generated.yaml:2044:  local_bbox_size:
configs/object_geometry.generated.yaml:2060:  local_bbox_min:
configs/object_geometry.generated.yaml:2064:  local_bbox_max:
configs/object_geometry.generated.yaml:2068:  local_bbox_size:
configs/object_geometry.generated.yaml:2084:  local_bbox_min:
configs/object_geometry.generated.yaml:2088:  local_bbox_max:
configs/object_geometry.generated.yaml:2092:  local_bbox_size:
configs/object_geometry.generated.yaml:2108:  local_bbox_min:
configs/object_geometry.generated.yaml:2112:  local_bbox_max:
configs/object_geometry.generated.yaml:2116:  local_bbox_size:
configs/object_geometry.generated.yaml:2132:  local_bbox_min:
configs/object_geometry.generated.yaml:2136:  local_bbox_max:
configs/object_geometry.generated.yaml:2140:  local_bbox_size:
configs/object_geometry.generated.yaml:2156:  local_bbox_min:
configs/object_geometry.generated.yaml:2160:  local_bbox_max:
configs/object_geometry.generated.yaml:2164:  local_bbox_size:
configs/object_geometry.generated.yaml:2180:  local_bbox_min:
configs/object_geometry.generated.yaml:2184:  local_bbox_max:
configs/object_geometry.generated.yaml:2188:  local_bbox_size:
configs/object_geometry.generated.yaml:2204:  local_bbox_min:
configs/object_geometry.generated.yaml:2208:  local_bbox_max:
configs/object_geometry.generated.yaml:2212:  local_bbox_size:
configs/object_geometry.generated.yaml:2228:  local_bbox_min:
configs/object_geometry.generated.yaml:2232:  local_bbox_max:
configs/object_geometry.generated.yaml:2236:  local_bbox_size:
configs/object_geometry.generated.yaml:2252:  local_bbox_min:
configs/object_geometry.generated.yaml:2256:  local_bbox_max:
configs/object_geometry.generated.yaml:2260:  local_bbox_size:
configs/object_geometry.generated.yaml:2276:  local_bbox_min:
configs/object_geometry.generated.yaml:2280:  local_bbox_max:
configs/object_geometry.generated.yaml:2284:  local_bbox_size:
configs/object_geometry.generated.yaml:2300:  local_bbox_min:
configs/object_geometry.generated.yaml:2304:  local_bbox_max:
configs/object_geometry.generated.yaml:2308:  local_bbox_size:
configs/object_geometry.generated.yaml:2324:  local_bbox_min:
configs/object_geometry.generated.yaml:2328:  local_bbox_max:
configs/object_geometry.generated.yaml:2332:  local_bbox_size:
configs/object_geometry.generated.yaml:2348:  local_bbox_min:
configs/object_geometry.generated.yaml:2352:  local_bbox_max:
configs/object_geometry.generated.yaml:2356:  local_bbox_size:
configs/object_geometry.generated.yaml:2372:  local_bbox_min:
configs/object_geometry.generated.yaml:2376:  local_bbox_max:
configs/object_geometry.generated.yaml:2380:  local_bbox_size:
configs/object_geometry.generated.yaml:2396:  local_bbox_min:
configs/object_geometry.generated.yaml:2400:  local_bbox_max:
configs/object_geometry.generated.yaml:2404:  local_bbox_size:
configs/object_geometry.generated.yaml:2420:  local_bbox_min:
configs/object_geometry.generated.yaml:2424:  local_bbox_max:
configs/object_geometry.generated.yaml:2428:  local_bbox_size:
configs/object_geometry.generated.yaml:2444:  local_bbox_min:
configs/object_geometry.generated.yaml:2448:  local_bbox_max:
configs/object_geometry.generated.yaml:2452:  local_bbox_size:
configs/object_geometry.generated.yaml:2468:  local_bbox_min:
configs/object_geometry.generated.yaml:2472:  local_bbox_max:
configs/object_geometry.generated.yaml:2476:  local_bbox_size:
configs/object_geometry.generated.yaml:2492:  local_bbox_min:
configs/object_geometry.generated.yaml:2496:  local_bbox_max:
configs/object_geometry.generated.yaml:2500:  local_bbox_size:
configs/object_geometry.generated.yaml:2516:  local_bbox_min:
configs/object_geometry.generated.yaml:2520:  local_bbox_max:
configs/object_geometry.generated.yaml:2524:  local_bbox_size:
configs/object_geometry.generated.yaml:2540:  local_bbox_min:
configs/object_geometry.generated.yaml:2544:  local_bbox_max:
configs/object_geometry.generated.yaml:2548:  local_bbox_size:
configs/object_geometry.generated.yaml:2564:  local_bbox_min:
configs/object_geometry.generated.yaml:2568:  local_bbox_max:
configs/object_geometry.generated.yaml:2572:  local_bbox_size:
configs/object_geometry.generated.yaml:2588:  local_bbox_min:
configs/object_geometry.generated.yaml:2592:  local_bbox_max:
configs/object_geometry.generated.yaml:2596:  local_bbox_size:
configs/object_geometry.generated.yaml:2612:  local_bbox_min:
configs/object_geometry.generated.yaml:2616:  local_bbox_max:
configs/object_geometry.generated.yaml:2620:  local_bbox_size:
configs/object_geometry.generated.yaml:2636:  local_bbox_min:
configs/object_geometry.generated.yaml:2640:  local_bbox_max:
configs/object_geometry.generated.yaml:2644:  local_bbox_size:
configs/object_geometry.generated.yaml:2660:  local_bbox_min:
configs/object_geometry.generated.yaml:2664:  local_bbox_max:
configs/object_geometry.generated.yaml:2668:  local_bbox_size:
configs/object_geometry.generated.yaml:2684:  local_bbox_min:
configs/object_geometry.generated.yaml:2688:  local_bbox_max:
configs/object_geometry.generated.yaml:2692:  local_bbox_size:
configs/object_geometry.generated.yaml:2708:  local_bbox_min:
configs/object_geometry.generated.yaml:2712:  local_bbox_max:
configs/object_geometry.generated.yaml:2716:  local_bbox_size:
configs/object_geometry.generated.yaml:2732:  local_bbox_min:
configs/object_geometry.generated.yaml:2736:  local_bbox_max:
configs/object_geometry.generated.yaml:2740:  local_bbox_size:
configs/object_geometry.generated.yaml:2756:  local_bbox_min:
configs/object_geometry.generated.yaml:2760:  local_bbox_max:
configs/object_geometry.generated.yaml:2764:  local_bbox_size:
configs/object_geometry.generated.yaml:2780:  local_bbox_min:
configs/object_geometry.generated.yaml:2784:  local_bbox_max:
configs/object_geometry.generated.yaml:2788:  local_bbox_size:
configs/object_geometry.generated.yaml:2804:  local_bbox_min:
configs/object_geometry.generated.yaml:2808:  local_bbox_max:
configs/object_geometry.generated.yaml:2812:  local_bbox_size:
configs/object_geometry.generated.yaml:2828:  local_bbox_min:
configs/object_geometry.generated.yaml:2832:  local_bbox_max:
configs/object_geometry.generated.yaml:2836:  local_bbox_size:
configs/object_geometry.generated.yaml:2852:  local_bbox_min:
configs/object_geometry.generated.yaml:2856:  local_bbox_max:
configs/object_geometry.generated.yaml:2860:  local_bbox_size:
configs/object_geometry.generated.yaml:2876:  local_bbox_min:
configs/object_geometry.generated.yaml:2880:  local_bbox_max:
configs/object_geometry.generated.yaml:2884:  local_bbox_size:
configs/object_geometry.generated.yaml:2900:  local_bbox_min:
configs/object_geometry.generated.yaml:2904:  local_bbox_max:
configs/object_geometry.generated.yaml:2908:  local_bbox_size:
configs/object_geometry.generated.yaml:2924:  local_bbox_min:
configs/object_geometry.generated.yaml:2928:  local_bbox_max:
configs/object_geometry.generated.yaml:2932:  local_bbox_size:
configs/object_geometry.generated.yaml:2948:  local_bbox_min:
configs/object_geometry.generated.yaml:2952:  local_bbox_max:
configs/object_geometry.generated.yaml:2956:  local_bbox_size:
configs/object_geometry.generated.yaml:2972:  local_bbox_min:
configs/object_geometry.generated.yaml:2976:  local_bbox_max:
configs/object_geometry.generated.yaml:2980:  local_bbox_size:
configs/object_geometry.generated.yaml:2996:  local_bbox_min:
configs/object_geometry.generated.yaml:3000:  local_bbox_max:
configs/object_geometry.generated.yaml:3004:  local_bbox_size:
configs/object_geometry.generated.yaml:3020:  local_bbox_min:
configs/object_geometry.generated.yaml:3024:  local_bbox_max:
configs/object_geometry.generated.yaml:3028:  local_bbox_size:
configs/object_geometry.generated.yaml:3044:  local_bbox_min:
configs/object_geometry.generated.yaml:3048:  local_bbox_max:
configs/object_geometry.generated.yaml:3052:  local_bbox_size:
configs/object_geometry.generated.yaml:3068:  local_bbox_min:
configs/object_geometry.generated.yaml:3072:  local_bbox_max:
configs/object_geometry.generated.yaml:3076:  local_bbox_size:
configs/object_geometry.generated.yaml:3092:  local_bbox_min:
configs/object_geometry.generated.yaml:3096:  local_bbox_max:
configs/object_geometry.generated.yaml:3100:  local_bbox_size:
configs/object_geometry.generated.yaml:3116:  local_bbox_min:
configs/object_geometry.generated.yaml:3120:  local_bbox_max:
configs/object_geometry.generated.yaml:3124:  local_bbox_size:
configs/object_geometry.generated.yaml:3140:  local_bbox_min:
configs/object_geometry.generated.yaml:3144:  local_bbox_max:
configs/object_geometry.generated.yaml:3148:  local_bbox_size:
configs/object_geometry.generated.yaml:3164:  local_bbox_min:
configs/object_geometry.generated.yaml:3168:  local_bbox_max:
configs/object_geometry.generated.yaml:3172:  local_bbox_size:
configs/object_geometry.generated.yaml:3188:  local_bbox_min:
configs/object_geometry.generated.yaml:3192:  local_bbox_max:
configs/object_geometry.generated.yaml:3196:  local_bbox_size:
configs/object_geometry.generated.yaml:3212:  local_bbox_min:
configs/object_geometry.generated.yaml:3216:  local_bbox_max:
configs/object_geometry.generated.yaml:3220:  local_bbox_size:
configs/object_geometry.generated.yaml:3236:  local_bbox_min:
configs/object_geometry.generated.yaml:3240:  local_bbox_max:
configs/object_geometry.generated.yaml:3244:  local_bbox_size:
configs/object_geometry.generated.yaml:3260:  local_bbox_min:
configs/object_geometry.generated.yaml:3264:  local_bbox_max:
configs/object_geometry.generated.yaml:3268:  local_bbox_size:
configs/object_geometry.generated.yaml:3284:  local_bbox_min:
configs/object_geometry.generated.yaml:3288:  local_bbox_max:
configs/object_geometry.generated.yaml:3292:  local_bbox_size:
configs/object_geometry.generated.yaml:3308:  local_bbox_min:
configs/object_geometry.generated.yaml:3312:  local_bbox_max:
configs/object_geometry.generated.yaml:3316:  local_bbox_size:
configs/object_geometry.generated.yaml:3332:  local_bbox_min:
configs/object_geometry.generated.yaml:3336:  local_bbox_max:
configs/object_geometry.generated.yaml:3340:  local_bbox_size:
configs/object_geometry.generated.yaml:3356:  local_bbox_min:
configs/object_geometry.generated.yaml:3360:  local_bbox_max:
configs/object_geometry.generated.yaml:3364:  local_bbox_size:
configs/object_geometry.generated.yaml:3380:  local_bbox_min:
configs/object_geometry.generated.yaml:3384:  local_bbox_max:
configs/object_geometry.generated.yaml:3388:  local_bbox_size:
configs/object_geometry.generated.yaml:3404:  local_bbox_min:
configs/object_geometry.generated.yaml:3408:  local_bbox_max:
configs/object_geometry.generated.yaml:3412:  local_bbox_size:
configs/object_geometry.generated.yaml:3428:  local_bbox_min:
configs/object_geometry.generated.yaml:3432:  local_bbox_max:
configs/object_geometry.generated.yaml:3436:  local_bbox_size:
configs/object_geometry.generated.yaml:3452:  local_bbox_min:
configs/object_geometry.generated.yaml:3456:  local_bbox_max:
configs/object_geometry.generated.yaml:3460:  local_bbox_size:
configs/object_geometry.generated.yaml:3476:  local_bbox_min:
configs/object_geometry.generated.yaml:3480:  local_bbox_max:
configs/object_geometry.generated.yaml:3484:  local_bbox_size:
configs/object_geometry.generated.yaml:3500:  local_bbox_min:
configs/object_geometry.generated.yaml:3504:  local_bbox_max:
configs/object_geometry.generated.yaml:3508:  local_bbox_size:
configs/object_geometry.generated.yaml:3524:  local_bbox_min:
configs/object_geometry.generated.yaml:3528:  local_bbox_max:
configs/object_geometry.generated.yaml:3532:  local_bbox_size:
configs/object_geometry.generated.yaml:3548:  local_bbox_min:
configs/object_geometry.generated.yaml:3552:  local_bbox_max:
configs/object_geometry.generated.yaml:3556:  local_bbox_size:
configs/object_geometry.generated.yaml:3572:  local_bbox_min:
configs/object_geometry.generated.yaml:3576:  local_bbox_max:
configs/object_geometry.generated.yaml:3580:  local_bbox_size:
configs/object_geometry.generated.yaml:3596:  local_bbox_min:
configs/object_geometry.generated.yaml:3600:  local_bbox_max:
configs/object_geometry.generated.yaml:3604:  local_bbox_size:
configs/object_geometry.generated.yaml:3620:  local_bbox_min:
configs/object_geometry.generated.yaml:3624:  local_bbox_max:
configs/object_geometry.generated.yaml:3628:  local_bbox_size:
configs/object_geometry.generated.yaml:3644:  local_bbox_min:
configs/object_geometry.generated.yaml:3648:  local_bbox_max:
configs/object_geometry.generated.yaml:3652:  local_bbox_size:
configs/object_geometry.generated.yaml:3668:  local_bbox_min:
configs/object_geometry.generated.yaml:3672:  local_bbox_max:
configs/object_geometry.generated.yaml:3676:  local_bbox_size:
configs/object_geometry.generated.yaml:3692:  local_bbox_min:
configs/object_geometry.generated.yaml:3696:  local_bbox_max:
configs/object_geometry.generated.yaml:3700:  local_bbox_size:
configs/object_geometry.generated.yaml:3716:  local_bbox_min:
configs/object_geometry.generated.yaml:3720:  local_bbox_max:
configs/object_geometry.generated.yaml:3724:  local_bbox_size:
configs/object_geometry.generated.yaml:3740:  local_bbox_min:
configs/object_geometry.generated.yaml:3744:  local_bbox_max:
configs/object_geometry.generated.yaml:3748:  local_bbox_size:
configs/object_geometry.generated.yaml:3764:  local_bbox_min:
configs/object_geometry.generated.yaml:3768:  local_bbox_max:
configs/object_geometry.generated.yaml:3772:  local_bbox_size:
configs/object_geometry.generated.yaml:3788:  local_bbox_min:
configs/object_geometry.generated.yaml:3792:  local_bbox_max:
configs/object_geometry.generated.yaml:3796:  local_bbox_size:
configs/object_geometry.generated.yaml:3812:  local_bbox_min:
configs/object_geometry.generated.yaml:3816:  local_bbox_max:
configs/object_geometry.generated.yaml:3820:  local_bbox_size:
configs/object_geometry.generated.yaml:3836:  local_bbox_min:
configs/object_geometry.generated.yaml:3840:  local_bbox_max:
configs/object_geometry.generated.yaml:3844:  local_bbox_size:
configs/object_geometry.generated.yaml:3860:  local_bbox_min:
configs/object_geometry.generated.yaml:3864:  local_bbox_max:
configs/object_geometry.generated.yaml:3868:  local_bbox_size:
configs/object_geometry.generated.yaml:3884:  local_bbox_min:
configs/object_geometry.generated.yaml:3888:  local_bbox_max:
configs/object_geometry.generated.yaml:3892:  local_bbox_size:
configs/object_geometry.generated.yaml:3908:  local_bbox_min:
configs/object_geometry.generated.yaml:3912:  local_bbox_max:
configs/object_geometry.generated.yaml:3916:  local_bbox_size:
configs/object_geometry.generated.yaml:3932:  local_bbox_min:
configs/object_geometry.generated.yaml:3936:  local_bbox_max:
configs/object_geometry.generated.yaml:3940:  local_bbox_size:
configs/object_geometry.generated.yaml:3956:  local_bbox_min:
configs/object_geometry.generated.yaml:3960:  local_bbox_max:
configs/object_geometry.generated.yaml:3964:  local_bbox_size:
configs/object_geometry.generated.yaml:3980:  local_bbox_min:
configs/object_geometry.generated.yaml:3984:  local_bbox_max:
configs/object_geometry.generated.yaml:3988:  local_bbox_size:
configs/object_geometry.generated.yaml:4004:  local_bbox_min:
configs/object_geometry.generated.yaml:4008:  local_bbox_max:
configs/object_geometry.generated.yaml:4012:  local_bbox_size:
configs/object_geometry.generated.yaml:4028:  local_bbox_min:
configs/object_geometry.generated.yaml:4032:  local_bbox_max:
configs/object_geometry.generated.yaml:4036:  local_bbox_size:
configs/object_geometry.generated.yaml:4052:  local_bbox_min:
configs/object_geometry.generated.yaml:4056:  local_bbox_max:
configs/object_geometry.generated.yaml:4060:  local_bbox_size:
configs/object_geometry.generated.yaml:4076:  local_bbox_min:
configs/object_geometry.generated.yaml:4080:  local_bbox_max:
configs/object_geometry.generated.yaml:4084:  local_bbox_size:
configs/object_geometry.generated.yaml:4100:  local_bbox_min:
configs/object_geometry.generated.yaml:4104:  local_bbox_max:
configs/object_geometry.generated.yaml:4108:  local_bbox_size:
configs/object_geometry.generated.yaml:4124:  local_bbox_min:
configs/object_geometry.generated.yaml:4128:  local_bbox_max:
configs/object_geometry.generated.yaml:4132:  local_bbox_size:
configs/object_geometry.generated.yaml:4148:  local_bbox_min:
configs/object_geometry.generated.yaml:4152:  local_bbox_max:
configs/object_geometry.generated.yaml:4156:  local_bbox_size:
configs/object_geometry.generated.yaml:4172:  local_bbox_min:
configs/object_geometry.generated.yaml:4176:  local_bbox_max:
configs/object_geometry.generated.yaml:4180:  local_bbox_size:
configs/object_geometry.generated.yaml:4196:  local_bbox_min:
configs/object_geometry.generated.yaml:4200:  local_bbox_max:
configs/object_geometry.generated.yaml:4204:  local_bbox_size:
configs/object_geometry.generated.yaml:4220:  local_bbox_min:
configs/object_geometry.generated.yaml:4224:  local_bbox_max:
configs/object_geometry.generated.yaml:4228:  local_bbox_size:
configs/object_geometry.generated.yaml:4244:  local_bbox_min:
configs/object_geometry.generated.yaml:4248:  local_bbox_max:
configs/object_geometry.generated.yaml:4252:  local_bbox_size:
configs/object_geometry.generated.yaml:4268:  local_bbox_min:
configs/object_geometry.generated.yaml:4272:  local_bbox_max:
configs/object_geometry.generated.yaml:4276:  local_bbox_size:
configs/object_geometry.generated.yaml:4292:  local_bbox_min:
configs/object_geometry.generated.yaml:4296:  local_bbox_max:
configs/object_geometry.generated.yaml:4300:  local_bbox_size:
configs/object_geometry.generated.yaml:4320:  local_bbox_min:
configs/object_geometry.generated.yaml:4324:  local_bbox_max:
configs/object_geometry.generated.yaml:4328:  local_bbox_size:
configs/object_geometry.generated.yaml:4344:  local_bbox_min:
configs/object_geometry.generated.yaml:4348:  local_bbox_max:
configs/object_geometry.generated.yaml:4352:  local_bbox_size:
configs/object_geometry.generated.yaml:4368:  local_bbox_min:
configs/object_geometry.generated.yaml:4372:  local_bbox_max:
configs/object_geometry.generated.yaml:4376:  local_bbox_size:
configs/object_geometry.generated.yaml:4392:  local_bbox_min:
configs/object_geometry.generated.yaml:4396:  local_bbox_max:
configs/object_geometry.generated.yaml:4400:  local_bbox_size:
configs/object_geometry.generated.yaml:4416:  local_bbox_min:
configs/object_geometry.generated.yaml:4420:  local_bbox_max:
configs/object_geometry.generated.yaml:4424:  local_bbox_size:
configs/object_geometry.generated.yaml:4440:  local_bbox_min:
configs/object_geometry.generated.yaml:4444:  local_bbox_max:
configs/object_geometry.generated.yaml:4448:  local_bbox_size:
configs/object_geometry.generated.yaml:4464:  local_bbox_min:
configs/object_geometry.generated.yaml:4468:  local_bbox_max:
configs/object_geometry.generated.yaml:4472:  local_bbox_size:
configs/object_geometry.generated.yaml:4488:  local_bbox_min:
configs/object_geometry.generated.yaml:4492:  local_bbox_max:
configs/object_geometry.generated.yaml:4496:  local_bbox_size:
configs/object_geometry.generated.yaml:4516:  local_bbox_min:
configs/object_geometry.generated.yaml:4520:  local_bbox_max:
configs/object_geometry.generated.yaml:4524:  local_bbox_size:
configs/object_geometry.generated.yaml:4540:  local_bbox_min:
configs/object_geometry.generated.yaml:4544:  local_bbox_max:
configs/object_geometry.generated.yaml:4548:  local_bbox_size:
configs/object_geometry.generated.yaml:4564:  local_bbox_min:
configs/object_geometry.generated.yaml:4568:  local_bbox_max:
configs/object_geometry.generated.yaml:4572:  local_bbox_size:
configs/object_geometry.generated.yaml:4588:  local_bbox_min:
configs/object_geometry.generated.yaml:4592:  local_bbox_max:
configs/object_geometry.generated.yaml:4596:  local_bbox_size:
configs/object_geometry.generated.yaml:4612:  local_bbox_min:
configs/object_geometry.generated.yaml:4616:  local_bbox_max:
configs/object_geometry.generated.yaml:4620:  local_bbox_size:
configs/object_geometry.generated.yaml:4636:  local_bbox_min:
configs/object_geometry.generated.yaml:4640:  local_bbox_max:
configs/object_geometry.generated.yaml:4644:  local_bbox_size:
configs/object_geometry.generated.yaml:4660:  local_bbox_min:
configs/object_geometry.generated.yaml:4664:  local_bbox_max:
configs/object_geometry.generated.yaml:4668:  local_bbox_size:
configs/object_geometry.generated.yaml:4684:  local_bbox_min:
configs/object_geometry.generated.yaml:4688:  local_bbox_max:
configs/object_geometry.generated.yaml:4692:  local_bbox_size:
configs/object_geometry.generated.yaml:4708:  local_bbox_min:
configs/object_geometry.generated.yaml:4712:  local_bbox_max:
configs/object_geometry.generated.yaml:4716:  local_bbox_size:
configs/object_geometry.generated.yaml:4732:  local_bbox_min:
configs/object_geometry.generated.yaml:4736:  local_bbox_max:
configs/object_geometry.generated.yaml:4740:  local_bbox_size:
configs/object_geometry.generated.yaml:4756:  local_bbox_min:
configs/object_geometry.generated.yaml:4760:  local_bbox_max:
configs/object_geometry.generated.yaml:4764:  local_bbox_size:
configs/object_geometry.generated.yaml:4780:  local_bbox_min:
configs/object_geometry.generated.yaml:4784:  local_bbox_max:
configs/object_geometry.generated.yaml:4788:  local_bbox_size:
configs/object_geometry.generated.yaml:4804:  local_bbox_min:
configs/object_geometry.generated.yaml:4808:  local_bbox_max:
configs/object_geometry.generated.yaml:4812:  local_bbox_size:
configs/object_geometry.generated.yaml:4832:  local_bbox_min:
configs/object_geometry.generated.yaml:4836:  local_bbox_max:
configs/object_geometry.generated.yaml:4840:  local_bbox_size:
configs/object_geometry.generated.yaml:4860:  local_bbox_min:
configs/object_geometry.generated.yaml:4864:  local_bbox_max:
configs/object_geometry.generated.yaml:4868:  local_bbox_size:
configs/object_geometry.generated.yaml:4888:  local_bbox_min:
configs/object_geometry.generated.yaml:4892:  local_bbox_max:
configs/object_geometry.generated.yaml:4896:  local_bbox_size:
configs/object_geometry.generated.yaml:4916:  local_bbox_min:
configs/object_geometry.generated.yaml:4920:  local_bbox_max:
configs/object_geometry.generated.yaml:4924:  local_bbox_size:
configs/object_geometry.generated.yaml:4944:  local_bbox_min:
configs/object_geometry.generated.yaml:4948:  local_bbox_max:
configs/object_geometry.generated.yaml:4952:  local_bbox_size:
configs/object_geometry.generated.yaml:4972:  local_bbox_min:
configs/object_geometry.generated.yaml:4976:  local_bbox_max:
configs/object_geometry.generated.yaml:4980:  local_bbox_size:
configs/object_geometry.generated.yaml:5000:  local_bbox_min:
configs/object_geometry.generated.yaml:5004:  local_bbox_max:
configs/object_geometry.generated.yaml:5008:  local_bbox_size:
configs/object_geometry.generated.yaml:5028:  local_bbox_min:
configs/object_geometry.generated.yaml:5032:  local_bbox_max:
configs/object_geometry.generated.yaml:5036:  local_bbox_size:
configs/object_geometry.generated.yaml:5056:  local_bbox_min:
configs/object_geometry.generated.yaml:5060:  local_bbox_max:
configs/object_geometry.generated.yaml:5064:  local_bbox_size:
configs/object_geometry.generated.yaml:5080:  local_bbox_min:
configs/object_geometry.generated.yaml:5084:  local_bbox_max:
configs/object_geometry.generated.yaml:5088:  local_bbox_size:
configs/object_geometry.generated.yaml:5104:  local_bbox_min:
configs/object_geometry.generated.yaml:5108:  local_bbox_max:
configs/object_geometry.generated.yaml:5112:  local_bbox_size:
configs/object_geometry.generated.yaml:5128:  local_bbox_min:
configs/object_geometry.generated.yaml:5132:  local_bbox_max:
configs/object_geometry.generated.yaml:5136:  local_bbox_size:
configs/object_geometry.generated.yaml:5152:  local_bbox_min:
configs/object_geometry.generated.yaml:5156:  local_bbox_max:
configs/object_geometry.generated.yaml:5160:  local_bbox_size:
configs/collection_reaching.yaml:16:  geometry_config: object_geometry.generated.yaml
configs/collection.yaml:16:  geometry_config: object_geometry.generated.yaml
configs/collection.yaml:24:placement_target:
configs/collection.yaml:26:  geometry_config: object_geometry.generated.yaml
configs/collection.yaml:36:  geometry_config: object_geometry.generated.yaml
configs/collection.yaml:46:  placement_target_margin_m: 0.035
configs/receptacle_goal_tests/receptacle_tray_tray04_fcan03_mass020.yaml:1:output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020
configs/receptacle_goal_tests/receptacle_tray_tray04_fcan03_mass020.yaml:26:physics_overrides:
configs/receptacle_goal_tests/receptacle_tray_tray04_fcan03_mass020.yaml:27:  target_mass: 0.20
configs/receptacle_goal_tests/receptacle_tray_tray04_fcan03_mass020.yaml:28:  gripper_stiffness: 150.0
configs/receptacle_goal_tests/receptacle_tray_tray04_fcan03_mass020.yaml:29:  gripper_damping: 15.0
tests/test_pick_place_task.py:11:    def test_make_pick_place_episode_spec_requires_bbox_metadata(self) -> None:
tests/test_pick_place_task.py:12:        with self.assertRaisesRegex(ValueError, "bbox metadata"):
tests/test_pick_place_task.py:20:    def test_make_pick_place_episode_spec_uses_bbox_height_for_object_and_place(self) -> None:
tests/test_pick_place_task.py:26:            object_local_bbox_min=(-0.02, -0.03, -0.024),
tests/test_pick_place_task.py:27:            object_local_bbox_max=(0.02, 0.03, 0.04),
tests/test_pick_place_task.py:41:            object_local_bbox_min=(-0.02, -0.03, -0.024),
tests/test_pick_place_task.py:42:            object_local_bbox_max=(0.02, 0.03, 0.04),
tests/test_pick_place_task.py:43:            placement_target_pos_local=(0.60, 0.25, 1.07),
tests/test_pick_place_task.py:44:            placement_target_local_bbox_min=(-0.07, -0.07, -0.02),
tests/test_pick_place_task.py:45:            placement_target_local_bbox_max=(0.07, 0.07, 0.06),
tests/test_pick_place_task.py:52:        self.assertEqual(spec.placement_target_pos_local, (0.60, 0.25, 1.07))
tests/test_pick_place_task.py:61:                object_local_bbox_min=(-0.02, -0.03, -0.024),
tests/test_pick_place_task.py:62:                object_local_bbox_max=(0.02, 0.03, 0.04),
tests/test_pick_place_task.py:63:                placement_target_pos_local=(0.60, 0.25, 1.07),
tests/test_placement_geometry.py:3:from franka_wrist_camera_scene.tasks.placement_geometry import (
tests/test_placement_geometry.py:9:def test_object_root_z_on_support_places_bbox_bottom_above_surface() -> None:
tests/test_placement_geometry.py:12:        object_bbox_min_z=-0.024,
tests/test_placement_geometry.py:23:        object_bbox_min_z=-0.024,
tests/test_success.py:14:    receptacle_xy_radius_from_bbox,
tests/test_success.py:21:    def test_receptacle_xy_radius_from_bbox(self) -> None:
tests/test_success.py:22:        bbox_min = (-0.1, -0.2, -0.05)
tests/test_success.py:23:        bbox_max = (0.1, 0.2, 0.05)
tests/test_success.py:28:        radius = receptacle_xy_radius_from_bbox(bbox_min, bbox_max, margin_m=0.025)
tests/test_success.py:43:            placement_target_pos_local=(0.5, 0.1, 1.0),
tests/test_success.py:44:            object_local_bbox_min=(-0.02, -0.02, -0.02),
tests/test_success.py:45:            object_local_bbox_max=(0.02, 0.02, 0.02),
tests/test_success.py:46:            placement_target_local_bbox_min=(-0.1, -0.1, -0.05),
tests/test_success.py:47:            placement_target_local_bbox_max=(0.1, 0.1, 0.05),
tests/test_clutter_sampling.py:1:"""Unit tests for geometry-aware clutter sampling."""
tests/test_clutter_sampling.py:19:    def test_planar_footprint_radius_m_uses_bbox_diagonal_and_margin(self) -> None:
tests/test_clutter_sampling.py:21:            bbox_min=(-0.1, -0.2, 0.0),
tests/test_clutter_sampling.py:22:            bbox_max=(0.1, 0.2, 0.1),

## Phase 2 — Trace of Existing Implementation

1. **Where target objects are selected**:
   Target objects are loaded in `src/franka_wrist_camera_scene/collection/pick_place.py` (line 262) via `_load_collection_object_context(target_object_cfg, target_rng)`. This delegates to `load_catalog_object_context` in `src/franka_wrist_camera_scene/scene/object_context.py`, which loads the catalog and calls `sample_catalog_object` from `src/franka_wrist_camera_scene/objects/selection.py`.

2. **Where placement targets are selected**:
   Placement targets are similarly loaded in `src/franka_wrist_camera_scene/collection/pick_place.py` (line 266) via `_load_collection_object_context(placement_target_cfg, placement_rng)`.

3. **Where object geometry dimensions are stored**:
   They are stored in `configs/object_geometry.generated.yaml` and loaded at runtime via `load_object_geometry_registry` in `src/franka_wrist_camera_scene/objects/geometry_registry.py`.

4. **Whether geometry dimensions are full dimensions, half-extents or local bounds**:
   They are stored as local bounds (`local_bbox_min`, `local_bbox_max`) and full dimensions (`local_bbox_size`) under each record.

5. **How the gripper usable aperture is represented**:
   It is derived from the task specification `PickPlaceTaskSpec` fields `open_finger_m` and `closed_finger_m`. Each finger has a range up to `open_finger_m = 0.04` m, representing a total opening width of `0.08` m.

6. **Where object mass currently comes from**:
   It comes from `physics_overrides` (specifically `target_mass`) parsed from the collection config in `src/franka_wrist_camera_scene/scene/tabletop.py`. If not provided, it defaults to the physical mass defined inside the USD asset.

7. **Whether static/dynamic friction materials are already configurable**:
   No, they are not configured or configurable in the current codebase.

8. **How receptacle inner usable bounds or placement affordance are represented**:
   Affordances are defined as strings in the catalog (`container` for bowls/boxes, `support` for trays). Inner bounds are not explicitly modeled; instead, the success check in `src/franka_wrist_camera_scene/episode/success.py` calculates a horizontal tolerance based on the outer bounding box size using `receptacle_xy_radius_from_bbox`.

9. **Where preflight validation currently runs**:
   Only simple directory existence checks run in `preflight_collection_output` within `scripts/collect.py` prior to launching the simulator.

10. **Why target-area episodes remain possible**:
    If `placement_target` is omitted or null in the configuration, `placement_context` resolves to `None`, which falls back to placing the target object directly on the table surface at `place_pos_local` rather than a receptacle.



## Preflight Matrix Summary

- **Total Objects**: 149
- **Accepted Objects**: 7 (variants with at least one feasible receptacle)
- **Rejected Oversized Objects**: 2
- **Rejected Missing-Geometry Objects**: 0
- **Supported Validated Pairs**: 7
- **Experimental Feasible Pairs**: 345
- **Rejected Pairs**: 8886


## Phase 11 & 13 — Strict Multi-Episode Validation Run & Physical Audit

We executed 6 consecutive episodes under strict validation mode (using seed `901`). All episodes placed supported objects into real receptacles.

### Validation Results Table

| Episode | Object Variant | Receptacle Variant | Receptacle USD | Success | Audit Classification | Success Metric |
|---------|----------------|--------------------|----------------|---------|----------------------|----------------|
| 1       | lime00         | box00              | objects/box/box00.usd | ✅ True | ACCEPTED             | inside_receptacle_center_approx |
| 2       | egg03          | box00              | objects/box/box00.usd | ✅ True | ACCEPTED             | inside_receptacle_center_approx |
| 3       | egg03          | box00              | objects/box/box00.usd | ✅ True | ACCEPTED             | inside_receptacle_center_approx |
| 4       | lime00         | box00              | objects/box/box00.usd | ✅ True | ACCEPTED             | inside_receptacle_center_approx |
| 5       | kiwi00         | bowl10             | objects/bowl/bowl10.usd | ✅ True | ACCEPTED             | inside_receptacle_center_approx |
| 6       | lime00         | box00              | objects/box/box00.usd | ✅ True | ACCEPTED             | inside_receptacle_center_approx |

- **No target-area episodes** were generated during this dataset configuration validation run.
- **Applied physics profiles** (such as `fcan03` mass of `0.15kg` and `top_grasp_depth_m` of `0.035m`, `apple01` `top_grasp_depth_m` of `0.045m`) were successfully resolved and injected from `configs/object_physics_profiles.yaml`.
- All generated MP4 videos and preview JPGs have been saved to `outputs/object_test_videos/007_smart_strict_collection/`.

---

## Phase 14 — Final Apple Regression

We executed one apple baseline episode separately in target-area regression mode (strict mode disabled):
- **Object**: `apple01`
- **Receptacle**: `None`
- **Seed**: `123`
- **Success**: ✅ True
- **Applied Grasp Depth**: `0.045m` (resolved from physics profiles)
- **Applied Mass**: Default from USD
- **Audit Classification**: ACCEPTED

---

## Conclusion & Readiness Decision

The smart preflight validation pipeline is **fully functional** and verified.
* All unit tests pass.
* Geometrically impossible pairs are rejected immediately before simulation (e.g. `box01` rejected on gripper limits).
* The resampling loop correctly samples feasible validated pairs when sampling is enabled.
* Physics profiles dynamically configure target assets.
* Target-area placement is strictly restricted to historical regression configs only.
