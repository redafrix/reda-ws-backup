# DOM Object Isaac World Inspection Report

Goal:
Load selected DOM object USDs into an Isaac world, inspect their visible mesh shape, collision-risk category, and usefulness for hard manipulation tests.

This is asset inspection only:
- no DynamicVLA data collection
- no translation
- no training
- no inference
- no repo modification
## Start
Thu Jun 11 02:40:39 PM CEST 2026
ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
/home/redafrix/tests/internship/isaac_dynamicVLA-test

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  258G   29G  91% /

## Existing Isaac/Kit/Omniverse processes
redafrix  112594  112590  0 14:40 ?        00:00:00 tee -a reports/DOM_OBJECT_ISAAC_WORLD_INSPECTION_REPORT.md
STOP: Another Isaac/Kit/Omniverse process appears to be running. I will not launch inspection.
No conflicting Isaac processes found. Proceeding.
SHORTLIST_JSON /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_hard_object_shortlist.json
SHORTLIST_CSV /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_hard_object_shortlist.csv
selected_count 48

01. bowl/bowl04.usd | score=162 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
02. bowl/bowl06.usd | score=162 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
03. bowl/bowl09.usd | score=162 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
04. bowl/bowl17.usd | score=162 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
05. bowl/bowl11.usd | score=158 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
06. bowl/bowl19.usd | score=158 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
07. bowl/bowl05.usd | score=154 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
08. bowl/bowl08.usd | score=154 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
09. bowl/bowl10.usd | score=154 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
10. bowl/bowl12.usd | score=154 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
11. bowl/bowl13.usd | score=154 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
12. bowl/bowl16.usd | score=154 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
13. bowl/bowl00.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
14. bowl/bowl01.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
15. bowl/bowl02.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
16. bowl/bowl07.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
17. bowl/bowl14.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
18. bowl/bowl15.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
19. bowl/bowl18.usd | score=150 | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
20. cup/cup05.usd | score=144 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
21. cup/cup06.usd | score=144 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
22. cup/cup07.usd | score=144 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
23. cup/cup08.usd | score=144 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
24. cup/cup09.usd | score=144 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
25. plate/plate16.usd | score=144 | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
26. bottle/dbottle04.usd | score=135 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
27. bottle/wbottle17.usd | score=135 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
28. bottle/wbottle02.usd | score=131 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
29. can/can11.usd | score=127 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
30. can/fcan05.usd | score=127 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
31. can/can00.usd | score=123 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
32. tray/tray05.usd | score=140 | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
33. tray/tray06.usd | score=140 | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
34. tray/tray07.usd | score=140 | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
35. plate/plate01.usd | score=140 | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
36. plate/plate03.usd | score=140 | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
37. box/box00.usd | score=135 | EXACT_OR_SHARED_MESH_LIKELY | edges/corners; exact/shared collision likely
38. box/box01.usd | score=135 | EXACT_OR_SHARED_MESH_LIKELY | edges/corners; exact/shared collision likely
39. box/box02.usd | score=135 | EXACT_OR_SHARED_MESH_LIKELY | edges/corners; exact/shared collision likely
40. tomato/tomato07.usd | score=105 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
41. tomato/tomato03.usd | score=101 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
42. tomato/tomato02.usd | score=72 | ROUGH_PRIMITIVE_COLLISION | collision risk/stress case
43. potato/potato00.usd | score=103 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
44. potato/potato17.usd | score=103 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
45. potato/potato07.usd | score=99 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
46. avocado/avocado04.usd | score=101 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
47. avocado/avocado05.usd | score=101 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
48. avocado/avocado01.usd | score=93 | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match

## Isaac showroom result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/isaac_dom_object_showroom.log

## Generated inspection files

## Important log lines
2026-06-11 12:41:19 [360ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:19 [360ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:19 [373ms] [Warning] [omni.platforminfo.plugin] failed to open the default display.  Can't verify X Server version.
2026-06-11 12:41:22 [2,832ms] [Warning] [gpu.foundation.plugin] Detected IOMMU is enabled. Running CUDA peer-to-peer bandwidth and latency validation.
2026-06-11 12:41:22 [3,289ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:22 [3,289ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:22 [3,304ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:22 [3,304ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:22 [3,313ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:22 [3,313ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
[3.325s] [ext: omni.kit.renderer.capture-0.0.0] startup
2026-06-11 12:41:22 [3,319ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:22 [3,319ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:22 [3,321ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:22 [3,321ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:22 [3,321ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:22 [3,321ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
[4.081s] [ext: omni.kvdb-106.5.7] startup
Starting kit application with the following args:  ['/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/exts/isaacsim.simulation_app/isaacsim/simulation_app/simulation_app.py', '/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/apps/isaacsim.exp.base.python.kit', '--/app/tokens/exe-path=/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/kit', '--/persistent/app/viewport/displayOptions=3094', '--/rtx/materialDb/syncLoads=True', '--/rtx/hydra/materialSyncLoads=True', '--/omni.kit.plugin/syncUsdLoads=True', '--/app/renderer/resolution/width=1920', '--/app/renderer/resolution/height=1080', '--/app/window/width=1440', '--/app/window/height=900', '--/renderer/multiGpu/enabled=True', '--/app/fastShutdown=True', '--/app/installSignalHandlers=0', '--ext-folder', '/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/exts', '--ext-folder', '/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/apps', '--/physics/cudaDevice=0', '--portable', '--no-window', '--/app/window/hideUi=1']
   CUDA Toolkit 11.8, Driver 13.0
     "cuda:0"   : "NVIDIA GeForce RTX 4060 Laptop GPU" (8 GiB, sm_89, mempool enabled)
2026-06-11 12:41:31 [12,167ms] [Error] [omni.kit.app._impl] [py stderr]: Traceback (most recent call last):
2026-06-11 12:41:31 [12,167ms] [Error] [omni.kit.app._impl] [py stderr]:   File "/home/redafrix/tests/internship/isaac_dynamicVLA-test/isaac_dom_object_showroom.py", line 75, in <module>
2026-06-11 12:41:31 [12,167ms] [Error] [omni.kit.app._impl] [py stderr]:     prim.AddTranslateOp().Set(Gf.Vec3f(x, y, 0.05))
2026-06-11 12:41:31 [12,167ms] [Error] [omni.kit.app._impl] [py stderr]: AttributeError: 'Prim' object has no attribute 'AddTranslateOp'

## Isaac showroom result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/isaac_dom_object_showroom.log

## Generated inspection files

## Important log lines
2026-06-11 12:41:49 [397ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:49 [397ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:49 [410ms] [Warning] [omni.platforminfo.plugin] failed to open the default display.  Can't verify X Server version.
2026-06-11 12:41:52 [2,917ms] [Warning] [gpu.foundation.plugin] Detected IOMMU is enabled. Running CUDA peer-to-peer bandwidth and latency validation.
2026-06-11 12:41:52 [3,620ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:52 [3,620ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:52 [3,640ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:52 [3,640ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:52 [3,649ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:52 [3,649ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
[3.661s] [ext: omni.kit.renderer.capture-0.0.0] startup
2026-06-11 12:41:52 [3,655ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:52 [3,655ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:52 [3,657ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:52 [3,657ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:41:52 [3,657ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:41:52 [3,657ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
[4.511s] [ext: omni.kvdb-106.5.7] startup
Starting kit application with the following args:  ['/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/exts/isaacsim.simulation_app/isaacsim/simulation_app/simulation_app.py', '/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/apps/isaacsim.exp.base.python.kit', '--/app/tokens/exe-path=/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/kit', '--/persistent/app/viewport/displayOptions=3094', '--/rtx/materialDb/syncLoads=True', '--/rtx/hydra/materialSyncLoads=True', '--/omni.kit.plugin/syncUsdLoads=True', '--/app/renderer/resolution/width=1920', '--/app/renderer/resolution/height=1080', '--/app/window/width=1440', '--/app/window/height=900', '--/renderer/multiGpu/enabled=True', '--/app/fastShutdown=True', '--/app/installSignalHandlers=0', '--ext-folder', '/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/exts', '--ext-folder', '/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/apps', '--/physics/cudaDevice=0', '--portable', '--no-window', '--/app/window/hideUi=1']
   CUDA Toolkit 11.8, Driver 13.0
     "cuda:0"   : "NVIDIA GeForce RTX 4060 Laptop GPU" (8 GiB, sm_89, mempool enabled)
2026-06-11 12:42:02 [13,020ms] [Error] [omni.kit.app._impl] [py stderr]: Traceback (most recent call last):
2026-06-11 12:42:02 [13,020ms] [Error] [omni.kit.app._impl] [py stderr]:   File "/home/redafrix/tests/internship/isaac_dynamicVLA-test/isaac_dom_object_showroom.py", line 64, in <module>
2026-06-11 12:42:02 [13,020ms] [Error] [omni.kit.app._impl] [py stderr]:     UsdGeom.Xformable(prim).AddTranslateOp().Set(Gf.Vec3f(x, y, 0.05))
2026-06-11 12:42:02 [13,020ms] [Error] [omni.kit.app._impl] [py stderr]: pxr.Tf.ErrorException: 
	Error in 'pxrInternal_v0_22__pxrReserved__::UsdGeomXformable::AddXformOp' at line 190 in file /builds/omniverse/usd-ci/USD/pxr/usd/usdGeom/xformable.cpp : 'The xformOp 'xformOp:translate' already exists in xformOpOrder [[xformOp:translate, xformOp:orient, xformOp:scale]].'

## Isaac showroom result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/isaac_dom_object_showroom.log

## Generated inspection files
reports/isaac_object_inspection/dom_hard_objects_showroom.usd | 7072 bytes
reports/isaac_object_inspection/showroom_angle.png | 2274148 bytes
reports/isaac_object_inspection/showroom_close_front.png | 2847785 bytes
reports/isaac_object_inspection/showroom_overview.png | 1224499 bytes

## Important log lines
2026-06-11 12:42:17 [370ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:17 [370ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:42:17 [382ms] [Warning] [omni.platforminfo.plugin] failed to open the default display.  Can't verify X Server version.
2026-06-11 12:42:19 [2,955ms] [Warning] [gpu.foundation.plugin] Detected IOMMU is enabled. Running CUDA peer-to-peer bandwidth and latency validation.
2026-06-11 12:42:20 [3,469ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:20 [3,469ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:42:20 [3,486ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:20 [3,486ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:42:20 [3,495ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:20 [3,495ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
[3.507s] [ext: omni.kit.renderer.capture-0.0.0] startup
2026-06-11 12:42:20 [3,505ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:20 [3,505ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:42:20 [3,507ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:20 [3,507ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
2026-06-11 12:42:20 [3,509ms] [Warning] [carb.windowing-glfw.plugin] GLFW initialization failed.
2026-06-11 12:42:20 [3,509ms] [Warning] [carb] Failed to startup plugin carb.windowing-glfw.plugin (interfaces: [carb::windowing::IGLContext v1.0],[carb::windowing::IWindowing v1.5]) (impl: carb.windowing-glfw.plugin)
[4.510s] [ext: omni.kvdb-106.5.7] startup

## HTML review
-rw-rw-r-- 1 redafrix redafrix 9.4K Jun 11 14:43 reports/isaac_object_inspection/index.html

## Manual open paths
/home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/index.html
/home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/dom_hard_objects_showroom.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/showroom_overview.png
/home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/showroom_angle.png
/home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/showroom_close_front.png

xdg-open log:

# FINAL SUMMARY
- report: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/DOM_OBJECT_ISAAC_WORLD_INSPECTION_REPORT.md
- shortlist json: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_hard_object_shortlist.json
- shortlist csv: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_hard_object_shortlist.csv
- review html: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/index.html
- showroom stage: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/isaac_object_inspection/dom_hard_objects_showroom.usd
- screenshots:
  - reports/isaac_object_inspection/showroom_angle.png | 2274148 bytes
  - reports/isaac_object_inspection/showroom_close_front.png | 2847785 bytes
  - reports/isaac_object_inspection/showroom_overview.png | 1224499 bytes

## Selected hard objects
01. bowl/bowl04.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
02. bowl/bowl06.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
03. bowl/bowl09.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
04. bowl/bowl17.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
05. bowl/bowl11.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
06. bowl/bowl19.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
07. bowl/bowl05.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
08. bowl/bowl08.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
09. bowl/bowl10.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
10. bowl/bowl12.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
11. bowl/bowl13.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
12. bowl/bowl16.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
13. bowl/bowl00.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
14. bowl/bowl01.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
15. bowl/bowl02.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
16. bowl/bowl07.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
17. bowl/bowl14.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
18. bowl/bowl15.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
19. bowl/bowl18.usd | bowl | EXACT_OR_SHARED_MESH_LIKELY | hollow/open-top; exact/shared collision likely
20. cup/cup05.usd | cup | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
21. cup/cup06.usd | cup | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
22. cup/cup07.usd | cup | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
23. cup/cup08.usd | cup | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
24. cup/cup09.usd | cup | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | hollow/open-top; simplified collision but bbox match
25. plate/plate16.usd | plate | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
26. bottle/dbottle04.usd | bottle | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
27. bottle/wbottle17.usd | bottle | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
28. bottle/wbottle02.usd | bottle | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
29. can/can11.usd | can | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
30. can/fcan05.usd | can | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
31. can/can00.usd | can | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | tall/cylindrical grasping; simplified collision but bbox match
32. tray/tray05.usd | tray | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
33. tray/tray06.usd | tray | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
34. tray/tray07.usd | tray | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
35. plate/plate01.usd | plate | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
36. plate/plate03.usd | plate | EXACT_OR_SHARED_MESH_LIKELY | thin/flat object; exact/shared collision likely
37. box/box00.usd | box | EXACT_OR_SHARED_MESH_LIKELY | edges/corners; exact/shared collision likely
38. box/box01.usd | box | EXACT_OR_SHARED_MESH_LIKELY | edges/corners; exact/shared collision likely
39. box/box02.usd | box | EXACT_OR_SHARED_MESH_LIKELY | edges/corners; exact/shared collision likely
40. tomato/tomato07.usd | tomato | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
41. tomato/tomato03.usd | tomato | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
42. tomato/tomato02.usd | tomato | ROUGH_PRIMITIVE_COLLISION | collision risk/stress case
43. potato/potato00.usd | potato | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
44. potato/potato17.usd | potato | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
45. potato/potato07.usd | potato | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
46. avocado/avocado04.usd | avocado | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
47. avocado/avocado05.usd | avocado | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match
48. avocado/avocado01.usd | avocado | BBOX_MATCH_BUT_SIMPLIFIED_COLLISION | simplified collision but bbox match

## Disk final
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  258G   29G  91% /
