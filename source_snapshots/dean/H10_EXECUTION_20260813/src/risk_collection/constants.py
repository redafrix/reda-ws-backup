"""Stable dimensions and feature order for the collection contract."""

SCHEMA_VERSION = "simvla_isaac_risk_collection_v1"
ACTION_HORIZON = 10
ACTION_DIM = 7
EXECUTION_MODE = "chunk_h10"
ACTIONS_PER_REPLAN = ACTION_HORIZON
MAX_SIM_STEPS = 2400
CONTROL_DECIMATION = 4
MAX_CONTROL_TICKS = MAX_SIM_STEPS // CONTROL_DECIMATION
MAX_DECISION_ROWS = MAX_CONTROL_TICKS // ACTIONS_PER_REPLAN
PROPRIO_DIM = 8
ACE_CANDIDATES = 8
TOTAL_CANDIDATES = 1 + ACE_CANDIDATES
ACE_DIM = 7
HISTORY_STEPS = 16
HISTORY_DIM = 21
UNCERTAINTY_PARAMETERIZATION = "softplus_raw_variance"
ACE_METRIC_STYLE = "new_training"
TOPK8_INDICES = (6, 21, 25, 27, 23, 2, 26, 24)
ACE_7D_KEYS = (
    "log_mean_centered_candidate_l2",
    "mean_pairwise_candidate_l2",
    "mean_action_std",
    "mean_translation_std",
    "mean_rotation_std",
    "mean_gripper_std",
    "mean_flat_action_std",
)

UNCERTAINTY_49D_KEYS = (
    "path_step_mean",
    "last_step_mean",
    "mean_path_var",
    "mean_last_var",
    "max_path_var",
    "max_last_var",
    "denoise_initial_mean",
    "denoise_final_mean",
    "denoise_delta",
    "denoise_slope",
    "denoise_final_max",
    "denoise_spike",
    "denoise_final_gripper",
    "denoise_final_rotation_mean",
    "denoise_velocity_norm_mean",
    "denoise_velocity_norm_max",
    "denoise_update_norm_mean",
    "denoise_update_norm_max",
    "denoise_update_norm_final",
    "denoise_update_spike",
    "denoise_update_oscillation_mean",
    "denoise_update_direction_flip_mean",
    "denoise_final_initial_action_l2",
    "sample_action_var_mean",
    "sample_action_var_max",
    "sample_action_l2_mean",
    "sample_action_l2_max",
    "sample_action_translation_var",
    "sample_action_rotation_var",
    "sample_action_gripper_var",
    "action_norm",
    "action_max_abs",
    "action_translation_norm",
    "action_rotation_norm",
    "action_gripper_abs",
    "action_delta_prev_norm",
    "action_delta_prev_max_abs",
    "plan_drift_l2",
    "plan_drift_mean_l2",
    "plan_drift_max_l2",
    "state_mahalanobis",
    "state_mahalanobis_eef",
    "state_mahalanobis_rotation",
    "state_mahalanobis_gripper",
    "state_eef_norm",
    "state_rotation_norm",
    "state_gripper_norm",
    "state_gripper_width",
    "state_delta_prev_norm",
)

UNCERTAINTY_DELTA_49D_KEYS = tuple(
    f"{name}_delta" for name in UNCERTAINTY_49D_KEYS
)

assert len(UNCERTAINTY_49D_KEYS) == 49
assert len(ACE_7D_KEYS) == ACE_DIM
assert MAX_CONTROL_TICKS == 600
assert MAX_DECISION_ROWS == 60
