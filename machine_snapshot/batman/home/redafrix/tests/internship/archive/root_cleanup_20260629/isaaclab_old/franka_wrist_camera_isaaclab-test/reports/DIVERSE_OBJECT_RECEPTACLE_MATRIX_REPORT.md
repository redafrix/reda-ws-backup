# Diverse Object and Receptacle Matrix Report

## Starting state
- branch: object-integration-static-assets
- commit: 07dab834f1d5db2f56647c486ee00e75a17fbdfb
- status:

07dab83 (HEAD -> object-integration-static-assets, tag: checkpoint/upstream-master-integrated-20260615, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
43da87b feat: add geometry-aware deterministic table clutter
4a65eac (backup/object-integration-before-master-20260615_093855, backup/object-integration-before-finalized-master-20260615_104358) Add true receptacle-goal metadata, instruction generation, success mode, and exit watchdog
8cc8080 feat: use receptacle bottom clearance for placement release height
286fa2b fix: make receptacle placement success geometry-aware
6e2cb86 feat: add sampled placement receptacle target
441bebd Implement config-driven receptacle-goal mode for pick-place and add verified configs
src/franka_wrist_camera_scene/collection/pick_place.py:21:from franka_wrist_camera_scene.episode.success import pick_place_success
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
src/franka_wrist_camera_scene/collection/pick_place.py:135:        success_metric=getattr(policy.spec, "success_metric", "target_area_center"),
src/franka_wrist_camera_scene/collection/pick_place.py:202:    success = bool(pick_place_success(scene, policy.spec)[0].item())
src/franka_wrist_camera_scene/collection/pick_place.py:230:    placement_target_cfg = collection_cfg.get("placement_target")
src/franka_wrist_camera_scene/collection/pick_place.py:265:            if placement_target_cfg is not None:
src/franka_wrist_camera_scene/collection/pick_place.py:266:                placement_context = _load_collection_object_context(placement_target_cfg, placement_rng)
src/franka_wrist_camera_scene/collection/pick_place.py:311:                placement_target_pos_local=placement_receptacle_pos_local,
src/franka_wrist_camera_scene/collection/pick_place.py:312:                placement_target_local_bbox_min=placement_context.geometry.local_bbox_min if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:313:                placement_target_local_bbox_max=placement_context.geometry.local_bbox_max if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:330:                    placement_target_context=placement_context,
src/franka_wrist_camera_scene/collection/pick_place.py:331:                    placement_target_xy=placement_xy,
src/franka_wrist_camera_scene/collection/pick_place.py:409:                placement_target_category_id=placement_context.category_id if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:410:                placement_target_variant_id=placement_context.variant_id if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:411:                placement_target_label=placement_context.label if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:412:                placement_target_usd_path=placement_usd_path,
src/franka_wrist_camera_scene/collection/pick_place.py:413:                placement_target_grasp_strategy=placement_context.grasp_strategy if placement_context is not None else None,
src/franka_wrist_camera_scene/collection/pick_place.py:414:                placement_target_pos_local=placement_receptacle_pos_local,
src/franka_wrist_camera_scene/episode/recorder.py:44:    placement_target_category_id: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:45:    placement_target_variant_id: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:46:    placement_target_label: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:47:    placement_target_usd_path: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:48:    placement_target_grasp_strategy: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:49:    placement_target_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/recorder.py:53:    success_metric: str | None = None
src/franka_wrist_camera_scene/episode/recorder.py:183:            placement_target_category_id=self.placement_target_category_id,
src/franka_wrist_camera_scene/episode/recorder.py:184:            placement_target_variant_id=self.placement_target_variant_id,
src/franka_wrist_camera_scene/episode/recorder.py:185:            placement_target_label=self.placement_target_label,
src/franka_wrist_camera_scene/episode/recorder.py:186:            placement_target_usd_path=self.placement_target_usd_path,
src/franka_wrist_camera_scene/episode/recorder.py:187:            placement_target_grasp_strategy=self.placement_target_grasp_strategy,
src/franka_wrist_camera_scene/episode/recorder.py:188:            placement_target_pos_local=self.placement_target_pos_local,
src/franka_wrist_camera_scene/episode/recorder.py:192:            success_metric=self.success_metric,
src/franka_wrist_camera_scene/episode/success.py:41:def pick_place_success(
src/franka_wrist_camera_scene/episode/success.py:54:    if spec.placement_target_pos_local is not None:
src/franka_wrist_camera_scene/episode/success.py:57:            or spec.placement_target_local_bbox_min is None
src/franka_wrist_camera_scene/episode/success.py:58:            or spec.placement_target_local_bbox_max is None
src/franka_wrist_camera_scene/episode/success.py:62:        receptacle_pos_local = torch.tensor(spec.placement_target_pos_local, device=obj_pos_w.device).view(1, 3)
src/franka_wrist_camera_scene/episode/success.py:67:            bbox_min=spec.placement_target_local_bbox_min,
src/franka_wrist_camera_scene/episode/success.py:68:            bbox_max=spec.placement_target_local_bbox_max,
src/franka_wrist_camera_scene/episode/success.py:73:        receptacle_top_z = receptacle_pos_w[:, 2] + float(spec.placement_target_local_bbox_max[2])
src/franka_wrist_camera_scene/episode/success.py:74:        receptacle_bottom_z = receptacle_pos_w[:, 2] + float(spec.placement_target_local_bbox_min[2])
src/franka_wrist_camera_scene/episode/schema.py:38:    placement_target_category_id: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:39:    placement_target_variant_id: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:40:    placement_target_label: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:41:    placement_target_usd_path: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:42:    placement_target_grasp_strategy: str | None = None
src/franka_wrist_camera_scene/episode/schema.py:43:    placement_target_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/schema.py:47:    success_metric: str | None = None
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
src/franka_wrist_camera_scene/scene/clutter.py:218:    placement_target_context: CatalogObjectContext | None,
src/franka_wrist_camera_scene/scene/clutter.py:219:    placement_target_xy: tuple[float, float] | None,
src/franka_wrist_camera_scene/scene/clutter.py:238:    if placement_target_context is not None and placement_target_xy is not None:
src/franka_wrist_camera_scene/scene/clutter.py:241:                xy=placement_target_xy,
src/franka_wrist_camera_scene/scene/clutter.py:243:                    placement_target_context,
src/franka_wrist_camera_scene/scene/clutter.py:244:                    margin_m=float(clutter_cfg["placement_target_margin_m"]),
src/franka_wrist_camera_scene/scene/clutter.py:248:    elif placement_target_xy is not None:
src/franka_wrist_camera_scene/scene/clutter.py:251:                xy=placement_target_xy,
src/franka_wrist_camera_scene/scene/clutter.py:254:                    margin_m=float(clutter_cfg["placement_target_margin_m"]),
src/franka_wrist_camera_scene/scene/clutter.py:318:    placement_target_context: CatalogObjectContext | None,
src/franka_wrist_camera_scene/scene/clutter.py:319:    placement_target_xy: tuple[float, float] | None,
src/franka_wrist_camera_scene/scene/clutter.py:347:                placement_target_context=placement_target_context,
src/franka_wrist_camera_scene/scene/clutter.py:348:                placement_target_xy=placement_target_xy,
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:51:            or self.spec.placement_target_local_bbox_min is None
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:56:        receptacle_bottom_z = receptacle_root_w[:, 2] + float(self.spec.placement_target_local_bbox_min[2])
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:142:            if self.spec.placement_target_pos_local is None:
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:145:                receptacle_local = torch.tensor(self.spec.placement_target_pos_local, device=self._device)
src/franka_wrist_camera_scene/tasks/pick_place.py:18:    success_metric: str = "target_area_center"
src/franka_wrist_camera_scene/tasks/pick_place.py:36:    placement_target_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:37:    placement_target_local_bbox_min: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:38:    placement_target_local_bbox_max: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/tasks/pick_place.py:76:    placement_target_pos_local: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:77:    placement_target_local_bbox_min: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:78:    placement_target_local_bbox_max: tuple[float, float, float] | None = None,
src/franka_wrist_camera_scene/tasks/pick_place.py:95:        placement_target_local_bbox_min
src/franka_wrist_camera_scene/tasks/pick_place.py:96:        if placement_target_local_bbox_min is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:97:        else base_spec.placement_target_local_bbox_min
src/franka_wrist_camera_scene/tasks/pick_place.py:100:        placement_target_local_bbox_max
src/franka_wrist_camera_scene/tasks/pick_place.py:101:        if placement_target_local_bbox_max is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:102:        else base_spec.placement_target_local_bbox_max
src/franka_wrist_camera_scene/tasks/pick_place.py:105:        placement_target_pos_local
src/franka_wrist_camera_scene/tasks/pick_place.py:106:        if placement_target_pos_local is not None
src/franka_wrist_camera_scene/tasks/pick_place.py:107:        else base_spec.placement_target_pos_local
src/franka_wrist_camera_scene/tasks/pick_place.py:171:        placement_target_pos_local=resolved_placement_pos,
src/franka_wrist_camera_scene/tasks/pick_place.py:172:        placement_target_local_bbox_min=resolved_placement_bbox_min,
src/franka_wrist_camera_scene/tasks/pick_place.py:173:        placement_target_local_bbox_max=resolved_placement_bbox_max,
src/franka_wrist_camera_scene/export/ila.py:71:        "placement_target_category_id": meta.get("placement_target_category_id"),
src/franka_wrist_camera_scene/export/ila.py:72:        "placement_target_variant_id": meta.get("placement_target_variant_id"),
src/franka_wrist_camera_scene/export/ila.py:73:        "placement_target_label": meta.get("placement_target_label"),
src/franka_wrist_camera_scene/export/ila.py:74:        "placement_target_usd_path": meta.get("placement_target_usd_path"),
src/franka_wrist_camera_scene/export/ila.py:75:        "placement_target_grasp_strategy": meta.get("placement_target_grasp_strategy"),
src/franka_wrist_camera_scene/export/ila.py:76:        "placement_target_pos_local": meta.get("placement_target_pos_local"),
scripts/inspect_target_sampling.py:32:        choices=("target_object", "placement_target", "clutter"),
scripts/inspect_collection.py:53:        "placement_target_category_id": meta.get("placement_target_category_id"),
scripts/inspect_collection.py:54:        "placement_target_variant_id": meta.get("placement_target_variant_id"),
scripts/inspect_collection.py:55:        "placement_target_label": meta.get("placement_target_label"),
scripts/inspect_collection.py:56:        "placement_target_usd_path": meta.get("placement_target_usd_path"),
scripts/inspect_collection.py:57:        "placement_target_grasp_strategy": meta.get("placement_target_grasp_strategy"),
scripts/inspect_collection.py:58:        "placement_target_pos_local": (
scripts/inspect_collection.py:59:            tuple(meta["placement_target_pos_local"])
scripts/inspect_collection.py:60:            if meta.get("placement_target_pos_local") is not None
scripts/inspect_collection.py:113:        placement_variant_id = item.get("placement_target_variant_id", "none") or "none"
scripts/inspect_collection.py:114:        placement_label = item.get("placement_target_label", "none") or "none"
scripts/inspect_collection.py:142:    placement_target_pos_local = summary["placement_target_pos_local"]
scripts/inspect_collection.py:147:            tuple(round(float(x), 4) for x in placement_target_pos_local)
scripts/inspect_collection.py:148:            if placement_target_pos_local is not None
scripts/debug_scene.py:93:from franka_wrist_camera_scene.episode.success import pick_place_success, reaching_success
scripts/debug_scene.py:165:                    success = pick_place_success(scene, policy.spec)
scripts/debug_scene.py:235:        placement_target_cfg = collection_cfg["placement_target"]
scripts/debug_scene.py:238:            catalog_config=placement_target_cfg["catalog_config"],
scripts/debug_scene.py:239:            geometry_config=placement_target_cfg["geometry_config"],
scripts/debug_scene.py:240:            category_id=placement_target_cfg["category_id"],
scripts/debug_scene.py:241:            variant_id=placement_target_cfg["variant_id"],
scripts/debug_scene.py:242:            split=placement_target_cfg["split"],
scripts/debug_scene.py:243:            role=placement_target_cfg["role"],
scripts/debug_scene.py:244:            required_affordances=tuple(placement_target_cfg["required_affordances"]),
scripts/debug_scene.py:245:            required_grasp_strategy=placement_target_cfg["required_grasp_strategy"],
scripts/debug_scene.py:268:            placement_target_pos_local=placement_receptacle_pos_local,
scripts/debug_scene.py:269:            placement_target_local_bbox_min=placement_context.geometry.local_bbox_min,
scripts/debug_scene.py:270:            placement_target_local_bbox_max=placement_context.geometry.local_bbox_max,
scripts/debug_scene.py:281:            placement_target_context=placement_context,
scripts/debug_scene.py:282:            placement_target_xy=(
tests/test_pick_place_task.py:43:            placement_target_pos_local=(0.60, 0.25, 1.07),
tests/test_pick_place_task.py:44:            placement_target_local_bbox_min=(-0.07, -0.07, -0.02),
tests/test_pick_place_task.py:45:            placement_target_local_bbox_max=(0.07, 0.07, 0.06),
tests/test_pick_place_task.py:52:        self.assertEqual(spec.placement_target_pos_local, (0.60, 0.25, 1.07))
tests/test_pick_place_task.py:63:                placement_target_pos_local=(0.60, 0.25, 1.07),
tests/test_success.py:15:    pick_place_success,
tests/test_success.py:31:    def test_pick_place_success_receptacle(self) -> None:
tests/test_success.py:43:            placement_target_pos_local=(0.5, 0.1, 1.0),
tests/test_success.py:46:            placement_target_local_bbox_min=(-0.1, -0.1, -0.05),
tests/test_success.py:47:            placement_target_local_bbox_max=(0.1, 0.1, 0.05),
tests/test_success.py:56:        success = pick_place_success(mock_scene, spec)
tests/test_success.py:61:        success = pick_place_success(mock_scene, spec)
tests/test_success.py:66:        success = pick_place_success(mock_scene, spec)
tests/test_success.py:71:        success = pick_place_success(mock_scene, spec)
tests/test_clutter_sampling.py:1:"""Unit tests for geometry-aware clutter sampling."""
configs/local_isaac45/upstream_sampled_receptacle_smoke.yaml:24:placement_target:
configs/local_isaac45/receptacle_tray_tray04_apple01_integrated.yaml:25:placement_target:
configs/local_isaac45/upstream_clutter_smoke.yaml:24:placement_target:
configs/local_isaac45/upstream_clutter_smoke.yaml:46:  placement_target_margin_m: 0.035
configs/collection.yaml:24:placement_target:
configs/collection.yaml:46:  placement_target_margin_m: 0.035
- video_run_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix

## Step 1 — Inspect the Geometry-Aware Success Path

### Answers to Trace Questions
- **Is geometry-aware receptacle success actually executed?**
  Yes. When `placement_target_pos_local` is specified (not None), the actual success evaluation function `pick_place_success` in `src/franka_wrist_camera_scene/episode/success.py` executes the geometry-aware branch rather than falling back to the target-area metric.
- **Where is success_metric assigned?**
  - Originally, it was set as a default value (`"target_area_center"`) on the `PickPlaceTaskSpec` class.
  - It is recorded in `meta.json` via the recorder using `policy.spec.success_metric`.
  - The metadata fix in `make_pick_place_episode_spec` in `src/franka_wrist_camera_scene/tasks/pick_place.py` resolves and overwrites this to `"on_receptacle_center"` (for trays) or `"inside_receptacle_center_approx"` (for bowls/boxes) if `resolved_placement_pos` is provided.
- **Is target_area_center only a stale metadata default?**
  Yes, for receptacle tasks, the string `"target_area_center"` was purely a stale metadata default from `PickPlaceTaskSpec` and did not control the actual geometry-aware checking logic.
- **Does the success function use receptacle geometry, bounds, or affordance?**
  Yes. It calls `receptacle_xy_radius_from_bbox` with the placement target's local bounding box bounds (`placement_target_local_bbox_min`, `placement_target_local_bbox_max`) to calculate a dynamic XY distance tolerance. It also uses the bounding box bounds to perform vertical correctness checks on the object's bottom Z coordinate.

## Step 3 — Selection Report

| Role | Category | Variant | USD Path | Dimensions (m) | Mass (kg) | Grasp | Affordances | Why Selected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Object | apple | apple01 | apple/apple01.usd | [0.085, 0.0811, 0.0829] | N/A | center_top | ['pickable', 'reachable'] | Visibly distinct red fruit placed in a deep container |
| Receptacle | bowl | bowl08 | bowl/bowl08.usd | [0.15, 0.15, 0.0617] | N/A | unsupported | ['reachable', 'container'] | Receptacle target |
| Object | avocado | avocado02 | avocado/avocado02.usd | [0.0522, 0.0517, 0.08] | N/A | center_top | ['pickable', 'reachable'] | Irregular green fruit placed in a shallow wide container |
| Receptacle | bowl | bowl01 | bowl/bowl01.usd | [0.15, 0.15, 0.0657] | N/A | unsupported | ['reachable', 'container'] | Receptacle target |
| Object | can | fcan03 | can/fcan03.usd | [0.0695, 0.0695, 0.11] | N/A | center_top | ['pickable', 'reachable'] | Cylindrical soda can placed on a flat support surface |
| Receptacle | tray | tray04 | tray/tray04.usd | [0.25, 0.15, 0.0425] | N/A | unsupported | ['reachable', 'support'] | Receptacle target |
| Object | onion | onion00 | onion/onion00.usd | [0.0436, 0.0432, 0.06] | N/A | center_top | ['pickable', 'reachable'] | Narrow onion object placed inside a deep curved bowl |
| Receptacle | bowl | bowl07 | bowl/bowl07.usd | [0.15, 0.15, 0.0496] | N/A | unsupported | ['reachable', 'container'] | Receptacle target |
| Object | kiwi | kiwi00 | kiwi/kiwi00.usd | [0.0388, 0.0435, 0.055] | N/A | center_top | ['pickable', 'reachable'] | Small fuzzy brown fruit placed in a wide deep bowl |
| Receptacle | bowl | bowl10 | bowl/bowl10.usd | [0.15, 0.15, 0.0699] | N/A | unsupported | ['reachable', 'container'] | Receptacle target |
| Object | lime | lime00 | lime/lime00.usd | [0.0572, 0.0594, 0.07] | N/A | center_top | ['pickable', 'reachable'] | Small narrow lime object placed inside a rectangular open box container |
| Receptacle | box | box00 | box/box00.usd | [0.2423, 0.1222, 0.12] | N/A | unsupported | ['reachable', 'container'] | Receptacle target |

## Step 5 & 6 — Diverse Matrix Results

### Run 01: pair1_apple_bowl.yaml
- **Instruction**: pick up the apple and place it in the bowl
- **Success**: True
- **Success Metric**: inside_receptacle_center_approx
- **Object Category**: apple
- **Object Variant**: apple01
- **Object USD Path**: objects/apple/apple01.usd
- **Placement Target Category**: bowl
- **Placement Target Variant**: bowl08
- **Placement Target USD Path**: objects/bowl/bowl08.usd
- **Object Position (Local)**: [0.6, -0.18, 1.097451]
- **Placement-Target Position (Local)**: [0.52, 0.26, 1.0868470000000001]
- **Place Position (Local)**: [0.52, 0.26, 1.097451]
- **Trajectory SHA256**: 23bdb798eb4e6f1ed6840dcc499cdeae6f4da9fa1035c82642e7a90f51888dd0
- **Agent First-Frame SHA256**: 8b5e621b2847cc47de5659cbd46575bbb94f701882032726d27ec16919d6fc4d
- **Wrist First-Frame SHA256**: 423032cd1cd33367d77f2f7daa2dfd65196e32e84572844af1e4877a8e8a593b
- **Video Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/01_apple01_into_bowl08_SUCCESS_agent_plus_wrist.mp4
- **Preview Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/01_apple01_into_bowl08_SUCCESS_agent_plus_wrist.preview.jpg

### Run 02: pair2_avocado_bowl.yaml
- **Instruction**: pick up the avocado and place it in the bowl
- **Success**: True
- **Success Metric**: inside_receptacle_center_approx
- **Object Category**: avocado
- **Object Variant**: avocado02
- **Object USD Path**: objects/avocado/avocado02.usd
- **Placement Target Category**: bowl
- **Placement Target Variant**: bowl01
- **Placement Target USD Path**: objects/bowl/bowl01.usd
- **Object Position (Local)**: [0.5499999999999999, -0.13, 1.096]
- **Placement-Target Position (Local)**: [0.5900000000000001, 0.19, 1.088858]
- **Place Position (Local)**: [0.5900000000000001, 0.19, 1.096]
- **Trajectory SHA256**: 3631fde0d046d7bce3ea7ecb452d130f3374aadcd7f6ac4b51770310944599aa
- **Agent First-Frame SHA256**: 0e13048c37a5123daf0f0929fba4f4d3eaf8ffd6d8fb6a79f3edfbb45700aea4
- **Wrist First-Frame SHA256**: 3b850fa07df31e6947d924b56fc594ca313f3a6b3ae33cbe159210b92c635c45
- **Video Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/02_avocado02_into_bowl01_SUCCESS_agent_plus_wrist.mp4
- **Preview Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/02_avocado02_into_bowl01_SUCCESS_agent_plus_wrist.preview.jpg

### Run 03: pair3_can_tray.yaml
- **Instruction**: pick up the can and place it in the tray
- **Success**: False
- **Success Metric**: on_receptacle_center
- **Object Category**: can
- **Object Variant**: fcan03
- **Object USD Path**: objects/can/fcan03.usd
- **Placement Target Category**: tray
- **Placement Target Variant**: tray04
- **Placement Target USD Path**: objects/tray/tray04.usd
- **Object Position (Local)**: [0.6, -0.18, 1.111]
- **Placement-Target Position (Local)**: [0.51, 0.25, 1.07725]
- **Place Position (Local)**: [0.51, 0.25, 1.111]
- **Trajectory SHA256**: 28cdc2fcff2c2e724562d02ddcbfcf3cb5bc597d5f4097a91726dd670fe8db81
- **Agent First-Frame SHA256**: fd553a316141027264425cbdba14375565692af955b7c65d1e2e250d3c7769f1
- **Wrist First-Frame SHA256**: 9341a3dcdf3144e0880de68d06043079447fb8c22116c05664481cfa031cda4b
- **Video Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/03_fcan03_into_tray04_FAIL_agent_plus_wrist.mp4
- **Preview Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/03_fcan03_into_tray04_FAIL_agent_plus_wrist.preview.jpg

### Run 04: pair4_box_bowl.yaml
- **Instruction**: pick up the onion and place it in the bowl
- **Success**: True
- **Success Metric**: inside_receptacle_center_approx
- **Object Category**: onion
- **Object Variant**: onion00
- **Object USD Path**: objects/onion/onion00.usd
- **Placement Target Category**: bowl
- **Placement Target Variant**: bowl07
- **Placement Target USD Path**: objects/bowl/bowl07.usd
- **Object Position (Local)**: [0.5599999999999999, -0.19, 1.086]
- **Placement-Target Position (Local)**: [0.5800000000000001, 0.27, 1.080821]
- **Place Position (Local)**: [0.5800000000000001, 0.27, 1.086]
- **Trajectory SHA256**: 21ccfc78defea0cef26919ef34e8609642372f0ba2376d2873cd0b3d104ac182
- **Agent First-Frame SHA256**: fcb79b192478d50cb48144ecb64bffaf5692b3ee7fafaf94cec56de473d8489b
- **Wrist First-Frame SHA256**: 8847feb96f4c9b77e9d79498512c39d81cc3029a4fe45dfa1a18902536a136ee
- **Video Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/04_onion00_into_bowl07_SUCCESS_agent_plus_wrist.mp4
- **Preview Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/04_onion00_into_bowl07_SUCCESS_agent_plus_wrist.preview.jpg

### Run 05: pair5_kiwi_bowl.yaml
- **Instruction**: pick up the kiwi and place it in the bowl
- **Success**: True
- **Success Metric**: inside_receptacle_center_approx
- **Object Category**: kiwi
- **Object Variant**: kiwi00
- **Object USD Path**: objects/kiwi/kiwi00.usd
- **Placement Target Category**: bowl
- **Placement Target Variant**: bowl10
- **Placement Target USD Path**: objects/bowl/bowl10.usd
- **Object Position (Local)**: [0.61, -0.14, 1.0835000000000001]
- **Placement-Target Position (Local)**: [0.5, 0.18, 1.090954]
- **Place Position (Local)**: [0.5, 0.18, 1.0835000000000001]
- **Trajectory SHA256**: b9b04778e52a2ee3ed7737dd45cac67344821861ee0c4104995e8f6d516ddc8a
- **Agent First-Frame SHA256**: 3643d4df5740dcd0bf639c21e74f3514b0d74d7e827891395a81cb7b06548b2b
- **Wrist First-Frame SHA256**: 44b62d6ec056e13eea52fa6027aca9aea71f7c137d6c41680e3a22c9d027231d
- **Video Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/05_kiwi00_into_bowl10_SUCCESS_agent_plus_wrist.mp4
- **Preview Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/05_kiwi00_into_bowl10_SUCCESS_agent_plus_wrist.preview.jpg

### Run 06: pair6_beer_box.yaml
- **Instruction**: pick up the lime and place it in the box
- **Success**: True
- **Success Metric**: inside_receptacle_center_approx
- **Object Category**: lime
- **Object Variant**: lime00
- **Object USD Path**: objects/lime/lime00.usd
- **Placement Target Category**: box
- **Placement Target Variant**: box00
- **Placement Target USD Path**: objects/box/box00.usd
- **Object Position (Local)**: [0.5399999999999999, -0.12, 1.091]
- **Placement-Target Position (Local)**: [0.6000000000000001, 0.16999999999999998, 1.1161320000000001]
- **Place Position (Local)**: [0.6000000000000001, 0.16999999999999998, 1.091]
- **Trajectory SHA256**: 92a0cbf82c7652f8414007413cc262da4a2f44cc7765b381eae4bf07b2b1a5ef
- **Agent First-Frame SHA256**: e5691e13a03a7cee4d25d2a7a540d83499924d0d1296e69add843ccaa5d4c4f6
- **Wrist First-Frame SHA256**: 889b4ad9755e2848c1360920b97c1262a9f4db1ef6dec620686330c17b0bea40
- **Video Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/06_lime00_into_box00_SUCCESS_agent_plus_wrist.mp4
- **Preview Path**: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix/06_lime00_into_box00_SUCCESS_agent_plus_wrist.preview.jpg


## Step 6 — Diversity Validation Checks

- **Validation Status**: PASSED
- **Checks**: All trajectory and camera hashes are distinct. All object/receptacle variants are distinct.
