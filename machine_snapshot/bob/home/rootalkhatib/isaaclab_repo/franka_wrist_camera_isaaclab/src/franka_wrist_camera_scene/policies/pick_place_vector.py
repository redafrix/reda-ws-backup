"""Vectorized pick-place policy wrapper."""

from __future__ import annotations

from dataclasses import dataclass

import torch
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene

from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
from franka_wrist_camera_scene.utils.tensors import as_torch


@dataclass(slots=True)
class _SlicedData:
    data: object
    env_index: int
    source_num_envs: int

    def __getattr__(self, name: str):
        value = getattr(self.data, name)
        if hasattr(value, "torch"):
            tensor = value.torch
            if isinstance(tensor, torch.Tensor) and tensor.shape[:1] == (self.source_num_envs,):
                return tensor[self.env_index : self.env_index + 1]
            return tensor
        if isinstance(value, torch.Tensor) and value.shape[:1] == (self.source_num_envs,):
            return value[self.env_index : self.env_index + 1]
        return value


@dataclass(slots=True)
class _SlicedEntity:
    entity: object
    env_index: int
    source_num_envs: int

    @property
    def data(self) -> _SlicedData:
        return _SlicedData(self.entity.data, self.env_index, self.source_num_envs)

    @property
    def device(self) -> torch.device:
        return self.entity.device

    def find_bodies(self, *args, **kwargs):
        return self.entity.find_bodies(*args, **kwargs)


class _EnvSliceScene:
    def __init__(self, scene: InteractiveScene, env_index: int):
        self._scene = scene
        self._env_index = env_index
        self.num_envs = 1
        self.env_origins = scene.env_origins[env_index : env_index + 1]

    def __getitem__(self, name: str) -> _SlicedEntity:
        return _SlicedEntity(self._scene[name], self._env_index, self._scene.num_envs)


class VectorPickPlaceScriptedPolicy:
    """Run one pick-place FSM per env and batch their commands."""

    def __init__(self, specs: tuple[PickPlaceTaskSpec, ...], active_env_count: int):
        if not specs:
            raise ValueError("VectorPickPlaceScriptedPolicy requires at least one spec.")
        if active_env_count <= 0 or active_env_count > len(specs):
            raise ValueError(
                f"active_env_count must be in [1, {len(specs)}], got {active_env_count}."
            )
        self.specs = specs
        self.active_env_count = active_env_count
        self._scene: InteractiveScene | None = None
        self._robot: Articulation | None = None
        self._policies: list[PickPlaceScriptedPolicy] = []
        self._failed = [False] * active_env_count
        self._failure_reasons: list[str | None] = [None] * active_env_count

    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
        if len(self.specs) != scene.num_envs:
            raise ValueError(
                f"Vector policy expected {scene.num_envs} specs, got {len(self.specs)}."
            )
        self._scene = scene
        self._robot = robot
        self._policies = []
        for env_index, spec in enumerate(self.specs):
            policy = PickPlaceScriptedPolicy(spec)
            policy.bind(_EnvSliceScene(scene, env_index), _SlicedEntity(robot, env_index, scene.num_envs))
            self._policies.append(policy)

    def reset(self) -> None:
        if not self._policies:
            raise RuntimeError("VectorPickPlaceScriptedPolicy was not bound before reset().")
        for policy in self._policies:
            policy.reset()
        self._failed = [False] * self.active_env_count
        self._failure_reasons = [None] * self.active_env_count

    def is_failed(self, env_index: int) -> bool:
        if env_index < 0 or env_index >= self.active_env_count:
            raise IndexError(f"env_index out of active range: {env_index}")
        return self._failed[env_index]

    def failure_reason(self, env_index: int) -> str | None:
        if env_index < 0 or env_index >= self.active_env_count:
            raise IndexError(f"env_index out of active range: {env_index}")
        return self._failure_reasons[env_index]

    def _failed_hold_command(self, env_index: int, policy: PickPlaceScriptedPolicy) -> PolicyCommand:
        if self._robot is None:
            raise RuntimeError("VectorPickPlaceScriptedPolicy was not bound before fallback command.")
        if policy._ee_body_id is None:
            raise RuntimeError("Child pick-place policy is missing end-effector body id.")

        ee_pos_w = as_torch(self._robot.data.body_pose_w)[env_index : env_index + 1, policy._ee_body_id, :3]
        quat_w = policy.quat_wxyz.to(device=ee_pos_w.device, dtype=ee_pos_w.dtype).view(1, 4)
        return PolicyCommand(
            target_pos_w=ee_pos_w,
            target_quat_w=quat_w,
            finger_opening_m=policy.spec.open_finger_m,
            done=True,
        )

    def step(self, obs: dict | None, sim_time_s: float) -> PolicyCommand:
        if not self._policies:
            raise RuntimeError("VectorPickPlaceScriptedPolicy was not bound before step().")

        commands = []
        for env_index, policy in enumerate(self._policies):
            if env_index < self.active_env_count and self._failed[env_index]:
                commands.append(self._failed_hold_command(env_index, policy))
                continue

            try:
                commands.append(policy.step(obs, sim_time_s))
            except Exception as err:
                if env_index >= self.active_env_count:
                    raise RuntimeError(
                        "Inactive vector pick-place child policy failed "
                        f"env_index={env_index}, state={policy.state}, sim_time_s={sim_time_s:.4f}: {err}"
                    ) from err
                self._failed[env_index] = True
                self._failure_reasons[env_index] = (
                    f"policy_exception: state={policy.state}, sim_time_s={sim_time_s:.4f}: {err}"
                )
                print(
                    "[WARN] Vector pick-place child policy failed; "
                    f"marking env_index={env_index} as failed: {err}",
                    flush=True,
                )
                commands.append(self._failed_hold_command(env_index, policy))

        target_quats = [cmd.target_quat_w for cmd in commands]
        if any(quat is None for quat in target_quats):
            raise RuntimeError("Pick-place vector policy requires pose commands from every env.")

        target_pos_w = torch.cat([cmd.target_pos_w for cmd in commands], dim=0)
        target_quat_w = torch.cat([cmd.target_quat_w for cmd in commands if cmd.target_quat_w is not None], dim=0)
        finger_opening_m = torch.tensor(
            [float(cmd.finger_opening_m) for cmd in commands],
            device=target_pos_w.device,
            dtype=target_pos_w.dtype,
        ).view(-1, 1)
        done = torch.tensor(
            [bool(cmd.done) for cmd in commands[: self.active_env_count]],
            device=target_pos_w.device,
            dtype=torch.bool,
        )
        return PolicyCommand(
            target_pos_w=target_pos_w,
            target_quat_w=target_quat_w,
            finger_opening_m=finger_opening_m,
            done=done,
        )
