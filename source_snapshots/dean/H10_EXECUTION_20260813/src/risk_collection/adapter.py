"""One-encoding, nine-candidate seeded SimVLA sampling adapter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

import numpy as np

from .constants import (
    ACTION_DIM,
    ACTION_HORIZON,
    TOTAL_CANDIDATES,
    UNCERTAINTY_PARAMETERIZATION,
)
from .features import DenoisingTrace


class CandidateBackend(Protocol):
    encoding_calls: int

    def encode_once(self, observation: Any) -> Any: ...

    def sample_one(
        self,
        encoding: Any,
        proprio: Any,
        seed: int,
        steps: int,
    ) -> tuple[np.ndarray, np.ndarray, DenoisingTrace]: ...


@dataclass(frozen=True)
class NineCandidateBatch:
    chunks_normalized: np.ndarray
    chunks_env: np.ndarray
    traces: tuple[DenoisingTrace, ...]
    seeds: tuple[int, ...]
    vlm_encoding_count: int

    def validate(self) -> None:
        expected = (TOTAL_CANDIDATES, ACTION_HORIZON, ACTION_DIM)
        if self.chunks_normalized.shape != expected:
            raise ValueError(
                f"normalized candidate shape {self.chunks_normalized.shape} != {expected}"
            )
        if self.chunks_env.shape != expected:
            raise ValueError(
                f"environment candidate shape {self.chunks_env.shape} != {expected}"
            )
        if len(self.traces) != TOTAL_CANDIDATES:
            raise ValueError("expected nine denoising traces")
        if len(self.seeds) != TOTAL_CANDIDATES or len(set(self.seeds)) != len(
            self.seeds
        ):
            raise ValueError("expected nine unique seeds")
        if self.vlm_encoding_count != 1:
            raise ValueError("each decision must encode the VLM exactly once")
        if not np.isfinite(self.chunks_normalized).all() or not np.isfinite(
            self.chunks_env
        ).all():
            raise ValueError("candidate actions contain nonfinite values")


def sample_nine_candidates(
    backend: CandidateBackend,
    observation: Any,
    proprio: Any,
    seeds: tuple[int, ...],
    steps: int = 10,
) -> NineCandidateBatch:
    if len(seeds) != TOTAL_CANDIDATES or len(set(seeds)) != TOTAL_CANDIDATES:
        raise ValueError("exactly nine unique candidate seeds are required")
    calls_before = int(backend.encoding_calls)
    encoding = backend.encode_once(observation)
    calls_after = int(backend.encoding_calls)
    if calls_after - calls_before != 1:
        raise RuntimeError("backend did not perform exactly one VLM encoding")

    normalized: list[np.ndarray] = []
    environment: list[np.ndarray] = []
    traces: list[DenoisingTrace] = []
    for seed in seeds:
        norm, env, trace = backend.sample_one(encoding, proprio, seed, steps)
        normalized.append(np.asarray(norm, dtype=np.float32))
        environment.append(np.asarray(env, dtype=np.float32))
        traces.append(trace)

    result = NineCandidateBatch(
        chunks_normalized=np.stack(normalized),
        chunks_env=np.stack(environment),
        traces=tuple(traces),
        seeds=tuple(int(seed) for seed in seeds),
        vlm_encoding_count=1,
    )
    result.validate()
    return result


class TorchSimVLABackend:
    """Runtime backend; imports Torch and model helpers only when instantiated."""

    def __init__(
        self,
        runtime: Any,
        *,
        input_ids: Any,
        image_input: Any,
        image_mask: Any,
    ) -> None:
        import torch

        if runtime.model is None:
            raise RuntimeError("SimVLA runtime model is not loaded")
        self.torch = torch
        self.runtime = runtime
        self.model = runtime.model
        self.input_ids = input_ids
        self.image_input = image_input
        self.image_mask = image_mask
        self.encoding_calls = 0

        if (
            getattr(self.model.config, "uncertainty_parameterization", None)
            != UNCERTAINTY_PARAMETERIZATION
        ):
            raise ValueError("runtime is not the verified softplus parameterization")

        from models.modeling_smolvlm_vla import uncertainty_output_to_variance

        self.uncertainty_output_to_variance = uncertainty_output_to_variance

    def encode_once(self, observation: Any) -> dict[str, Any]:
        del observation
        self.encoding_calls += 1
        with self.torch.inference_mode():
            return self.model.forward_vlm_efficient(
                self.image_input,
                self.image_mask,
                self.input_ids,
            )

    def sample_one(
        self,
        encoding: dict[str, Any],
        proprio: Any,
        seed: int,
        steps: int,
    ) -> tuple[np.ndarray, np.ndarray, DenoisingTrace]:
        torch = self.torch
        model = self.model
        device = proprio.device
        dtype = proprio.dtype
        if hasattr(model.action_space, "normalize_state"):
            proprio_norm = model.action_space.normalize_state(proprio)
        elif hasattr(model.action_space, "normalize"):
            proprio_norm = model.action_space.normalize(proprio)
        else:
            proprio_norm = proprio

        generator = torch.Generator(device=device)
        generator.manual_seed(int(seed))
        x_t = torch.randn(
            (1, model.num_actions, model.action_space.dim_action),
            device=device,
            dtype=dtype,
            generator=generator,
        )
        initial_noise = x_t.detach().clone()
        path_variance = torch.zeros_like(x_t)
        last_step_variance = torch.zeros_like(x_t)
        denoise_means = []
        velocity_norms = []
        update_norms = []
        update_vectors = []
        steps = max(1, int(steps))
        dt = -1.0 / steps
        t = 1.0

        with torch.inference_mode():
            while t > -dt / 2:
                t_tensor = torch.full((1,), t, device=device, dtype=dtype)
                velocity, raw_uncertainty = model.transformer(
                    vlm_features=encoding["vlm_features"],
                    action_with_noise=x_t,
                    proprio=proprio_norm,
                    t=t_tensor,
                )
                variance = self.uncertainty_output_to_variance(
                    raw_uncertainty,
                    model.config.uncertainty_parameterization,
                    model.config.uncertainty_eps,
                )
                denoise_means.append(variance.mean())
                last_step_variance = variance
                path_variance = path_variance + (dt * dt) * variance
                update = dt * velocity
                velocity_norms.append(velocity.norm(dim=-1).mean())
                update_norms.append(update.norm(dim=-1).mean())
                update_vectors.append(update.flatten())
                x_t = x_t + update
                t += dt
            env = model.action_space.postprocess(x_t)

        norm_np = x_t[0].detach().cpu().numpy().astype(np.float32)
        env_np = env[0].detach().cpu().numpy().astype(np.float32)
        trace = DenoisingTrace(
            path_variance=path_variance[0].detach().cpu().numpy(),
            last_step_variance=last_step_variance[0].detach().cpu().numpy(),
            denoise_mean_trace=np.asarray(
                [float(value.detach().cpu()) for value in denoise_means],
                dtype=np.float32,
            ),
            velocity_norm_trace=np.asarray(
                [float(value.detach().cpu()) for value in velocity_norms],
                dtype=np.float32,
            ),
            update_norm_trace=np.asarray(
                [float(value.detach().cpu()) for value in update_norms],
                dtype=np.float32,
            ),
            update_vector_trace=np.stack(
                [value.detach().cpu().numpy() for value in update_vectors]
            ).astype(np.float32),
            initial_noise=initial_noise[0].detach().cpu().numpy(),
            final_action_normalized=norm_np,
        )
        trace.validate()
        return norm_np, env_np, trace
