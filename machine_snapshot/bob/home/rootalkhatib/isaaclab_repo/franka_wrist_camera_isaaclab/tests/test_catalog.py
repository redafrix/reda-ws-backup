"""Unit tests for catalog generator semantic and physical affordances."""

from __future__ import annotations

import unittest

from franka_wrist_camera_scene.objects.catalog_generator import (
    CATEGORY_LABEL_OVERRIDES,
    PHYSICAL_CONTAINER_CATEGORIES,
    SUPPORT_RECEPTACLE_CATEGORIES,
    VARIANT_AFFORDANCE_OVERRIDES,
    VARIANT_GRASP_STRATEGY_OVERRIDES,
    VERIFIED_PHYSICAL_CONTAINER_VARIANTS,
    affordances_for_label,
    grasp_strategy_for_label,
    label_for_category_id,
    role_for_label,
)


class CatalogGeneratorTests(unittest.TestCase):
    def test_cups_are_visual_containers_not_physical_receptacles(self) -> None:
        self.assertEqual(affordances_for_label("cup"), ["reachable", "container"])
        self.assertNotIn(("cup", "cup00"), VERIFIED_PHYSICAL_CONTAINER_VARIANTS)

    def test_physical_receptacle_categories_get_physical_container_affordance(self) -> None:
        self.assertGreaterEqual(PHYSICAL_CONTAINER_CATEGORIES, {"basket", "bin", "bowl"})
        for label in PHYSICAL_CONTAINER_CATEGORIES:
            self.assertEqual(
                affordances_for_label(label),
                ["reachable", "container", "physical_container"],
            )
            self.assertEqual(grasp_strategy_for_label(label), "unsupported")

    def test_support_receptacles_are_target_physical_containers(self) -> None:
        self.assertEqual(SUPPORT_RECEPTACLE_CATEGORIES, {"plate", "tray"})
        for label in SUPPORT_RECEPTACLE_CATEGORIES:
            self.assertEqual(
                affordances_for_label(label),
                ["reachable", "support", "container", "physical_container"],
            )
            self.assertEqual(role_for_label(label), "target")
            self.assertEqual(grasp_strategy_for_label(label), "unsupported")

    def test_box_assets_are_labeled_as_baskets(self) -> None:
        self.assertEqual(CATEGORY_LABEL_OVERRIDES["box"], "basket")
        self.assertEqual(label_for_category_id("box"), "basket")

    def test_hollow_box_variants_are_physical_container_overrides(self) -> None:
        self.assertGreater(len(VERIFIED_PHYSICAL_CONTAINER_VARIANTS), 1)
        self.assertEqual(
            VARIANT_AFFORDANCE_OVERRIDES[("box", "box00")],
            ["reachable", "container", "physical_container"],
        )
        for variant_key in VERIFIED_PHYSICAL_CONTAINER_VARIANTS:
            self.assertEqual(
                VARIANT_AFFORDANCE_OVERRIDES[variant_key],
                ["reachable", "container", "physical_container"],
            )
            self.assertEqual(VARIANT_GRASP_STRATEGY_OVERRIDES[variant_key], "unsupported")


if __name__ == "__main__":
    unittest.main()
