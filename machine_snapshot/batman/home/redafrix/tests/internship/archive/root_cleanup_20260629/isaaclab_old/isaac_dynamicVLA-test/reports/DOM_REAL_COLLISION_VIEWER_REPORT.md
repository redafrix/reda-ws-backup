# DOM Real Collision Viewer Report

Goal:
Create and launch an interactive Isaac/Omniverse GUI stage to inspect visible meshes and physics/collision geometry overlays.

This corrects the previous screenshot/showroom task.
This is a real 3D collision viewer task.
## Start
Thu Jun 11 02:47:33 PM CEST 2026
ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
/home/redafrix/tests/internship/isaac_dynamicVLA-test

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  258G   29G  91% /

## Existing Isaac/Kit/Omniverse processes
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/isaac_dynamicVLA-test/create_dom_collision_viewer_stage.py", line 90, in <module>
    prim.AddTranslateOp().Set(Gf.Vec3f(x, y, 0.05))
pxr.Tf.ErrorException: 
	Error in 'pxrInternal_v0_25_11__pxrReserved__::UsdGeomXformable::AddXformOp' at line 172 in file /opt/USD/pxr/usd/usdGeom/xformable.cpp : 'The xformOp 'xformOp:translate' already exists in xformOpOrder [[xformOp:translate, xformOp:orient, xformOp:scale]].'
There was an error running python
STAGE_CREATED /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/real_collision_viewer/dom_collision_viewer_stage.usd
PLACED_COUNT 24
Stage: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/real_collision_viewer/dom_collision_viewer_stage.usd
Checking for running Isaac/Kit/Omniverse processes...
STOP: Another Isaac/Kit/Omniverse process is running. Not launching.
redafrix  117218    7153  0 14:48 ?        00:00:00 /usr/bin/bash -c shopt -u promptvars nullglob extglob nocaseglob dotglob; _bgpids_file=/tmp/gemini-shell-DJy1jL/bgpids.tmp (   trap 'jobs -p > "$_bgpids_file"' EXIT export ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test cd "$ROOT"  chmod +x reports/real_collision_viewer/launch_collision_viewer.sh  reports/real_collision_viewer/launch_collision_viewer.sh \   2>&1 | tee -a reports/DOM_REAL_COLLISION_VIEWER_REPORT.md  {   echo   echo "## GUI launch log tail"   sleep 10   tail -80 logs/dom_collision_viewer_gui.log || true   echo   echo "## PID"   cat logs/dom_collision_viewer_gui.pid 2>/dev/null || true } | tee -a reports/DOM_REAL_COLLISION_VIEWER_REPORT.md ) __code=$? exit $__code
redafrix  117219  117218  0 14:48 ?        00:00:00 /usr/bin/bash -c shopt -u promptvars nullglob extglob nocaseglob dotglob; _bgpids_file=/tmp/gemini-shell-DJy1jL/bgpids.tmp (   trap 'jobs -p > "$_bgpids_file"' EXIT export ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test cd "$ROOT"  chmod +x reports/real_collision_viewer/launch_collision_viewer.sh  reports/real_collision_viewer/launch_collision_viewer.sh \   2>&1 | tee -a reports/DOM_REAL_COLLISION_VIEWER_REPORT.md  {   echo   echo "## GUI launch log tail"   sleep 10   tail -80 logs/dom_collision_viewer_gui.log || true   echo   echo "## PID"   cat logs/dom_collision_viewer_gui.pid 2>/dev/null || true } | tee -a reports/DOM_REAL_COLLISION_VIEWER_REPORT.md ) __code=$? exit $__code

## GUI launch log tail

## PID
Stage: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/real_collision_viewer/dom_collision_viewer_stage.usd
Checking for running Isaac/Kit/Omniverse processes...
Launching Isaac GUI:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/isaac-sim.sh /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/real_collision_viewer/dom_collision_viewer_stage.usd
LAUNCHED_PID=117367
LOG=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/dom_collision_viewer_gui.log
## GUI launch log tail (after 15s)
[12.015s] [ext: omni.physx.supportui-106.5.7] startup
[12.041s] [ext: omni.physx.telemetry-106.5.7] startup
[12.046s] [ext: isaacsim.replicator.examples-1.1.2] startup
[12.054s] [ext: omni.kit.property.isaac-1.0.2] startup
2026-06-11 12:49:14 [12,036ms] [Warning] [omni.kit.property.isaac] omni.kit.property.isaac has been deprecated in favor of isaacsim.gui.property. Please update your code accordingly.
2026-06-11 12:49:14 [12,039ms] [Warning] [omni.kit.property.isaac.widgets] omni.kit.property.isaac.widgets has been deprecated in favor of isaacsim.gui.property.widgets. Please update your code accordingly.
[12.079s] [ext: omni.kit.viewport.menubar.lighting-106.0.2] startup
[12.098s] [ext: omni.kit.window.console-0.2.14] startup
[12.115s] [ext: omni.kit.window.status_bar-0.1.7] startup
[12.218s] [ext: omni.kit.widget.collection-0.1.18] startup
[12.240s] [ext: omni.physx.bundle-106.5.7] startup
[12.241s] [ext: omni.replicator.isaac-2.0.3] startup
2026-06-11 12:49:14 [12,212ms] [Warning] [omni.replicator.isaac] omni.replicator.isaac has been deprecated in favor of isaacsim.replicator.domain_randomization, isaacsim.replicator.examples, isaacsim.replicator.writers. Please update your code accordingly.
[12.242s] [ext: omni.replicator.replicator_yaml-2.0.10] startup
[12.253s] [ext: omni.rtx.settings.core-0.6.3] startup
[12.260s] [ext: omni.kit.converter.jt_core-503.2.2] startup
[12.347s] [ext: omni.usd.metrics.assembler.ui-106.5.0] startup
[12.350s] [ext: omni.kit.window.collection-0.2.0] startup
[12.352s] [ext: isaacsim.sensors.physx.ui-2.2.1] startup
[12.355s] [ext: semantics.schema.editor-0.3.10] startup
[12.359s] [ext: omni.kit.ui.actions-1.0.2] startup
[12.361s] [ext: semantics.schema.property-1.0.5] startup
[12.363s] [ext: omni.kit.converter.jt-503.2.2] startup
[12.366s] [ext: omni.kit.quicklayout-1.0.8] startup
[12.368s] [ext: omni.kit.window.commands-0.2.7] startup
[12.372s] [ext: omni.isaac.range_sensor.ui-2.0.2] startup
2026-06-11 12:49:14 [12,343ms] [Warning] [omni.isaac.range_sensor.ui] omni.isaac.range_sensor.ui has been deprecated in favor of isaacsim.sensors.physx.ui. Please update your code accordingly.
2026-06-11 12:49:14 [12,343ms] [Warning] [omni.isaac.range_sensor.ui.menu] omni.isaac.range_sensor.ui.menu has been deprecated in favor of isaacsim.sensors.physx.ui.menu. Please update your code accordingly.
[12.373s] [ext: isaacsim.robot.wheeled_robots.ui-2.1.5] startup
[12.377s] [ext: omni.kit.menu.common-1.1.9] startup
[12.380s] [ext: isaacsim.exp.base-4.5.0] startup
[12.381s] [ext: omni.kit.converter.cad-202.2.0] startup
[12.381s] [ext: omni.kit.window.stats-0.1.7] startup
[12.382s] [ext: isaacsim.app.setup-1.3.5] startup
[12.384s] Isaac Sim Full Version: 4.5.0-rc.36
[12.384s] Writing Isaac Sim icon file
[12.385s] [ext: omni.kit.profiler.window-2.3.1] startup
[12.400s] [ext: isaacsim.exp.full-4.5.0] startup
[12.537s] [ext: isaacsim.ros2.bridge-4.1.15] startup
[12.718s] Attempting to load system rclpy
[12.766s] rclpy loaded
2026-06-11 12:49:15 [13,192ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 7508933632
2026-06-11 12:49:15 [13,192ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid false, within: false
2026-06-11 12:49:15 [13,192ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : decrement: 167690, decrement size: 7433845248
2026-06-11 12:49:15 [13,192ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : New limit 9574251 (slope: 447, intercept: 13179904)
2026-06-11 12:49:15 [13,192ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 4287216384
2026-06-11 12:49:15 [13,192ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid true, within: true
[13.342s] app ready
2026-06-11 12:49:16 [14,303ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults-transient/meshlights/forceDisable'
2026-06-11 12:49:17 [14,776ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults/post/dlss/execMode'
## Summary
Interactive collision viewer stage created and launched.
Manual inspection instructions ready in reports/real_collision_viewer/HOW_TO_ENABLE_COLLISION_OVERLAY.md
