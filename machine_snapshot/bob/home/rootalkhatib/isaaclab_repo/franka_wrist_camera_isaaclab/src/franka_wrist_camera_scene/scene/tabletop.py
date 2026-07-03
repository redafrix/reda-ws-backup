"""Isaac Lab scene configuration for a Franka tabletop setup with cameras."""

from __future__ import annotations

import copy

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sensors import CameraCfg
from isaaclab.utils.configclass import configclass
from isaaclab_assets import FRANKA_PANDA_HIGH_PD_CFG

from ..settings import (
    CAMERA_HEIGHT,
    CAMERA_WIDTH,
    ROBOT_BASE_POS,
    TABLE_COLOR,
    TABLE_HEIGHT_M,
    TABLE_SIZE,
)
from franka_wrist_camera_scene.scene.clutter import ClutterObjectSpec
from franka_wrist_camera_scene.scene.object_context import CatalogObjectContext

PICK_PLACE_CLUTTER_SLOT_COUNT = 8
REACHING_CLUTTER_SLOT_COUNT = 12
PARKED_ASSET_POS = (100.0, 100.0, -10.0)
WRIST_CAMERA_ROT_XYZW = (-0.0493, 0.0493, -0.7054, 0.7054)
AGENT_CAMERA_ROT_XYZW = (-0.33316794, 0.0, 0.94286750, 0.0)
RGB_CAMERA_DATA_TYPES = ["rgb"]
RGBD_CAMERA_DATA_TYPES = ["rgb", "distance_to_image_plane"]
FRANKA_TOP_DOWN_READY_JOINT_POS = {
    "panda_joint1": 0.0,
    "panda_joint2": -0.569,
    "panda_joint3": 0.0,
    "panda_joint4": -2.810,
    "panda_joint5": 0.0,
    "panda_joint6": 2.35619,
    "panda_joint7": -2.395,
    "panda_finger_joint.*": 0.04,
}
FRANKA_REACHING_READY_JOINT_POS = {
    **FRANKA_TOP_DOWN_READY_JOINT_POS,
    "panda_joint7": -2.2751,
}


def pinhole_camera_cfg(clipping_range: tuple[float, float]) -> sim_utils.PinholeCameraCfg:
    """Return a compact RGB-D pinhole camera model."""
    return sim_utils.PinholeCameraCfg(
        focal_length=18.0,
        focus_distance=0.55,
        horizontal_aperture=20.955,
        clipping_range=clipping_range,
    )


def camera_data_types(record_depth: bool) -> list[str]:
    """Return camera data types required by the collection config."""
    return list(RGBD_CAMERA_DATA_TYPES if record_depth else RGB_CAMERA_DATA_TYPES)


def configure_scene_cameras(
    scene_cfg,
    *,
    width: int,
    height: int,
    record_depth: bool,
    camera_fps: int,
) -> None:
    """Apply collection camera resolution, data types, and update period."""
    if width <= 0 or height <= 0:
        raise ValueError(f"Camera resolution must be positive, got width={width}, height={height}.")
    if camera_fps <= 0:
        raise ValueError(f"camera_fps must be positive, got {camera_fps}.")

    data_types = camera_data_types(record_depth)
    update_period = 1.0 / float(camera_fps)
    for camera_cfg in (scene_cfg.agent_camera, scene_cfg.wrist_camera):
        camera_cfg.width = width
        camera_cfg.height = height
        camera_cfg.data_types = list(data_types)
        camera_cfg.update_period = update_period


def static_clutter_slot_cfg(index: int) -> RigidObjectCfg:
    return RigidObjectCfg(
        prim_path=f"{{ENV_REGEX_NS}}/ClutterObject{index}",
        spawn=sim_utils.UsdFileCfg(
            usd_path="",
            rigid_props=sim_utils.RigidBodyPropertiesCfg(kinematic_enabled=True, disable_gravity=True),
            collision_props=sim_utils.CollisionPropertiesCfg(),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.0, 0.0, 0.0)),
    )


@configclass
class TabletopFrankaSceneCfg(InteractiveSceneCfg):
    """Tabletop scene with a Franka Panda and two camera sensors."""

    table = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/Table",
        spawn=sim_utils.CuboidCfg(
            size=TABLE_SIZE,
            collision_props=sim_utils.CollisionPropertiesCfg(),
            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=TABLE_COLOR),
        ),
        # Cuboid origin is at its center; keep TABLE_HEIGHT_M as the tabletop z.
        init_state=AssetBaseCfg.InitialStateCfg(pos=(0.45, 0.0, TABLE_HEIGHT_M - 0.5 * TABLE_SIZE[2])),
    )

    dome_light = AssetBaseCfg(
        prim_path="/World/Light",
        spawn=sim_utils.DomeLightCfg(intensity=900.0, color=(0.9, 0.9, 0.9)),
    )

    robot: ArticulationCfg = FRANKA_PANDA_HIGH_PD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
    robot.spawn.fix_base = True
    robot.init_state.pos = ROBOT_BASE_POS
    robot.init_state.joint_pos = FRANKA_TOP_DOWN_READY_JOINT_POS

    target_cube = RigidObjectCfg(
        prim_path="{ENV_REGEX_NS}/TargetCube",
        spawn=sim_utils.UsdFileCfg(
            usd_path="",
            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
            collision_props=sim_utils.CollisionPropertiesCfg(),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.58, -0.16, TABLE_HEIGHT_M + 0.05)),
    )

    wrist_camera = CameraCfg(
        prim_path="{ENV_REGEX_NS}/Robot/panda_hand/wrist_rgbd_camera",
        update_period=1.0 / 30.0,
        height=CAMERA_HEIGHT,
        width=CAMERA_WIDTH,
        data_types=["rgb"],
        update_latest_camera_pose=True,
        spawn=pinhole_camera_cfg(clipping_range=(0.02, 4.0)),
        offset=CameraCfg.OffsetCfg(
            pos=(-0.042, 0.0, 0.020),
            rot=WRIST_CAMERA_ROT_XYZW,
            convention="ros",
        ),
    )

    agent_camera = CameraCfg(
        prim_path="{ENV_REGEX_NS}/AgentViewCamera",
        update_period=1.0 / 30.0,
        height=CAMERA_HEIGHT,
        width=CAMERA_WIDTH,
        data_types=["rgb"],
        spawn=pinhole_camera_cfg(clipping_range=(0.05, 25.0)),
        offset=CameraCfg.OffsetCfg(
            pos=(1.4186131747, 0.0, 1.7603500240),
            rot=AGENT_CAMERA_ROT_XYZW,
            convention="world",
        ),
    )


@configclass
class PickPlaceTabletopFrankaSceneCfg(TabletopFrankaSceneCfg):
    """Tabletop scene with a sampled placement receptacle."""

    place_receptacle = RigidObjectCfg(
        prim_path="{ENV_REGEX_NS}/PlaceReceptacle",
        spawn=sim_utils.UsdFileCfg(
            usd_path="",
            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
            collision_props=sim_utils.CollisionPropertiesCfg(),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.55, 0.22, TABLE_HEIGHT_M + 0.05)),
    )

    clutter_0 = static_clutter_slot_cfg(0)
    clutter_1 = static_clutter_slot_cfg(1)
    clutter_2 = static_clutter_slot_cfg(2)
    clutter_3 = static_clutter_slot_cfg(3)
    clutter_4 = static_clutter_slot_cfg(4)
    clutter_5 = static_clutter_slot_cfg(5)
    clutter_6 = static_clutter_slot_cfg(6)
    clutter_7 = static_clutter_slot_cfg(7)


@configclass
class ReachingClutterTabletopFrankaSceneCfg(TabletopFrankaSceneCfg):
    """Tabletop reaching scene with dense static distractors."""

    clutter_0 = static_clutter_slot_cfg(0)
    clutter_1 = static_clutter_slot_cfg(1)
    clutter_2 = static_clutter_slot_cfg(2)
    clutter_3 = static_clutter_slot_cfg(3)
    clutter_4 = static_clutter_slot_cfg(4)
    clutter_5 = static_clutter_slot_cfg(5)
    clutter_6 = static_clutter_slot_cfg(6)
    clutter_7 = static_clutter_slot_cfg(7)
    clutter_8 = static_clutter_slot_cfg(8)
    clutter_9 = static_clutter_slot_cfg(9)
    clutter_10 = static_clutter_slot_cfg(10)
    clutter_11 = static_clutter_slot_cfg(11)


def _reaching_clutter_slots(scene_cfg: ReachingClutterTabletopFrankaSceneCfg) -> tuple[AssetBaseCfg, ...]:
    return (
        scene_cfg.clutter_0,
        scene_cfg.clutter_1,
        scene_cfg.clutter_2,
        scene_cfg.clutter_3,
        scene_cfg.clutter_4,
        scene_cfg.clutter_5,
        scene_cfg.clutter_6,
        scene_cfg.clutter_7,
        scene_cfg.clutter_8,
        scene_cfg.clutter_9,
        scene_cfg.clutter_10,
        scene_cfg.clutter_11,
    )


def _pick_place_clutter_slots(scene_cfg: PickPlaceTabletopFrankaSceneCfg) -> tuple[AssetBaseCfg, ...]:
    return (
        scene_cfg.clutter_0,
        scene_cfg.clutter_1,
        scene_cfg.clutter_2,
        scene_cfg.clutter_3,
        scene_cfg.clutter_4,
        scene_cfg.clutter_5,
        scene_cfg.clutter_6,
        scene_cfg.clutter_7,
    )


def make_tabletop_scene_cfg(
    object_context: CatalogObjectContext,
    num_envs: int = 1,
    env_spacing: float = 2.5,
) -> TabletopFrankaSceneCfg:
    """Create a tabletop scene configuration with the specified target object."""
    scene_cfg = TabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
    scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
    return scene_cfg


def make_reaching_tabletop_scene_cfg(
    object_context: CatalogObjectContext,
    clutter_specs: tuple[ClutterObjectSpec, ...],
    num_envs: int = 1,
    env_spacing: float = 2.5,
) -> ReachingClutterTabletopFrankaSceneCfg:
    """Create a reaching scene with a target object and static distractors."""
    if len(clutter_specs) < 1 or len(clutter_specs) > REACHING_CLUTTER_SLOT_COUNT:
        raise ValueError(
            f"Expected 1 to {REACHING_CLUTTER_SLOT_COUNT} reaching clutter specs, "
            f"got {len(clutter_specs)}."
        )

    scene_cfg = ReachingClutterTabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
    scene_cfg.robot = copy.deepcopy(scene_cfg.robot)
    scene_cfg.robot.init_state = copy.deepcopy(scene_cfg.robot.init_state)
    scene_cfg.robot.init_state.joint_pos = dict(FRANKA_REACHING_READY_JOINT_POS)
    scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
    clutter_slots = _reaching_clutter_slots(scene_cfg)

    for clutter_spec, clutter_slot in zip(clutter_specs, clutter_slots[:len(clutter_specs)], strict=True):
        clutter_slot.spawn.usd_path = str(clutter_spec.context.usd_path)
        clutter_slot.init_state.pos = clutter_spec.pos_local

    parked_context = clutter_specs[0].context
    for clutter_slot in clutter_slots[len(clutter_specs):]:
        clutter_slot.spawn.usd_path = str(parked_context.usd_path)
        clutter_slot.init_state.pos = PARKED_ASSET_POS

    for clutter_slot in clutter_slots:
        if not clutter_slot.spawn.usd_path:
            raise RuntimeError("All reaching clutter slots must be patched with concrete USD paths.")

    return scene_cfg


def make_reaching_asset_bank_scene_cfg(
    target_usd_paths: dict[str, str],
    clutter_usd_paths: dict[str, str],
    initial_target_name: str,
    initial_clutter_names: tuple[str, ...],
    initial_clutter_specs: tuple[ClutterObjectSpec, ...],
    num_envs: int = 1,
    env_spacing: float = 2.5,
) -> ReachingClutterTabletopFrankaSceneCfg:
    """Create a reaching scene with all sampled assets spawned once."""
    if len(initial_clutter_names) != len(initial_clutter_specs):
        raise ValueError(
            "Initial clutter names/specs length mismatch: "
            f"names={len(initial_clutter_names)}, specs={len(initial_clutter_specs)}."
        )
    if not initial_clutter_specs:
        raise ValueError("Reaching asset-bank scene requires at least one initial clutter spec.")

    scene_cfg = ReachingClutterTabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
    scene_cfg.robot = copy.deepcopy(scene_cfg.robot)
    scene_cfg.robot.init_state = copy.deepcopy(scene_cfg.robot.init_state)
    scene_cfg.robot.init_state.joint_pos = dict(FRANKA_REACHING_READY_JOINT_POS)
    scene_cfg.target_cube.spawn.usd_path = target_usd_paths[initial_target_name]

    clutter_slots = _reaching_clutter_slots(scene_cfg)
    for clutter_name, clutter_spec, clutter_slot in zip(
        initial_clutter_names,
        initial_clutter_specs,
        clutter_slots[:len(initial_clutter_specs)],
        strict=True,
    ):
        clutter_slot.spawn.usd_path = clutter_usd_paths[clutter_name]
        clutter_slot.init_state.pos = clutter_spec.pos_local

    parked_context = initial_clutter_specs[0].context
    for clutter_slot in clutter_slots[len(initial_clutter_specs):]:
        clutter_slot.spawn.usd_path = str(parked_context.usd_path)
        clutter_slot.init_state.pos = PARKED_ASSET_POS

    for entity_name, usd_path in target_usd_paths.items():
        if entity_name == "target_cube":
            continue
        setattr(scene_cfg, entity_name, make_rigid_usd_object_cfg(entity_name, usd_path))

    base_clutter_names = {f"clutter_{slot_index}" for slot_index in range(REACHING_CLUTTER_SLOT_COUNT)}
    for entity_name, usd_path in clutter_usd_paths.items():
        if entity_name in base_clutter_names:
            continue
        setattr(scene_cfg, entity_name, make_static_usd_object_cfg(entity_name, usd_path))

    return scene_cfg


def make_pick_place_tabletop_scene_cfg(
    object_context: CatalogObjectContext,
    placement_context: CatalogObjectContext,
    placement_pos_local: tuple[float, float, float],
    clutter_specs: tuple[ClutterObjectSpec, ...],
    num_envs: int = 1,
    env_spacing: float = 2.5,
) -> PickPlaceTabletopFrankaSceneCfg:
    """Create a pick-place scene with a sampled target object and receptacle."""
    if len(clutter_specs) != PICK_PLACE_CLUTTER_SLOT_COUNT:
        raise ValueError(
            f"Expected {PICK_PLACE_CLUTTER_SLOT_COUNT} clutter specs, "
            f"got {len(clutter_specs)}."
        )

    scene_cfg = PickPlaceTabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
    scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
    scene_cfg.place_receptacle.spawn.usd_path = str(placement_context.usd_path)
    scene_cfg.place_receptacle.init_state.pos = placement_pos_local

    clutter_slots = (
        scene_cfg.clutter_0,
        scene_cfg.clutter_1,
        scene_cfg.clutter_2,
    )

    for clutter_spec, clutter_slot in zip(clutter_specs, clutter_slots, strict=True):
        clutter_slot.spawn.usd_path = str(clutter_spec.context.usd_path)
        clutter_slot.init_state.pos = clutter_spec.pos_local

    for clutter_slot in clutter_slots:
        if not clutter_slot.spawn.usd_path:
            raise RuntimeError("All clutter slots must be patched with concrete USD paths.")

    return scene_cfg


def make_rigid_usd_object_cfg(
    entity_name: str,
    usd_path: str,
    pos: tuple[float, float, float] = PARKED_ASSET_POS,
) -> RigidObjectCfg:
    return RigidObjectCfg(
        prim_path=f"{{ENV_REGEX_NS}}/{entity_name}",
        spawn=sim_utils.UsdFileCfg(
            usd_path=usd_path,
            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
            collision_props=sim_utils.CollisionPropertiesCfg(),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=pos),
    )


def make_static_usd_object_cfg(
    entity_name: str,
    usd_path: str,
    pos: tuple[float, float, float] = PARKED_ASSET_POS,
) -> RigidObjectCfg:
    return RigidObjectCfg(
        prim_path=f"{{ENV_REGEX_NS}}/{entity_name}",
        spawn=sim_utils.UsdFileCfg(
            usd_path=usd_path,
            rigid_props=sim_utils.RigidBodyPropertiesCfg(kinematic_enabled=True, disable_gravity=True),
            collision_props=sim_utils.CollisionPropertiesCfg(),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=pos),
    )


def make_pick_place_asset_bank_scene_cfg(
    target_usd_paths: dict[str, str],
    receptacle_usd_paths: dict[str, str],
    clutter_usd_paths: dict[str, str],
    initial_target_name: str,
    initial_receptacle_name: str,
    initial_clutter_names: tuple[str, ...],
    initial_receptacle_pos: tuple[float, float, float],
    initial_clutter_specs: tuple[ClutterObjectSpec, ...],
    num_envs: int = 1,
    env_spacing: float = 2.5,
) -> PickPlaceTabletopFrankaSceneCfg:
    """Create a pick-place scene with all sampled assets spawned once."""
    if len(initial_clutter_names) != len(initial_clutter_specs):
        raise ValueError(
            "Initial clutter names/specs length mismatch: "
            f"names={len(initial_clutter_names)}, specs={len(initial_clutter_specs)}."
        )
    if not initial_clutter_specs:
        raise ValueError("Pick-place asset-bank scene requires at least one initial clutter spec.")
    if len(initial_clutter_specs) > PICK_PLACE_CLUTTER_SLOT_COUNT:
        raise ValueError(
            f"Expected at most {PICK_PLACE_CLUTTER_SLOT_COUNT} initial clutter specs, "
            f"got {len(initial_clutter_specs)}."
        )

    scene_cfg = PickPlaceTabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)

    scene_cfg.target_cube.spawn.usd_path = target_usd_paths[initial_target_name]
    scene_cfg.place_receptacle.spawn.usd_path = receptacle_usd_paths[initial_receptacle_name]
    scene_cfg.place_receptacle.init_state.pos = initial_receptacle_pos

    base_clutter_slots = _pick_place_clutter_slots(scene_cfg)
    for clutter_name, clutter_spec, clutter_slot in zip(
        initial_clutter_names,
        initial_clutter_specs,
        base_clutter_slots[:len(initial_clutter_specs)],
        strict=True,
    ):
        clutter_slot.spawn.usd_path = clutter_usd_paths[clutter_name]
        clutter_slot.init_state.pos = clutter_spec.pos_local

    parked_context = initial_clutter_specs[0].context
    for clutter_slot in base_clutter_slots[len(initial_clutter_specs):]:
        clutter_slot.spawn.usd_path = str(parked_context.usd_path)
        clutter_slot.init_state.pos = PARKED_ASSET_POS

    for entity_name, usd_path in target_usd_paths.items():
        if entity_name == "target_cube":
            continue
        setattr(scene_cfg, entity_name, make_rigid_usd_object_cfg(entity_name, usd_path))

    for entity_name, usd_path in receptacle_usd_paths.items():
        if entity_name == "place_receptacle":
            continue
        setattr(scene_cfg, entity_name, make_rigid_usd_object_cfg(entity_name, usd_path))

    base_clutter_names = {f"clutter_{slot_index}" for slot_index in range(PICK_PLACE_CLUTTER_SLOT_COUNT)}
    for entity_name, usd_path in clutter_usd_paths.items():
        if entity_name in base_clutter_names:
            continue
        setattr(scene_cfg, entity_name, make_static_usd_object_cfg(entity_name, usd_path))

    return scene_cfg
