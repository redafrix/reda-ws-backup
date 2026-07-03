"""Run LIBERO evaluation with the Video Action Model (VAM) policy."""

from __future__ import annotations

import json
import os
import pathlib
import pickle
import random
import re
import time
from collections import deque
from collections.abc import Iterable
from pathlib import Path

import imageio
import numpy as np
import torch
import torch.nn.functional as F
torch.set_float32_matmul_precision('high')
import tqdm
import tyro
from einops import rearrange
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import bddl_utils as BDDLUtils
from libero.libero.envs import OffScreenRenderEnv
from scipy.spatial.transform import Rotation

from cosmos_predict2.configs.config import make_config
from cosmos_predict2.data.action.utils import extract_normalization_types
from cosmos_predict2.pipelines.video2world import Video2WorldPipeline
from cosmos_predict2.pipelines.video2world2action import Video2World2ActionPipeline
from cosmos_predict2.pipelines.world2action import World2ActionPipeline
from imaginaire.constants import CHECKPOINTS_DIR
from imaginaire.lazy_config import instantiate
from imaginaire.utils.config_helper import override
from model.uncertainty import V2WCalibration, V2WUncertaintyModel
from model.uncertainty.v2w_losses import clamped_log_variance

try:
    from eval.libero.prompt_embeddings import prompt_embedding_filename
except ImportError:
    from prompt_embeddings import prompt_embedding_filename

LIBERO_SUITE_MAX_STEPS = {
    "libero_spatial": 220,
    "libero_object": 280,
    "libero_goal": 300,
    "libero_spatial_object": 220,
    "libero_object_object": 280,
    "libero_goal_object": 300,
    "libero_goal_env": 300,
    "libero_goal_lan": 300,
    "libero_goal_object_ood": 300,
    "libero_goal_relation_ood": 300,
    "libero_goal_semantic_ood": 300,
    "libero_goal_swap": 300,
    "libero_goal_task": 300,
    "libero_goal_temp": 300,
}

CAMERA_HEIGHT = 480
CAMERA_WIDTH = 640

DUMMY_ACTION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]


def goal_predicate_state(env: OffScreenRenderEnv) -> dict[str, object]:
    """Evaluate each BDDL goal predicate in the current simulator state."""
    task_env = getattr(env, "env", None)
    if task_env is None or not hasattr(task_env, "parsed_problem") or not hasattr(task_env, "_eval_predicate"):
        raise RuntimeError("LIBERO environment does not expose parsed_problem and _eval_predicate.")

    goal_state = task_env.parsed_problem.get("goal_state")
    if goal_state is None:
        raise RuntimeError("LIBERO parsed_problem does not contain goal_state.")

    predicates = [_serialize_predicate(predicate) for predicate in goal_state]
    predicate_names = [_predicate_name(predicate) for predicate in goal_state]
    satisfied = [bool(task_env._eval_predicate(predicate)) for predicate in goal_state]
    satisfied_count = int(sum(satisfied))
    predicate_count = int(len(satisfied))
    return {
        "goal_predicates": predicates,
        "goal_predicate_names": predicate_names,
        "goal_satisfied": satisfied,
        "goal_satisfied_count": satisfied_count,
        "goal_predicate_count": predicate_count,
        "goal_fraction": satisfied_count / max(predicate_count, 1),
        "goal_all_satisfied": bool(predicate_count > 0 and satisfied_count == predicate_count),
    }


def build_query_outcome_record(
    *,
    query_ids: dict[str, object],
    env_step_start: int,
    env_step_end: int,
    predicate_before: dict[str, object],
    predicate_after: dict[str, object],
    episode_done_after_query: bool,
    truncated_by_episode_end: bool,
) -> dict[str, object]:
    """Build one local outcome label for the policy query/action chunk."""
    before_values = list(predicate_before["goal_satisfied"])
    after_values = list(predicate_after["goal_satisfied"])
    if len(before_values) != len(after_values):
        raise RuntimeError(
            "Goal predicate count changed within an episode: "
            f"before={len(before_values)}, after={len(after_values)}."
        )

    completed = [idx for idx, (before, after) in enumerate(zip(before_values, after_values)) if not before and after]
    regressed = [idx for idx, (before, after) in enumerate(zip(before_values, after_values)) if before and not after]
    progress_delta = float(predicate_after["goal_fraction"]) - float(predicate_before["goal_fraction"])
    return {
        **query_ids,
        "env_step_start": int(env_step_start),
        "env_step_end": int(env_step_end),
        "low_level_steps_executed": int(max(0, env_step_end - env_step_start + 1)),
        "episode_done_after_query": bool(episode_done_after_query),
        "truncated_by_episode_end": bool(truncated_by_episode_end),
        "goal_predicates": predicate_before["goal_predicates"],
        "goal_predicate_names": predicate_before["goal_predicate_names"],
        "goal_satisfied_before": before_values,
        "goal_satisfied_after": after_values,
        "goal_satisfied_count_before": int(predicate_before["goal_satisfied_count"]),
        "goal_satisfied_count_after": int(predicate_after["goal_satisfied_count"]),
        "goal_predicate_count": int(predicate_before["goal_predicate_count"]),
        "goal_fraction_before": float(predicate_before["goal_fraction"]),
        "goal_fraction_after": float(predicate_after["goal_fraction"]),
        "goal_progress_delta": progress_delta,
        "completed_predicate_indices": completed,
        "regressed_predicate_indices": regressed,
        "chunk_completed_any_predicate": bool(completed),
        "chunk_regressed_any_predicate": bool(regressed),
        "chunk_made_predicate_progress": bool(progress_delta > 0.0 or completed),
        "chunk_no_predicate_progress": bool(progress_delta <= 0.0 and not completed),
        "chunk_completed_goal": bool(predicate_after["goal_all_satisfied"]),
    }


def _serialize_predicate(predicate: object) -> list[str]:
    if not isinstance(predicate, (list, tuple)):
        raise RuntimeError(f"Unexpected LIBERO goal predicate format: {predicate!r}")
    return [str(item) for item in predicate]


def _predicate_name(predicate: object) -> str:
    serialized = _serialize_predicate(predicate)
    if not serialized:
        return ""
    return f"{serialized[0]}({', '.join(serialized[1:])})"


def normalize_task_description(task_language: str) -> str:
    """Match the prompt form used by the released LIBERO checkpoints."""
    task_description = task_language.replace("black bowl", "bowl")
    task_description = re.sub(r" table \d+$", "", task_description)
    return task_description


def normalize_bddl_checkpoint_language(task_language: str) -> str:
    task_description = normalize_task_description(task_language)
    drawer_patterns = (
        r"open the (top|middle|bottom) drawer of the cabinet",
        r"open the cabinet[’']s (top|middle|bottom) drawer",
    )
    for pattern in drawer_patterns:
        task_description = re.sub(
            pattern,
            lambda match: f"open the {match.group(1)} layer of the drawer",
            task_description,
        )
    task_description = re.sub(
        r"put the (.+?) on the top of the drawer",
        lambda match: f"put the {match.group(1)} on top of the cabinet",
        task_description,
    )
    return task_description


def resolve_task_bddl_path(task) -> Path:
    """Return the BDDL file that defines the task's true language and scene."""
    task_bddl_path = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    if task_bddl_path.exists():
        return task_bddl_path

    if "_view_" in task.bddl_file and "_initstate_" in task.bddl_file:
        base_bddl = task.bddl_file.split("_view_")[0] + ".bddl"
        task_bddl_path = Path(get_libero_path("bddl_files")) / task.problem_folder / base_bddl
        if task_bddl_path.exists():
            return task_bddl_path

    raise FileNotFoundError(f"Unable to resolve BDDL file for task '{task.name}': {task_bddl_path}")


def task_description_for_policy(task, prompt_source: str) -> str:
    """Return the instruction text passed to the policy."""
    if prompt_source == "normalized_task_language":
        return normalize_task_description(task.language)
    if prompt_source == "task_language":
        return task.language
    if prompt_source == "bddl_language":
        problem_info = BDDLUtils.get_problem_info(str(resolve_task_bddl_path(task)))
        return problem_info["language_instruction"]
    if prompt_source == "checkpoint_bddl_language":
        problem_info = BDDLUtils.get_problem_info(str(resolve_task_bddl_path(task)))
        return normalize_bddl_checkpoint_language(problem_info["language_instruction"])
    raise ValueError(
        "prompt_source must be one of: normalized_task_language, task_language, "
        "bddl_language, checkpoint_bddl_language. "
        f"Received: {prompt_source}"
    )


def parse_task_ids(task_ids: str) -> list[int] | None:
    """Parse comma-separated task ids and ranges like '1,3,10-12'."""
    if not task_ids:
        return None

    parsed: list[int] = []
    for part in task_ids.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            parsed.extend(range(int(start), int(end) + 1))
        else:
            parsed.append(int(part))
    return parsed


def get_task_init_states_compatible(task_suite, task_id: int):
    """Load LIBERO init states across PyTorch versions.

    Newer PyTorch releases default ``torch.load`` to ``weights_only=True``.
    LIBERO stores NumPy arrays in trusted local ``.pruned_init`` files, so
    upstream LIBERO loaders that omit this flag can fail under PyTorch 2.6+.
    """
    try:
        return task_suite.get_task_init_states(task_id)
    except pickle.UnpicklingError:
        task = task_suite.get_task(task_id)
        init_states_path = Path(get_libero_path("init_states")) / task.problem_folder / task.init_states_file
        return torch.load(init_states_path, weights_only=False)


def set_seed_everywhere(seed: int) -> None:
    """Sets the random seed for Python, NumPy, and PyTorch functions."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ["PYTHONHASHSEED"] = str(seed)


def read_completed_episode_outcomes(path: Path) -> dict[int, dict[str, object]]:
    """Read completed episode outcomes keyed by global episode index."""
    if not path.exists():
        return {}
    outcomes: dict[int, dict[str, object]] = {}
    with path.open("r", encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            row = json.loads(line)
            global_episode_index = int(row["global_episode_index"])
            if global_episode_index in outcomes:
                raise RuntimeError(f"Duplicate episode outcome for global_episode_index={global_episode_index}.")
            outcomes[global_episode_index] = row
    return outcomes


def balanced_targets_reached(
    successes: int,
    failures: int,
    success_target: int,
    failure_target: int,
) -> bool:
    success_done = success_target <= 0 or successes >= success_target
    failure_done = failure_target <= 0 or failures >= failure_target
    return (success_target > 0 or failure_target > 0) and success_done and failure_done


def _ensure_finite_tensor(values: torch.Tensor, label: str) -> None:
    if not bool(torch.isfinite(values).all()):
        raise ValueError(f"{label} contains non-finite values.")


def _ensure_finite_array(values: np.ndarray, label: str) -> None:
    if not bool(np.isfinite(values).all()):
        raise ValueError(f"{label} contains non-finite values.")


def load_video2world2action_pipeline(
    experiment_name: str,
    video_model_path: str,
    action_model_path: str,
    dataset_statistics_path: pathlib.Path,
    dtype: torch.dtype = torch.float16,
    use_text_encoder: bool = False,
) -> Video2World2ActionPipeline:
    """Instantiate the video-to-world-to-action pipeline and load normalizer statistics."""
    config = make_config()
    config = override(config, ["--", f"experiment={experiment_name}"])

    # all libero task descriptions have been verified to be unproblematic
    config.model.config.video_pipe_config.guardrail_config.enabled = False
    config.model.config.video_pipe_config.precision = "float16"
    config.model.config.pipe_config.precision = "float16"
    config.model.config.pipe_config.net.atten_backend = "torch"

    video2world_pipe = Video2WorldPipeline.from_config(
        config=config.model.config.video_pipe_config,
        dit_path=video_model_path,
        use_text_encoder=use_text_encoder,
        device="cuda",
        torch_dtype=dtype,
        load_ema_to_reg=False,
    )

    world2action_pipe = World2ActionPipeline.from_config(
        config.model.config.pipe_config,
        dit_path=action_model_path,
        device="cuda",
        dtype=dtype,
    )

    data_config = instantiate(config.data_config)

    with dataset_statistics_path.open("rb") as stats_file:
        stats = json.load(stats_file)
    world2action_pipe.normalizer.build_from_stats(
        stats,
        normalization_types=extract_normalization_types(data_config.policy_io.policy_io),
        concat_groups=data_config.policy_io.concat_groups,
        device="cuda",
        dtype=dtype,
    )

    return Video2World2ActionPipeline(video2world_pipe, world2action_pipe).cuda()


class VAMInference:
    """Helper class that maintains temporal context and queries the VAM policy."""

    def __init__(
        self,
        experiment_name: str,
        video_model_path: str,
        action_model_path: str,
        dataset_statistics_path: pathlib.Path,
        img_horizon: int,
        lowdim_horizon: int,
        stop_video_denoising_step: int,
        num_execute_actions: int,
        num_sampling_steps: int,
        rollout_dir: pathlib.Path,
        use_text_encoder: bool = False,
        uq_num_action_candidates: int = 1,
        uq_action_candidate_batch_size: int = 1,
        uq_num_world_candidates: int = 1,
        uq_log_action_candidates: bool = True,
        uq_save_candidate_arrays: bool = False,
        v2w_uncertainty_head_path: pathlib.Path | None = None,
        v2w_uncertainty_calibration_path: pathlib.Path | None = None,
        v2w_uncertainty_variant: str = "a",
        v2w_uncertainty_save_variance_arrays: bool = False,
        uq_control_policy: str = "first_candidate",
        uq_min_execute_actions: int = 1,
        uq_adaptive_spike_z: float = 3.0,
        uq_adaptive_spike_warmup: int = 4,
        uq_adaptive_variance_floor: float = 0.0,
    ):
        self.model = load_video2world2action_pipeline(
            experiment_name,
            video_model_path,
            action_model_path,
            dataset_statistics_path,
            use_text_encoder=use_text_encoder,
        )
        self._image_horizon = img_horizon
        self._lowdim_horizon = lowdim_horizon
        self.stop_video_denoising_step = stop_video_denoising_step
        self.num_execute_actions = num_execute_actions
        self.num_sampling_steps = num_sampling_steps
        self.rollout_dir = rollout_dir
        self.uq_num_action_candidates = uq_num_action_candidates
        self.uq_action_candidate_batch_size = uq_action_candidate_batch_size
        self.uq_num_world_candidates = uq_num_world_candidates
        self.uq_log_action_candidates = uq_log_action_candidates
        self.uq_save_candidate_arrays = uq_save_candidate_arrays
        self._query_index = 0
        self._uq_log_path = rollout_dir / "action_candidate_uncertainty.jsonl"
        self._uq_array_dir = rollout_dir / "action_candidate_arrays"
        self._v2w_uncertainty_log_path = rollout_dir / "v2w_uncertainty_scores.jsonl"
        self._v2w_uncertainty_array_dir = rollout_dir / "v2w_uncertainty_variance_arrays"
        self._episode_outcome_log_path = rollout_dir / "episode_outcomes.jsonl"
        self._query_outcome_log_path = rollout_dir / "query_outcomes.jsonl"
        if self.uq_save_candidate_arrays:
            self._uq_array_dir.mkdir(parents=True, exist_ok=True)
        self.v2w_uncertainty_save_variance_arrays = v2w_uncertainty_save_variance_arrays
        if self.v2w_uncertainty_save_variance_arrays:
            self._v2w_uncertainty_array_dir.mkdir(parents=True, exist_ok=True)
        self.uq_control_policy = self._validate_uq_control_policy(uq_control_policy)
        self.uq_min_execute_actions = int(uq_min_execute_actions)
        self.uq_adaptive_spike_z = float(uq_adaptive_spike_z)
        self.uq_adaptive_spike_warmup = int(uq_adaptive_spike_warmup)
        self.uq_adaptive_variance_floor = float(uq_adaptive_variance_floor)
        if self.uq_min_execute_actions < 1:
            raise ValueError(f"uq_min_execute_actions must be >= 1, got {self.uq_min_execute_actions}.")
        if self.uq_min_execute_actions > self.num_execute_actions:
            raise ValueError(
                "uq_min_execute_actions must not exceed num_execute_actions "
                f"({self.uq_min_execute_actions} > {self.num_execute_actions})."
            )
        if self.uq_adaptive_spike_z < 0.0:
            raise ValueError(f"uq_adaptive_spike_z must be non-negative, got {self.uq_adaptive_spike_z}.")
        if self.uq_adaptive_spike_warmup < 1:
            raise ValueError(
                f"uq_adaptive_spike_warmup must be >= 1, got {self.uq_adaptive_spike_warmup}."
            )
        if self.uq_adaptive_variance_floor < 0.0:
            raise ValueError(
                f"uq_adaptive_variance_floor must be non-negative, got {self.uq_adaptive_variance_floor}."
            )
        self.v2w_uncertainty_model, self.v2w_calibration = self._load_v2w_uncertainty(
            v2w_uncertainty_head_path,
            v2w_uncertainty_calibration_path,
            v2w_uncertainty_variant,
        )
        if self._uses_world_context_control() and self.uq_num_world_candidates < 2:
            raise ValueError(
                f"uq_control_policy={self.uq_control_policy!r} requires uq_num_world_candidates >= 2."
            )
        if self.uq_control_policy == "world_lowest_v2w_variance" and self.v2w_uncertainty_model is None:
            raise ValueError("world_lowest_v2w_variance requires a loaded V2W uncertainty head.")
        if self.uq_num_action_candidates < 1:
            raise ValueError(f"uq_num_action_candidates must be >= 1, got {self.uq_num_action_candidates}.")
        if self.uq_action_candidate_batch_size < 1:
            raise ValueError(
                f"uq_action_candidate_batch_size must be >= 1, got {self.uq_action_candidate_batch_size}."
            )
        if self.uq_num_world_candidates < 1:
            raise ValueError(f"uq_num_world_candidates must be >= 1, got {self.uq_num_world_candidates}.")
        if self.num_sampling_steps < 1:
            raise ValueError(f"num_sampling_steps must be >= 1, got {self.num_sampling_steps}.")
        if self.stop_video_denoising_step > self.num_sampling_steps:
            raise ValueError(
                "stop_video_denoising_step must not exceed num_sampling_steps "
                f"({self.stop_video_denoising_step} > {self.num_sampling_steps})."
            )
        self.reset(task_description="")

    def _uses_world_context_control(self) -> bool:
        return self.uq_control_policy in {"world_action_medoid", "world_lowest_v2w_variance"}

    @staticmethod
    def _validate_uq_control_policy(policy: str) -> str:
        normalized = policy.lower().replace("-", "_")
        valid = {
            "first_candidate",
            "action_cycle",
            "action_medoid",
            "action_antimedoid",
            "adaptive_horizon",
            "medoid_adaptive_horizon",
            "world_action_medoid",
            "world_lowest_v2w_variance",
        }
        if normalized not in valid:
            raise ValueError(f"uq_control_policy must be one of {sorted(valid)}, got {policy!r}.")
        return normalized

    @staticmethod
    def _load_v2w_uncertainty(
        head_path: pathlib.Path | None,
        calibration_path: pathlib.Path | None,
        variant: str,
    ) -> tuple[V2WUncertaintyModel | None, V2WCalibration | None]:
        """Load the optional learned V2W uncertainty head used for runtime scoring."""
        if head_path is None and calibration_path is None:
            return None, None
        if head_path is None or calibration_path is None:
            raise ValueError("Both v2w_uncertainty_head_path and v2w_uncertainty_calibration_path are required.")

        variant = variant.lower()
        if variant not in {"a", "b"}:
            raise ValueError(f"v2w_uncertainty_variant must be 'a' or 'b', got {variant!r}.")

        use_variant_b = variant == "b"
        model = V2WUncertaintyModel(use_variant_b=use_variant_b).cuda().eval()
        model.load_state_dict(torch.load(head_path, map_location="cuda"))

        calibration = V2WCalibration(num_bins=10, use_variant_b=use_variant_b)
        calibration.load(str(calibration_path))
        if calibration.use_variant_b != use_variant_b:
            raise ValueError(
                f"Calibration variant mismatch: calibration.use_variant_b={calibration.use_variant_b}, "
                f"requested use_variant_b={use_variant_b}."
            )

        summary = calibration.summary()
        if not summary["finite"] or not summary["positive"]:
            raise ValueError(f"Invalid V2W calibration baseline: {json.dumps(summary, sort_keys=True)}")
        print(f"Loaded V2W uncertainty head: {head_path}")
        print(f"Loaded V2W calibration: {calibration_path}")
        print(f"V2W calibration summary: {json.dumps(summary, sort_keys=True)}")
        return model, calibration

    def reset(self, task_description: str) -> None:
        """Reset internal state for a new task/episode."""
        self.task_description = task_description
        self._image_history: deque[np.ndarray] = deque(maxlen=(self._image_horizon - 1) * 4 + 1)
        self._lowdim_history: deque[np.ndarray] = deque(maxlen=self._lowdim_horizon)
        self.action_buffer: np.ndarray | None = None
        self.action_buffer_idx = 0
        self._execute_horizon = 0
        self._previous_action_chunk: np.ndarray | None = None
        self._previous_execute_horizon = 0
        self._pending_execute_horizon = self.num_execute_actions
        self._last_control_decision: dict[str, object] = {}
        self._episode_task_id: int | None = None
        self._episode_index: int | None = None
        self._global_episode_index: int | None = None
        self._episode_query_count = 0

    def set_episode_context(self, task_id: int, episode_idx: int, global_episode_idx: int) -> None:
        """Attach rollout identifiers to uncertainty logs for later analysis."""
        self._episode_task_id = task_id
        self._episode_index = episode_idx
        self._global_episode_index = global_episode_idx

    def will_start_query(self, task_description: str) -> bool:
        """Return whether the next step will issue a fresh policy query."""
        return task_description != self.task_description or self.action_buffer is None

    def current_query_ids(self) -> dict[str, object]:
        """Return identifiers for the most recent policy query."""
        return {
            "query_index": int(self._query_index),
            "episode_query_index": int(self._episode_query_count),
            "task_id": self._episode_task_id,
            "episode_index": self._episode_index,
            "global_episode_index": self._global_episode_index,
            "task_description": self.task_description,
            "num_execute_actions": int(self.num_execute_actions),
        }

    def log_query_outcome(self, record: dict[str, object]) -> None:
        """Append local predicate-progress labels for one policy query/action chunk."""
        with self._query_outcome_log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def step(
        self,
        image: np.ndarray,
        task_description: str,
        obs: dict,
    ) -> np.ndarray:
        """Return the next action for the given observation."""
        if image.dtype != np.uint8:
            raise ValueError(f"Expected image dtype uint8, received {image.dtype}.")

        if task_description != self.task_description:
            self.reset(task_description)

        processed_image = self._process_image(image)
        self._add_image_to_history(processed_image)

        state_vec = self._state_from_observation(obs)
        self._add_lowdim_to_history(state_vec)

        if self.action_buffer is None:
            self._query_policy(task_description)

        current_action = self.action_buffer[self.action_buffer_idx]
        self.action_buffer_idx += 1
        if self.action_buffer_idx >= self._execute_horizon:
            self._previous_action_chunk = self.action_buffer.copy()
            self._previous_execute_horizon = self._execute_horizon
            self.action_buffer = None

        return self._convert_action(current_action)

    def _query_policy(self, task_description: str) -> None:
        """Query the model and cache the planned action sequence."""
        images, lowdims = self._snapshot_history()
        self._query_index += 1
        self._episode_query_count += 1
        self._pending_execute_horizon = self.num_execute_actions
        self._last_control_decision = {}
        self.action_buffer = self._predict_actions(task_description, images, lowdims)
        self._execute_horizon = self._bounded_execute_horizon(
            self._pending_execute_horizon,
            available_actions=self.action_buffer.shape[0],
        )
        self.action_buffer_idx = 0

    def _bounded_execute_horizon(self, requested_horizon: int, available_actions: int) -> int:
        return int(max(1, min(int(requested_horizon), self.num_execute_actions, int(available_actions))))

    def _snapshot_history(self) -> tuple[np.ndarray, np.ndarray]:
        """Copy the current temporal context for inference."""
        images = np.concatenate(list(self._image_history)[::4], axis=1)  # downsample from 20 fps to 5
        lowdims = np.stack(list(self._lowdim_history), axis=0)
        return images.copy(), lowdims.copy()

    def _predict_actions(self, task_description: str, images: np.ndarray, lowdims: np.ndarray) -> np.ndarray:
        """Run the model once and return an unnormalized action chunk on CPU."""
        input_vid = torch.from_numpy(images[None]).pin_memory().cuda(non_blocking=True).to(dtype=torch.float16)
        state_tensor = torch.from_numpy(lowdims[None]).pin_memory().cuda(non_blocking=True).to(dtype=torch.float16)

        # Look up precomputed embedding if available.
        prompt_embedding = None
        filename = prompt_embedding_filename(task_description)
        embedding_path = Path(CHECKPOINTS_DIR) / "precomputed_embeddings" / filename
        if embedding_path.exists():
            prompt_embedding = torch.load(embedding_path, map_location="cpu").pin_memory().cuda(non_blocking=True).to(dtype=torch.float16)
        else:
            if self.model.video2world_pipeline.text_encoder is None:
                raise RuntimeError(
                    f"Precomputed embedding not found for prompt: '{task_description}' (filename: '{filename}') "
                    f"at '{embedding_path}', and text_encoder is disabled (use_text_encoder=False). "
                    f"Please run the precomputation script first!"
                )

        if self.uq_num_action_candidates == 1:
            if self.v2w_uncertainty_model is not None:
                return self._predict_single_action_with_v2w_uncertainty(
                    input_vid=input_vid,
                    state_tensor=state_tensor,
                    task_description=task_description,
                    prompt_embedding=prompt_embedding,
                )

            with torch.inference_mode():
                pred_actions = self.model(
                    input_vid=input_vid,
                    state_B_HO_O=state_tensor,
                    prompt=task_description,
                    prompt_embedding=prompt_embedding,
                    num_sampling_step=self.num_sampling_steps,
                    stop_after_step=self.stop_video_denoising_step,
                    use_cuda_graphs=True,
                )

            return pred_actions[0].float().cpu().numpy()

        seeds = list(range(self.uq_num_action_candidates))
        if self.v2w_uncertainty_model is not None:
            return self._predict_action_candidates_with_v2w_uncertainty(
                input_vid=input_vid,
                state_tensor=state_tensor,
                task_description=task_description,
                prompt_embedding=prompt_embedding,
                seeds=seeds,
            )

        torch.cuda.reset_peak_memory_stats()
        started_at = time.perf_counter()
        pred_actions, actual_action_batch_size, oom_fallback = self._predict_action_candidates(
            input_vid=input_vid,
            state_tensor=state_tensor,
            task_description=task_description,
            prompt_embedding=prompt_embedding,
            seeds=seeds,
        )
        torch.cuda.synchronize()
        query_seconds = time.perf_counter() - started_at

        candidates = pred_actions.float().cpu().numpy()
        control_decision = self._decide_uq_control(candidates)
        selected_candidate_index = int(control_decision["selected_candidate_index"])
        self._pending_execute_horizon = int(control_decision["selected_execute_horizon"])
        self._last_control_decision = control_decision
        world_context_uncertainty = self._predict_world_context_uncertainty(
            input_vid=input_vid,
            state_tensor=state_tensor,
            task_description=task_description,
            prompt_embedding=prompt_embedding,
            executed_candidate=candidates[selected_candidate_index],
        )
        if self.uq_log_action_candidates:
            self._log_action_candidate_uncertainty(
                task_description,
                seeds,
                candidates,
                query_seconds,
                actual_action_batch_size,
                oom_fallback,
                self._compute_receding_overlap_consistency(candidates),
                world_context_uncertainty,
                None,
                control_decision,
            )

        return candidates[selected_candidate_index]

    def _predict_action_candidates_with_v2w_uncertainty(
        self,
        input_vid: torch.Tensor,
        state_tensor: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
        seeds: list[int],
    ) -> np.ndarray:
        if self.v2w_uncertainty_model is None or self.v2w_calibration is None:
            raise RuntimeError("V2W uncertainty head was not loaded.")

        torch.cuda.reset_peak_memory_stats()
        started_at = time.perf_counter()
        with torch.no_grad():
            crossattn_emb, video_sigma, uncertainty_metrics, variance_grid = self._generate_scored_action_context(
                input_vid=input_vid,
                task_description=task_description,
                prompt_embedding=prompt_embedding,
                seed=int(seeds[0]),
            )
            pred_actions, actual_action_batch_size, oom_fallback = self._decode_action_candidates_from_context(
                state_tensor=state_tensor,
                crossattn_emb=crossattn_emb,
                video_sigma=video_sigma,
                seeds=seeds,
            )
        torch.cuda.synchronize()
        query_seconds = time.perf_counter() - started_at

        self._log_v2w_uncertainty(
            task_description,
            query_seconds,
            uncertainty_metrics,
            variance_grid,
            context_seed=int(seeds[0]),
            context_role="executed_shared",
        )

        candidates = pred_actions.float().cpu().numpy()
        control_decision = self._decide_uq_control(candidates)
        selected_candidate_index = int(control_decision["selected_candidate_index"])
        world_context_uncertainty, world_context_actions = self._predict_scored_world_context_uncertainty(
            input_vid=input_vid,
            state_tensor=state_tensor,
            task_description=task_description,
            prompt_embedding=prompt_embedding,
            executed_candidate=candidates[selected_candidate_index],
            executed_context=(crossattn_emb, video_sigma),
            executed_action=candidates[selected_candidate_index],
            executed_uncertainty_metrics=uncertainty_metrics,
        )
        selected_action = candidates[selected_candidate_index]
        if self._uses_world_context_control():
            if world_context_actions is None or not world_context_uncertainty.get("world_context_uncertainty_available"):
                raise RuntimeError(
                    f"uq_control_policy={self.uq_control_policy!r} requires available world context actions."
                )
            selected_action, control_decision = self._decide_world_context_control(
                world_context_actions,
                world_context_uncertainty,
                fallback_decision=control_decision,
            )
        self._pending_execute_horizon = int(control_decision["selected_execute_horizon"])
        self._last_control_decision = control_decision
        candidate_array_path = self._save_action_candidate_arrays(
            candidates=candidates,
            world_context_actions=world_context_actions,
            selected_candidate_index=selected_candidate_index,
            selected_world_context_index=control_decision.get("selected_world_context_index"),
        )
        if self.uq_log_action_candidates:
            self._log_action_candidate_uncertainty(
                task_description,
                seeds,
                candidates,
                query_seconds,
                actual_action_batch_size,
                oom_fallback,
                self._compute_receding_overlap_consistency(candidates),
                world_context_uncertainty,
                candidate_array_path,
                control_decision,
            )

        return selected_action

    def _predict_single_action_with_v2w_uncertainty(
        self,
        input_vid: torch.Tensor,
        state_tensor: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
    ) -> np.ndarray:
        """Run one V2W context, score it with the learned head, then decode actions."""
        if self.v2w_uncertainty_model is None or self.v2w_calibration is None:
            raise RuntimeError("V2W uncertainty head was not loaded.")

        torch.cuda.reset_peak_memory_stats()
        started_at = time.perf_counter()
        with torch.no_grad():
            crossattn_emb, video_sigma, uncertainty_metrics, variance_grid = self._generate_scored_action_context(
                input_vid=input_vid,
                task_description=task_description,
                prompt_embedding=prompt_embedding,
            )
            pred_actions = self.model.world2action_pipeline(
                state_B_HO_O=state_tensor,
                crossattn_emb=crossattn_emb,
                context_timesteps_B_1=video_sigma,
                seed=0,
                use_cuda_graphs=False,
            )
        torch.cuda.synchronize()
        self._log_v2w_uncertainty(
            task_description,
            time.perf_counter() - started_at,
            uncertainty_metrics,
            variance_grid,
        )
        return pred_actions[0].float().cpu().numpy()

    def _generate_scored_action_context(
        self,
        input_vid: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
        seed: int = 0,
    ) -> tuple[torch.Tensor, torch.Tensor, dict[str, object], np.ndarray | None]:
        """Return W2A context and learned V2W uncertainty metrics for that exact context."""
        self.model._check_prompt(task_description)
        input_frames = input_vid.shape[2]
        if input_frames not in {1, 5}:
            raise ValueError(f"Expected 1 or 5 input frames, got {input_frames}.")

        num_latent_conditional_frames = 1 if input_frames == 1 else 2
        hidden_states, sigma = self.model.video2world_pipeline.generate_video(
            vid_input=input_vid,
            num_latent_conditional_frames=num_latent_conditional_frames,
            prompt=task_description,
            prompt_embedding=prompt_embedding,
            negative_prompt="",
            guidance=0.0,
            num_sampling_step=self.num_sampling_steps,
            seed=seed,
            use_cuda_graphs=True,
            return_context_at_step=self.stop_video_denoising_step,
            hidden_state_layer_idx=self.model.world2action_pipeline.config.xattn_layer_idx,
        )
        if hidden_states is None:
            raise RuntimeError("V2W did not return hidden states for uncertainty scoring.")

        if sigma.ndim == 0:
            sigma_B_1 = sigma.repeat(hidden_states.shape[0]).unsqueeze(1)
        elif sigma.ndim == 1:
            sigma_B_1 = sigma.unsqueeze(1)
        else:
            sigma_B_1 = sigma
        condition_mask = self._condition_mask_for_hidden_states(hidden_states, num_latent_conditional_frames)
        uncertainty_metrics, variance_grid = self._score_v2w_uncertainty(hidden_states, sigma_B_1, condition_mask)

        hidden_state_shape = hidden_states.shape
        crossattn_emb = hidden_states.reshape(hidden_state_shape[0], -1, hidden_state_shape[-1])
        return crossattn_emb, sigma_B_1, uncertainty_metrics, variance_grid

    @staticmethod
    def _condition_mask_for_hidden_states(
        hidden_states: torch.Tensor,
        num_latent_conditional_frames: int,
    ) -> torch.Tensor:
        batch_size, time_tokens, height_tokens, width_tokens, _ = hidden_states.shape
        condition_mask = torch.zeros(
            (batch_size, 1, time_tokens, height_tokens, width_tokens),
            device=hidden_states.device,
            dtype=torch.float32,
        )
        condition_mask[:, :, :num_latent_conditional_frames] = 1.0
        return condition_mask

    def _score_v2w_uncertainty(
        self,
        hidden_states: torch.Tensor,
        sigma_B_1: torch.Tensor,
        condition_mask: torch.Tensor,
    ) -> tuple[dict[str, object], np.ndarray | None]:
        if self.v2w_uncertainty_model is None or self.v2w_calibration is None:
            raise RuntimeError("V2W uncertainty head was not loaded.")

        out = self.v2w_uncertainty_model(hidden_states.detach(), sigma_B_1, condition_mask)
        delta_log_var = self._resize_delta_log_variance(out["delta_log_var"], hidden_states.shape[1:4])
        log_variance = clamped_log_variance(self.v2w_calibration.get_baseline(sigma_B_1), delta_log_var)
        variance = torch.exp(log_variance.float())
        token_variance = variance.mean(dim=1) if variance.ndim == 5 else variance
        future_mask = (1.0 - condition_mask.squeeze(1)).bool()
        future_values = token_variance[future_mask]

        if future_values.numel() == 0:
            raise RuntimeError("No future V2W tokens available for uncertainty scoring.")

        quantiles = torch.quantile(
            future_values.float(),
            torch.tensor([0.5, 0.9, 0.95, 0.99], device=future_values.device),
        )
        top_count = min(64, future_values.numel())
        top_values = torch.topk(future_values.float(), k=top_count).values
        per_time_mean = self._future_time_stat(token_variance, future_mask, "mean")
        per_time_max = self._future_time_stat(token_variance, future_mask, "max")
        variance_grid = token_variance.detach().float().cpu().numpy() if self.v2w_uncertainty_save_variance_arrays else None
        return {
            "v2w_uncertainty_available": True,
            "v2w_context_seed": None,
            "v2w_context_role": None,
            "v2w_sigma": float(sigma_B_1.detach().flatten()[0].cpu()),
            "v2w_num_future_tokens": int(future_values.numel()),
            "v2w_variance_mean": float(future_values.mean().detach().cpu()),
            "v2w_variance_std": float(future_values.std(unbiased=False).detach().cpu()),
            "v2w_variance_p50": float(quantiles[0].detach().cpu()),
            "v2w_variance_p90": float(quantiles[1].detach().cpu()),
            "v2w_variance_p95": float(quantiles[2].detach().cpu()),
            "v2w_variance_p99": float(quantiles[3].detach().cpu()),
            "v2w_variance_max": float(future_values.max().detach().cpu()),
            "v2w_variance_top64_mean": float(top_values.mean().detach().cpu()),
            "v2w_variance_top64_min": float(top_values.min().detach().cpu()),
            "v2w_per_time_variance_mean": per_time_mean,
            "v2w_per_time_variance_max": per_time_max,
            "v2w_delta_log_var_mean": float(delta_log_var.float().mean().detach().cpu()),
            "v2w_delta_log_var_std": float(delta_log_var.float().std(unbiased=False).detach().cpu()),
            "v2w_aux_mu_lat": float(out["mu_lat"].detach().flatten()[0].cpu()),
            "v2w_aux_log_var_lat": float(out["log_var_lat"].detach().flatten()[0].cpu()),
            "v2w_aux_mu_act": float(out["mu_act"].detach().flatten()[0].cpu()),
            "v2w_aux_log_var_act": float(out["log_var_act"].detach().flatten()[0].cpu()),
        }, variance_grid

    @staticmethod
    def _future_time_stat(token_variance: torch.Tensor, future_mask: torch.Tensor, stat: str) -> list[float | None]:
        values = token_variance.float()
        result: list[float | None] = []
        for time_idx in range(values.shape[1]):
            time_values = values[:, time_idx][future_mask[:, time_idx]]
            if time_values.numel() == 0:
                result.append(None)
            elif stat == "mean":
                result.append(float(time_values.mean().detach().cpu()))
            elif stat == "max":
                result.append(float(time_values.max().detach().cpu()))
            else:
                raise ValueError(f"Unsupported time statistic: {stat}")
        return result

    @staticmethod
    def _resize_delta_log_variance(
        delta_log_variance: torch.Tensor,
        target_shape: tuple[int, int, int],
    ) -> torch.Tensor:
        if tuple(delta_log_variance.shape[-3:]) == target_shape:
            return delta_log_variance
        if delta_log_variance.ndim == 4:
            resized = F.interpolate(
                delta_log_variance.unsqueeze(1).float(),
                size=target_shape,
                mode="trilinear",
                align_corners=False,
            )
            return resized.squeeze(1).type_as(delta_log_variance)
        if delta_log_variance.ndim == 5:
            return F.interpolate(
                delta_log_variance.float(),
                size=target_shape,
                mode="trilinear",
                align_corners=False,
            ).type_as(delta_log_variance)
        raise ValueError(f"Unsupported delta_log_variance shape: {tuple(delta_log_variance.shape)}")

    def _log_v2w_uncertainty(
        self,
        task_description: str,
        query_seconds: float,
        uncertainty_metrics: dict[str, object],
        variance_grid: np.ndarray | None,
        context_seed: int = 0,
        context_role: str = "executed_shared",
    ) -> None:
        variance_array_path = None
        if variance_grid is not None:
            array_name = (
                f"episode{self._global_episode_index:06d}_"
                f"query{self._episode_query_count:04d}_"
                f"seed{context_seed:03d}_{context_role}_variance.npz"
            )
            variance_array_path = self._v2w_uncertainty_array_dir / array_name
            np.savez_compressed(variance_array_path, token_variance=variance_grid.astype(np.float16))

        record = {
            "query_index": self._query_index,
            "episode_query_index": self._episode_query_count,
            "task_id": self._episode_task_id,
            "episode_index": self._episode_index,
            "global_episode_index": self._global_episode_index,
            "task_description": task_description,
            "num_sampling_steps": int(self.num_sampling_steps),
            "stop_video_denoising_step": int(self.stop_video_denoising_step),
            "num_execute_actions": int(self.num_execute_actions),
            "query_seconds": query_seconds,
            "cuda_peak_memory_gb": torch.cuda.max_memory_allocated() / (1024**3),
            "v2w_variance_array_path": str(variance_array_path) if variance_array_path is not None else None,
            **uncertainty_metrics,
            "v2w_context_seed": int(context_seed),
            "v2w_context_role": context_role,
        }
        with self._v2w_uncertainty_log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def _decode_action_candidates_from_context(
        self,
        state_tensor: torch.Tensor,
        crossattn_emb: torch.Tensor,
        video_sigma: torch.Tensor,
        seeds: list[int],
    ) -> tuple[torch.Tensor, int, bool]:
        action_batch_size = min(self.uq_action_candidate_batch_size, len(seeds))
        try:
            return (
                self._decode_action_candidate_batches(
                    state_tensor,
                    crossattn_emb,
                    video_sigma,
                    seeds,
                    action_batch_size,
                ),
                action_batch_size,
                False,
            )
        except torch.cuda.OutOfMemoryError:
            if action_batch_size == 1:
                raise
            torch.cuda.empty_cache()
            return (
                self._decode_action_candidate_batches(
                    state_tensor,
                    crossattn_emb,
                    video_sigma,
                    seeds,
                    1,
                ),
                1,
                True,
            )

    def _decode_action_candidate_batches(
        self,
        state_tensor: torch.Tensor,
        crossattn_emb: torch.Tensor,
        video_sigma: torch.Tensor,
        seeds: list[int],
        action_batch_size: int,
    ) -> torch.Tensor:
        chunks = []
        for start in range(0, len(seeds), action_batch_size):
            seed_batch = [int(seed) for seed in seeds[start : start + action_batch_size]]
            batch_size = len(seed_batch)
            chunks.append(
                self.model.world2action_pipeline(
                    state_B_HO_O=state_tensor.expand(batch_size, -1, -1).contiguous(),
                    crossattn_emb=crossattn_emb.expand(batch_size, -1, -1).contiguous(),
                    context_timesteps_B_1=video_sigma.expand(batch_size, -1).contiguous(),
                    seed=seed_batch,
                    use_cuda_graphs=False,
                )
            )
        return torch.cat(chunks, dim=0)

    def _predict_scored_world_context_uncertainty(
        self,
        input_vid: torch.Tensor,
        state_tensor: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
        executed_candidate: np.ndarray,
        executed_context: tuple[torch.Tensor, torch.Tensor],
        executed_action: np.ndarray,
        executed_uncertainty_metrics: dict[str, object],
    ) -> tuple[dict[str, object], np.ndarray | None]:
        if self.uq_num_world_candidates == 1:
            return {
                "world_context_uncertainty_available": False,
                "world_context_unavailable_reason": "disabled",
                "world_context_num_candidates": 1,
                "world_context_seconds": 0.0,
            }, None

        started_at = time.perf_counter()
        seeds = list(range(self.uq_num_world_candidates))
        context_snapshots = [executed_context[0].detach().float().cpu()]
        action_chunks = [executed_action]
        v2w_variance_means = [float(executed_uncertainty_metrics["v2w_variance_mean"])]
        v2w_variance_maxes = [float(executed_uncertainty_metrics["v2w_variance_max"])]
        try:
            for seed in seeds[1:]:
                crossattn_emb, video_sigma, uncertainty_metrics, variance_grid = self._generate_scored_action_context(
                    input_vid=input_vid,
                    task_description=task_description,
                    prompt_embedding=prompt_embedding,
                    seed=int(seed),
                )
                self._log_v2w_uncertainty(
                    task_description,
                    time.perf_counter() - started_at,
                    uncertainty_metrics,
                    variance_grid,
                    context_seed=int(seed),
                    context_role="world_candidate",
                )
                action = self.model.world2action_pipeline(
                    state_B_HO_O=state_tensor,
                    crossattn_emb=crossattn_emb,
                    context_timesteps_B_1=video_sigma,
                    seed=0,
                    use_cuda_graphs=False,
                )
                action_chunks.append(action[0].float().cpu().numpy())
                context_snapshots.append(crossattn_emb.detach().float().cpu())
                v2w_variance_means.append(float(uncertainty_metrics["v2w_variance_mean"]))
                v2w_variance_maxes.append(float(uncertainty_metrics["v2w_variance_max"]))
            torch.cuda.synchronize()
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            return {
                "world_context_uncertainty_available": False,
                "world_context_unavailable_reason": "cuda_oom",
                "world_context_num_candidates": int(self.uq_num_world_candidates),
                "world_context_seconds": time.perf_counter() - started_at,
            }, None

        actions = np.stack(action_chunks, axis=0)
        try:
            _ensure_finite_array(actions, "world-context induced actions")
            context_metrics = self.model._summarize_context_disagreement(context_snapshots)
        except ValueError as exc:
            return self._unavailable_world_context_metrics("non_finite_world_context", started_at, str(exc)), None
        pairwise_mse = self._mean_pairwise_action_mse(actions)
        if not np.isfinite(pairwise_mse):
            return self._unavailable_world_context_metrics(
                "non_finite_world_context_action_metric",
                started_at,
                "world-context induced action pairwise MSE was not finite",
            ), None
        return {
            "world_context_uncertainty_available": True,
            "world_context_unavailable_reason": None,
            "world_context_num_candidates": int(actions.shape[0]),
            "world_context_seeds": seeds,
            "world_context_seconds": time.perf_counter() - started_at,
            "world_context_v2w_variance_mean": v2w_variance_means,
            "world_context_v2w_variance_max": v2w_variance_maxes,
            **context_metrics,
            "world_context_induced_action_pairwise_mse_mean": pairwise_mse,
            "world_context_induced_action_vs_executed_mse_mean": float(
                np.mean((actions - executed_candidate[None]) ** 2)
            ),
            "world_context_induced_action_vs_executed_mse_max": float(
                np.max(np.mean((actions - executed_candidate[None]) ** 2, axis=(1, 2)))
            ),
            "trajectory_available": False,
            "trajectory_unavailable_reason": "scored_world_context_path",
        }, actions

    @staticmethod
    def _mean_pairwise_action_mse(actions: np.ndarray) -> float:
        pairwise_mse = 0.0
        num_pairs = 0
        for i in range(actions.shape[0]):
            for j in range(i + 1, actions.shape[0]):
                pairwise_mse += float(np.mean((actions[i] - actions[j]) ** 2))
                num_pairs += 1
        return pairwise_mse / num_pairs if num_pairs else 0.0

    def _save_action_candidate_arrays(
        self,
        candidates: np.ndarray,
        world_context_actions: np.ndarray | None,
        selected_candidate_index: int,
        selected_world_context_index: object | None = None,
    ) -> str | None:
        if not self.uq_save_candidate_arrays:
            return None
        array_name = f"episode{self._global_episode_index:06d}_query{self._episode_query_count:04d}_actions.npz"
        array_path = self._uq_array_dir / array_name
        payload = {
            "action_candidates": candidates.astype(np.float16),
            "action_variance": np.var(candidates, axis=0).astype(np.float16),
            "selected_candidate_index": np.asarray(selected_candidate_index, dtype=np.int16),
            "selected_world_context_index": np.asarray(
                -1 if selected_world_context_index is None else int(selected_world_context_index),
                dtype=np.int16,
            ),
        }
        if world_context_actions is not None:
            payload["world_context_actions"] = world_context_actions.astype(np.float16)
        np.savez_compressed(array_path, **payload)
        return str(array_path)

    def _predict_action_candidates(
        self,
        input_vid: torch.Tensor,
        state_tensor: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
        seeds: list[int],
    ) -> tuple[torch.Tensor, int, bool]:
        """Run one V2W pass and K W2A candidate passes with OOM fallback."""
        action_batch_size = min(self.uq_action_candidate_batch_size, len(seeds))
        actual_action_batch_size = action_batch_size
        oom_fallback = False
        try:
            pred_actions = self.model.action_candidates(
                input_vid=input_vid,
                state_B_HO_O=state_tensor,
                prompt=task_description,
                prompt_embedding=prompt_embedding,
                num_sampling_step=self.num_sampling_steps,
                stop_after_step=self.stop_video_denoising_step,
                seeds=seeds,
                action_batch_size=action_batch_size,
                use_cuda_graphs=True,
                use_cuda_graphs_for_action=False,
            )
        except torch.cuda.OutOfMemoryError:
            if action_batch_size == 1:
                raise
            torch.cuda.empty_cache()
            actual_action_batch_size = 1
            oom_fallback = True
            pred_actions = self.model.action_candidates(
                input_vid=input_vid,
                state_B_HO_O=state_tensor,
                prompt=task_description,
                prompt_embedding=prompt_embedding,
                num_sampling_step=self.num_sampling_steps,
                stop_after_step=self.stop_video_denoising_step,
                seeds=seeds,
                action_batch_size=1,
                use_cuda_graphs=True,
                use_cuda_graphs_for_action=False,
            )
        return pred_actions, actual_action_batch_size, oom_fallback

    def _predict_world_context_uncertainty(
        self,
        input_vid: torch.Tensor,
        state_tensor: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
        executed_candidate: np.ndarray,
    ) -> dict[str, object]:
        """Run optional V2W multiseed diagnostics without changing the executed action."""
        if self.uq_num_world_candidates == 1:
            return {
                "world_context_uncertainty_available": False,
                "world_context_unavailable_reason": "disabled",
                "world_context_num_candidates": 1,
                "world_context_seconds": 0.0,
            }

        seeds = list(range(self.uq_num_world_candidates))
        started_at = time.perf_counter()
        try:
            pred_actions, context_metrics = self.model.world_context_action_candidates(
                input_vid=input_vid,
                state_B_HO_O=state_tensor,
                prompt=task_description,
                prompt_embedding=prompt_embedding,
                num_sampling_step=self.num_sampling_steps,
                stop_after_step=self.stop_video_denoising_step,
                seeds=seeds,
                action_seed=0,
                use_cuda_graphs=True,
                use_cuda_graphs_for_action=False,
            )
            torch.cuda.synchronize()
            world_context_seconds = time.perf_counter() - started_at
            _ensure_finite_tensor(pred_actions, "world-context induced actions")
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            return {
                "world_context_uncertainty_available": False,
                "world_context_unavailable_reason": "cuda_oom",
                "world_context_num_candidates": int(self.uq_num_world_candidates),
                "world_context_seconds": time.perf_counter() - started_at,
            }
        except ValueError as exc:
            return self._unavailable_world_context_metrics("non_finite_world_context", started_at, str(exc))

        actions = pred_actions.float().cpu().numpy()
        pairwise_mse = 0.0
        num_pairs = 0
        for i in range(actions.shape[0]):
            for j in range(i + 1, actions.shape[0]):
                pairwise_mse += float(np.mean((actions[i] - actions[j]) ** 2))
                num_pairs += 1
        if num_pairs:
            pairwise_mse /= num_pairs
        if not np.isfinite(pairwise_mse):
            return self._unavailable_world_context_metrics(
                "non_finite_world_context_action_metric",
                started_at,
                "world-context induced action pairwise MSE was not finite",
            )

        traj_metrics = {}
        if self.stop_video_denoising_step > 0:
            try:
                traj_metrics = self.model.world_context_trajectory_metrics(
                    input_vid=input_vid,
                    prompt=task_description,
                    prompt_embedding=prompt_embedding,
                    num_sampling_step=self.num_sampling_steps,
                    stop_after_step=self.stop_video_denoising_step,
                    seeds=seeds,
                    use_cuda_graphs=True,
                )
            except Exception as e:
                traj_metrics = {
                    "trajectory_available": False,
                    "trajectory_error": str(e)
                }

        return {
            "world_context_uncertainty_available": True,
            "world_context_unavailable_reason": None,
            "world_context_num_candidates": int(actions.shape[0]),
            "world_context_seeds": seeds,
            "world_context_seconds": world_context_seconds,
            **context_metrics,
            "world_context_induced_action_pairwise_mse_mean": pairwise_mse,
            "world_context_induced_action_vs_executed_mse_mean": float(
                np.mean((actions - executed_candidate[None]) ** 2)
            ),
            "world_context_induced_action_vs_executed_mse_max": float(
                np.max(np.mean((actions - executed_candidate[None]) ** 2, axis=(1, 2)))
            ),
            **traj_metrics,
        }

    def _unavailable_world_context_metrics(
        self,
        reason: str,
        started_at: float,
        detail: str,
    ) -> dict[str, object]:
        return {
            "world_context_uncertainty_available": False,
            "world_context_unavailable_reason": reason,
            "world_context_error": detail,
            "world_context_num_candidates": int(self.uq_num_world_candidates),
            "world_context_seconds": time.perf_counter() - started_at,
            "trajectory_available": False,
            "trajectory_unavailable_reason": reason,
        }

    def _log_action_candidate_uncertainty(
        self,
        task_description: str,
        seeds: list[int],
        candidates: np.ndarray,
        query_seconds: float,
        actual_action_batch_size: int,
        oom_fallback: bool,
        overlap_consistency: dict[str, object],
        world_context_uncertainty: dict[str, object],
        candidate_array_path: str | None,
        control_decision: dict[str, object],
    ) -> None:
        """Append compact multiseed action uncertainty metrics for this policy query."""
        variance = np.var(candidates, axis=0)
        flat_variance = variance.reshape(-1)
        tail_count = max(1, int(np.ceil(0.10 * flat_variance.size)))
        tail_variance = float(np.mean(np.partition(flat_variance, -tail_count)[-tail_count:]))

        pairwise_mse = 0.0
        num_pairs = 0
        for i in range(candidates.shape[0]):
            for j in range(i + 1, candidates.shape[0]):
                pairwise_mse += float(np.mean((candidates[i] - candidates[j]) ** 2))
                num_pairs += 1
        if num_pairs:
            pairwise_mse /= num_pairs

        record = {
            "query_index": self._query_index,
            "episode_query_index": self._episode_query_count,
            "task_id": self._episode_task_id,
            "episode_index": self._episode_index,
            "global_episode_index": self._global_episode_index,
            "task_description": task_description,
            "num_candidates": int(candidates.shape[0]),
            "seeds": seeds,
            "action_shape": list(candidates.shape[1:]),
            "requested_candidate_batch_size": int(self.uq_action_candidate_batch_size),
            "actual_candidate_batch_size": int(actual_action_batch_size),
            "oom_fallback": bool(oom_fallback),
            "query_seconds": query_seconds,
            "cuda_peak_memory_gb": torch.cuda.max_memory_allocated() / (1024**3),
            "action_candidate_array_path": candidate_array_path,
            "variance_mean": float(np.mean(variance)),
            "variance_max": float(np.max(variance)),
            "variance_tail_top10_mean": tail_variance,
            "pairwise_mse_mean": pairwise_mse,
            "first_candidate_vs_mean_mse": float(np.mean((candidates[0] - np.mean(candidates, axis=0)) ** 2)),
            "per_step_variance_mean": np.mean(variance, axis=1).astype(float).tolist(),
            "per_dim_variance_mean": np.mean(variance, axis=0).astype(float).tolist(),
            **overlap_consistency,
            **world_context_uncertainty,
            **control_decision,
        }
        with self._uq_log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def _decide_uq_control(self, candidates: np.ndarray) -> dict[str, object]:
        if candidates.ndim != 3:
            raise ValueError(f"Expected candidates with shape (K, H, A), got {candidates.shape}.")
        if candidates.shape[0] < 1 or candidates.shape[1] < 1:
            raise ValueError(f"Candidate array must have non-empty K and H axes, got {candidates.shape}.")

        selected_candidate_index = 0
        medoid_scores = None
        if self.uq_control_policy == "action_cycle":
            selected_candidate_index = int((self._episode_query_count - 1) % candidates.shape[0])

        if self.uq_control_policy in {"action_medoid", "action_antimedoid", "medoid_adaptive_horizon"}:
            medoid_scores = self._candidate_medoid_scores(candidates)
            if self.uq_control_policy == "action_antimedoid":
                selected_candidate_index = int(np.argmax(medoid_scores))
            elif self.uq_control_policy in {"action_medoid", "medoid_adaptive_horizon"}:
                selected_candidate_index = int(np.argmin(medoid_scores))

        selected_execute_horizon = self.num_execute_actions
        spike_threshold = None
        first_spike_step = None
        per_step_variance_mean = None
        if self.uq_control_policy in {"adaptive_horizon", "medoid_adaptive_horizon"}:
            (
                selected_execute_horizon,
                spike_threshold,
                first_spike_step,
                per_step_variance_mean,
            ) = self._adaptive_execute_horizon(candidates)

        return self._control_decision_record(
            selected_candidate_index=selected_candidate_index,
            selected_execute_horizon=selected_execute_horizon,
            candidates=candidates,
            medoid_scores=medoid_scores,
            spike_threshold=spike_threshold,
            first_spike_step=first_spike_step,
            per_step_variance_mean=per_step_variance_mean,
        )

    def _decide_world_context_control(
        self,
        world_context_actions: np.ndarray,
        world_context_uncertainty: dict[str, object],
        fallback_decision: dict[str, object],
    ) -> tuple[np.ndarray, dict[str, object]]:
        if world_context_actions.ndim != 3:
            raise ValueError(
                f"Expected world_context_actions with shape (K_world, H, A), got {world_context_actions.shape}."
            )
        if world_context_actions.shape[0] < 2:
            raise ValueError("World-context control requires at least two world action candidates.")

        world_medoid_scores = None
        if self.uq_control_policy == "world_action_medoid":
            world_medoid_scores = self._candidate_medoid_scores(world_context_actions)
            selected_world_context_index = int(np.argmin(world_medoid_scores))
        elif self.uq_control_policy == "world_lowest_v2w_variance":
            variance_means = world_context_uncertainty.get("world_context_v2w_variance_mean")
            if not isinstance(variance_means, list) or len(variance_means) != world_context_actions.shape[0]:
                raise RuntimeError(
                    "world_lowest_v2w_variance requires one V2W variance mean per world context action."
                )
            selected_world_context_index = int(np.argmin(np.asarray(variance_means, dtype=np.float64)))
        else:
            raise RuntimeError(f"Unsupported world-context control policy: {self.uq_control_policy}")

        decision = {
            **fallback_decision,
            "selected_candidate_index": 0,
            "selected_candidate_medoid_score": None,
            "candidate_medoid_scores": None,
            "selected_world_context_index": int(selected_world_context_index),
            "selected_world_context_medoid_score": (
                float(world_medoid_scores[selected_world_context_index])
                if world_medoid_scores is not None
                else None
            ),
            "world_context_medoid_scores": (
                world_medoid_scores.astype(float).tolist() if world_medoid_scores is not None else None
            ),
        }
        return world_context_actions[selected_world_context_index], decision

    @staticmethod
    def _candidate_medoid_scores(candidates: np.ndarray) -> np.ndarray:
        flat = candidates.reshape(candidates.shape[0], -1).astype(np.float32)
        diff = flat[:, None, :] - flat[None, :, :]
        return np.mean(diff * diff, axis=2).mean(axis=1)

    def _adaptive_execute_horizon(
        self,
        candidates: np.ndarray,
    ) -> tuple[int, float, int | None, np.ndarray]:
        action_variance = np.var(candidates.astype(np.float32), axis=0)
        horizon = min(self.num_execute_actions, action_variance.shape[0])
        per_step_variance = np.mean(action_variance[:horizon], axis=1)
        warmup = min(self.uq_adaptive_spike_warmup, per_step_variance.size)
        baseline = per_step_variance[:warmup]
        median = float(np.median(baseline))
        mad = float(np.median(np.abs(baseline - median)))
        robust_scale = max(1.4826 * mad, np.finfo(np.float32).eps)
        threshold = median + self.uq_adaptive_spike_z * robust_scale
        threshold = max(threshold, self.uq_adaptive_variance_floor)
        spike_indices = np.flatnonzero(per_step_variance > threshold)
        if spike_indices.size == 0:
            return self.num_execute_actions, threshold, None, per_step_variance

        first_spike_step = int(spike_indices[0])
        execute_horizon = max(self.uq_min_execute_actions, first_spike_step)
        execute_horizon = self._bounded_execute_horizon(execute_horizon, available_actions=candidates.shape[1])
        return execute_horizon, threshold, first_spike_step, per_step_variance

    def _control_decision_record(
        self,
        *,
        selected_candidate_index: int,
        selected_execute_horizon: int,
        candidates: np.ndarray,
        medoid_scores: np.ndarray | None,
        spike_threshold: float | None,
        first_spike_step: int | None,
        per_step_variance_mean: np.ndarray | None,
    ) -> dict[str, object]:
        selected_execute_horizon = self._bounded_execute_horizon(
            selected_execute_horizon,
            available_actions=candidates.shape[1],
        )
        return {
            "uq_control_policy": self.uq_control_policy,
            "selected_candidate_index": int(selected_candidate_index),
            "selected_execute_horizon": int(selected_execute_horizon),
            "selected_candidate_medoid_score": (
                float(medoid_scores[selected_candidate_index]) if medoid_scores is not None else None
            ),
            "candidate_medoid_scores": medoid_scores.astype(float).tolist() if medoid_scores is not None else None,
            "adaptive_spike_threshold": spike_threshold,
            "adaptive_first_spike_step": first_spike_step,
            "adaptive_per_step_variance_mean": (
                per_step_variance_mean.astype(float).tolist() if per_step_variance_mean is not None else None
            ),
            "adaptive_min_execute_actions": int(self.uq_min_execute_actions),
            "adaptive_spike_z": float(self.uq_adaptive_spike_z),
            "adaptive_spike_warmup": int(self.uq_adaptive_spike_warmup),
            "adaptive_variance_floor": float(self.uq_adaptive_variance_floor),
        }

    def _compute_receding_overlap_consistency(self, candidates: np.ndarray) -> dict[str, object]:
        """Compare the new plan with the unexecuted tail of the previous receding-horizon plan."""
        base_record: dict[str, object] = {
            "receding_overlap_available": False,
            "receding_overlap_horizon": 0,
            "receding_overlap_execute_horizon": int(self._previous_execute_horizon),
        }
        if self._previous_action_chunk is None:
            return {**base_record, "receding_overlap_unavailable_reason": "first_query"}

        previous_tail = self._previous_action_chunk[self._previous_execute_horizon :]
        overlap_horizon = min(previous_tail.shape[0], candidates.shape[1])
        if overlap_horizon <= 0:
            return {**base_record, "receding_overlap_unavailable_reason": "no_future_overlap"}

        previous_overlap = previous_tail[:overlap_horizon]
        candidate_overlap = candidates[:, :overlap_horizon]
        diff = candidate_overlap - previous_overlap[None]
        per_candidate_mse = np.mean(diff**2, axis=(1, 2))
        first_per_step_mse = np.mean(diff[0] ** 2, axis=1)
        first_per_step_l2 = np.linalg.norm(diff[0], axis=1)

        previous_flat = previous_overlap.reshape(-1)
        first_flat = candidate_overlap[0].reshape(-1)
        denom = np.linalg.norm(previous_flat) * np.linalg.norm(first_flat)
        cosine = float(np.dot(previous_flat, first_flat) / denom) if denom > 0 else None

        return {
            **base_record,
            "receding_overlap_available": True,
            "receding_overlap_horizon": int(overlap_horizon),
            "receding_overlap_unavailable_reason": None,
            "receding_overlap_mse_first": float(per_candidate_mse[0]),
            "receding_overlap_l2_mean_first": float(np.mean(first_per_step_l2)),
            "receding_overlap_l2_max_first": float(np.max(first_per_step_l2)),
            "receding_overlap_cosine_first": cosine,
            "receding_overlap_mse_candidates_mean": float(np.mean(per_candidate_mse)),
            "receding_overlap_mse_candidates_std": float(np.std(per_candidate_mse)),
            "receding_overlap_mse_candidates_min": float(np.min(per_candidate_mse)),
            "receding_overlap_mse_candidates_max": float(np.max(per_candidate_mse)),
            "receding_overlap_per_step_mse_first": first_per_step_mse.astype(float).tolist(),
        }

    def log_episode_outcome(self, success: bool, replay_frames: int) -> None:
        """Append one rollout-level record that can be joined with per-query uncertainty logs."""
        record = {
            "task_id": self._episode_task_id,
            "episode_index": self._episode_index,
            "global_episode_index": self._global_episode_index,
            "task_description": self.task_description,
            "success": bool(success),
            "replay_frames": int(replay_frames),
            "policy_queries": int(self._episode_query_count),
        }
        with self._episode_outcome_log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def _process_image(self, image: np.ndarray) -> np.ndarray:
        tensor = rearrange(image, "h w c -> c h w")[:, None, :, :]
        return 2.0 * (tensor.astype(np.float32) / 255.0 - 0.5)

    def _add_image_to_history(self, image: np.ndarray) -> None:
        self._image_history.append(image)
        while len(self._image_history) < self._image_history.maxlen:
            self._image_history.append(image.copy())

    def _add_lowdim_to_history(self, lowdim: np.ndarray) -> None:
        self._lowdim_history.append(lowdim)
        while len(self._lowdim_history) < self._lowdim_horizon:
            self._lowdim_history.append(lowdim.copy())

    @staticmethod
    def _state_from_observation(obs: dict[str, np.ndarray]) -> np.ndarray:
        rot_6d = Rotation.from_quat(obs["robot0_eef_quat"]).as_matrix()[:2].reshape((6,))
        return np.concatenate((obs["robot0_eef_pos"], rot_6d, obs["robot0_gripper_qpos"][0][None]), axis=0)

    @staticmethod
    def _matrix_from_6d(orient6: np.ndarray) -> np.ndarray:
        r1 = orient6[:3]
        r2 = orient6[3:]
        r1_norm = r1 / (np.linalg.norm(r1) + 1e-9)
        r2_orth = r2 - np.dot(r2, r1_norm) * r1_norm
        r2_norm = r2_orth / (np.linalg.norm(r2_orth) + 1e-9)
        r3 = np.cross(r1_norm, r2_norm)
        return np.stack([r1_norm, r2_norm, r3], axis=0)

    def _convert_action(self, action: np.ndarray) -> np.ndarray:
        delta_pos = action[:3]
        rot_matrix = self._matrix_from_6d(action[3:9])
        rot_vec = Rotation.from_matrix(rot_matrix).as_rotvec()
        gripper = np.sign(action[9][None])
        return np.concatenate([delta_pos, rot_vec, gripper], axis=0)


def get_libero_env(task, prompt_source: str) -> tuple[OffScreenRenderEnv, str]:
    """Initializes and returns the LIBERO environment alongside the task description."""
    task_description = task_description_for_policy(task, prompt_source)
    task_bddl_file = os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file)
    env_args = {
        "bddl_file_name": task_bddl_file,
        "camera_heights": CAMERA_HEIGHT,
        "camera_widths": CAMERA_WIDTH,
    }
    env = OffScreenRenderEnv(**env_args)
    env.seed(0)
    return env, task_description


def get_libero_image(obs: dict[str, np.ndarray]) -> np.ndarray:
    """Extract the agentview image and check that it matches the expected resolution."""
    image = obs["agentview_image"][::-1, ::-1]
    if image.shape != (CAMERA_HEIGHT, CAMERA_WIDTH, 3):
        raise ValueError(f"Unexpected agentview image shape {image.shape}.")
    return image


def save_rollout_video(
    rollout_images: Iterable[np.ndarray],
    idx: int,
    success: bool,
    task_description: str,
    rollout_dir: Path,
) -> Path:
    """Save an MP4 replay of the episode."""
    rollout_dir.mkdir(parents=True, exist_ok=True)
    processed_task_description = task_description.lower().replace(" ", "_").replace("\n", "_").replace(".", "_")
    mp4_path = rollout_dir / f"episode{idx}_{'success' if success else 'failure'}_{processed_task_description}.mp4"
    video_writer = imageio.get_writer(mp4_path, fps=20)
    try:
        for img in rollout_images:
            video_writer.append_data(img)
    finally:
        video_writer.close()
    print(f"Saved rollout MP4 at path {mp4_path}")
    return mp4_path


def run_episode(
    env: OffScreenRenderEnv,
    policy: VAMInference,
    task_description: str,
    initial_observation: dict[str, np.ndarray],
    max_steps: int,
    num_steps_wait: int,
) -> tuple[bool, list[np.ndarray]]:
    """Execute a single episode and return success flag along with captured frames."""
    obs = initial_observation
    replay_images: list[np.ndarray] = []
    success = False
    active_query: dict[str, object] | None = None

    for step_idx in range(max_steps + num_steps_wait):
        if step_idx < num_steps_wait:
            obs, _, done, info = env.step(DUMMY_ACTION)
            if done:
                success = True
                break
            continue

        image = get_libero_image(obs)
        replay_images.append(image)

        policy_step_idx = step_idx - num_steps_wait
        starts_query = policy.will_start_query(task_description)
        if starts_query:
            if active_query is not None:
                raise RuntimeError("A new policy query started before the previous query outcome was logged.")
            active_query = {
                "env_step_start": policy_step_idx,
                "predicate_before": goal_predicate_state(env),
            }

        action = policy.step(image, task_description, obs)
        if starts_query:
            active_query["query_ids"] = policy.current_query_ids()

        obs, _, done, info = env.step(action.tolist())
        query_finished = active_query is not None and (done or policy.action_buffer is None)
        if query_finished:
            policy.log_query_outcome(
                build_query_outcome_record(
                    query_ids=active_query["query_ids"],
                    env_step_start=active_query["env_step_start"],
                    env_step_end=policy_step_idx,
                    predicate_before=active_query["predicate_before"],
                    predicate_after=goal_predicate_state(env),
                    episode_done_after_query=done,
                    truncated_by_episode_end=False,
                )
            )
            active_query = None

        if done:
            success = True
            break

    if active_query is not None:
        policy.log_query_outcome(
            build_query_outcome_record(
                query_ids=active_query["query_ids"],
                env_step_start=active_query["env_step_start"],
                env_step_end=max_steps - 1,
                predicate_before=active_query["predicate_before"],
                predicate_after=goal_predicate_state(env),
                episode_done_after_query=False,
                truncated_by_episode_end=True,
            )
        )

    return success, replay_images


def eval_vam_libero(
    vam_experiment_name: str,
    vam_video_model_path: str,
    vam_action_model_path: pathlib.Path,
    vam_dataset_statistics_path: pathlib.Path,
    vam_img_horizon: int,
    vam_lowdim_horizon: int,
    vam_stop_video_denoising_step: int,
    vam_num_execute_actions: int,
    task_suite_name: str,
    vam_num_sampling_steps: int = 35,
    num_trials_per_task: int = 50,
    trial_start_index: int = 0,
    eval_rank: int = 0,
    eval_world_size: int = 1,
    num_steps_wait: int = 10,
    seed: int = 0,
    use_text_encoder: bool = False,
    run_suffix: str = "",
    max_tasks: int | None = None,
    prompt_source: str = "normalized_task_language",
    task_ids: str = "",
    save_videos: bool = True,
    uq_num_action_candidates: int = 1,
    uq_action_candidate_batch_size: int = 1,
    uq_num_world_candidates: int = 1,
    uq_log_action_candidates: bool = True,
    uq_save_candidate_arrays: bool = False,
    v2w_uncertainty_head_path: pathlib.Path | None = None,
    v2w_uncertainty_calibration_path: pathlib.Path | None = None,
    v2w_uncertainty_variant: str = "a",
    v2w_uncertainty_save_variance_arrays: bool = False,
    uq_control_policy: str = "first_candidate",
    uq_min_execute_actions: int = 1,
    uq_adaptive_spike_z: float = 3.0,
    uq_adaptive_spike_warmup: int = 4,
    uq_adaptive_variance_floor: float = 0.0,
    balanced_success_target: int = 0,
    balanced_failure_target: int = 0,
    max_episode_steps: int | None = None,
) -> None:
    set_seed_everywhere(seed)
    if balanced_success_target < 0 or balanced_failure_target < 0:
        raise ValueError("balanced_success_target and balanced_failure_target must be non-negative.")
    if max_episode_steps is not None and max_episode_steps <= 0:
        raise ValueError("max_episode_steps must be positive when provided.")
    if uq_adaptive_variance_floor < 0.0:
        raise ValueError("uq_adaptive_variance_floor must be non-negative.")
    uq_control_policy = VAMInference._validate_uq_control_policy(uq_control_policy)

    run_label = (
        f"{vam_action_model_path.stem}_step{vam_num_sampling_steps}"
        f"_stopafter{vam_stop_video_denoising_step}_execute{vam_num_execute_actions}"
    )
    if uq_num_action_candidates > 1:
        run_label = f"{run_label}_uqK{uq_num_action_candidates}_w2ab{uq_action_candidate_batch_size}"
    if uq_num_world_candidates > 1:
        run_label = f"{run_label}_wuqK{uq_num_world_candidates}"
    if v2w_uncertainty_head_path is not None:
        run_label = f"{run_label}_v2wuq"
    if uq_control_policy != "first_candidate":
        control_tags = {
            "action_cycle": "ctrlcycle",
            "action_medoid": "ctrlmedoid",
            "action_antimedoid": "ctrlantimed",
            "adaptive_horizon": "ctrladap",
            "medoid_adaptive_horizon": "ctrlmedadap",
            "world_action_medoid": "ctrlwmedoid",
            "world_lowest_v2w_variance": "ctrlwlowvar",
        }
        run_label = (
            f"{run_label}_{control_tags[uq_control_policy]}"
            f"_min{uq_min_execute_actions}_z{uq_adaptive_spike_z:g}_vf{uq_adaptive_variance_floor:g}"
        )
    if run_suffix:
        run_label = f"{run_label}_{run_suffix}"
    rollout_dir = Path("./results") / run_label / task_suite_name
    rollout_dir.mkdir(parents=True, exist_ok=True)
    completed_outcomes = read_completed_episode_outcomes(rollout_dir / "episode_outcomes.jsonl")
    target_successes = sum(1 for row in completed_outcomes.values() if bool(row["success"]))
    target_failures = sum(1 for row in completed_outcomes.values() if not bool(row["success"]))

    policy = VAMInference(
        vam_experiment_name,
        vam_video_model_path,
        str(vam_action_model_path),
        vam_dataset_statistics_path,
        vam_img_horizon,
        vam_lowdim_horizon,
        vam_stop_video_denoising_step,
        vam_num_execute_actions,
        vam_num_sampling_steps,
        rollout_dir,
        use_text_encoder=use_text_encoder,
        uq_num_action_candidates=uq_num_action_candidates,
        uq_action_candidate_batch_size=uq_action_candidate_batch_size,
        uq_num_world_candidates=uq_num_world_candidates,
        uq_log_action_candidates=uq_log_action_candidates,
        uq_save_candidate_arrays=uq_save_candidate_arrays,
        v2w_uncertainty_head_path=v2w_uncertainty_head_path,
        v2w_uncertainty_calibration_path=v2w_uncertainty_calibration_path,
        v2w_uncertainty_variant=v2w_uncertainty_variant,
        v2w_uncertainty_save_variance_arrays=v2w_uncertainty_save_variance_arrays,
        uq_control_policy=uq_control_policy,
        uq_min_execute_actions=uq_min_execute_actions,
        uq_adaptive_spike_z=uq_adaptive_spike_z,
        uq_adaptive_spike_warmup=uq_adaptive_spike_warmup,
        uq_adaptive_variance_floor=uq_adaptive_variance_floor,
    )

    benchmark_dict = benchmark.get_benchmark_dict()
    if task_suite_name not in benchmark_dict:
        raise ValueError(f"Task suite {task_suite_name} not available.")
    task_suite = benchmark_dict[task_suite_name]()
    num_tasks = task_suite.n_tasks

    default_max_steps = LIBERO_SUITE_MAX_STEPS[task_suite_name]
    max_steps = max_episode_steps or default_max_steps
    if max_steps > default_max_steps:
        raise ValueError(
            f"max_episode_steps={max_steps} exceeds the {task_suite_name} default of {default_max_steps}."
        )

    total_episodes = 0
    total_successes = target_successes

    if max_tasks is not None:
        num_tasks = min(num_tasks, max_tasks)

    selected_task_ids = parse_task_ids(task_ids)
    if selected_task_ids is None:
        selected_task_ids = list(range(num_tasks))
    elif max_tasks is not None:
        selected_task_ids = selected_task_ids[:max_tasks]

    for task_id in tqdm.tqdm(selected_task_ids, desc="Tasks"):
        if balanced_targets_reached(
            target_successes,
            target_failures,
            balanced_success_target,
            balanced_failure_target,
        ):
            print(
                "Balanced raw target reached before next task: "
                f"successes={target_successes}/{balanced_success_target}, "
                f"failures={target_failures}/{balanced_failure_target}."
            )
            break
        if task_id < 0 or task_id >= task_suite.n_tasks:
            raise ValueError(f"Task id {task_id} is out of range for {task_suite_name} ({task_suite.n_tasks} tasks).")
        task = task_suite.get_task(task_id)
        initial_states = get_task_init_states_compatible(task_suite, task_id)
        env, task_description = get_libero_env(task, prompt_source)

        if len(initial_states) == 0:
            raise ValueError(f"No initial states provided for task {task_id}.")
        required_initial_states = trial_start_index + num_trials_per_task
        if required_initial_states > len(initial_states):
            raise ValueError(
                f"Task {task_id} only has {len(initial_states)} initial states, "
                f"but trials {trial_start_index}-{required_initial_states - 1} were requested."
            )

        task_successes = 0
        task_episodes = 0

        try:
            for episode_idx in tqdm.tqdm(range(num_trials_per_task), desc="Episodes", leave=False):
                if balanced_targets_reached(
                    target_successes,
                    target_failures,
                    balanced_success_target,
                    balanced_failure_target,
                ):
                    break
                trial_index = trial_start_index + episode_idx
                task_episodes += 1
                total_episodes += 1

                if total_episodes % eval_world_size != eval_rank:
                    continue
                existing_outcome = completed_outcomes.get(total_episodes)
                if existing_outcome is not None:
                    if bool(existing_outcome["success"]):
                        task_successes += 1
                    continue
                should_skip = False
                for ep in map(str, rollout_dir.iterdir()):
                    if f"episode{total_episodes}_" not in ep:
                        continue
                    should_skip = True
                    if "success" in ep:
                        task_successes += 1
                        total_successes += 1
                    break
                if should_skip:
                    continue

                env.reset()
                obs = env.set_init_state(initial_states[trial_index])

                policy.reset(task_description)
                policy.set_episode_context(task_id, trial_index, total_episodes)

                success, replay_images = run_episode(
                    env,
                    policy,
                    task_description,
                    obs,
                    max_steps,
                    num_steps_wait,
                )
                policy.log_episode_outcome(success, replay_frames=len(replay_images))
                completed_outcomes[total_episodes] = {
                    "global_episode_index": int(total_episodes),
                    "success": bool(success),
                }

                if success:
                    task_successes += 1
                    total_successes += 1
                    target_successes += 1
                else:
                    target_failures += 1

                if save_videos:
                    save_rollout_video(
                        replay_images,
                        total_episodes,
                        success,
                        task_description,
                        rollout_dir,
                    )

                success_rate = total_successes / max(total_episodes, 1)
                print(
                    f"Task {task_id} | Trial {trial_index} | Success: {success} "
                    f"| Total Success Rate: {success_rate:.3f} "
                    f"| Balanced raw counts: S={target_successes}/{balanced_success_target}, "
                    f"F={target_failures}/{balanced_failure_target}\n"
                )
        finally:
            env.close()

        task_success_rate = task_successes / max(task_episodes, 1)
        print(f"Task {task_id} success rate: {task_success_rate:.3f}")

    overall_success_rate = total_successes / max(total_episodes, 1)
    print(
        f"Completed {total_episodes} episodes | "
        f"Total successes: {total_successes} | "
        f"Balanced raw successes: {target_successes} | "
        f"Balanced raw failures: {target_failures} | "
        f"Overall success rate: {overall_success_rate:.3f}\n"
    )


if __name__ == "__main__":
    tyro.cli(eval_vam_libero)
