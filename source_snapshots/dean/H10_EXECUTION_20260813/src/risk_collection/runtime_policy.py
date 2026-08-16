"""Runtime planning adapter shared by the Isaac collection entry point."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .ace import compute_ace_new_training
from .adapter import TorchSimVLABackend, sample_nine_candidates
from .features import build_uncertainty_49d
from .history import DeployableHistory
from .seeds import candidate_seeds


@dataclass(frozen=True)
class RiskDecisionPlan:
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


class RiskCollectionPlanner:
    def __init__(
        self,
        runtime: Any,
        *,
        image_rotation: str,
        global_seed: int,
        source_episode_id: int,
        state_mean: np.ndarray,
        state_std: np.ndarray,
        verify_single_runtime_parity: bool = False,
        parity_tolerance: float = 1e-5,
    ) -> None:
        self.runtime = runtime
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

    def plan(self, observation: Any) -> RiskDecisionPlan:
        import torch

        from franka_wrist_camera_scene.simvla.geometry import SimVLAProprioSource
        from franka_wrist_camera_scene.simvla.image_preprocessing import (
            preprocess_camera_views,
        )
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
            image_input=images.image_input.to(
                device=self.runtime.device, dtype=torch.float32
            ),
            image_mask=images.image_mask.to(
                device=self.runtime.device, dtype=torch.bool
            ),
        )
        seeds = candidate_seeds(
            self.global_seed,
            self.source_episode_id,
            self.decision_index,
        )
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
                np.max(
                    np.abs(
                        np.asarray(single.actions, dtype=np.float32)
                        - candidates.chunks_env[0]
                    )
                )
            )
            if parity_max_abs > self.parity_tolerance:
                raise RuntimeError(
                    "candidate-0 parity failed: "
                    f"max_abs={parity_max_abs:.9g} "
                    f"tolerance={self.parity_tolerance:.9g}"
                )
        ace = compute_ace_new_training(candidates.chunks_normalized[1:])
        uncertainty, _feature_map = build_uncertainty_49d(
            main_trace=candidates.traces[0],
            all_candidate_chunks_env=candidates.chunks_env,
            proprio=proprio,
            state_mean=self.state_mean,
            state_std=self.state_std,
            previous_executed_action=self.previous_executed_action,
            previous_proprio=self.previous_proprio,
        )
        delta = (
            np.zeros(49, dtype=np.float32)
            if self.previous_uncertainty is None
            else uncertainty - self.previous_uncertainty
        )
        plan = RiskDecisionPlan(
            decision_index=self.decision_index,
            proprio=proprio.copy(),
            history=self.history.snapshot(),
            main_seed=seeds[0],
            ace_seeds=seeds[1:],
            main_chunk_normalized=candidates.chunks_normalized[0].copy(),
            main_chunk_env=candidates.chunks_env[0].copy(),
            ace_chunks_normalized=candidates.chunks_normalized[1:].copy(),
            ace_chunks_env=candidates.chunks_env[1:].copy(),
            ace=ace,
            uncertainty_49d=uncertainty,
            uncertainty_delta_49d=delta,
            uncertainty_raw={
                "uncertainty_parameterization": (
                    self.runtime.config.uncertainty_parameterization
                ),
                **candidates.traces[0].raw_payload(),
            },
            vlm_encoding_count=candidates.vlm_encoding_count,
            single_runtime_parity_max_abs=parity_max_abs,
        )
        self.previous_uncertainty = uncertainty.copy()
        self.decision_index += 1
        return plan

    def commit_executed(
        self,
        plan: RiskDecisionPlan,
        executed_action_sequence: np.ndarray,
    ) -> None:
        sequence = np.asarray(executed_action_sequence, dtype=np.float32)
        if sequence.ndim != 2 or sequence.shape[1] != 7 or not 1 <= sequence.shape[0] <= 10:
            raise ValueError(f"invalid executed action sequence: {sequence.shape}")
        self.history.append(plan.proprio, sequence[0], plan.ace)
        self.previous_executed_action = sequence[0].copy()
        self.previous_proprio = plan.proprio.copy()
