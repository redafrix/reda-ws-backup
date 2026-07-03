import csv
from pathlib import Path
from franka_wrist_camera_scene.utils.paths import REPO_ROOT
from franka_wrist_camera_scene.objects.catalog import load_object_catalog
from franka_wrist_camera_scene.objects.geometry_registry import load_object_geometry_registry, get_object_geometry
from franka_wrist_camera_scene.validation.pick_place_preflight import (
    validate_pick_place_pair,
    load_physics_profiles,
    load_receptacle_compatibility,
)

def main():
    geometry_registry = load_object_geometry_registry()
    catalog = load_object_catalog(geometry_registry.catalog_config)
    physics_profiles = load_physics_profiles()
    compatibility = load_receptacle_compatibility()
    
    profiles = physics_profiles.get("profiles", {})
    validated_pairs = compatibility.get("validated_pairs", [])
    
    # 1. Separate target objects and receptacles from the catalog
    target_variants = []
    receptacle_variants = []
    
    for category in catalog.categories:
        # Check if category is a receptacle by affordance
        from franka_wrist_camera_scene.objects.selection import variant_affordances
        is_receptacle_category = any(aff in category.affordances for aff in ("container", "support"))
        
        for variant in category.variants:
            v_affs = variant_affordances(category, variant)
            is_receptacle = any(aff in v_affs for aff in ("container", "support"))
            
            # Receptacles
            if is_receptacle:
                receptacle_variants.append((category.id, variant.id))
            
            # Target objects (pickable)
            if "pickable" in v_affs:
                target_variants.append((category.id, variant.id))
                
    print(f"Found {len(target_variants)} target variants and {len(receptacle_variants)} receptacles.")
    
    csv_path = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/SMART_OBJECT_RECEPTACLE_PREFLIGHT_MATRIX.csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Stats counters
    total_objects_count = len(target_variants)
    missing_geo_count = 0
    oversized_obj_count = 0
    accepted_obj_variants = set()
    
    supported_validated_pairs_count = 0
    experimental_feasible_pairs_count = 0
    rejected_pairs_count = 0
    
    rows = []
    
    for obj_cat, obj_var in target_variants:
        obj_profile = profiles.get(obj_var, {})
        obj_status = obj_profile.get("status", "unknown")
        
        # Check geometry
        try:
            obj_geo = get_object_geometry(geometry_registry, obj_cat, obj_var)
            obj_dims = obj_geo.local_bbox_size
            obj_dims_str = f"[{obj_dims[0]:.4f}, {obj_dims[1]:.4f}, {obj_dims[2]:.4f}]"
        except KeyError:
            missing_geo_count += 1
            # Log failure row with None receptacle
            rows.append({
                "object_category": obj_cat,
                "object_variant": obj_var,
                "object_dimensions_m": "None",
                "object_mass_kg": "None",
                "profile_status": obj_status,
                "receptacle_category": "None",
                "receptacle_variant": "None",
                "receptacle_inner_dimensions_m": "None",
                "grasp_axis": "None",
                "required_grasp_width_m": "None",
                "usable_gripper_width_m": "None",
                "fit_clearance_m": "None",
                "accepted": "False",
                "rejection_code": "MISSING_OBJECT_GEOMETRY",
                "reason": "Missing geometry in registry",
            })
            continue

        obj_mass = obj_profile.get("mass_kg", "None")
        
        # Check if object is globally rejected for width
        is_globally_oversized = obj_status == "rejected" and obj_profile.get("rejection_code") == "OBJECT_TOO_WIDE_FOR_GRIPPER"
        if is_globally_oversized:
            oversized_obj_count += 1

        for rec_cat, rec_var in receptacle_variants:
            try:
                rec_geo = get_object_geometry(geometry_registry, rec_cat, rec_var)
            except KeyError:
                continue
            
            # Run preflight pair validation (we set reject_unknown_pairs=False to find experimental feasible pairs)
            res = validate_pick_place_pair(
                object_category_id=obj_cat,
                object_variant_id=obj_var,
                receptacle_category_id=rec_cat,
                receptacle_variant_id=rec_var,
                collection_policy={"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
            )
            
            # Usable / Fit clearances
            rec_inner_str = "None"
            if res.receptacle_inner_dimensions_m is not None:
                rec_inner = res.receptacle_inner_dimensions_m
                rec_inner_str = f"[{rec_inner[0]:.4f}, {rec_inner[1]:.4f}, {rec_inner[2]:.4f}]"
            
            fit_clearance = "None"
            if res.receptacle_inner_dimensions_m is not None:
                # fit clearance along min dimension
                fit_clearance = f"{min(rec_inner[0], rec_inner[1]) - min(obj_dims[0], obj_dims[1]):.4f}"
                
            if res.accepted:
                accepted_obj_variants.add(obj_var)
                
                # Check if validated
                is_validated = any(p.get("object") == obj_var and p.get("placement_target") == rec_var for p in validated_pairs)
                if is_validated:
                    supported_validated_pairs_count += 1
                else:
                    experimental_feasible_pairs_count += 1
            else:
                rejected_pairs_count += 1
                if res.code == "OBJECT_TOO_WIDE_FOR_GRIPPER" and not is_globally_oversized:
                    # Double-check if we missed counting it
                    is_globally_oversized = True
                    oversized_obj_count += 1
            
            rows.append({
                "object_category": obj_cat,
                "object_variant": obj_var,
                "object_dimensions_m": obj_dims_str,
                "object_mass_kg": str(obj_mass),
                "profile_status": obj_status,
                "receptacle_category": rec_cat,
                "receptacle_variant": rec_var,
                "receptacle_inner_dimensions_m": rec_inner_str,
                "grasp_axis": str(res.grasp_axis),
                "required_grasp_width_m": f"{res.required_grasp_width_m:.4f}" if res.required_grasp_width_m is not None else "None",
                "usable_gripper_width_m": f"{res.usable_gripper_width_m:.4f}" if res.usable_gripper_width_m is not None else "None",
                "fit_clearance_m": fit_clearance,
                "accepted": str(res.accepted),
                "rejection_code": res.code,
                "reason": res.reason,
            })
            
    # Write CSV
    headers = [
        "object_category", "object_variant", "object_dimensions_m", "object_mass_kg",
        "profile_status", "receptacle_category", "receptacle_variant",
        "receptacle_inner_dimensions_m", "grasp_axis", "required_grasp_width_m",
        "usable_gripper_width_m", "fit_clearance_m", "accepted", "rejection_code", "reason"
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Preflight matrix written to {csv_path}")
    
    # 2. Print Summary for Report
    summary = f"""
## Preflight Matrix Summary

- **Total Objects**: {total_objects_count}
- **Accepted Objects**: {len(accepted_obj_variants)} (variants with at least one feasible receptacle)
- **Rejected Oversized Objects**: {oversized_obj_count}
- **Rejected Missing-Geometry Objects**: {missing_geo_count}
- **Supported Validated Pairs**: {supported_validated_pairs_count}
- **Experimental Feasible Pairs**: {experimental_feasible_pairs_count}
- **Rejected Pairs**: {rejected_pairs_count}
"""
    print(summary)
    
    # Append to report
    report_path = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/SMART_OBJECT_RECEPTACLE_PREFLIGHT_REPORT.md")
    with open(report_path, "a", encoding="utf-8") as f:
        f.write("\n" + summary + "\n")

if __name__ == "__main__":
    main()
