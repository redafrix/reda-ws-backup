from pathlib import Path
import json, csv, math
from collections import Counter
from pxr import Usd, UsdGeom, UsdPhysics, Gf

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
OBJ_ROOT = ROOT / "assets_staging/objects"
REPORTS = ROOT / "reports"

usd_files = sorted(list(OBJ_ROOT.rglob("*.usd")) + list(OBJ_ROOT.rglob("*.usda")))

COLLISION_NAME_HINTS = [
    "collision", "collider", "collisions", "colliders",
    "convex", "physics", "physx", "proxy", "col", "decomp"
]

VISUAL_PURPOSES = {"default", "render"}
COLLISION_PURPOSES = {"guide", "proxy"}

primitive_types = {"Cube", "Sphere", "Cylinder", "Cone", "Capsule"}

def vec_tuple(v):
    return tuple(float(x) for x in v)

def bbox_for_prims(stage, prims):
    if not prims:
        return None
    try:
        cache = UsdGeom.BBoxCache(0, ["default", "render", "proxy", "guide"])
        boxes = []
        for prim in prims:
            try:
                b = cache.ComputeWorldBound(prim).ComputeAlignedBox()
                if not b.IsEmpty():
                    boxes.append(b)
            except Exception:
                pass
        if not boxes:
            return None
        mn = Gf.Vec3d(
            min(b.GetMin()[0] for b in boxes),
            min(b.GetMin()[1] for b in boxes),
            min(b.GetMin()[2] for b in boxes),
        )
        mx = Gf.Vec3d(
            max(b.GetMax()[0] for b in boxes),
            max(b.GetMax()[1] for b in boxes),
            max(b.GetMax()[2] for b in boxes),
        )
        size = mx - mn
        return {
            "min": vec_tuple(mn),
            "max": vec_tuple(mx),
            "size": vec_tuple(size),
            "volume": float(max(size[0],0) * max(size[1],0) * max(size[2],0)),
        }
    except Exception as e:
        return {"error": repr(e)}

def mesh_counts(prim):
    try:
        mesh = UsdGeom.Mesh(prim)
        pts = mesh.GetPointsAttr().Get() or []
        fvc = mesh.GetFaceVertexCountsAttr().Get() or []
        return len(pts), len(fvc)
    except Exception:
        return 0, 0

def has_collision_api(prim):
    try:
        return prim.HasAPI(UsdPhysics.CollisionAPI)
    except Exception:
        return False

def get_purpose(prim):
    try:
        img = UsdGeom.Imageable(prim)
        attr = img.GetPurposeAttr()
        if attr:
            val = attr.Get()
            return str(val) if val else "default"
    except Exception:
        pass
    return "default"

def name_collision_hint(prim):
    s = str(prim.GetPath()).lower()
    return any(h in s for h in COLLISION_NAME_HINTS)

def safe_ratio(a, b):
    try:
        if b is None or b == 0:
            return None
        return float(a) / float(b)
    except Exception:
        return None

def bbox_ratio_metrics(vis, col):
    if not vis or not col or "size" not in vis or "size" not in col:
        return {}
    vs = vis["size"]
    cs = col["size"]
    ratios = []
    for c, v in zip(cs, vs):
        ratios.append(safe_ratio(c, v))
    vol_ratio = safe_ratio(col.get("volume"), vis.get("volume"))
    return {
        "size_ratio_x": ratios[0],
        "size_ratio_y": ratios[1],
        "size_ratio_z": ratios[2],
        "volume_ratio": vol_ratio,
    }

def ratio_good(r):
    vals = [r.get("size_ratio_x"), r.get("size_ratio_y"), r.get("size_ratio_z")]
    vals = [v for v in vals if v is not None]
    if len(vals) != 3:
        return False
    return all(0.85 <= v <= 1.15 for v in vals)

def ratio_bad(r):
    vals = [r.get("size_ratio_x"), r.get("size_ratio_y"), r.get("size_ratio_z")]
    vals = [v for v in vals if v is not None]
    if len(vals) != 3:
        return False
    return any(v < 0.60 or v > 1.60 for v in vals)

def inspect_file(path):
    rel = path.relative_to(OBJ_ROOT)
    category = rel.parts[0] if len(rel.parts) > 1 else "ROOT"

    row = {
        "category": category,
        "rel": str(rel),
        "file": str(path),
        "open_ok": False,
        "total_mesh_prims": 0,
        "visual_mesh_prims": 0,
        "collision_mesh_prims": 0,
        "collision_api_prims": 0,
        "collision_name_hint_prims": 0,
        "primitive_collision_prims": 0,
        "visual_points": 0,
        "visual_faces": 0,
        "collision_points": 0,
        "collision_faces": 0,
        "visual_bbox_size": "",
        "collision_bbox_size": "",
        "size_ratio_x": "",
        "size_ratio_y": "",
        "size_ratio_z": "",
        "volume_ratio": "",
        "verdict": "UNCLEAR",
        "notes": "",
    }

    try:
        stage = Usd.Stage.Open(str(path))
        if not stage:
            row["notes"] = "Stage.Open returned None"
            return row
        row["open_ok"] = True

        visual_prims = []
        collision_prims = []
        mesh_prims = []

        for prim in stage.Traverse():
            t = prim.GetTypeName()
            purpose = get_purpose(prim)
            coll_api = has_collision_api(prim)
            coll_hint = name_collision_hint(prim)

            if coll_api:
                row["collision_api_prims"] += 1
            if coll_hint:
                row["collision_name_hint_prims"] += 1

            if t in primitive_types and (coll_api or coll_hint or purpose in COLLISION_PURPOSES):
                row["primitive_collision_prims"] += 1
                collision_prims.append(prim)

            if t == "Mesh":
                mesh_prims.append(prim)
                pts, faces = mesh_counts(prim)
                
                # A mesh can be both
                is_coll = coll_api or coll_hint or purpose in COLLISION_PURPOSES
                # Visual if it's explicitly render/default AND not clearly ONLY collision
                is_vis = purpose in VISUAL_PURPOSES or (purpose == "default" and not coll_hint and purpose not in COLLISION_PURPOSES)

                if is_vis:
                    visual_prims.append(prim)
                    row["visual_points"] += pts
                    row["visual_faces"] += faces
                if is_coll:
                    collision_prims.append(prim)
                    row["collision_points"] += pts
                    row["collision_faces"] += faces

        row["total_mesh_prims"] = len(mesh_prims)
        row["visual_mesh_prims"] = len(visual_prims)
        row["collision_mesh_prims"] = len([p for p in collision_prims if p.GetTypeName() == "Mesh"])

        vis_bbox = bbox_for_prims(stage, visual_prims)
        col_bbox = bbox_for_prims(stage, collision_prims)

        if vis_bbox and "size" in vis_bbox:
            row["visual_bbox_size"] = ",".join(f"{x:.6f}" for x in vis_bbox["size"])
        if col_bbox and "size" in col_bbox:
            row["collision_bbox_size"] = ",".join(f"{x:.6f}" for x in col_bbox["size"])

        metrics = bbox_ratio_metrics(vis_bbox, col_bbox)
        for k in ["size_ratio_x", "size_ratio_y", "size_ratio_z", "volume_ratio"]:
            if k in metrics and metrics[k] is not None:
                row[k] = f"{metrics[k]:.4f}"

        if not collision_prims:
            row["verdict"] = "NO_COLLISION_FOUND"
        elif row["visual_points"] > 0 and row["collision_points"] == row["visual_points"] and ratio_good(metrics):
            row["verdict"] = "EXACT_OR_SHARED_MESH_LIKELY"
        elif ratio_good(metrics) and row["collision_points"] >= row["visual_points"] * 0.5:
            row["verdict"] = "GOOD_COLLISION_MATCH"
        elif ratio_good(metrics):
            row["verdict"] = "BBOX_MATCH_BUT_SIMPLIFIED_COLLISION"
        elif ratio_bad(metrics):
            row["verdict"] = "BAD_BBOX_MISMATCH"
        elif row["primitive_collision_prims"] > 0:
            row["verdict"] = "ROUGH_PRIMITIVE_COLLISION"
        else:
            row["verdict"] = "UNCLEAR_NEEDS_OVERLAY"

        return row

    except Exception as e:
        row["notes"] = repr(e)
        return row

rows = [inspect_file(p) for p in usd_files]

csv_path = REPORTS / "dom_collision_vs_visual_audit.csv"
json_path = REPORTS / "dom_collision_vs_visual_audit.json"

fieldnames = list(rows[0].keys()) if rows else []
with csv_path.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

json_path.write_text(json.dumps(rows, indent=2))

print("## Collision vs visual static audit")
print("usd_files:", len(rows))
print("csv:", csv_path)
print("json:", json_path)

from collections import Counter
print("\nverdict_counts:")
print(Counter(r["verdict"] for r in rows))
