import os
import yaml
from pathlib import Path

WS = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test")
REPO = WS / "franka_wrist_camera_isaaclab"
REPORT = WS / "reports/DIVERSE_OBJECT_RECEPTACLE_MATRIX_REPORT.md"

catalog = yaml.safe_load(open(REPO / "configs/object_catalog.generated.yaml"))
geometry = yaml.safe_load(open(REPO / "configs/object_geometry.generated.yaml"))

cat_dict = {c['id']: c for c in catalog['categories']}
geom_dict = {g['category_id'] + '/' + g['variant_id']: g for g in geometry['records']}

pairs = [
    # (obj_cat, obj_var, rec_cat, rec_var, description)
    ("apple", "apple01", "bowl", "bowl08", "apple -> deep bowl", "Visibly distinct red fruit placed in a deep container"),
    ("avocado", "avocado02", "bowl", "bowl01", "avocado -> shallow bowl", "Irregular green fruit placed in a shallow wide container"),
    ("can", "fcan03", "tray", "tray04", "can -> large tray", "Cylindrical soda can placed on a flat support surface"),
    ("box", "box01", "bowl", "bowl07", "box -> deep bowl", "Cuboid box object placed inside a deep curved bowl"),
    ("kiwi", "kiwi00", "bowl", "bowl10", "kiwi -> wide bowl", "Small fuzzy brown fruit placed in a wide deep bowl"),
    ("beer", "beer00", "box", "box00", "tall beer -> open box", "Tall cylindrical bottle/can placed inside a rectangular open box container")
]

lines = [
    "",
    "## Step 3 — Selection Report",
    "",
    "| Role | Category | Variant | USD Path | Dimensions (m) | Mass (kg) | Grasp | Affordances | Why Selected |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"
]

for obj_cat, obj_var, rec_cat, rec_var, label, reason in pairs:
    # Target Object
    c_obj = cat_dict[obj_cat]
    v_obj = [v for v in c_obj['variants'] if v['id'] == obj_var][0]
    g_obj = geom_dict[f"{obj_cat}/{obj_var}"]
    dim_obj = [
        round(g_obj['local_bbox_max'][i] - g_obj['local_bbox_min'][i], 4)
        for i in range(3)
    ]
    
    lines.append(
        f"| Object | {obj_cat} | {obj_var} | {v_obj.get('usd_path', '')} | {dim_obj} | {v_obj.get('mass', 'N/A') or 'N/A'} | {c_obj['grasp_strategy']} | {c_obj['affordances']} | {reason} |"
    )
    
    # Placement Receptacle
    c_rec = cat_dict[rec_cat]
    v_rec = [v for v in c_rec['variants'] if v['id'] == rec_var][0]
    g_rec = geom_dict[f"{rec_cat}/{rec_var}"]
    dim_rec = [
        round(g_rec['local_bbox_max'][i] - g_rec['local_bbox_min'][i], 4)
        for i in range(3)
    ]
    aff_rec = v_rec.get('affordances', c_rec['affordances'])
    grasp_rec = v_rec.get('grasp_strategy', c_rec['grasp_strategy'])
    
    lines.append(
        f"| Receptacle | {rec_cat} | {rec_var} | {v_rec.get('usd_path', '')} | {dim_rec} | {v_rec.get('mass', 'N/A') or 'N/A'} | {grasp_rec} | {aff_rec} | Receptacle target |"
    )

with open(REPORT, "a", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("Selection report appended successfully.")
