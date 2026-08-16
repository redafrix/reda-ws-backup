"""Deterministic, audit-friendly policy seed derivation."""

from __future__ import annotations

import hashlib

from .constants import TOTAL_CANDIDATES


def deterministic_candidate_seed(
    global_seed: int,
    source_episode_id: int,
    decision_index: int,
    candidate_index: int,
) -> int:
    if min(global_seed, source_episode_id, decision_index, candidate_index) < 0:
        raise ValueError("seed coordinates must be nonnegative")
    key = (
        f"simvla-isaac-risk-v1|{global_seed}|{source_episode_id}|"
        f"{decision_index}|{candidate_index}"
    ).encode("ascii")
    return int(hashlib.sha256(key).hexdigest()[:16], 16) % (2**31 - 1)


def candidate_seeds(
    global_seed: int,
    source_episode_id: int,
    decision_index: int,
    count: int = TOTAL_CANDIDATES,
) -> tuple[int, ...]:
    if count <= 0:
        raise ValueError("count must be positive")
    values = tuple(
        deterministic_candidate_seed(
            global_seed,
            source_episode_id,
            decision_index,
            candidate_index,
        )
        for candidate_index in range(count)
    )
    if len(set(values)) != len(values):
        raise RuntimeError(f"candidate seed collision: {values}")
    return values
