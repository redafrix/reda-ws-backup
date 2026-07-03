"""Run LIBERO evaluation with the Video Action Model (VAM) policy."""

from __future__ import annotations

import json
import os
import pathlib
import pickle
import random
import time
from collections import deque
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import imageio
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
torch.set_float32_matmul_precision('high')
import tqdm
import tyro
from einops import rearrange
from libero.libero import benchmark, get_libero_path
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
from model.uncertainty.skill_reliability.full_uq import (
    ACTION_SCALAR_FIELDS,
    AVAILABILITY_FIELDS,
    FIPER_ACE_FEATURE_PROFILES,
    FiperACEGeometry,
    FullUQCandidateNormalizer,
    V2W_SCALAR_FIELDS,
    build_single_candidate_action_token,
    build_full_uq_action_tokens,
    build_full_uq_feature_matrix,
)
from model.uncertainty.skill_reliability.model import (
    FullUQCandidateRiskModel,
    FullUQCandidateRiskModelConfig,
    FullUQHistoryRiskModel,
    FullUQHistoryRiskModelConfig,
    FullUQNextGenRiskModel,
    FullUQNextGenRiskModelConfig,
)
from model.uncertainty.skill_reliability.schema import NormalizerStats
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
    if prompt_source == "task_language":
        return task.language
    raise ValueError(
        "prompt_source must be 'task_language'. "
        f"Received: {prompt_source!r}"
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


class OnlineFullUQRiskScorer:
    """Score full-UQ query rows online with a trained risk monitor."""

    def __init__(self, model_dir: pathlib.Path, device: torch.device) -> None:
        self.model_dir = pathlib.Path(model_dir)
        metadata_path = self.model_dir / "metadata.json"
        model_path = self.model_dir / "model.pt"
        if not metadata_path.exists():
            raise FileNotFoundError(metadata_path)
        if not model_path.exists():
            raise FileNotFoundError(model_path)

        self.metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        self._validate_label_semantics(self.metadata)
        self.deployment_threshold = self._deployment_threshold_from_metadata(self.metadata)
        self.history = int(self.metadata["history"])
        self.feature_profile = self._feature_profile_from_metadata(self.metadata)
        self.fiper_ace_geometry = self._fiper_ace_geometry_from_metadata(self.metadata, self.feature_profile)
        self.action_candidate_policy = self._action_candidate_policy_from_metadata(self.metadata)
        self.normalizer = self._normalizer_from_metadata(self.metadata)
        self.model = self._build_model(self.metadata)
        self.model.load_state_dict(torch.load(model_path, map_location=device))
        self.model.to(device)
        self.model.eval()
        self.device = device
        self._rows: list[dict[str, object]] = []
        self._action_token_overrides: list[np.ndarray | None] = []
        self._schema_scalar_fields = set(V2W_SCALAR_FIELDS) | set(ACTION_SCALAR_FIELDS) | set(AVAILABILITY_FIELDS)
        self._expected_scalar_fields = [
            name for name in self.metadata["feature_names"] if name in self._schema_scalar_fields
        ]
        self.last_unavailable_scalar_fields: list[str] = []

    def reset_episode(self) -> None:
        self._rows.clear()
        self._action_token_overrides.clear()

    def score_query(self, row: dict[str, object]) -> float:
        risk = self.preview_query(row)
        self._rows.append(dict(row))
        self._action_token_overrides.append(None)
        return risk

    def score_query_with_action_token(self, row: dict[str, object], action_token: np.ndarray) -> float:
        risk = self.preview_query_with_action_token(row, action_token)
        self._rows.append(dict(row))
        self._action_token_overrides.append(action_token.copy())
        return risk

    def preview_query(self, row: dict[str, object]) -> float:
        return self._score_query_rows([*self._rows, row], [*self._action_token_overrides, None])

    def preview_query_with_action_token(self, row: dict[str, object], action_token: np.ndarray) -> float:
        return self._score_query_rows([*self._rows, row], [*self._action_token_overrides, action_token])

    def preview_candidate_risks(self, row: dict[str, object], candidates: np.ndarray) -> list[float]:
        if not isinstance(self.normalizer, FullUQCandidateNormalizer):
            raise RuntimeError("Candidate risk selection requires a candidate-conditioned risk model.")
        if candidates.ndim != 3:
            raise ValueError(f"Expected candidates with shape (K, H, A), got {candidates.shape}.")
        if candidates.shape[0] < 2:
            raise ValueError("Candidate risk selection requires at least two action candidates.")
        return [
            self.preview_query_with_action_token(row, self.candidate_action_token(candidates, idx))
            for idx in range(candidates.shape[0])
        ]

    def candidate_action_token(self, candidates: np.ndarray, candidate_index: int) -> np.ndarray:
        return build_single_candidate_action_token(
            candidates,
            candidate_index,
            policy=self.action_candidate_policy,
        )

    def _score_query_rows(
        self,
        query_rows: list[dict[str, object]],
        action_token_overrides: list[np.ndarray | None],
    ) -> float:
        if len(query_rows) != len(action_token_overrides):
            raise ValueError(
                f"Expected one action-token override per query row, got {len(action_token_overrides)} "
                f"overrides for {len(query_rows)} rows."
            )
        rows = pd.DataFrame(query_rows)
        rows["episode_key"] = rows["run_id"].astype(str) + "::" + rows["global_episode_index"].astype(str)
        self.last_unavailable_scalar_fields = self._add_unavailable_scalar_schema_columns(rows)
        features, feature_names = build_full_uq_feature_matrix(
            rows,
            feature_profile=self.feature_profile,
            fiper_ace_geometry=self.fiper_ace_geometry,
        )
        action_tokens, action_names = build_full_uq_action_tokens(rows, policy=self.action_candidate_policy)
        self._validate_schema(feature_names, action_names)
        for idx, action_token_override in enumerate(action_token_overrides):
            if action_token_override is None:
                continue
            if action_token_override.shape != action_tokens[idx].shape:
                raise ValueError(
                    "Candidate action-token override shape mismatch: "
                    f"got {action_token_override.shape}, expected {action_tokens[idx].shape}."
                )
            action_tokens[idx] = action_token_override

        idx = len(rows) - 1
        history_indices = self._history_indices(rows, idx)
        with torch.no_grad():
            if isinstance(self.normalizer, FullUQCandidateNormalizer):
                batch = {
                    "history": torch.as_tensor(
                        self.normalizer.static.transform(features)[history_indices][None],
                        dtype=torch.float32,
                        device=self.device,
                    ),
                    "action": torch.as_tensor(
                        self.normalizer.action.transform(action_tokens[idx : idx + 1]),
                        dtype=torch.float32,
                        device=self.device,
                    ),
                    "static": torch.as_tensor(
                        self.normalizer.static.transform(features[idx : idx + 1]),
                        dtype=torch.float32,
                        device=self.device,
                    ),
                }
            elif isinstance(self.normalizer, NormalizerStats):
                batch = {
                    "history": torch.as_tensor(
                        self.normalizer.transform(features)[history_indices][None],
                        dtype=torch.float32,
                        device=self.device,
                    ),
                }
            else:
                raise TypeError(f"Unsupported normalizer type: {type(self.normalizer)!r}")
            logit = self.model(batch)["risk_logit"].detach().float().flatten()[0]
        return float(torch.sigmoid(logit).cpu())

    def _add_unavailable_scalar_schema_columns(self, rows: pd.DataFrame) -> list[str]:
        missing = [name for name in self._expected_scalar_fields if name not in rows.columns]
        unavailable = []
        for name in missing:
            if not self._scalar_field_is_unavailable(rows, name):
                raise RuntimeError(
                    f"Risk model required scalar feature {name!r}, but the online row did not provide it "
                    "and no availability flag marks it as unavailable."
                )
            rows[name] = 0.0
            unavailable.append(name)
        return unavailable

    @staticmethod
    def _scalar_field_is_unavailable(rows: pd.DataFrame, name: str) -> bool:
        if name.startswith("receding_overlap_") and "receding_overlap_available" in rows.columns:
            return not rows["receding_overlap_available"].fillna(False).astype(bool).any()
        if name.startswith("world_context_") and "world_context_uncertainty_available" in rows.columns:
            return not rows["world_context_uncertainty_available"].fillna(False).astype(bool).any()
        if name.startswith("v2w_") and "v2w_uncertainty_available" in rows.columns:
            return not rows["v2w_uncertainty_available"].fillna(False).astype(bool).any()
        return False

    def _validate_schema(self, feature_names: list[str], action_names: list[str]) -> None:
        expected_features = list(self.metadata["feature_names"])
        if feature_names != expected_features:
            missing = [name for name in expected_features if name not in feature_names]
            unexpected = [name for name in feature_names if name not in expected_features]
            raise RuntimeError(
                f"Risk model feature schema mismatch: got {len(feature_names)} names, "
                f"expected {len(expected_features)}. Missing={missing}; unexpected={unexpected}."
            )
        if isinstance(self.normalizer, FullUQCandidateNormalizer):
            expected_actions = list(self.metadata["action_token_names"])
            if action_names != expected_actions:
                raise RuntimeError(
                    f"Risk model action-token schema mismatch: got {len(action_names)} names, "
                    f"expected {len(expected_actions)}."
                )

    def _history_indices(self, rows: pd.DataFrame, idx: int) -> np.ndarray:
        start = max(0, idx - self.history + 1)
        window = np.arange(start, idx + 1, dtype=np.int64)
        if len(window) < self.history:
            pad = np.full(self.history - len(window), int(window[0]), dtype=np.int64)
            window = np.concatenate([pad, window])
        return window.astype(np.int64)

    @staticmethod
    def _normalizer_from_metadata(metadata: dict[str, object]) -> NormalizerStats | FullUQCandidateNormalizer:
        payload = metadata["normalizer"]
        if not isinstance(payload, dict):
            raise RuntimeError("Risk model metadata normalizer must be a dictionary.")
        if "static" in payload and "action" in payload:
            return FullUQCandidateNormalizer(
                static=NormalizerStats.from_dict(payload["static"]),
                action=NormalizerStats.from_dict(payload["action"]),
            )
        return NormalizerStats.from_dict(payload)

    @staticmethod
    def _build_model(metadata: dict[str, object]) -> torch.nn.Module:
        family = str(metadata["model_family"])
        config = metadata["model"]
        if not isinstance(config, dict):
            raise RuntimeError("Risk model metadata model config must be a dictionary.")
        if family == "history":
            return FullUQHistoryRiskModel(FullUQHistoryRiskModelConfig(**config))
        if family == "baseline":
            return FullUQCandidateRiskModel(FullUQCandidateRiskModelConfig(**config))
        if family in {"nextgen", "predicate_nextgen"}:
            return FullUQNextGenRiskModel(FullUQNextGenRiskModelConfig(**config))
        raise ValueError(f"Unsupported risk model family: {family!r}")

    @staticmethod
    def _deployment_threshold_from_metadata(metadata: dict[str, object]) -> float | None:
        if "deployment_threshold" not in metadata:
            return None
        threshold = float(metadata["deployment_threshold"])
        if threshold <= 0.0 or threshold >= 1.0:
            raise ValueError(f"Risk model deployment threshold must be in (0, 1), got {threshold}.")
        return threshold

    @staticmethod
    def _validate_label_semantics(metadata: dict[str, object]) -> None:
        label_column = str(metadata.get("label_column", ""))
        if label_column != "failure_label":
            raise RuntimeError(
                "Online WM risk control only accepts models trained on episode-level failure_label. "
                f"Got label_column={label_column!r}."
            )

    @staticmethod
    def _feature_profile_from_metadata(metadata: dict[str, object]) -> str:
        value = metadata.get("feature_profile")
        if value is not None:
            return str(value)

        feature_names = metadata.get("feature_names")
        if not isinstance(feature_names, list) or not all(isinstance(name, str) for name in feature_names):
            raise RuntimeError("Legacy risk model metadata missing a valid feature_names list.")
        rich_action_names = [name for name in feature_names if name.startswith("candidate_")]
        if rich_action_names:
            raise RuntimeError(
                "Legacy risk model metadata is missing feature_profile but contains rich-action scalar "
                f"features: {rich_action_names[:8]}."
            )
        return "core"

    @staticmethod
    def _fiper_ace_geometry_from_metadata(
        metadata: dict[str, object],
        feature_profile: str,
    ) -> FiperACEGeometry | None:
        payload = metadata.get("fiper_ace_geometry")
        if feature_profile in FIPER_ACE_FEATURE_PROFILES:
            if not isinstance(payload, dict):
                raise RuntimeError(
                    f"ACE risk model with feature_profile={feature_profile!r} is missing fitted "
                    "fiper_ace_geometry metadata."
                )
            return FiperACEGeometry.from_dict(payload)
        if payload is not None:
            raise RuntimeError("Non-ACE risk model unexpectedly contains fiper_ace_geometry metadata.")
        return None

    @staticmethod
    def _action_candidate_policy_from_metadata(metadata: dict[str, object]) -> str:
        value = metadata.get("action_candidate_policy")
        if value is not None:
            return str(value)

        action_token_names = metadata.get("action_token_names")
        if isinstance(action_token_names, list) and action_token_names:
            return "require"
        if str(metadata.get("model_family", "")) == "history":
            return "ignore"
        raise RuntimeError(
            "Risk model metadata missing action_candidate_policy and does not contain enough schema "
            "information to infer it."
        )


class RiskAdaptiveController:
    """Map calibrated online risk scores to an execution horizon."""

    def __init__(
        self,
        scorer: OnlineFullUQRiskScorer,
        *,
        threshold: float,
        medium_threshold: float,
        persistence: int,
        medium_horizon: int,
        high_horizon: int,
        default_horizon: int,
    ) -> None:
        if threshold <= 0.0 or threshold >= 1.0:
            raise ValueError(f"Risk threshold must be in (0, 1), got {threshold}.")
        if medium_threshold < 0.0 or medium_threshold >= 1.0:
            raise ValueError(f"Risk medium threshold must be in [0, 1), got {medium_threshold}.")
        if persistence < 1:
            raise ValueError(f"Risk persistence must be >= 1, got {persistence}.")
        self.scorer = scorer
        self.threshold = float(threshold)
        self.medium_threshold = float(medium_threshold)
        self.persistence = int(persistence)
        self.medium_horizon = int(medium_horizon)
        self.high_horizon = int(high_horizon)
        self.default_horizon = int(default_horizon)
        self._recent_high: deque[bool] = deque(maxlen=self.persistence)
        self._recent_risk: deque[float] = deque(maxlen=max(1, self.persistence))

    def reset_episode(self) -> None:
        self.scorer.reset_episode()
        self._recent_high.clear()
        self._recent_risk.clear()

    def decide(self, row: dict[str, object], action_token: np.ndarray | None = None) -> dict[str, object]:
        if action_token is None:
            risk = self.scorer.score_query(row)
        else:
            risk = self.scorer.score_query_with_action_token(row, action_token)
        is_high = risk > self.threshold
        self._recent_high.append(is_high)
        self._recent_risk.append(risk)
        persistent_high = len(self._recent_high) == self.persistence and all(self._recent_high)
        if persistent_high:
            horizon = self.high_horizon
            reason = "persistent_high_risk"
        elif self.medium_threshold > 0.0 and risk > self.medium_threshold:
            horizon = self.medium_horizon
            reason = "medium_risk"
        else:
            horizon = self.default_horizon
            reason = "low_risk"
        return {
            "risk_probability": float(risk),
            "risk_threshold": float(self.threshold),
            "risk_medium_threshold": float(self.medium_threshold),
            "risk_persistence": int(self.persistence),
            "risk_recent_values": [float(value) for value in self._recent_risk],
            "risk_recent_high": [bool(value) for value in self._recent_high],
            "risk_persistent_high": bool(persistent_high),
            "risk_horizon_reason": reason,
            "risk_unavailable_scalar_fields": list(self.scorer.last_unavailable_scalar_fields),
            "selected_execute_horizon": int(horizon),
        }


def _resolve_risk_threshold(
    requested_threshold: float | None,
    scorer: OnlineFullUQRiskScorer,
) -> float:
    if requested_threshold is not None:
        return float(requested_threshold)
    if scorer.deployment_threshold is not None:
        return float(scorer.deployment_threshold)
    raise ValueError(
        "calibrator_adaptive_horizon requires --uq-risk-threshold unless the risk model metadata "
        "contains deployment_threshold or deployment.risk_threshold."
    )


def _risk_threshold_for_run_label(
    control_policy: str,
    model_dir: pathlib.Path | None,
    requested_threshold: float | None,
) -> float:
    risk_control_policies = {
        "calibrator_adaptive_horizon",
        "action_medoid_calibrator_adaptive_horizon",
        "action_medoid_calibrator_recovery",
        "lowest_risk_candidate_calibrator_horizon",
        "risk_gated_action_medoid_horizon",
    }
    if control_policy not in risk_control_policies:
        return 0.0
    if requested_threshold is not None:
        return float(requested_threshold)
    if model_dir is None:
        raise ValueError(f"{control_policy} requires --uq-risk-model-dir.")
    metadata_path = pathlib.Path(model_dir) / "metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(metadata_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    threshold = OnlineFullUQRiskScorer._deployment_threshold_from_metadata(metadata)
    if threshold is None:
        raise ValueError(
            "calibrator_adaptive_horizon requires --uq-risk-threshold unless the risk model metadata "
            "contains deployment_threshold or deployment.risk_threshold."
        )
    return threshold


@dataclass(frozen=True)
class EpisodeManifest:
    path: pathlib.Path
    pairs_by_suite: dict[str, set[tuple[int, int]]]
    row_count_by_suite: dict[str, int]


def load_episode_manifest(path: pathlib.Path | None) -> EpisodeManifest | None:
    if path is None:
        return None
    if not path.exists():
        raise FileNotFoundError(path)
    frame = pd.read_csv(path)
    required = {"task_suite_name", "task_id", "initial_state_index", "eval_seed"}
    missing = required - set(frame.columns)
    if missing:
        raise RuntimeError(f"{path} is missing required columns: {sorted(missing)}")
    invalid_seed = frame["eval_seed"].astype(int) != 0
    if invalid_seed.any():
        examples = frame.loc[invalid_seed, ["task_suite_name", "task_id", "initial_state_index", "eval_seed"]]
        raise RuntimeError(f"{path} contains nonzero eval seeds: {examples.head(5).to_dict('records')}")
    if "trial_index" in frame.columns:
        mismatched_trial = frame["trial_index"].astype(int) != frame["initial_state_index"].astype(int)
        if mismatched_trial.any():
            examples = frame.loc[
                mismatched_trial,
                ["task_suite_name", "task_id", "trial_index", "initial_state_index"],
            ]
            raise RuntimeError(
                f"{path} contains rows where trial_index != initial_state_index: "
                f"{examples.head(5).to_dict('records')}"
            )
    if "episode_uid" in frame.columns:
        duplicate_uid = frame["episode_uid"].duplicated(keep=False)
        if duplicate_uid.any():
            examples = frame.loc[duplicate_uid, ["episode_uid", "task_suite_name", "task_id", "initial_state_index"]]
            raise RuntimeError(f"{path} contains duplicate episode_uid rows: {examples.head(5).to_dict('records')}")

    selected: dict[str, set[tuple[int, int]]] = {}
    row_count_by_suite: dict[str, int] = {}
    identities: set[tuple[str, int, int, int]] = set()
    for row in frame.to_dict("records"):
        suite = str(row["task_suite_name"])
        task_id = int(row["task_id"])
        state_index = int(row["initial_state_index"])
        eval_seed = int(row["eval_seed"])
        identity = (suite, task_id, state_index, eval_seed)
        if identity in identities:
            raise RuntimeError(f"{path} contains duplicate episode identity: {identity}")
        identities.add(identity)
        selected.setdefault(suite, set()).add((task_id, state_index))
        row_count_by_suite[suite] = row_count_by_suite.get(suite, 0) + 1
    return EpisodeManifest(path=path, pairs_by_suite=selected, row_count_by_suite=row_count_by_suite)


def validate_episode_manifest_request(
    manifest: EpisodeManifest | None,
    task_suite_name: str,
    selected_task_ids: list[int],
    trial_start_index: int,
    num_trials_per_task: int,
) -> None:
    if manifest is None:
        return
    if task_suite_name not in manifest.pairs_by_suite:
        raise ValueError(f"Episode manifest has no rows for task suite {task_suite_name!r}.")

    requested_tasks = set(selected_task_ids)
    requested_trials = set(range(trial_start_index, trial_start_index + num_trials_per_task))
    pairs = manifest.pairs_by_suite[task_suite_name]
    outside_tasks = sorted({task_id for task_id, _ in pairs} - requested_tasks)
    outside_trials = sorted({trial for _, trial in pairs} - requested_trials)
    if outside_tasks:
        raise ValueError(
            f"Episode manifest {manifest.path} contains task IDs not requested for {task_suite_name}: "
            f"{outside_tasks[:10]}"
        )
    if outside_trials:
        raise ValueError(
            f"Episode manifest {manifest.path} contains initial-state indices outside requested range "
            f"{trial_start_index}-{trial_start_index + num_trials_per_task - 1}: {outside_trials[:10]}"
        )


def validate_resume_outcome(row: dict[str, object], task_id: int, trial_index: int, task_description: str) -> None:
    if int(row["task_id"]) != int(task_id):
        raise RuntimeError(f"Stale episode outcome has task_id={row['task_id']}, expected {task_id}.")
    if int(row["episode_index"]) != int(trial_index):
        raise RuntimeError(
            f"Stale episode outcome has episode_index={row['episode_index']}, expected trial {trial_index}."
        )
    if str(row["task_description"]) != task_description:
        raise RuntimeError(
            "Stale episode outcome uses a different task description: "
            f"{row['task_description']!r} != {task_description!r}."
        )


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
        uq_risk_model_dir: pathlib.Path | None = None,
        uq_risk_threshold: float | None = None,
        uq_risk_medium_threshold: float = 0.0,
        uq_risk_persistence: int = 2,
        uq_risk_medium_execute_actions: int = 7,
        uq_risk_high_execute_actions: int = 4,
        uq_recovery_steps: int = 0,
        uq_recovery_delta_z: float = 0.0,
        uq_recovery_gripper: float = -1.0,
        uq_recovery_cooldown_queries: int = 0,
        uq_recovery_max_per_episode: int = 0,
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
        self._query_runtime_log_path = rollout_dir / "policy_query_runtime.jsonl"
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
        self.uq_recovery_steps = int(uq_recovery_steps)
        self.uq_recovery_delta_z = float(uq_recovery_delta_z)
        self.uq_recovery_gripper = float(uq_recovery_gripper)
        self.uq_recovery_cooldown_queries = int(uq_recovery_cooldown_queries)
        self.uq_recovery_max_per_episode = int(uq_recovery_max_per_episode)
        self.risk_controller = None
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
        if self._uses_recovery_control():
            self._validate_recovery_parameters()
        if self._uses_calibrator_horizon_control():
            if uq_risk_model_dir is None:
                raise ValueError(f"{self.uq_control_policy} requires --uq-risk-model-dir.")
            scorer = OnlineFullUQRiskScorer(pathlib.Path(uq_risk_model_dir), torch.device("cuda"))
            risk_threshold = _resolve_risk_threshold(uq_risk_threshold, scorer)
            self.risk_controller = RiskAdaptiveController(
                scorer,
                threshold=risk_threshold,
                medium_threshold=float(uq_risk_medium_threshold),
                persistence=int(uq_risk_persistence),
                medium_horizon=int(uq_risk_medium_execute_actions),
                high_horizon=int(uq_risk_high_execute_actions),
                default_horizon=int(self.num_execute_actions),
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
        if (self._uses_candidate_risk_selection() or self._uses_risk_gated_action_medoid()) and (
            self.uq_num_action_candidates < 2
        ):
            raise ValueError(f"{self.uq_control_policy} requires uq_num_action_candidates >= 2.")
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

    def _uses_calibrator_horizon_control(self) -> bool:
        return self.uq_control_policy in {
            "calibrator_adaptive_horizon",
            "action_medoid_calibrator_adaptive_horizon",
            "action_medoid_calibrator_recovery",
            "lowest_risk_candidate_calibrator_horizon",
            "risk_gated_action_medoid_horizon",
        }

    def _uses_candidate_risk_selection(self) -> bool:
        return self.uq_control_policy == "lowest_risk_candidate_calibrator_horizon"

    def _uses_risk_gated_action_medoid(self) -> bool:
        return self.uq_control_policy == "risk_gated_action_medoid_horizon"

    def _uses_recovery_control(self) -> bool:
        return self.uq_control_policy == "action_medoid_calibrator_recovery"

    def _validate_recovery_parameters(self) -> None:
        if self.uq_recovery_steps < 1:
            raise ValueError("action_medoid_calibrator_recovery requires uq_recovery_steps >= 1.")
        if self.uq_recovery_delta_z <= 0.0:
            raise ValueError("action_medoid_calibrator_recovery requires uq_recovery_delta_z > 0.")
        if self.uq_recovery_gripper == 0.0:
            raise ValueError("uq_recovery_gripper must be non-zero so np.sign gives a defined gripper command.")
        if self.uq_recovery_cooldown_queries < 0:
            raise ValueError("uq_recovery_cooldown_queries must be non-negative.")
        if self.uq_recovery_max_per_episode < 1:
            raise ValueError("action_medoid_calibrator_recovery requires uq_recovery_max_per_episode >= 1.")

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
            "calibrator_adaptive_horizon",
            "action_medoid_calibrator_adaptive_horizon",
            "action_medoid_calibrator_recovery",
            "lowest_risk_candidate_calibrator_horizon",
            "risk_gated_action_medoid_horizon",
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
        self._recovery_count = 0
        self._recovery_cooldown_remaining = 0
        self._episode_task_id: int | None = None
        self._episode_index: int | None = None
        self._global_episode_index: int | None = None
        self._episode_query_count = 0
        if self.risk_controller is not None:
            self.risk_controller.reset_episode()

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
        torch.cuda.synchronize()
        query_started_at = time.perf_counter()
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
        torch.cuda.synchronize()
        query_wall_seconds = time.perf_counter() - query_started_at
        with self._query_runtime_log_path.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "query_index": self._query_index,
                        "episode_query_index": self._episode_query_count,
                        "task_id": self._episode_task_id,
                        "episode_index": self._episode_index,
                        "global_episode_index": self._global_episode_index,
                        "query_wall_seconds": query_wall_seconds,
                        "selected_execute_horizon": self._execute_horizon,
                        "cuda_peak_memory_gb": torch.cuda.max_memory_allocated() / (1024**3),
                    }
                )
                + "\n"
            )

    def _bounded_execute_horizon(self, requested_horizon: int, available_actions: int) -> int:
        requested = int(requested_horizon)
        available = int(available_actions)
        if requested < 1:
            raise RuntimeError(f"Requested execute horizon must be positive, got {requested}.")
        if requested > self.num_execute_actions:
            raise RuntimeError(
                f"Requested execute horizon {requested} exceeds configured maximum {self.num_execute_actions}."
            )
        if requested > available:
            raise RuntimeError(
                f"Requested execute horizon {requested} exceeds produced action chunk length {available}."
            )
        return requested

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

            return self._predict_single_action_without_v2w_uncertainty(
                input_vid=input_vid,
                state_tensor=state_tensor,
                task_description=task_description,
                prompt_embedding=prompt_embedding,
            )

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
        candidate_array_path = self._save_action_candidate_arrays(
            candidates=candidates,
            world_context_actions=world_context_actions,
            selected_candidate_index=selected_candidate_index,
            selected_world_context_index=control_decision.get("selected_world_context_index"),
        )
        overlap_consistency = self._compute_receding_overlap_consistency(candidates)
        action_record = self._action_candidate_uncertainty_record(
            task_description,
            seeds,
            candidates,
            query_seconds,
            actual_action_batch_size,
            oom_fallback,
            overlap_consistency,
            world_context_uncertainty,
            candidate_array_path,
            {},
        )
        control_decision = self._apply_candidate_risk_selection(
            action_record=action_record,
            v2w_metrics=uncertainty_metrics,
            candidates=candidates,
            fallback_decision=control_decision,
        )
        selected_candidate_index = int(control_decision["selected_candidate_index"])
        selected_action = candidates[selected_candidate_index]
        control_decision = self._apply_risk_control(
            action_record=action_record,
            v2w_metrics=uncertainty_metrics,
            fallback_decision=control_decision,
            available_actions=candidates.shape[1],
            candidates=candidates,
        )
        control_decision = self._apply_risk_gated_action_medoid(
            candidates=candidates,
            control_decision=control_decision,
        )
        selected_candidate_index = int(control_decision["selected_candidate_index"])
        selected_action = candidates[selected_candidate_index]
        candidate_array_path = self._save_action_candidate_arrays(
            candidates=candidates,
            world_context_actions=world_context_actions,
            selected_candidate_index=selected_candidate_index,
            selected_world_context_index=control_decision.get("selected_world_context_index"),
        )
        action_record["action_candidate_array_path"] = candidate_array_path
        selected_action, control_decision = self._apply_recovery_control(selected_action, control_decision)
        self._pending_execute_horizon = int(control_decision["selected_execute_horizon"])
        self._last_control_decision = control_decision
        if self.uq_log_action_candidates:
            self._write_action_candidate_uncertainty({**action_record, **control_decision})

        return selected_action

    def _apply_risk_gated_action_medoid(
        self,
        *,
        candidates: np.ndarray,
        control_decision: dict[str, object],
    ) -> dict[str, object]:
        if not self._uses_risk_gated_action_medoid():
            return control_decision

        medoid_scores = control_decision.get("candidate_medoid_scores")
        if medoid_scores is None:
            raise RuntimeError("risk_gated_action_medoid_horizon requires candidate medoid scores.")
        if str(control_decision.get("risk_horizon_reason")) != "persistent_high_risk":
            selected_candidate_index = 0
            selection_reason = "low_risk_first_candidate"
        else:
            scores = np.asarray(medoid_scores, dtype=np.float64)
            if scores.shape != (candidates.shape[0],):
                raise RuntimeError(
                    "candidate medoid score count does not match action candidate count "
                    f"({scores.shape} vs {candidates.shape[0]})."
                )
            selected_candidate_index = int(np.argmin(scores))
            selection_reason = "high_risk_action_medoid"

        return {
            **control_decision,
            "selected_candidate_index": selected_candidate_index,
            "selected_candidate_medoid_score": float(medoid_scores[selected_candidate_index]),
            "candidate_selection_reason": selection_reason,
        }

    def _apply_recovery_control(
        self,
        selected_action: np.ndarray,
        control_decision: dict[str, object],
    ) -> tuple[np.ndarray, dict[str, object]]:
        if not self._uses_recovery_control():
            return selected_action, control_decision

        if not self._should_trigger_recovery(control_decision):
            return selected_action, {
                **control_decision,
                "recovery_triggered": False,
                "recovery_count": int(self._recovery_count),
                "recovery_cooldown_remaining": int(self._recovery_cooldown_remaining),
            }

        self._recovery_count += 1
        self._recovery_cooldown_remaining = self.uq_recovery_cooldown_queries
        recovery_chunk = self._recovery_action_chunk(selected_action.shape[-1])
        return recovery_chunk, {
            **control_decision,
            "recovery_triggered": True,
            "recovery_count": int(self._recovery_count),
            "recovery_cooldown_remaining": int(self._recovery_cooldown_remaining),
            "recovery_delta_z": float(self.uq_recovery_delta_z),
            "selected_execute_horizon": int(recovery_chunk.shape[0]),
        }

    def _should_trigger_recovery(self, control_decision: dict[str, object]) -> bool:
        if self._recovery_count >= self.uq_recovery_max_per_episode:
            return False
        if self._recovery_cooldown_remaining > 0:
            self._recovery_cooldown_remaining -= 1
            return False
        return str(control_decision.get("risk_horizon_reason")) == "persistent_high_risk"

    def _recovery_action_chunk(self, action_dim: int) -> np.ndarray:
        if action_dim != 10:
            raise ValueError(f"Recovery control expects 10D W2A actions before conversion, got {action_dim}.")
        chunk = np.zeros((self.uq_recovery_steps, action_dim), dtype=np.float32)
        chunk[:, 2] = self.uq_recovery_delta_z
        chunk[:, 3] = 1.0
        chunk[:, 7] = 1.0
        chunk[:, 9] = self.uq_recovery_gripper
        return chunk

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

    def _predict_single_action_without_v2w_uncertainty(
        self,
        input_vid: torch.Tensor,
        state_tensor: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
    ) -> np.ndarray:
        with torch.no_grad():
            crossattn_emb, video_sigma = self._generate_action_context_for_w2a(
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
        return pred_actions[0].float().cpu().numpy()

    def _generate_action_context_for_w2a(
        self,
        input_vid: torch.Tensor,
        task_description: str,
        prompt_embedding: torch.Tensor | None,
        seed: int = 0,
    ) -> tuple[torch.Tensor, torch.Tensor]:
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
        sigma_B_1 = sigma.unsqueeze(1) if sigma.ndim == 1 else sigma
        hidden_state_shape = hidden_states.shape
        crossattn_emb = hidden_states.reshape(hidden_state_shape[0], -1, hidden_state_shape[-1])
        return crossattn_emb, sigma_B_1

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
            raise RuntimeError("World-context uncertainty generation ran out of CUDA memory.") from None

        actions = np.stack(action_chunks, axis=0)
        try:
            _ensure_finite_array(actions, "world-context induced actions")
            context_metrics = self.model._summarize_context_disagreement(context_snapshots)
        except ValueError as exc:
            raise RuntimeError("World-context uncertainty produced non-finite values.") from exc
        pairwise_mse = self._mean_pairwise_action_mse(actions)
        if not np.isfinite(pairwise_mse):
            raise RuntimeError("World-context induced action pairwise MSE was not finite.")
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
        """Run one V2W pass and K W2A candidate passes."""
        action_batch_size = min(self.uq_action_candidate_batch_size, len(seeds))
        actual_action_batch_size = action_batch_size
        oom_fallback = False
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
            raise RuntimeError("World-context uncertainty generation ran out of CUDA memory.") from None
        except ValueError as exc:
            raise RuntimeError("World-context uncertainty produced non-finite values.") from exc

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
            raise RuntimeError("World-context induced action pairwise MSE was not finite.")

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
            except Exception as exc:
                raise RuntimeError("World-context trajectory metrics failed.") from exc

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
        record = self._action_candidate_uncertainty_record(
            task_description,
            seeds,
            candidates,
            query_seconds,
            actual_action_batch_size,
            oom_fallback,
            overlap_consistency,
            world_context_uncertainty,
            candidate_array_path,
            control_decision,
        )
        self._write_action_candidate_uncertainty(record)

    def _action_candidate_uncertainty_record(
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
    ) -> dict[str, object]:
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
        return record

    def _write_action_candidate_uncertainty(self, record: dict[str, object]) -> None:
        with self._uq_log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def _apply_risk_control(
        self,
        *,
        action_record: dict[str, object],
        v2w_metrics: dict[str, object],
        fallback_decision: dict[str, object],
        available_actions: int,
        candidates: np.ndarray | None = None,
    ) -> dict[str, object]:
        if self.risk_controller is None:
            return fallback_decision
        risk_row = self._risk_row(action_record, v2w_metrics)
        action_token = None
        if self._uses_candidate_risk_selection():
            if candidates is None:
                raise RuntimeError("Candidate risk selection requires the full candidate action batch.")
            selected_index = int(fallback_decision["selected_candidate_index"])
            action_token = self.risk_controller.scorer.candidate_action_token(candidates, selected_index)
        risk_decision = self.risk_controller.decide(risk_row, action_token=action_token)
        selected_horizon = self._bounded_execute_horizon(
            int(risk_decision["selected_execute_horizon"]),
            available_actions=available_actions,
        )
        return {
            **fallback_decision,
            **risk_decision,
            "uq_control_policy": self.uq_control_policy,
            "selected_execute_horizon": selected_horizon,
        }

    def _apply_candidate_risk_selection(
        self,
        *,
        action_record: dict[str, object],
        v2w_metrics: dict[str, object],
        candidates: np.ndarray,
        fallback_decision: dict[str, object],
    ) -> dict[str, object]:
        if not self._uses_candidate_risk_selection():
            return fallback_decision
        if self.risk_controller is None:
            raise RuntimeError("lowest_risk_candidate_calibrator_horizon requires a risk controller.")
        risk_row = self._risk_row(action_record, v2w_metrics)
        candidate_risks = self.risk_controller.scorer.preview_candidate_risks(risk_row, candidates)
        selected_candidate_index = int(np.argmin(np.asarray(candidate_risks, dtype=np.float64)))
        return {
            **fallback_decision,
            "selected_candidate_index": selected_candidate_index,
            "candidate_risk_probabilities": [float(value) for value in candidate_risks],
            "selected_candidate_risk_probability": float(candidate_risks[selected_candidate_index]),
            "candidate_risk_selection_semantics": "minimum_candidate_failure_probability",
        }

    def _risk_row(
        self,
        action_record: dict[str, object],
        v2w_metrics: dict[str, object],
    ) -> dict[str, object]:
        return {
            **action_record,
            **v2w_metrics,
            "run_id": f"{self.rollout_dir.parent.name}/{self.rollout_dir.name}",
            "success": False,
            "failure_label": 0.0,
            "rollout_dir": str(self.rollout_dir),
        }

    def _decide_uq_control(self, candidates: np.ndarray) -> dict[str, object]:
        if candidates.ndim != 3:
            raise ValueError(f"Expected candidates with shape (K, H, A), got {candidates.shape}.")
        if candidates.shape[0] < 1 or candidates.shape[1] < 1:
            raise ValueError(f"Candidate array must have non-empty K and H axes, got {candidates.shape}.")

        selected_candidate_index = 0
        medoid_scores = None
        if self.uq_control_policy == "action_cycle":
            selected_candidate_index = int((self._episode_query_count - 1) % candidates.shape[0])

        if self.uq_control_policy in {
            "action_medoid",
            "action_antimedoid",
            "medoid_adaptive_horizon",
            "action_medoid_calibrator_adaptive_horizon",
            "action_medoid_calibrator_recovery",
            "risk_gated_action_medoid_horizon",
        }:
            medoid_scores = self._candidate_medoid_scores(candidates)
            if self.uq_control_policy == "action_antimedoid":
                selected_candidate_index = int(np.argmax(medoid_scores))
            elif self.uq_control_policy in {
                "action_medoid",
                "medoid_adaptive_horizon",
                "action_medoid_calibrator_adaptive_horizon",
                "action_medoid_calibrator_recovery",
            }:
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

    def log_episode_outcome(
        self,
        success: bool,
        replay_frames: int,
        wall_time_seconds: float,
    ) -> None:
        """Append one rollout-level record that can be joined with per-query uncertainty logs."""
        record = {
            "task_id": self._episode_task_id,
            "episode_index": self._episode_index,
            "global_episode_index": self._global_episode_index,
            "task_description": self.task_description,
            "success": bool(success),
            "replay_frames": int(replay_frames),
            "policy_queries": int(self._episode_query_count),
            "wall_time_seconds": float(wall_time_seconds),
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
    prompt_source: str = "task_language",
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
    uq_risk_model_dir: pathlib.Path | None = None,
    uq_risk_threshold: float | None = None,
    uq_risk_medium_threshold: float = 0.0,
    uq_risk_persistence: int = 2,
    uq_risk_medium_execute_actions: int = 7,
    uq_risk_high_execute_actions: int = 4,
    uq_recovery_steps: int = 0,
    uq_recovery_delta_z: float = 0.0,
    uq_recovery_gripper: float = -1.0,
    uq_recovery_cooldown_queries: int = 0,
    uq_recovery_max_per_episode: int = 0,
    episode_manifest_path: pathlib.Path | None = None,
    balanced_success_target: int = 0,
    balanced_failure_target: int = 0,
    max_episode_steps: int | None = None,
    output_dir: pathlib.Path | None = None,
) -> None:
    evaluation_started_at = time.perf_counter()
    set_seed_everywhere(seed)
    if balanced_success_target < 0 or balanced_failure_target < 0:
        raise ValueError("balanced_success_target and balanced_failure_target must be non-negative.")
    if max_episode_steps is not None and max_episode_steps <= 0:
        raise ValueError("max_episode_steps must be positive when provided.")
    if uq_adaptive_variance_floor < 0.0:
        raise ValueError("uq_adaptive_variance_floor must be non-negative.")
    uq_control_policy = VAMInference._validate_uq_control_policy(uq_control_policy)
    episode_manifest = load_episode_manifest(episode_manifest_path)
    risk_threshold_for_label = _risk_threshold_for_run_label(
        uq_control_policy,
        uq_risk_model_dir,
        uq_risk_threshold,
    )

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
            "calibrator_adaptive_horizon": "ctrlriskadap",
            "action_medoid_calibrator_adaptive_horizon": "ctrlmedriskadap",
            "action_medoid_calibrator_recovery": "ctrlrec",
            "lowest_risk_candidate_calibrator_horizon": "ctrllowriskcand",
            "risk_gated_action_medoid_horizon": "ctrlriskgatedmed",
            "world_action_medoid": "ctrlwmedoid",
            "world_lowest_v2w_variance": "ctrlwlowvar",
        }
        if uq_control_policy in {
            "calibrator_adaptive_horizon",
            "action_medoid_calibrator_adaptive_horizon",
            "action_medoid_calibrator_recovery",
            "lowest_risk_candidate_calibrator_horizon",
            "risk_gated_action_medoid_horizon",
        }:
            run_label = (
                f"{run_label}_{control_tags[uq_control_policy]}"
                f"_p{uq_risk_persistence}_mh{uq_risk_medium_execute_actions}_hh{uq_risk_high_execute_actions}"
                f"_rt{risk_threshold_for_label:g}_rmt{uq_risk_medium_threshold:g}"
            )
            if uq_control_policy == "action_medoid_calibrator_recovery":
                run_label = (
                    f"{run_label}_r{uq_recovery_steps}"
                    f"z{uq_recovery_delta_z:g}"
                    f"c{uq_recovery_cooldown_queries}"
                    f"m{uq_recovery_max_per_episode}"
                )
        else:
            run_label = (
                f"{run_label}_{control_tags[uq_control_policy]}"
                f"_min{uq_min_execute_actions}_z{uq_adaptive_spike_z:g}_vf{uq_adaptive_variance_floor:g}"
            )
    if run_suffix:
        run_label = f"{run_label}_{run_suffix}"
    rollout_dir = output_dir or Path("./results") / run_label / task_suite_name
    rollout_dir.mkdir(parents=True, exist_ok=True)
    completed_outcomes = read_completed_episode_outcomes(rollout_dir / "episode_outcomes.jsonl")
    completed_before_session = len(completed_outcomes)
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
        uq_risk_model_dir=uq_risk_model_dir,
        uq_risk_threshold=uq_risk_threshold,
        uq_risk_medium_threshold=uq_risk_medium_threshold,
        uq_risk_persistence=uq_risk_persistence,
        uq_risk_medium_execute_actions=uq_risk_medium_execute_actions,
        uq_risk_high_execute_actions=uq_risk_high_execute_actions,
        uq_recovery_steps=uq_recovery_steps,
        uq_recovery_delta_z=uq_recovery_delta_z,
        uq_recovery_gripper=uq_recovery_gripper,
        uq_recovery_cooldown_queries=uq_recovery_cooldown_queries,
        uq_recovery_max_per_episode=uq_recovery_max_per_episode,
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
    validate_episode_manifest_request(
        episode_manifest,
        task_suite_name,
        selected_task_ids,
        trial_start_index,
        num_trials_per_task,
    )

    rollout_started_at = time.perf_counter()

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
                total_episodes += 1
                if episode_manifest is not None and (task_id, trial_index) not in episode_manifest.pairs_by_suite[
                    task_suite_name
                ]:
                    continue

                if total_episodes % eval_world_size != eval_rank:
                    continue
                task_episodes += 1
                existing_outcome = completed_outcomes.get(total_episodes)
                if existing_outcome is not None:
                    validate_resume_outcome(existing_outcome, task_id, trial_index, task_description)
                    if bool(existing_outcome["success"]):
                        task_successes += 1
                    continue
                stale_episode_files = [
                    str(path)
                    for path in rollout_dir.iterdir()
                    if f"episode{total_episodes}_" in str(path)
                ]
                if stale_episode_files:
                    raise RuntimeError(
                        "Found episode artifacts without a matching episode_outcomes.jsonl row. "
                        "Use a fresh output directory or repair the outcome log before resuming: "
                        f"{stale_episode_files[:5]}"
                    )

                episode_started_at = time.perf_counter()
                env.seed(seed)
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
                policy.log_episode_outcome(
                    success,
                    replay_frames=len(replay_images),
                    wall_time_seconds=time.perf_counter() - episode_started_at,
                )
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

                completed_episode_count = target_successes + target_failures
                success_rate = total_successes / max(completed_episode_count, 1)
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

    completed_episode_count = target_successes + target_failures
    overall_success_rate = total_successes / max(completed_episode_count, 1)
    rollout_wall_seconds = time.perf_counter() - rollout_started_at
    total_wall_seconds = time.perf_counter() - evaluation_started_at
    setup_wall_seconds = total_wall_seconds - rollout_wall_seconds
    session_episode_count = completed_episode_count - completed_before_session
    if session_episode_count > 0:
        episodes_per_hour = 3600.0 * session_episode_count / rollout_wall_seconds
        projected_hours_200 = 200.0 / episodes_per_hour
        projected_hours_1000 = 1000.0 / episodes_per_hour
        runtime_projection_text = (
            f"Throughput: {episodes_per_hour:.2f} episodes/h | "
            f"Projected 200 episodes: {projected_hours_200:.2f} h | "
            f"Projected 1000 episodes: {projected_hours_1000:.2f} h"
        )
    else:
        episodes_per_hour = None
        projected_hours_200 = None
        projected_hours_1000 = None
        runtime_projection_text = "No new episodes were executed in this session"
    runtime_summary = {
        "completed_episodes": completed_episode_count,
        "successes": total_successes,
        "failures": target_failures,
        "session_new_episodes": session_episode_count,
        "setup_wall_seconds": setup_wall_seconds,
        "rollout_wall_seconds": rollout_wall_seconds,
        "total_wall_seconds": total_wall_seconds,
        "episodes_per_hour": episodes_per_hour,
        "projected_wall_hours_200_episodes": projected_hours_200,
        "projected_wall_hours_1000_episodes": projected_hours_1000,
    }
    (rollout_dir / "runtime_summary.json").write_text(
        json.dumps(runtime_summary, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Completed {completed_episode_count} episodes | "
        f"Total successes: {total_successes} | "
        f"Balanced raw successes: {target_successes} | "
        f"Balanced raw failures: {target_failures} | "
        f"Overall success rate: {overall_success_rate:.3f} | "
        f"Setup: {setup_wall_seconds / 3600.0:.2f} h | "
        f"Rollout: {rollout_wall_seconds / 3600.0:.2f} h | "
        f"Total: {total_wall_seconds / 3600.0:.2f} h | "
        f"{runtime_projection_text}\n"
    )


if __name__ == "__main__":
    tyro.cli(eval_vam_libero)
