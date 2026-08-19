"""Candidate0 exact denoising reconstruction and 25-scalar dynamics summary."""

from __future__ import annotations

from typing import Tuple
import numpy as np

from .constants import DT, RECONSTRUCTION_PARITY_TOLERANCE


def reconstruct_c0_trajectory(
    initial_noise: np.ndarray,
    update_vector_trace: np.ndarray,
    final_action_normalized: np.ndarray,
    tolerance: float = RECONSTRUCTION_PARITY_TOLERANCE,
) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Reconstruct exact candidate0 state trajectory X_0..X_9, X_10 and velocities V_0..V_9.
    
    Returns:
        X: [11, 10, 7] pre-update states X_0..X_10
        V: [10, 10, 7] velocities V_0..V_9
        max_abs_parity_error: float
    """
    init_n = np.asarray(initial_noise, dtype=np.float32).reshape(10, 7)
    updates = np.asarray(update_vector_trace, dtype=np.float32).reshape(10, 10, 7)
    final_norm = np.asarray(final_action_normalized, dtype=np.float32).reshape(10, 7)

    X = np.zeros((11, 10, 7), dtype=np.float32)
    X[0] = init_n

    running_sum = init_n.copy()
    for d in range(10):
        running_sum = running_sum + updates[d]
        X[d + 1] = running_sum

    # Parity check on X_10
    parity_err = float(np.max(np.abs(X[10] - final_norm)))
    if parity_err > tolerance:
        raise ValueError(
            f"Candidate0 reconstruction parity violation: max_abs={parity_err:.9e} > {tolerance:.9e}"
        )

    # Velocities: V_d = U_d / dt where dt = -0.1
    V = (updates / DT).astype(np.float32)  # [10, 10, 7]

    return X, V, parity_err


def compute_c0_dynamics_25(
    X: np.ndarray,
    V: np.ndarray,
) -> np.ndarray:
    """
    Compute 25 denoising-dynamics scalars from reconstructed X (11, 10, 7) and V (10, 10, 7).
    
    Five traces:
        A. c0_residual_to_final_mse: mean((X_d - X_10)^2) over 10x7
        B. c0_state_variance_max: max_j(Var_h(X_d[:, j]))
        C. c0_state_variance_mean: mean_j(Var_h(X_d[:, j]))
        D. c0_velocity_mse_mean: mean(V_d^2) over 10x7
        E. c0_vector_field_l2_mean: mean_h(||V_d[h, :]||_2)
        
    Each trace summarized as: [first, last, mean, max, last_minus_first].
    Concatenation A..E -> [25] scalars.
    """
    X_10 = X[10]  # [10, 7]

    trace_A = np.zeros(10, dtype=np.float32)
    trace_B = np.zeros(10, dtype=np.float32)
    trace_C = np.zeros(10, dtype=np.float32)
    trace_D = np.zeros(10, dtype=np.float32)
    trace_E = np.zeros(10, dtype=np.float32)

    for d in range(10):
        X_d = X[d]  # [10, 7]
        V_d = V[d]  # [10, 7]

        # A. Residual to final MSE
        trace_A[d] = float(np.mean((X_d - X_10) ** 2))

        # B & C. State variance across 10 horizon steps
        var_h = np.var(X_d, axis=0, ddof=0)  # [7]
        trace_B[d] = float(np.max(var_h))
        trace_C[d] = float(np.mean(var_h))

        # D. Velocity MSE mean
        trace_D[d] = float(np.mean(V_d ** 2))

        # E. Vector field L2 mean over horizon steps
        l2_norms = np.linalg.norm(V_d, axis=-1)  # [10]
        trace_E[d] = float(np.mean(l2_norms))

    traces = [trace_A, trace_B, trace_C, trace_D, trace_E]
    summaries = []

    for tr in traces:
        first = float(tr[0])
        last = float(tr[9])
        mean_val = float(np.mean(tr))
        max_val = float(np.max(tr))
        last_minus_first = float(last - first)
        summaries.extend([first, last, mean_val, max_val, last_minus_first])

    result = np.asarray(summaries, dtype=np.float32)
    if result.shape != (25,):
        raise RuntimeError(f"Expected 25 summary scalars, got shape {result.shape}")
    return result
