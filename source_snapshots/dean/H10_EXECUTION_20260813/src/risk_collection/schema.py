"""Strict runtime validation for finalized decision rows."""

from __future__ import annotations

from collections.abc import Sequence
import math
from typing import Any

from .constants import (
    ACE_CANDIDATES,
    ACE_DIM,
    ACTION_DIM,
    ACTION_HORIZON,
    HISTORY_DIM,
    HISTORY_STEPS,
    PROPRIO_DIM,
    SCHEMA_VERSION,
)


class RowValidationError(ValueError):
    pass


def _shape(value: Any) -> tuple[int, ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        return ()
    if not value:
        return (0,)
    child_shapes = [_shape(item) for item in value]
    if len(set(child_shapes)) != 1:
        raise RowValidationError("ragged array")
    return (len(value),) + child_shapes[0]


def _require_shape(row: dict[str, Any], key: str, expected: tuple[int, ...]) -> None:
    actual = _shape(row.get(key))
    if actual != expected:
        raise RowValidationError(f"{key}: expected shape {expected}, got {actual}")


def _finite(value: Any) -> bool:
    if isinstance(value, dict):
        return all(_finite(item) for item in value.values())
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return all(_finite(item) for item in value)
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return True
    if isinstance(value, (int, float)):
        return math.isfinite(float(value))
    return False


def validate_row(row: dict[str, Any]) -> None:
    if row.get("schema_version") != SCHEMA_VERSION:
        raise RowValidationError("schema_version mismatch")
    if row.get("execution_mode") != "chunk_h10":
        raise RowValidationError("H10 dataset requires execution_mode=chunk_h10")
    if not isinstance(row.get("episode_id"), str) or not row["episode_id"]:
        raise RowValidationError("episode_id must be a nonempty string")
    if not isinstance(row.get("decision_index"), int) or row["decision_index"] < 0:
        raise RowValidationError("invalid decision_index")

    _require_shape(
        row,
        "main_candidate_action_chunk_normalized",
        (ACTION_HORIZON, ACTION_DIM),
    )
    _require_shape(
        row,
        "main_candidate_action_chunk_env",
        (ACTION_HORIZON, ACTION_DIM),
    )
    _require_shape(
        row,
        "ace_candidate_chunks_normalized",
        (ACE_CANDIDATES, ACTION_HORIZON, ACTION_DIM),
    )
    _require_shape(
        row,
        "ace_candidate_chunks_env",
        (ACE_CANDIDATES, ACTION_HORIZON, ACTION_DIM),
    )
    _require_shape(row, "ace_features_7d", (ACE_DIM,))
    _require_shape(row, "executed_action", (ACTION_DIM,))
    executed_shape = _shape(row.get("executed_action_sequence"))
    if (
        len(executed_shape) != 2
        or not 1 <= executed_shape[0] <= ACTION_HORIZON
        or executed_shape[1] != ACTION_DIM
    ):
        raise RowValidationError(
            f"invalid executed_action_sequence shape: {executed_shape}"
        )
    _require_shape(row, "simvla_uncertainty_49d", (49,))
    _require_shape(row, "simvla_uncertainty_delta_49d", (49,))
    _require_shape(row, "history", (HISTORY_STEPS, HISTORY_DIM))
    current = row.get("current")
    if not isinstance(current, dict) or _shape(current.get("proprio")) != (
        PROPRIO_DIM,
    ):
        raise RowValidationError("current.proprio must have shape (8,)")

    main_seed = row.get("main_seed")
    ace_seeds = row.get("ace_candidate_seeds")
    if not isinstance(main_seed, int) or main_seed < 0:
        raise RowValidationError("invalid main_seed")
    if (
        not isinstance(ace_seeds, list)
        or len(ace_seeds) != ACE_CANDIDATES
        or len(set(ace_seeds)) != ACE_CANDIDATES
        or main_seed in ace_seeds
    ):
        raise RowValidationError("candidate seeds must be nine unique integers")

    outcome = row.get("parent_episode_outcome")
    label = row.get("parent_episode_risk_label")
    if outcome not in {"success", "failure_or_timeout", "error"}:
        raise RowValidationError("invalid parent episode outcome")
    if outcome == "success" and label != 0:
        raise RowValidationError("success must have risk label 0")
    if outcome == "failure_or_timeout" and label != 1:
        raise RowValidationError("failure_or_timeout must have risk label 1")
    if outcome == "error" and label is not None:
        raise RowValidationError("infrastructure error must have null risk label")

    metadata = row.get("metadata")
    required_metadata = {
        "checkpoint_model_sha256",
        "uncertainty_parameterization",
        "manifest_fingerprint_sha256",
        "policy_sampling_seed",
    }
    if not isinstance(metadata, dict) or not required_metadata <= metadata.keys():
        raise RowValidationError("missing required metadata")
    if not isinstance(row.get("simvla_uncertainty_raw"), dict):
        raise RowValidationError("simvla_uncertainty_raw must be an object")
    if not _finite(row):
        raise RowValidationError("row contains nonfinite or unsupported values")
