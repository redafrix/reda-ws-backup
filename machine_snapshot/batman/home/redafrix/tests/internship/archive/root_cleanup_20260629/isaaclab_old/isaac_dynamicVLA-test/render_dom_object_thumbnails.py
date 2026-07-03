from pathlib import Path
import json, math, sys, os

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
OBJ_ROOT = ROOT / "assets_staging/objects"
OUT = ROOT / "reports/object_thumbnails"
OUT.mkdir(parents=True, exist_ok=True)

rows = json.loads((ROOT / "reports/dom_object_asset_catalog.json").read_text())

priority_terms = ["mug", "cup", "banana", "bowl", "bottle", "can", "tomato", "apple", "orange", "lemon", "peach", "kiwi", "tangerine", "avocado", "egg", "beer", "tray", "box"]

selected = []
for term in priority_terms:
    matches = [r for r in rows if term in r["category"].lower() or term in Path(r["file"]).name.lower()]
    # Pick best few by point count / texture availability.
    matches = sorted(matches, key=lambda r: (r["quality_guess"] == "GOOD_TEXTURED_MESH", r["point_count"], r["texture_ref_count"]), reverse=True)
    selected += matches[:3]

# Deduplicate.
seen = set()
selected2 = []
for r in selected:
    if r["file"] not in seen:
        selected2.append(r)
        seen.add(r["file"])
selected = selected2[:50]

print("selected_count", len(selected))
for r in selected:
    print("SELECTED", r["rel"], r["quality_guess"], r["point_count"])

# Try Isaac rendering.
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": True, "width": 256, "height": 256})

import omni.usd
from pxr import Usd, UsdGeom, Gf, Sdf

# Note: robust screenshot APIs vary across Isaac versions.
# We create stages with the asset referenced, camera and light, then use viewport capture if available.
import omni.kit.viewport.utility as vp_utils

def clear_stage():
    ctx = omni.usd.get_context()
    ctx.new_stage()
    return ctx.get_stage()

def setup_asset(path):
    stage = clear_stage()
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    asset_prim = stage.DefinePrim("/World/Object", "Xform")
    asset_prim.GetReferences().AddReference(str(path))

    # Light
    light = stage.DefinePrim("/World/DistantLight", "DistantLight")
    light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(600.0)

    # Camera
    cam = UsdGeom.Camera.Define(stage, "/World/Camera")
    cam.AddTranslateOp().Set(Gf.Vec3d(1.2, -1.2, 0.8))
    cam.AddRotateXYZOp().Set(Gf.Vec3f(60, 0, 45))
    stage.SetDefaultPrim(asset_prim)

    return stage

def capture(path, out_path):
    try:
        setup_asset(path)

        viewport = vp_utils.get_active_viewport()
        viewport.camera_path = "/World/Camera"
        # Let stage render a few frames
        for _ in range(30):
            simulation_app.update()

        from omni.kit.viewport.utility import capture_viewport_to_file
        capture_viewport_to_file(viewport, str(out_path))
        for _ in range(10):
            simulation_app.update()
        return out_path.exists()
    except Exception as e:
        print("CAPTURE_ERROR", path, repr(e))
        import traceback
        traceback.print_exc()
        return False

results = []
for r in selected:
    p = Path(r["file"])
    safe = r["rel"].replace("/", "__").replace(".usd", ".png").replace(".usda", ".png")
    out_path = OUT / safe
    ok = capture(p, out_path)
    print("RENDER", r["rel"], "->", out_path, "ok", ok)
    results.append({"rel": r["rel"], "thumbnail": str(out_path), "ok": ok})

(ROOT / "reports/object_thumbnail_results.json").write_text(json.dumps(results, indent=2))

simulation_app.close()
