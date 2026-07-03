"""Collection batching policies."""

from __future__ import annotations


def effective_asset_bank_episode_batch_size(
    configured_batch_size: int,
    *,
    episode_count: int,
    record_cameras: bool,
) -> int:
    """Return the asset-bank batch size that is safe for the collection mode."""
    if configured_batch_size <= 0:
        raise ValueError(
            f"asset_bank_episode_batch_size must be positive, got {configured_batch_size}."
        )
    if episode_count < 0:
        raise ValueError(f"episode_count must be non-negative, got {episode_count}.")

    if record_cameras and configured_batch_size < episode_count:
        return episode_count
    return configured_batch_size
