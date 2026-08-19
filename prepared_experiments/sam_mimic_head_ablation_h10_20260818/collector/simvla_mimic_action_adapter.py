"""Deterministic bidirectional action adapter between SimVLA 7D and Mimic 10D."""

from __future__ import annotations

import numpy as np
from scipy.spatial.transform import Rotation as R


def rotmat_to_rot6d(rot_mat: np.ndarray) -> np.ndarray:
    """Convert rotation matrices (..., 3, 3) to 6D rotation (..., 6).

    Friend Mimic convention: first two rows of rotation matrix flattened row-major.
    """
    mat = np.asarray(rot_mat, dtype=np.float64)
    if mat.shape[-2:] != (3, 3):
        raise ValueError(f"Expected trailing shape (3, 3), got {mat.shape}")
    orig_shape = mat.shape[:-2]
    flat_mat = mat.reshape(-1, 3, 3)
    r6 = flat_mat[:, :2, :].reshape(-1, 6)
    return r6.reshape(orig_shape + (6,)).astype(np.float32)


def rot6d_to_rotmat(rot6: np.ndarray) -> np.ndarray:
    """Convert 6D rotation vectors (..., 6) to 3x3 rotation matrices (..., 3, 3).

    Gram-Schmidt orthonormalization on row 0 and row 1, followed by cross product.
    """
    r6 = np.asarray(rot6, dtype=np.float64)
    if r6.shape[-1] != 6:
        raise ValueError(f"Expected trailing dimension 6, got {r6.shape}")

    orig_shape = r6.shape[:-1]
    flat = r6.reshape(-1, 6)

    r0 = flat[:, :3]
    r1 = flat[:, 3:6]

    norm0 = np.linalg.norm(r0, axis=-1, keepdims=True)
    norm0 = np.where(norm0 < 1e-8, 1.0, norm0)
    e0 = r0 / norm0

    dot = np.sum(e0 * r1, axis=-1, keepdims=True)
    r1_orth = r1 - dot * e0
    norm1 = np.linalg.norm(r1_orth, axis=-1, keepdims=True)
    norm1 = np.where(norm1 < 1e-8, 1.0, norm1)
    e1 = r1_orth / norm1

    e2 = np.cross(e0, e1)
    mat = np.stack([e0, e1, e2], axis=1)
    return mat.reshape(orig_shape + (3, 3)).astype(np.float64)


def action_7d_to_10d(action_7d: np.ndarray) -> np.ndarray:
    """Convert SimVLA 7D action (..., 7) to Mimic 10D action (..., 10).

    SimVLA 7D: [dx, dy, dz, rotvec_x, rotvec_y, rotvec_z, gripper]
    Mimic 10D: [dx, dy, dz, r00, r01, r02, r10, r11, r12, gripper]
    """
    a7 = np.asarray(action_7d, dtype=np.float32)
    if a7.shape[-1] != 7:
        raise ValueError(f"Expected trailing dimension 7, got {a7.shape}")

    orig_shape = a7.shape[:-1]
    flat = a7.reshape(-1, 7)

    trans = flat[:, :3]
    rotvec = flat[:, 3:6]
    gripper = flat[:, 6:7]

    rot_mat = R.from_rotvec(rotvec.astype(np.float64)).as_matrix()
    rot6 = rotmat_to_rot6d(rot_mat).reshape(-1, 6)

    a10 = np.concatenate([trans, rot6, gripper], axis=-1)
    return a10.reshape(orig_shape + (10,)).astype(np.float32)


def action_10d_to_7d(action_10d: np.ndarray) -> np.ndarray:
    """Convert Mimic 10D action (..., 10) to SimVLA 7D action (..., 7).

    Mimic 10D: [dx, dy, dz, r00, r01, r02, r10, r11, r12, gripper]
    SimVLA 7D: [dx, dy, dz, rotvec_x, rotvec_y, rotvec_z, gripper]
    """
    a10 = np.asarray(action_10d, dtype=np.float32)
    if a10.shape[-1] != 10:
        raise ValueError(f"Expected trailing dimension 10, got {a10.shape}")

    orig_shape = a10.shape[:-1]
    flat = a10.reshape(-1, 10)

    trans = flat[:, :3]
    rot6 = flat[:, 3:9]
    gripper = flat[:, 9:10]

    rot_mat = rot6d_to_rotmat(rot6)
    rotvec = R.from_matrix(rot_mat).as_rotvec().astype(np.float32)

    a7 = np.concatenate([trans, rotvec, gripper], axis=-1)
    return a7.reshape(orig_shape + (7,)).astype(np.float32)
