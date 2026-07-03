from pathlib import Path
import json, csv, re
from pxr import Usd, UsdGeom, UsdShade, Sdf

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
OBJ_ROOT = ROOT / "assets_staging/objects"
REPORTS = ROOT / "reports"

usd_files = sorted(list(OBJ_ROOT.rglob("*.usd")) + list(OBJ_ROOT.rglob("*.usda")))

texture_exts = {".jpg", ".jpeg", ".png", ".tga", ".exr", ".hdr", ".bmp"}
primitive_types = {"Cube", "Sphere", "Cylinder", "Cone", "Capsule"}

rows = []

def get_bbox(stage, prim):
    try:
        cache = UsdGeom.BBoxCache(0, ["default", "render", "proxy"])
        box = cache.ComputeWorldBound(prim).ComputeAlignedBox()
        mn = box.GetMin()
        mx = box.GetMax()
        size = box.GetSize()
        return tuple(float(x) for x in mn), tuple(float(x) for x in mx), tuple(float(x) for x in size)
    except Exception:
        return None, None, None

def inspect_usd(path: Path):
    rel = path.relative_to(OBJ_ROOT)
    category = rel.parts[0] if len(rel.parts) > 1 else "ROOT"
    row = {
        "category": category,
        "file": str(path),
        "rel": str(rel),
        "open_ok": False,
        "mesh_count": 0,
        "primitive_count": 0,
        "xform_count": 0,
        "material_count": 0,
        "texture_ref_count": 0,
        "point_count": 0,
        "face_count": 0,
        "has_uv": False,
        "has_texture_files_nearby": False,
        "bbox_size": "",
        "quality_guess": "UNKNOWN",
        "notes": "",
    }
    try:
        stage = Usd.Stage.Open(str(path))
        if not stage:
            row["notes"] = "Usd.Stage.Open returned None"
            return row
        row["open_ok"] = True
        default = stage.GetDefaultPrim()
        root_prim = default if default and default.IsValid() else stage.GetPseudoRoot()
        _, _, size = get_bbox(stage, root_prim)
        if size:
            row["bbox_size"] = ",".join(f"{x:.4f}" for x in size)

        texture_refs = set()

        for prim in stage.Traverse():
            t = prim.GetTypeName()
            if t == "Mesh":
                row["mesh_count"] += 1
                mesh = UsdGeom.Mesh(prim)
                pts = mesh.GetPointsAttr().Get() or []
                row["point_count"] += len(pts)
                fvc = mesh.GetFaceVertexCountsAttr().Get() or []
                row["face_count"] += len(fvc)

                # UV primvars
                primvars = UsdGeom.PrimvarsAPI(prim).GetPrimvars()
                for pv in primvars:
                    if "st" in pv.GetName().lower() or "uv" in pv.GetName().lower():
                        row["has_uv"] = True

            elif t in primitive_types:
                row["primitive_count"] += 1
            elif t == "Xform":
                row["xform_count"] += 1
            elif t == "Material":
                row["material_count"] += 1

            # Scan attributes for asset texture references.
            for attr in prim.GetAttributes():
                try:
                    val = attr.Get()
                except Exception:
                    continue
                vals = val if isinstance(val, (list, tuple)) else [val]
                for v in vals:
                    s = str(v)
                    if any(ext in s.lower() for ext in texture_exts):
                        texture_refs.add(s)

        row["texture_ref_count"] = len(texture_refs)

        # nearby textures
        parent = path.parent
        nearby = []
        for ext in texture_exts:
            nearby += list(parent.rglob(f"*{ext}"))
        row["has_texture_files_nearby"] = len(nearby) > 0

        # Heuristic quality label.
        if row["mesh_count"] == 0 and row["primitive_count"] > 0:
            row["quality_guess"] = "LOW_PRIMITIVE_ONLY"
        elif row["mesh_count"] > 0 and row["point_count"] < 200 and row["texture_ref_count"] == 0 and not row["has_texture_files_nearby"]:
            row["quality_guess"] = "LOW_SIMPLE_MESH"
        elif row["mesh_count"] > 0 and row["point_count"] >= 1000 and (row["texture_ref_count"] > 0 or row["has_texture_files_nearby"]):
            row["quality_guess"] = "GOOD_TEXTURED_MESH"
        elif row["mesh_count"] > 0 and row["point_count"] >= 500:
            row["quality_guess"] = "MEDIUM_GEOMETRY_CHECK_VISUAL"
        else:
            row["quality_guess"] = "UNCLEAR_CHECK_VISUAL"

        return row
    except Exception as e:
        row["notes"] = repr(e)
        return row

for p in usd_files:
    rows.append(inspect_usd(p))

csv_path = REPORTS / "dom_object_asset_catalog.csv"
json_path = REPORTS / "dom_object_asset_catalog.json"

with csv_path.open("w", newline="") as f:
    if rows:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

json_path.write_text(json.dumps(rows, indent=2))

print("## Static USD asset audit")
print("usd_files:", len(usd_files))
print("csv:", csv_path)
print("json:", json_path)

from collections import Counter, defaultdict
print("\nquality_guess_counts:")
print(Counter(r["quality_guess"] for r in rows))
print("\ncategory_counts:")
print(Counter(r["category"] for r in rows))

print("\nTop 30 highest point_count:")
for r in sorted(rows, key=lambda x: x["point_count"], reverse=True)[:30]:
    print(r["category"], Path(r["file"]).name, "points", r["point_count"], "faces", r["face_count"], "textures", r["texture_ref_count"], "nearby_tex", r["has_texture_files_nearby"], "quality", r["quality_guess"])

print("\nPotential low-quality / primitive-only:")
for r in [x for x in rows if x["quality_guess"].startswith("LOW")][:60]:
    print(r["category"], Path(r["file"]).name, "mesh", r["mesh_count"], "prim", r["primitive_count"], "points", r["point_count"], "tex", r["texture_ref_count"], "note", r["notes"])
