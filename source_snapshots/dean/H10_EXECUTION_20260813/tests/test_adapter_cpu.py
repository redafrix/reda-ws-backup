from __future__ import annotations

import unittest

import numpy as np

from risk_collection.adapter import sample_nine_candidates
from risk_collection.features import DenoisingTrace
from risk_collection.seeds import candidate_seeds


class FakeBackend:
    def __init__(self) -> None:
        self.encoding_calls = 0

    def encode_once(self, observation):
        self.encoding_calls += 1
        return {"encoded": observation}

    def sample_one(self, encoding, proprio, seed, steps):
        del encoding, proprio
        rng = np.random.default_rng(seed)
        normalized = rng.normal(size=(10, 7)).astype(np.float32)
        environment = normalized * 0.1
        trace = DenoisingTrace(
            path_variance=np.abs(normalized),
            last_step_variance=np.abs(environment),
            denoise_mean_trace=np.linspace(1, 0.1, steps, dtype=np.float32),
            velocity_norm_trace=np.ones(steps, dtype=np.float32),
            update_norm_trace=np.ones(steps, dtype=np.float32) / steps,
            update_vector_trace=np.ones((steps, 70), dtype=np.float32),
            initial_noise=normalized + 1,
            final_action_normalized=normalized,
        )
        return normalized, environment, trace


class AdapterCpuTest(unittest.TestCase):
    def test_nine_candidates_one_encoding(self) -> None:
        backend = FakeBackend()
        seeds = candidate_seeds(1, 2, 3)
        result = sample_nine_candidates(
            backend, observation={"fake": True}, proprio=np.zeros(8), seeds=seeds
        )
        self.assertEqual(backend.encoding_calls, 1)
        self.assertEqual(result.vlm_encoding_count, 1)
        self.assertEqual(result.chunks_normalized.shape, (9, 10, 7))
        self.assertEqual(result.chunks_env.shape, (9, 10, 7))
        self.assertEqual(len(result.traces), 9)
        self.assertEqual(len(set(result.seeds)), 9)

    def test_candidate_zero_is_seed_stable(self) -> None:
        seeds = candidate_seeds(10, 20, 30)
        a = sample_nine_candidates(FakeBackend(), None, None, seeds)
        b = sample_nine_candidates(FakeBackend(), None, None, seeds)
        np.testing.assert_array_equal(
            a.chunks_normalized[0], b.chunks_normalized[0]
        )


if __name__ == "__main__":
    unittest.main()
