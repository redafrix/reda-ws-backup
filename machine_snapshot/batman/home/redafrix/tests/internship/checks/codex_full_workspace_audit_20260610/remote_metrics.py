#!/usr/bin/env python3
import hashlib
import json
import os
from pathlib import Path


ROOTS = [
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_20260609",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610",
    "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2_adaptive_horizon_20260610",
    "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610",
    "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610",
    "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2d_commit_gate_20260610",
]

HASH_PATHS = [
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO/model.safetensors",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors",
    "/tmp/ood_ckpt60000/model.safetensors",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8/model.pt",
    "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/base/model.pt",
    "/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000/model.safetensors",
    "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8/model.pt",
]


def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_success(row):
    if "success" in row:
        return bool(row["success"])
    if row.get("outcome") == "success":
        return True
    if row.get("reward_success") is True:
        return True
    if row.get("checked_success") is True:
        return True
    return False


def steps(row):
    for key in ("num_steps", "steps", "step_count"):
        if key in row and isinstance(row[key], (int, float)):
            return float(row[key])
    return 0.0


def mods(row):
    total = 0
    for key in (
        "num_modifications",
        "total_modifications",
        "action_modifications",
        "modification_count",
        "adaptive_risk_trigger_count",
        "replan_count",
    ):
        val = row.get(key)
        if isinstance(val, (int, float)):
            total += int(val)
    return total


def load_jsonl(path: Path):
    rows = []
    errors = 0
    with path.open("r", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                errors += 1
    return rows, errors


def summarize_rows(rows):
    n = len(rows)
    succ = sum(1 for r in rows if is_success(r))
    step_values = [steps(r) for r in rows]
    seed_values = [r.get("reset_seed") for r in rows if "reset_seed" in r]
    mod_values = [mods(r) for r in rows]
    return {
        "episodes": n,
        "successes": succ,
        "success_rate": round(succ / n, 6) if n else None,
        "mean_steps": round(sum(step_values) / n, 4) if n else None,
        "total_mods_or_adaptive_events": int(sum(mod_values)),
        "unique_reset_seeds": len(set(seed_values)),
        "duplicate_reset_seeds": len(seed_values) - len(set(seed_values)),
        "min_seed": min(seed_values) if seed_values else None,
        "max_seed": max(seed_values) if seed_values else None,
    }


def config_digest(root: Path):
    cfg_dir = root / "configs"
    result = {
        "config_count": 0,
        "suite_values": {},
        "task_ids": [],
        "threshold_values": {},
        "execution_horizons": {},
        "seed_lengths": {},
        "risk_dirs": {},
        "checkpoints": {},
    }
    if not cfg_dir.exists():
        return result
    for cfg_path in sorted(cfg_dir.glob("*.json")):
        if cfg_path.name == "seed_plan.json":
            continue
        try:
            cfg = json.loads(cfg_path.read_text())
        except Exception as exc:
            result.setdefault("config_errors", {})[cfg_path.name] = repr(exc)
            continue
        result["config_count"] += 1
        result["suite_values"][str(cfg.get("suite"))] = result["suite_values"].get(str(cfg.get("suite")), 0) + 1
        if cfg.get("task_id") is not None:
            result["task_ids"].append(cfg.get("task_id"))
        for key in ("selection_main_threshold", "selection_streak_threshold", "selection_min_margin", "selection_strong_margin"):
            if key in cfg:
                result["threshold_values"].setdefault(key, {})
                val = str(cfg.get(key))
                result["threshold_values"][key][val] = result["threshold_values"][key].get(val, 0) + 1
        val = str(cfg.get("execution_horizon"))
        result["execution_horizons"][val] = result["execution_horizons"].get(val, 0) + 1
        seeds = cfg.get("reset_seeds")
        if isinstance(seeds, list):
            result["seed_lengths"].setdefault(str(len(seeds)), 0)
            result["seed_lengths"][str(len(seeds))] += 1
        risk_dir = cfg.get("risk_model_unc_topk8_dir") or cfg.get("risk_model_dir")
        if risk_dir:
            result["risk_dirs"][risk_dir] = result["risk_dirs"].get(risk_dir, 0) + 1
        checkpoint = cfg.get("checkpoint")
        if checkpoint:
            result["checkpoints"][checkpoint] = result["checkpoints"].get(checkpoint, 0) + 1
    result["task_ids"] = sorted(set(result["task_ids"]))
    return result


def root_summary(root_str: str):
    root = Path(root_str)
    out = {"root": root_str, "exists": root.exists()}
    if not root.exists():
        return out
    out["configs"] = config_digest(root)
    out["episode_files"] = {}
    out["aggregate_by_policy"] = {}
    out["aggregate_by_task_policy"] = {}
    parse_errors = 0
    for path in sorted(root.rglob("episode_summaries.jsonl")):
        rows, errors = load_jsonl(path)
        parse_errors += errors
        rel = path.relative_to(root).as_posix()
        summary = summarize_rows(rows)
        out["episode_files"][rel] = summary
        parts = rel.split("/")
        task = next((p for p in parts if p.startswith("task")), "unknown_task")
        policy = parts[-2] if len(parts) >= 2 else "unknown_policy"
        out["aggregate_by_policy"].setdefault(policy, []).extend(rows)
        out["aggregate_by_task_policy"].setdefault(task, {}).setdefault(policy, []).extend(rows)
    out["jsonl_parse_errors"] = parse_errors
    out["aggregate_by_policy"] = {k: summarize_rows(v) for k, v in sorted(out["aggregate_by_policy"].items())}
    out["aggregate_by_task_policy"] = {
        task: {policy: summarize_rows(rows) for policy, rows in sorted(pols.items())}
        for task, pols in sorted(out["aggregate_by_task_policy"].items())
    }
    for log_name in ("sweep_supervisor.log",):
        log_path = root / log_name
        if log_path.exists():
            txt = log_path.read_text(errors="replace")
            out.setdefault("logs", {})[log_name] = {
                "traceback_count": txt.count("Traceback"),
                "oom_count": txt.lower().count("out of memory"),
                "keyboard_interrupt_count": txt.count("KeyboardInterrupt"),
                "tail": txt[-2000:],
            }
    return out


def main():
    report = {
        "host": os.uname().nodename,
        "roots": [root_summary(r) for r in ROOTS],
        "hashes": {},
    }
    for p in HASH_PATHS:
        path = Path(p)
        if path.exists():
            report["hashes"][p] = {"sha256": sha256(path), "size": path.stat().st_size}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
