"""Shared independent numerical parity audit for seen and OOD risk rows."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from .ace import compute_ace_new_training
from .features import DenoisingTrace, build_uncertainty_49d
from .history import DeployableHistory
from .schema import validate_row
from .seeds import candidate_seeds


def assert_close(
    name: str, actual: np.ndarray, expected: np.ndarray, tolerance: float
) -> float:
    if actual.shape != expected.shape:
        raise RuntimeError(f"{name} shape mismatch: {actual.shape} != {expected.shape}")
    difference = float(np.max(np.abs(actual - expected), initial=0.0))
    if difference > tolerance:
        raise RuntimeError(
            f"{name} mismatch: max_abs={difference:.9g} tolerance={tolerance:.9g}"
        )
    return difference


def trace_from_row(row: dict[str, Any]) -> DenoisingTrace:
    raw = row["simvla_uncertainty_raw"]
    return DenoisingTrace(
        path_variance=np.asarray(raw["path_variance"], dtype=np.float32),
        last_step_variance=np.asarray(raw["last_step_variance"], dtype=np.float32),
        denoise_mean_trace=np.asarray(raw["denoise_mean_trace"], dtype=np.float32),
        velocity_norm_trace=np.asarray(raw["velocity_norm_trace"], dtype=np.float32),
        update_norm_trace=np.asarray(raw["update_norm_trace"], dtype=np.float32),
        update_vector_trace=np.asarray(raw["update_vector_trace"], dtype=np.float32),
        initial_noise=np.asarray(raw["initial_noise"], dtype=np.float32),
        final_action_normalized=np.asarray(
            raw["final_action_normalized"], dtype=np.float32
        ),
    )


def validate_h10_executed_sequence(
    executed: np.ndarray,
    executed_sequence: np.ndarray,
    main_chunk_env: np.ndarray,
) -> float:
    """Prove that the simulator consumed a contiguous prefix of the H10 plan."""
    if (
        executed_sequence.ndim != 2
        or executed_sequence.shape[1] != 7
        or not 1 <= executed_sequence.shape[0] <= 10
    ):
        raise RuntimeError(
            "H10 executed sequence must have shape [1..10,7]; "
            "only a terminal success may end the final chunk early"
        )
    return max(
        assert_close("executed action", executed, main_chunk_env[0], 0.0),
        assert_close(
            "executed action sequence",
            executed_sequence,
            main_chunk_env[: executed_sequence.shape[0]],
            0.0,
        ),
    )


@dataclass
class ParityMetrics:
    max_ace_abs_difference: float = 0.0
    max_feature49_abs_difference: float = 0.0
    max_feature_delta_abs_difference: float = 0.0
    max_history_abs_difference: float = 0.0
    max_executed_action_abs_difference: float = 0.0
    max_candidate0_trace_abs_difference: float = 0.0
    max_candidate_seed_difference: int = 0
    rows_audited: int = 0

    def to_dict(self) -> dict[str, float | int]:
        return asdict(self)


class EpisodeParityAuditor:
    """Recompute all deployable risk inputs independently for one episode."""

    def __init__(
        self,
        *,
        global_seed: int,
        source_episode_id: int,
        state_mean: np.ndarray,
        state_std: np.ndarray,
    ) -> None:
        self.global_seed = int(global_seed)
        self.source_episode_id = int(source_episode_id)
        self.state_mean = np.asarray(state_mean, dtype=np.float32)
        self.state_std = np.asarray(state_std, dtype=np.float32)
        self.history = DeployableHistory()
        self.previous_uncertainty: np.ndarray | None = None
        self.previous_action: np.ndarray | None = None
        self.previous_proprio: np.ndarray | None = None
        self.metrics = ParityMetrics()

    def audit(self, row: dict[str, Any], decision_index: int) -> None:
        validate_row(row)
        main_norm = np.asarray(
            row["main_candidate_action_chunk_normalized"], dtype=np.float32
        )
        main_env = np.asarray(row["main_candidate_action_chunk_env"], dtype=np.float32)
        alternatives_norm = np.asarray(
            row["ace_candidate_chunks_normalized"], dtype=np.float32
        )
        alternatives_env = np.asarray(
            row["ace_candidate_chunks_env"], dtype=np.float32
        )
        executed = np.asarray(row["executed_action"], dtype=np.float32)
        executed_sequence = np.asarray(row["executed_action_sequence"], dtype=np.float32)
        self.metrics.max_executed_action_abs_difference = max(
            self.metrics.max_executed_action_abs_difference,
            validate_h10_executed_sequence(executed, executed_sequence, main_env),
        )

        expected_seeds = candidate_seeds(
            self.global_seed, self.source_episode_id, decision_index
        )
        saved_seeds = (
            int(row["main_seed"]),
            *map(int, row["ace_candidate_seeds"]),
        )
        if saved_seeds != expected_seeds:
            self.metrics.max_candidate_seed_difference = max(
                self.metrics.max_candidate_seed_difference,
                max(
                    abs(left - right)
                    for left, right in zip(saved_seeds, expected_seeds, strict=True)
                ),
            )
            raise RuntimeError("candidate seed mismatch")
        if len(set(saved_seeds)) != 9:
            raise RuntimeError("candidate seeds are not distinct")

        expected_ace = compute_ace_new_training(alternatives_norm)
        self.metrics.max_ace_abs_difference = max(
            self.metrics.max_ace_abs_difference,
            assert_close(
                "ACE",
                np.asarray(row["ace_features_7d"], dtype=np.float32),
                expected_ace,
                1e-6,
            ),
        )

        trace = trace_from_row(row)
        self.metrics.max_candidate0_trace_abs_difference = max(
            self.metrics.max_candidate0_trace_abs_difference,
            assert_close(
                "candidate-zero trace", trace.final_action_normalized, main_norm, 0.0
            ),
        )
        all_env = np.concatenate([main_env[None], alternatives_env], axis=0)
        proprio = np.asarray(row["current"]["proprio"], dtype=np.float32)
        expected_features, _ = build_uncertainty_49d(
            main_trace=trace,
            all_candidate_chunks_env=all_env,
            proprio=proprio,
            state_mean=self.state_mean,
            state_std=self.state_std,
            previous_executed_action=self.previous_action,
            previous_proprio=self.previous_proprio,
        )
        saved_features = np.asarray(row["simvla_uncertainty_49d"], dtype=np.float32)
        self.metrics.max_feature49_abs_difference = max(
            self.metrics.max_feature49_abs_difference,
            assert_close("49D features", saved_features, expected_features, 1e-6),
        )
        expected_delta = (
            np.zeros(49, dtype=np.float32)
            if self.previous_uncertainty is None
            else expected_features - self.previous_uncertainty
        )
        self.metrics.max_feature_delta_abs_difference = max(
            self.metrics.max_feature_delta_abs_difference,
            assert_close(
                "49D delta",
                np.asarray(row["simvla_uncertainty_delta_49d"], dtype=np.float32),
                expected_delta,
                1e-6,
            ),
        )
        self.metrics.max_history_abs_difference = max(
            self.metrics.max_history_abs_difference,
            assert_close(
                "history",
                np.asarray(row["history"], dtype=np.float32),
                self.history.snapshot(),
                1e-6,
            ),
        )
        self.history.append(proprio, executed, expected_ace)
        self.previous_uncertainty = expected_features
        self.previous_action = executed
        self.previous_proprio = proprio
        self.metrics.rows_audited += 1


def merge_metrics(target: ParityMetrics, source: ParityMetrics) -> None:
    target.max_ace_abs_difference = max(
        target.max_ace_abs_difference, source.max_ace_abs_difference
    )
    target.max_feature49_abs_difference = max(
        target.max_feature49_abs_difference, source.max_feature49_abs_difference
    )
    target.max_feature_delta_abs_difference = max(
        target.max_feature_delta_abs_difference,
        source.max_feature_delta_abs_difference,
    )
    target.max_history_abs_difference = max(
        target.max_history_abs_difference, source.max_history_abs_difference
    )
    target.max_executed_action_abs_difference = max(
        target.max_executed_action_abs_difference,
        source.max_executed_action_abs_difference,
    )
    target.max_candidate0_trace_abs_difference = max(
        target.max_candidate0_trace_abs_difference,
        source.max_candidate0_trace_abs_difference,
    )
    target.max_candidate_seed_difference = max(
        target.max_candidate_seed_difference,
        source.max_candidate_seed_difference,
    )
    target.rows_audited += source.rows_audited
