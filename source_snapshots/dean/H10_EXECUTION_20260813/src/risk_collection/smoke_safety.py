"""Fail-closed validation for the synthetic forced-timeout smoke."""

from __future__ import annotations

from pathlib import Path


def validate_forced_timeout_smoke_request(
    *,
    enabled: bool,
    output_dir: Path,
    smoke_root: Path,
    count: int | None,
    execution_mode: str,
    inference_only: bool,
    max_steps_override: int | None,
) -> None:
    if not enabled:
        return
    output = output_dir.resolve()
    root = smoke_root.resolve()
    if output == root or not output.is_relative_to(root):
        raise ValueError(
            "forced-timeout smoke output must be a child of "
            f"{root}, got {output}"
        )
    if count != 1:
        raise ValueError("forced-timeout smoke requires exactly --count 1")
    if execution_mode != "chunk_h10":
        raise ValueError("forced-timeout smoke requires chunk_h10")
    if inference_only:
        raise ValueError("forced-timeout smoke cannot be inference-only")
    if max_steps_override not in (None, 2400):
        raise ValueError("forced-timeout smoke requires exactly 2400 max steps")
