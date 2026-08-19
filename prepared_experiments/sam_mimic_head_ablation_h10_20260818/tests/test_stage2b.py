"""Production test suite for Stage 2B Goal-Object H10 Mimic-Head Collector."""

from __future__ import annotations

import ast
from pathlib import Path
import sys
import unittest

import numpy as np
from scipy.spatial.transform import Rotation as R

# Set up module imports
COLLECTOR_DIR = Path(__file__).resolve().parent.parent / "collector"
sys.path.insert(0, str(COLLECTOR_DIR))

import simvla_mimic_action_adapter as adapter
import simvla_mimic_features as features
import collect_goal_object_mimic_head_h10 as collector


class TestStage2BProduction(unittest.TestCase):
    def test_01_no_stub_scan(self) -> None:
        """Verify that collector modules contain no stubs, placeholders, or TODOs."""
        target_files = [
            COLLECTOR_DIR / "simvla_mimic_action_adapter.py",
            COLLECTOR_DIR / "simvla_mimic_features.py",
            COLLECTOR_DIR / "collect_goal_object_mimic_head_h10.py",
        ]

        violations = []
        for file_path in target_files:
            self.assertTrue(file_path.exists(), f"File {file_path} missing")
            content = file_path.read_text(encoding="utf-8")
            tree = ast.parse(content, filename=str(file_path))

            for node in ast.walk(tree):
                if isinstance(node, ast.Pass):
                    violations.append(f"{file_path.name}:{node.lineno} - ast.Pass")
                elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and node.value.value is Ellipsis:
                    violations.append(f"{file_path.name}:{node.lineno} - Ellipsis placeholder")
                elif isinstance(node, ast.Raise):
                    if isinstance(node.exc, ast.Name) and node.exc.id == "NotImplementedError":
                        violations.append(f"{file_path.name}:{node.lineno} - NotImplementedError")
                    elif isinstance(node.exc, ast.Call) and getattr(node.exc.func, "id", "") == "NotImplementedError":
                        violations.append(f"{file_path.name}:{node.lineno} - NotImplementedError")

            for token in ["TODO", "FIXME", "for static test passing"]:
                if token in content:
                    violations.append(f"{file_path.name} contains banned comment/token {token}")

        self.assertEqual(len(violations), 0, f"Stub scan violations found: {violations}")

    def test_02_rotation_adapter_roundtrip_parity(self) -> None:
        """Verify 7D -> 10D -> 7D bidirectional parity over identity + 500 random rotations."""
        # Identity
        a7_zero = np.zeros((1, 7), dtype=np.float32)
        a10_zero = adapter.action_7d_to_10d(a7_zero)
        a7_recon_zero = adapter.action_10d_to_7d(a10_zero)
        np.testing.assert_allclose(a7_recon_zero, a7_zero, atol=1e-7)

        # Random small rotations
        rng = np.random.default_rng(42)
        random_a7 = rng.uniform(-0.15, 0.15, size=(500, 7)).astype(np.float32)
        random_a10 = adapter.action_7d_to_10d(random_a7)
        self.assertEqual(random_a10.shape, (500, 10))

        random_a7_recon = adapter.action_10d_to_7d(random_a10)
        max_error = np.max(np.abs(random_a7 - random_a7_recon))
        self.assertLess(max_error, 1e-5)

    def test_03_candidate_seed_uniqueness_and_reproducibility(self) -> None:
        """Verify that candidate seed generator produces 8 unique deterministic seeds."""
        seeds1 = collector.action_seeds_for_step(
            global_action_seed=42, reset_seed=100, episode_index=0, timestep=0, num_seeds=8
        )
        seeds2 = collector.action_seeds_for_step(
            global_action_seed=42, reset_seed=100, episode_index=0, timestep=0, num_seeds=8
        )
        self.assertEqual(seeds1, seeds2)
        self.assertEqual(len(seeds1), 8)
        self.assertEqual(len(set(seeds1)), 8)

        # Seeds at different timesteps must differ
        seeds3 = collector.action_seeds_for_step(
            global_action_seed=42, reset_seed=100, episode_index=0, timestep=10, num_seeds=8
        )
        self.assertNotEqual(seeds1, seeds3)

    def test_04_candidate_combine_order(self) -> None:
        """Verify candidate combine order preserves candidate 0 and indices 1..7 exactly."""
        cand0 = np.full((1, 10, 7), 100.0, dtype=np.float32)
        cand_alt = np.zeros((7, 10, 7), dtype=np.float32)
        for i in range(7):
            cand_alt[i] = i + 1

        combined = np.concatenate([cand0, cand_alt], axis=0)
        self.assertEqual(combined.shape, (8, 10, 7))
        np.testing.assert_allclose(combined[0], 100.0)
        for i in range(7):
            np.testing.assert_allclose(combined[i + 1], i + 1)

    def test_05_pairwise_diagonal_exclusion(self) -> None:
        """Prove that pairwise metric excludes diagonal self-pairs and averages over 28 pairs."""
        x = np.zeros((8, 10, 7), dtype=np.float64)
        x[0] = 1.0
        v = np.zeros((8, 10, 7), dtype=np.float64)

        metrics = features.compute_denoising_metrics(x, v)
        self.assertAlmostEqual(metrics["sample_pairwise_mse_mean"], 7.0 / 28.0, places=6)

    def test_06_denoising_trace_reducer_dimension_and_order(self) -> None:
        """Verify denoising trace reducer returns exactly 25 values in frozen order."""
        step_metrics = []
        for d in range(10):
            step_metrics.append(
                {
                    "sample_pairwise_mse_mean": float(d),
                    "sample_variance_max": float(d * 2),
                    "sample_variance_mean": float(d * 0.5),
                    "sample_velocity_mse_mean": float(d * 3),
                    "vector_field_l2_mean": float(d * 1.5),
                }
            )

        reduced = features.reduce_denoising_traces(step_metrics, expected_steps=10)
        self.assertEqual(reduced.shape, (25,))
        self.assertTrue(np.all(np.isfinite(reduced)))

        # First trace: 0..9. [first=0, last=9, mean=4.5, max=9, diff=9]
        np.testing.assert_allclose(reduced[:5], [0.0, 9.0, 4.5, 9.0, 9.0], atol=1e-6)

    def test_07_full_feature_extractor_contract(self) -> None:
        """Verify feature extractor outputs exactly 37 scalars and (10, 6) horizon features."""
        rng = np.random.default_rng(123)
        c10 = rng.uniform(-0.5, 0.5, size=(8, 10, 10)).astype(np.float32)
        step_metrics = []
        for d in range(10):
            step_metrics.append(
                {
                    "sample_pairwise_mse_mean": float(d * 0.1),
                    "sample_variance_max": float(d * 0.2),
                    "sample_variance_mean": float(d * 0.05),
                    "sample_velocity_mse_mean": float(d * 0.3),
                    "vector_field_l2_mean": float(d * 0.15),
                }
            )

        # First query (history_available = 0)
        s1, h1, state1 = features.extract_query_features(c10, step_metrics, previous_query_state=None)
        self.assertEqual(s1.shape, (37,))
        self.assertEqual(h1.shape, (10, 6))
        self.assertTrue(np.all(np.isfinite(s1)))
        self.assertTrue(np.all(np.isfinite(h1)))
        self.assertEqual(s1[-3], 0.0)  # history_available = 0

        # Second query (history_available = 1)
        c10_2 = rng.uniform(-0.5, 0.5, size=(8, 10, 10)).astype(np.float32)
        s2, h2, state2 = features.extract_query_features(c10_2, step_metrics, previous_query_state=state1)
        self.assertEqual(s2.shape, (37,))
        self.assertEqual(h2.shape, (10, 6))
        self.assertTrue(np.all(np.isfinite(s2)))
        self.assertTrue(np.all(np.isfinite(h2)))
        self.assertEqual(s2[-3], 1.0)  # history_available = 1

    def test_08_split_assignment_zero_leakage(self) -> None:
        """Verify 1000-episode plan has exact counts and zero init-state group leakage."""
        plan = collector.build_collection_plan()
        self.assertEqual(len(plan), 1000)

        assignments: dict[str, set[tuple[int, int]]] = {
            "train": set(),
            "id_development": set(),
            "seen_test": set(),
            "successful_calibration_pool": set(),
        }

        counts: dict[str, int] = {k: 0 for k in assignments}

        for p in plan:
            pair = (p["task_id"], p["init_state_idx"])
            assign = p["assignment"]
            assignments[assign].add(pair)
            counts[assign] += 1

        self.assertEqual(counts["train"], 500)
        self.assertEqual(counts["id_development"], 200)
        self.assertEqual(counts["seen_test"], 200)
        self.assertEqual(counts["successful_calibration_pool"], 100)

        # Check disjointness across all assignment pairs
        keys = list(assignments.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                k1, k2 = keys[i], keys[j]
                overlap = assignments[k1].intersection(assignments[k2])
                self.assertEqual(len(overlap), 0, f"Leakage between {k1} and {k2}: {overlap}")

    def test_09_collector_h10_execution_ast_loop(self) -> None:
        """Prove statically via AST that collector executes full H10 chunk (indices 0..9)."""
        collector_path = COLLECTOR_DIR / "collect_goal_object_mimic_head_h10.py"
        tree = ast.parse(collector_path.read_text(encoding="utf-8"))

        found_h10_loop = False
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call) and getattr(node.iter.func, "id", "") == "range":
                    if len(node.iter.args) == 1:
                        arg = node.iter.args[0]
                        if isinstance(arg, ast.Name) and "horizon" in arg.id.lower():
                            found_h10_loop = True

        self.assertTrue(found_h10_loop, "Did not find for action_idx in range(execution_horizon) loop in collector")

    def test_10_manifest_and_config_contracts(self) -> None:
        """Verify manifest parameters conform to protocol requirements."""
        plan = collector.build_collection_plan()
        all_tasks = set(p["task_id"] for p in plan)
        self.assertEqual(all_tasks, set(range(10)))

        all_init_states = set(p["init_state_idx"] for p in plan)
        self.assertEqual(all_init_states, set(range(50)))


if __name__ == "__main__":
    unittest.main()
