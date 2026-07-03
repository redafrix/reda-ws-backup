"""Remote OpenPI Pi0.5 websocket runtime."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass(frozen=True, slots=True)
class Pi05RemoteRuntimeConfig:
    host: str = "127.0.0.1"
    port: int = 8005
    action_horizon: int = 10
    action_dim: int = 7
    observation_schema: str = "libero"


class Pi05RemoteRuntime:
    """Strict client for an OpenPI policy server serving `pi05_libero`."""

    def __init__(self, config: Pi05RemoteRuntimeConfig) -> None:
        self.config = config
        self.client: Any | None = None

    def load(self) -> None:
        from openpi_client import websocket_client_policy

        self.client = websocket_client_policy.WebsocketClientPolicy(host=self.config.host, port=self.config.port)
        metadata = self.client.get_server_metadata()
        print(f"[INFO] Connected to Pi0.5 policy server metadata={metadata}", flush=True)

    def infer(self, observation: dict) -> np.ndarray:
        if self.client is None:
            raise RuntimeError("Pi05RemoteRuntime.load() must be called before infer().")
        self._validate_observation(observation)
        output = self.client.infer(observation)
        if "actions" not in output:
            raise RuntimeError(f"Pi0.5 server response missing 'actions'; keys={sorted(output)}")
        actions = np.asarray(output["actions"], dtype=np.float32)
        expected_shape = (self.config.action_horizon, self.config.action_dim)
        if actions.shape != expected_shape:
            raise RuntimeError(f"Pi0.5 action output must have shape {expected_shape}, got {actions.shape}.")
        if not np.all(np.isfinite(actions)):
            raise RuntimeError("Pi0.5 action output contains non-finite values.")
        return actions

    def reset(self) -> None:
        if self.client is not None:
            self.client.reset()

    def _validate_observation(self, observation: dict) -> None:
        if self.config.observation_schema == "libero":
            self._validate_libero_observation(observation)
        elif self.config.observation_schema == "droid":
            self._validate_droid_observation(observation)
        else:
            raise ValueError(f"Unsupported Pi0.5 observation_schema={self.config.observation_schema!r}.")

    def _validate_libero_observation(self, observation: dict) -> None:
        required = {"observation/image", "observation/wrist_image", "observation/state", "prompt"}
        missing = required - set(observation)
        if missing:
            raise ValueError(f"Pi0.5 observation missing keys: {sorted(missing)}")
        for key in ("observation/image", "observation/wrist_image"):
            self._validate_image(observation, key)
        state = np.asarray(observation["observation/state"], dtype=np.float32)
        if state.shape != (8,):
            raise ValueError(f"observation/state must have shape (8,), got {state.shape}.")
        if not np.all(np.isfinite(state)):
            raise ValueError("observation/state contains non-finite values.")
        self._validate_prompt(observation)

    def _validate_droid_observation(self, observation: dict) -> None:
        required = {
            "observation/exterior_image_1_left",
            "observation/wrist_image_left",
            "observation/joint_position",
            "observation/gripper_position",
            "prompt",
        }
        missing = required - set(observation)
        if missing:
            raise ValueError(f"Pi0.5 DROID observation missing keys: {sorted(missing)}")
        for key in ("observation/exterior_image_1_left", "observation/wrist_image_left"):
            self._validate_image(observation, key)
        joint_position = np.asarray(observation["observation/joint_position"], dtype=np.float32)
        if joint_position.shape != (7,):
            raise ValueError(f"observation/joint_position must have shape (7,), got {joint_position.shape}.")
        if not np.all(np.isfinite(joint_position)):
            raise ValueError("observation/joint_position contains non-finite values.")
        gripper_position = np.asarray(observation["observation/gripper_position"], dtype=np.float32)
        if gripper_position.shape != (1,):
            raise ValueError(f"observation/gripper_position must have shape (1,), got {gripper_position.shape}.")
        if not np.all(np.isfinite(gripper_position)):
            raise ValueError("observation/gripper_position contains non-finite values.")
        self._validate_prompt(observation)

    def _validate_image(self, observation: dict, key: str) -> None:
        image = np.asarray(observation[key])
        if image.shape != (224, 224, 3) or image.dtype != np.uint8:
            raise ValueError(f"{key} must be uint8 (224, 224, 3), got {image.dtype} {image.shape}.")
        if not image.flags.c_contiguous:
            raise ValueError(f"{key} must be contiguous.")

    def _validate_prompt(self, observation: dict) -> None:
        prompt = observation["prompt"]
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("prompt must be a non-empty string.")
