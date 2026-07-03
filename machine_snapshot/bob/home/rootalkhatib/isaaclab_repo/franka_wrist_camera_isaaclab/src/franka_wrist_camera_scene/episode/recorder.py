"""Episode recorder for internal raw dataset format."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import atexit
from concurrent.futures import Future, ThreadPoolExecutor

import numpy as np
import torch
from isaaclab.scene import InteractiveScene

from franka_wrist_camera_scene.episode.suite import EMPTY_SUITE_METADATA, SuiteMetadata
from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
from franka_wrist_camera_scene.episode.camera_validation import validate_camera_recordings
from franka_wrist_camera_scene.episode.schema import EpisodeMetadata
from franka_wrist_camera_scene.utils.tensors import as_torch

_BACKGROUND_SAVE_EXECUTOR = ThreadPoolExecutor(max_workers=2, thread_name_prefix="episode-save-writer")
_PENDING_SAVE_FUTURES: list[Future] = []


def wait_for_pending_episode_writes() -> None:
    """Wait for queued background save writes and surface any writer errors."""
    while _PENDING_SAVE_FUTURES:
        future = _PENDING_SAVE_FUTURES.pop(0)
        future.result()


def wait_for_pending_video_writes() -> None:
    """Backward-compatible alias for waiting on background episode writes."""
    wait_for_pending_episode_writes()


atexit.register(wait_for_pending_episode_writes)


def _camera_video_fps(camera_timestamps_s: list[float]) -> float:
    if len(camera_timestamps_s) < 2:
        return 1.0

    intervals = np.diff(np.asarray(camera_timestamps_s, dtype=np.float32))
    median_interval = float(np.median(intervals))
    if median_interval <= 0.0:
        return 1.0
    return 1.0 / median_interval


def _write_rgb_video(path: Path, frames: list[np.ndarray], fps: float) -> None:
    import cv2

    if not frames:
        raise RuntimeError(f"Cannot write video with no frames: {path}")

    first_frame = frames[0]
    height, width = first_frame.shape[:2]
    writer = cv2.VideoWriter(
        str(path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )
    if not writer.isOpened():
        raise RuntimeError(f"Failed to open video writer: {path}")

    try:
        for frame in frames:
            writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    finally:
        writer.release()


def _write_npz_file(path: Path, compress: bool, arrays: dict[str, np.ndarray]) -> None:
    if compress:
        np.savez_compressed(path, **arrays)
    else:
        np.savez(path, **arrays)


def _refresh_camera_outputs(scene: InteractiveScene, sim_dt: float) -> None:
    for camera_name in ("agent_camera", "wrist_camera"):
        scene[camera_name].update(sim_dt, force_recompute=True)


@dataclass(slots=True)
class EpisodeRecorder:
    """Record one episode into a simple internal directory format."""

    output_dir: Path
    episode_id: int
    task_name: str
    instruction: str
    sim_dt: float
    ee_body_id: int
    object_name: str
    env_index: int | None = None
    max_steps: int | None = None
    state_record_stride: int = 1
    compress_trajectory: bool = False
    save_rgb_arrays: bool = False
    save_training_rgb_arrays: bool = True
    background_video_encoding: bool = True

    record_cameras: bool = False
    record_depth: bool = False
    camera_width: int | None = None
    camera_height: int | None = None
    camera_fps: int | None = None
    suite: SuiteMetadata = EMPTY_SUITE_METADATA
    object_pos_local: tuple[float, float, float] | None = None
    object_quat_wxyz: tuple[float, float, float, float] | None = None
    object_reach_offset_local: tuple[float, float, float] | None = None
    reach_success_threshold_m: float | None = None
    max_success_target_displacement_m: float | None = None
    success_mode: str | None = None
    place_pos_local: tuple[float, float, float] | None = None
    seed: int | None = None
    object_xy_offset: tuple[float, float] | None = None
    place_xy_offset: tuple[float, float] | None = None
    object_category_id: str | None = None
    object_variant_id: str | None = None
    object_label: str | None = None
    object_usd_path: str | None = None
    object_grasp_strategy: str | None = None
    target_source_name: str | None = None
    object_affordances: list[str] | None = None
    object_yaw_relevant: bool | None = None
    object_planar_aspect_ratio: float | None = None
    object_planar_minor_axis_local: tuple[float, float] | None = None
    object_planar_major_axis_local: tuple[float, float] | None = None
    grasp_closing_axis_xy: tuple[float, float] | None = None
    placement_target_category_id: str | None = None
    placement_target_variant_id: str | None = None
    placement_target_label: str | None = None
    placement_target_usd_path: str | None = None
    placement_target_grasp_strategy: str | None = None
    placement_target_pos_local: tuple[float, float, float] | None = None
    placement_target_quat_wxyz: tuple[float, float, float, float] | None = None
    light_intensity: float | None = None
    light_color: tuple[float, float, float] | None = None
    table_color: tuple[float, float, float] | None = None
    active_clutter_count: int | None = None
    clutter_objects: list[dict] | None = None

    joint_pos: list[torch.Tensor] = field(default_factory=list)
    joint_vel: list[torch.Tensor] = field(default_factory=list)
    ee_pos_w: list[torch.Tensor] = field(default_factory=list)
    ee_quat_w: list[torch.Tensor] = field(default_factory=list)
    object_pos_w: list[torch.Tensor] = field(default_factory=list)
    action_target_pos_w: list[torch.Tensor] = field(default_factory=list)
    action_target_quat_w: list[torch.Tensor] = field(default_factory=list)
    action_finger_opening_m: list[torch.Tensor] = field(default_factory=list)

    timestamps_s: list[torch.Tensor] = field(default_factory=list)
    state_step_indices: list[torch.Tensor] = field(default_factory=list)
    camera_step_indices: list[int] = field(default_factory=list)
    camera_timestamps_s: list[float] = field(default_factory=list)
    agent_rgb: list[np.ndarray] = field(default_factory=list)
    wrist_rgb: list[np.ndarray] = field(default_factory=list)
    agent_depth: list[np.ndarray] = field(default_factory=list)
    wrist_depth: list[np.ndarray] = field(default_factory=list)
    _state_count: int = 0
    _state_capacity: int = 0
    _timestamps_s_buffer: torch.Tensor | None = None
    _state_step_indices_buffer: torch.Tensor | None = None
    _joint_pos_buffer: torch.Tensor | None = None
    _joint_vel_buffer: torch.Tensor | None = None
    _ee_pos_w_buffer: torch.Tensor | None = None
    _ee_quat_w_buffer: torch.Tensor | None = None
    _object_pos_w_buffer: torch.Tensor | None = None
    _action_target_pos_w_buffer: torch.Tensor | None = None
    _action_target_quat_w_buffer: torch.Tensor | None = None
    _action_finger_opening_m_buffer: torch.Tensor | None = None

    def __post_init__(self) -> None:
        if self.max_steps is not None and self.max_steps <= 0:
            raise ValueError(f"max_steps must be positive when set, got {self.max_steps}.")
        if self.state_record_stride <= 0:
            raise ValueError(f"state_record_stride must be positive, got {self.state_record_stride}.")
        if self.save_rgb_arrays and not self.record_cameras:
            raise ValueError("save_rgb_arrays requires record_cameras=true.")

    @property
    def episode_dir(self) -> Path:
        return self.output_dir / f"{self.episode_id:06d}"

    def validate_output_path(self) -> None:
        if self.episode_dir.exists():
            raise FileExistsError(f"Episode directory already exists: {self.episode_dir}")

    def record_step(self, scene: InteractiveScene, cmd: PolicyCommand, step: int, sim_time_s: float) -> None:
        # Dataset convention: record state_t and command_t before advancing to state_{t+1}.
        if step % self.state_record_stride != 0:
            return

        robot = scene["robot"]
        obj = scene[self.object_name]
        env_slice = slice(None) if self.env_index is None else slice(self.env_index, self.env_index + 1)

        joint_pos = as_torch(robot.data.joint_pos)[env_slice].detach().clone()
        joint_vel = as_torch(robot.data.joint_vel)[env_slice].detach().clone()
        ee_pose_w = as_torch(robot.data.body_pose_w)[env_slice, self.ee_body_id]
        ee_pos_w = ee_pose_w[:, :3].detach().clone()
        ee_quat_w = ee_pose_w[:, 3:7].detach().clone()
        object_pos_w = as_torch(obj.data.root_pos_w)[env_slice].detach().clone()
        action_target_pos_w = cmd.target_pos_w[env_slice].detach().clone()
        if cmd.target_quat_w is None:
            action_target_quat_w = torch.full(
                (1 if self.env_index is not None else scene.num_envs, 4),
                torch.nan,
                device=action_target_pos_w.device,
                dtype=action_target_pos_w.dtype,
            )
        else:
            action_target_quat_w = cmd.target_quat_w[env_slice].detach().clone()
        finger_opening_m = self._finger_opening_value(cmd.finger_opening_m)

        if self.max_steps is not None:
            self._record_step_to_buffers(
                step=step,
                sim_time_s=sim_time_s,
                joint_pos=joint_pos,
                joint_vel=joint_vel,
                ee_pos_w=ee_pos_w,
                ee_quat_w=ee_quat_w,
                object_pos_w=object_pos_w,
                action_target_pos_w=action_target_pos_w,
                action_target_quat_w=action_target_quat_w,
                finger_opening_m=finger_opening_m,
            )
            return

        self.timestamps_s.append(torch.tensor(sim_time_s, device=joint_pos.device, dtype=torch.float32))
        self.state_step_indices.append(torch.tensor(step, device=joint_pos.device, dtype=torch.int64))
        self.joint_pos.append(joint_pos)
        self.joint_vel.append(joint_vel)
        self.ee_pos_w.append(ee_pos_w)
        self.ee_quat_w.append(ee_quat_w)
        self.object_pos_w.append(object_pos_w)
        self.action_target_pos_w.append(action_target_pos_w)
        self.action_target_quat_w.append(action_target_quat_w)
        self.action_finger_opening_m.append(
            torch.tensor(finger_opening_m, device=joint_pos.device, dtype=torch.float32)
        )

    def _finger_opening_value(self, finger_opening_m: float | torch.Tensor) -> float:
        if not isinstance(finger_opening_m, torch.Tensor):
            return float(finger_opening_m)
        if self.env_index is None:
            return float(finger_opening_m.reshape(-1)[0].item())
        return float(finger_opening_m[self.env_index].reshape(-1)[0].item())

    @property
    def recorded_state_count(self) -> int:
        if self.max_steps is not None:
            return self._state_count
        return len(self.joint_pos)

    def first_object_pos_w(self) -> np.ndarray:
        if self.recorded_state_count == 0:
            raise RuntimeError("No state samples were recorded.")
        if self._object_pos_w_buffer is not None:
            return self._object_pos_w_buffer[0].detach().cpu().numpy()
        return self.object_pos_w[0].detach().cpu().numpy()

    def _ensure_state_buffers(
        self,
        *,
        joint_pos: torch.Tensor,
        joint_vel: torch.Tensor,
        ee_pos_w: torch.Tensor,
        ee_quat_w: torch.Tensor,
        object_pos_w: torch.Tensor,
        action_target_pos_w: torch.Tensor,
        action_target_quat_w: torch.Tensor,
    ) -> None:
        if self._joint_pos_buffer is not None:
            return
        if self.max_steps is None:
            raise RuntimeError("State buffers require max_steps.")

        self._state_capacity = self.max_steps // self.state_record_stride + 2
        device = joint_pos.device
        self._timestamps_s_buffer = torch.empty(self._state_capacity, device=device, dtype=torch.float32)
        self._state_step_indices_buffer = torch.empty(self._state_capacity, device=device, dtype=torch.int64)
        self._joint_pos_buffer = torch.empty((self._state_capacity, *joint_pos.shape), device=device, dtype=joint_pos.dtype)
        self._joint_vel_buffer = torch.empty((self._state_capacity, *joint_vel.shape), device=device, dtype=joint_vel.dtype)
        self._ee_pos_w_buffer = torch.empty((self._state_capacity, *ee_pos_w.shape), device=device, dtype=ee_pos_w.dtype)
        self._ee_quat_w_buffer = torch.empty((self._state_capacity, *ee_quat_w.shape), device=device, dtype=ee_quat_w.dtype)
        self._object_pos_w_buffer = torch.empty(
            (self._state_capacity, *object_pos_w.shape),
            device=device,
            dtype=object_pos_w.dtype,
        )
        self._action_target_pos_w_buffer = torch.empty(
            (self._state_capacity, *action_target_pos_w.shape),
            device=device,
            dtype=action_target_pos_w.dtype,
        )
        self._action_target_quat_w_buffer = torch.empty(
            (self._state_capacity, *action_target_quat_w.shape),
            device=device,
            dtype=action_target_quat_w.dtype,
        )
        self._action_finger_opening_m_buffer = torch.empty(self._state_capacity, device=device, dtype=torch.float32)

    def _record_step_to_buffers(
        self,
        *,
        step: int,
        sim_time_s: float,
        joint_pos: torch.Tensor,
        joint_vel: torch.Tensor,
        ee_pos_w: torch.Tensor,
        ee_quat_w: torch.Tensor,
        object_pos_w: torch.Tensor,
        action_target_pos_w: torch.Tensor,
        action_target_quat_w: torch.Tensor,
        finger_opening_m: float,
    ) -> None:
        self._ensure_state_buffers(
            joint_pos=joint_pos,
            joint_vel=joint_vel,
            ee_pos_w=ee_pos_w,
            ee_quat_w=ee_quat_w,
            object_pos_w=object_pos_w,
            action_target_pos_w=action_target_pos_w,
            action_target_quat_w=action_target_quat_w,
        )
        if self._state_count >= self._state_capacity:
            raise RuntimeError(
                f"EpisodeRecorder state buffer overflow: capacity={self._state_capacity}, "
                f"step={step}, stride={self.state_record_stride}."
            )

        index = self._state_count
        self._timestamps_s_buffer[index] = float(sim_time_s)
        self._state_step_indices_buffer[index] = int(step)
        self._joint_pos_buffer[index].copy_(joint_pos)
        self._joint_vel_buffer[index].copy_(joint_vel)
        self._ee_pos_w_buffer[index].copy_(ee_pos_w)
        self._ee_quat_w_buffer[index].copy_(ee_quat_w)
        self._object_pos_w_buffer[index].copy_(object_pos_w)
        self._action_target_pos_w_buffer[index].copy_(action_target_pos_w)
        self._action_target_quat_w_buffer[index].copy_(action_target_quat_w)
        self._action_finger_opening_m_buffer[index] = float(finger_opening_m)
        self._state_count += 1

    def record_cameras_step(
        self,
        scene: InteractiveScene,
        step: int,
        sim_time_s: float,
        refresh: bool = True,
    ) -> None:
        """Record camera observations for this control step."""
        if not self.record_cameras:
            return

        if refresh:
            _refresh_camera_outputs(scene, self.sim_dt)

        self.camera_step_indices.append(int(step))
        self.camera_timestamps_s.append(float(sim_time_s))

        for camera_name, buffer in (
            ("agent_camera", self.agent_rgb),
            ("wrist_camera", self.wrist_rgb),
        ):
            camera_env_index = 0 if self.env_index is None else self.env_index
            rgb = scene[camera_name].data.output["rgb"][camera_env_index].detach().cpu().numpy()[..., :3]
            buffer.append(np.clip(rgb, 0, 255).astype(np.uint8).copy())

        if self.record_depth:
            for camera_name, buffer in (
                ("agent_camera", self.agent_depth),
                ("wrist_camera", self.wrist_depth),
            ):
                camera_env_index = 0 if self.env_index is None else self.env_index
                depth = scene[camera_name].data.output["distance_to_image_plane"][camera_env_index, ..., 0]
                buffer.append(depth.detach().cpu().numpy().astype(np.float32).copy())

    def save(self, success: bool, success_mode: str | None = None) -> Path:
        episode_dir = self.episode_dir
        if episode_dir.exists():
            raise FileExistsError(f"Episode directory already exists: {episode_dir}")
        episode_dir.mkdir(parents=True)

        arrays = self._state_arrays()

        if self.record_cameras:
            # Enforce that recorded RGB camera frames are valid and not completely black/zeros
            validate_camera_recordings(self.agent_rgb, self.wrist_rgb)
            video_fps = _camera_video_fps(self.camera_timestamps_s)
            self._write_or_queue_rgb_video(episode_dir / "agent_camera.mp4", self.agent_rgb, video_fps)
            arrays.update(
                camera_step_indices=np.asarray(self.camera_step_indices, dtype=np.int64),
                camera_timestamps_s=np.asarray(self.camera_timestamps_s, dtype=np.float32),
            )
            if self.save_training_rgb_arrays:
                self._write_or_queue_npz(
                    episode_dir / "rgb.npz",
                    compress=False,
                    arrays={
                        "agent_rgb": np.asarray(self.agent_rgb, dtype=np.uint8),
                        "wrist_rgb": np.asarray(self.wrist_rgb, dtype=np.uint8),
                    },
                )
            if self.save_rgb_arrays:
                arrays.update(
                    agent_rgb=np.asarray(self.agent_rgb, dtype=np.uint8),
                    wrist_rgb=np.asarray(self.wrist_rgb, dtype=np.uint8),
                )

        if self.record_cameras and self.record_depth:
            self._write_or_queue_npz(
                episode_dir / "depth.npz",
                compress=True,
                arrays={
                    "agent_depth": np.asarray(self.agent_depth, dtype=np.float32),
                    "wrist_depth": np.asarray(self.wrist_depth, dtype=np.float32),
                },
            )

        self._write_npz(episode_dir / "trajectory.npz", **arrays)

        meta = EpisodeMetadata(
            episode_id=self.episode_id,
            task_name=self.task_name,
            instruction=self.instruction,
            success=success,
            success_mode=success_mode,
            num_steps=self.recorded_state_count,
            sim_dt=self.sim_dt,
            seed=self.seed,
            record_cameras=self.record_cameras,
            record_depth=self.record_depth,
            num_camera_frames=len(self.camera_step_indices) if self.record_cameras else 0,
            camera_width=self.camera_width,
            camera_height=self.camera_height,
            camera_fps=self.camera_fps,
            suite_name=self.suite.name,
            suite_split=self.suite.split,
            suite_difficulty=self.suite.difficulty,
            suite_tags=self.suite.tags,
            suite_description=self.suite.description,
            object_pos_local=self.object_pos_local,
            object_quat_wxyz=self.object_quat_wxyz,
            object_reach_offset_local=self.object_reach_offset_local,
            reach_success_threshold_m=self.reach_success_threshold_m,
            max_success_target_displacement_m=self.max_success_target_displacement_m,
            place_pos_local=self.place_pos_local,
            object_xy_offset=self.object_xy_offset,
            place_xy_offset=self.place_xy_offset,
            object_category_id=self.object_category_id,
            object_variant_id=self.object_variant_id,
            object_label=self.object_label,
            object_usd_path=self.object_usd_path,
            object_grasp_strategy=self.object_grasp_strategy,
            target_source_name=self.target_source_name,
            object_affordances=self.object_affordances,
            object_yaw_relevant=self.object_yaw_relevant,
            object_planar_aspect_ratio=self.object_planar_aspect_ratio,
            object_planar_minor_axis_local=self.object_planar_minor_axis_local,
            object_planar_major_axis_local=self.object_planar_major_axis_local,
            grasp_closing_axis_xy=self.grasp_closing_axis_xy,
            placement_target_category_id=self.placement_target_category_id,
            placement_target_variant_id=self.placement_target_variant_id,
            placement_target_label=self.placement_target_label,
            placement_target_usd_path=self.placement_target_usd_path,
            placement_target_grasp_strategy=self.placement_target_grasp_strategy,
            placement_target_pos_local=self.placement_target_pos_local,
            placement_target_quat_wxyz=self.placement_target_quat_wxyz,
            light_intensity=self.light_intensity,
            light_color=self.light_color,
            table_color=self.table_color,
            active_clutter_count=self.active_clutter_count,
            clutter_objects=self.clutter_objects,
        )
        meta.save(episode_dir / "meta.json")
        return episode_dir

    def _write_npz(self, path: Path, **arrays: np.ndarray) -> None:
        _write_npz_file(path, self.compress_trajectory, arrays)

    def _write_or_queue_npz(self, path: Path, *, compress: bool, arrays: dict[str, np.ndarray]) -> None:
        if not self.background_video_encoding:
            _write_npz_file(path, compress, arrays)
            return
        _PENDING_SAVE_FUTURES.append(
            _BACKGROUND_SAVE_EXECUTOR.submit(_write_npz_file, path, compress, arrays)
        )

    def _write_or_queue_rgb_video(self, path: Path, frames: list[np.ndarray], fps: float) -> None:
        if not self.background_video_encoding:
            _write_rgb_video(path, frames, fps)
            return
        _PENDING_SAVE_FUTURES.append(_BACKGROUND_SAVE_EXECUTOR.submit(_write_rgb_video, path, list(frames), fps))

    def _state_arrays(self) -> dict[str, np.ndarray]:
        if self._joint_pos_buffer is not None:
            count = self._state_count
            return {
                "timestamps_s": self._timestamps_s_buffer[:count].detach().cpu().numpy(),
                "state_step_indices": self._state_step_indices_buffer[:count].detach().cpu().numpy(),
                "joint_pos": self._joint_pos_buffer[:count].detach().cpu().numpy(),
                "joint_vel": self._joint_vel_buffer[:count].detach().cpu().numpy(),
                "ee_pos_w": self._ee_pos_w_buffer[:count].detach().cpu().numpy(),
                "ee_quat_w": self._ee_quat_w_buffer[:count].detach().cpu().numpy(),
                "object_pos_w": self._object_pos_w_buffer[:count].detach().cpu().numpy(),
                "action_target_pos_w": self._action_target_pos_w_buffer[:count].detach().cpu().numpy(),
                "action_target_quat_w": self._action_target_quat_w_buffer[:count].detach().cpu().numpy(),
                "action_finger_opening_m": self._action_finger_opening_m_buffer[:count].detach().cpu().numpy(),
            }

        def stack_or_empty(values: list[torch.Tensor], shape: tuple[int, ...], dtype: np.dtype) -> np.ndarray:
            if values:
                return torch.stack(values).detach().cpu().numpy()
            return np.empty(shape, dtype=dtype)

        return {
            "timestamps_s": stack_or_empty(self.timestamps_s, (0,), np.float32).astype(np.float32, copy=False),
            "state_step_indices": stack_or_empty(self.state_step_indices, (0,), np.int64).astype(np.int64, copy=False),
            "joint_pos": stack_or_empty(self.joint_pos, (0,), np.float32),
            "joint_vel": stack_or_empty(self.joint_vel, (0,), np.float32),
            "ee_pos_w": stack_or_empty(self.ee_pos_w, (0,), np.float32),
            "ee_quat_w": stack_or_empty(self.ee_quat_w, (0,), np.float32),
            "object_pos_w": stack_or_empty(self.object_pos_w, (0,), np.float32),
            "action_target_pos_w": stack_or_empty(self.action_target_pos_w, (0,), np.float32),
            "action_target_quat_w": stack_or_empty(self.action_target_quat_w, (0,), np.float32),
            "action_finger_opening_m": stack_or_empty(self.action_finger_opening_m, (0,), np.float32).astype(
                np.float32,
                copy=False,
            ),
        }
