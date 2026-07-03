"""Tensor compatibility helpers for Isaac Lab buffer wrappers."""

from __future__ import annotations

import torch


def as_torch(value) -> torch.Tensor:
    """Return a Torch tensor from Isaac Lab wrapper buffers or plain tensors."""
    if hasattr(value, "torch"):
        return value.torch
    return value
