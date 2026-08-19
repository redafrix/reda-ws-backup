"""Action adapter: converts between Isaac 7D and Mimic 10D representations."""

from __future__ import annotations

import numpy as np
from scipy.spatial.transform import Rotation


def isaac_7d_to_mimic_10d(action_7d: np.ndarray) -> np.ndarray:
    """Convert Isaac 7D [trans(3), rotvec(3), grip(1)] to Mimic 10D [trans(3), rot6(6), grip(1)]."""
    arr = np.asarray(action_7d, dtype=np.float32)
    orig_shape = arr.shape
    if orig_shape[-1] != 7:
        raise ValueError(f"Expected last dimension 7, got {orig_shape[-1]}")

    flat_7d = arr.reshape(-1, 7)
    pos = flat_7d[:, :3]
    rotvec = flat_7d[:, 3:6]
    grip = flat_7d[:, 6:7]

    # Convert axis-angle rotation vector to 3x3 rotation matrix
    rot_mat = Rotation.from_rotvec(rotvec).as_matrix()  # [N, 3, 3]

    # Extract first two rows and flatten to 6D
    rot6 = rot_mat[:, :2, :].reshape(-1, 6).astype(np.float32)  # [N, 6]

    flat_10d = np.concatenate([pos, rot6, grip], axis=-1)
    new_shape = list(orig_shape[:-1]) + [10]
    return flat_10d.reshape(new_shape).astype(np.float32)


def mimic_10d_to_isaac_7d(action_10d: np.ndarray) -> np.ndarray:
    """Convert Mimic 10D [trans(3), rot6(6), grip(1)] to Isaac 7D [trans(3), rotvec(3), grip(1)]."""
    arr = np.asarray(action_10d, dtype=np.float32)
    orig_shape = arr.shape
    if orig_shape[-1] != 10:
        raise ValueError(f"Expected last dimension 10, got {orig_shape[-1]}")

    flat_10d = arr.reshape(-1, 10)
    pos = flat_10d[:, :3]
    rot6 = flat_10d[:, 3:9]
    grip = flat_10d[:, 9:10]

    # Gram-Schmidt orthonormalization on rot6
    rows = rot6.reshape(-1, 2, 3)
    row0 = rows[:, 0, :]
    row1 = rows[:, 1, :]

    norm0 = np.linalg.norm(row0, axis=-1, keepdims=True)
    norm0 = np.where(norm0 < 1e-8, 1.0, norm0)
    first = row0 / norm0

    dot = np.sum(first * row1, axis=-1, keepdims=True)
    second_raw = row1 - first * dot
    norm1 = np.linalg.norm(second_raw, axis=-1, keepdims=True)
    norm1 = np.where(norm1 < 1e-8, 1.0, norm1)
    second = second_raw / norm1

    third = np.cross(first, second)
    rot_mat = np.stack([first, second, third], axis=1)  # [N, 3, 3]

    rotvec = Rotation.from_matrix(rot_mat).as_rotvec().astype(np.float32)
    flat_7d = np.concatenate([pos, rotvec, grip], axis=-1)
    new_shape = list(orig_shape[:-1]) + [7]
    return flat_7d.reshape(new_shape).astype(np.float32)
