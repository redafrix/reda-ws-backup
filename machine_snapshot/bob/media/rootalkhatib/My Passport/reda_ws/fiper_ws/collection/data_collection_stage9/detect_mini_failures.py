from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from .mini_failure_features import (
        PICK_PHASES,
        PLACE_PHASES,
        aggregate_window,
        append_jsonl,
        clamp,
        compute_features,
        iter_episode_dirs,
        load_episode,
        safe_float,
        summarize_features,
        write_json,
    )
except ImportError:  # pragma: no cover - supports direct script execution
    from mini_failure_features import (  # type: ignore
        PICK_PHASES,
        PLACE_PHASES,
        aggregate_window,
        append_jsonl,
        clamp,
        compute_features,
        iter_episode_dirs,
        load_episode,
        safe_float,
        summarize_features,
        write_json,
    )


DETECTOR_SCHEMA_VERSION = "stage9_mini_failure_detector_v1"
PICK_PLACE_RELATIONS = {"pick", "place_or_put"}
PLACE_RELATIONS = {"place_or_put"}
GENERIC_OBJECT_TOKENS = {
    "main", "body", "object", "visual", "collision", "geom", "root", "base",
    "handle", "lid", "top", "bottom", "left", "right", "front", "back",
}


def _phase_hit(window: dict[str, Any], phases: set[str]) -> bool:
    return any(str(p).upper() in phases for p in window.get("phases") or [])


def _recent_target_held(features: list[dict[str, Any]], start: int, lookback: int) -> float:
    prev = features[max(0, start - lookback): start]
    if not prev:
        return 0.0
    return sum(1 for f in prev if f.get("target_held_after")) / len(prev)


def _recent_phase_hit(features: list[dict[str, Any]], start: int, lookback: int, phases: set[str]) -> bool:
    prev = features[max(0, start - lookback): start]
    return any(str(f.get("phase") or "").upper() in phases for f in prev)


def _evidence_available(window: dict[str, Any]) -> float:
    available = 0
    total = 4
    if window.get("target_motion_total") is not None:
        available += 1
    if window.get("eef_motion_total") is not None:
        available += 1
    if window.get("target_height_delta_total") is not None:
        available += 1
    if window.get("target_to_goal_delta") is not None:
        available += 1
    return available / total


def _semantic_tokens(name: str | None) -> set[str]:
    if not name:
        return set()
    text = str(name).lower().replace("-", "_").replace(" ", "_")
    stop = {"main", "body", "geom", "collision", "visual"}
    return {tok for tok in text.split("_") if tok and not tok.isdigit() and tok not in stop}


def _same_semantic_family(a: str | None, b: str | None) -> bool:
    ta = _semantic_tokens(a)
    tb = _semantic_tokens(b)
    if not ta or not tb:
        return False
    shared = ta & tb
    distinctive = {tok for tok in shared if tok not in GENERIC_OBJECT_TOKENS}
    # Instance variants like alphabet_soup_1 / alphabet_soup_2, red_box_1 /
    # red_box_2, or black_bowl_1 / black_bowl_2 are the same semantic family.
    # Keep this object-agnostic; only generic body/component words are ignored.
    if len(distinctive) >= 2:
        return True
    return bool(len(distinctive) >= 1 and any(len(tok) >= 6 for tok in distinctive) and len(shared) >= 2)


def _task_relation(features: list[dict[str, Any]], start: int) -> str:
    if start >= len(features):
        return "unknown"
    return str(features[start].get("task_relation") or "").lower()


def _is_pick_or_place_task(features: list[dict[str, Any]], start: int) -> bool:
    return _task_relation(features, start) in PICK_PLACE_RELATIONS


def _is_place_task(features: list[dict[str, Any]], start: int) -> bool:
    return _task_relation(features, start) in PLACE_RELATIONS


def _same_family_motion_sum(window: dict[str, Any], target_base: str | None) -> float:
    total = 0.0
    for name, motion in (window.get("object_motion_sums") or {}).items():
        if _same_semantic_family(str(name), target_base):
            total += float(motion or 0.0)
    return total


def _vec(value: Any) -> tuple[float, float, float] | None:
    if value is None:
        return None
    try:
        vals = [float(x) for x in value[:3]]
    except Exception:
        return None
    if len(vals) < 3:
        return None
    return vals[0], vals[1], vals[2]


def _distance(a: tuple[float, float, float] | None, b: tuple[float, float, float] | None) -> float | None:
    if a is None or b is None:
        return None
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def _same_family_names(features: list[dict[str, Any]], start: int, end: int, target_base: str | None) -> list[str]:
    names: set[str] = set()
    for feature in features[max(0, start): min(len(features), end)]:
        for key in ["object_positions_before", "object_positions_after"]:
            for name in (feature.get(key) or {}):
                if _same_semantic_family(str(name), target_base):
                    names.add(str(name))
    return sorted(names)


def _object_pos(feature: dict[str, Any], name: str, after: bool = True) -> tuple[float, float, float] | None:
    key = "object_positions_after" if after else "object_positions_before"
    pos = (feature.get(key) or {}).get(name)
    return _vec(pos)


def _same_family_pick_stability(
    features: list[dict[str, Any]],
    start: int,
    args: argparse.Namespace,
) -> dict[str, Any]:
    if start >= len(features):
        return {"available": False}
    target_base = features[start].get("target_base")
    end = min(len(features), start + int(args.pick_confirmation_steps))
    names = _same_family_names(features, start, end, str(target_base) if target_base else None)
    best: dict[str, Any] = {
        "available": bool(names),
        "object": None,
        "stable_lift_success": False,
        "max_stable_lift_run": 0,
        "max_target_held_run": 0,
        "max_target_held_lift_run": 0,
        "max_height_gain": 0.0,
        "final_height_gain": 0.0,
        "motion_from_start": 0.0,
        "fell_after_lift": False,
    }
    for name in names:
        base = _object_pos(features[start], name, after=False) or _object_pos(features[start], name, after=True)
        if base is None:
            continue
        positions: list[tuple[int, tuple[float, float, float], tuple[float, float, float] | None]] = []
        for idx in range(start, end):
            pos = _object_pos(features[idx], name, after=True)
            eef = _vec(features[idx].get("eef_pos_after"))
            if pos is not None:
                positions.append((idx, pos, eef))
        if not positions:
            continue
        gains = [pos[2] - base[2] for _idx, pos, _eef in positions]
        max_gain = max(gains)
        final_gain = gains[-1]
        motion = max((_distance(base, pos) or 0.0) for _idx, pos, _eef in positions)
        stable_run = 0
        target_held_run = 0
        target_held_lift_run = 0
        max_run = 0
        max_target_held_run = 0
        max_target_held_lift_run = 0
        for idx, pos, eef in positions:
            near_eef = (_distance(pos, eef) or 999.0) <= args.stable_hold_eef_distance
            lifted = (pos[2] - base[2]) >= args.stable_lift_height
            feature = features[idx]
            target_held_hint = bool(feature.get("target_held_after")) and _same_semantic_family(name, str(feature.get("target_base") or target_base))
            if target_held_hint:
                target_held_run += 1
                max_target_held_run = max(max_target_held_run, target_held_run)
            else:
                target_held_run = 0
            if lifted and target_held_hint:
                target_held_lift_run += 1
                max_target_held_lift_run = max(max_target_held_lift_run, target_held_lift_run)
            else:
                target_held_lift_run = 0
            if lifted and (near_eef or target_held_hint):
                stable_run += 1
                max_run = max(max_run, stable_run)
            else:
                stable_run = 0
        fell_after_lift = max_gain >= args.stable_lift_height and final_gain < args.stable_lift_height * 0.50
        sustained_held_motion = max_target_held_run >= args.stable_lift_steps and motion >= args.same_semantic_motion_suppression
        stable_success = (max_run >= args.stable_lift_steps or sustained_held_motion) and not fell_after_lift
        score_tuple = (int(stable_success), max_run, max_target_held_run, max_target_held_lift_run, max_gain, motion)
        best_tuple = (
            int(bool(best["stable_lift_success"])),
            int(best["max_stable_lift_run"]),
            int(best["max_target_held_run"]),
            int(best["max_target_held_lift_run"]),
            float(best["max_height_gain"]),
            float(best["motion_from_start"]),
        )
        if score_tuple > best_tuple:
            best = {
                "available": True,
                "object": name,
                "stable_lift_success": stable_success,
                "max_stable_lift_run": int(max_run),
                "max_target_held_run": int(max_target_held_run),
                "max_target_held_lift_run": int(max_target_held_lift_run),
                "max_height_gain": float(max_gain),
                "final_height_gain": float(final_gain),
                "motion_from_start": float(motion),
                "fell_after_lift": bool(fell_after_lift),
                "checked_steps": int(end - start),
                "required_stable_lift_steps": int(args.stable_lift_steps),
                "stable_lift_height": float(args.stable_lift_height),
            }
    return best


def _pick_attempt_evidence(window: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    target_eef_min = safe_float(window.get("target_to_eef_min"))
    closing = float(window.get("gripper_closing_max") or 0.0)
    closed = bool(window.get("gripper_closed_any"))
    near_tight = target_eef_min is not None and target_eef_min <= args.tight_grasp_attempt_target_distance
    near_loose = target_eef_min is not None and target_eef_min <= args.grasp_attempt_target_distance
    eef_lift = safe_float(window.get("eef_height_delta_total"), 0.0) or 0.0
    return {
        "closed": closed,
        "closing_delta": closing,
        "near_tight": near_tight,
        "near_loose": near_loose,
        "target_to_eef_min": target_eef_min,
        "eef_lift": eef_lift,
        "attempt": bool(closed and near_loose and eef_lift >= args.lift_attempt_threshold and (closing >= args.close_delta or near_tight)),
    }


def _label_core_end(start: int, args: argparse.Namespace) -> int:
    return int(start + max(1, int(getattr(args, "core_label_steps", 10))) - 1)


def _base_event(
    *,
    episode_id: str,
    event_type: str,
    start: int,
    end: int,
    onset: int,
    severity: float,
    confidence: float,
    evidence: dict[str, Any],
    explanation: str,
    confirmation_start: int | None = None,
    confirmation_end: int | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": DETECTOR_SCHEMA_VERSION,
        "episode_id": episode_id,
        "event_type": event_type,
        "onset_step": int(onset),
        "core_start_step": int(start),
        "core_end_step": int(end),
        "severity": clamp(float(severity)),
        "confidence": clamp(float(confidence)),
        "evidence": evidence,
        "explanation": explanation,
        "confirmation_start_step": int(confirmation_start if confirmation_start is not None else start),
        "confirmation_end_step": int(confirmation_end if confirmation_end is not None else end),
    }


def detect_missed_pick(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_pick_or_place_task(features, start):
        return None
    if not _phase_hit(window, PICK_PHASES):
        return None
    attempt = _pick_attempt_evidence(window, args)
    target_eef_min = attempt["target_to_eef_min"]
    close = bool(attempt["attempt"])
    eef_lift = safe_float(window.get("eef_height_delta_total"), 0.0) or 0.0
    target_motion = safe_float(window.get("target_motion_total"), 0.0) or 0.0
    target_lift = safe_float(window.get("target_height_delta_total"), 0.0) or 0.0
    target_held_fraction = safe_float(window.get("target_held_fraction"), 0.0) or 0.0
    non_target_fraction = safe_float(window.get("non_target_held_fraction"), 0.0) or 0.0
    target_base = (features[start] if start < len(features) else {}).get("target_base")
    dominant = window.get("dominant_moving_object") or {}
    same_family_motion = _same_family_motion_sum(window, str(target_base) if target_base else None)
    stability = _same_family_pick_stability(features, start, args)
    if not close or eef_lift < args.lift_attempt_threshold:
        return None
    if non_target_fraction >= args.wrong_object_fraction:
        return None
    if target_eef_min is None or target_eef_min > args.grasp_attempt_target_distance:
        return None
    if stability.get("stable_lift_success"):
        return None
    if same_family_motion >= args.same_semantic_motion_suppression:
        return None
    if target_motion > args.missed_pick_target_motion_max or target_lift > args.missed_pick_target_lift_max:
        return None
    if target_held_fraction >= 0.25:
        return None
    lift_score = clamp((eef_lift - args.lift_attempt_threshold) / 0.08)
    static_score = clamp((args.missed_pick_target_motion_max - target_motion) / args.missed_pick_target_motion_max)
    severity = 0.62 + 0.20 * lift_score + 0.14 * static_score
    confidence = 0.55 + 0.25 * _evidence_available(window) + 0.15 * lift_score
    evidence = {
        "window": window,
        "detector": "close_plus_eef_lift_but_target_static",
        "close_evidence": close,
        "eef_lift": eef_lift,
        "target_motion_total": target_motion,
        "target_lift": target_lift,
        "target_held_fraction": target_held_fraction,
        "non_target_held_fraction": non_target_fraction,
        "target_to_eef_min": target_eef_min,
        "same_semantic_target_family_motion_sum": same_family_motion,
        "dominant_moving_object": dominant,
        "pick_stability": stability,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="missed_pick",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="gripper closed and EEF lifted, but target stayed static and was not held",
        confirmation_start=start,
        confirmation_end=start + int(window["len"]) - 1,
    )


def detect_unstable_pick_or_failed_lift(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_pick_or_place_task(features, start):
        return None
    if not _phase_hit(window, PICK_PHASES):
        return None
    attempt = _pick_attempt_evidence(window, args)
    if not attempt["attempt"]:
        return None
    target_base = (features[start] if start < len(features) else {}).get("target_base")
    stability = _same_family_pick_stability(features, start, args)
    if stability.get("stable_lift_success"):
        return None
    same_family_motion = _same_family_motion_sum(window, str(target_base) if target_base else None)
    max_gain = float(stability.get("max_height_gain") or 0.0)
    motion = float(stability.get("motion_from_start") or 0.0)
    moved_or_lifted = (
        same_family_motion >= args.same_semantic_motion_suppression
        or motion >= args.same_semantic_motion_suppression
        or max_gain >= args.unstable_lift_min_height
    )
    if not moved_or_lifted:
        return None
    severity = 0.60 + 0.16 * clamp((max_gain - args.unstable_lift_min_height) / 0.08) + 0.10 * clamp(motion / 0.12)
    if stability.get("fell_after_lift"):
        severity += 0.10
    confidence = 0.56 + 0.20 * _evidence_available(window) + 0.14 * clamp(float(stability.get("max_stable_lift_run") or 0.0) / max(1, args.stable_lift_steps))
    evidence = {
        "window": window,
        "detector": "pick_attempt_moved_same_family_object_but_no_stable_lift",
        "attempt": attempt,
        "same_semantic_target_family_motion_sum": same_family_motion,
        "pick_stability": stability,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="unstable_pick_or_failed_lift",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="object moved/lifted during a pick attempt but did not become a stable held object",
        confirmation_start=start,
        confirmation_end=min(len(features) - 1, start + int(args.pick_confirmation_steps) - 1),
    )


def detect_wrong_object_pick(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_pick_or_place_task(features, start):
        return None
    if not _phase_hit(window, PICK_PHASES | {"TRANSPORT"}):
        return None
    close = bool(window.get("gripper_closed_any")) or float(window.get("gripper_closing_max") or 0.0) >= args.close_delta
    non_target_fraction = safe_float(window.get("non_target_held_fraction"), 0.0) or 0.0
    target_motion = safe_float(window.get("target_motion_total"), 0.0) or 0.0
    object_motion_sums = window.get("object_motion_sums") or {}
    non_target_objects = [str(x) for x in (window.get("non_target_held_objects") or [])]
    target_base = (features[start] if start < len(features) else {}).get("target_base")
    non_target_objects = [obj for obj in non_target_objects if not _same_semantic_family(obj, str(target_base) if target_base else None)]
    non_target_motion = max([float(object_motion_sums.get(obj, 0.0) or 0.0) for obj in non_target_objects] or [0.0])
    eef_lift = safe_float(window.get("eef_height_delta_total"), 0.0) or 0.0
    if not close or non_target_fraction < args.wrong_object_fraction:
        return None
    if not non_target_objects:
        return None
    if target_motion > args.wrong_object_target_motion_max:
        return None
    if non_target_motion < args.wrong_object_motion_min:
        return None
    if eef_lift < args.lift_attempt_threshold:
        return None
    severity = 0.82 + 0.16 * clamp((non_target_fraction - args.wrong_object_fraction) / 0.50)
    confidence = 0.70 + 0.20 * _evidence_available(window)
    evidence = {
        "window": window,
        "detector": "non_target_object_held_while_target_static",
        "non_target_held_fraction": non_target_fraction,
        "non_target_held_objects": non_target_objects,
        "non_target_motion_sum": non_target_motion,
        "target_motion_total": target_motion,
        "eef_lift": eef_lift,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="wrong_object_picked",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="a non-target object appears held while the target remains static",
        confirmation_start=start,
        confirmation_end=start + int(window["len"]) - 1,
    )


def detect_drop_or_slip(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_pick_or_place_task(features, start):
        return None
    recent_held = _recent_target_held(features, start, args.held_lookback)
    held_here = safe_float(window.get("target_held_fraction"), 0.0) or 0.0
    if max(recent_held, held_here) < args.held_fraction_min:
        return None
    drop = safe_float(window.get("target_height_drop_total"), 0.0) or 0.0
    goal_after = safe_float(window.get("target_to_goal_after"))
    goal_delta = safe_float(window.get("target_to_goal_delta"), 0.0)
    landed_at_goal = goal_after is not None and goal_after <= args.goal_success_distance
    if drop < args.drop_height_threshold or landed_at_goal:
        return None
    contact_bad = int(window.get("target_bad_surface_contact_count") or 0)
    severity = 0.74 + 0.20 * clamp((drop - args.drop_height_threshold) / 0.12)
    confidence = 0.62 + 0.18 * _evidence_available(window) + 0.10 * clamp(recent_held + held_here)
    if contact_bad:
        confidence += 0.08
        severity += 0.04
    evidence = {
        "window": window,
        "detector": "target_was_held_then_height_dropped_without_goal_progress",
        "recent_target_held_fraction": recent_held,
        "held_fraction_in_window": held_here,
        "target_height_drop": drop,
        "target_to_goal_after": goal_after,
        "target_goal_delta": goal_delta,
        "target_bad_surface_contact_count": contact_bad,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="drop_or_slip",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="target was held recently, then dropped/slipped without meaningful goal progress",
        confirmation_start=start,
        confirmation_end=start + int(window["len"]) - 1,
    )


def detect_transport_entanglement(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_place_task(features, start):
        return None
    if not (_phase_hit(window, {"TRANSPORT", "PLACE_OR_GOAL"}) or _recent_phase_hit(features, start, args.held_lookback, {"TRANSPORT"})):
        return None
    recent_held = _recent_target_held(features, start, args.held_lookback)
    held_here = safe_float(window.get("target_held_fraction"), 0.0) or 0.0
    if max(recent_held, held_here) < args.held_fraction_min:
        return None
    other_contacts = int(window.get("target_other_object_contact_count") or 0)
    bad_contacts = int(window.get("target_bad_surface_contact_count") or 0)
    goal_delta = safe_float(window.get("target_to_goal_delta"), 0.0)
    target_motion = safe_float(window.get("target_motion_total"), 0.0) or 0.0
    no_progress = goal_delta is None or goal_delta > -args.weak_goal_progress
    if other_contacts < args.entanglement_contact_min or not no_progress:
        return None
    severity = 0.62 + 0.17 * clamp(other_contacts / 8.0) + 0.08 * clamp(target_motion / 0.10)
    confidence = 0.50 + 0.22 * _evidence_available(window) + 0.10 * clamp(recent_held + held_here)
    if bad_contacts:
        severity += 0.04
        confidence += 0.04
    evidence = {
        "window": window,
        "detector": "held_target_with_repeated_other_object_contacts_and_no_goal_progress",
        "recent_target_held_fraction": recent_held,
        "held_fraction_in_window": held_here,
        "target_other_object_contact_count": other_contacts,
        "target_bad_surface_contact_count": bad_contacts,
        "target_goal_delta": goal_delta,
        "target_motion_total": target_motion,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="transport_entanglement",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="held target repeatedly contacts other objects while failing to make goal progress",
        confirmation_start=start,
        confirmation_end=start + int(window["len"]) - 1,
    )


def detect_missed_place(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_place_task(features, start):
        return None
    if not (_phase_hit(window, PLACE_PHASES) or _recent_phase_hit(features, start, args.held_lookback, {"TRANSPORT"})):
        return None
    recent_held = _recent_target_held(features, start, args.held_lookback)
    if recent_held < args.held_fraction_min:
        return None
    opening = bool(window.get("gripper_open_any")) or float(window.get("gripper_opening_max") or 0.0) >= args.open_delta
    if not opening:
        return None
    goal_after = safe_float(window.get("target_to_goal_after"))
    goal_delta = safe_float(window.get("target_to_goal_delta"), 0.0)
    if goal_after is not None and goal_after <= args.goal_success_distance:
        return None
    if goal_delta is not None and goal_delta <= -args.strong_goal_progress:
        return None
    held_after = safe_float(window.get("target_held_fraction"), 0.0) or 0.0
    release_score = clamp((recent_held - held_after) / 0.60) if held_after < recent_held else 0.25
    severity = 0.66 + 0.18 * release_score
    confidence = 0.58 + 0.22 * _evidence_available(window) + 0.10 * clamp(recent_held)
    evidence = {
        "window": window,
        "detector": "release_after_transport_without_goal_success_or_goal_progress",
        "recent_target_held_fraction": recent_held,
        "held_fraction_in_window": held_after,
        "gripper_opening": opening,
        "target_to_goal_after": goal_after,
        "target_to_goal_delta": goal_delta,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="missed_place",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="target was released after transport but did not land within/closer to the goal",
        confirmation_start=start,
        confirmation_end=start + int(window["len"]) - 1,
    )


def detect_target_moved_away(
    episode_id: str,
    features: list[dict[str, Any]],
    start: int,
    window: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    if not _is_place_task(features, start):
        return None
    goal_delta = safe_float(window.get("target_to_goal_delta"))
    target_motion = safe_float(window.get("target_motion_total"), 0.0) or 0.0
    if goal_delta is None:
        return None
    if goal_delta < args.target_moved_away_threshold or target_motion < args.target_motion_min:
        return None
    if window.get("success_any"):
        return None

    # NEW: Strict conditions for RISKY labeling
    parse_conf = (features[start] if start < len(features) else {}).get("parse_confidence")
    recent_held = _recent_target_held(features, start, args.held_lookback)
    in_transport = _phase_hit(window, {"TRANSPORT", "PLACE_OR_GOAL"})
    target_to_goal_before = safe_float(window.get("target_to_goal_before"))
    not_already_at_goal = target_to_goal_before is not None and target_to_goal_before > args.goal_success_distance

    # Check if we should treat this as a Risky event or just Uncertain/Audit
    is_risky_candidate = (
        getattr(args, "enable_target_moved_away_risk", False)
        and parse_conf == "HIGH"
        and (recent_held >= args.held_fraction_min or in_transport)
        and not_already_at_goal
    )

    severity = 0.58 + 0.24 * clamp((goal_delta - args.target_moved_away_threshold) / 0.12)
    confidence = 0.55 + 0.25 * _evidence_available(window)

    if not is_risky_candidate:
        # Downgrade to Uncertain/Audit level
        severity = clamp(severity * 0.50, 0.40, 0.60)
        confidence = clamp(confidence * 0.60, 0.30, 0.50)

    evidence = {
        "window": window,
        "detector": "target_goal_distance_increased_with_target_motion",
        "target_to_goal_delta": goal_delta,
        "target_motion_total": target_motion,
        "strict_conditions_met": is_risky_candidate,
        "parse_confidence": parse_conf,
        "recent_target_held_fraction": recent_held,
        "in_transport_phase": in_transport,
        "target_to_goal_before": target_to_goal_before,
    }
    return _base_event(
        episode_id=episode_id,
        event_type="target_moved_away_from_goal",
        start=start,
        end=_label_core_end(start, args),
        onset=start,
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        explanation="target moved and its distance to the goal increased" if is_risky_candidate else "target moved away from goal (low confidence/non-transport)",
        confirmation_start=start,
        confirmation_end=start + int(window["len"]) - 1,
    )


def detect_events_for_episode(
    episode_id: str,
    features: list[dict[str, Any]],
    args: argparse.Namespace,
) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    detectors = [
        detect_wrong_object_pick,
        detect_missed_pick,
        detect_unstable_pick_or_failed_lift,
        detect_drop_or_slip,
        detect_transport_entanglement,
        detect_missed_place,
        detect_target_moved_away,
    ]
    for start in range(0, max(0, len(features) - args.event_window + 1), args.scan_stride):
        window = aggregate_window(features, start, start + args.event_window)
        if window.get("empty"):
            continue
        for detector in detectors:
            event = detector(episode_id, features, start, window, args)
            if event is not None:
                candidates.append(event)
    return nonmax_suppress_events(candidates, args)


def _overlaps(a: dict[str, Any], b: dict[str, Any], slack: int = 0) -> bool:
    return not (
        int(a["core_end_step"]) + slack < int(b["core_start_step"])
        or int(b["core_end_step"]) + slack < int(a["core_start_step"])
    )


def nonmax_suppress_events(events: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    ranked = sorted(
        events,
        key=lambda e: (float(e.get("severity", 0.0)) * float(e.get("confidence", 0.0)), float(e.get("severity", 0.0))),
        reverse=True,
    )
    kept: list[dict[str, Any]] = []
    for event in ranked:
        duplicate = False
        for old in kept:
            same_type = old.get("event_type") == event.get("event_type")
            if same_type and _overlaps(old, event, slack=args.nms_slack):
                duplicate = True
                break
        if not duplicate:
            kept.append(event)
    return sorted(kept, key=lambda e: (int(e["onset_step"]), str(e["event_type"])))


def _default_step_risk(feature: dict[str, Any]) -> tuple[float, float, str]:
    if feature.get("success_after") or float(feature.get("reward") or 0.0) > 0.0:
        return 0.04, 0.80, "success_or_reward"
    phase = str(feature.get("phase") or "").upper()
    goal_delta = safe_float(feature.get("target_to_goal_delta"))
    height_delta = safe_float(feature.get("target_height_delta"))
    eef_target_delta = safe_float(feature.get("target_to_eef_delta"))
    progress = False
    if goal_delta is not None and goal_delta < -0.008:
        progress = True
    if height_delta is not None and height_delta > 0.006 and phase in {"NEAR_GRASP", "GRASP_OR_LIFT"}:
        progress = True
    if eef_target_delta is not None and eef_target_delta < -0.008 and phase in PICK_PHASES:
        progress = True
    if progress:
        return 0.12, 0.55, "local_progress"
    if phase in {"APPROACH", "NEAR_GRASP"}:
        return 0.28, 0.35, "no_event_early_phase_uncertain"
    return 0.42, 0.30, "no_event_uncertain"


def label_steps_and_chunks(
    episode: dict[str, Any],
    features: list[dict[str, Any]],
    events: list[dict[str, Any]],
    args: argparse.Namespace,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    step_labels: list[dict[str, Any]] = []
    episode_summary = episode.get("summary") or {}
    episode_metadata = episode.get("metadata") or {}
    task_context = episode_metadata.get("task_context") or episode_summary.get("task_context") or {}
    episode_context = {
        "episode_success": episode_summary.get("episode_success"),
        "episode_failure": episode_summary.get("episode_failure"),
        "episode_timeout": episode_summary.get("episode_timeout"),
        "episode_steps": episode_summary.get("episode_steps"),
        "task_language": episode_metadata.get("task_language") or episode_summary.get("task_language"),
        "task_context": task_context,
    }
    event_by_step: dict[int, list[dict[str, Any]]] = {}
    for event in events:
        pre_start = max(0, int(event["onset_step"]) - args.pre_failure_steps)
        core_start = int(event["core_start_step"])
        core_end = int(event["core_end_step"])
        for step in range(pre_start, core_end + 1):
            event_by_step.setdefault(step, []).append(event)

    for feature in features:
        step = int(feature.get("env_step", 0))
        base_risk, base_conf, base_reason = _default_step_risk(feature)
        applied = event_by_step.get(step) or []
        risk = base_risk
        conf = base_conf
        event_refs: list[dict[str, Any]] = []
        for event in applied:
            onset = int(event["onset_step"])
            severity = float(event["severity"])
            ev_conf = float(event["confidence"])
            if step < onset:
                span = max(1, onset - max(0, onset - args.pre_failure_steps))
                proximity = 1.0 - ((onset - step) / span)
                multiplier = 0.45 + 0.35 * proximity
                role = "pre_failure"
            else:
                multiplier = 1.0
                role = "failure_core"
            event_risk = clamp(severity * multiplier)
            risk = max(risk, event_risk)
            conf = max(conf, ev_conf * (0.75 if role == "pre_failure" else 1.0))
            event_refs.append({
                "event_type": event["event_type"],
                "onset_step": event["onset_step"],
                "role": role,
                "event_severity": event["severity"],
                "event_confidence": event["confidence"],
            })
        step_labels.append({
            "schema_version": "stage9_mini_failure_step_label_v1",
            "episode_id": episode_id_from_episode(episode),
            "env_step": step,
            "parent_chunk_index": feature.get("parent_chunk_index"),
            "parent_chunk_position": feature.get("parent_chunk_position"),
            "risk_score": clamp(risk),
            "quality_score": clamp(1.0 - risk),
            "confidence": clamp(conf),
            "risk_bin": risk_bin(risk),
            "label_source": "mini_failure_event_detector" if event_refs else "default_no_event_scorer",
            "default_reason": base_reason,
            "events": event_refs,
            "phase": feature.get("phase"),
            "task_relation": feature.get("task_relation"),
            "parse_confidence": feature.get("parse_confidence"),
            "target_base": feature.get("target_base"),
            "goal_base": feature.get("goal_base"),
            "episode_context": episode_context,
            "paths": feature.get("paths") or {},
            "evidence": {
                "target_motion": feature.get("target_motion"),
                "target_height_delta": feature.get("target_height_delta"),
                "target_to_goal_delta": feature.get("target_to_goal_delta"),
                "target_to_eef_delta": feature.get("target_to_eef_delta"),
                "target_held_after": feature.get("target_held_after"),
                "held_object_after": feature.get("held_object_after"),
            },
            "action_env": feature.get("action_env"),
            "action_normalized": feature.get("action_normalized"),
        })

    by_chunk: dict[str, list[dict[str, Any]]] = {}
    for row in step_labels:
        idx = row.get("parent_chunk_index")
        if idx is None:
            idx = int(row["env_step"]) // args.chunk_size
        key = str(idx)
        by_chunk.setdefault(key, []).append(row)

    chunk_labels: list[dict[str, Any]] = []
    for chunk_key, rows in sorted(by_chunk.items(), key=lambda kv: int(kv[0])):
        risks = [float(r["risk_score"]) for r in rows]
        confs = [float(r["confidence"]) for r in rows]
        events_flat = [ev for r in rows for ev in (r.get("events") or [])]
        event_types = sorted(set(str(ev.get("event_type")) for ev in events_flat))
        max_idx = max(range(len(rows)), key=lambda i: risks[i])
        chunk_labels.append({
            "schema_version": "stage9_mini_failure_chunk_label_v1",
            "episode_id": episode_id_from_episode(episode),
            "chunk_index": int(chunk_key),
            "start_step": int(min(r["env_step"] for r in rows)),
            "end_step": int(max(r["env_step"] for r in rows)),
            "num_steps": len(rows),
            "risk_score": clamp(max(risks)),
            "risk_score_mean": float(sum(risks) / len(risks)),
            "quality_score": clamp(1.0 - max(risks)),
            "confidence": clamp(max(confs)),
            "risk_bin": risk_bin(max(risks)),
            "event_types": event_types,
            "events": events_flat,
            "peak_step": int(rows[max_idx]["env_step"]),
            "phase_counts": phase_counts(rows),
            "task_relation": rows[0].get("task_relation"),
            "parse_confidence": rows[0].get("parse_confidence"),
            "target_base": rows[0].get("target_base"),
            "goal_base": rows[0].get("goal_base"),
            "episode_context": episode_context,
            "paths": {
                "first": rows[0].get("paths") or {},
                "peak": rows[max_idx].get("paths") or {},
                "last": rows[-1].get("paths") or {},
            },
        })
    return step_labels, chunk_labels


def risk_bin(risk: float) -> str:
    if risk <= 0.20:
        return "SAFE_STRONG"
    if risk <= 0.40:
        return "SAFE_WEAK"
    if risk < 0.65:
        return "UNCERTAIN"
    if risk < 0.80:
        return "RISKY_WEAK"
    return "RISKY_STRONG"


def phase_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        phase = str(row.get("phase") or "UNKNOWN")
        counts[phase] = counts.get(phase, 0) + 1
    return counts


def episode_id_from_episode(episode: dict[str, Any]) -> str:
    meta = episode.get("metadata") or {}
    summary = episode.get("summary") or {}
    if meta.get("episode_id"):
        return str(meta["episode_id"])
    if summary.get("episode_id"):
        return str(summary["episode_id"])
    return Path(str(episode.get("episode_dir", "unknown"))).name


def summarize_run(events: list[dict[str, Any]], step_labels: list[dict[str, Any]], chunk_labels: list[dict[str, Any]]) -> dict[str, Any]:
    event_counts: dict[str, int] = {}
    step_bins: dict[str, int] = {}
    chunk_bins: dict[str, int] = {}
    for event in events:
        event_counts[str(event.get("event_type"))] = event_counts.get(str(event.get("event_type")), 0) + 1
    for row in step_labels:
        step_bins[str(row.get("risk_bin"))] = step_bins.get(str(row.get("risk_bin")), 0) + 1
    for row in chunk_labels:
        chunk_bins[str(row.get("risk_bin"))] = chunk_bins.get(str(row.get("risk_bin")), 0) + 1
    risky_chunks = [row for row in chunk_labels if float(row.get("risk_score", 0.0)) >= 0.65]
    return {
        "schema_version": "stage9_mini_failure_detection_summary_v1",
        "detector_schema_version": DETECTOR_SCHEMA_VERSION,
        "episodes": len(set(str(row.get("episode_id")) for row in step_labels)),
        "step_labels": len(step_labels),
        "chunk_labels": len(chunk_labels),
        "events": len(events),
        "event_counts": event_counts,
        "step_risk_bins": step_bins,
        "chunk_risk_bins": chunk_bins,
        "risky_chunk_count": len(risky_chunks),
        "risky_chunk_event_counts": event_counts_for_chunks(risky_chunks),
    }


def event_counts_for_chunks(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        for event_type in row.get("event_types") or []:
            counts[str(event_type)] = counts.get(str(event_type), 0) + 1
    return counts


def write_report(out_dir: Path, args: argparse.Namespace, summary: dict[str, Any], episode_summaries: list[dict[str, Any]]) -> None:
    lines = [
        "# Stage 9 Mini-Failure Detector Report",
        "",
        "This is a simulator-state event detector for local mini-failures. It does not use terminal episode failure as a label.",
        "",
        "## Inputs",
        "",
        f"- Raw root: `{args.raw_root}`",
        f"- Event window: `{args.event_window}` steps",
        f"- Pre-failure window: `{args.pre_failure_steps}` steps",
        f"- Chunk size: `{args.chunk_size}` steps",
        "",
        "## Summary",
        "",
        f"- Episodes processed: `{summary['episodes']}`",
        f"- Step labels: `{summary['step_labels']}`",
        f"- Chunk labels: `{summary['chunk_labels']}`",
        f"- Mini-failure events: `{summary['events']}`",
        f"- Risky chunks: `{summary['risky_chunk_count']}`",
        "",
        "## Event Counts",
        "",
        "```json",
        json.dumps(summary["event_counts"], indent=2, sort_keys=True),
        "```",
        "",
        "## Chunk Risk Bins",
        "",
        "```json",
        json.dumps(summary["chunk_risk_bins"], indent=2, sort_keys=True),
        "```",
        "",
        "## Episode Feature Summaries",
        "",
        "```json",
        json.dumps(episode_summaries, indent=2, sort_keys=True)[:12000],
        "```",
        "",
        "## Outputs",
        "",
        f"- Events: `{out_dir / 'mini_failure_events.jsonl'}`",
        f"- Step labels: `{out_dir / 'mini_failure_step_labels.jsonl'}`",
        f"- Chunk labels: `{out_dir / 'mini_failure_chunk_labels.jsonl'}`",
        f"- Summary: `{out_dir / 'mini_failure_summary.json'}`",
    ]
    (out_dir / "STAGE9_MINI_FAILURE_DETECTION_REPORT.md").write_text("\n".join(lines) + "\n")


def run(args: argparse.Namespace) -> dict[str, Any]:
    raw_root = Path(args.raw_root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in ["mini_failure_events.jsonl", "mini_failure_step_labels.jsonl", "mini_failure_chunk_labels.jsonl"]:
        path = out_dir / name
        if path.exists():
            path.unlink()

    all_events: list[dict[str, Any]] = []
    all_step_labels: list[dict[str, Any]] = []
    all_chunk_labels: list[dict[str, Any]] = []
    episode_feature_summaries: list[dict[str, Any]] = []

    for episode_dir in iter_episode_dirs(raw_root):
        episode = load_episode(episode_dir)
        episode_id = episode_id_from_episode(episode)
        features = compute_features(episode)
        events = detect_events_for_episode(episode_id, features, args)
        step_labels, chunk_labels = label_steps_and_chunks(episode, features, events, args)

        feature_summary = summarize_features(features)
        feature_summary.update({
            "episode_id": episode_id,
            "episode_dir": str(episode_dir),
            "events": len(events),
            "chunks": len(chunk_labels),
            "risky_chunks": sum(1 for row in chunk_labels if float(row.get("risk_score", 0.0)) >= 0.65),
        })
        episode_feature_summaries.append(feature_summary)

        append_jsonl(out_dir / "mini_failure_events.jsonl", events)
        append_jsonl(out_dir / "mini_failure_step_labels.jsonl", step_labels)
        append_jsonl(out_dir / "mini_failure_chunk_labels.jsonl", chunk_labels)

        all_events.extend(events)
        all_step_labels.extend(step_labels)
        all_chunk_labels.extend(chunk_labels)

    summary = summarize_run(all_events, all_step_labels, all_chunk_labels)
    summary.update({
        "raw_root": str(raw_root),
        "out_dir": str(out_dir),
        "episode_feature_summaries": episode_feature_summaries,
        "config": vars(args),
    })
    write_json(out_dir / "mini_failure_summary.json", summary)
    write_report(out_dir, args, summary, episode_feature_summaries)
    return summary


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--event-window", type=int, default=20)
    parser.add_argument("--scan-stride", type=int, default=1)
    parser.add_argument("--chunk-size", type=int, default=10)
    parser.add_argument("--pre-failure-steps", type=int, default=60)
    parser.add_argument("--core-label-steps", type=int, default=10)
    parser.add_argument("--held-lookback", type=int, default=20)
    parser.add_argument("--nms-slack", type=int, default=4)
    parser.add_argument("--close-delta", type=float, default=0.008)
    parser.add_argument("--open-delta", type=float, default=0.008)
    parser.add_argument("--lift-attempt-threshold", type=float, default=0.025)
    parser.add_argument("--grasp-attempt-target-distance", type=float, default=0.085)
    parser.add_argument("--tight-grasp-attempt-target-distance", type=float, default=0.055)
    parser.add_argument("--pick-confirmation-steps", type=int, default=60)
    parser.add_argument("--stable-lift-steps", type=int, default=30)
    parser.add_argument("--stable-lift-height", type=float, default=0.030)
    parser.add_argument("--unstable-lift-min-height", type=float, default=0.012)
    parser.add_argument("--stable-hold-eef-distance", type=float, default=0.095)
    parser.add_argument("--missed-pick-target-motion-max", type=float, default=0.018)
    parser.add_argument("--missed-pick-target-lift-max", type=float, default=0.015)
    parser.add_argument("--wrong-object-fraction", type=float, default=0.25)
    parser.add_argument("--wrong-object-target-motion-max", type=float, default=0.025)
    parser.add_argument("--wrong-object-motion-min", type=float, default=0.035)
    parser.add_argument("--same-semantic-motion-suppression", type=float, default=0.030)
    parser.add_argument("--held-fraction-min", type=float, default=0.20)
    parser.add_argument("--drop-height-threshold", type=float, default=0.035)
    parser.add_argument("--strong-goal-progress", type=float, default=0.030)
    parser.add_argument("--weak-goal-progress", type=float, default=0.010)
    parser.add_argument("--goal-success-distance", type=float, default=0.120)
    parser.add_argument("--entanglement-contact-min", type=int, default=2)
    parser.add_argument("--target-moved-away-threshold", type=float, default=0.030)
    parser.add_argument("--target-motion-min", type=float, default=0.018)
    parser.add_argument("--enable-target-moved-away-risk", action="store_true", default=False)
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    summary = run(args)
    print(json.dumps(summary, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
