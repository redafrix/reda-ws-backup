"""Constants for the Isaac Mimic H10 Single-Head offline ablation."""

from __future__ import annotations

# Experiment metadata
EXPERIMENT_NAME = "isaac_mimic_h10_c0dyn_v1"
MACHINE = "dean"
TOTAL_EPISODES = 4000
TOTAL_ROWS = 75603

# Splits
TRAIN_EPISODES = 2800
VAL_EPISODES = 600
TEST_EPISODES = 600

TRAIN_ROWS = 52825
VAL_ROWS = 11410
TEST_ROWS = 11368

# Dimensions and shapes
ISAAC_ACTION_DIM = 7
MIMIC_ACTION_DIM = 10
HORIZON_STEPS = 10
HORIZON_CHANNELS = 6
SCALAR_DIM = 37
QUERY_EMBED_DIM = 64
HISTORY_WINDOW_LENGTH = 8
PRIMARY_CANDIDATES = 8  # main candidate + alternatives 1..7

# Denoising dynamics
DT = -0.1
DENOISING_STEPS = 10
RECONSTRUCTION_PARITY_TOLERANCE = 1e-5

# Model architecture constants
SCALAR_BRANCH_WIDTH = 128
HORIZON_BRANCH_WIDTH = 128
TRANSFORMER_LAYERS = 2
TRANSFORMER_HEADS = 4
TRANSFORMER_FFN_DIM = 512
DROPOUT = 0.1
GRU_HIDDEN_DIM = 128
GRU_NUM_LAYERS = 1

# Training constants
BATCH_SIZE = 64
EPOCHS = 25
LR = 1e-3
WEIGHT_DECAY = 1e-4
GRAD_CLIP_NORM = 1.0
SEEDS = (0, 1, 2, 3, 4)
PRIMARY_SEED = 0

# Calibration constants
CONFORMAL_ALPHAS = (0.05, 0.10, 0.15)
PRIMARY_ALPHA = 0.10
PERCENTILES = (90, 95, 99)

# Feature names
DISAGREEMENT_SCALAR_NAMES = (
    "w2a_action_variance_mean",
    "w2a_action_variance_max",
    "w2a_pairwise_mse_mean",
    "w2a_first_candidate_vs_mean_mse",
    "w2a_endpoint_position_spread_mean_m",
    "w2a_endpoint_position_spread_max_m",
    "w2a_position_variance_mean",
    "w2a_rotation_variance_mean",
    "w2a_gripper_variance_mean",
)

C0_PROXY_TRACE_NAMES = (
    "c0_residual_to_final_mse",
    "c0_state_variance_max",
    "c0_state_variance_mean",
    "c0_velocity_mse_mean",
    "c0_vector_field_l2_mean",
)

SUMMARY_STAT_NAMES = (
    "first",
    "last",
    "mean",
    "max",
    "last_minus_first",
)

TEMPORAL_SCALAR_NAMES = (
    "history_available",
    "abs_delta_action_variance_mean",
    "abs_delta_endpoint_spread_mean",
)

HORIZON_CHANNEL_NAMES = (
    "position_variance_mean",
    "position_variance_max",
    "rotation_variance_mean",
    "gripper_variance",
    "cumulative_position_spread_mean",
    "cumulative_position_spread_max",
)
