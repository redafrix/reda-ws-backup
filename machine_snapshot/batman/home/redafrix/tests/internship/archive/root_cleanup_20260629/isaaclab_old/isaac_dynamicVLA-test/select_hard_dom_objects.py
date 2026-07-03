from pathlib import Path
import json, csv

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
reports = ROOT / "reports"

asset_catalog = json.loads((reports / "dom_object_asset_catalog.json").read_text())
collision_audit = json.loads((reports / "dom_collision_vs_visual_audit.json").read_text())

by_rel_asset = {r["rel"]: r for r in asset_catalog}
by_rel_col = {r["rel"]: r for r in collision_audit}

priority_categories = {
    "cup": 100,
    "bowl": 95,
    "bottle": 90,
    "can": 88,
    "tray": 86,
    "plate": 84,
    "box": 82,
    "tomato": 70,
    "potato": 68,
    "avocado": 66,
    "egg": 64,
    "beer": 62,
    "peach": 60,
    "kiwi": 58,
    "tangerine": 56,
    "apple": 40,
    "orange": 38,
    "lemon": 36,
    "lime": 34,
    "onion": 32,
}

collision_score = {
    "EXACT_OR_SHARED_MESH_LIKELY": 30,
    "BBOX_MATCH_BUT_SIMPLIFIED_COLLISION": 15,
    "ROUGH_PRIMITIVE_COLLISION": -10,
    "BAD_BBOX_MISMATCH": -40,
}

shape_bonus = {
    "cup": 25,       # hollow/open top
    "bowl": 25,      # hollow/open top
    "tray": 20,      # thin + open
    "plate": 18,     # thin/flat
    "bottle": 18,    # tall/narrow
    "can": 16,       # cylinder grasping
    "box": 15,       # edges/corners
    "beer": 15,
    "tomato": 8,
    "potato": 8,
    "avocado": 8,
}

rows = []
for rel, col in by_rel_col.items():
    cat = col.get("category", rel.split("/")[0])
    asset = by_rel_asset.get(rel, {})
    base = priority_categories.get(cat, 10)
    score = base
    score += collision_score.get(col.get("verdict"), 0)
    score += shape_bonus.get(cat, 0)

    # Prefer visually detailed mesh, but don't make this only about visuals.
    pts = int(asset.get("point_count", 0) or col.get("visual_points", 0) or 0)
    if pts > 50000:
        score += 12
    elif pts > 5000:
        score += 8
    elif pts > 1000:
        score += 4

    # Penalize obvious bad collision, but keep a few bad examples for stress inspection.
    verdict = col.get("verdict", "")
    if verdict == "BAD_BBOX_MISMATCH":
        score -= 20

    reason = []
    if cat in ["cup", "bowl"]:
        reason.append("hollow/open-top")
    if cat in ["bottle", "can", "beer"]:
        reason.append("tall/cylindrical grasping")
    if cat in ["tray", "plate", "placemat"]:
        reason.append("thin/flat object")
    if cat == "box":
        reason.append("edges/corners")
    if verdict == "EXACT_OR_SHARED_MESH_LIKELY":
        reason.append("exact/shared collision likely")
    elif verdict == "BBOX_MATCH_BUT_SIMPLIFIED_COLLISION":
        reason.append("simplified collision but bbox match")
    elif verdict in ["ROUGH_PRIMITIVE_COLLISION", "BAD_BBOX_MISMATCH"]:
        reason.append("collision risk/stress case")

    rows.append({
        "rel": rel,
        "file": str(ROOT / "assets_staging/objects" / rel),
        "category": cat,
        "score": score,
        "collision_verdict": verdict,
        "visual_points": col.get("visual_points"),
        "collision_points": col.get("collision_points"),
        "quality_guess": asset.get("quality_guess", ""),
        "point_count": asset.get("point_count", ""),
        "reason": "; ".join(reason),
    })

rows = sorted(rows, key=lambda r: r["score"], reverse=True)

# Take a balanced set:
# - top hard objects
# - include at least some from each key category
selected = []
seen = set()

def add(row):
    if row["rel"] not in seen:
        selected.append(row)
        seen.add(row["rel"])

# top globally
for r in rows[:25]:
    add(r)

# ensure category coverage
for cat in ["cup", "bowl", "bottle", "can", "tray", "plate", "box", "tomato", "potato", "avocado", "beer"]:
    cat_rows = [r for r in rows if r["category"] == cat]
    for r in cat_rows[:3]:
        add(r)

# include a few bad/stress cases
for r in rows:
    if r["collision_verdict"] in ["ROUGH_PRIMITIVE_COLLISION", "BAD_BBOX_MISMATCH"]:
        add(r)
    if len([x for x in selected if x["collision_verdict"] in ["ROUGH_PRIMITIVE_COLLISION", "BAD_BBOX_MISMATCH"]]) >= 8:
        break

selected = selected[:48]

json_path = reports / "dom_hard_object_shortlist.json"
csv_path = reports / "dom_hard_object_shortlist.csv"
json_path.write_text(json.dumps(selected, indent=2))

with csv_path.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(selected[0].keys()))
    w.writeheader()
    w.writerows(selected)

print("SHORTLIST_JSON", json_path)
print("SHORTLIST_CSV", csv_path)
print("selected_count", len(selected))
print()
for i, r in enumerate(selected, 1):
    print(f"{i:02d}. {r['rel']} | score={r['score']} | {r['collision_verdict']} | {r['reason']}")
