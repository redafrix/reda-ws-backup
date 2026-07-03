"""In-process SimVLA model runtime."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Any

import numpy as np
import torch


@dataclass(frozen=True, slots=True)
class SimVLARuntimeConfig:
    simvla_repo_path: Path
    checkpoint_path: Path
    smolvlm_model_path: Path
    norm_stats_path: Path
    device: str = "cuda"
    action_mode: str = "libero_joint"
    num_view_slots: int = 3
    image_size: int = 384
    num_actions: int = 10
    inference_steps: int = 10
    predict_uncertainty: bool = True
    num_action_samples: int = 1


@dataclass(frozen=True, slots=True)
class SimVLAInferenceOutput:
    actions: np.ndarray
    uncertainty: dict[str, np.ndarray]


class SimVLARuntime:
    """Thin wrapper around the local SimVLA code, with strict shape checks."""

    def __init__(self, config: SimVLARuntimeConfig) -> None:
        self.config = config
        self.model: Any | None = None
        self.processor: Any | None = None
        self.device = torch.device(config.device)

    def load(self) -> None:
        self._require_paths()
        repo = str(self.config.simvla_repo_path)
        if repo not in sys.path:
            sys.path.insert(0, repo)

        import models

        self._validate_imported_models_package(models)
        from models import SmolVLMVLA, SmolVLMVLAProcessor, build_action_space

        self._validate_checkpoint_config()

        self.processor = SmolVLMVLAProcessor.from_pretrained(
            str(self.config.checkpoint_path),
            smolvlm_model_path=str(self.config.smolvlm_model_path),
        )
        self.model = SmolVLMVLA.from_pretrained(
            str(self.config.checkpoint_path),
            action_mode=self.config.action_mode,
            num_actions=self.config.num_actions,
            smolvlm_model_path=str(self.config.smolvlm_model_path),
            predict_uncertainty=self.config.predict_uncertainty,
            trust_remote_code=True,
        ).to(self.device)
        self.model.action_space = build_action_space(
            self.config.action_mode,
            norm_stats_path=str(self.config.norm_stats_path),
        )
        self.model.eval()

    def infer(
        self,
        language_instruction: str,
        image_input: torch.Tensor,
        image_mask: torch.Tensor,
        proprio: np.ndarray,
    ) -> SimVLAInferenceOutput:
        if self.model is None or self.processor is None:
            raise RuntimeError("SimVLARuntime.load() must be called before infer().")
        self._validate_inference_inputs(language_instruction, image_input, image_mask)
        proprio_tensor = torch.as_tensor(proprio, dtype=torch.float32, device=self.device).view(1, -1)
        if proprio_tensor.shape != (1, 8):
            raise ValueError(f"SimVLA proprio must have shape (8,), got {tuple(proprio_tensor.shape)}.")

        encoded = self.processor.encode_language(language_instruction)
        input_ids = encoded["input_ids"].to(self.device)
        image_input = image_input.to(device=self.device, dtype=torch.float32)
        image_mask = image_mask.to(device=self.device, dtype=torch.bool)
        with torch.no_grad():
            if self.config.predict_uncertainty:
                output = self.model.generate_actions_with_uncertainty(
                    input_ids=input_ids,
                    image_input=image_input,
                    image_mask=image_mask,
                    proprio=proprio_tensor,
                    steps=self.config.inference_steps,
                    num_action_samples=self.config.num_action_samples,
                )
                actions = output["action"]
                uncertainty = {
                    key: value.detach().cpu().numpy()
                    for key, value in output.items()
                    if key != "action" and torch.is_tensor(value)
                }
                self._validate_uncertainty(uncertainty)
            else:
                actions = self.model.generate_actions(
                    input_ids=input_ids,
                    image_input=image_input,
                    image_mask=image_mask,
                    proprio=proprio_tensor,
                    steps=self.config.inference_steps,
                )
                uncertainty = {}

        actions_np = actions.squeeze(0).detach().cpu().numpy().astype(np.float32)
        expected_shape = (self.config.num_actions, 7)
        if actions_np.shape != expected_shape:
            raise RuntimeError(f"SimVLA action output must have shape {expected_shape}, got {actions_np.shape}.")
        if not np.all(np.isfinite(actions_np)):
            raise RuntimeError("SimVLA action output contains non-finite values.")
        return SimVLAInferenceOutput(actions=actions_np, uncertainty=uncertainty)

    def _validate_inference_inputs(
        self,
        language_instruction: str,
        image_input: torch.Tensor,
        image_mask: torch.Tensor,
    ) -> None:
        if not isinstance(language_instruction, str) or not language_instruction.strip():
            raise ValueError("language_instruction must be a non-empty string.")
        expected_image_shape = (
            1,
            self.config.num_view_slots,
            3,
            self.config.image_size,
            self.config.image_size,
        )
        if tuple(image_input.shape) != expected_image_shape:
            raise ValueError(f"image_input must have shape {expected_image_shape}, got {tuple(image_input.shape)}.")
        expected_mask_shape = (1, self.config.num_view_slots)
        if tuple(image_mask.shape) != expected_mask_shape:
            raise ValueError(f"image_mask must have shape {expected_mask_shape}, got {tuple(image_mask.shape)}.")
        if image_mask.bool().tolist() != [[True, True, False]]:
            raise ValueError(f"image_mask must be [[True, True, False]], got {image_mask.bool().tolist()}.")

    def _validate_checkpoint_config(self) -> None:
        config_path = self.config.checkpoint_path / "config.json"
        if not config_path.is_file():
            raise FileNotFoundError(config_path)
        checkpoint = json.loads(config_path.read_text(encoding="utf-8"))
        expected = {
            "action_mode": self.config.action_mode,
            "num_actions": self.config.num_actions,
            "num_views": self.config.num_view_slots,
            "image_size": self.config.image_size,
        }
        for key, value in expected.items():
            if checkpoint.get(key) != value:
                raise ValueError(f"Checkpoint config {key}={checkpoint.get(key)!r} does not match {value!r}.")

    def _validate_imported_models_package(self, models_module: Any) -> None:
        module_file = Path(models_module.__file__).resolve()
        repo_root = self.config.simvla_repo_path.resolve()
        if not module_file.is_relative_to(repo_root):
            raise ImportError(f"Imported models package from {module_file}, expected under {repo_root}.")

    def _validate_uncertainty(self, uncertainty: dict[str, np.ndarray]) -> None:
        for key, value in uncertainty.items():
            if not np.all(np.isfinite(value)):
                raise RuntimeError(f"SimVLA uncertainty output {key!r} contains non-finite values.")

    def _require_paths(self) -> None:
        for path in (
            self.config.simvla_repo_path,
            self.config.checkpoint_path,
            self.config.smolvlm_model_path,
            self.config.norm_stats_path,
        ):
            if not path.exists():
                raise FileNotFoundError(path)
