from __future__ import annotations
RULE_VERSION = "stage9_rules_v6_four_class_evidence"

LABEL_GOOD_STRONG = "GOOD_STRONG"
LABEL_GOOD_WEAK = "GOOD_WEAK"
LABEL_BAD = "BAD"
LABEL_AMBIGUOUS = "AMBIGUOUS"


def _phase(e: dict) -> str:
    tm = e.get("target_motion")
    th = e.get("target_height_delta")
    tgt_eef = e.get("target_to_eef_before")
    gripper_closed = e.get("gripper_closed_near_target")
    if tm is not None and tm > 0.015:
        if th is not None and th > 0.015:
            return "grasp_or_lift"
        return "transport_or_place"
    if gripper_closed:
        return "near_grasp"
    if tgt_eef is not None and tgt_eef < 0.09:
        return "near_grasp"
    return "approach"


def _truthy(v) -> bool:
    return bool(v) if v is not None else False


def _collect_evidence(outcome: dict) -> dict:
    delta = outcome.get("delta", {}) or {}
    task = delta.get("task_progress", {}) or {}
    rs = float(outcome.get("reward_sum_H", 0.0))
    nz = int(outcome.get("nonzero_reward_count_H", 0))
    success = bool(outcome.get("success_within_H") or outcome.get("success_after"))
    e = {
        "reward_sum_H": rs,
        "nonzero_reward_count_H": nz,
        "success": success,
        "eef_delta": delta.get("eef_delta"),
        "object_delta_max": delta.get("object_delta_max"),
        "height_drop_max": delta.get("height_drop_max"),
        "target_base": task.get("target_base"),
        "goal_base": task.get("goal_base"),
        "task_relation": task.get("relation"),
        "parse_confidence": task.get("parse_confidence"),
        "target_pos_available": task.get("target_pos_available"),
        "goal_pos_available": task.get("goal_pos_available"),
        "target_motion": task.get("target_motion"),
        "target_height_delta": task.get("target_height_delta"),
        "target_height_drop": task.get("target_height_drop"),
        "target_to_goal_delta": task.get("target_to_goal_delta"),
        "target_to_eef_before": task.get("target_to_eef_before"),
        "target_to_eef_after": task.get("target_to_eef_after"),
        "target_to_eef_delta": task.get("target_to_eef_delta"),
        "gripper_closed_near_target": task.get("gripper_closed_near_target"),
        "gripper_opened_near_target": task.get("gripper_opened_near_target"),
        "non_target_motion_max": task.get("non_target_motion_max"),
        "unstable_state": task.get("unstable_state"),
        "bad_contact_confident": task.get("bad_contact_confident"),
    }
    e["phase"] = _phase(e)
    return e


def _bad_evidence(e: dict) -> list[str]:
    reasons = []
    th_drop = e.get("target_height_drop")
    global_drop = e.get("height_drop_max")
    goal_delta = e.get("target_to_goal_delta")
    target_motion = e.get("target_motion")
    target_eef_delta = e.get("target_to_eef_delta")
    eef = e.get("eef_delta")
    if th_drop is not None and th_drop > 0.10:
        reasons.append("target_object_dropped")
    if global_drop is not None and global_drop > 0.18:
        reasons.append("large_object_height_drop")
    if goal_delta is not None and goal_delta > 0.06 and target_motion is not None and target_motion > 0.02:
        reasons.append("target_object_moved_away_from_goal")
    if e.get("phase") in {"approach", "near_grasp"} and target_eef_delta is not None and target_eef_delta > 0.045:
        reasons.append("eef_moved_away_from_target_during_approach")
    if _truthy(e.get("gripper_opened_near_target")) and th_drop is not None and th_drop > 0.04:
        reasons.append("gripper_lost_or_released_target")
    if _truthy(e.get("bad_contact_confident")):
        reasons.append("confident_bad_contact")
    if _truthy(e.get("unstable_state")):
        reasons.append("unstable_state")
    no_eef = eef is not None and eef < 0.008
    no_target_motion = target_motion is not None and target_motion < 0.003
    no_goal_progress = goal_delta is None or goal_delta > -0.003
    no_target_approach = target_eef_delta is None or target_eef_delta > -0.003
    if e.get("nonzero_reward_count_H", 0) == 0 and no_eef and no_target_motion and no_goal_progress and no_target_approach:
        reasons.append("zero_reward_no_eef_target_or_goal_progress")
    return reasons


def _strong_good_evidence(e: dict) -> list[str]:
    reasons = []
    goal_delta = e.get("target_to_goal_delta")
    target_motion = e.get("target_motion")
    target_height_delta = e.get("target_height_delta")
    if e.get("success"):
        reasons.append("success_within_horizon")
    if goal_delta is not None and goal_delta < -0.025:
        reasons.append("target_object_closer_to_goal")
    if target_height_delta is not None and target_height_delta > 0.025 and target_motion is not None and target_motion > 0.012:
        reasons.append("target_object_lifted")
    if target_motion is not None and target_motion > 0.045 and goal_delta is not None and goal_delta < -0.010:
        reasons.append("target_object_moved_correct_direction")
    return reasons


def _weak_good_evidence(e: dict) -> list[str]:
    reasons = []
    target_eef_delta = e.get("target_to_eef_delta")
    eef = e.get("eef_delta")
    target_motion = e.get("target_motion")
    goal_delta = e.get("target_to_goal_delta")
    if e.get("phase") in {"approach", "near_grasp"} and target_eef_delta is not None and target_eef_delta < -0.020:
        reasons.append("eef_closer_to_target_before_grasp")
    if _truthy(e.get("gripper_closed_near_target")):
        reasons.append("gripper_closed_near_target")
    if target_motion is not None and 0.010 <= target_motion <= 0.045 and (goal_delta is None or goal_delta <= 0.010):
        reasons.append("small_target_motion_not_strong")
    if eef is not None and eef > 0.01 and target_eef_delta is not None and -0.020 <= target_eef_delta < -0.006:
        reasons.append("weak_target_alignment_improved")
    return reasons


def label_outcome(outcome: dict, task_context: dict | None = None) -> dict:
    e = _collect_evidence(outcome)
    if not e.get("target_base") or not e.get("target_pos_available"):
        return {"label": LABEL_AMBIGUOUS, "label_confidence": "LOW", "bad_event_type": "unknown", "label_reasons": ["target_object_unknown_or_position_missing"], "numeric_evidence": e, "rule_version": RULE_VERSION, "strong_good_evidence": [], "weak_good_evidence": [], "bad_evidence": []}
    bad = _bad_evidence(e)
    strong = _strong_good_evidence(e)
    weak = _weak_good_evidence(e)
    if bad:
        return {"label": LABEL_BAD, "label_confidence": "HIGH" if any("drop" in r or "unstable" in r for r in bad) else "MEDIUM", "bad_event_type": bad[0], "label_reasons": bad, "numeric_evidence": e, "rule_version": RULE_VERSION, "strong_good_evidence": strong, "weak_good_evidence": weak, "bad_evidence": bad}
    if strong:
        return {"label": LABEL_GOOD_STRONG, "label_confidence": "HIGH", "bad_event_type": None, "label_reasons": strong, "numeric_evidence": e, "rule_version": RULE_VERSION, "strong_good_evidence": strong, "weak_good_evidence": weak, "bad_evidence": []}
    if weak:
        return {"label": LABEL_GOOD_WEAK, "label_confidence": "MEDIUM", "bad_event_type": None, "label_reasons": weak, "numeric_evidence": e, "rule_version": RULE_VERSION, "strong_good_evidence": [], "weak_good_evidence": weak, "bad_evidence": []}
    return {"label": LABEL_AMBIGUOUS, "label_confidence": "LOW", "bad_event_type": "unknown", "label_reasons": ["no_clear_task_relevant_progress_or_bad_event"], "numeric_evidence": e, "rule_version": RULE_VERSION, "strong_good_evidence": [], "weak_good_evidence": [], "bad_evidence": []}
