from __future__ import annotations

import yaml
from dataclasses import dataclass
from pathlib import Path

from franka_wrist_camera_scene.utils.paths import REPO_ROOT
from franka_wrist_camera_scene.objects.geometry_registry import load_object_geometry_registry, get_object_geometry


@dataclass(frozen=True)
class PreflightResult:
    accepted: bool
    code: str
    reason: str
    grasp_axis: str | None
    required_grasp_width_m: float | None
    usable_gripper_width_m: float | None
    object_dimensions_m: tuple[float, float, float] | None
    receptacle_inner_dimensions_m: tuple[float, float, float] | None


def load_physics_profiles() -> dict:
    profile_path = REPO_ROOT / "configs" / "object_physics_profiles.yaml"
    if not profile_path.exists():
        return {"defaults": {"require_explicit_profile": True}, "profiles": {}}
    with open(profile_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_receptacle_compatibility() -> dict:
    compat_path = REPO_ROOT / "configs" / "object_receptacle_compatibility.yaml"
    if not compat_path.exists():
        return {"validated_pairs": [], "excluded_pairs": []}
    with open(compat_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def validate_pick_place_pair(
    object_category_id: str,
    object_variant_id: str,
    receptacle_category_id: str | None,
    receptacle_variant_id: str | None,
    collection_policy: dict | None = None,
    preflight_cfg: dict | None = None,
    open_finger_m: float = 0.04,  # Single finger displacement
) -> PreflightResult:
    # Set default configurations
    collection_policy = collection_policy or {}
    preflight_cfg = preflight_cfg or {}

    require_real_receptacle = collection_policy.get("require_real_receptacle", True)
    reject_unknown_objects = collection_policy.get("reject_unknown_objects", True)
    reject_unknown_pairs = collection_policy.get("reject_unknown_pairs", True)

    if not require_real_receptacle:
        return PreflightResult(
            accepted=True,
            code="ACCEPTED_REGRESSION_MODE",
            reason="Strict mode is disabled (require_real_receptacle=False). Accepted for regression testing.",
            grasp_axis=None,
            required_grasp_width_m=None,
            usable_gripper_width_m=None,
            object_dimensions_m=None,
            receptacle_inner_dimensions_m=None,
        )

    gripper_width_safety_margin_m = preflight_cfg.get("gripper_width_safety_margin_m", 0.008)
    receptacle_xy_clearance_m = preflight_cfg.get("receptacle_xy_clearance_m", 0.012)
    receptacle_wall_clearance_m = preflight_cfg.get("receptacle_wall_clearance_m", 0.010)
    approach_clearance_m = preflight_cfg.get("approach_clearance_m", 0.010)
    max_object_mass_kg = preflight_cfg.get("max_object_mass_kg", 0.8)
    max_object_height_m = preflight_cfg.get("max_object_height_m", 0.22)

    # 1. Load profiles and compatibility
    physics_profiles = load_physics_profiles()
    compatibility = load_receptacle_compatibility()

    defaults_cfg = physics_profiles.get("defaults", {})
    require_explicit_profile = defaults_cfg.get("require_explicit_profile", True)
    profiles = physics_profiles.get("profiles", {})

    # 2. Check Object Profile
    profile = profiles.get(object_variant_id)
    if profile is None:
        if require_explicit_profile or reject_unknown_objects:
            return PreflightResult(
                accepted=False,
                code="UNSUPPORTED_OBJECT_PROFILE",
                reason=f"Object variant '{object_variant_id}' has no configured physics profile.",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )
    else:
        status = profile.get("status", "experimental")
        if status == "rejected":
            rejection_code = profile.get("rejection_code", "UNSUPPORTED_OBJECT_PROFILE")
            return PreflightResult(
                accepted=False,
                code=rejection_code,
                reason=f"Object variant '{object_variant_id}' is explicitly rejected in physics profile: {profile.get('reason', '')}",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )
        elif status == "unsupported":
            return PreflightResult(
                accepted=False,
                code="UNSUPPORTED_OBJECT_PROFILE",
                reason=f"Object variant '{object_variant_id}' is marked as unsupported: {profile.get('reason', '')}",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )
        elif reject_unknown_objects and status not in ("supported", "experimental"):
            return PreflightResult(
                accepted=False,
                code="UNSUPPORTED_OBJECT_PROFILE",
                reason=f"Object variant '{object_variant_id}' profile status is '{status}' (not supported).",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )

    # 3. Check Placement Target existence
    if require_real_receptacle:
        if not receptacle_category_id or not receptacle_variant_id:
            return PreflightResult(
                accepted=False,
                code="MISSING_PLACEMENT_TARGET",
                reason="strict collection mode requires a real placement target, but none was specified.",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )

    # 4. Load Geometry
    try:
        geometry_registry = load_object_geometry_registry()
    except Exception as e:
        return PreflightResult(
            accepted=False,
            code="MISSING_OBJECT_GEOMETRY",
            reason=f"Failed to load object geometry registry: {e}",
            grasp_axis=None,
            required_grasp_width_m=None,
            usable_gripper_width_m=None,
            object_dimensions_m=None,
            receptacle_inner_dimensions_m=None,
        )

    try:
        obj_geo = get_object_geometry(geometry_registry, object_category_id, object_variant_id)
    except KeyError:
        return PreflightResult(
            accepted=False,
            code="MISSING_OBJECT_GEOMETRY",
            reason=f"Missing geometry registry record for target object variant: '{object_category_id}/{object_variant_id}'",
            grasp_axis=None,
            required_grasp_width_m=None,
            usable_gripper_width_m=None,
            object_dimensions_m=None,
            receptacle_inner_dimensions_m=None,
        )

    # Receptacle details
    rec_geo = None
    if receptacle_category_id and receptacle_variant_id:
        try:
            rec_geo = get_object_geometry(geometry_registry, receptacle_category_id, receptacle_variant_id)
        except KeyError:
            return PreflightResult(
                accepted=False,
                code="MISSING_OBJECT_GEOMETRY",
                reason=f"Missing geometry registry record for receptacle variant: '{receptacle_category_id}/{receptacle_variant_id}'",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )

    # 5. Check Receptacle Affordance
    if rec_geo is not None:
        # Load from catalog to check affordance
        # In catalog.py, we can load the catalog
        from franka_wrist_camera_scene.objects.catalog import load_object_catalog
        try:
            catalog = load_object_catalog(geometry_registry.catalog_config)
            category_matches = [c for c in catalog.categories if c.id == receptacle_category_id]
            if not category_matches:
                return PreflightResult(
                    accepted=False,
                    code="INVALID_RECEPTACLE_AFFORDANCE",
                    reason=f"Receptacle category '{receptacle_category_id}' not found in catalog.",
                    grasp_axis=None,
                    required_grasp_width_m=None,
                    usable_gripper_width_m=None,
                    object_dimensions_m=None,
                    receptacle_inner_dimensions_m=None,
                )
            category = category_matches[0]
            variant_matches = [v for v in category.variants if v.id == receptacle_variant_id]
            if not variant_matches:
                return PreflightResult(
                    accepted=False,
                    code="INVALID_RECEPTACLE_AFFORDANCE",
                    reason=f"Receptacle variant '{receptacle_variant_id}' not found in catalog.",
                    grasp_axis=None,
                    required_grasp_width_m=None,
                    usable_gripper_width_m=None,
                    object_dimensions_m=None,
                    receptacle_inner_dimensions_m=None,
                )
            variant = variant_matches[0]
            from franka_wrist_camera_scene.objects.selection import variant_affordances
            affordances = variant_affordances(category, variant)
            if not any(aff in affordances for aff in ("container", "support")):
                return PreflightResult(
                    accepted=False,
                    code="INVALID_RECEPTACLE_AFFORDANCE",
                    reason=f"Receptacle '{receptacle_variant_id}' has invalid affordances: {affordances}. Must have 'container' or 'support'.",
                    grasp_axis=None,
                    required_grasp_width_m=None,
                    usable_gripper_width_m=None,
                    object_dimensions_m=None,
                    receptacle_inner_dimensions_m=None,
                )
        except Exception as e:
            return PreflightResult(
                accepted=False,
                code="INVALID_RECEPTACLE_AFFORDANCE",
                reason=f"Failed to verify receptacle catalog affordances: {e}",
                grasp_axis=None,
                required_grasp_width_m=None,
                usable_gripper_width_m=None,
                object_dimensions_m=None,
                receptacle_inner_dimensions_m=None,
            )

    # 6. Gripper Feasibility
    usable_aperture = 2 * open_finger_m - gripper_width_safety_margin_m
    grasp_axis = None
    required_grasp_width_m = None

    if obj_geo.yaw_relevant:
        grasp_axis = "minor"
        required_grasp_width_m = obj_geo.planar_extent_minor
    else:
        # Check both X and Y dimensions, take the smaller one as the target grasp width
        grasp_axis = "smaller_horizontal"
        required_grasp_width_m = min(obj_geo.local_bbox_size[0], obj_geo.local_bbox_size[1])

    if required_grasp_width_m > usable_aperture:
        return PreflightResult(
            accepted=False,
            code="OBJECT_TOO_WIDE_FOR_GRIPPER",
            reason=f"Object required grasp width ({required_grasp_width_m:.4f}m) exceeds usable gripper aperture ({usable_aperture:.4f}m).",
            grasp_axis=grasp_axis,
            required_grasp_width_m=required_grasp_width_m,
            usable_gripper_width_m=usable_aperture,
            object_dimensions_m=obj_geo.local_bbox_size,
            receptacle_inner_dimensions_m=None,
        )

    # Approach height check
    if obj_geo.local_bbox_size[2] > max_object_height_m:
        return PreflightResult(
            accepted=False,
            code="OBJECT_TOO_TALL_FOR_APPROACH",
            reason=f"Object height ({obj_geo.local_bbox_size[2]:.4f}m) exceeds configured approach limit ({max_object_height_m:.4f}m).",
            grasp_axis=grasp_axis,
            required_grasp_width_m=required_grasp_width_m,
            usable_gripper_width_m=usable_aperture,
            object_dimensions_m=obj_geo.local_bbox_size,
            receptacle_inner_dimensions_m=None,
        )

    # Mass check
    # Check if object mass is specified in profile or override
    mass_val = None
    if profile is not None and profile.get("mass_kg") is not None:
        mass_val = profile.get("mass_kg")
    
    # Check if a custom mass exists in overrides
    if preflight_cfg.get("target_mass") is not None:
        mass_val = preflight_cfg.get("target_mass")

    if mass_val is not None and mass_val > max_object_mass_kg:
        return PreflightResult(
            accepted=False,
            code="OBJECT_TOO_HEAVY",
            reason=f"Object mass ({mass_val:.4f}kg) exceeds configured limit ({max_object_mass_kg:.4f}kg).",
            grasp_axis=grasp_axis,
            required_grasp_width_m=required_grasp_width_m,
            usable_gripper_width_m=usable_aperture,
            object_dimensions_m=obj_geo.local_bbox_size,
            receptacle_inner_dimensions_m=None,
        )

    # 7. Receptacle Fit check
    inner_dim = None
    if rec_geo is not None:
        # Calculate inner footprint
        if receptacle_category_id == "bowl":
            outer_d = min(rec_geo.local_bbox_size[0], rec_geo.local_bbox_size[1])
            inner_diameter = outer_d - 2 * receptacle_wall_clearance_m
            inner_x = inner_diameter
            inner_y = inner_diameter
        else:
            inner_x = rec_geo.local_bbox_size[0] - 2 * receptacle_wall_clearance_m
            inner_y = rec_geo.local_bbox_size[1] - 2 * receptacle_wall_clearance_m
        
        inner_z = rec_geo.local_bbox_size[2] # Depth
        inner_dim = (inner_x, inner_y, inner_z)

        if inner_x <= 0 or inner_y <= 0:
            return PreflightResult(
                accepted=False,
                code="INSUFFICIENT_RECEPTACLE_CLEARANCE",
                reason=f"Receptacle inner bounds are non-positive after subtracting clearance: ({inner_x:.4f}, {inner_y:.4f}).",
                grasp_axis=grasp_axis,
                required_grasp_width_m=required_grasp_width_m,
                usable_gripper_width_m=usable_aperture,
                object_dimensions_m=obj_geo.local_bbox_size,
                receptacle_inner_dimensions_m=inner_dim,
            )

        # Footprint fit check
        obj_x, obj_y, obj_z = obj_geo.local_bbox_size
        if receptacle_category_id == "bowl":
            obj_max_horiz = max(obj_x, obj_y)
            if obj_max_horiz + receptacle_xy_clearance_m > inner_x:
                return PreflightResult(
                    accepted=False,
                    code="OBJECT_DOES_NOT_FIT_RECEPTACLE",
                    reason=f"Object max footprint ({obj_max_horiz:.4f}m) + clearance ({receptacle_xy_clearance_m:.4f}m) does not fit inside bowl inner diameter ({inner_x:.4f}m).",
                    grasp_axis=grasp_axis,
                    required_grasp_width_m=required_grasp_width_m,
                    usable_gripper_width_m=usable_aperture,
                    object_dimensions_m=obj_geo.local_bbox_size,
                    receptacle_inner_dimensions_m=inner_dim,
                )
        else:
            # Check rectangular fit (can be aligned or rotated 90 deg)
            fit_aligned = (obj_x + receptacle_xy_clearance_m <= inner_x) and (obj_y + receptacle_xy_clearance_m <= inner_y)
            fit_rotated = (obj_y + receptacle_xy_clearance_m <= inner_x) and (obj_x + receptacle_xy_clearance_m <= inner_y)
            if not (fit_aligned or fit_rotated):
                return PreflightResult(
                    accepted=False,
                    code="OBJECT_DOES_NOT_FIT_RECEPTACLE",
                    reason=f"Object footprint ({obj_x:.4f}x{obj_y:.4f}m) + clearance ({receptacle_xy_clearance_m:.4f}m) does not fit inside rectangular receptacle inner bounds ({inner_x:.4f}x{inner_y:.4f}m).",
                    grasp_axis=grasp_axis,
                    required_grasp_width_m=required_grasp_width_m,
                    usable_gripper_width_m=usable_aperture,
                    object_dimensions_m=obj_geo.local_bbox_size,
                    receptacle_inner_dimensions_m=inner_dim,
                )

        # Gripper approach clearance check
        # We need to verify if the gripper enters the receptacle and has enough clearance
        # relative height calculation
        receptacle_release_bottom_clearance_m = 0.015  # Default release height clearance
        top_grasp_depth_m = 0.025
        if profile is not None and profile.get("top_grasp_depth_m") is not None:
            top_grasp_depth_m = profile.get("top_grasp_depth_m")

        # Object top position relative to receptacle bottom
        obj_top_rel = receptacle_release_bottom_clearance_m + obj_z
        # Gripper bottom relative to receptacle bottom
        gripper_bottom_rel = obj_top_rel - top_grasp_depth_m
        
        if gripper_bottom_rel < inner_z:
            # Gripper enters receptacle during release. Verify width clearance.
            gripper_full_width = 2 * open_finger_m
            required_opening_with_clearance = gripper_full_width + approach_clearance_m
            
            if receptacle_category_id == "bowl":
                if required_opening_with_clearance > inner_diameter:
                    return PreflightResult(
                        accepted=False,
                        code="INSUFFICIENT_RECEPTACLE_CLEARANCE",
                        reason=f"Gripper enters bowl (gripper_bottom={gripper_bottom_rel:.4f}m < bowl_depth={inner_z:.4f}m). Open gripper width + approach clearance ({required_opening_with_clearance:.4f}m) exceeds bowl inner diameter ({inner_diameter:.4f}m).",
                        grasp_axis=grasp_axis,
                        required_grasp_width_m=required_grasp_width_m,
                        usable_gripper_width_m=usable_aperture,
                        object_dimensions_m=obj_geo.local_bbox_size,
                        receptacle_inner_dimensions_m=inner_dim,
                    )
            else:
                # For rectangular, gripper enters. The gripper typically approaches aligned with one of the axes.
                # It must fit along the maximum or both axes.
                # To be conservative, check if the required opening fits in the receptacle width.
                if required_opening_with_clearance > max(inner_x, inner_y):
                    return PreflightResult(
                        accepted=False,
                        code="INSUFFICIENT_RECEPTACLE_CLEARANCE",
                        reason=f"Gripper enters container (gripper_bottom={gripper_bottom_rel:.4f}m < depth={inner_z:.4f}m). Open gripper width + approach clearance ({required_opening_with_clearance:.4f}m) exceeds container inner bounds max footprint ({max(inner_x, inner_y):.4f}m).",
                        grasp_axis=grasp_axis,
                        required_grasp_width_m=required_grasp_width_m,
                        usable_gripper_width_m=usable_aperture,
                        object_dimensions_m=obj_geo.local_bbox_size,
                        receptacle_inner_dimensions_m=inner_dim,
                    )

    # 8. Pair compatibility checks
    if rec_geo is not None:
        # Excluded pairs check
        excluded_pairs = compatibility.get("excluded_pairs", [])
        for pair in excluded_pairs:
            if pair.get("object") == object_variant_id and pair.get("placement_target") == receptacle_variant_id:
                return PreflightResult(
                    accepted=False,
                    code="UNSUPPORTED_OBJECT_RECEPTACLE_PAIR",
                    reason=f"Pair '{object_variant_id} -> {receptacle_variant_id}' is explicitly excluded: {pair.get('reason', '')}",
                    grasp_axis=grasp_axis,
                    required_grasp_width_m=required_grasp_width_m,
                    usable_gripper_width_m=usable_aperture,
                    object_dimensions_m=obj_geo.local_bbox_size,
                    receptacle_inner_dimensions_m=inner_dim,
                )

        # Validated pairs check
        if reject_unknown_pairs:
            validated_pairs = compatibility.get("validated_pairs", [])
            is_validated = False
            for pair in validated_pairs:
                if pair.get("object") == object_variant_id and pair.get("placement_target") == receptacle_variant_id:
                    is_validated = True
                    break
            if not is_validated:
                return PreflightResult(
                    accepted=False,
                    code="UNSUPPORTED_OBJECT_RECEPTACLE_PAIR",
                    reason=f"Pair '{object_variant_id} -> {receptacle_variant_id}' is not in the validated pairs registry.",
                    grasp_axis=grasp_axis,
                    required_grasp_width_m=required_grasp_width_m,
                    usable_gripper_width_m=usable_aperture,
                    object_dimensions_m=obj_geo.local_bbox_size,
                    receptacle_inner_dimensions_m=inner_dim,
                )

    return PreflightResult(
        accepted=True,
        code="ACCEPTED",
        reason="Object and receptacle pair passed all preflight feasibility audits.",
        grasp_axis=grasp_axis,
        required_grasp_width_m=required_grasp_width_m,
        usable_gripper_width_m=usable_aperture,
        object_dimensions_m=obj_geo.local_bbox_size,
        receptacle_inner_dimensions_m=inner_dim,
    )
