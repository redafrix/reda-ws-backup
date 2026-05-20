from __future__ import annotations
import json, os
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw
from .label_rules import label_outcome, RULE_VERSION
from .task_parser import parse_task_context

ROOT = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
OUT = ROOT / "asynchvla_ws/stage9_libero_pro_risk_data/rule_tests"
REPORTS = ROOT / "asynchvla_ws/stage9_libero_pro_risk_data/reports"


def image(path: Path, title: str, color: tuple[int, int, int]):
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (320, 180), color)
    d = ImageDraw.Draw(img)
    d.text((12, 12), title, fill=(255,255,255))
    img.save(path)
    return str(path)


def outcome(task_progress: dict, **kw) -> dict:
    delta = {
        "eef_delta": kw.get("eef_delta", 0.05),
        "object_delta_max": kw.get("object_delta_max", task_progress.get("target_motion", 0.0) or 0.0),
        "height_drop_max": kw.get("height_drop_max", max(0.0, -(task_progress.get("target_height_delta") or 0.0))),
        "task_progress": {
            "task_context_available": True,
            "target_base": kw.get("target_base", "alphabet_soup_1"),
            "goal_base": kw.get("goal_base", "basket_1"),
            "relation": kw.get("relation", "place_or_put"),
            "parse_confidence": kw.get("parse_confidence", "MEDIUM"),
            "target_pos_available": kw.get("target_pos_available", True),
            "goal_pos_available": kw.get("goal_pos_available", True),
            **task_progress,
        },
    }
    return {
        "H_used": kw.get("H_used", 20),
        "reward_sum_H": kw.get("reward_sum_H", 0.0),
        "nonzero_reward_count_H": kw.get("nonzero_reward_count_H", 0),
        "success_before": False,
        "success_after": kw.get("success_after", False),
        "success_within_H": kw.get("success_within_H", False),
        "done_within_H": kw.get("done_within_H", False),
        "delta": delta,
    }


def run_case(idx, name, expected, task_progress, note, **kw):
    case_dir = OUT / f"test_{idx:02d}_{name}"
    before = image(case_dir / "before.png", f"{name} before", (40, 40, 70))
    after = image(case_dir / "after.png", f"{name} after", (40, 90, 60) if expected.startswith("GOOD") else (100, 50, 50) if expected == "BAD" else (80, 80, 80))
    outc = outcome(task_progress, **kw)
    lab = label_outcome(outc)
    actual = lab["label"]
    status = "PASS" if actual == expected else "FAIL"
    result = {
        "test_name": name,
        "expected": expected,
        "actual": actual,
        "status": status,
        "note": note,
        "before_image": before,
        "after_image": after,
        "outcome": outc,
        "label_output": lab,
    }
    (case_dir / "result.json").write_text(json.dumps(result, indent=2))
    md = f"# Stage 9 Rule Test {idx:02d}: {name}\n\nStatus: `{status}`\n\nExpected: `{expected}`\n\nActual: `{actual}`\n\nNote: {note}\n\nBefore image: `{before}`\n\nAfter image: `{after}`\n\n```json\n{json.dumps(result, indent=2)}\n```\n"
    report_name = {
        1: "stage9_rule_test_01_success.md",
        2: "stage9_rule_test_02_eef_target_approach.md",
        3: "stage9_rule_test_03_wrong_object.md",
        4: "stage9_rule_test_04_object_lift.md",
        5: "stage9_rule_test_05_object_drop.md",
        6: "stage9_rule_test_06_object_goal_distance.md",
        7: "stage9_rule_test_07_no_progress.md",
        8: "stage9_rule_test_08_contact.md",
        9: "stage9_rule_test_09_gripper_relation.md",
        10: "stage9_rule_test_10_mixed_signal.md",
    }[idx]
    (REPORTS / report_name).write_text(md)
    return result


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    # Target parser smoke using real-ish obs keys.
    obs = {"alphabet_soup_1_pos":[0,0,0], "basket_1_pos":[1,0,0], "robot0_eef_pos":[0,0,0]}
    parse = parse_task_context("pick the alphabet soup and place it in the basket", obs)
    parse_pass = parse.get("target_base") == "alphabet_soup_1" and parse.get("goal_base") == "basket_1"
    results = []
    results.append(run_case(1, "success_rule_test", "GOOD_STRONG", {"target_motion":0.0,"target_to_eef_before":0.2,"target_to_eef_delta":0.0}, "Success flag is strong GOOD evidence.", success_within_H=True))
    results.append(run_case(2, "eef_target_approach_rule_test", "GOOD_WEAK", {"target_motion":0.0,"target_to_eef_before":0.30,"target_to_eef_after":0.24,"target_to_eef_delta":-0.06}, "EEF-target approach before grasp is weak only, not strong."))
    results.append(run_case(3, "wrong_object_rule_test", "AMBIGUOUS", {"target_motion":0.0,"target_to_eef_before":0.30,"target_to_eef_after":0.30,"target_to_eef_delta":0.0,"non_target_motion_max":0.12}, "Only non-target/random object motion must not be GOOD."))
    results.append(run_case(4, "object_lift_rule_test", "GOOD_STRONG", {"target_motion":0.04,"target_height_delta":0.05,"target_height_drop":-0.05,"target_to_eef_before":0.05,"target_to_eef_delta":-0.01}, "Target lift is strong local progress."))
    results.append(run_case(5, "object_drop_rule_test", "BAD", {"target_motion":0.06,"target_height_delta":-0.14,"target_height_drop":0.14,"target_to_eef_before":0.04,"target_to_eef_delta":0.03}, "Target height drop is BAD."))
    results.append(run_case(6, "object_goal_distance_rule_test", "GOOD_STRONG", {"target_motion":0.05,"target_to_goal_before":0.40,"target_to_goal_after":0.34,"target_to_goal_delta":-0.06,"target_to_eef_before":0.08,"target_to_eef_delta":0.01}, "Target moved closer to correct goal is strong GOOD."))
    results.append(run_case(7, "no_progress_rule_test", "BAD", {"target_motion":0.0,"target_to_goal_delta":0.0,"target_to_eef_before":0.30,"target_to_eef_delta":0.0}, "No EEF/target/goal/reward progress is BAD.", eef_delta=0.0))
    results.append(run_case(8, "contact_rule_test", "AMBIGUOUS", {"target_motion":0.0,"target_to_eef_before":0.2,"target_to_eef_delta":0.0,"bad_contact_confident":False}, "Unconfident/raw contact is weak only, not BAD."))
    results.append(run_case(9, "gripper_relation_rule_test", "GOOD_WEAK", {"target_motion":0.0,"target_to_eef_before":0.06,"target_to_eef_delta":-0.01,"gripper_closed_near_target":True}, "Gripper closes near target is weak phase evidence."))
    results.append(run_case(10, "mixed_signal_rule_test", "BAD", {"target_motion":0.05,"target_to_goal_delta":-0.04,"target_height_delta":-0.13,"target_height_drop":0.13,"target_to_eef_before":0.05,"target_to_eef_delta":-0.02}, "Strong BAD overrides progress."))
    pass_count=sum(r["status"]=="PASS" for r in results)
    summary={"generated":datetime.now().isoformat(timespec="seconds"),"rule_version":RULE_VERSION,"target_parser_pass":parse_pass,"target_parser_output":parse,"num_tests":len(results),"pass_count":pass_count,"fail_count":len(results)-pass_count,"results":[{"name":r["test_name"],"expected":r["expected"],"actual":r["actual"],"status":r["status"]} for r in results]}
    (OUT/"summary.json").write_text(json.dumps(summary, indent=2))
    table="\n".join([f"| {r['test_name']} | {r['status']} | {r['expected']} | {r['actual']} | {'yes' if r['status']=='PASS' and r['expected'] in ['GOOD_STRONG','BAD'] else 'weak/no'} |" for r in results])
    md=f"# Stage 9 Rule Unit Test Summary\n\nGenerated: `{summary['generated']}`\n\nTarget parser pass: `{parse_pass}`\n\nRule version: `{RULE_VERSION}`\n\nPassed: `{pass_count}/10`\n\n| Rule | Status | Expected | Actual | Strong Evidence Allowed? |\n|---|---:|---|---|---|\n{table}\n\nGate decision: `{'PASS' if parse_pass and pass_count >= 6 else 'FAIL'}`\n\n```json\n{json.dumps(summary, indent=2)}\n```\n"
    (REPORTS/"stage9_rule_unit_test_summary.md").write_text(md)
    progress=f"# Stage 9 Rule Test Progress\n\nUpdated: `{summary['generated']}`\n\n## Current Step\n\nStep 4 complete: rule unit tests executed.\n\n## Completed Tests\n\n{len(results)} rule tests plus target parser smoke.\n\n## Passed Tests\n\n{pass_count}/10.\n\n## Failed Tests\n\n{len(results)-pass_count}/10.\n\n## Files Changed\n\n- `asynchvla_ws/src/data_collection_stage9/run_rule_unit_tests.py`\n- `asynchvla_ws/src/data_collection_stage9/label_rules.py`\n\n## Reports Written\n\n- `stage9_rule_test_01_success.md` through `stage9_rule_test_10_mixed_signal.md`\n- `stage9_rule_unit_test_summary.md`\n\n## Current Blocker\n\n{'None for rule tests; proceed to harder/later-state pilot.' if parse_pass and pass_count >= 6 else 'Rule-test gate failed; do not run pilot.'}\n\n## Exact Next Command To Continue\n\n```bash\ncd \"/media/rootalkhatib/My Passport/reda_ws\"\nsource asynchvla_ws/scripts/activate_simvla_bob.sh\nexport LIBERO_CONFIG_PATH=\"/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob\"\nexport MUJOCO_GL=egl PYOPENGL_PLATFORM=egl\nexport PYTHONPATH=\"$PWD/asynchvla_ws/src:$PYTHONPATH\"\npython3 -m data_collection_stage9.collect_counterfactual_dataset --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug --task-ids 0 1 --states-per-task 6 --simvla-seeds 0 1 2 3 4 5 6 7 --horizon 20 --history-k 8 --parent-roll-steps 40 --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3 --save-images\n```\n"
    (REPORTS/"STAGE9_RULE_TEST_PROGRESS.md").write_text(progress)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
