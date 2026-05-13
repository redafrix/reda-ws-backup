"""Phase-2 TDQC calibration utilities for SimVLA uncertainty rollouts."""

from .features import (
    ACTION_TRACE_FEATURE_KEYS,
    DEFAULT_TRACE_FEATURE_KEYS,
    DENOISE_TRACE_FEATURE_KEYS,
    STATE_TRACE_FEATURE_KEYS,
    SUMMARY_DENOISE_TRACE_FEATURE_KEYS,
    aggregate_variance_tensors,
    record_to_episode,
    raw_trace_feature_keys,
    trace_step_to_raw_features,
    trace_step_to_features,
)
from .model import TDQCCalibrator, td0_brier_loss
from .dataset import TDQCEpisodeDataset, collate_tdqc_episodes, load_tdqc_dataset

__all__ = [
    "ACTION_TRACE_FEATURE_KEYS",
    "DEFAULT_TRACE_FEATURE_KEYS",
    "DENOISE_TRACE_FEATURE_KEYS",
    "STATE_TRACE_FEATURE_KEYS",
    "SUMMARY_DENOISE_TRACE_FEATURE_KEYS",
    "aggregate_variance_tensors",
    "record_to_episode",
    "raw_trace_feature_keys",
    "trace_step_to_raw_features",
    "trace_step_to_features",
    "TDQCCalibrator",
    "td0_brier_loss",
    "TDQCEpisodeDataset",
    "collate_tdqc_episodes",
    "load_tdqc_dataset",
]
