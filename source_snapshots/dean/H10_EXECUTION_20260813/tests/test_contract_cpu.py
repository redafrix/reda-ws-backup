from __future__ import annotations

import unittest

import numpy as np

from risk_collection.ace import compute_ace_new_training
from risk_collection.constants import UNCERTAINTY_49D_KEYS
from risk_collection.features import DenoisingTrace, build_uncertainty_49d
from risk_collection.history import DeployableHistory
from risk_collection.seeds import candidate_seeds


def trusted_new_training_reference(candidates: np.ndarray) -> np.ndarray:
    arr = np.asarray(candidates, dtype=np.float32)
    flat = arr.reshape(arr.shape[0], -1)
    centered = flat - flat.mean(axis=0, keepdims=True)
    per_candidate_l2 = np.linalg.norm(centered, axis=1)
    diffs = flat[:, None, :] - flat[None, :, :]
    pairwise = np.linalg.norm(diffs, axis=-1)
    tr = arr[:, :, :3].reshape(arr.shape[0], -1)
    rot = arr[:, :, 3:6].reshape(arr.shape[0], -1)
    grip = arr[:, :, 6:7].reshape(arr.shape[0], -1)
    std_all = arr.std(axis=0)
    out = np.zeros(7, dtype=np.float32)
    out[0] = float(np.log(np.mean(per_candidate_l2) + 1e-6))
    out[1] = float(pairwise[np.triu_indices(arr.shape[0], 1)].mean())
    out[2] = float(std_all.mean())
    out[3] = float(tr.std(axis=0).mean())
    out[4] = float(rot.std(axis=0).mean())
    out[5] = float(grip.std(axis=0).mean())
    out[6] = float(flat.std(axis=0).mean())
    return np.nan_to_num(out).astype(np.float32)


class ContractCpuTest(unittest.TestCase):
    def test_seed_determinism_and_uniqueness(self) -> None:
        first = candidate_seeds(20260730, 123, 45)
        second = candidate_seeds(20260730, 123, 45)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 9)
        self.assertEqual(len(set(first)), 9)
        self.assertNotEqual(first, candidate_seeds(20260730, 123, 46))

    def test_ace_matches_trusted_new_training(self) -> None:
        rng = np.random.default_rng(20260730)
        chunks = rng.normal(size=(8, 10, 7)).astype(np.float32)
        actual = compute_ace_new_training(chunks)
        expected = trusted_new_training_reference(chunks)
        np.testing.assert_allclose(actual, expected, rtol=0.0, atol=0.0)

    def test_history_is_past_only_and_resets(self) -> None:
        history = DeployableHistory()
        np.testing.assert_array_equal(history.snapshot(), np.zeros((16, 21)))
        history.append(
            np.arange(8, dtype=np.float32),
            np.arange(7, dtype=np.float32),
            np.arange(7, dtype=np.float32),
        )
        snapshot = history.snapshot()
        self.assertTrue(np.all(snapshot[:-1] == 0))
        np.testing.assert_array_equal(snapshot[-1, :8], np.arange(8))
        np.testing.assert_array_equal(snapshot[-1, 8:15], np.arange(7))
        np.testing.assert_array_equal(snapshot[-1, 15:], np.arange(6))
        history.reset()
        np.testing.assert_array_equal(history.snapshot(), np.zeros((16, 21)))

    def test_feature_order_and_finiteness(self) -> None:
        rng = np.random.default_rng(9)
        path = np.abs(rng.normal(size=(10, 7))).astype(np.float32)
        last = np.abs(rng.normal(size=(10, 7))).astype(np.float32)
        trace = DenoisingTrace(
            path_variance=path,
            last_step_variance=last,
            denoise_mean_trace=np.linspace(1.0, 0.1, 10, dtype=np.float32),
            velocity_norm_trace=np.linspace(2.0, 1.0, 10, dtype=np.float32),
            update_norm_trace=np.linspace(0.2, 0.1, 10, dtype=np.float32),
            update_vector_trace=rng.normal(size=(10, 70)).astype(np.float32),
            initial_noise=rng.normal(size=(10, 7)).astype(np.float32),
            final_action_normalized=rng.normal(size=(10, 7)).astype(np.float32),
        )
        chunks = rng.normal(size=(9, 10, 7)).astype(np.float32)
        vector, feature_map = build_uncertainty_49d(
            main_trace=trace,
            all_candidate_chunks_env=chunks,
            proprio=np.zeros(8, dtype=np.float32),
            state_mean=np.zeros(8, dtype=np.float32),
            state_std=np.ones(8, dtype=np.float32),
            previous_executed_action=None,
            previous_proprio=None,
        )
        self.assertEqual(vector.shape, (49,))
        self.assertTrue(np.isfinite(vector).all())
        self.assertEqual(tuple(feature_map), UNCERTAINTY_49D_KEYS)
        self.assertEqual(feature_map["action_delta_prev_norm"], 0.0)
        self.assertEqual(feature_map["state_delta_prev_norm"], 0.0)

        denoise = trace.denoise_mean_trace.astype(np.float64)
        velocity = trace.velocity_norm_trace.astype(np.float64)
        update = trace.update_norm_trace.astype(np.float64)
        vectors = trace.update_vector_trace.astype(np.float64)
        sample_var = chunks.var(axis=0)
        sample_mean = chunks.mean(axis=0, keepdims=True)
        sample_l2 = np.linalg.norm(chunks - sample_mean, axis=-1)
        action = chunks[0, 0]
        plan_delta_norms = np.linalg.norm(np.diff(chunks[0], axis=0), axis=-1)
        x = np.arange(denoise.size, dtype=np.float64)
        x -= x.mean()
        y = denoise - denoise.mean()
        a = vectors[1:]
        b = vectors[:-1]
        cos = np.sum(a * b, axis=1) / np.maximum(
            np.linalg.norm(a, axis=1) * np.linalg.norm(b, axis=1), 1e-12
        )
        expected = {
            "path_step_mean": float(path.mean(axis=-1)[0]),
            "last_step_mean": float(last.mean(axis=-1)[0]),
            "mean_path_var": float(path.mean()),
            "mean_last_var": float(last.mean()),
            "max_path_var": float(path.max()),
            "max_last_var": float(last.max()),
            "denoise_initial_mean": float(denoise[0]),
            "denoise_final_mean": float(denoise[-1]),
            "denoise_delta": float(denoise[0] - denoise[-1]),
            "denoise_slope": float(np.dot(x, y) / np.dot(x, x)),
            "denoise_final_max": float(last.max()),
            "denoise_spike": float(np.maximum(np.diff(denoise), 0.0).max()),
            "denoise_final_gripper": float(last[:, -1].mean()),
            "denoise_final_rotation_mean": float(last[:, 3:6].mean()),
            "denoise_velocity_norm_mean": float(velocity.mean()),
            "denoise_velocity_norm_max": float(velocity.max()),
            "denoise_update_norm_mean": float(update.mean()),
            "denoise_update_norm_max": float(update.max()),
            "denoise_update_norm_final": float(update[-1]),
            "denoise_update_spike": float(
                np.maximum(np.diff(update), 0.0).max()
            ),
            "denoise_update_oscillation_mean": float(
                np.linalg.norm(np.diff(vectors, axis=0), axis=1).mean()
            ),
            "denoise_update_direction_flip_mean": float((1.0 - cos).mean()),
            "denoise_final_initial_action_l2": float(
                np.linalg.norm(
                    trace.final_action_normalized.astype(np.float64)
                    - trace.initial_noise.astype(np.float64)
                )
            ),
            "sample_action_var_mean": float(sample_var.mean()),
            "sample_action_var_max": float(sample_var.max()),
            "sample_action_l2_mean": float(sample_l2.mean()),
            "sample_action_l2_max": float(sample_l2.max()),
            "sample_action_translation_var": float(sample_var[..., :3].mean()),
            "sample_action_rotation_var": float(sample_var[..., 3:6].mean()),
            "sample_action_gripper_var": float(sample_var[..., -1].mean()),
            "action_norm": float(np.linalg.norm(action)),
            "action_max_abs": float(np.abs(action).max()),
            "action_translation_norm": float(np.linalg.norm(action[:3])),
            "action_rotation_norm": float(np.linalg.norm(action[3:6])),
            "action_gripper_abs": float(abs(action[-1])),
            "action_delta_prev_norm": 0.0,
            "action_delta_prev_max_abs": 0.0,
            "plan_drift_l2": float(np.linalg.norm(chunks[0, -1] - chunks[0, 0])),
            "plan_drift_mean_l2": float(plan_delta_norms.mean()),
            "plan_drift_max_l2": float(plan_delta_norms.max()),
            "state_mahalanobis": 0.0,
            "state_mahalanobis_eef": 0.0,
            "state_mahalanobis_rotation": 0.0,
            "state_mahalanobis_gripper": 0.0,
            "state_eef_norm": 0.0,
            "state_rotation_norm": 0.0,
            "state_gripper_norm": 0.0,
            "state_gripper_width": 0.0,
            "state_delta_prev_norm": 0.0,
        }
        np.testing.assert_allclose(
            vector,
            np.asarray([expected[key] for key in UNCERTAINTY_49D_KEYS]),
            rtol=1e-6,
            atol=1e-7,
        )


if __name__ == "__main__":
    unittest.main()
