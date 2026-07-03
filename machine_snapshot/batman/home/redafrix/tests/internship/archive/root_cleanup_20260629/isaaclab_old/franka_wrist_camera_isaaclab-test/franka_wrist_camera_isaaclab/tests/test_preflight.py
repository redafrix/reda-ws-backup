from unittest import TestCase
from franka_wrist_camera_scene.validation.pick_place_preflight import (
    validate_pick_place_pair,
    load_physics_profiles,
    load_receptacle_compatibility,
)
from scripts.collect import preflight_feasibility_check


class PickPlacePreflightTest(TestCase):
    def test_01_oversized_box_rejected(self) -> None:
        # box01 is explicitly marked as rejected with OBJECT_TOO_WIDE_FOR_GRIPPER
        res = validate_pick_place_pair(
            object_category_id="box",
            object_variant_id="box01",
            receptacle_category_id="bowl",
            receptacle_variant_id="bowl08",
            collection_policy={"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
        )
        self.assertFalse(res.accepted)
        self.assertEqual(res.code, "OBJECT_TOO_WIDE_FOR_GRIPPER")

    def test_02_narrow_grasp_axis_accepted(self) -> None:
        # fcan03 is supported and fits within standard gripper aperture
        res = validate_pick_place_pair(
            object_category_id="can",
            object_variant_id="fcan03",
            receptacle_category_id="tray",
            receptacle_variant_id="tray04",
            collection_policy={"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
        )
        self.assertTrue(res.accepted)

    def test_03_too_wide_both_axes_rejected(self) -> None:
        # Setting open_finger_m very small (e.g. 0.005m -> aperture 0.01m) forces rejection
        res = validate_pick_place_pair(
            object_category_id="apple",
            object_variant_id="apple01",
            receptacle_category_id="bowl",
            receptacle_variant_id="bowl08",
            collection_policy={"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
            open_finger_m=0.005,
        )
        self.assertFalse(res.accepted)
        self.assertEqual(res.code, "OBJECT_TOO_WIDE_FOR_GRIPPER")

    def test_04_larger_than_receptacle_rejected(self) -> None:
        # Setting receptacle_xy_clearance_m to a very large value (e.g. 1.0m) forces footprint fit rejection
        res = validate_pick_place_pair(
            object_category_id="avocado",
            object_variant_id="avocado02",
            receptacle_category_id="bowl",
            receptacle_variant_id="bowl08",
            collection_policy={"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
            preflight_cfg={"receptacle_xy_clearance_m": 1.0},
        )
        self.assertFalse(res.accepted)
        self.assertEqual(res.code, "OBJECT_DOES_NOT_FIT_RECEPTACLE")

    def test_05_missing_placement_target_rejected_in_strict(self) -> None:
        # In strict mode (require_real_receptacle = True), missing placement target is rejected
        res = validate_pick_place_pair(
            object_category_id="avocado",
            object_variant_id="avocado02",
            receptacle_category_id=None,
            receptacle_variant_id=None,
            collection_policy={"require_real_receptacle": True},
        )
        self.assertFalse(res.accepted)
        self.assertEqual(res.code, "MISSING_PLACEMENT_TARGET")

    def test_06_missing_geometry_rejected(self) -> None:
        # missing_geo_object has a profile but is missing from geometry registry
        res = validate_pick_place_pair(
            object_category_id="mock_cat",
            object_variant_id="missing_geo_object",
            receptacle_category_id="bowl",
            receptacle_variant_id="bowl08",
            collection_policy={"require_real_receptacle": True, "reject_unknown_objects": False, "reject_unknown_pairs": False},
        )
        self.assertFalse(res.accepted)
        self.assertEqual(res.code, "MISSING_OBJECT_GEOMETRY")

    def test_07_unsupported_profile_rejected(self) -> None:
        # beer00 is explicitly unsupported
        res = validate_pick_place_pair(
            object_category_id="beer",
            object_variant_id="beer00",
            receptacle_category_id="bowl",
            receptacle_variant_id="bowl01",
            collection_policy={"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
        )
        self.assertFalse(res.accepted)
        self.assertEqual(res.code, "UNSUPPORTED_OBJECT_PROFILE")

    def test_08_fcan03_profile_resolves(self) -> None:
        profiles = load_physics_profiles().get("profiles", {})
        self.assertIn("fcan03", profiles)
        self.assertEqual(profiles["fcan03"]["mass_kg"], 0.15)
        self.assertEqual(profiles["fcan03"]["top_grasp_depth_m"], 0.035)

    def test_09_apple_profile_resolves(self) -> None:
        profiles = load_physics_profiles().get("profiles", {})
        self.assertIn("apple01", profiles)
        self.assertEqual(profiles["apple01"]["top_grasp_depth_m"], 0.045)

    def test_10_old_target_area_mode_available(self) -> None:
        # In non-strict mode (require_real_receptacle = False), missing placement target is allowed
        res = validate_pick_place_pair(
            object_category_id="avocado",
            object_variant_id="avocado02",
            receptacle_category_id=None,
            receptacle_variant_id=None,
            collection_policy={"require_real_receptacle": False, "reject_unknown_objects": True, "reject_unknown_pairs": False},
        )
        self.assertTrue(res.accepted)

    def test_11_preflight_rejection_does_not_launch_isaac(self) -> None:
        # preflight_feasibility_check raises ValueError for rejected pair, stopping simulator launch
        config = {
            "target_object": {"category_id": "box", "variant_id": "box01"},
            "placement_target": {"category_id": "bowl", "variant_id": "bowl08"},
            "collection_policy": {"require_real_receptacle": True, "reject_unknown_objects": True, "reject_unknown_pairs": False},
        }
        with self.assertRaisesRegex(ValueError, "PREFLIGHT_REJECTED: OBJECT_TOO_WIDE_FOR_GRIPPER"):
            preflight_feasibility_check(config)
