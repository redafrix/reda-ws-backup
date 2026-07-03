
# Architecture Summary

## Top-level files
agent_camera.mp4
AGENTS.md
.gitignore
guidelines.md
pyproject.toml
README.md
run_collect
run_collect.sh
run_sim.sh
sim_output.log
wrist_camera.mp4

## Scripts
collect.py
debug_scene.py
export_ila.py
generate_object_catalog.py
inspect_collection.py
inspect_episode.py
inspect_ila_dataset.py
inspect_object_catalog.py
inspect_objects.py
run.sh
visualize_ila_episode.py
write_ila_splits.py
write_ila_stats.py

## Source modules
src/franka_wrist_camera_scene/app/camera_warmup.py
src/franka_wrist_camera_scene/app/__init__.py
src/franka_wrist_camera_scene/app/launcher.py
src/franka_wrist_camera_scene/collection/__init__.py
src/franka_wrist_camera_scene/collection/pick_place.py
src/franka_wrist_camera_scene/control/gripper.py
src/franka_wrist_camera_scene/control/ik.py
src/franka_wrist_camera_scene/control/__init__.py
src/franka_wrist_camera_scene/control/motion_primitives.py
src/franka_wrist_camera_scene/control/trajectory.py
src/franka_wrist_camera_scene/datasets/ila.py
src/franka_wrist_camera_scene/datasets/__init__.py
src/franka_wrist_camera_scene/debug/camera_probe.py
src/franka_wrist_camera_scene/debug/__init__.py
src/franka_wrist_camera_scene/debug/video_recorder.py
src/franka_wrist_camera_scene/debug/visualization.py
src/franka_wrist_camera_scene/episode/__init__.py
src/franka_wrist_camera_scene/episode/manifest.py
src/franka_wrist_camera_scene/episode/recorder.py
src/franka_wrist_camera_scene/episode/reset.py
src/franka_wrist_camera_scene/episode/schema.py
src/franka_wrist_camera_scene/episode/success.py
src/franka_wrist_camera_scene/export/ila.py
src/franka_wrist_camera_scene/export/ila_splits.py
src/franka_wrist_camera_scene/export/ila_stats.py
src/franka_wrist_camera_scene/export/__init__.py
src/franka_wrist_camera_scene/__init__.py
src/franka_wrist_camera_scene/objects/catalog_generator.py
src/franka_wrist_camera_scene/objects/catalog.py
src/franka_wrist_camera_scene/objects/__init__.py
src/franka_wrist_camera_scene/objects/registry.py
src/franka_wrist_camera_scene/objects/selection.py
src/franka_wrist_camera_scene/policies/circle_policy.py
src/franka_wrist_camera_scene/policies/__init__.py
src/franka_wrist_camera_scene/policies/pick_place_scripted.py
src/franka_wrist_camera_scene/policies/scripted_base.py
src/franka_wrist_camera_scene/scene/__init__.py
src/franka_wrist_camera_scene/scene/lighting.py
src/franka_wrist_camera_scene/scene/object_context.py
src/franka_wrist_camera_scene/scene/tabletop.py
src/franka_wrist_camera_scene/settings.py
src/franka_wrist_camera_scene/tasks/base.py
src/franka_wrist_camera_scene/tasks/__init__.py
src/franka_wrist_camera_scene/tasks/pick_place.py
src/franka_wrist_camera_scene/tasks/sampling.py
src/franka_wrist_camera_scene/utils/__init__.py
src/franka_wrist_camera_scene/utils/paths.py

## Config files
configs/collection.yaml
configs/object_catalog.generated.yaml
configs/object_catalog.yaml
configs/objects.yaml
configs/scene.yaml

## Key symbol map
scripts/inspect_objects.py:15:def main() -> None:
scripts/write_ila_stats.py:22:def main() -> None:
scripts/inspect_ila_dataset.py:23:def main() -> None:
scripts/inspect_episode.py:19:def main() -> None:
scripts/inspect_collection.py:53:def main() -> None:
scripts/inspect_object_catalog.py:27:def main() -> None:
scripts/export_ila.py:23:def main() -> None:
scripts/collect.py:51:def main() -> None:
scripts/visualize_ila_episode.py:34:def main() -> None:
scripts/visualize_ila_episode.py:41:        agent_rgb = episode["agent_rgb"]
scripts/visualize_ila_episode.py:47:        frame_count = int(agent_rgb.shape[0])
scripts/visualize_ila_episode.py:57:            ax.imshow(agent_rgb[frame_idx])
scripts/write_ila_splits.py:23:def main() -> None:
scripts/generate_object_catalog.py:34:def main() -> None:
scripts/debug_scene.py:2:"""Run the Franka tabletop wrist-camera scene in Isaac Lab."""
scripts/debug_scene.py:19:    parser = argparse.ArgumentParser(description="Franka Panda tabletop scene with wrist and agent cameras.")
scripts/debug_scene.py:69:from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg
scripts/debug_scene.py:146:def main() -> None:
scripts/debug_scene.py:159:    scene = InteractiveScene(TabletopFrankaSceneCfg(num_envs=args_cli.num_envs, env_spacing=2.5))
src/franka_wrist_camera_scene/collection/pick_place.py:17:from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg, make_tabletop_scene_cfg
src/franka_wrist_camera_scene/episode/reset.py:1:"""Reset logic for Franka tabletop episodes."""
src/franka_wrist_camera_scene/episode/reset.py:12:def reset_robot_to_default(scene: InteractiveScene) -> None:
src/franka_wrist_camera_scene/episode/reset.py:27:def reset_pick_place_objects(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
src/franka_wrist_camera_scene/episode/reset.py:42:def reset_pick_place_episode(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
src/franka_wrist_camera_scene/episode/recorder.py:52:    agent_rgb: list[np.ndarray] = field(default_factory=list)
src/franka_wrist_camera_scene/episode/recorder.py:54:    agent_depth: list[np.ndarray] = field(default_factory=list)
src/franka_wrist_camera_scene/episode/recorder.py:90:            ("agent_camera", self.agent_rgb),
src/franka_wrist_camera_scene/episode/recorder.py:98:                ("agent_camera", self.agent_depth),
src/franka_wrist_camera_scene/episode/recorder.py:104:    def save(self, success: bool) -> Path:
src/franka_wrist_camera_scene/episode/recorder.py:125:                agent_rgb=np.asarray(self.agent_rgb, dtype=np.uint8),
src/franka_wrist_camera_scene/episode/recorder.py:131:                agent_depth=np.asarray(self.agent_depth, dtype=np.float32),
src/franka_wrist_camera_scene/episode/success.py:11:def pick_place_success(
src/franka_wrist_camera_scene/scene/tabletop.py:1:"""Isaac Lab scene configuration for a Franka tabletop setup with cameras."""
src/franka_wrist_camera_scene/scene/tabletop.py:6:from isaaclab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
src/franka_wrist_camera_scene/scene/tabletop.py:8:from isaaclab.sensors import CameraCfg
src/franka_wrist_camera_scene/scene/tabletop.py:19:def pinhole_camera_cfg(clipping_range: tuple[float, float]) -> sim_utils.PinholeCameraCfg:
src/franka_wrist_camera_scene/scene/tabletop.py:21:    return sim_utils.PinholeCameraCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:30:class TabletopFrankaSceneCfg(InteractiveSceneCfg):
src/franka_wrist_camera_scene/scene/tabletop.py:31:    """Warehouse tabletop scene with a Franka Panda and two camera sensors."""
src/franka_wrist_camera_scene/scene/tabletop.py:59:    target_cube = RigidObjectCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:66:        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.58, -0.16, TABLE_HEIGHT_M + 0.05)),
src/franka_wrist_camera_scene/scene/tabletop.py:78:    wrist_camera = CameraCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:79:        prim_path="{ENV_REGEX_NS}/Robot/panda_hand/wrist_rgbd_camera",
src/franka_wrist_camera_scene/scene/tabletop.py:86:        offset=CameraCfg.OffsetCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:93:    agent_camera = CameraCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:100:        offset=CameraCfg.OffsetCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:112:) -> TabletopFrankaSceneCfg:
src/franka_wrist_camera_scene/scene/tabletop.py:114:    scene_cfg = TabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
src/franka_wrist_camera_scene/debug/video_recorder.py:39:                for camera_name in ("wrist_camera", "agent_camera"):
src/franka_wrist_camera_scene/debug/video_recorder.py:45:                print("[INFO] Recording wrist_camera.mp4 and agent_camera.mp4 until stop or 20 seconds.")
src/franka_wrist_camera_scene/debug/video_recorder.py:56:                print("[INFO] Saved wrist_camera.mp4 and agent_camera.mp4")
src/franka_wrist_camera_scene/policies/circle_policy.py:13:class CircleMotionPolicy:
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:15:class PickPlaceScriptedPolicy:
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:39:    def reset(self) -> None:
src/franka_wrist_camera_scene/policies/scripted_base.py:10:class PolicyCommand:
src/franka_wrist_camera_scene/tasks/base.py:1:"""Base definitions for Franka tabletop tasks."""
src/franka_wrist_camera_scene/tasks/pick_place.py:14:    ee_body_name: str = "panda_hand"
src/franka_wrist_camera_scene/export/ila.py:33:            "agent_rgb": traj["agent_rgb"],
src/franka_wrist_camera_scene/export/ila.py:45:        if "agent_depth" in traj.files and "wrist_depth" in traj.files:
src/franka_wrist_camera_scene/export/ila.py:46:            arrays["agent_depth"] = traj["agent_depth"]
src/franka_wrist_camera_scene/export/ila.py:91:        "camera_names": ["agent_rgb", "wrist_rgb"],
src/franka_wrist_camera_scene/export/ila.py:103:            "agent_rgb",
src/franka_wrist_camera_scene/control/ik.py:14:class CartesianIKController:
src/franka_wrist_camera_scene/control/ik.py:20:        end_effector_body: str = "panda_hand",
src/franka_wrist_camera_scene/control/ik.py:53:    def reset(self) -> None:
src/franka_wrist_camera_scene/control/gripper.py:10:class GripperController:
src/franka_wrist_camera_scene/app/camera_warmup.py:15:    for camera_name in ("wrist_camera", "agent_camera"):
src/franka_wrist_camera_scene/__init__.py:1:"""Franka tabletop Isaac Lab data-collection package."""
configs/scene.yaml:1:# Isaac Lab Franka Tabletop Scene Configurations (Active parameters only)
