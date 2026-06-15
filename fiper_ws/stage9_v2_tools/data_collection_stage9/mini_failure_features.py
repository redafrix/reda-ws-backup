from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


FEATURE_SCHEMA_VERSION = "stage9_mini_failure_features_v1"

PICK_PHASES = {"APPROACH", "NEAR_GRASP", "GRASP_OR_LIFT", "APPROACH_OR_NEAR_GRASP"}
PLACE_PHASES = {"TRANSPORT", "PLACE_OR_GOAL", "GRASP_OR_LIFT"}
BAD_CONTACT_TOKENS = ("table", "floor", "wall", "counter", "arena")
ROBOT_CONTACT_TOKENS = ("robot", "gripper", "finger", "eef", "wrist", "hand")


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    if value != value:
        return lo
    return max(lo, min(hi, value))


def safe_float(value: Any, default: float | None = None) -> float | None:
    if value is None:
        return default
    try:
        out = float(value)
    except (TypeError, ValueError):
        return default
    if math.isnan(out):
        return default
    return out


def safe_vec(value: Any) -> np.ndarray | None:
    if value is None:
        return None
    try:
        arr = np.asarray(value, dtype=float).reshape(-1)
    except Exception:
        return None
    if arr.size < 3 or np.any(~np.isfinite(arr[:3])):
        return None
    return arr[:3]


def vec_list(value: np.ndarray | None) -> list[float] | None:
    if value is None:
        return None
    return [float(x) for x in np.asarray(value, dtype=float).reshape(-1).tolist()]


def object_positions_payload(objects: dict[str, Any]) -> dict[str, list[float]]:
    out: dict[str, list[float]] = {}
    for name, value in (objects or {}).items():
        pos = safe_vec(value)
        if pos is not None:
            out[str(name)] = vec_list(pos) or []
    return out


def dist(a: np.ndarray | None, b: np.ndarray | None) -> float | None:
    if a is None or b is None:
        return None
    return float(np.linalg.norm(a - b))


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def iter_episode_dirs(root: Path) -> list[Path]:
    """Return raw episode dirs that contain Stage 9 `steps.jsonl` files."""
    roots = [root]
    if (root / "episodes").exists():
        roots.append(root / "episodes")
    out: list[Path] = []
    for candidate_root in roots:
        if not candidate_root.exists():
            continue
        for path in sorted(candidate_root.rglob("steps.jsonl")):
            out.append(path.parent)
    return sorted(set(out))


def load_episode(episode_dir: Path) -> dict[str, Any]:
    metadata = load_json(episode_dir / "episode_metadata.json")
    summary = load_json(episode_dir / "summary.json")
    steps = load_jsonl(episode_dir / "steps.jsonl")
    return {
        "episode_dir": str(episode_dir),
        "metadata": metadata,
        "summary": summary,
        "steps": steps,
    }


def _npz_signal(path: str | None, keys: tuple[str, ...]) -> dict[str, Any]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    out: dict[str, Any] = {}
    try:
        with np.load(p, allow_pickle=False) as data:
            for key in keys:
                if key in data:
                    out[key] = np.asarray(data[key], dtype=float)
    except Exception:
        return {}
    return out


def obs_signal(path: str | None, object_bases: list[str]) -> dict[str, Any]:
    keys = ["robot0_eef_pos", "robot0_gripper_qpos"]
    keys.extend(f"{base}_pos" for base in object_bases if base)
    return _npz_signal(path, tuple(keys))


def base_tokens(name: str | None) -> set[str]:
    if not name:
        return set()
    text = str(name).lower().replace("-", "_").replace(" ", "_")
    return {tok for tok in text.split("_") if tok and not tok.isdigit()}


def object_position(
    objects: dict[str, Any],
    obs: dict[str, Any],
    base: str | None,
    prefix: str | None = None,
) -> tuple[str | None, np.ndarray | None]:
    if not base and not prefix:
        return None, None
    candidates = [x for x in [base, prefix] if x]
    for cand in candidates:
        key = f"{cand}_pos"
        if key in obs:
            return str(cand), safe_vec(obs[key])
        if cand in objects:
            return str(cand), safe_vec(objects[cand])

    lower_candidates = [str(x).lower() for x in candidates]
    for name, value in objects.items():
        low = str(name).lower()
        if any(low.startswith(cand) for cand in lower_candidates):
            return str(name), safe_vec(value)

    query_tokens = set()
    for cand in candidates:
        query_tokens |= base_tokens(cand)
    best: tuple[int, str, np.ndarray] | None = None
    for name, value in objects.items():
        toks = base_tokens(name)
        shared = len(query_tokens & toks)
        pos = safe_vec(value)
        if shared > 0 and pos is not None:
            item = (shared, str(name), pos)
            if best is None or item[0] > best[0]:
                best = item
    if best is not None:
        return best[1], best[2]
    return None, None


def gripper_scalar(qpos: Any) -> float | None:
    if qpos is None:
        return None
    try:
        arr = np.asarray(qpos, dtype=float).reshape(-1)
    except Exception:
        return None
    if arr.size == 0:
        return None
    return float(np.mean(np.abs(arr)))


def is_gripper_closed(value: float | None) -> bool:
    return value is not None and value <= 0.018


def is_gripper_open(value: float | None) -> bool:
    return value is not None and value >= 0.030


def contact_pairs(summary: dict[str, Any] | None) -> list[tuple[str, str]]:
    if not isinstance(summary, dict):
        return []
    out: list[tuple[str, str]] = []
    for pair in summary.get("contacts") or []:
        if isinstance(pair, (list, tuple)) and len(pair) >= 2:
            out.append((str(pair[0] or ""), str(pair[1] or "")))
    return out


def contact_mentions_object(pair: tuple[str, str], object_name: str | None) -> bool:
    if not object_name:
        return False
    object_toks = base_tokens(object_name)
    pair_text = " ".join(pair).lower().replace("-", "_")
    if str(object_name).lower() in pair_text:
        return True
    return bool(object_toks and any(tok in pair_text for tok in object_toks))


def contact_kind_for_object(summary: dict[str, Any] | None, object_name: str | None) -> dict[str, Any]:
    pairs = contact_pairs(summary)
    related = [pair for pair in pairs if contact_mentions_object(pair, object_name)]
    related_text = [" ".join(pair).lower() for pair in related]
    bad_surface = sum(1 for text in related_text if any(tok in text for tok in BAD_CONTACT_TOKENS))
    robot = sum(1 for text in related_text if any(tok in text for tok in ROBOT_CONTACT_TOKENS))
    other_object = max(0, len(related) - bad_surface - robot)
    return {
        "all_contact_count": int((summary or {}).get("contact_count") or len(pairs)),
        "object_contact_count": len(related),
        "object_bad_surface_contact_count": bad_surface,
        "object_robot_contact_count": robot,
        "object_other_object_contact_count": other_object,
        "object_contact_pairs": [list(pair) for pair in related[:10]],
    }


def moving_objects(
    before_objects: dict[str, Any],
    after_objects: dict[str, Any],
    min_motion: float = 0.006,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name, before in before_objects.items():
        if name not in after_objects:
            continue
        bp = safe_vec(before)
        ap = safe_vec(after_objects.get(name))
        if bp is None or ap is None:
            continue
        motion = float(np.linalg.norm(ap - bp))
        if motion >= min_motion:
            rows.append({
                "object": str(name),
                "motion": motion,
                "height_delta": float(ap[2] - bp[2]),
                "before": vec_list(bp),
                "after": vec_list(ap),
            })
    rows.sort(key=lambda r: float(r["motion"]), reverse=True)
    return rows


def nearest_object_to_eef(
    objects: dict[str, Any],
    eef: np.ndarray | None,
    exclude_tokens: tuple[str, ...] = (),
) -> dict[str, Any] | None:
    if eef is None:
        return None
    best: tuple[float, str, np.ndarray] | None = None
    for name, value in objects.items():
        low = str(name).lower()
        if any(tok in low for tok in exclude_tokens):
            continue
        pos = safe_vec(value)
        if pos is None:
            continue
        d = float(np.linalg.norm(pos - eef))
        if best is None or d < best[0]:
            best = (d, str(name), pos)
    if best is None:
        return None
    return {"object": best[1], "distance": best[0], "position": vec_list(best[2])}


def _same_object(name: str | None, target_name: str | None, target_base: str | None) -> bool:
    if not name:
        return False
    low = str(name).lower()
    if target_name and low == str(target_name).lower():
        return True
    if target_base and low.startswith(str(target_base).lower()):
        return True
    target_toks = base_tokens(target_name) | base_tokens(target_base)
    return bool(target_toks and target_toks.issubset(base_tokens(name)))


def step_feature(row: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    task_context = metadata.get("task_context") or row.get("task_context") or {}
    target_base = task_context.get("target_base")
    target_prefix = task_context.get("target_body_prefix") or target_base
    goal_base = task_context.get("goal_base")
    goal_prefix = task_context.get("goal_body_prefix") or goal_base
    object_bases = [x for x in [target_base, target_prefix, goal_base, goal_prefix] if x]

    paths = row.get("paths") or {}
    before_obs = obs_signal(paths.get("before_obs_npz"), object_bases)
    after_obs = obs_signal(paths.get("after_obs_npz"), object_bases)
    before_objects = row.get("before_object_positions") or {}
    after_objects = row.get("after_object_positions") or {}
    target_name_b, target_b = object_position(before_objects, before_obs, target_base, target_prefix)
    target_name_a, target_a = object_position(after_objects, after_obs, target_base, target_prefix)
    goal_name_b, goal_b = object_position(before_objects, before_obs, goal_base, goal_prefix)
    goal_name_a, goal_a = object_position(after_objects, after_obs, goal_base, goal_prefix)
    eef_b = safe_vec(before_obs.get("robot0_eef_pos"))
    eef_a = safe_vec(after_obs.get("robot0_eef_pos"))
    grip_b = gripper_scalar(before_obs.get("robot0_gripper_qpos"))
    grip_a = gripper_scalar(after_obs.get("robot0_gripper_qpos"))
    nearest_a = nearest_object_to_eef(after_objects, eef_a)
    nearest_b = nearest_object_to_eef(before_objects, eef_b)
    moves = moving_objects(before_objects, after_objects)
    target_motion = dist(target_b, target_a)
    eef_motion = dist(eef_b, eef_a)
    target_eef_b = dist(target_b, eef_b)
    target_eef_a = dist(target_a, eef_a)
    target_goal_b = dist(target_b, goal_b) if target_base != goal_base else None
    target_goal_a = dist(target_a, goal_a) if target_base != goal_base else None
    closed_a = is_gripper_closed(grip_a)
    closed_b = is_gripper_closed(grip_b)
    open_a = is_gripper_open(grip_a)
    open_b = is_gripper_open(grip_b)

    near_target_a = target_eef_a is not None and target_eef_a <= 0.055
    target_contact = contact_kind_for_object(row.get("after_contact"), target_name_a or target_name_b or target_base)
    held_candidate = nearest_a if nearest_a and nearest_a.get("distance", 1.0) <= 0.060 and closed_a else None
    held_name = str(held_candidate["object"]) if held_candidate else None
    target_held = bool(closed_a and near_target_a)
    non_target_held = bool(held_name and not _same_object(held_name, target_name_a or target_name_b, target_base))

    return {
        "schema_version": FEATURE_SCHEMA_VERSION,
        "episode_id": row.get("episode_id") or metadata.get("episode_id"),
        "env_step": int(row.get("env_step", 0)),
        "phase": str(row.get("phase_before") or "UNKNOWN"),
        "parent_chunk_index": row.get("parent_chunk_index"),
        "parent_chunk_position": row.get("parent_chunk_position"),
        "reward": safe_float(row.get("reward"), 0.0) or 0.0,
        "done": bool(row.get("done")),
        "success_before": bool(row.get("success_before")),
        "success_after": bool(row.get("success_after")),
        "target_base": target_base,
        "goal_base": goal_base,
        "task_relation": task_context.get("relation"),
        "parse_confidence": task_context.get("parse_confidence"),
        "target_name_before": target_name_b,
        "target_name_after": target_name_a,
        "goal_name_before": goal_name_b,
        "goal_name_after": goal_name_a,
        "target_pos_before": vec_list(target_b),
        "target_pos_after": vec_list(target_a),
        "goal_pos_before": vec_list(goal_b),
        "goal_pos_after": vec_list(goal_a),
        "eef_pos_before": vec_list(eef_b),
        "eef_pos_after": vec_list(eef_a),
        "gripper_before": grip_b,
        "gripper_after": grip_a,
        "gripper_closed_before": closed_b,
        "gripper_closed_after": closed_a,
        "gripper_open_before": open_b,
        "gripper_open_after": open_a,
        "gripper_closing_delta": (grip_b - grip_a) if grip_b is not None and grip_a is not None else None,
        "gripper_opening_delta": (grip_a - grip_b) if grip_b is not None and grip_a is not None else None,
        "target_motion": target_motion,
        "target_height_delta": float(target_a[2] - target_b[2]) if target_b is not None and target_a is not None else None,
        "target_height_drop": float(target_b[2] - target_a[2]) if target_b is not None and target_a is not None else None,
        "eef_motion": eef_motion,
        "eef_height_delta": float(eef_a[2] - eef_b[2]) if eef_b is not None and eef_a is not None else None,
        "target_to_eef_before": target_eef_b,
        "target_to_eef_after": target_eef_a,
        "target_to_eef_delta": (target_eef_a - target_eef_b) if target_eef_a is not None and target_eef_b is not None else None,
        "target_to_goal_before": target_goal_b,
        "target_to_goal_after": target_goal_a,
        "target_to_goal_delta": (target_goal_a - target_goal_b) if target_goal_a is not None and target_goal_b is not None else None,
        "target_held_after": target_held,
        "nearest_object_before": nearest_b,
        "nearest_object_after": nearest_a,
        "held_object_after": held_name,
        "non_target_held_after": non_target_held,
        "moving_objects": moves[:10],
        "dominant_moving_object": moves[0] if moves else None,
        "after_contact": row.get("after_contact") or {},
        "target_contact": target_contact,
        "object_positions_before": object_positions_payload(before_objects),
        "object_positions_after": object_positions_payload(after_objects),
        "paths": paths,
        "action_env": row.get("action_env"),
        "action_normalized": row.get("action_normalized"),
    }


def compute_features(episode: dict[str, Any]) -> list[dict[str, Any]]:
    metadata = dict(episode.get("metadata") or {})
    if not metadata.get("task_context"):
        metadata["task_context"] = (episode.get("summary") or {}).get("task_context") or {}
    return [step_feature(row, metadata) for row in episode.get("steps") or []]


def feature_pos(feature: dict[str, Any], key: str) -> np.ndarray | None:
    return safe_vec(feature.get(key))


def aggregate_window(features: list[dict[str, Any]], start: int, end: int) -> dict[str, Any]:
    window = features[max(0, start): max(0, end)]
    if not window:
        return {"empty": True}
    first = window[0]
    last = window[-1]
    target_start = feature_pos(first, "target_pos_before")
    target_end = feature_pos(last, "target_pos_after")
    eef_start = feature_pos(first, "eef_pos_before")
    eef_end = feature_pos(last, "eef_pos_after")
    goal_start = feature_pos(first, "goal_pos_before")
    goal_end = feature_pos(last, "goal_pos_after")
    target_motion_total = dist(target_start, target_end)
    eef_motion_total = dist(eef_start, eef_end)
    target_height_delta = float(target_end[2] - target_start[2]) if target_start is not None and target_end is not None else None
    eef_height_delta = float(eef_end[2] - eef_start[2]) if eef_start is not None and eef_end is not None else None
    target_goal_before = dist(target_start, goal_start) if target_start is not None and goal_start is not None else None
    target_goal_after = dist(target_end, goal_end) if target_end is not None and goal_end is not None else None
    held_steps = sum(1 for f in window if f.get("target_held_after"))
    non_target_held = [f.get("held_object_after") for f in window if f.get("non_target_held_after")]
    phases = sorted(set(str(f.get("phase") or "UNKNOWN") for f in window))
    moving: dict[str, float] = {}
    for f in window:
        for obj in f.get("moving_objects") or []:
            name = str(obj.get("object"))
            moving[name] = moving.get(name, 0.0) + float(obj.get("motion") or 0.0)
    dominant_moving = None
    if moving:
        name = max(moving, key=lambda k: moving[k])
        dominant_moving = {"object": name, "motion_sum": moving[name]}
    target_contact_bad = sum(int((f.get("target_contact") or {}).get("object_bad_surface_contact_count") or 0) for f in window)
    target_contact_other = sum(int((f.get("target_contact") or {}).get("object_other_object_contact_count") or 0) for f in window)
    eef_target_distances = [
        x
        for f in window
        for x in [safe_float(f.get("target_to_eef_before")), safe_float(f.get("target_to_eef_after"))]
        if x is not None
    ]
    return {
        "empty": False,
        "start_step": int(first.get("env_step", start)),
        "end_step": int(last.get("env_step", end - 1)),
        "len": len(window),
        "phases": phases,
        "reward_sum": float(sum(float(f.get("reward") or 0.0) for f in window)),
        "success_any": any(bool(f.get("success_after")) for f in window),
        "done_any": any(bool(f.get("done")) for f in window),
        "gripper_closed_any": any(bool(f.get("gripper_closed_after")) for f in window),
        "gripper_open_any": any(bool(f.get("gripper_open_after")) for f in window),
        "gripper_closing_max": max([safe_float(f.get("gripper_closing_delta"), 0.0) or 0.0 for f in window] or [0.0]),
        "gripper_opening_max": max([safe_float(f.get("gripper_opening_delta"), 0.0) or 0.0 for f in window] or [0.0]),
        "target_held_fraction": held_steps / max(1, len(window)),
        "non_target_held_fraction": len(non_target_held) / max(1, len(window)),
        "non_target_held_objects": sorted(set(str(x) for x in non_target_held if x)),
        "object_motion_sums": moving,
        "target_motion_total": target_motion_total,
        "target_height_delta_total": target_height_delta,
        "target_height_drop_total": -target_height_delta if target_height_delta is not None else None,
        "eef_motion_total": eef_motion_total,
        "eef_height_delta_total": eef_height_delta,
        "target_to_goal_before": target_goal_before,
        "target_to_goal_after": target_goal_after,
        "target_to_goal_delta": (target_goal_after - target_goal_before) if target_goal_after is not None and target_goal_before is not None else None,
        "target_to_eef_min": min(eef_target_distances) if eef_target_distances else None,
        "dominant_moving_object": dominant_moving,
        "target_bad_surface_contact_count": target_contact_bad,
        "target_other_object_contact_count": target_contact_other,
        "first_paths": first.get("paths") or {},
        "last_paths": last.get("paths") or {},
    }


def summarize_features(features: list[dict[str, Any]]) -> dict[str, Any]:
    phases: dict[str, int] = {}
    held = 0
    non_target_held = 0
    target_motion_values = []
    goal_delta_values = []
    for f in features:
        phase = str(f.get("phase") or "UNKNOWN")
        phases[phase] = phases.get(phase, 0) + 1
        held += int(bool(f.get("target_held_after")))
        non_target_held += int(bool(f.get("non_target_held_after")))
        if f.get("target_motion") is not None:
            target_motion_values.append(float(f["target_motion"]))
        if f.get("target_to_goal_delta") is not None:
            goal_delta_values.append(float(f["target_to_goal_delta"]))
    return {
        "feature_schema_version": FEATURE_SCHEMA_VERSION,
        "steps": len(features),
        "phase_counts": phases,
        "target_held_steps": held,
        "non_target_held_steps": non_target_held,
        "target_motion_total_stepwise": float(sum(target_motion_values)) if target_motion_values else None,
        "target_goal_delta_sum_stepwise": float(sum(goal_delta_values)) if goal_delta_values else None,
    }
