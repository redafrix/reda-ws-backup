"""OpenPI-compatible image preprocessing for Pi0.5 policy inference."""

from __future__ import annotations

import numpy as np
from PIL import Image


def resize_with_pad_uint8(frame: np.ndarray, height: int = 224, width: int = 224) -> np.ndarray:
    """Match openpi_client.image_tools.resize_with_pad for a single HWC RGB frame."""
    image = _require_uint8_hwc(frame)
    cur_height, cur_width = image.shape[:2]
    if (cur_height, cur_width) == (height, width):
        return np.ascontiguousarray(image)

    ratio = max(cur_width / width, cur_height / height)
    resized_height = int(cur_height / ratio)
    resized_width = int(cur_width / ratio)
    pil = Image.fromarray(image)
    resized = pil.resize((resized_width, resized_height), resample=Image.BILINEAR)

    padded = Image.new(resized.mode, (width, height), 0)
    pad_height = max(0, int((height - resized_height) / 2))
    pad_width = max(0, int((width - resized_width) / 2))
    padded.paste(resized, (pad_width, pad_height))
    arr = np.asarray(padded, dtype=np.uint8)
    if arr.shape != (height, width, 3):
        raise RuntimeError(f"OpenPI image preprocessing produced {arr.shape}, expected {(height, width, 3)}.")
    return np.ascontiguousarray(arr)


def _require_uint8_hwc(frame: np.ndarray) -> np.ndarray:
    arr = np.asarray(frame)
    if arr.ndim != 3 or arr.shape[2] != 3:
        raise ValueError(f"RGB frame must have shape (H, W, 3), got {arr.shape}.")
    if np.issubdtype(arr.dtype, np.floating):
        arr = (255.0 * np.clip(arr, 0.0, 1.0)).astype(np.uint8)
    elif arr.dtype != np.uint8:
        arr = np.clip(arr, 0, 255).astype(np.uint8)
    return arr
