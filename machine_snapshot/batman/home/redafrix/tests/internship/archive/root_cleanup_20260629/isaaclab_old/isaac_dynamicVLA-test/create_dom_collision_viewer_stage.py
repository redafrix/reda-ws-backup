from pathlib import Path
import json, math

from pxr import Usd, UsdGeom, Gf, UsdLux, Sdf

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
OUT_DIR = ROOT / "reports/real_collision_viewer"
OUT_DIR.mkdir(parents=True, exist_ok=True)

shortlist_path = ROOT / "reports/dom_hard_object_shortlist.json"
collision_path = ROOT / "reports/dom_collision_vs_visual_audit.json"

shortlist = json.loads(shortlist_path.read_text())
collision_rows = {r["rel"]: r for r in json.loads(collision_path.read_text())}

# Make the viewer readable: pick hard categories and stress cases.
priority_cats = ["bowl", "cup", "bottle", "can", "tray", "plate", "box", "tomato", "kiwi", "lime", "peach", "tangerine"]
selected = []
seen = set()

def add(obj):
    if obj["rel"] not in seen:
        selected.append(obj)
        seen.add(obj["rel"])

# Select up to 32 objects: hard/common + bad/stress cases.
for cat in priority_cats:
    cat_objs = [o for o in shortlist if o.get("category") == cat]
    for o in cat_objs[:3]:
        add(o)

for o in shortlist:
    verdict = o.get("collision_verdict", "")
    if verdict in ["ROUGH_PRIMITIVE_COLLISION", "BAD_BBOX_MISMATCH"]:
        add(o)

selected = selected[:32]

stage_path = OUT_DIR / "dom_collision_viewer_stage.usd"
if stage_path.exists():
    stage_path.unlink()

stage = Usd.Stage.CreateNew(str(stage_path))
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

# Ground plane.
ground = UsdGeom.Cube.Define(stage, "/World/Ground")
ground.AddScaleOp().Set(Gf.Vec3f(5.0, 4.0, 0.01))
ground.AddTranslateOp().Set(Gf.Vec3f(0, 0, -0.02))

# Lights.
dome = UsdLux.DomeLight.Define(stage, "/World/DomeLight")
dome.CreateIntensityAttr(800)

sun = UsdLux.DistantLight.Define(stage, "/World/Sun")
sun.CreateIntensityAttr(1400)
sun.AddRotateXYZOp().Set(Gf.Vec3f(-50, 0, 35))

# Camera.
cam = UsdGeom.Camera.Define(stage, "/World/Camera")
cam.AddTranslateOp().Set(Gf.Vec3f(0.0, -4.5, 2.6))
cam.AddRotateXYZOp().Set(Gf.Vec3f(58, 0, 0))
cam.CreateFocalLengthAttr(28)

# Place objects.
cols = 8
spacing_x = 0.55
spacing_y = 0.55

objects_root = UsdGeom.Xform.Define(stage, "/World/Objects")

placed = []
for idx, obj in enumerate(selected):
    rel = obj["rel"]
    # FIX: Correct asset path
    usd_path = ROOT / "assets_staging/objects" / rel
    cat = obj.get("category", rel.split("/")[0])
    verdict = obj.get("collision_verdict", collision_rows.get(rel, {}).get("verdict", "UNKNOWN"))

    row = idx // cols
    col = idx % cols
    x = (col - (cols - 1) / 2) * spacing_x
    y = 1.2 - row * spacing_y

    safe = rel.replace("/", "_").replace(".usd", "").replace(".usda", "").replace("-", "_")
    prim_path = f"/World/Objects/o{idx:02d}_{cat}_{safe}"

    xform = UsdGeom.Xform.Define(stage, prim_path)
    xform.GetPrim().GetReferences().AddReference(str(usd_path))
    
    # FIX: Clear Xform Op Order to avoid conflict with referenced asset transformations
    xform.ClearXformOpOrder()
    xform.AddTranslateOp().Set(Gf.Vec3f(x, y, 0.05))

    # Add custom metadata-like attributes for inspection.
    xform.GetPrim().CreateAttribute("userProperties:source_rel", Sdf.ValueTypeNames.String).Set(rel)
    xform.GetPrim().CreateAttribute("userProperties:collision_verdict", Sdf.ValueTypeNames.String).Set(verdict)

    placed.append({
        "index": idx,
        "rel": rel,
        "prim_path": prim_path,
        "category": cat,
        "collision_verdict": verdict,
        "x": x,
        "y": y,
    })

stage.GetRootLayer().Save()

(OUT_DIR / "placed_objects.json").write_text(json.dumps(placed, indent=2))

print("STAGE_CREATED", stage_path)
print("PLACED_COUNT", len(placed))
