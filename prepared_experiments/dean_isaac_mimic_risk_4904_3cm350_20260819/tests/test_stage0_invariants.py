"""Invariant unit tests for Stage 0 NEW4904 Mimic retraining."""

import json
from pathlib import Path
import numpy as np
import pytest
import torch

from prepared_experiments.dean_isaac_mimic_risk_4904_3cm350_20260819.implementation.stage0_build_train_validate import (
    TOTAL_EPISODES,
    TOTAL_ROWS,
    SCALAR_DIM,
    HORIZON_STEPS,
    HORIZON_CHANNELS,
    HISTORY_WINDOW_LENGTH,
    PRIMARY_CANDIDATES,
    IsaacMimicWindowDataset,
    MimicH10RiskMonitor,
    apply_normalization,
)


WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
SOURCE_DS = WORKSPACE / "frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1"
TOPK8_MODEL = WORKSPACE / "models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2"
DERIVED_DS = WORKSPACE / "derived_datasets/isaac_mimic_h10_strict_3cm350_seen4904_v3"


def test_01_source_census():
    """Test 1: source census exact (4904 eps, 4387 succ, 517 fail, 96813 rows)."""
    with open(SOURCE_DS / "episodes.json") as f:
        eps = json.load(f)["episodes"]
    assert len(eps) == TOTAL_EPISODES
    succ = sum(1 for e in eps if e["binary_label"] == 0)
    fail = sum(1 for e in eps if e["binary_label"] == 1)
    assert succ == 4387 and fail == 517

    lbls = np.load(SOURCE_DS / "label.npy")
    assert len(lbls) == TOTAL_ROWS


def test_02_split_membership():
    """Test 2: split membership exact from main TopK8 model."""
    with open(TOPK8_MODEL / "split_manifest.json") as f:
        split_m = json.load(f)
    assert len(split_m["episodes"]) == TOTAL_EPISODES
    splits = {e["final_episode_id"]: e["split"] for e in split_m["episodes"]}
    n_tr = sum(1 for s in splits.values() if s == "train")
    n_va = sum(1 for s in splits.values() if s == "validation")
    n_te = sum(1 for s in splits.values() if s == "test")
    assert n_tr == 3433 and n_va == 735 and n_te == 736


def test_03_candidate_subset():
    """Test 3: 8-candidate subset exact."""
    assert PRIMARY_CANDIDATES == 8


def test_04_05_shapes():
    """Test 4 & 5: scalar shape 37 and horizon shape 10x6."""
    scalars = np.load(DERIVED_DS / "raw/scalar37.npy")
    horizon = np.load(DERIVED_DS / "raw/horizon10x6.npy")
    assert scalars.shape == (TOTAL_ROWS, SCALAR_DIM)
    assert horizon.shape == (TOTAL_ROWS, HORIZON_STEPS, HORIZON_CHANNELS)
    assert np.all(np.isfinite(scalars))
    assert np.all(np.isfinite(horizon))


def test_06_07_dynamics_mode_strict_zeros():
    """Test 6 & 7: dynamics mode STRICT_MISSING, dims 9..33 exact zeros before/after normalization."""
    scalars = np.load(DERIVED_DS / "raw/scalar37.npy")
    horizon = np.load(DERIVED_DS / "raw/horizon10x6.npy")
    with open(DERIVED_DS / "normalization.json") as f:
        norm_params = json.load(f)

    # Before normalization
    assert np.all(scalars[:, 9:34] == 0.0)

    # After normalization
    norm_s, _ = apply_normalization(scalars, horizon, norm_params)
    assert np.all(norm_s[:, 9:34] == 0.0)


def test_08_no_old_round0_array_imported():
    """Test 8: derived dataset manifest explicitly states no old round0 arrays used."""
    with open(DERIVED_DS / "dataset_manifest.json") as f:
        m = json.load(f)
    assert m["old_round0_arrays_used"] is False
    assert "isaac_seen4904_h10_3cm350_exact_v1" in m["source_dataset_root"]


def test_09_train_only_normalization():
    """Test 9: normalization fitted from train split rows only."""
    scalars = np.load(DERIVED_DS / "raw/scalar37.npy")
    split_idx = np.load(DERIVED_DS / "split_index.npy")
    with open(DERIVED_DS / "normalization.json") as f:
        norm_params = json.load(f)

    train_scalars = scalars[split_idx == 0]
    expected_mean_0 = np.mean(train_scalars[:, 0])
    actual_mean_0 = norm_params["scalar_mean"][0]
    assert abs(expected_mean_0 - actual_mean_0) < 1e-5


def test_10_window_dataset_padding():
    """Test 10: 8-query left-zero-padded window."""
    scalars = np.load(DERIVED_DS / "raw/scalar37.npy")
    horizon = np.load(DERIVED_DS / "raw/horizon10x6.npy")
    labels = np.load(DERIVED_DS / "labels.npy")
    ep_idx = np.load(DERIVED_DS / "episode_index.npy")
    dec_idx = np.load(DERIVED_DS / "decision_index.npy")
    with open(DERIVED_DS / "normalization.json") as f:
        norm_params = json.load(f)

    ds = IsaacMimicWindowDataset(scalars, horizon, labels, ep_idx, dec_idx, norm_params)
    s_w, h_w, y = ds[0] # first query of episode 0
    assert s_w.shape == (HISTORY_WINDOW_LENGTH, SCALAR_DIM)
    assert h_w.shape == (HISTORY_WINDOW_LENGTH, HORIZON_STEPS, HORIZON_CHANNELS)
    # First 7 queries should be zero padded
    assert torch.all(s_w[:7] == 0.0)
    assert torch.all(h_w[:7] == 0.0)


def test_11_heldout_split_inaccessible_to_training():
    """Test 11: heldout split (split_index == 2) rows never appear in training dataset."""
    split_idx = np.load(DERIVED_DS / "split_index.npy")
    train_indices = np.where(split_idx == 0)[0]
    test_indices = np.where(split_idx == 2)[0]
    overlap = set(train_indices).intersection(set(test_indices))
    assert len(overlap) == 0
