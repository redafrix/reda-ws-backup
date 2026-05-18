from __future__ import annotations

import argparse
import json
import os
import traceback
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np

from .label_rules import label_outcome
from .strict_label_utils import (
    DOWNGRADE_TO_AMBIGUOUS,
    INVALID_BAD,
    LABEL_AMBIGUOUS,
    LABEL_BAD,
    NEEDS_MANUAL_REVIEW,
    REDA_WS,
    STAGE9_ROOT,
    VALIDATED_BAD,
    dataset_jsonl_path,
    dataset_name_from_path,
    group_by_state,
    label_distribution,
    load_datasets,
    reason_distribution,
    resolve_workspace_path,
    sample_label,
    sample_uid,
    state_group_key,
    sample_reasons,
    validate_bad_sample,
    write_csv,
    write_json,
    write_jsonl,
)


DEFAULT_DATASETS = [
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2",
]


def load_state_npz(path: Path) -> dict[str, Any]:
    data = np.load(path, allow_pickle=True)
    kind_raw = data["kind"]
    try:
        kind = str(kind_raw.item())
    except Exception:
        kind = str(kind_raw)
    out = {"kind": kind}
    if "flat" in data:
        out["flat"] = np.asarray(data["flat"], dtype=np.float64)
    else:
        raise ValueError(f"state file missing flat array: {path}")
    return out


def env_observation(env) -> dict[str, Any]:
    candidates = [env, getattr(env, "env", None), getattr(env, "base_env", None)]
    for obj in candidates:
        if obj is None:
            continue
        for name in ("_get_observations", "_get_observation", "get_observation"):
            fn = getattr(obj, name, None)
            if callable(fn):
                obs = fn()
                if isinstance(obs, dict):
                    return obs
    raise RuntimeError("could not obtain observation after restoring simulator state")


def task_key(sample: dict[str, Any]) -> tuple[str, int]:
    meta = sample.get("metadata") or {}
    suite = str(meta.get("libero_pro_suite_or_task") or "")
    task_name = str(meta.get("task_name") or "")
    task_id = None
    if "_task" in task_name:
        try:
            task_id = int(task_name.rsplit("_task", 1)[1])
        except ValueError:
            task_id = None
    if task_id is None:
        sid = str(meta.get("state_id") or "")
        import re

        m = re.search(r"_t(\d+)_", sid)
        if m:
            task_id = int(m.group(1))
    if not suite or task_id is None:
        raise ValueError(f"cannot infer suite/task_id from sample {sample.get('sample_id')}")
    return suite, task_id


def replay_one_sample(
    sample: dict[str, Any],
    env_cache: dict[tuple[str, int], Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    from .outcome_metrics import execute_action_chunk
    from .sim_state_utils import set_state
    from .libero_pro_env_utils import make_env

    current = sample.get("current") or {}
    state_path = resolve_workspace_path(current.get("sim_state_path"), sample.get("_dataset_dir"))
    if state_path is None or not state_path.exists():
        return {
            "sample_uid": sample_uid(sample),
            "sample_id": sample.get("sample_id"),
            "status": "missing_state",
            "state_path": str(state_path) if state_path else None,
            "attempts": [],
            "original_bad_reasons": sample_reasons(sample),
        }

    try:
        key = task_key(sample)
        if key not in env_cache:
            env, _bundle = make_env(key[0], key[1], resolution=args.resolution, seed=args.env_seed)
            env.reset()
            env_cache[key] = env
        env = env_cache[key]
        state = load_state_npz(state_path)
        chunk = np.asarray((sample.get("candidate_action") or {}).get("candidate_action_env"), dtype=np.float32)
        if chunk.ndim != 2 or chunk.shape[0] == 0:
            raise ValueError("candidate_action_env missing or empty")

        attempts = []
        for attempt_idx in range(args.replay_attempts):
            for horizon in args.replay_horizons:
                if horizon > len(chunk):
                    attempts.append({
                        "attempt": attempt_idx,
                        "requested_horizon": horizon,
                        "status": "not_available_saved_action_too_short",
                        "available_action_steps": int(len(chunk)),
                    })
                    continue
                set_state(env, state)
                before_obs = env_observation(env)
                outcome = execute_action_chunk(
                    env,
                    chunk[:horizon],
                    int(horizon),
                    before_obs,
                    task_context=(current.get("task_context") or {}),
                    return_after_obs=False,
                )
                label = label_outcome(outcome, task_context=(current.get("task_context") or {}))
                attempts.append({
                    "attempt": attempt_idx,
                    "requested_horizon": int(horizon),
                    "status": "ok",
                    "outcome": outcome,
                    "label": label,
                })
        usable = [a for a in attempts if a.get("status") == "ok"]
        return {
            "sample_uid": sample_uid(sample),
            "sample_id": sample.get("sample_id"),
            "status": "ok" if usable else "no_usable_replay",
            "state_path": str(state_path),
            "attempts": attempts,
            "original_bad_reasons": sample_reasons(sample),
        }
    except Exception as exc:
        return {
            "sample_uid": sample_uid(sample),
            "sample_id": sample.get("sample_id"),
            "status": "error",
            "error": str(exc),
            "traceback": traceback.format_exc(limit=5),
            "attempts": [],
            "original_bad_reasons": sample_reasons(sample),
        }


def replay_bad_samples(bad_rows: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, dict[str, Any]]:
    results = {}
    env_cache: dict[tuple[str, int], Any] = {}
    try:
        selected = bad_rows
        if args.max_replay_bad is not None:
            selected = selected[: args.max_replay_bad]
        for idx, sample in enumerate(selected, 1):
            print(f"[strict-replay] {idx}/{len(selected)} {sample.get('sample_id')}", flush=True)
            results[sample_uid(sample)] = replay_one_sample(sample, env_cache, args)
    finally:
        for env in env_cache.values():
            try:
                env.close()
            except Exception:
                pass
    return results


def corrected_rows_by_dataset(rows_by_dataset: dict[str, list[dict[str, Any]]], validations: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    status_by_id = {v["sample_uid"]: v for v in validations}
    out: dict[str, list[dict[str, Any]]] = {}
    for dataset, rows in rows_by_dataset.items():
        fixed = []
        for row in rows:
            row = json.loads(json.dumps(row, default=str))
            val = status_by_id.get(f"{dataset}:{row.get('sample_id')}")
            if val:
                row.setdefault("strict_validation", val)
                if val["corrected_label_suggestion"] != sample_label(row):
                    row.setdefault("label", {})["strict_corrected_label_suggestion"] = val["corrected_label_suggestion"]
                    row.setdefault("label", {})["strict_validation_status"] = val["validation_status"]
                    row.setdefault("label", {})["strict_validation_failure_reasons"] = val["failure_reasons"]
            fixed.append(row)
        out[dataset] = fixed
    return out


def build_report(
    rows: list[dict[str, Any]],
    validations: list[dict[str, Any]],
    replay_results: dict[str, dict[str, Any]],
    args: argparse.Namespace,
) -> str:
    total_bad = len([r for r in rows if sample_label(r) == LABEL_BAD])
    statuses = Counter(v["validation_status"] for v in validations)
    before_reasons = reason_distribution(rows)
    after_reason_counter = Counter()
    for v in validations:
        if v["validation_status"] == VALIDATED_BAD:
            after_reason_counter["+".join(v["original_bad_reasons"]) if v["original_bad_reasons"] else "unknown"] += 1
    replay_statuses = Counter()
    replay_attempt_statuses = Counter()
    for rr in replay_results.values():
        replay_statuses[rr.get("status")] += 1
        for attempt in rr.get("attempts") or []:
            replay_attempt_statuses[attempt.get("status")] += 1

    valid_examples = [v for v in validations if v["validation_status"] == VALIDATED_BAD][:5]
    bad_examples = [v for v in validations if v["validation_status"] != VALIDATED_BAD][:10]

    can_trust = (
        total_bad > 0
        and statuses.get(VALIDATED_BAD, 0) / max(1, total_bad) >= 0.80
        and statuses.get(INVALID_BAD, 0) == 0
        and statuses.get(DOWNGRADE_TO_AMBIGUOUS, 0) / max(1, total_bad) < 0.20
    )

    def compact(v: dict[str, Any]) -> dict[str, Any]:
        return {
            "sample_id": v["sample_id"],
            "dataset": v["dataset"],
            "status": v["validation_status"],
            "reasons": v["original_bad_reasons"],
            "failures": v["failure_reasons"],
            "parent_phase": v["parent_context"].get("parent_phase"),
            "same_state_has_better_seed": v["same_state_comparison"].get("has_better_real_seed"),
            "replay_status": v.get("replay_status"),
        }

    lines = [
        "# Stage 9 Strict BAD Label Validation Report",
        "",
        f"Generated: `2026-05-18`",
        "",
        "## Inputs",
        "",
        *[f"- `{d}`" for d in args.data_dirs],
        "",
        "## Summary",
        "",
        f"- Total BAD samples audited: `{total_bad}`",
        f"- VALIDATED_BAD: `{statuses.get(VALIDATED_BAD, 0)}`",
        f"- DOWNGRADE_TO_AMBIGUOUS: `{statuses.get(DOWNGRADE_TO_AMBIGUOUS, 0)}`",
        f"- INVALID_BAD: `{statuses.get(INVALID_BAD, 0)}`",
        f"- NEEDS_MANUAL_REVIEW: `{statuses.get(NEEDS_MANUAL_REVIEW, 0)}`",
        f"- BAD labels can be trusted now: `{'YES' if can_trust else 'NO'}`",
        "",
        "## BAD Reasons Before Validation",
        "",
        "```json",
        json.dumps(before_reasons, indent=2, sort_keys=True),
        "```",
        "",
        "## BAD Reasons After Strict Validation",
        "",
        "```json",
        json.dumps(dict(after_reason_counter), indent=2, sort_keys=True),
        "```",
        "",
        "## Replay Results",
        "",
        "```json",
        json.dumps({"sample_replay_status": dict(replay_statuses), "attempt_status": dict(replay_attempt_statuses)}, indent=2, sort_keys=True),
        "```",
        "",
        "## Same-State Comparison Results",
        "",
        "```json",
        json.dumps(
            {
                "bad_with_better_same_state_seed": sum(1 for v in validations if v["same_state_comparison"].get("has_better_real_seed")),
                "bad_with_successful_same_state_seed": sum(1 for v in validations if v["same_state_comparison"].get("has_successful_alternative")),
                "bad_without_better_same_state_seed": sum(1 for v in validations if not v["same_state_comparison"].get("has_better_real_seed")),
            },
            indent=2,
            sort_keys=True,
        ),
        "```",
        "",
        "## Examples Of Valid BAD",
        "",
        "```json",
        json.dumps([compact(v) for v in valid_examples], indent=2, sort_keys=True),
        "```",
        "",
        "## Examples Of Invalid Or Suspicious BAD",
        "",
        "```json",
        json.dumps([compact(v) for v in bad_examples], indent=2, sort_keys=True),
        "```",
        "",
        "## Decision",
        "",
        "Current BAD labels are not trustworthy unless the strict pass rate is at least 80%, replay confirms BAD, and same-state alternatives show the BAD action is truly worse. This run does not approve final collection unless the counts above satisfy those gates.",
        "",
        "Artifacts:",
        f"- `{args.out_dir}/strict_bad_validation_results.json`",
        f"- `{args.out_dir}/strict_bad_validation_results.csv`",
        f"- `{args.out_dir}/corrected_label_suggestions.jsonl`",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dirs", nargs="+", default=DEFAULT_DATASETS)
    parser.add_argument("--out-dir", default=str(STAGE9_ROOT / "validation/strict_bad_labels"))
    parser.add_argument("--report-path", default=str(STAGE9_ROOT / "reports/STAGE9_STRICT_BAD_LABEL_VALIDATION_REPORT.md"))
    parser.add_argument("--write-corrected", action="store_true")
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--replay-attempts", type=int, default=2)
    parser.add_argument("--replay-horizons", nargs="+", type=int, default=[10, 20, 40, 80])
    parser.add_argument("--max-replay-bad", type=int, default=None)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--env-seed", type=int, default=7)
    args = parser.parse_args()

    rows, rows_by_dataset = load_datasets(args.data_dirs)
    groups = group_by_state(rows)
    bad_rows = [r for r in rows if sample_label(r) == LABEL_BAD]

    replay_results = replay_bad_samples(bad_rows, args) if args.replay else {}
    validations = [
        validate_bad_sample(
            sample,
            groups.get(state_group_key(sample), [sample]),
            replay=replay_results.get(sample_uid(sample)),
            require_replay=args.replay,
        )
        for sample in bad_rows
    ]

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "strict_bad_validation_results.json", {
        "input_data_dirs": args.data_dirs,
        "label_distribution_before": label_distribution(rows),
        "bad_reason_distribution_before": reason_distribution(rows),
        "validation_status_counts": dict(Counter(v["validation_status"] for v in validations)),
        "validations": validations,
        "replay_results": replay_results,
    })
    write_csv(
        out_dir / "strict_bad_validation_results.csv",
        [
            {
                "dataset": v["dataset"],
                "sample_id": v["sample_id"],
                "state_id": v["state_id"],
                "seed": v["seed"],
                "original_bad_reasons": "+".join(v["original_bad_reasons"]),
                "validation_status": v["validation_status"],
                "corrected_label_suggestion": v["corrected_label_suggestion"],
                "failure_reasons": "+".join(v["failure_reasons"]),
                "parent_phase": v["parent_context"].get("parent_phase"),
                "same_state_has_better_seed": v["same_state_comparison"].get("has_better_real_seed"),
                "replay_status": v["replay_status"],
            }
            for v in validations
        ],
    )
    write_jsonl(out_dir / "corrected_label_suggestions.jsonl", validations)

    if args.write_corrected:
        corrected = corrected_rows_by_dataset(rows_by_dataset, validations)
        for data_dir in args.data_dirs:
            name = dataset_name_from_path(data_dir)
            src = dataset_jsonl_path(data_dir)
            write_jsonl(src.parent / "counterfactual_samples.strict_corrected.jsonl", corrected[name])

    report = build_report(rows, validations, replay_results, args)
    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    print(json.dumps({
        "bad_samples": len(bad_rows),
        "status_counts": dict(Counter(v["validation_status"] for v in validations)),
        "out_dir": str(out_dir),
        "report_path": str(report_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
