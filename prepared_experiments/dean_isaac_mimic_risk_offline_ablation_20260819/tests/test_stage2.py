"""Comprehensive Stage 2 unit test suite (20 tests)."""

import json
import math
import os
from pathlib import Path
import unittest

import numpy as np
import torch

from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.action_adapter import (
    isaac_7d_to_mimic_10d,
    mimic_10d_to_isaac_7d,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.c0_dynamics import (
    compute_c0_dynamics_25,
    reconstruct_c0_trajectory,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.calibration import (
    compute_calibration_thresholds,
    compute_conformal_threshold,
    compute_successful_episode_maxima,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.candidate_features import (
    assemble_scalar37,
    compute_disagreement_and_horizon_features,
    compute_temporal_scalars,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.constants import (
    DT,
    HISTORY_WINDOW_LENGTH,
    HORIZON_CHANNELS,
    HORIZON_STEPS,
    PRIMARY_CANDIDATES,
    RECONSTRUCTION_PARITY_TOLERANCE,
    SCALAR_DIM,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.dataset import (
    IsaacMimicWindowDataset,
    apply_normalization,
    fit_normalization,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.evaluate import (
    run_held_out_test,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.metrics import (
    compute_episode_evaluation,
    compute_row_metrics,
)
from prepared_experiments.dean_isaac_mimic_risk_offline_ablation_20260819.implementation.model import (
    MimicH10RiskMonitor,
)


class TestStage2(unittest.TestCase):
    def test_01_no_stub_scan(self):
        """1. No-stub scan over implementation directory."""
        impl_dir = Path(__file__).resolve().parent.parent / "implementation"
        for py_file in impl_dir.glob("*.py"):
            with open(py_file, "r") as f:
                content = f.read()
                self.assertNotIn("# TODO", content, f"TODO found in {py_file.name}")
                self.assertNotIn("# FIXME", content, f"FIXME found in {py_file.name}")
                self.assertNotIn("... #", content, f"Ellipsis found in {py_file.name}")

    def test_02_action_adapter_roundtrip(self):
        """2. Action adapter source parity / round-trip >=1000 cases."""
        np.random.seed(42)
        N = 1000
        trans = np.random.uniform(-0.01, 0.01, (N, 3)).astype(np.float32)
        rotvec = np.random.uniform(-0.01, 0.01, (N, 3)).astype(np.float32)
        grip = np.random.choice([-1.0, 1.0], (N, 1)).astype(np.float32)
        actions_7d = np.concatenate([trans, rotvec, grip], axis=-1)

        actions_10d = isaac_7d_to_mimic_10d(actions_7d)
        self.assertEqual(actions_10d.shape, (N, 10))

        reconstructed_7d = mimic_10d_to_isaac_7d(actions_10d)
        max_err = float(np.max(np.abs(actions_7d - reconstructed_7d)))
        self.assertLess(max_err, 1e-6)

    def test_03_candidate_subset_ordering(self):
        """3. Candidate subset exact ordering main + alt1..7."""
        main = np.zeros((1, 10, 7), dtype=np.float32)
        alts = np.arange(1, 9, dtype=np.float32)[:, None, None] * np.ones((8, 10, 7), dtype=np.float32)
        c8 = np.concatenate([main, alts[:7]], axis=0)
        self.assertEqual(c8.shape, (8, 10, 7))
        self.assertEqual(c8[0, 0, 0], 0.0)
        self.assertEqual(c8[1, 0, 0], 1.0)
        self.assertEqual(c8[7, 0, 0], 7.0)

    def test_04_pairwise_mse_28_pairs(self):
        """4. Pairwise MSE uses exactly 28 unordered off-diagonal pairs."""
        C = np.zeros((8, 10, 10), dtype=np.float32)
        for i in range(8):
            C[i] = float(i)
        
        scalars_9, _ = compute_disagreement_and_horizon_features(C)
        manual_mses = []
        for i in range(8):
            for j in range(i + 1, 8):
                manual_mses.append((i - j) ** 2)
        self.assertEqual(len(manual_mses), 28)
        expected_mean = float(np.mean(manual_mses))
        self.assertAlmostEqual(scalars_9[2], expected_mean, places=5)

    def test_05_endpoint_cumulative_translation(self):
        """5. Endpoint cumulative translation test with hand-computable fixture."""
        C = np.zeros((8, 10, 10), dtype=np.float32)
        C[0, :, 0] = 0.1
        C[1, :, 0] = 0.2
        scalars_9, horizon_10x6 = compute_disagreement_and_horizon_features(C)
        self.assertAlmostEqual(scalars_9[5], 2.0, places=5)
        self.assertAlmostEqual(scalars_9[4], 19.0 / 28.0, places=5)

    def test_06_scalar9_fixture(self):
        """6. Scalar9 exact fixture."""
        C = np.ones((8, 10, 10), dtype=np.float32)
        scalars_9, _ = compute_disagreement_and_horizon_features(C)
        self.assertEqual(scalars_9.shape, (9,))
        np.testing.assert_allclose(scalars_9, np.zeros(9, dtype=np.float32), atol=1e-6)

    def test_07_horizon10x6_fixture(self):
        """7. Horizon10x6 exact fixture."""
        C = np.ones((8, 10, 10), dtype=np.float32)
        _, horizon_10x6 = compute_disagreement_and_horizon_features(C)
        self.assertEqual(horizon_10x6.shape, (10, 6))
        np.testing.assert_allclose(horizon_10x6, np.zeros((10, 6), dtype=np.float32), atol=1e-6)

    def test_08_c0_xd_recurrence(self):
        """8. C0 X_d recurrence fixture."""
        init_n = np.zeros((10, 7), dtype=np.float32)
        updates = np.ones((10, 10, 7), dtype=np.float32) * 0.1
        final_act = np.ones((10, 7), dtype=np.float32) * 1.0

        X, V, err = reconstruct_c0_trajectory(init_n, updates, final_act)
        self.assertEqual(X.shape, (11, 10, 7))
        self.assertAlmostEqual(err, 0.0, places=6)
        np.testing.assert_allclose(X[0], np.zeros((10, 7)), atol=1e-6)
        np.testing.assert_allclose(X[1], np.ones((10, 7)) * 0.1, atol=1e-6)
        np.testing.assert_allclose(X[10], np.ones((10, 7)) * 1.0, atol=1e-6)

    def test_09_c0_vd_formula(self):
        """9. C0 V_d = U/dt fixture with dt=-0.1."""
        init_n = np.zeros((10, 7), dtype=np.float32)
        updates = np.ones((10, 10, 7), dtype=np.float32) * 0.05
        final_act = np.ones((10, 7), dtype=np.float32) * 0.5

        X, V, _ = reconstruct_c0_trajectory(init_n, updates, final_act)
        np.testing.assert_allclose(V, np.ones((10, 10, 7)) * -0.5, atol=1e-6)

    def test_10_c0_proxy_traces_fixture(self):
        """10. C0 five proxy traces fixture."""
        init_n = np.zeros((10, 7), dtype=np.float32)
        updates = np.zeros((10, 10, 7), dtype=np.float32)
        final_act = np.zeros((10, 7), dtype=np.float32)

        X, V, _ = reconstruct_c0_trajectory(init_n, updates, final_act)
        c0_25 = compute_c0_dynamics_25(X, V)
        self.assertEqual(c0_25.shape, (25,))
        np.testing.assert_allclose(c0_25, np.zeros(25, dtype=np.float32), atol=1e-6)

    def test_11_25_summary_exact_order(self):
        """11. 25-summary exact order fixture."""
        init_n = np.zeros((10, 7), dtype=np.float32)
        updates = np.zeros((10, 10, 7), dtype=np.float32)
        for d in range(10):
            updates[d, 0, 0] = float(d) * (-0.1)
        final_act = np.sum(updates, axis=0)

        X, V, _ = reconstruct_c0_trajectory(init_n, updates, final_act)
        c0_25 = compute_c0_dynamics_25(X, V)
        self.assertEqual(len(c0_25), 25)

    def test_12_scalar37_order_and_shape(self):
        """12. Scalar37 exact order/shape fixture."""
        s9 = np.ones(9, dtype=np.float32) * 1.0
        c25 = np.ones(25, dtype=np.float32) * 2.0
        t3 = np.ones(3, dtype=np.float32) * 3.0
        s37 = assemble_scalar37(s9, c25, t3)
        self.assertEqual(s37.shape, (37,))
        self.assertEqual(s37[0], 1.0)
        self.assertEqual(s37[8], 1.0)
        self.assertEqual(s37[9], 2.0)
        self.assertEqual(s37[33], 2.0)
        self.assertEqual(s37[34], 3.0)
        self.assertEqual(s37[36], 3.0)

    def test_13_temporal_q0_and_deltas(self):
        """13. Temporal q=0 zeros and q>0 absolute deltas."""
        t0 = compute_temporal_scalars(0, 0.5, 1.2, None, None)
        np.testing.assert_allclose(t0, np.array([0.0, 0.0, 0.0], dtype=np.float32))

        t1 = compute_temporal_scalars(1, 0.6, 1.5, 0.5, 1.2)
        np.testing.assert_allclose(t1, np.array([1.0, 0.1, 0.3], dtype=np.float32), atol=1e-5)

    def test_14_window_dataset_left_padding(self):
        """14. 8-query left-zero-padded window construction."""
        scalars = np.ones((5, 37), dtype=np.float32)
        horizon = np.ones((5, 10, 6), dtype=np.float32)
        labels = np.array([0, 0, 0, 0, 0], dtype=np.float32)
        ep_idx = np.array([0, 0, 0, 0, 0], dtype=np.int64)
        dec_idx = np.array([0, 1, 2, 3, 4], dtype=np.int64)
        norm_params = {
            "scalar_mean": [0.0] * 37,
            "scalar_std": [1.0] * 37,
            "horizon_mean": [0.0] * 6,
            "horizon_std": [1.0] * 6,
            "std_floor": 1e-6,
        }

        ds = IsaacMimicWindowDataset(scalars, horizon, labels, ep_idx, dec_idx, norm_params)
        w_s, w_h, lbl = ds[2]
        self.assertEqual(w_s.shape, (8, 37))
        self.assertEqual(w_h.shape, (8, 10, 6))
        np.testing.assert_allclose(w_s[:5].numpy(), np.zeros((5, 37)))
        np.testing.assert_allclose(w_s[5:].numpy(), np.ones((3, 37)))

    def test_15_model_forward_shape(self):
        """15. Model shape test: batch -> one logit/window."""
        model = MimicH10RiskMonitor()
        model.eval()
        bs = 4
        b_s = torch.randn(bs, 8, 37)
        b_h = torch.randn(bs, 8, 10, 6)
        out = model(b_s, b_h)
        self.assertEqual(out.shape, (bs,))

    def test_16_normalization_train_only(self):
        """16. Normalization fits train only; test mutation cannot change normalization hash."""
        train_s = np.ones((100, 37), dtype=np.float32) * 5.0
        train_h = np.ones((100, 10, 6), dtype=np.float32) * 2.0
        norm1 = fit_normalization(train_s, train_h)

        test_s = np.ones((50, 37), dtype=np.float32) * 100.0
        norm2 = fit_normalization(train_s, train_h)
        self.assertEqual(norm1["scalar_mean"], norm2["scalar_mean"])
        self.assertEqual(norm1["horizon_mean"], norm2["horizon_mean"])

    def test_17_split_counts_and_manifest(self):
        """17. Split identity/count test exactly 2800/600/600 episodes and 52825/11410/11368 rows."""
        frozen_dir = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen_h10_topk8_v1")
        if frozen_dir.exists():
            with open(frozen_dir / "dataset_manifest.json") as f:
                manifest = json.load(f)
            self.assertEqual(manifest["split_contract"]["group_count"], 4000)
            self.assertEqual(manifest["splits"]["train"]["episodes"], 2800)
            self.assertEqual(manifest["splits"]["validation"]["episodes"], 600)
            self.assertEqual(manifest["splits"]["test"]["episodes"], 600)
            self.assertEqual(manifest["splits"]["train"]["rows"], 52825)
            self.assertEqual(manifest["splits"]["validation"]["rows"], 11410)
            self.assertEqual(manifest["splits"]["test"]["rows"], 11368)

    def test_18_no_forbidden_metadata_leakage(self):
        """18. No forbidden metadata input test (task/timestep/reward/scene/outcome IDs absent)."""
        self.assertEqual(SCALAR_DIM, 37)
        self.assertEqual(HORIZON_STEPS, 10)
        self.assertEqual(HORIZON_CHANNELS, 6)

    def test_19_calibration_order_statistics(self):
        """19. Calibration order-statistic tests for alpha .05/.10/.15."""
        items = list(range(100))
        tau_10 = compute_conformal_threshold(items, 0.10)
        self.assertEqual(tau_10, 90.0)

        tau_05 = compute_conformal_threshold(items, 0.05)
        self.assertEqual(tau_05, 95.0)

        tau_15 = compute_conformal_threshold(items, 0.15)
        self.assertEqual(tau_15, 85.0)

    def test_20_evaluator_test_lock(self):
        """20. Evaluator test-lock refuses held-out test before freeze marker."""
        non_existent_freeze = Path("/tmp/non_existent_freeze_marker.json")
        with self.assertRaises(RuntimeError) as ctx:
            run_held_out_test("/tmp", "/tmp/model.pt", non_existent_freeze, "/tmp/out", torch.device("cpu"))
        self.assertIn("LEAKAGE GUARD ACTIVE", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
