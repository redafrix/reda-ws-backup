"""Image preprocessing that matches the converted IsaacLab SimVLA dataset."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from PIL import Image
import torch

from franka_wrist_camera_scene.simvla.constants import (
    DEFAULT_SIMVLA_CONVENTION,
    IMAGE_ROTATION_180,
    SimVLADataConvention,
    validate_image_rotation,
)

IMAGENET_MEAN = torch.tensor((0.485, 0.456, 0.406), dtype=torch.float32).view(3, 1, 1)
IMAGENET_STD = torch.tensor((0.229, 0.224, 0.225), dtype=torch.float32).view(3, 1, 1)


@dataclass(frozen=True, slots=True)
class SimVLAImageBatch:
    image_input: torch.Tensor
    image_mask: torch.Tensor


def crop_resize_rgb(
    frame: np.ndarray,
    convention: SimVLADataConvention = DEFAULT_SIMVLA_CONVENTION,
) -> np.ndarray:
    expected_shape = (convention.source_height, convention.source_width, 3)
    if frame.shape != expected_shape:
        raise ValueError(f"RGB frame shape must be {expected_shape}, got {frame.shape}.")
    if frame.dtype != np.uint8:
        raise TypeError(f"RGB frame dtype must be uint8, got {frame.dtype}.")

    crop = frame[convention.crop_y0 : convention.crop_y1, convention.crop_x0 : convention.crop_x1]
    try:
        resample = Image.Resampling.BICUBIC
    except AttributeError:
        resample = Image.BICUBIC
    image = Image.fromarray(crop)
    resized = image.resize((convention.image_size, convention.image_size), resample=resample)
    return np.array(resized, dtype=np.uint8, copy=True)


def rotate_rgb_for_mode(frame: np.ndarray, image_rotation: str) -> np.ndarray:
    mode = validate_image_rotation(image_rotation)
    if mode == IMAGE_ROTATION_180:
        return np.ascontiguousarray(frame[::-1, ::-1])
    return np.ascontiguousarray(frame)


def preprocess_rgb_uint8(
    frame: np.ndarray,
    image_rotation: str,
    convention: SimVLADataConvention = DEFAULT_SIMVLA_CONVENTION,
) -> np.ndarray:
    resized = crop_resize_rgb(frame, convention)
    return rotate_rgb_for_mode(resized, image_rotation)


def normalize_rgb_uint8(frame: np.ndarray) -> torch.Tensor:
    if frame.ndim != 3 or frame.shape[-1] != 3:
        raise ValueError(f"Expected RGB image with shape [H, W, 3], got {frame.shape}.")
    if frame.dtype != np.uint8:
        raise TypeError(f"Normalized RGB input must be uint8, got {frame.dtype}.")

    tensor = torch.from_numpy(np.ascontiguousarray(frame)).permute(2, 0, 1).float() / 255.0
    return (tensor - IMAGENET_MEAN) / IMAGENET_STD


def preprocess_camera_views(
    agent_rgb: np.ndarray,
    wrist_rgb: np.ndarray,
    image_rotation: str,
    device: torch.device | str | None = None,
    convention: SimVLADataConvention = DEFAULT_SIMVLA_CONVENTION,
) -> SimVLAImageBatch:
    agent = normalize_rgb_uint8(preprocess_rgb_uint8(agent_rgb, image_rotation, convention))
    wrist = normalize_rgb_uint8(preprocess_rgb_uint8(wrist_rgb, image_rotation, convention))
    zero_pad = torch.zeros_like(agent)

    image_input = torch.stack((agent, wrist, zero_pad), dim=0).unsqueeze(0)
    image_mask = torch.tensor([[True, True, False]], dtype=torch.bool)
    if device is not None:
        image_input = image_input.to(device)
        image_mask = image_mask.to(device)
    return SimVLAImageBatch(image_input=image_input, image_mask=image_mask)
