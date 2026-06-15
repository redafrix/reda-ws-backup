from __future__ import annotations

import math
from collections import Counter
from typing import Any


SCORE_VERSION = "stage9_continuous_risk_v3_dense_metric"

RISK_SAFE_STRONG = "SAFE_STRONG"
RISK_SAFE_WEAK = "SAFE_WEAK"
RISK_UNCERTAIN = "UNCERTAIN"
RISK_RISKY_WEAK = "RISKY_WEAK"
RISK_RISKY_STRONG = "RISKY_STRONG"

LEGACY_GOOD_STRONG = "GOOD_STRONG"
LEGACY_GOOD_WEAK = "GOOD_WEAK"
LEGACY_VALIDATED_BAD = "VALIDATED_BAD"
LEGACY_AMBIGUOUS = "AMBIGUOUS"

BAD_SUBTYPE_ACTION_SPECIFIC = "action_specific"
BAD_SUBTYPE_STATE_CONTEXT = "state_context"
BAD_SUBTYPE_UNKNOWN = "unknown"


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    if value != value:
        return lo
    return max(lo, min(hi, value))


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


def sample_label(sample: dict[str, Any]) -> str:
    label = sample.get("label")
    if isinstance(label, dict):
        return str(label.get("final_label") or label.get("label") or "")
    return str(label or "")


def state_id(sample: dict[str, Any]) -> str:
    meta = sample.get("metadata") or {}
    return str(meta.get("state_id") or sample.get("state_id") or sample.get("sample_id") or "unknown")


def seed(sample: dict[str, Any]) -> Any:
    meta = sample.get("metadata") or {}
    return meta.get("simvla_generation_seed", meta.get("seed", sample.get("seed")))


def parent_phase(sample: dict[str, Any]) -> str:
    meta = sample.get("metadata") or {}
    label = sample.get("label") or {}
    if isinstance(label, dict) and label.get("parent_phase"):
        return str(label.get("parent_phase"))
    return str(meta.get("parent_phase") or meta.get("phase") or sample.get("phase") or "UNKNOWN")


def _raw_label(sample: dict[str, Any]) -> dict[str, Any]:
    label = sample.get("label") or {}
    if isinstance(sample.get("raw_local_label"), dict):
        return sample["raw_local_label"]
    if isinstance(label, dict) and isinstance(label.get("raw_local_label"), dict):
        return label["raw_local_label"]
    return {}


def merged_numeric_evidence(sample: dict[str, Any]) -> dict[str, Any]:
    """Collect all local, non-terminal metrics used by the continuous scorer."""
    out: dict[str, Any] = {}
    raw = _raw_label(sample)
    if isinstance(raw.get("numeric_evidence"), dict):
        out.update(raw["numeric_evidence"])

    outcome = sample.get("outcome") or {}
    delta = outcome.get("delta") or {}
    task = delta.get("task_progress") or {}
    trace = outcome.get("horizon_trace") or {}
    initial = trace.get("initial") or {}
    final = trace.get("final") or {}

    local_values = {
        "reward_sum_H": outcome.get("reward_sum_H"),
        "nonzero_reward_count_H": outcome.get("nonzero_reward_count_H"),
        "success_within_H": outcome.get("success_within_H"),
        "success_after": outcome.get("success_after"),
        "done_within_H": outcome.get("done_within_H"),
        "steps_executed": outcome.get("steps_executed"),
        "H_used": outcome.get("H_used"),
        "eef_delta": delta.get("eef_delta"),
        "object_delta_max": delta.get("object_delta_max"),
        "height_drop_max": delta.get("height_drop_max"),
    }
    for key, value in local_values.items():
        if out.get(key) is None and value is not None:
            out[key] = value
    for key, value in task.items():
        if out.get(key) is None and value is not None:
            out[key] = value

    if out.get("target_height_drop") is None and out.get("target_height_delta") is not None:
        out["target_height_drop"] = -as_float(out.get("target_height_delta"), 0.0)
    if out.get("target_to_goal_before") is None:
        out["target_to_goal_before"] = initial.get("object_goal_distance")
    if out.get("target_to_goal_after") is None:
        out["target_to_goal_after"] = final.get("object_goal_distance")
    if out.get("target_to_goal_delta") is None:
        b = as_float(out.get("target_to_goal_before"))
        a = as_float(out.get("target_to_goal_after"))
        if b is not None and a is not None:
            out["target_to_goal_delta"] = a - b
    if out.get("target_to_eef_before") is None:
        out["target_to_eef_before"] = initial.get("eef_target_distance")
    if out.get("target_to_eef_after") is None:
        out["target_to_eef_after"] = final.get("eef_target_distance")
    if out.get("target_to_eef_delta") is None:
        b = as_float(out.get("target_to_eef_before"))
        a = as_float(out.get("target_to_eef_after"))
        if b is not None and a is not None:
            out["target_to_eef_delta"] = a - b

    out["success"] = bool(
        out.get("success")
        or out.get("success_within_H")
        or out.get("success_after")
    )
    out["phase"] = str(out.get("phase") or parent_phase(sample))
    out["local_trace_len"] = len(trace.get("rewards") or [])
    out["terminal_success_audit_only"] = outcome.get("terminal_success")
    out["terminal_failure_audit_only"] = outcome.get("terminal_failure")
    out["terminal_timeout_audit_only"] = outcome.get("terminal_timeout")
    return out


def _goal_progress(e: dict[str, Any]) -> float:
    delta = as_float(e.get("target_to_goal_delta"))
    if delta is None:
        return 0.0
    return clamp(-delta / 0.08)


def _goal_worsening(e: dict[str, Any]) -> float:
    delta = as_float(e.get("target_to_goal_delta"))
    motion = as_float(e.get("target_motion"), 0.0) or 0.0
    if delta is None or motion < 0.010:
        return 0.0
    return clamp((delta - 0.015) / 0.10)


def _lift_progress(e: dict[str, Any]) -> float:
    delta = as_float(e.get("target_height_delta"))
    if delta is None:
        return 0.0
    return clamp(delta / 0.08)


def _approach_progress(e: dict[str, Any]) -> float:
    phase = str(e.get("phase") or "").upper()
    if phase not in {"APPROACH", "NEAR_GRASP", "APPROACH_OR_NEAR_GRASP"}:
        return 0.0
    delta = as_float(e.get("target_to_eef_delta"))
    if delta is None:
        return 0.0
    return clamp(-delta / 0.05)


def _motion_credits(e: dict[str, Any]) -> dict[str, float]:
    """Continuous diagnostic credits used to avoid scorer plateaus.

    These are not labels by themselves. They expose small but real simulator
    differences between same-state seeds so dense mining can tell apart
    "all candidates are identical" from "the old thresholds hid variation".
    """
    eef_delta = as_float(e.get("eef_delta"))
    target_motion = as_float(e.get("target_motion"))
    goal_delta = as_float(e.get("target_to_goal_delta"))
    target_eef_delta = as_float(e.get("target_to_eef_delta"))
    height_delta = as_float(e.get("target_height_delta"))
    return {
        "eef_motion_credit": clamp((eef_delta or 0.0) / 0.10) if eef_delta is not None else 0.0,
        "target_motion_credit": clamp((target_motion or 0.0) / 0.06) if target_motion is not None else 0.0,
        "goal_progress_credit": clamp(-(goal_delta or 0.0) / 0.08) if goal_delta is not None else 0.0,
        "goal_worsening_credit": clamp((goal_delta or 0.0) / 0.08) if goal_delta is not None else 0.0,
        "eef_approach_credit": clamp(-(target_eef_delta or 0.0) / 0.05) if target_eef_delta is not None else 0.0,
        "eef_away_credit": clamp((target_eef_delta or 0.0) / 0.08) if target_eef_delta is not None else 0.0,
        "lift_credit": clamp((height_delta or 0.0) / 0.08) if height_delta is not None else 0.0,
        "height_drop_credit": clamp(-(height_delta or 0.0) / 0.10) if height_delta is not None else 0.0,
    }


def _drop_risk(e: dict[str, Any], goal_progress: float) -> float:
    drop = as_float(e.get("target_height_drop"))
    if drop is None:
        drop = as_float(e.get("height_drop_max"))
    if drop is None:
        return 0.0
    risk = clamp((drop - 0.035) / 0.12)
    goal_after = as_float(e.get("target_to_goal_after"))
    placed_or_moved_to_goal = goal_progress >= 0.55 or (goal_after is not None and goal_after <= 0.12)
    if placed_or_moved_to_goal:
        risk *= 0.20
    return risk


def _lost_grasp_risk(e: dict[str, Any], drop_risk: float, goal_progress: float) -> float:
    target_eef_delta = as_float(e.get("target_to_eef_delta"))
    target_motion = as_float(e.get("target_motion"), 0.0) or 0.0
    if target_eef_delta is None:
        return 0.0
    if goal_progress >= 0.55:
        return 0.0
    # Moving far away from the target while the target drops is strong lost-grasp
    # evidence. EEF-away by itself is never enough.
    if target_eef_delta > 0.06 and (drop_risk > 0.35 or target_motion > 0.04):
        return clamp((target_eef_delta - 0.04) / 0.12)
    return 0.0


def _no_progress_risk(e: dict[str, Any], progress_credit: float) -> float:
    if as_bool(e.get("success")):
        return 0.0
    reward = as_float(e.get("reward_sum_H"), 0.0) or 0.0
    if reward > 0 or progress_credit >= 0.35:
        return 0.0

    phase = str(e.get("phase") or "").upper()
    motion = _motion_credits(e)
    approach_relevant = phase in {"APPROACH", "NEAR_GRASP", "APPROACH_OR_NEAR_GRASP"}
    approach_credit = motion["eef_approach_credit"] if approach_relevant else 0.0
    target_work = max(
        motion["target_motion_credit"],
        motion["goal_progress_credit"],
        motion["lift_credit"],
        approach_credit,
        progress_credit,
    )
    # EEF motion alone is weak. In manipulation/transport/place phases it must
    # not hide no-progress just because the arm moved around while the object
    # stayed still.
    diagnostic_motion = max(target_work, 0.20 * motion["eef_motion_credit"])
    if phase in {
        "GRASP_OR_LIFT",
        "TRANSPORT",
        "PLACE_OR_GOAL",
        "STUCK_OR_NO_PROGRESS",
        "TRANSPORT_OR_PLACE",
    }:
        expected_weight = 1.0
    elif phase in {"NEAR_GRASP", "APPROACH", "APPROACH_OR_NEAR_GRASP"}:
        expected_weight = 0.70
    else:
        expected_weight = 0.55
    if phase == "STUCK_OR_NO_PROGRESS":
        expected_weight = 1.05

    stall = 1.0 - diagnostic_motion
    # Worsening goal/EEF relation should keep no-progress risk high even when
    # there is motion. This matters for failure-onset scans.
    worsening = max(motion["goal_worsening_credit"], 0.50 * motion["eef_away_credit"])
    return clamp(expected_weight * stall + 0.20 * worsening)


def _evidence_confidence(e: dict[str, Any], positive: list[str], negative: list[str]) -> float:
    conf = 0.20
    if e.get("target_pos_available") or e.get("target_base"):
        conf += 0.16
    if e.get("goal_pos_available") or e.get("goal_base"):
        conf += 0.12
    if int(e.get("local_trace_len") or 0) > 0:
        conf += 0.12
    if as_float(e.get("target_motion")) is not None:
        conf += 0.08
    if as_float(e.get("target_to_goal_delta")) is not None:
        conf += 0.10
    if as_float(e.get("target_to_eef_delta")) is not None:
        conf += 0.06
    if positive or negative:
        conf += 0.10
    if len(negative) >= 2 or len(positive) >= 2:
        conf += 0.07
    return clamp(conf)


def risk_bin(risk_score: float) -> str:
    if risk_score <= 0.20:
        return RISK_SAFE_STRONG
    if risk_score <= 0.40:
        return RISK_SAFE_WEAK
    if risk_score < 0.65:
        return RISK_UNCERTAIN
    if risk_score < 0.80:
        return RISK_RISKY_WEAK
    return RISK_RISKY_STRONG


def _legacy_suggestion(risk_score: float, confidence: float, strong_bad: list[str], strong_good: list[str]) -> str:
    if risk_score <= 0.20 and confidence >= 0.55 and strong_good:
        return LEGACY_GOOD_STRONG
    if risk_score <= 0.40 and confidence >= 0.45:
        return LEGACY_GOOD_WEAK
    if risk_score >= 0.80 and confidence >= 0.70 and strong_bad:
        return LEGACY_VALIDATED_BAD
    return LEGACY_AMBIGUOUS


def _final_risk_from_components(components: dict[str, float], confidence: float) -> tuple[float, float, float]:
    raw = (
        0.30 * components.get("local_damage_risk", 0.0)
        + 0.25 * components.get("no_progress_risk", 0.0)
        + 0.20 * components.get("same_state_disadvantage_risk", 0.0)
        + 0.15 * components.get("expert_deviation_risk", 0.0)
        + 0.10 * components.get("failure_onset_risk", 0.0)
        - 0.20 * components.get("local_progress_credit", 0.0)
    )
    raw = clamp(raw)
    damage = components.get("local_damage_risk", 0.0)
    no_progress = components.get("no_progress_risk", 0.0)
    same_state = components.get("same_state_disadvantage_risk", 0.0)
    failure_onset = components.get("failure_onset_risk", 0.0)
    progress = components.get("local_progress_credit", 0.0)
    if damage >= 0.75:
        raw = max(raw, 0.72 + 0.22 * damage - 0.08 * progress)
    state_context = components.get("state_context_no_progress_risk", 0.0)
    if no_progress >= 0.80 and failure_onset >= 0.50:
        raw = max(raw, 0.58 + 0.24 * no_progress + 0.08 * failure_onset - 0.10 * progress)
    if no_progress >= 0.80 and same_state >= 0.50:
        raw = max(raw, 0.60 + 0.22 * no_progress + 0.12 * same_state - 0.10 * progress)
    if no_progress >= 0.80 and failure_onset >= 0.50 and same_state >= 0.20:
        raw = max(raw, 0.62 + 0.20 * no_progress + 0.08 * failure_onset + 0.08 * same_state - 0.10 * progress)
    if no_progress >= 0.80 and state_context >= 0.80:
        raw = max(raw, 0.64 + 0.22 * no_progress + 0.06 * failure_onset - 0.10 * progress)
    # Low-confidence samples are pulled toward uncertainty instead of forced
    # safe or risky. This is the continuous equivalent of AMBIGUOUS.
    risk = clamp(confidence * raw + (1.0 - confidence) * 0.50)
    return raw, risk, 1.0 - risk


def score_sample_local(sample: dict[str, Any]) -> dict[str, Any]:
    """Score one candidate chunk using local simulator evidence only.

    Terminal continuation outcomes are copied into audit fields but are not used
    to create high risk or low risk.
    """
    e = merged_numeric_evidence(sample)
    positive: list[str] = []
    negative: list[str] = []
    weak_negative: list[str] = []
    ambiguous: list[str] = []

    goal_progress = _goal_progress(e)
    lift_progress = _lift_progress(e)
    approach_progress = _approach_progress(e)
    motion = _motion_credits(e)
    reward = as_float(e.get("reward_sum_H"), 0.0) or 0.0
    success = as_bool(e.get("success"))
    local_success_progress = 1.0 if success or reward > 0 else 0.0
    progress_credit = max(goal_progress, lift_progress, approach_progress, local_success_progress)

    if success:
        positive.append("local_success")
    if reward > 0:
        positive.append("local_reward")
    if goal_progress >= 0.35:
        positive.append("target_moved_toward_goal")
    if lift_progress >= 0.35:
        positive.append("target_lifted")
    if approach_progress >= 0.35:
        positive.append("eef_approached_target_in_approach_phase")

    drop_risk = _drop_risk(e, goal_progress)
    away_risk = _goal_worsening(e)
    lost_grasp_risk = _lost_grasp_risk(e, drop_risk, goal_progress)
    collision_risk = 1.0 if as_bool(e.get("bad_contact_confident")) else 0.0
    unstable_risk = 1.0 if as_bool(e.get("unstable_state")) else 0.0
    damage_risk = max(drop_risk, away_risk, lost_grasp_risk, collision_risk, unstable_risk)

    if drop_risk >= 0.55:
        negative.append("object_drop_not_explained_by_goal_progress")
    elif drop_risk >= 0.20:
        weak_negative.append("possible_object_drop")
    if away_risk >= 0.45:
        negative.append("target_moved_away_from_goal")
    if lost_grasp_risk >= 0.45:
        negative.append("gripper_lost_object")
    if collision_risk:
        negative.append("bad_collision_confirmed")
    if unstable_risk:
        negative.append("unstable_state")

    meta = sample.get("metadata") or {}
    failure_onset_risk = 0.0
    if meta.get("window_selection_reason"):
        reason = str(meta.get("window_selection_reason"))
        if reason in {"high_local_risk", "negative_evidence"}:
            failure_onset_risk = 0.90
        elif reason in {"failure_tail", "top_local_risk"}:
            failure_onset_risk = 0.75
        elif reason in {"branchpoint_scan", "pre_failure_offset"}:
            failure_onset_risk = 0.65
        elif reason == "dense_failure_every_timestep":
            dist = as_float(meta.get("distance_to_failure_or_timeout"))
            if dist is None or dist < 0:
                failure_onset_risk = 0.50
            elif dist <= 20:
                failure_onset_risk = 0.85
            elif dist <= 60:
                failure_onset_risk = 0.70
            elif dist <= 120:
                failure_onset_risk = 0.45
            else:
                failure_onset_risk = 0.25

    no_progress_risk = _no_progress_risk(e, progress_credit)
    if no_progress_risk >= 0.75:
        if failure_onset_risk >= 0.50 or str(e.get("phase") or "").upper() == "STUCK_OR_NO_PROGRESS":
            negative.append("no_progress_strong")
        else:
            weak_negative.append("no_progress_observed_without_context")
    elif no_progress_risk >= 0.45:
        weak_negative.append("no_progress_weak")

    if not positive and not negative and not weak_negative:
        ambiguous.append("no_clear_local_signal")
    if e.get("terminal_timeout_audit_only") and not negative:
        ambiguous.append("terminal_timeout_audit_only_not_label_proof")

    components = {
        "local_damage_risk": damage_risk,
        "no_progress_risk": no_progress_risk,
        "same_state_disadvantage_risk": 0.0,
        "expert_deviation_risk": 0.0,
        "failure_onset_risk": failure_onset_risk,
        "local_progress_credit": progress_credit,
        **motion,
    }
    confidence = _evidence_confidence(e, positive, negative)
    raw_risk, risk_score, chunk_quality = _final_risk_from_components(components, confidence)

    # Absence of bad evidence is not evidence of a good action.  This matters
    # at preterminal branchpoints where sparse LIBERO rewards are often zero
    # and tiny object jitter can avoid the no-progress detector.  Those samples
    # must stay uncertain unless we have real positive progress/success/reward.
    if not positive and not negative:
        if weak_negative:
            ambiguous.append("no_positive_progress_only_weak_negative")
            uncertain_floor = clamp(0.42 + 0.10 * no_progress_risk + 0.04 * failure_onset_risk - 0.06 * progress_credit)
            risk_score = max(risk_score, uncertain_floor)
        else:
            ambiguous.append("no_positive_or_negative_local_evidence")
            uncertain_floor = clamp(0.46 + 0.08 * no_progress_risk + 0.03 * failure_onset_risk - 0.06 * progress_credit)
            risk_score = max(risk_score, uncertain_floor)
        chunk_quality = 1.0 - risk_score

    strong_bad = list(dict.fromkeys(negative))
    strong_good = list(dict.fromkeys(positive))
    bin_name = risk_bin(risk_score)

    return {
        "score_version": SCORE_VERSION,
        "action_target": "simvla_candidate_action_chunk",
        "terminal_outcome_policy": "audit_only_not_label_source",
        "risk_score_local": risk_score,
        "risk_score_raw_local": raw_risk,
        "chunk_quality_local": chunk_quality,
        "risk_confidence_local": confidence,
        "risk_components": components,
        "risk_bin_local": bin_name,
        "legacy_label_suggestion_local": _legacy_suggestion(risk_score, confidence, strong_bad, strong_good),
        "bad_subtype": BAD_SUBTYPE_UNKNOWN,
        "positive_evidence": strong_good,
        "negative_evidence": strong_bad,
        "weak_negative_evidence": list(dict.fromkeys(weak_negative)),
        "ambiguous_evidence": list(dict.fromkeys(ambiguous)),
        "numeric_evidence": e,
    }


def score_state_group(samples: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return continuous risk labels for one same-state group."""
    local_rows = [score_sample_local(sample) for sample in samples]
    n = len(samples)
    local_risks = [float(row["risk_score_local"]) for row in local_rows]
    local_conf = [float(row["risk_confidence_local"]) for row in local_rows]
    best_risk = min(local_risks) if local_risks else 0.50
    worst_risk = max(local_risks) if local_risks else 0.50
    high_risk_count = sum(1 for r, c in zip(local_risks, local_conf) if r >= 0.70 and c >= 0.55)
    low_risk_count = sum(1 for r, c in zip(local_risks, local_conf) if r <= 0.35 and c >= 0.45)
    majority_high = high_risk_count >= max(3, (n + 1) // 2)
    no_progress_context_count = sum(
        1
        for row in local_rows
        if float(row["risk_components"].get("no_progress_risk", 0.0)) >= 0.80
        and float(row["risk_components"].get("failure_onset_risk", 0.0)) >= 0.50
    )
    majority_no_progress_context = no_progress_context_count >= max(3, (n + 1) // 2)

    rows: list[dict[str, Any]] = []
    for sample, row in zip(samples, local_rows):
        components = dict(row["risk_components"])
        candidate_local = float(row["risk_score_local"])
        same_state_disadvantage = 0.0
        if n >= 2:
            same_state_disadvantage = clamp((candidate_local - best_risk - 0.10) / 0.45)
        components["same_state_disadvantage_risk"] = same_state_disadvantage
        if majority_no_progress_context and components.get("no_progress_risk", 0.0) >= 0.80:
            components["state_context_no_progress_risk"] = 1.0

        confidence = float(row["risk_confidence_local"])
        if n >= 4:
            confidence = clamp(confidence + 0.10)
        if same_state_disadvantage >= 0.50 and low_risk_count:
            confidence = clamp(confidence + 0.08)

        negative = list(row["negative_evidence"])
        weak_negative = list(row["weak_negative_evidence"])
        ambiguous = list(row["ambiguous_evidence"])
        no_progress_component = float(components.get("no_progress_risk", 0.0))
        if (
            same_state_disadvantage >= 0.50
            and low_risk_count > 0
            and no_progress_component >= 0.80
        ):
            negative.append("no_progress_strong_vs_same_state_alternatives")
        elif (
            components.get("state_context_no_progress_risk", 0.0) >= 0.80
            and no_progress_component >= 0.80
        ):
            negative.append("no_progress_strong_state_context")
        if same_state_disadvantage >= 0.50:
            weak_negative.append("same_state_candidate_worse_than_alternatives")

        raw_risk, risk_score, chunk_quality = _final_risk_from_components(components, confidence)
        if not row["positive_evidence"] and not negative:
            if weak_negative:
                ambiguous.append("no_positive_progress_only_weak_negative")
                uncertain_floor = clamp(
                    0.42
                    + 0.10 * float(components.get("no_progress_risk", 0.0))
                    + 0.04 * float(components.get("failure_onset_risk", 0.0))
                    + 0.05 * same_state_disadvantage
                    - 0.06 * float(components.get("local_progress_credit", 0.0))
                )
                risk_score = max(risk_score, uncertain_floor)
            else:
                ambiguous.append("no_positive_or_negative_local_evidence")
                uncertain_floor = clamp(
                    0.46
                    + 0.08 * float(components.get("no_progress_risk", 0.0))
                    + 0.03 * float(components.get("failure_onset_risk", 0.0))
                    + 0.04 * same_state_disadvantage
                    - 0.06 * float(components.get("local_progress_credit", 0.0))
                )
                risk_score = max(risk_score, uncertain_floor)
            chunk_quality = 1.0 - risk_score

        bad_subtype = BAD_SUBTYPE_UNKNOWN
        if risk_score >= 0.75 and negative:
            if low_risk_count > 0 and same_state_disadvantage >= 0.45:
                bad_subtype = BAD_SUBTYPE_ACTION_SPECIFIC
            elif majority_high or majority_no_progress_context:
                bad_subtype = BAD_SUBTYPE_STATE_CONTEXT

        strong_bad_for_legacy = negative if bad_subtype != BAD_SUBTYPE_UNKNOWN else []
        out = dict(row)
        out.update({
            "risk_score": risk_score,
            "risk_score_raw": raw_risk,
            "chunk_quality": chunk_quality,
            "risk_confidence": confidence,
            "risk_bin": risk_bin(risk_score),
            "legacy_label_suggestion": _legacy_suggestion(
                risk_score,
                confidence,
                strong_bad_for_legacy,
                list(row["positive_evidence"]),
            ),
            "bad_subtype": bad_subtype,
            "risk_components": components,
            "weak_negative_evidence": list(dict.fromkeys(weak_negative)),
            "ambiguous_evidence": list(dict.fromkeys(ambiguous)),
            "same_state_comparison_v2": {
                "state_id": state_id(sample),
                "num_siblings": n,
                "candidate_seed": seed(sample),
                "candidate_local_risk": candidate_local,
                "best_local_risk": best_risk,
                "worst_local_risk": worst_risk,
                "same_state_disadvantage_risk": same_state_disadvantage,
                "low_risk_alternative_count": low_risk_count,
                "high_risk_candidate_count": high_risk_count,
                "no_progress_context_count": no_progress_context_count,
                "majority_high_risk": majority_high,
                "majority_no_progress_context": majority_no_progress_context,
            },
        })
        rows.append(out)
    return rows


def summarize_continuous_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    bins = Counter(row.get("risk_bin") for row in rows)
    legacy = Counter(row.get("legacy_label_suggestion") for row in rows)
    subtypes = Counter(row.get("bad_subtype") or BAD_SUBTYPE_UNKNOWN for row in rows)
    scores = [float(row.get("risk_score", 0.5)) for row in rows]
    confs = [float(row.get("risk_confidence", 0.0)) for row in rows]
    return {
        "num_samples": len(rows),
        "risk_bin_counts": dict(bins),
        "legacy_label_suggestion_counts": dict(legacy),
        "bad_subtype_counts": dict(subtypes),
        "risk_score_mean": sum(scores) / len(scores) if scores else None,
        "risk_score_min": min(scores) if scores else None,
        "risk_score_max": max(scores) if scores else None,
        "risk_confidence_mean": sum(confs) / len(confs) if confs else None,
        "high_risk_confident_count": sum(1 for r, c in zip(scores, confs) if r >= 0.80 and c >= 0.70),
        "low_risk_confident_count": sum(1 for r, c in zip(scores, confs) if r <= 0.20 and c >= 0.55),
        "uncertain_or_low_confidence_count": sum(1 for r, c in zip(scores, confs) if 0.40 < r < 0.65 or c < 0.45),
    }


def summarize_state_group_risks(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize whether one same-state seed set is useful for action risk.

    This is saved as metadata/evidence. It is not a model input.
    """
    bins = Counter(row.get("risk_bin") for row in rows)
    subtypes = Counter(row.get("bad_subtype") or BAD_SUBTYPE_UNKNOWN for row in rows)
    scores = [float(row.get("risk_score", 0.5)) for row in rows]
    high_count = sum(1 for row in rows if row.get("risk_bin") in {RISK_RISKY_WEAK, RISK_RISKY_STRONG})
    low_count = sum(1 for row in rows if row.get("risk_bin") in {RISK_SAFE_WEAK, RISK_SAFE_STRONG})
    uncertain_count = len(rows) - high_count - low_count
    action_specific_count = sum(1 for row in rows if row.get("bad_subtype") == BAD_SUBTYPE_ACTION_SPECIFIC)
    state_context_count = sum(1 for row in rows if row.get("bad_subtype") == BAD_SUBTYPE_STATE_CONTEXT)
    if high_count > 0 and low_count > 0 and action_specific_count > 0:
        group_type = "action_specific_mixed"
    elif high_count > 0 and low_count > 0:
        group_type = "mixed_needs_review"
    elif high_count == len(rows) and len(rows) > 0:
        group_type = "all_risky_state_context_candidate"
    elif low_count == len(rows) and len(rows) > 0:
        group_type = "all_safe_or_weak_safe"
    else:
        group_type = "uncertain_or_low_confidence"
    return {
        "schema_version": "stage9_same_state_group_summary_v2",
        "num_candidates": len(rows),
        "group_type": group_type,
        "risk_bin_counts": dict(bins),
        "bad_subtype_counts": dict(subtypes),
        "high_risk_count": high_count,
        "low_risk_count": low_count,
        "uncertain_count": uncertain_count,
        "action_specific_count": action_specific_count,
        "state_context_count": state_context_count,
        "risk_score_min": min(scores) if scores else None,
        "risk_score_max": max(scores) if scores else None,
        "risk_score_range": (max(scores) - min(scores)) if scores else None,
    }
