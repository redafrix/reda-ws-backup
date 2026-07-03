from pathlib import Path
import json, math, time

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
OUT = ROOT / "reports/isaac_object_inspection"
OUT.mkdir(parents=True, exist_ok=True)
SHORTLIST = ROOT / "reports/dom_hard_object_shortlist.json"

objects = json.loads(SHORTLIST.read_text())

from isaacsim import SimulationApp
simulation_app = SimulationApp({
    "headless": True,
    "width": 1920,
    "height": 1080,
    "renderer": "RayTracedLighting",
})

import omni.usd
from pxr import UsdGeom, Gf, Sdf, UsdLux, UsdPhysics

ctx = omni.usd.get_context()
ctx.new_stage()
stage = ctx.get_stage()
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

# World
world = stage.DefinePrim("/World", "Xform")
stage.SetDefaultPrim(world)

# Ground plane
ground_prim = stage.DefinePrim("/World/Ground", "Cube")
ground = UsdGeom.Cube(ground_prim)
x_ground = UsdGeom.Xformable(ground_prim)
x_ground.ClearXformOpOrder()
x_ground.AddScaleOp().Set(Gf.Vec3f(8.0, 5.0, 0.02))
x_ground.AddTranslateOp().Set(Gf.Vec3f(0.0, 0.0, -0.02))

# Lights
dome_prim = stage.DefinePrim("/World/DomeLight", "DomeLight")
dome = UsdLux.DomeLight(dome_prim)
dome.CreateIntensityAttr(700)

sun_prim = stage.DefinePrim("/World/Sun", "DistantLight")
sun = UsdLux.DistantLight(sun_prim)
sun.CreateIntensityAttr(1200)
x_sun = UsdGeom.Xformable(sun_prim)
x_sun.ClearXformOpOrder()
x_sun.AddRotateXYZOp().Set(Gf.Vec3f(-45, 0, 35))

# Place objects in grid.
cols = 8
spacing_x = 0.55
spacing_y = 0.55

placed = []
for idx, obj in enumerate(objects):
    rel = obj["rel"]
    usd_path = ROOT / "assets_staging/objects" / rel
    row = idx // cols
    col = idx % cols
    x = (col - (cols-1)/2) * spacing_x
    y = -row * spacing_y + 1.0

    prim_path = f"/World/Objects/obj_{idx:02d}_{rel.replace('/', '_').replace('.usd','').replace('.usda','')}"
    prim = stage.DefinePrim(prim_path, "Xform")
    prim.GetReferences().AddReference(str(usd_path))
    
    xformable = UsdGeom.Xformable(prim)
    xformable.ClearXformOpOrder()
    xformable.AddTranslateOp().Set(Gf.Vec3f(x, y, 0.05))

    placed.append((prim_path, rel, x, y))

# Cameras
cam1_prim = stage.DefinePrim("/World/Camera_Overview", "Camera")
cam1 = UsdGeom.Camera(cam1_prim)
x1 = UsdGeom.Xformable(cam1_prim)
x1.ClearXformOpOrder()
x1.AddTranslateOp().Set(Gf.Vec3f(0.0, -5.2, 3.2))
x1.AddRotateXYZOp().Set(Gf.Vec3f(58, 0, 0))
cam1.CreateFocalLengthAttr(24)

cam2_prim = stage.DefinePrim("/World/Camera_Angle", "Camera")
cam2 = UsdGeom.Camera(cam2_prim)
x2 = UsdGeom.Xformable(cam2_prim)
x2.ClearXformOpOrder()
x2.AddTranslateOp().Set(Gf.Vec3f(3.0, -4.5, 2.4))
x2.AddRotateXYZOp().Set(Gf.Vec3f(58, 0, 35))
cam2.CreateFocalLengthAttr(28)

cam3_prim = stage.DefinePrim("/World/Camera_Close", "Camera")
cam3 = UsdGeom.Camera(cam3_prim)
x3 = UsdGeom.Xformable(cam3_prim)
x3.ClearXformOpOrder()
x3.AddTranslateOp().Set(Gf.Vec3f(0.0, -2.4, 1.2))
x3.AddRotateXYZOp().Set(Gf.Vec3f(63, 0, 0))
cam3.CreateFocalLengthAttr(45)

# Save the stage
stage_path = OUT / "dom_hard_objects_showroom.usd"
stage.GetRootLayer().Export(str(stage_path))
print("SHOWROOM_STAGE", stage_path)

# Render
import omni.kit.viewport.utility as vp_utils

viewport = vp_utils.get_active_viewport()
viewport.resolution = (1920, 1080)

def capture(camera_path, filename):
    viewport.camera_path = camera_path
    for _ in range(150): # More steps for loading high-point meshes
        simulation_app.update()
    out_path = OUT / filename
    try:
        from omni.kit.viewport.utility import capture_viewport_to_file
        capture_viewport_to_file(viewport, str(out_path))
        for _ in range(60):
            simulation_app.update()
        print("CAPTURE", out_path, "exists", out_path.exists())
    except Exception as e:
        print("CAPTURE_ERROR", camera_path, repr(e))

capture("/World/Camera_Overview", "showroom_overview.png")
capture("/World/Camera_Angle", "showroom_angle.png")
capture("/World/Camera_Close", "showroom_close_front.png")

print("PLACED_OBJECTS")
for i, (prim_path, rel, x, y) in enumerate(placed, 1):
    print(f"{i:02d} {rel} at x={x:.2f} y={y:.2f} prim={prim_path}")

simulation_app.close()
