from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

import numpy as np

try:
    from .detect_mini_failures import build_arg_parser, run
except ImportError:  # pragma: no cover
    from detect_mini_failures import build_arg_parser, run  # type: ignore


TASK_CONTEXT = {
    "task_language": "pick up the black bowl and place it on the plate",
    "target_base": "black_bowl",
    "target_body_prefix": "black_bowl",
    "goal_base": "plate",
    "goal_body_prefix": "plate",
    "relation": "place_or_put",
    "parse_confidence": "HIGH",
}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def write_step_npz(path: Path, eef: tuple[float, float, float], gripper: float, target: tuple[float, float, float], plate: tuple[float, float, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        path,
        robot0_eef_pos=np.asarray(eef, dtype=float),
        robot0_gripper_qpos=np.asarray([gripper, gripper], dtype=float),
        black_bowl_pos=np.asarray(target, dtype=float),
        plate_pos=np.asarray(plate, dtype=float),
    )


def make_episode(root: Path, episode_id: str, scenario: str) -> None:
    ep = root / "episodes" / episode_id
    (ep / "obs_npz").mkdir(parents=True)
    write_json(ep / "episode_metadata.json", {"episode_id": episode_id, "task_context": TASK_CONTEXT})
    steps = []
    plate = (0.50, 0.00, 0.04)
    other = (0.08, 0.10, 0.04)
    target = (0.10, 0.00, 0.04)
    total_steps = 90 if scenario in {"healthy_pick", "unstable_pick"} else (70 if scenario in {"drop", "missed_place"} else 40)
    for i in range(total_steps):
        phase = "GRASP_OR_LIFT"
        before_target = target
        after_target = target
        before_other = other
        after_other = other
        before_eef = (0.10, 0.00, 0.06 + 0.002 * i)
        after_eef = (0.10, 0.00, 0.065 + 0.006 * i)
        before_gripper = 0.040 if i < 2 else 0.012
        after_gripper = 0.012
        after_contact = {"contact_available": True, "contact_count": 0, "contacts": []}

        if scenario == "missed_pick":
            # EEF lifts after gripper closure; target stays on table.
            after_target = target
        elif scenario == "healthy_pick":
            phase = "GRASP_OR_LIFT" if i < 35 else "TRANSPORT"
            before_eef = (0.10 + 0.001 * i, 0.00, 0.08 + min(i, 35) * 0.0025)
            after_eef = (0.101 + 0.001 * i, 0.00, 0.082 + min(i + 1, 35) * 0.0025)
            before_gripper = 0.040 if i < 4 else 0.010
            after_gripper = 0.010
            if i < 8:
                before_target = target
                after_target = target
            else:
                before_target = (before_eef[0], before_eef[1], before_eef[2] - 0.020)
                after_target = (after_eef[0], after_eef[1], after_eef[2] - 0.020)
        elif scenario == "unstable_pick":
            phase = "GRASP_OR_LIFT"
            before_gripper = 0.040 if i < 4 else 0.010
            after_gripper = 0.010
            before_eef = (0.10, 0.00, 0.07 + min(i, 18) * 0.003)
            after_eef = (0.10, 0.00, 0.073 + min(i + 1, 18) * 0.003)
            if i < 8:
                before_target = target
                after_target = target
            elif i < 22:
                lift = min(i - 8, 10) * 0.003
                before_target = (0.10, 0.00, 0.04 + lift)
                after_target = (0.10, 0.00, 0.043 + lift)
            else:
                before_target = (0.10, 0.00, 0.070)
                after_target = (0.10, 0.00, 0.045)
        elif scenario == "wrong_object":
            # Wrong object follows the EEF while target stays still.
            after_other = (after_eef[0], after_eef[1], after_eef[2] - 0.015)
        elif scenario == "drop":
            phase = "TRANSPORT"
            before_eef = (0.18 + 0.002 * i, 0.00, 0.20)
            after_eef = (0.182 + 0.002 * i, 0.00, 0.20)
            before_gripper = after_gripper = 0.012
            if i < 35:
                before_target = (before_eef[0], before_eef[1], 0.17)
                after_target = (after_eef[0], after_eef[1], 0.17)
            else:
                before_target = (0.25, 0.00, 0.17)
                after_target = (0.25 + 0.001 * (i - 35), 0.00, 0.06)
                after_contact = {"contact_available": True, "contact_count": 1, "contacts": [["black_bowl_geom", "table_collision"]]}
        elif scenario == "missed_place":
            phase = "PLACE_OR_GOAL"
            before_eef = (0.30 + 0.001 * i, 0.00, 0.16)
            after_eef = (0.301 + 0.001 * i, 0.00, 0.155)
            if i < 35:
                before_target = (before_eef[0], before_eef[1], 0.135)
                after_target = (after_eef[0], after_eef[1], 0.135)
                before_gripper = after_gripper = 0.012
            else:
                before_target = (0.32, 0.00, 0.12)
                after_target = (0.32, 0.00, 0.04)
                before_gripper = 0.012
                after_gripper = 0.045

        before_obs = ep / "obs_npz" / f"step_{i:04d}_before_obs.npz"
        after_obs = ep / "obs_npz" / f"step_{i:04d}_after_obs.npz"
        write_step_npz(before_obs, before_eef, before_gripper, before_target, plate)
        write_step_npz(after_obs, after_eef, after_gripper, after_target, plate)
        row = {
            "episode_id": episode_id,
            "env_step": i,
            "phase_before": phase,
            "parent_chunk_index": i // 10,
            "parent_chunk_position": i % 10,
            "reward": 0.0,
            "done": False,
            "success_before": False,
            "success_after": False,
            "before_object_positions": {
                "black_bowl": list(before_target),
                "plate": list(plate),
                "ramekin": list(before_other),
            },
            "after_object_positions": {
                "black_bowl": list(after_target),
                "plate": list(plate),
                "ramekin": list(after_other),
            },
            "before_contact": {"contact_available": True, "contact_count": 0, "contacts": []},
            "after_contact": after_contact,
            "paths": {
                "before_obs_npz": str(before_obs),
                "after_obs_npz": str(after_obs),
            },
            "action_env": [0.0] * 7,
        }
        steps.append(row)
    with (ep / "steps.jsonl").open("w") as f:
        for row in steps:
            f.write(json.dumps(row, sort_keys=True) + "\n")
    write_json(ep / "summary.json", {"episode_id": episode_id, "episode_steps": len(steps), "episode_success": False, "task_context": TASK_CONTEXT})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep-dir", default=None)
    args = parser.parse_args()
    temp = Path(args.keep_dir) if args.keep_dir else Path(tempfile.mkdtemp(prefix="stage9_mini_failure_smoke_"))
    if temp.exists() and args.keep_dir:
        shutil.rmtree(temp)
    temp.mkdir(parents=True, exist_ok=True)
    raw = temp / "raw"
    out = temp / "out"
    for scenario in ["missed_pick", "wrong_object", "drop", "missed_place", "healthy_pick", "unstable_pick"]:
        make_episode(raw, scenario, scenario)

    detector_parser = build_arg_parser()
    detector_args = detector_parser.parse_args([
        "--raw-root", str(raw),
        "--out-dir", str(out),
        "--event-window", "20",
        "--pre-failure-steps", "60",
        "--core-label-steps", "10",
    ])
    summary = run(detector_args)
    event_counts = summary.get("event_counts") or {}
    episode_summaries = {
        row["episode_id"]: row
        for row in summary.get("episode_feature_summaries") or []
    }
    expected = {
        "missed_pick": 1,
        "wrong_object_picked": 1,
        "drop_or_slip": 1,
        "missed_place": 1,
        "unstable_pick_or_failed_lift": 1,
    }
    failures = {}
    for key, minimum in expected.items():
        if int(event_counts.get(key, 0)) < minimum:
            failures[key] = {"expected_at_least": minimum, "actual": event_counts.get(key, 0)}
    per_episode_expected = {
        "missed_pick": "missed_pick",
        "wrong_object": "wrong_object_picked",
        "drop": "drop_or_slip",
        "missed_place": "missed_place",
        "unstable_pick": "unstable_pick_or_failed_lift",
    }
    events_path = out / "mini_failure_events.jsonl"
    by_episode: dict[str, set[str]] = {}
    with events_path.open() as f:
        for line in f:
            event = json.loads(line)
            by_episode.setdefault(str(event.get("episode_id")), set()).add(str(event.get("event_type")))
    for episode_id, event_type in per_episode_expected.items():
        if event_type not in by_episode.get(episode_id, set()):
            failures[f"episode_{episode_id}"] = {
                "expected_event": event_type,
                "actual_events": sorted(by_episode.get(episode_id, set())),
                "episode_summary": episode_summaries.get(episode_id),
            }
    if by_episode.get("healthy_pick"):
        failures["episode_healthy_pick"] = {
            "expected_events": [],
            "actual_events": sorted(by_episode.get("healthy_pick", set())),
            "episode_summary": episode_summaries.get("healthy_pick"),
        }
    result = {
        "status": "pass" if not failures else "fail",
        "temp_dir": str(temp),
        "summary": summary,
        "failures": failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
