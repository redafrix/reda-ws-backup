# Branch Hygiene Before Object Integration Report

Goal:
Clean/freeze the object-integration branch before adding new objects.

Known good baseline:
- baseline apple recheck succeeded
- Episode 0 success=True
## Current state
object-integration-static-assets
5fb88036e0824d0773e714edbe3da044a1d88843
?? configs/baseline_reachable_apple.yaml
?? configs/tiny_collection.yaml
?? run_stabilization_collect.sh
?? scratch/
?? scripts/debug_scene.py.bak_baseline_stabilize
?? src/sitecustomize.py

## Untracked file previews

### configs/baseline_reachable_apple.yaml
output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple
start_episode_id: 0
num_episodes: 1
max_steps: 2400
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 123

target_object:
  catalog_config: object_catalog.yaml
  category_id: apple
  variant_id: apple01

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

### configs/tiny_collection.yaml
output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/tiny_collect
start_episode_id: 0
num_episodes: 1
max_steps: 2400
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 123

target_object:
  catalog_config: object_catalog.yaml
  category_id: apple
  variant_id: apple01

pose_randomization:
  object_xy_range:
    x: [-0.05, 0.05]
    y: [-0.05, 0.05]
  place_xy_range:
    x: [-0.06, 0.06]
    y: [-0.06, 0.06]

lighting_randomization:
  dome_light_intensity_range: [650.0, 1200.0]
  dome_light_color_options:
    - [0.90, 0.90, 0.90]
    - [1.00, 0.92, 0.84]
    - [0.82, 0.88, 1.00]

### run_stabilization_collect.sh
#!/usr/bin/env bash
set -e

WS="/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test"
REPO="$WS/franka_wrist_camera_isaaclab"
REPORTS="$WS/reports"
LOGS="$WS/logs"
OUT="$WS/outputs"

cd "$REPO"

echo "Clearing old baseline reachable apple outputs..."
rm -rf "$OUT/baseline_reachable_apple"
mkdir -p "$OUT/baseline_reachable_apple"

export ISAACLAB_ROOT="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab"
export TERM=xterm
export PYTHONPATH="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_assets:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_mimic:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_rl:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_tasks:$REPO/src"

echo "Starting data collection with baseline_reachable_apple.yaml..."
set +e
timeout --signal=INT --kill-after=60s 1800s \
  "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/collect.py \
  --headless \
  --collection_config baseline_reachable_apple.yaml \
  2>&1 | tee "$LOGS/baseline_reachable_apple_collect.log"

COLLECT_STATUS=${PIPESTATUS[0]}
set -e

echo "Collection finished with status: $COLLECT_STATUS"

{
  echo
  echo "## baseline reachable apple collect result"
  echo "status=$COLLECT_STATUS"
  echo "log=$LOGS/baseline_reachable_apple_collect.log"
  grep -Ei "success|failed|Traceback|Exception|Error|episode|saved|out of reach|reach|object|apple|omni.kvdb|lock|CUDA|out of memory" \
    "$LOGS/baseline_reachable_apple_collect.log" | tail -400 || true
  echo
  echo "## outputs"
  find "$OUT/baseline_reachable_apple" -maxdepth 5 -type f -printf "%p | %s bytes\n" | sort || true
} | tee -a "$REPORTS/BASELINE_STABILIZATION_REPORT.md"

exit $COLLECT_STATUS

### src/sitecustomize.py
print("sitecustomize: pre-importing torch to avoid PyTorch/Isaac Sim conflict...")
import torch

### scripts/debug_scene.py.bak_baseline_stabilize
#!/usr/bin/env python3
"""Run the Franka tabletop wrist-camera scene in Isaac Lab."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

from franka_wrist_camera_scene.app import launcher  # noqa: F401
from isaaclab.app import AppLauncher  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Franka Panda tabletop scene with wrist and agent cameras.")
    parser.add_argument("--num_envs", type=int, default=1, help="Number of cloned tabletop scenes.")
    parser.add_argument(
        "--max_steps", type=int, default=0, help="Stop after this many simulation steps; 0 runs forever."
    )
    parser.add_argument(
        "--task",
        type=str,
        default="circle",
        choices=["circle", "pick_place"],
        help="Task/policy to run.",
    )
    parser.add_argument(
        "--circle_diameter", type=float, default=0.40, help="Gripper circle diameter in meters."
    )
    parser.add_argument("--circle_frequency", type=float, default=0.045, help="Circle frequency in Hz.")
    parser.add_argument("--probe_u", type=int, default=320, help="Wrist-camera pixel u coordinate.")
    parser.add_argument("--probe_v", type=int, default=240, help="Wrist-camera pixel v coordinate.")
    parser.add_argument(
        "--save_probe_every", type=int, default=0, help="Save wrist-camera overlay every N steps; 0 disables."
    )
    parser.add_argument("--video", action="store_true", help="Record a video from the wrist camera.")
    parser.add_argument(
        "--show_markers", action="store_true", help="Show physical circle debug markers in the scene."
    )
    AppLauncher.add_app_launcher_args(parser)
    args = parser.parse_args()
    args.enable_cameras = True
    args.kit_args = f"{args.kit_args} --/rtx/hydra/readTransformsFromFabricInRenderDelegate=false".strip()
    return args


args_cli = parse_args()
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

launcher.patch_physx_schema()

import isaaclab.sim as sim_utils  # noqa: E402
from isaaclab.assets import Articulation  # noqa: E402
from isaaclab.scene import InteractiveScene  # noqa: E402

from franka_wrist_camera_scene.control.gripper import GripperController
from franka_wrist_camera_scene.control.ik import CartesianIKController
from franka_wrist_camera_scene.control.trajectory import CircleTrajectoryCfg, circle_points_w
from franka_wrist_camera_scene.debug.camera_probe import WristCameraProbe
from franka_wrist_camera_scene.debug.video_recorder import VideoRecorder
from franka_wrist_camera_scene.debug.visualization import CircleMotionMarkers
from franka_wrist_camera_scene.policies.circle_policy import CircleMotionPolicy
from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg
from franka_wrist_camera_scene.settings import CIRCLE_CENTER_LOCAL, GRIPPER_DOWN_QUAT_WXYZ, SIM_DT
from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
from franka_wrist_camera_scene.app.camera_warmup import nudge_camera_prims
from franka_wrist_camera_scene.episode.reset import reset_robot_to_default, reset_pick_place_episode
from franka_wrist_camera_scene.episode.success import pick_place_success


def run_simulator(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    policy: CircleMotionPolicy | PickPlaceScriptedPolicy,
    ik: CartesianIKController,
    gripper: GripperController,
    probe: WristCameraProbe,
    max_steps: int,
    video: bool = False,
    show_markers: bool = False,
) -> None:
    """Run the scene until the app closes or the optional step limit is reached."""
    robot: Articulation = scene["robot"]
    sim_dt = sim.get_physics_dt()
    sim_time_s = 0.0
    step = 0

    video_recorder = VideoRecorder(video, sim_dt)

    # Debug markers (only applicable for circle task)
    markers = None
    if show_markers and isinstance(policy, CircleMotionPolicy):
        markers = CircleMotionMarkers()
        points_w = circle_points_w(scene, policy.cfg, robot.device)
        markers.draw_path(points_w)

    settling = False
    settle_steps = 0
    max_settle_steps = int(1.0 / sim_dt)

    while simulation_app.is_running() and (max_steps <= 0 or step < max_steps):
        # 1. Step the policy to get reference actions
        cmd = policy.step(None, sim_time_s)

        # 2. Update and apply Cartesian IK command
        ik.set_target_pose(cmd.target_pos_w, cmd.target_quat_w)
        ik.apply(scene, robot)

        # 3. Update and apply gripper command
        gripper.set_width(cmd.finger_opening_m)
        gripper.apply(robot)

        scene.write_data_to_sim()

        sim.step()
        sim_time_s += sim_dt
        step += 1
        scene.update(sim_dt)
        probe.maybe_save(scene, step)

        if markers is not None:
            markers.draw_target(cmd.target_pos_w)

        video_recorder.record_step(scene, step)

        if cmd.done:
            if not settling:
                print(f"[INFO] Scripted policy completed execution. Settling for 1.0s ({max_settle_steps} steps)...", flush=True)
                settling = True
            settle_steps += 1
            if settle_steps >= max_settle_steps:
                if isinstance(policy, PickPlaceScriptedPolicy):
                    success = pick_place_success(scene, policy.spec)
                    print(f"[INFO] Pick-place success: {success.detach().cpu().tolist()}", flush=True)
                break

    video_recorder.close()


def main() -> None:
    sim_cfg = sim_utils.SimulationCfg(
        dt=SIM_DT,
        device=args_cli.device,
        physx=sim_utils.PhysxCfg(
            enable_external_forces_every_iteration=True,
            min_velocity_iteration_count=1,
            min_position_iteration_count=4,
        ),
    )
    sim = sim_utils.SimulationContext(sim_cfg)
    sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])

    scene = InteractiveScene(TabletopFrankaSceneCfg(num_envs=args_cli.num_envs, env_spacing=2.5))
    robot: Articulation = scene["robot"]

    # Choose policy based on selected task
    if args_cli.task == "circle":
        trajectory_cfg = CircleTrajectoryCfg(
            center_local=CIRCLE_CENTER_LOCAL,
            diameter_m=args_cli.circle_diameter,
            frequency_hz=args_cli.circle_frequency,
            orientation_wxyz=GRIPPER_DOWN_QUAT_WXYZ,
        )
        policy = CircleMotionPolicy(cfg=trajectory_cfg)
    else:  # pick_place
        spec = PickPlaceTaskSpec()
        policy = PickPlaceScriptedPolicy(spec=spec)

    ik = CartesianIKController()
    gripper = GripperController()
    probe = WristCameraProbe(args_cli.probe_u, args_cli.probe_v, args_cli.save_probe_every)

    sim.reset()
    policy.bind(scene, robot)
    ik.bind(scene, robot)
    gripper.bind(scene, robot)
    if args_cli.task == "pick_place":
        reset_pick_place_episode(scene, spec)
    else:
        reset_robot_to_default(scene)
        scene.reset()
    ik.reset()

    nudge_camera_prims(sim, scene)
    run_simulator(
        sim,
        scene,
        policy,
        ik,
        gripper,
        probe,
        args_cli.max_steps,
        video=args_cli.video,
        show_markers=args_cli.show_markers,
    )


if __name__ == "__main__":
    main()
    simulation_app.close()

## scratch listing
scratch/debug_out.txt | 134615 bytes
scratch/inspect_apple_physics.py | 2431 bytes
scratch/inspect_out.txt | 8084 bytes
scratch/inspect_usd.py | 648 bytes
scratch/out.txt | 25444 bytes
scratch/test_print.py | 353 bytes

## After removing backup/scratch
?? configs/baseline_reachable_apple.yaml
?? configs/tiny_collection.yaml
?? run_stabilization_collect.sh
?? src/sitecustomize.py

## Staged diff
 configs/baseline_reachable_apple.yaml | 31 ++++++++++++++++++++++++
 configs/tiny_collection.yaml          | 31 ++++++++++++++++++++++++
 run_stabilization_collect.sh          | 45 +++++++++++++++++++++++++++++++++++
 src/sitecustomize.py                  |  2 ++
 4 files changed, 109 insertions(+)
diff --git a/configs/baseline_reachable_apple.yaml b/configs/baseline_reachable_apple.yaml
new file mode 100644
index 0000000..8ceb4fd
--- /dev/null
+++ b/configs/baseline_reachable_apple.yaml
@@ -0,0 +1,31 @@
+output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple
+start_episode_id: 0
+num_episodes: 1
+max_steps: 2400
+settle_time_s: 1.0
+
+record_cameras: true
+camera_fps: 30
+record_depth: true
+
+seed: 123
+
+target_object:
+  catalog_config: object_catalog.yaml
+  category_id: apple
+  variant_id: apple01
+
+pose_randomization:
+  object_xy_range:
+    x: [0.0, 0.0]
+    y: [0.0, 0.0]
+  place_xy_range:
+    x: [0.0, 0.0]
+    y: [0.0, 0.0]
+
+lighting_randomization:
+  dome_light_intensity_range: [650.0, 1200.0]
+  dome_light_color_options:
+    - [0.90, 0.90, 0.90]
+    - [1.00, 0.92, 0.84]
+    - [0.82, 0.88, 1.00]
diff --git a/configs/tiny_collection.yaml b/configs/tiny_collection.yaml
new file mode 100644
index 0000000..f1ab702
--- /dev/null
+++ b/configs/tiny_collection.yaml
@@ -0,0 +1,31 @@
+output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/tiny_collect
+start_episode_id: 0
+num_episodes: 1
+max_steps: 2400
+settle_time_s: 1.0
+
+record_cameras: true
+camera_fps: 30
+record_depth: true
+
+seed: 123
+
+target_object:
+  catalog_config: object_catalog.yaml
+  category_id: apple
+  variant_id: apple01
+
+pose_randomization:
+  object_xy_range:
+    x: [-0.05, 0.05]
+    y: [-0.05, 0.05]
+  place_xy_range:
+    x: [-0.06, 0.06]
+    y: [-0.06, 0.06]
+
+lighting_randomization:
+  dome_light_intensity_range: [650.0, 1200.0]
+  dome_light_color_options:
+    - [0.90, 0.90, 0.90]
+    - [1.00, 0.92, 0.84]
+    - [0.82, 0.88, 1.00]
diff --git a/run_stabilization_collect.sh b/run_stabilization_collect.sh
new file mode 100755
index 0000000..e99b587
--- /dev/null
+++ b/run_stabilization_collect.sh
@@ -0,0 +1,45 @@
+#!/usr/bin/env bash
+set -e
+
+WS="/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test"
+REPO="$WS/franka_wrist_camera_isaaclab"
+REPORTS="$WS/reports"
+LOGS="$WS/logs"
+OUT="$WS/outputs"
+
+cd "$REPO"
+
+echo "Clearing old baseline reachable apple outputs..."
+rm -rf "$OUT/baseline_reachable_apple"
+mkdir -p "$OUT/baseline_reachable_apple"
+
+export ISAACLAB_ROOT="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab"
+export TERM=xterm
+export PYTHONPATH="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_assets:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_mimic:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_rl:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_tasks:$REPO/src"
+
+echo "Starting data collection with baseline_reachable_apple.yaml..."
+set +e
+timeout --signal=INT --kill-after=60s 1800s \
+  "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/collect.py \
+  --headless \
+  --collection_config baseline_reachable_apple.yaml \
+  2>&1 | tee "$LOGS/baseline_reachable_apple_collect.log"
+
+COLLECT_STATUS=${PIPESTATUS[0]}
+set -e
+
+echo "Collection finished with status: $COLLECT_STATUS"
+
+{
+  echo
+  echo "## baseline reachable apple collect result"
+  echo "status=$COLLECT_STATUS"
+  echo "log=$LOGS/baseline_reachable_apple_collect.log"
+  grep -Ei "success|failed|Traceback|Exception|Error|episode|saved|out of reach|reach|object|apple|omni.kvdb|lock|CUDA|out of memory" \
+    "$LOGS/baseline_reachable_apple_collect.log" | tail -400 || true
+  echo
+  echo "## outputs"
+  find "$OUT/baseline_reachable_apple" -maxdepth 5 -type f -printf "%p | %s bytes\n" | sort || true
+} | tee -a "$REPORTS/BASELINE_STABILIZATION_REPORT.md"
+
+exit $COLLECT_STATUS
diff --git a/src/sitecustomize.py b/src/sitecustomize.py
new file mode 100644
index 0000000..3a139e3
--- /dev/null
+++ b/src/sitecustomize.py
@@ -0,0 +1,2 @@
+print("sitecustomize: pre-importing torch to avoid PyTorch/Isaac Sim conflict...")
+import torch

## After hygiene commit
object-integration-static-assets
2c8bfbbe19656baae0df607ba81caae8a3e30185
2c8bfbb Freeze local Isaac 4.5 baseline configs before object integration
5fb8803 Add output_dir argument override to collect.py
162ab15 Stabilize baseline apple collection: fix scale, add rolling resistance damping, tune gripper actuator gains, and correct finger joint limits
5029899 chore: ignore and untrack thumbnail cache folders
9ca7002 refactor: simplify relative path resolution for durable usd path

# FINAL SUMMARY
- branch: object-integration-static-assets
- commit: 2c8bfbbe19656baae0df607ba81caae8a3e30185
- patch: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/patches/object_branch_hygiene_before_objects.patch

## status

## next recommendation
Repo clean. Ready to add exactly one new object variant in the next step.
