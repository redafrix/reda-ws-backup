#!/usr/bin/env python3
"""Exact Dean Isaac port of the final LIBERO TopK8 argmin-on-alarm controller.

Controller contract:
- sample the same nine SimVLA H10 candidates as the data collector;
- compute the same new-training ACE vector from candidates 1..8 once;
- build candidate-specific 49D uncertainty features for all nine candidates;
- score all nine candidates with the single trained H10/TopK8 SeqRiskModel;
- intervene only when the main score reaches the configured seen-derived alarm threshold;
- select the lowest-risk alternative only when its score is within the configured
  seen-derived selected-score cap; no margin is used.

This mirrors the final LIBERO `argmin_on_alarm` + cap logic. It does not shorten the
H10 execution horizon and it does not alter SimVLA weights.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import sys
from typing import Any

import numpy as np

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
sys.path.insert(0, str(WORKSPACE / "src"))

from risk_collection.ace import compute_ace_new_training, action_statistics  # noqa: E402
from risk_collection.adapter import TorchSimVLABackend, sample_nine_candidates  # noqa: E402
from risk_collection.constants import TOPK8_INDICES  # noqa: E402
from risk_collection.features import build_uncertainty_49d  # noqa: E402
from risk_collection.history import DeployableHistory  # noqa: E402
from risk_collection.seeds import candidate_seeds  # noqa: E402




def load_stats(path: Path) -> dict[str, dict[str, np.ndarray]]:
    payload = json.loads(path.read_text())
    raw = payload.get("stats", payload)
    return {
        name: {key: np.asarray(value, dtype=np.float32) for key, value in values.items()}
        for name, values in raw.items()
    }


def normalize(
    history: np.ndarray, action: np.ndarray, static: np.ndarray,
    stats: dict[str, dict[str, np.ndarray]],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        ((history - stats["history"]["mean"]) / stats["history"]["std"]).astype(np.float32),
        ((action - stats["action"]["mean"]) / stats["action"]["std"]).astype(np.float32),
        ((static - stats["static"]["mean"]) / stats["static"]["std"]).astype(np.float32),
    )


def make_seq_risk_model():
    import torch
    import torch.nn as nn

    class SeqRiskModel(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            width = 128
            self.hist_proj = nn.Linear(21, width)
            self.action_proj = nn.Linear(7, width)
            layer = nn.TransformerEncoderLayer(
                width, 4, 512, dropout=0.1, batch_first=True, activation="gelu"
            )
            self.cls = nn.Parameter(torch.zeros(1, 1, width))
            self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
            self.seq = nn.TransformerEncoder(layer, 3)
            self.static = nn.Sequential(nn.Linear(51, width), nn.GELU())
            self.head = nn.Sequential(
                nn.LayerNorm(width * 2), nn.Linear(width * 2, width), nn.GELU(),
                nn.Dropout(0.1), nn.Linear(width, 1),
            )

        def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
            tokens = torch.cat(
                [self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1
            )
            batch_size = tokens.shape[0]
            tokens = torch.cat([self.cls.expand(batch_size, -1, -1), tokens], dim=1)
            sequence = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
            static = self.static(batch["static"])
            return self.head(torch.cat([sequence, static], dim=-1)).squeeze(-1)

    return SeqRiskModel()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _candidate_feature_49d(
    *,
    candidate_index: int,
    traces: tuple[Any, ...],
    chunks_env: np.ndarray,
    proprio: np.ndarray,
    state_mean: np.ndarray,
    state_std: np.ndarray,
    previous_executed_action: np.ndarray | None,
    previous_proprio: np.ndarray | None,
) -> np.ndarray:
    """Build the trusted 49D vector as if candidate_index were candidate zero.

    `build_uncertainty_49d` intentionally takes candidate zero as the action/plan whose
    risk is described, while its sample-spread statistics use all nine candidates.
    Reordering is therefore the exact way to obtain candidate-specific action/plan
    features without changing the nine-sample distribution.
    """
    order = [candidate_index] + [i for i in range(9) if i != candidate_index]
    reordered = np.asarray(chunks_env, dtype=np.float32)[order]
    feature, _ = build_uncertainty_49d(
        main_trace=traces[candidate_index],
        all_candidate_chunks_env=reordered,
        proprio=proprio,
        state_mean=state_mean,
        state_std=state_std,
        previous_executed_action=previous_executed_action,
        previous_proprio=previous_proprio,
    )
    return feature


def build_candidate_feature_matrix(
    *,
    traces: tuple[Any, ...],
    chunks_env: np.ndarray,
    proprio: np.ndarray,
    state_mean: np.ndarray,
    state_std: np.ndarray,
    previous_executed_action: np.ndarray | None,
    previous_proprio: np.ndarray | None,
) -> np.ndarray:
    result = np.stack(
        [
            _candidate_feature_49d(
                candidate_index=i,
                traces=traces,
                chunks_env=chunks_env,
                proprio=proprio,
                state_mean=state_mean,
                state_std=state_std,
                previous_executed_action=previous_executed_action,
                previous_proprio=previous_proprio,
            )
            for i in range(9)
        ],
        axis=0,
    ).astype(np.float32)
    if result.shape != (9, 49) or not np.isfinite(result).all():
        raise RuntimeError(f"invalid candidate 49D feature matrix: {result.shape}")
    return result


@dataclass(frozen=True)
class SelectionDecision:
    selected_index: int
    reason: str
    main_score: float
    selected_score: float
    best_alternative_index: int
    best_alternative_score: float
    proposed_modification: bool


def select_argmin_on_alarm(
    scores: np.ndarray,
    *,
    main_threshold: float,
    selected_score_cap: float,
    min_delta: float = 0.0,
) -> SelectionDecision:
    """Final LIBERO-style argmin-on-alarm + selected-risk-cap rule."""
    values = np.asarray(scores, dtype=np.float64)
    if values.shape != (9,) or not np.isfinite(values).all():
        raise ValueError(f"scores must be finite shape (9,), got {values.shape}")
    main = float(values[0])
    alt_rel = int(np.argmin(values[1:]))
    best_idx = alt_rel + 1
    best = float(values[best_idx])
    delta = main - best
    if best >= main:
        return SelectionDecision(0, "main_is_lowest", main, main, best_idx, best, False)
    if main < float(main_threshold):
        return SelectionDecision(0, "main_below_alarm_threshold", main, main, best_idx, best, False)
    if best > float(selected_score_cap):
        return SelectionDecision(0, "best_alternative_above_cap", main, main, best_idx, best, False)
    if delta < float(min_delta):
        return SelectionDecision(0, "risk_delta_below_min_delta", main, main, best_idx, best, False)
    return SelectionDecision(best_idx, "argmin_on_alarm_cap_pass", main, best, best_idx, best, True)


class OnlineRiskSelector:
    def __init__(
        self,
        *,
        model_root: Path | None = None,
        model_path: Path | None = None,
        normalization_path: Path,
        main_threshold_name: str | None = None,
        selected_cap_name: str | None = None,
        controller_config_path: Path | None = None,
        device: str = "cuda:0",
    ) -> None:
        import torch

        self.device = torch.device(device)
        self.normalization_path = Path(normalization_path).resolve()

        if controller_config_path is not None:
            self.controller_config_path = Path(controller_config_path).resolve()
            controller_cfg = json.loads(self.controller_config_path.read_text())
            self.main_threshold_name = str(controller_cfg["main_threshold_name"])
            self.main_threshold = float(controller_cfg["main_threshold_value"])
            self.selected_cap_name = str(controller_cfg["alternative_cap_name"])
            self.selected_score_cap = float(controller_cfg["alternative_cap_value"])
            self.min_delta = float(controller_cfg.get("min_delta", 0.0))
            if model_path is not None:
                self.model_path = Path(model_path).resolve()
            elif model_root is not None:
                self.model_path = (Path(model_root) / "model.pt").resolve()
            else:
                self.model_path = WORKSPACE / "models/isaac_h10_topk8_temporal_v1/model.pt"
            self.thresholds_path = self.model_path.parent / "thresholds.json"
        else:
            if model_path is not None:
                self.model_path = Path(model_path).resolve()
                self.model_root = self.model_path.parent
            else:
                self.model_root = Path(model_root).resolve()
                self.model_path = self.model_root / "model.pt"
            self.thresholds_path = self.model_root / "thresholds.json"
            self.model_path = self.model_root / "model.pt"
            self.main_threshold_name = str(main_threshold_name)
            self.selected_cap_name = str(selected_cap_name)
            thresholds = json.loads(self.thresholds_path.read_text())
            if self.main_threshold_name not in thresholds:
                raise KeyError(f"unknown main threshold {self.main_threshold_name!r}")
            if self.selected_cap_name not in thresholds:
                raise KeyError(f"unknown selected cap {self.selected_cap_name!r}")
            self.main_threshold = float(thresholds[self.main_threshold_name])
            self.selected_score_cap = float(thresholds[self.selected_cap_name])
            self.min_delta = 0.0

        self.stats = load_stats(self.normalization_path)
        self.model = make_seq_risk_model().to(self.device)
        state = torch.load(self.model_path, map_location="cpu", weights_only=True)
        self.model.load_state_dict(state)
        self.model.eval()
        self.model_sha256 = sha256_file(self.model_path)
        self.normalization_sha256 = sha256_file(self.normalization_path)
        self.thresholds_sha256 = sha256_file(self.thresholds_path) if self.thresholds_path.exists() else None

    def score(
        self,
        *,
        history: np.ndarray,
        chunks_normalized: np.ndarray,
        ace: np.ndarray,
        proprio: np.ndarray,
        features_49d: np.ndarray,
    ) -> np.ndarray:
        import torch

        history = np.asarray(history, dtype=np.float32)
        chunks = np.asarray(chunks_normalized, dtype=np.float32)
        ace = np.asarray(ace, dtype=np.float32)
        proprio = np.asarray(proprio, dtype=np.float32)
        features = np.asarray(features_49d, dtype=np.float32)
        if history.shape != (16, 21):
            raise ValueError(f"history shape mismatch: {history.shape}")
        if chunks.shape != (9, 10, 7):
            raise ValueError(f"candidate chunk shape mismatch: {chunks.shape}")
        if ace.shape != (7,) or proprio.shape != (8,) or features.shape != (9, 49):
            raise ValueError("static input shape mismatch")
        static = np.stack(
            [
                np.concatenate(
                    [
                        action_statistics(chunks[i]),
                        ace,
                        proprio,
                        features[i, list(TOPK8_INDICES)],
                    ]
                ).astype(np.float32)
                for i in range(9)
            ],
            axis=0,
        )
        h = np.repeat(history[None, :, :], 9, axis=0)
        h, action, static = normalize(h, chunks, static, self.stats)
        with torch.inference_mode():
            logits = self.model(
                {
                    "history": torch.as_tensor(h, dtype=torch.float32, device=self.device),
                    "action": torch.as_tensor(action, dtype=torch.float32, device=self.device),
                    "static": torch.as_tensor(static, dtype=torch.float32, device=self.device),
                }
            )
            scores = torch.sigmoid(logits).detach().cpu().numpy().astype(np.float32)
        if scores.shape != (9,) or not np.isfinite(scores).all():
            raise RuntimeError(f"invalid model scores: {scores}")
        return scores

    def choose(self, scores: np.ndarray) -> SelectionDecision:
        return select_argmin_on_alarm(
            scores,
            main_threshold=self.main_threshold,
            selected_score_cap=self.selected_score_cap,
        )

    def provenance(self) -> dict[str, Any]:
        return {
            "controller": "libero_final_topk8_argmin_on_alarm_selected_cap_port",
            "selection_rule": "argmin_on_alarm",
            "selection_min_margin": 0.0,
            "main_threshold_name": self.main_threshold_name,
            "main_threshold": self.main_threshold,
            "selected_cap_name": self.selected_cap_name,
            "selected_score_cap": self.selected_score_cap,
            "risk_model_path": str(self.model_path),
            "risk_model_sha256": self.model_sha256,
            "normalization_path": str(self.normalization_path),
            "normalization_sha256": self.normalization_sha256,
            "thresholds_path": str(self.thresholds_path),
            "thresholds_sha256": self.thresholds_sha256,
            "topk8_indices": list(TOPK8_INDICES),
            "execution_horizon": 10,
            "candidate_count": 9,
            "ace_alternative_count": 8,
            "ace_metric_style": "new_training",
        }


@dataclass(frozen=True)
class OnlineRiskDecisionPlan:
    decision_index: int
    proprio: np.ndarray
    history: np.ndarray
    main_seed: int
    ace_seeds: tuple[int, ...]
    main_chunk_normalized: np.ndarray
    main_chunk_env: np.ndarray
    ace_chunks_normalized: np.ndarray
    ace_chunks_env: np.ndarray
    ace: np.ndarray
    uncertainty_49d: np.ndarray
    uncertainty_delta_49d: np.ndarray
    uncertainty_raw: dict[str, Any]
    vlm_encoding_count: int
    single_runtime_parity_max_abs: float | None
    all_chunks_normalized: np.ndarray
    all_chunks_env: np.ndarray
    candidate_uncertainty_49d: np.ndarray
    candidate_scores: np.ndarray
    selection: SelectionDecision

    @property
    def selected_chunk_normalized(self) -> np.ndarray:
        return self.all_chunks_normalized[self.selection.selected_index]

    @property
    def selected_chunk_env(self) -> np.ndarray:
        return self.all_chunks_env[self.selection.selected_index]


class OnlineRiskPlanner:
    def __init__(
        self,
        runtime: Any,
        *,
        selector: OnlineRiskSelector,
        image_rotation: str,
        global_seed: int,
        source_episode_id: int,
        state_mean: np.ndarray,
        state_std: np.ndarray,
        verify_single_runtime_parity: bool = False,
        parity_tolerance: float = 1e-5,
    ) -> None:
        self.runtime = runtime
        self.selector = selector
        self.image_rotation = image_rotation
        self.global_seed = int(global_seed)
        self.source_episode_id = int(source_episode_id)
        self.state_mean = np.asarray(state_mean, dtype=np.float32)
        self.state_std = np.asarray(state_std, dtype=np.float32)
        self.verify_single_runtime_parity = bool(verify_single_runtime_parity)
        self.parity_tolerance = float(parity_tolerance)
        self.history = DeployableHistory()
        self.decision_index = 0
        self.previous_uncertainty: np.ndarray | None = None
        self.previous_executed_action: np.ndarray | None = None
        self.previous_proprio: np.ndarray | None = None

    def plan(self, observation: Any) -> OnlineRiskDecisionPlan:
        import torch
        from franka_wrist_camera_scene.simvla.geometry import SimVLAProprioSource
        from franka_wrist_camera_scene.simvla.image_preprocessing import preprocess_camera_views
        from franka_wrist_camera_scene.simvla.reaching_pose_v1 import (
            encode_reaching_pose_proprio,
            validate_language_instruction,
        )

        instruction = validate_language_instruction(observation.language_instruction)
        images = preprocess_camera_views(
            observation.agent_rgb,
            observation.wrist_rgb,
            self.image_rotation,
            device=self.runtime.device,
        )
        proprio = encode_reaching_pose_proprio(
            SimVLAProprioSource(
                ee_pos_w=observation.ee_pos_w,
                ee_quat_wxyz=observation.ee_quat_wxyz,
                robot_base_pos_w=observation.robot_base_pos_w,
                robot_base_quat_wxyz=observation.robot_base_quat_wxyz,
                finger_opening_m=observation.finger_opening_m,
            )
        )
        proprio_tensor = torch.as_tensor(
            proprio, dtype=torch.float32, device=self.runtime.device
        ).view(1, 8)
        encoded = self.runtime.processor.encode_language(instruction)
        backend = TorchSimVLABackend(
            self.runtime,
            input_ids=encoded["input_ids"].to(self.runtime.device),
            image_input=images.image_input.to(device=self.runtime.device, dtype=torch.float32),
            image_mask=images.image_mask.to(device=self.runtime.device, dtype=torch.bool),
        )
        seeds = candidate_seeds(self.global_seed, self.source_episode_id, self.decision_index)
        candidates = sample_nine_candidates(
            backend,
            observation=None,
            proprio=proprio_tensor,
            seeds=seeds,
            steps=self.runtime.config.inference_steps,
        )
        parity_max_abs = None
        if self.verify_single_runtime_parity:
            torch.manual_seed(seeds[0])
            single = self.runtime.infer(
                language_instruction=instruction,
                image_input=images.image_input,
                image_mask=images.image_mask,
                proprio=proprio,
            )
            parity_max_abs = float(
                np.max(np.abs(np.asarray(single.actions, dtype=np.float32) - candidates.chunks_env[0]))
            )
            if parity_max_abs > self.parity_tolerance:
                raise RuntimeError(
                    f"candidate-0 parity failed: max_abs={parity_max_abs:.9g} "
                    f"tolerance={self.parity_tolerance:.9g}"
                )
        ace = compute_ace_new_training(candidates.chunks_normalized[1:])
        features = build_candidate_feature_matrix(
            traces=candidates.traces,
            chunks_env=candidates.chunks_env,
            proprio=proprio,
            state_mean=self.state_mean,
            state_std=self.state_std,
            previous_executed_action=self.previous_executed_action,
            previous_proprio=self.previous_proprio,
        )
        history = self.history.snapshot()
        scores = self.selector.score(
            history=history,
            chunks_normalized=candidates.chunks_normalized,
            ace=ace,
            proprio=proprio,
            features_49d=features,
        )
        selection = self.selector.choose(scores)
        main_uncertainty = features[0].copy()
        delta = (
            np.zeros(49, dtype=np.float32)
            if self.previous_uncertainty is None
            else main_uncertainty - self.previous_uncertainty
        )
        plan = OnlineRiskDecisionPlan(
            decision_index=self.decision_index,
            proprio=np.asarray(proprio, dtype=np.float32).copy(),
            history=history,
            main_seed=seeds[0],
            ace_seeds=seeds[1:],
            main_chunk_normalized=candidates.chunks_normalized[0].copy(),
            main_chunk_env=candidates.chunks_env[0].copy(),
            ace_chunks_normalized=candidates.chunks_normalized[1:].copy(),
            ace_chunks_env=candidates.chunks_env[1:].copy(),
            ace=ace.copy(),
            uncertainty_49d=main_uncertainty,
            uncertainty_delta_49d=delta,
            uncertainty_raw={
                "uncertainty_parameterization": self.runtime.config.uncertainty_parameterization,
                **candidates.traces[0].raw_payload(),
            },
            vlm_encoding_count=candidates.vlm_encoding_count,
            single_runtime_parity_max_abs=parity_max_abs,
            all_chunks_normalized=candidates.chunks_normalized.copy(),
            all_chunks_env=candidates.chunks_env.copy(),
            candidate_uncertainty_49d=features.copy(),
            candidate_scores=scores.copy(),
            selection=selection,
        )
        self.previous_uncertainty = main_uncertainty.copy()
        self.decision_index += 1
        return plan

    def commit_executed(self, plan: OnlineRiskDecisionPlan, executed_action_sequence: np.ndarray) -> None:
        sequence = np.asarray(executed_action_sequence, dtype=np.float32)
        if sequence.ndim != 2 or sequence.shape[1] != 7 or not 1 <= sequence.shape[0] <= 10:
            raise ValueError(f"invalid executed action sequence: {sequence.shape}")
        self.history.append(plan.proprio, sequence[0], plan.ace)
        self.previous_executed_action = sequence[0].copy()
        self.previous_proprio = plan.proprio.copy()
