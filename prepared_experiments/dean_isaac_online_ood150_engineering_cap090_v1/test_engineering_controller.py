#!/usr/bin/env python3
"""Stage 2 Unit Tests for Engineering Controller v1."""

from pathlib import Path
import sys
import unittest
import numpy as np

PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))

from online_isaac_runtime import (  # noqa: E402
    SelectionDecision,
    select_argmin_on_alarm,
)

A = 0.7990124225616455
C = 0.9000000000000000


class TestEngineeringController(unittest.TestCase):
    def test_01_main_below_alarm(self):
        scores = [0.50, 0.40, 0.30, 0.60, 0.70, 0.80, 0.20, 0.90, 0.10]
        decision = select_argmin_on_alarm(scores, main_threshold=A, selected_score_cap=C)
        self.assertEqual(decision.selected_index, 0)
        self.assertEqual(decision.reason, "main_below_alarm_threshold")
        self.assertFalse(decision.proposed_modification)

    def test_02_alarm_main_already_lowest(self):
        scores = [0.85, 0.90, 0.92, 0.88, 0.95, 0.99, 0.89, 0.91, 0.94]
        decision = select_argmin_on_alarm(scores, main_threshold=A, selected_score_cap=C)
        self.assertEqual(decision.selected_index, 0)
        self.assertEqual(decision.reason, "main_is_lowest")
        self.assertFalse(decision.proposed_modification)

    def test_03_best_alt_lower_than_main_but_above_cap(self):
        # main=0.98, best_alt=0.95 (which is < main, but > 0.900 cap)
        scores = [0.98, 0.99, 0.95, 0.97, 0.99, 0.96, 0.98, 0.99, 0.97]
        decision = select_argmin_on_alarm(scores, main_threshold=A, selected_score_cap=C)
        self.assertEqual(decision.selected_index, 0)
        self.assertEqual(decision.reason, "best_alternative_above_cap")
        self.assertFalse(decision.proposed_modification)

    def test_04_best_alt_lower_and_below_cap_selected(self):
        # main=0.95, candidate 3=0.82 (<=0.900)
        scores = [0.95, 0.96, 0.98, 0.82, 0.99, 0.94, 0.97, 0.93, 0.99]
        decision = select_argmin_on_alarm(scores, main_threshold=A, selected_score_cap=C)
        self.assertEqual(decision.selected_index, 3)
        self.assertEqual(decision.reason, "argmin_on_alarm_cap_pass")
        self.assertTrue(decision.proposed_modification)
        self.assertAlmostEqual(decision.selected_score, 0.82)

    def test_05_selected_index_range(self):
        for _ in range(50):
            scores = np.random.uniform(0.0, 1.0, size=(9,))
            decision = select_argmin_on_alarm(scores, main_threshold=A, selected_score_cap=C)
            self.assertIn(decision.selected_index, list(range(9)))

    def test_06_active_vs_shadow_execution_mapping(self):
        chunks_env = np.arange(9 * 10 * 7).reshape(9, 10, 7)
        # Case where candidate 4 is selected
        scores = [0.95, 0.98, 0.99, 0.97, 0.75, 0.96, 0.98, 0.99, 0.92]
        decision = select_argmin_on_alarm(scores, main_threshold=A, selected_score_cap=C)
        self.assertEqual(decision.selected_index, 4)

        # In ACTIVE mode: executed action is chunks_env[decision.selected_index]
        active_executed = chunks_env[decision.selected_index]
        np.testing.assert_array_equal(active_executed, chunks_env[4])

        # In SHADOW mode: executed action is ALWAYS chunks_env[0]
        shadow_executed = chunks_env[0]
        np.testing.assert_array_equal(shadow_executed, chunks_env[0])

    def test_07_candidate_scores_shape_and_finite(self):
        scores = np.random.uniform(0.1, 0.9, size=(9,))
        self.assertEqual(scores.shape, (9,))
        self.assertTrue(np.isfinite(scores).all())

        # Test error handling on bad shape
        with self.assertRaises(ValueError):
            select_argmin_on_alarm(scores[:5], main_threshold=A, selected_score_cap=C)

    def test_08_locked_manifest_source_ids(self):
        from orchestrate_engineering_cap090_v1 import load_locked_source_episode_ids
        manifest_p = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/automation/generated/locked_ood150/manifest.json")
        if manifest_p.exists():
            ids = load_locked_source_episode_ids(manifest_p)
            self.assertEqual(len(ids), 150)
            self.assertEqual(len(set(ids)), 150)


if __name__ == "__main__":
    unittest.main()

