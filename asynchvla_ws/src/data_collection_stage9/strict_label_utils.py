from __future__ import annotations

import csv
import json
import math
import os
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


LABEL_GOOD_STRONG = "GOOD_STRONG"
LABEL_GOOD_WEAK = "GOOD_WEAK"
LABEL_BAD = "BAD"
LABEL_VALIDATED_BAD = "VALIDATED_BAD"
LABEL_AMBIGUOUS = "AMBIGUOUS"

VALIDATED_BAD = "VALIDATED_BAD"
DOWNGRADE_TO_AMBIGUOUS = "DOWNGRADE_TO_AMBIGUOUS"
NEEDS_MANUAL_REVIEW = "NEEDS_MANUAL_REVIEW"
INVALID_BAD = "INVALID_BAD"

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
STAGE9_ROOT = REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data"

STRONG_BAD_REASONS = {
    "target_object_dropped",
    "large_object_height_drop",
    "target_object_moved_away_from_goal",
    "gripper_lost_or_released_target",
    "gripper_lost_object",
    "confident_bad_contact",
    "bad_collision",
    "unstable_state",
    "done_bad",
    "unrecoverable_done_bad",
    "no_progress_strong",
    "zero_reward_no_eef_target_or_goal_progress",
}

EEF_AWAY_REASON = "eef_moved_away_from_target_during_approach"


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    rows = []
    with p.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: str | Path, data: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def write_csv(path: str | Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        keys = []
        seen = set()
        for row in rows:
            for key in row:
                if key not in seen:
                    seen.add(key)
                    keys.append(key)
        fieldnames = keys
    with p.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def resolve_workspace_path(path: str | Path | None, dataset_dir: str | Path | None = None) -> Path | None:
    if not path:
        return None
    p = Path(path)
    if p.is_absolute():
        return p
    if str(p).startswith("asynchvla_ws/"):
        return REDA_WS / p
    if dataset_dir:
        candidate = Path(dataset_dir) / p
        if candidate.exists():
            return candidate
    return REDA_WS / p


def dataset_jsonl_path(data_dir: str | Path) -> Path:
    p = resolve_workspace_path(data_dir)
    if p is None:
        raise ValueError("missing data_dir")
    if p.is_file():
        return p
    return p / "counterfactual_samples.jsonl"


def dataset_name_from_path(data_dir: str | Path) -> str:
    p = Path(str(data_dir).rstrip("/"))
    if p.name == "counterfactual_samples.jsonl":
        return p.parent.name
    return p.name


def sample_label(sample: dict[str, Any]) -> str | None:
    label = sample.get("label")
    if isinstance(label, dict):
        return label.get("label")
    return label


def sample_reasons(sample: dict[str, Any]) -> list[str]:
    label = sample.get("label") or {}
    if not isinstance(label, dict):
        return []
    reasons = label.get("bad_evidence") or label.get("label_reasons") or []
    if isinstance(reasons, str):
        reasons = [reasons]
    return [str(x) for x in reasons if x is not None]


def bad_event_type(sample: dict[str, Any]) -> str | None:
    label = sample.get("label") or {}
    if not isinstance(label, dict):
        return None
    value = label.get("bad_event_type")
    if value in ("", "None"):
        return None
    return value


def evidence(sample: dict[str, Any]) -> dict[str, Any]:
    label = sample.get("label") or {}
    if isinstance(label, dict) and isinstance(label.get("numeric_evidence"), dict):
        out = dict(label["numeric_evidence"])
    else:
        out = {}
    outcome = sample.get("outcome") or {}
    delta = outcome.get("delta") or {}
    task = delta.get("task_progress") or {}

    for key, value in {
        "reward_sum_H": outcome.get("reward_sum_H"),
        "nonzero_reward_count_H": outcome.get("nonzero_reward_count_H"),
        "success_within_H": outcome.get("success_within_H"),
        "success_after": outcome.get("success_after"),
        "done_within_H": outcome.get("done_within_H"),
        "eef_delta": delta.get("eef_delta"),
        "object_delta_max": delta.get("object_delta_max"),
        "height_drop_max": delta.get("height_drop_max"),
    }.items():
        if out.get(key) is None and value is not None:
            out[key] = value
    for key, value in task.items():
        if out.get(key) is None and value is not None:
            out[key] = value

    out["success"] = bool(
        out.get("success")
        or out.get("success_within_H")
        or out.get("success_after")
        or outcome.get("success_within_H")
        or outcome.get("success_after")
    )
    return out


def as_float(value: Any, default: float | None = None) -> float | None:
    if value is None:
        return default
    try:
        value = float(value)
    except (TypeError, ValueError):
        return default
    if math.isnan(value):
        return default
    return value


def as_bool(value: Any) -> bool:
    return bool(value) if value is not None else False


def parent_episode_id(sample: dict[str, Any]) -> str:
    meta = sample.get("metadata") or {}
    state_id = str(meta.get("state_id") or sample.get("sample_id") or "unknown")
    return re.sub(r"_s\d+_state.*$", "", state_id)


def state_id(sample: dict[str, Any]) -> str:
    return str((sample.get("metadata") or {}).get("state_id") or sample.get("sample_id") or "unknown")


def sample_uid(sample: dict[str, Any]) -> str:
    return f"{sample.get('_dataset_name') or 'unknown_dataset'}:{sample.get('sample_id')}"


def state_group_key(sample: dict[str, Any]) -> str:
    return f"{sample.get('_dataset_name') or 'unknown_dataset'}:{state_id(sample)}"


def parent_phase(sample: dict[str, Any]) -> str:
    meta = sample.get("metadata") or {}
    label = sample.get("label") or {}
    if isinstance(label, dict) and label.get("parent_phase"):
        return str(label.get("parent_phase"))
    return str(meta.get("parent_phase") or "UNKNOWN")


def seed(sample: dict[str, Any]) -> Any:
    return (sample.get("metadata") or {}).get("simvla_generation_seed")


def parent_context(sample: dict[str, Any]) -> dict[str, Any]:
    meta = sample.get("metadata") or {}
    label = sample.get("label") or {}
    if not isinstance(label, dict):
        label = {}
    parent_steps = label.get("parent_episode_steps")
    step = meta.get("parent_step_index")
    try:
        parent_steps_int = int(parent_steps) if parent_steps is not None else None
        step_int = int(step) if step is not None else None
    except (TypeError, ValueError):
        parent_steps_int = None
        step_int = None
    distance = None
    if parent_steps_int is not None and step_int is not None:
        distance = max(0, parent_steps_int - step_int)
    rewards = []
    for h in sample.get("history") or []:
        if isinstance(h, dict) and h.get("reward") is not None:
            try:
                rewards.append(float(h.get("reward")))
            except (TypeError, ValueError):
                pass
    return {
        "parent_episode_id": parent_episode_id(sample),
        "parent_episode_success": label.get("parent_episode_success"),
        "parent_failed_or_timeout": label.get("parent_failed_or_timeout"),
        "parent_episode_steps": parent_steps_int,
        "parent_phase": parent_phase(sample),
        "parent_step_index": step_int,
        "distance_to_failure_or_timeout_steps": distance,
        "state_before_parent_failure_or_timeout": bool(label.get("parent_failed_or_timeout")) if label.get("parent_failed_or_timeout") is not None else None,
        "history_reward_sum": sum(rewards) if rewards else 0.0,
        "history_rewards_tail": rewards[-8:],
    }


def strong_good_signals(e: dict[str, Any]) -> list[str]:
    reasons = []
    goal_delta = as_float(e.get("target_to_goal_delta"))
    motion = as_float(e.get("target_motion"))
    height_delta = as_float(e.get("target_height_delta"))
    if as_bool(e.get("success")):
        reasons.append("success_within_horizon")
    if goal_delta is not None and goal_delta < -0.025:
        reasons.append("target_object_closer_to_goal")
    if height_delta is not None and height_delta > 0.025 and motion is not None and motion > 0.012:
        reasons.append("target_object_lifted")
    if motion is not None and motion > 0.045 and goal_delta is not None and goal_delta < -0.010:
        reasons.append("target_object_moved_correct_direction")
    return reasons


def weak_good_signals(e: dict[str, Any]) -> list[str]:
    reasons = []
    target_eef_delta = as_float(e.get("target_to_eef_delta"))
    motion = as_float(e.get("target_motion"))
    goal_delta = as_float(e.get("target_to_goal_delta"))
    phase = str(e.get("phase") or "").lower()
    if phase in {"approach", "near_grasp"} and target_eef_delta is not None and target_eef_delta < -0.020:
        reasons.append("eef_closer_to_target_before_grasp")
    if as_bool(e.get("gripper_closed_near_target")):
        reasons.append("gripper_closed_near_target")
    if motion is not None and 0.010 <= motion <= 0.045 and (goal_delta is None or goal_delta <= 0.010):
        reasons.append("small_target_motion_not_strong")
    return reasons


def strong_bad_signals(e: dict[str, Any]) -> list[str]:
    reasons = []
    target_drop = as_float(e.get("target_height_drop"))
    global_drop = as_float(e.get("height_drop_max"))
    goal_delta = as_float(e.get("target_to_goal_delta"))
    motion = as_float(e.get("target_motion"))
    target_eef_delta = as_float(e.get("target_to_eef_delta"))
    eef_delta = as_float(e.get("eef_delta"))
    if target_drop is not None and target_drop > 0.10:
        reasons.append("target_object_dropped")
    if global_drop is not None and global_drop > 0.18:
        reasons.append("large_object_height_drop")
    if goal_delta is not None and goal_delta > 0.06 and motion is not None and motion > 0.02:
        reasons.append("target_object_moved_away_from_goal")
    if as_bool(e.get("gripper_opened_near_target")) and target_drop is not None and target_drop > 0.04:
        reasons.append("gripper_lost_or_released_target")
    if as_bool(e.get("bad_contact_confident")):
        reasons.append("confident_bad_contact")
    if as_bool(e.get("unstable_state")):
        reasons.append("unstable_state")
    no_eef = eef_delta is not None and eef_delta < 0.008
    no_target_motion = motion is not None and motion < 0.003
    no_goal_progress = goal_delta is None or goal_delta > -0.003
    no_target_approach = target_eef_delta is None or target_eef_delta > -0.003
    if int(e.get("nonzero_reward_count_H") or 0) == 0 and no_eef and no_target_motion and no_goal_progress and no_target_approach:
        reasons.append("no_progress_strong")
    return reasons


def quality_score(sample: dict[str, Any]) -> float:
    e = evidence(sample)
    score = 0.0
    reward = as_float(e.get("reward_sum_H"), 0.0) or 0.0
    score += 20.0 * reward
    if as_bool(e.get("success")):
        score += 100.0
    goal_delta = as_float(e.get("target_to_goal_delta"))
    if goal_delta is not None:
        score += max(-50.0, min(50.0, -400.0 * goal_delta))
    height_delta = as_float(e.get("target_height_delta"))
    if height_delta is not None:
        score += max(-30.0, min(30.0, 300.0 * height_delta))
    target_eef_delta = as_float(e.get("target_to_eef_delta"))
    if target_eef_delta is not None:
        score += max(-12.0, min(12.0, -120.0 * target_eef_delta))
    target_drop = as_float(e.get("target_height_drop"))
    if target_drop is not None and target_drop > 0:
        score -= min(80.0, 450.0 * target_drop)
    if "no_progress_strong" in strong_bad_signals(e) or "zero_reward_no_eef_target_or_goal_progress" in strong_bad_signals(e):
        score -= 15.0
    return score


def same_state_summary(sample: dict[str, Any], siblings: list[dict[str, Any]]) -> dict[str, Any]:
    sid = sample.get("sample_id")
    candidate_score = quality_score(sample)
    rows = []
    for sibling in siblings:
        se = evidence(sibling)
        rows.append({
            "sample_id": sibling.get("sample_id"),
            "seed": seed(sibling),
            "label": sample_label(sibling),
            "quality_score": quality_score(sibling),
            "reward_sum_H": as_float(se.get("reward_sum_H"), 0.0),
            "success": as_bool(se.get("success")),
            "strong_good": strong_good_signals(se),
            "strong_bad": strong_bad_signals(se),
            "bad_reasons": sample_reasons(sibling) if sample_label(sibling) == LABEL_BAD else [],
        })
    rows.sort(key=lambda x: x["quality_score"], reverse=True)
    scores = [r["quality_score"] for r in rows]
    best = max(scores) if scores else candidate_score
    worst = min(scores) if scores else candidate_score
    better = [r for r in rows if r["sample_id"] != sid and r["quality_score"] >= candidate_score + 8.0]
    successful_alt = [r for r in rows if r["sample_id"] != sid and (r["success"] or r["reward_sum_H"] and r["reward_sum_H"] > 0)]
    strong_good_alt = [r for r in rows if r["sample_id"] != sid and r["strong_good"]]
    candidate_rank = next((idx + 1 for idx, r in enumerate(rows) if r["sample_id"] == sid), None)
    return {
        "state_id": state_id(sample),
        "num_siblings": len(siblings),
        "candidate_quality_score": candidate_score,
        "best_quality_score": best,
        "worst_quality_score": worst,
        "candidate_rank_1_is_best": candidate_rank,
        "has_better_real_seed": bool(better),
        "has_successful_alternative": bool(successful_alt),
        "has_strong_good_alternative": bool(strong_good_alt),
        "candidate_is_bottom_half": bool(candidate_rank is not None and candidate_rank > max(1, len(rows) // 2)),
        "top_siblings": rows[:8],
    }


def anti_false_bad_checks(sample: dict[str, Any]) -> dict[str, Any]:
    e = evidence(sample)
    reasons = sample_reasons(sample)
    strong_good = strong_good_signals(e)
    strong_bad = strong_bad_signals(e)
    parent = parent_context(sample)
    bad_reason_unknown = not reasons or any(r in {"unknown", "None", "null"} for r in reasons)
    eef_only = reasons == [EEF_AWAY_REASON] or (set(reasons) == {EEF_AWAY_REASON})
    parent_phase_value = str(parent.get("parent_phase") or "").upper()
    parse_conf = str(e.get("parse_confidence") or "").upper()
    target_confident = bool(e.get("target_base") and e.get("target_pos_available") and parse_conf not in {"", "LOW"})
    target_eef_delta = as_float(e.get("target_to_eef_delta"))
    reward = as_float(e.get("reward_sum_H"), 0.0) or 0.0
    target_motion = as_float(e.get("target_motion"), 0.0) or 0.0
    goal_delta = as_float(e.get("target_to_goal_delta"))
    target_height_delta = as_float(e.get("target_height_delta"))
    strong_target_progress = bool(strong_good)
    object_toward_goal = bool(goal_delta is not None and goal_delta < -0.025)
    lifted_or_placed = bool(
        (target_height_delta is not None and target_height_delta > 0.025)
        or as_bool(e.get("success"))
        or object_toward_goal
    )
    eef_phase_ok = parent_phase_value in {"APPROACH", "NEAR_GRASP"}
    eef_threshold_ok = target_eef_delta is not None and target_eef_delta > 0.045
    no_positive_local_outcome = not as_bool(e.get("success")) and reward <= 0 and not strong_target_progress and target_motion < 0.010
    return {
        "success_within_H": as_bool(e.get("success")),
        "strong_good_evidence": strong_good,
        "strong_bad_evidence_recomputed": strong_bad,
        "bad_reason_unknown": bad_reason_unknown,
        "bad_reason_only_eef_away": eef_only,
        "parent_phase_requires_approach": eef_phase_ok,
        "target_confident": target_confident,
        "eef_away_threshold_ok": eef_threshold_ok,
        "no_positive_local_outcome": no_positive_local_outcome,
        "strong_target_progress": strong_target_progress,
        "object_moves_toward_goal_strongly": object_toward_goal,
        "object_lifted_or_placed_correctly": lifted_or_placed,
        "tiny_bad_evidence": bool(eef_only and (not eef_threshold_ok or not no_positive_local_outcome)),
    }


def replay_summary_ok(replay: dict[str, Any] | None, required: bool) -> tuple[bool, str]:
    if not required:
        return True, "not_required"
    if not replay:
        return False, "missing_replay"
    attempts = replay.get("attempts") or []
    if not attempts:
        return False, "missing_replay"
    usable = [a for a in attempts if a.get("status") == "ok"]
    if not usable:
        return False, "missing_usable_replay"
    hard_errors = [a for a in attempts if a.get("status") not in {"ok", "not_available_saved_action_too_short"}]
    if hard_errors:
        return False, "replay_error"
    labels = [a.get("label", {}).get("label") for a in usable]
    if not labels or any(label != LABEL_BAD for label in labels):
        return False, "replay_not_bad"
    reason_sets = [set(a.get("label", {}).get("bad_evidence") or a.get("label", {}).get("label_reasons") or []) for a in usable]
    original = set(replay.get("original_bad_reasons") or [])
    if original and any(not (rs & original) for rs in reason_sets):
        return False, "replay_reason_mismatch"
    return True, "replay_confirmed"


def validate_bad_sample(
    sample: dict[str, Any],
    siblings: list[dict[str, Any]],
    replay: dict[str, Any] | None = None,
    require_replay: bool = False,
) -> dict[str, Any]:
    reasons = sample_reasons(sample)
    e = evidence(sample)
    anti = anti_false_bad_checks(sample)
    same = same_state_summary(sample, siblings)
    replay_ok, replay_status = replay_summary_ok(replay, require_replay)
    failures = []

    if sample_label(sample) != LABEL_BAD:
        failures.append("original_label_not_bad")
    if anti["success_within_H"]:
        failures.append("success_within_H_true")
    if anti["strong_target_progress"]:
        failures.append("strong_target_progress_present")
    if anti["object_moves_toward_goal_strongly"]:
        failures.append("object_moves_toward_goal_strongly")
    if anti["object_lifted_or_placed_correctly"]:
        failures.append("object_lifted_or_placed_correctly")
    if anti["bad_reason_unknown"]:
        failures.append("bad_reason_unknown")
    if not reasons:
        failures.append("missing_bad_reason")

    has_strong_reason = any(r in STRONG_BAD_REASONS for r in reasons)
    has_eef_reason = EEF_AWAY_REASON in reasons
    if not has_strong_reason and not has_eef_reason:
        failures.append("no_allowed_strong_bad_reason")

    if has_eef_reason and set(reasons) == {EEF_AWAY_REASON}:
        if not anti["parent_phase_requires_approach"]:
            failures.append("eef_away_parent_phase_not_approach_or_near_grasp")
        if not anti["target_confident"]:
            failures.append("eef_away_target_not_confident")
        if not anti["eef_away_threshold_ok"]:
            failures.append("eef_away_below_threshold")
        if not anti["no_positive_local_outcome"]:
            failures.append("eef_away_has_positive_local_outcome")
        if not same["has_better_real_seed"]:
            failures.append("eef_away_no_better_same_state_real_seed")
        if not replay_ok:
            failures.append(replay_status)

    if has_strong_reason and not same["has_better_real_seed"]:
        if not ({"target_object_dropped", "large_object_height_drop", "unstable_state", "confident_bad_contact"} & set(reasons)):
            failures.append("bad_not_worse_than_same_state_alternatives")

    if require_replay and not replay_ok and not any(f.startswith("replay") or f == "missing_replay" for f in failures):
        failures.append(replay_status)

    invalid_failures = {
        "success_within_H_true",
        "strong_target_progress_present",
        "object_moves_toward_goal_strongly",
        "object_lifted_or_placed_correctly",
        "bad_reason_unknown",
        "eef_away_parent_phase_not_approach_or_near_grasp",
        "eef_away_no_better_same_state_real_seed",
    }
    if failures:
        status = INVALID_BAD if any(f in invalid_failures for f in failures) else DOWNGRADE_TO_AMBIGUOUS
        corrected = LABEL_AMBIGUOUS
    elif not replay_ok:
        status = NEEDS_MANUAL_REVIEW
        corrected = LABEL_AMBIGUOUS
    else:
        status = VALIDATED_BAD
        corrected = LABEL_BAD

    return {
        "sample_uid": sample_uid(sample),
        "sample_id": sample.get("sample_id"),
        "dataset": sample.get("_dataset_name"),
        "state_id": state_id(sample),
        "seed": seed(sample),
        "original_label": sample_label(sample),
        "original_bad_reasons": reasons,
        "original_bad_event_type": bad_event_type(sample),
        "validation_status": status,
        "corrected_label_suggestion": corrected,
        "failure_reasons": failures,
        "anti_false_bad_checks": anti,
        "parent_context": parent_context(sample),
        "same_state_comparison": same,
        "replay_status": replay_status,
        "replay": replay,
        "numeric_evidence": e,
    }


def group_by_state(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[state_group_key(row)].append(row)
    return groups


def load_datasets(data_dirs: list[str | Path]) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    all_rows = []
    by_dataset = {}
    for data_dir in data_dirs:
        name = dataset_name_from_path(data_dir)
        p = dataset_jsonl_path(data_dir)
        rows = load_jsonl(p)
        for row in rows:
            row["_dataset_name"] = name
            row["_dataset_dir"] = str(p.parent)
        by_dataset[name] = rows
        all_rows.extend(rows)
    return all_rows, by_dataset


def label_distribution(rows: list[dict[str, Any]]) -> dict[str, int]:
    return dict(Counter(sample_label(r) for r in rows))


def reason_distribution(rows: list[dict[str, Any]]) -> dict[str, int]:
    counter = Counter()
    for row in rows:
        if sample_label(row) == LABEL_BAD:
            reasons = sample_reasons(row)
            counter["+".join(reasons) if reasons else "unknown"] += 1
    return dict(counter)


def copy_if_exists(src: Path | None, dst: Path) -> str | None:
    if not src or not src.exists():
        return None
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return str(dst)
