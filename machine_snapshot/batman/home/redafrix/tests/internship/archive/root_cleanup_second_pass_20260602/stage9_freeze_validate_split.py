#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ALLOWED_LABELS = {"GOOD_STRONG", "GOOD_WEAK", "VALIDATED_BAD", "AMBIGUOUS"}
ALLOWED_BAD_SUBTYPES = {"action_specific", "state_context"}
BAD_EEF_ONLY = {"eef_moved_away_from_target_during_approach"}
PARENT_ONLY_REASONS = {
    "parent_failed",
    "parent_failure",
    "parent_timeout",
    "parent_episode_failed",
    "parent_episode_timeout",
    "repeated_failure_from_parent_only",
}
STRONG_BAD_REASON_PREFIXES = {
    "no_progress_strong",
    "object_dropped",
    "gripper_lost_object",
    "target_moved_away_from_goal",
    "bad_collision_confirmed",
    "done_bad",
    "unrecoverable",
    "repeated_same_state_failure_tail_no_progress",
    "terminal_failure_with_successful_same_state_alternative",
    "target_object_dropped",
    "large_object_height_drop",
    "target_object_moved_away_from_goal",
}
REQUIRED_TRACE_LISTS = [
    "rewards",
    "success_flags",
    "done_flags",
    "eef_positions",
    "target_object_positions",
    "target_object_heights",
    "object_goal_distances",
    "eef_target_distances",
    "gripper_states",
    "contact_summaries",
]


def sample_label(sample: dict[str, Any]) -> str | None:
    label = sample.get("label")
    if isinstance(label, dict):
        return label.get("final_label") or label.get("label")
    if isinstance(label, str):
        return label
    return sample.get("final_label")


def raw_label(sample: dict[str, Any]) -> str | None:
    raw = sample.get("raw_local_label") or {}
    if isinstance(raw, dict):
        return raw.get("label")
    label = sample.get("label") or {}
    if isinstance(label, dict):
        nested = label.get("raw_local_label") or {}
        if isinstance(nested, dict):
            return nested.get("label")
    return sample.get("raw_label")


def label_dict(sample: dict[str, Any]) -> dict[str, Any]:
    label = sample.get("label")
    return label if isinstance(label, dict) else {}


def metadata(sample: dict[str, Any]) -> dict[str, Any]:
    meta = sample.get("metadata")
    return meta if isinstance(meta, dict) else {}


def outcome(sample: dict[str, Any]) -> dict[str, Any]:
    out = sample.get("outcome")
    return out if isinstance(out, dict) else {}


def horizon_trace(sample: dict[str, Any]) -> dict[str, Any]:
    tr = outcome(sample).get("horizon_trace")
    return tr if isinstance(tr, dict) else {}


def label_evidence(sample: dict[str, Any]) -> dict[str, Any]:
    ev = label_dict(sample).get("label_evidence")
    return ev if isinstance(ev, dict) else {}


def same_state_comparison(sample: dict[str, Any]) -> dict[str, Any]:
    comp = label_dict(sample).get("same_state_comparison")
    return comp if isinstance(comp, dict) else {}


def label_reasons(sample: dict[str, Any]) -> list[str]:
    lab = label_dict(sample)
    reasons = lab.get("validated_bad_reasons") or lab.get("label_reasons") or []
    return [str(r) for r in reasons] if isinstance(reasons, list) else []


def raw_reasons(sample: dict[str, Any]) -> list[str]:
    raw = sample.get("raw_local_label") or {}
    if isinstance(raw, dict):
        reasons = raw.get("bad_evidence") or raw.get("label_reasons") or []
        return [str(r) for r in reasons] if isinstance(reasons, list) else []
    return []


def bad_subtype(sample: dict[str, Any]) -> str:
    return str(label_dict(sample).get("bad_subtype") or "unknown")


def trace_len(sample: dict[str, Any]) -> int:
    tr = horizon_trace(sample)
    rewards = tr.get("rewards")
    if isinstance(rewards, list):
        return len(rewards)
    rewards = outcome(sample).get("rewards")
    return len(rewards) if isinstance(rewards, list) else 0


def requested_horizon(sample: dict[str, Any]) -> int:
    tr = horizon_trace(sample)
    value = tr.get("requested_horizon") or outcome(sample).get("H_used") or 40
    try:
        return int(value)
    except (TypeError, ValueError):
        return 40


def terminal_success(sample: dict[str, Any]) -> bool:
    out = outcome(sample)
    tr = horizon_trace(sample)
    return bool(
        out.get("terminal_success")
        or out.get("success_within_H")
        or out.get("success_after")
        or tr.get("terminal_success")
    )


def terminal_done(sample: dict[str, Any]) -> bool:
    out = outcome(sample)
    tr = horizon_trace(sample)
    return bool(out.get("terminal_done") or out.get("done_within_H") or tr.get("terminal_success"))


def terminal_timeout(sample: dict[str, Any]) -> bool:
    out = outcome(sample)
    tr = horizon_trace(sample)
    return bool(out.get("terminal_timeout") or tr.get("terminal_timeout"))


def terminal_failure(sample: dict[str, Any]) -> bool:
    out = outcome(sample)
    tr = horizon_trace(sample)
    return bool(out.get("terminal_failure") or tr.get("terminal_failure") or out.get("terminal_timeout"))


def quality_score(sample: dict[str, Any]) -> float:
    comp = same_state_comparison(sample)
    try:
        return float(comp.get("candidate_quality_score"))
    except (TypeError, ValueError):
        return 0.0


def strong_bad_reason(reasons: list[str]) -> bool:
    for reason in reasons:
        if any(reason == allowed or reason.startswith(allowed + ":") for allowed in STRONG_BAD_REASON_PREFIXES):
            return True
    return False


def stable_state_key(sample: dict[str, Any]) -> tuple[str, str]:
    meta = metadata(sample)
    return (str(sample.get("_chunk_name") or ""), str(meta.get("state_id") or sample.get("state_id") or "missing_state"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def short_sample(sample: dict[str, Any], issue: str | None = None) -> dict[str, Any]:
    meta = metadata(sample)
    out = outcome(sample)
    lab = label_dict(sample)
    tr = horizon_trace(sample)
    return {
        "issue": issue,
        "sample_id": sample.get("sample_id"),
        "chunk": sample.get("_chunk_name"),
        "label": sample_label(sample),
        "raw_label": raw_label(sample),
        "bad_subtype": bad_subtype(sample),
        "reasons": label_reasons(sample),
        "raw_reasons": raw_reasons(sample),
        "task_name": meta.get("task_name"),
        "suite": meta.get("libero_pro_suite_or_task"),
        "perturbation_type": meta.get("perturbation_type"),
        "seed": meta.get("simvla_generation_seed"),
        "state_id": meta.get("state_id"),
        "phase": meta.get("parent_phase"),
        "parent_success": meta.get("parent_episode_success"),
        "parent_failed_or_timeout": meta.get("parent_failed_or_timeout"),
        "distance_to_failure_or_timeout": meta.get("distance_to_failure_or_timeout"),
        "trace_len": trace_len(sample),
        "requested_horizon": requested_horizon(sample),
        "terminal_success": terminal_success(sample),
        "terminal_failure": terminal_failure(sample),
        "terminal_timeout": terminal_timeout(sample),
        "terminal_steps": out.get("terminal_steps") or tr.get("terminal_steps"),
        "reward_sum_H": out.get("reward_sum_H"),
        "same_state_comparison": lab.get("same_state_comparison"),
        "label_evidence": lab.get("label_evidence"),
        "current_image": (sample.get("current") or {}).get("image_path"),
        "frame_paths_count": len(tr.get("frame_paths") or []) if isinstance(tr.get("frame_paths"), list) else 0,
    }


def split_task_id(task_name: str | None) -> int | None:
    if not task_name:
        return None
    m = re.search(r"_task(\d+)$", task_name)
    return int(m.group(1)) if m else None


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def load_samples(data_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    chunks_root = data_root / "chunks"
    chunk_reports: list[dict[str, Any]] = []
    corrupt_rows: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    for chunk_dir in sorted(p for p in chunks_root.iterdir() if p.is_dir()):
        sample_path = chunk_dir / "counterfactual_samples.jsonl"
        summary_path = chunk_dir / "summary.json"
        report = {
            "chunk": chunk_dir.name,
            "path": str(chunk_dir),
            "has_samples": sample_path.exists(),
            "has_summary": summary_path.exists(),
            "num_lines": 0,
            "summary_num_samples": None,
            "summary_selected_states": None,
            "summary_seeds": None,
            "sample_sha256": None,
            "summary_sha256": None,
            "incomplete": False,
            "issues": [],
        }
        if not sample_path.exists():
            report["incomplete"] = True
            report["issues"].append("missing_counterfactual_samples_jsonl")
            chunk_reports.append(report)
            continue
        report["sample_sha256"] = sha256_file(sample_path)
        if summary_path.exists():
            report["summary_sha256"] = sha256_file(summary_path)
            try:
                summary = json.loads(summary_path.read_text())
                report["summary_num_samples"] = summary.get("num_samples")
                report["summary_selected_states"] = summary.get("selected_states")
                report["summary_seeds"] = summary.get("simvla_seeds")
            except Exception as exc:  # noqa: BLE001
                report["incomplete"] = True
                report["issues"].append(f"summary_parse_error:{exc}")
        else:
            report["incomplete"] = True
            report["issues"].append("missing_summary_json")
        with sample_path.open() as f:
            for line_no, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    sample = json.loads(line)
                except Exception as exc:  # noqa: BLE001
                    corrupt_rows.append({"chunk": chunk_dir.name, "line": line_no, "error": str(exc)})
                    continue
                sample["_chunk_name"] = chunk_dir.name
                sample["_source_jsonl"] = str(sample_path)
                samples.append(sample)
                report["num_lines"] += 1
        if report["summary_num_samples"] is not None and report["summary_num_samples"] != report["num_lines"]:
            report["incomplete"] = True
            report["issues"].append(
                f"summary_count_mismatch:{report['summary_num_samples']}!={report['num_lines']}"
            )
        seeds = report.get("summary_seeds")
        selected = report.get("summary_selected_states")
        if isinstance(seeds, list) and isinstance(selected, int):
            expected = selected * len(seeds)
            if expected != report["num_lines"]:
                report["incomplete"] = True
                report["issues"].append(f"selected_states_times_seeds_mismatch:{expected}!={report['num_lines']}")
        chunk_reports.append(report)
    return samples, chunk_reports, corrupt_rows


def validate_samples(samples: list[dict[str, Any]]) -> dict[str, Any]:
    label_counts = Counter()
    raw_label_counts = Counter()
    bad_subtype_counts = Counter()
    bad_reason_counts = Counter()
    bad_reason_by_phase = Counter()
    bad_reason_by_task = Counter()
    task_counts = Counter()
    phase_counts = Counter()
    perturb_counts = Counter()
    seed_counts = Counter()
    trace_len_counts = Counter()
    trace_completeness = Counter()
    frame_counts = Counter()
    suspicious: list[dict[str, Any]] = []
    corrected_suggestions: list[dict[str, Any]] = []
    duplicate_ids: dict[str, list[str]] = defaultdict(list)
    state_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)

    for sample in samples:
        sid = str(sample.get("sample_id") or "")
        duplicate_ids[sid].append(str(sample.get("_source_jsonl")))
        state_groups[stable_state_key(sample)].append(sample)

        lab = sample_label(sample)
        rlab = raw_label(sample)
        meta = metadata(sample)
        label_counts[lab] += 1
        raw_label_counts[rlab] += 1
        task_counts[meta.get("task_name")] += 1
        phase_counts[meta.get("parent_phase")] += 1
        perturb_counts[meta.get("perturbation_type")] += 1
        seed_counts[str(meta.get("simvla_generation_seed"))] += 1
        trace_len_counts[str(trace_len(sample))] += 1
        frames = horizon_trace(sample).get("frame_paths")
        frame_counts[str(len(frames) if isinstance(frames, list) else 0)] += 1

        sample_issues: list[str] = []
        if lab not in ALLOWED_LABELS:
            sample_issues.append(f"invalid_label:{lab}")
        if not label_evidence(sample):
            sample_issues.append("missing_label_evidence")
        if not same_state_comparison(sample):
            sample_issues.append("missing_same_state_comparison")

        tr = horizon_trace(sample)
        n = trace_len(sample)
        h = requested_horizon(sample)
        if n >= h:
            trace_completeness["full_horizon"] += 1
        elif n > 0 and terminal_done(sample) and not terminal_timeout(sample):
            trace_completeness["terminal_before_horizon"] += 1
        else:
            trace_completeness["short_unjustified"] += 1
            sample_issues.append("trace_short_without_terminal_done")
        for key in REQUIRED_TRACE_LISTS:
            values = tr.get(key)
            if not isinstance(values, list):
                sample_issues.append(f"trace_missing_list:{key}")
            elif len(values) != n:
                sample_issues.append(f"trace_length_mismatch:{key}:{len(values)}!={n}")

        if lab == "GOOD_STRONG":
            if not terminal_success(sample):
                sample_issues.append("good_strong_without_terminal_success")
            if not label_reasons(sample):
                sample_issues.append("good_strong_missing_reason")

        if lab == "VALIDATED_BAD":
            reasons = label_reasons(sample)
            subtype = bad_subtype(sample)
            for reason in reasons:
                bad_reason_counts[reason] += 1
                bad_reason_by_phase[(reason, meta.get("parent_phase"))] += 1
                bad_reason_by_task[(reason, meta.get("task_name"))] += 1
            bad_subtype_counts[subtype] += 1
            if not reasons:
                sample_issues.append("validated_bad_missing_reason")
            if subtype not in ALLOWED_BAD_SUBTYPES:
                sample_issues.append(f"validated_bad_unknown_or_invalid_subtype:{subtype}")
            if set(reasons) == BAD_EEF_ONLY:
                sample_issues.append("validated_bad_eef_away_only")
            if any(reason in PARENT_ONLY_REASONS for reason in reasons):
                sample_issues.append("validated_bad_parent_only_reason")
            if not strong_bad_reason(reasons):
                sample_issues.append("validated_bad_no_allowed_strong_reason")
            if terminal_success(sample):
                sample_issues.append("validated_bad_terminal_success")
            if not terminal_failure(sample):
                sample_issues.append("validated_bad_without_terminal_failure")
            comp = same_state_comparison(sample)
            if subtype == "action_specific":
                terminal_success_count = int(comp.get("terminal_success_count") or 0)
                if not (
                    comp.get("has_successful_alternative")
                    or comp.get("has_strong_good_alternative")
                    or terminal_success_count > 0
                ):
                    sample_issues.append("action_specific_bad_without_success_or_strong_good_alternative")
            if subtype == "state_context":
                sibling_count = int(comp.get("num_siblings") or 0)
                failure_count = int(comp.get("terminal_failure_count") or 0)
                if sibling_count <= 0:
                    sample_issues.append("state_context_bad_missing_sibling_count")
                elif not (comp.get("terminal_failure_majority") or failure_count >= max(1, sibling_count // 2 + 1)):
                    sample_issues.append("state_context_bad_without_failure_majority")

        if sample_issues:
            suspicious.append(short_sample(sample, ";".join(sample_issues)))

        suggestion = {
            "sample_id": sample.get("sample_id"),
            "chunk": sample.get("_chunk_name"),
            "original_label": lab,
            "suggested_final_label": "AMBIGUOUS" if sample_issues and lab in {"GOOD_STRONG", "VALIDATED_BAD"} else lab,
            "suggested_bad_subtype": bad_subtype(sample) if lab == "VALIDATED_BAD" and not sample_issues else "unknown",
            "issues": sample_issues,
            "reasons": label_reasons(sample),
            "raw_label": rlab,
            "raw_reasons": raw_reasons(sample),
        }
        corrected_suggestions.append(suggestion)

    duplicate_details = [
        {"sample_id": sid, "count": len(paths), "paths": sorted(set(paths))[:5]}
        for sid, paths in duplicate_ids.items()
        if sid and len(paths) > 1
    ]
    missing_id_count = sum(1 for sid in duplicate_ids if not sid)

    group_issues: list[dict[str, Any]] = []
    group_summary: list[dict[str, Any]] = []
    for (chunk, state_id), group in state_groups.items():
        seeds = [metadata(s).get("simvla_generation_seed") for s in group]
        labels = Counter(sample_label(s) for s in group)
        terminal_successes = sum(terminal_success(s) for s in group)
        terminal_failures = sum(terminal_failure(s) for s in group)
        entry = {
            "chunk": chunk,
            "state_id": state_id,
            "num_candidates": len(group),
            "num_unique_seeds": len(set(seeds)),
            "label_counts": dict(labels),
            "terminal_success_count": terminal_successes,
            "terminal_failure_count": terminal_failures,
            "phase": metadata(group[0]).get("parent_phase"),
            "task_name": metadata(group[0]).get("task_name"),
        }
        group_summary.append(entry)
        if len(group) != 8:
            group_issues.append({**entry, "issue": "same_state_group_not_8_candidates"})
        if len(set(seeds)) != len(group):
            group_issues.append({**entry, "issue": "duplicate_seed_in_same_state_group"})
        for s in group:
            comp = same_state_comparison(s)
            if int(comp.get("num_siblings") or 0) != len(group):
                group_issues.append({**entry, "sample_id": s.get("sample_id"), "issue": "comparison_num_siblings_mismatch"})
                break

    eligible = [
        s
        for s in samples
        if sample_label(s) in {"GOOD_STRONG", "VALIDATED_BAD"}
        and not any(x.get("sample_id") == s.get("sample_id") for x in suspicious)
    ]
    random.seed(9009)
    review: list[dict[str, Any]] = []
    by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in samples:
        by_label[str(sample_label(sample))].append(sample)
    for lab in sorted(by_label):
        choices = by_label[lab][:]
        random.shuffle(choices)
        review.extend(short_sample(s) for s in choices[:12])

    checks = {
        "chunks_complete": None,
        "json_parse_clean": None,
        "no_duplicate_sample_ids": len(duplicate_details) == 0 and missing_id_count == 0,
        "allowed_labels_only": set(label_counts) <= ALLOWED_LABELS,
        "label_evidence_present": all(bool(label_evidence(s)) for s in samples),
        "same_state_comparison_present": all(bool(same_state_comparison(s)) for s in samples),
        "same_state_groups_complete": len(group_issues) == 0,
        "h40_trace_complete_or_terminal_before_h": trace_completeness.get("short_unjustified", 0) == 0,
        "no_unknown_validated_bad": all(bad_subtype(s) in ALLOWED_BAD_SUBTYPES for s in samples if sample_label(s) == "VALIDATED_BAD"),
        "no_eef_away_only_validated_bad": all(set(label_reasons(s)) != BAD_EEF_ONLY for s in samples if sample_label(s) == "VALIDATED_BAD"),
        "no_suspicious_good_or_bad": not any(x["label"] in {"GOOD_STRONG", "VALIDATED_BAD"} for x in suspicious),
        "has_good_strong": label_counts.get("GOOD_STRONG", 0) > 0,
        "has_validated_bad": label_counts.get("VALIDATED_BAD", 0) > 0,
        "training_eligible_samples": len(eligible),
    }
    return {
        "samples": samples,
        "label_counts": dict(label_counts),
        "raw_label_counts": dict(raw_label_counts),
        "bad_subtype_counts": dict(bad_subtype_counts),
        "bad_reason_counts": dict(bad_reason_counts),
        "bad_reason_by_phase": {" | ".join(map(str, k)): v for k, v in bad_reason_by_phase.items()},
        "bad_reason_by_task": {" | ".join(map(str, k)): v for k, v in bad_reason_by_task.items()},
        "task_counts": dict(task_counts),
        "phase_counts": dict(phase_counts),
        "perturbation_counts": dict(perturb_counts),
        "seed_counts": dict(seed_counts),
        "trace_length_counts": dict(trace_len_counts),
        "trace_completeness": dict(trace_completeness),
        "frame_path_count_distribution": dict(frame_counts),
        "suspicious": suspicious,
        "corrected_suggestions": corrected_suggestions,
        "duplicate_details": duplicate_details,
        "missing_sample_id_count": missing_id_count,
        "same_state_group_issues": group_issues,
        "same_state_group_summary": group_summary,
        "random_review": review,
        "checks": checks,
        "eligible_count": len(eligible),
    }


def create_splits(samples: list[dict[str, Any]], freeze_dir: Path) -> dict[str, Any]:
    split_dir = freeze_dir / "splits"
    split_dir.mkdir(parents=True, exist_ok=True)
    by_split: dict[str, list[dict[str, Any]]] = defaultdict(list)

    perturb_counts = Counter(metadata(s).get("perturbation_type") for s in samples)
    holdout_perturbation = None
    if len(perturb_counts) > 1:
        # Hold out a real but not dominant perturbation when possible.
        candidates = [(k, v) for k, v in perturb_counts.items() if k is not None]
        if candidates:
            holdout_perturbation = sorted(candidates, key=lambda kv: (kv[1], str(kv[0])))[0][0]

    task_names = sorted({metadata(s).get("task_name") for s in samples if metadata(s).get("task_name")})
    unseen_tasks = {
        t for t in task_names if split_task_id(t) in {8, 9}
    }
    if not unseen_tasks and task_names:
        unseen_tasks = {task_names[-1]}

    seeds = sorted({metadata(s).get("simvla_generation_seed") for s in samples if metadata(s).get("simvla_generation_seed") is not None})
    unseen_seed_values = {s for s in seeds if isinstance(s, int) and s % 8 == 7}
    if not unseen_seed_values and seeds:
        unseen_seed_values = {seeds[-1]}

    for sample in samples:
        meta = metadata(sample)
        task = meta.get("task_name")
        perturb = meta.get("perturbation_type")
        seed = meta.get("simvla_generation_seed")
        state_id = meta.get("state_id") or sample.get("sample_id")
        row = {
            "sample_id": sample.get("sample_id"),
            "chunk": sample.get("_chunk_name"),
            "source_jsonl": sample.get("_source_jsonl"),
            "state_id": state_id,
            "label": sample_label(sample),
            "bad_subtype": bad_subtype(sample) if sample_label(sample) == "VALIDATED_BAD" else "unknown",
            "task_name": task,
            "perturbation_type": perturb,
            "seed": seed,
            "phase": meta.get("parent_phase"),
        }
        if holdout_perturbation is not None and perturb == holdout_perturbation:
            by_split["test_unseen_perturbation"].append(row)
        elif task in unseen_tasks:
            by_split["test_unseen_task"].append(row)
        elif seed in unseen_seed_values:
            by_split["test_unseen_seed"].append(row)
        else:
            digest = int(hashlib.sha1(str(state_id).encode()).hexdigest()[:8], 16) % 100
            if digest < 10:
                by_split["calib"].append(row)
            elif digest < 20:
                by_split["test_seen_task"].append(row)
            else:
                by_split["train"].append(row)

    for required in ["train", "calib", "test_seen_task", "test_unseen_task", "test_unseen_seed", "test_unseen_perturbation"]:
        by_split.setdefault(required, [])
        write_jsonl(split_dir / f"{required}.jsonl", by_split[required])

    split_counts = {
        name: {
            "num_samples": len(rows),
            "label_counts": dict(Counter(r["label"] for r in rows)),
            "bad_subtype_counts": dict(Counter(r["bad_subtype"] for r in rows if r["label"] == "VALIDATED_BAD")),
            "task_counts": dict(Counter(r["task_name"] for r in rows)),
            "perturbation_counts": dict(Counter(r["perturbation_type"] for r in rows)),
        }
        for name, rows in by_split.items()
    }
    manifest = {
        "split_dir": str(split_dir),
        "holdout_perturbation": holdout_perturbation,
        "unseen_tasks": sorted(unseen_tasks),
        "unseen_seed_values": sorted(unseen_seed_values),
        "split_counts": split_counts,
    }
    write_json(split_dir / "split_manifest.json", manifest)
    return manifest


def render_report(
    data_root: Path,
    freeze_dir: Path,
    chunk_reports: list[dict[str, Any]],
    corrupt_rows: list[dict[str, Any]],
    validation: dict[str, Any],
    splits: dict[str, Any] | None,
    ready: bool,
    proc_checks: dict[str, Any],
) -> str:
    incomplete_chunks = [c for c in chunk_reports if c["incomplete"]]
    checks = validation["checks"].copy()
    checks["chunks_complete"] = len(incomplete_chunks) == 0
    checks["json_parse_clean"] = len(corrupt_rows) == 0
    blocker_lines: list[str] = []
    if incomplete_chunks:
        blocker_lines.append(f"- incomplete chunks: {len(incomplete_chunks)}")
    if corrupt_rows:
        blocker_lines.append(f"- corrupt JSONL rows: {len(corrupt_rows)}")
    for key, value in checks.items():
        if value is False:
            blocker_lines.append(f"- failed check: `{key}`")
    if validation["label_counts"].get("GOOD_STRONG", 0) < 1 or validation["label_counts"].get("VALIDATED_BAD", 0) < 1:
        blocker_lines.append("- missing GOOD_STRONG or VALIDATED_BAD examples")
    if not blocker_lines:
        blocker_lines.append("- none")

    def table_from_counter(title: str, counter: dict[str, Any]) -> list[str]:
        rows = [f"## {title}", "", "| key | count |", "|---|---:|"]
        for k, v in sorted(counter.items(), key=lambda kv: (-int(kv[1]), str(kv[0]))):
            rows.append(f"| `{k}` | {v} |")
        rows.append("")
        return rows

    random_examples = validation["random_review"][:16]
    valid_bad_examples = [r for r in validation["random_review"] if r["label"] == "VALIDATED_BAD"][:8]
    good_examples = [r for r in validation["random_review"] if r["label"] == "GOOD_STRONG"][:8]
    suspicious_examples = validation["suspicious"][:12]

    lines = [
        "# Stage 9 Stop, Validate, Split Report",
        "",
        f"Generated: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
        "## Executive Summary",
        "",
        "- Collection was stopped gracefully: the watchdogs were stopped and Bob's in-flight chunk was allowed to finish before validation.",
        f"- Frozen dataset root: `{data_root}`",
        f"- Freeze manifest/output directory: `{freeze_dir}`",
        f"- Total samples: `{len(validation['samples'])}`",
        f"- Total same-state groups: `{len(validation['same_state_group_summary'])}`",
        f"- Total chunks with JSONL: `{sum(1 for c in chunk_reports if c['has_samples'])}`",
        f"- Incomplete chunks: `{len(incomplete_chunks)}`",
        f"- Corrupt JSONL rows: `{len(corrupt_rows)}`",
        f"- DATASET_READY_FOR_TRAINING = {'YES' if ready else 'NO'}",
        "",
        "## Stop Status",
        "",
        f"- Bob process check after stop: `{proc_checks.get('bob')}`",
        f"- Sam process check after stop: `{proc_checks.get('sam')}`",
        "- No hard kill was used for the Bob collector; the final chunk completed and was analyzed after the watchdog had been stopped.",
        "",
        "## Freeze Snapshot",
        "",
        f"- Dataset root: `{data_root}`",
        f"- Freeze directory: `{freeze_dir}`",
        f"- Chunk manifest: `{freeze_dir / 'chunk_manifest.json'}`",
        f"- Validation summary: `{freeze_dir / 'validation_summary.json'}`",
        f"- Corrected label suggestions: `{freeze_dir / 'corrected_label_suggestions.jsonl'}`",
        f"- Random review samples: `{freeze_dir / 'random_review_samples.jsonl'}`",
        "",
    ]
    lines.extend(table_from_counter("Label Counts", validation["label_counts"]))
    lines.extend(table_from_counter("Raw Label Counts", validation["raw_label_counts"]))
    lines.extend(table_from_counter("VALIDATED_BAD Subtype Counts", validation["bad_subtype_counts"]))
    lines.extend(table_from_counter("VALIDATED_BAD Reason Counts", validation["bad_reason_counts"]))
    lines.extend(table_from_counter("Task Counts", validation["task_counts"]))
    lines.extend(table_from_counter("Phase Counts", validation["phase_counts"]))
    lines.extend(table_from_counter("Perturbation Counts", validation["perturbation_counts"]))
    lines.extend(table_from_counter("Trace Completeness", validation["trace_completeness"]))
    lines.extend(table_from_counter("Frame Path Count Distribution", validation["frame_path_count_distribution"]))

    lines.extend(
        [
            "## Integrity And Label Checks",
            "",
            "| check | result |",
            "|---|---:|",
        ]
    )
    for key, value in sorted(checks.items()):
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            f"- Duplicate sample IDs: `{len(validation['duplicate_details'])}`",
            f"- Missing sample IDs: `{validation['missing_sample_id_count']}`",
            f"- Same-state group issues: `{len(validation['same_state_group_issues'])}`",
            f"- Suspicious GOOD_STRONG / VALIDATED_BAD samples: `{sum(1 for s in validation['suspicious'] if s['label'] in {'GOOD_STRONG', 'VALIDATED_BAD'})}`",
            f"- All suspicious samples across all labels: `{len(validation['suspicious'])}`",
            "",
            "## Correctness Audit",
            "",
            "- `VALIDATED_BAD` was required to have a known subtype, non-empty strong reason, terminal-failure evidence, trace evidence, same-state comparison, and no EEF-away-only reason.",
            "- `GOOD_STRONG` was required to have terminal-success evidence and label evidence.",
            "- Parent episode failure/timeout was checked as metadata only; parent-only reasons were treated as invalid.",
            "- Same-state groups were required to contain eight real SimVLA seed candidates with matching comparison metadata.",
            "- Suspicious strong labels were assigned corrected suggestions to `AMBIGUOUS`; no label was upgraded to BAD during this audit.",
            "",
            "## Random Review Sample",
            "",
            "| label | sample_id | task | phase | seed | reasons | terminal_success | terminal_failure | trace_len |",
            "|---|---|---|---|---:|---|---:|---:|---:|",
        ]
    )
    for row in random_examples:
        reasons = ",".join(row.get("reasons") or [])
        lines.append(
            f"| `{row['label']}` | `{row['sample_id']}` | `{row['task_name']}` | `{row['phase']}` | `{row['seed']}` | `{reasons}` | `{row['terminal_success']}` | `{row['terminal_failure']}` | `{row['trace_len']}` |"
        )
    lines.extend(
        [
            "",
            "## VALIDATED_BAD Examples",
            "",
            "| sample_id | subtype | task | phase | reasons | terminal_failure | same-state summary |",
            "|---|---|---|---|---|---:|---|",
        ]
    )
    for row in valid_bad_examples:
        comp = row.get("same_state_comparison") or {}
        same = f"success_alt={comp.get('has_successful_alternative')}, fail_count={comp.get('terminal_failure_count')}/{comp.get('num_siblings')}"
        lines.append(
            f"| `{row['sample_id']}` | `{row['bad_subtype']}` | `{row['task_name']}` | `{row['phase']}` | `{','.join(row.get('reasons') or [])}` | `{row['terminal_failure']}` | `{same}` |"
        )
    lines.extend(
        [
            "",
            "## GOOD_STRONG Examples",
            "",
            "| sample_id | task | phase | reasons | terminal_success | reward_sum_H | trace_len |",
            "|---|---|---|---|---:|---:|---:|",
        ]
    )
    for row in good_examples:
        lines.append(
            f"| `{row['sample_id']}` | `{row['task_name']}` | `{row['phase']}` | `{','.join(row.get('reasons') or [])}` | `{row['terminal_success']}` | `{row['reward_sum_H']}` | `{row['trace_len']}` |"
        )
    lines.extend(
        [
            "",
            "## Suspicious Samples",
            "",
        ]
    )
    if suspicious_examples:
        lines.extend(["| label | sample_id | issue | task | phase |", "|---|---|---|---|---|"])
        for row in suspicious_examples:
            lines.append(f"| `{row['label']}` | `{row['sample_id']}` | `{row['issue']}` | `{row['task_name']}` | `{row['phase']}` |")
    else:
        lines.append("- None found by the strict audit.")
    lines.extend(["", "## Splits", ""])
    if splits:
        lines.extend(
            [
                f"- Split directory: `{splits['split_dir']}`",
                f"- Unseen perturbation holdout: `{splits['holdout_perturbation']}`",
                f"- Unseen task holdouts: `{splits['unseen_tasks']}`",
                f"- Unseen seed holdouts: `{splits['unseen_seed_values']}`",
                "",
                "| split | samples | GOOD_STRONG | VALIDATED_BAD | GOOD_WEAK | AMBIGUOUS |",
                "|---|---:|---:|---:|---:|---:|",
            ]
        )
        for name, stats in sorted(splits["split_counts"].items()):
            lc = stats["label_counts"]
            lines.append(
                f"| `{name}` | {stats['num_samples']} | {lc.get('GOOD_STRONG', 0)} | {lc.get('VALIDATED_BAD', 0)} | {lc.get('GOOD_WEAK', 0)} | {lc.get('AMBIGUOUS', 0)} |"
            )
    else:
        lines.append("- Final training splits were not created because validation did not pass.")

    lines.extend(
        [
            "",
            "## Blockers",
            "",
            *blocker_lines,
            "",
            "## Final Decision",
            "",
            f"DATASET_READY_FOR_TRAINING = {'YES' if ready else 'NO'}",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def proc_status(host: str, pattern: str) -> str:
    try:
        out = subprocess.run(
            ["ssh", host, f"ps -eo pid,ppid,etime,pcpu,pmem,cmd | egrep '{pattern}' | grep -v egrep | grep -v grep || true"],
            check=False,
            text=True,
            capture_output=True,
            timeout=20,
        )
        text = out.stdout.strip()
        return text if text else "no matching process"
    except Exception as exc:  # noqa: BLE001
        return f"process_check_failed:{exc}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", required=True)
    parser.add_argument("--freeze-root", required=True)
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--duplicate-report-path", required=True)
    args = parser.parse_args()

    data_root = Path(args.data_root)
    freeze_root = Path(args.freeze_root)
    freeze_id = "stage9_stop_validate_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    freeze_dir = freeze_root / freeze_id
    freeze_dir.mkdir(parents=True, exist_ok=False)

    samples, chunk_reports, corrupt_rows = load_samples(data_root)
    validation = validate_samples(samples)
    incomplete_chunks = [c for c in chunk_reports if c["incomplete"]]
    validation["checks"]["chunks_complete"] = len(incomplete_chunks) == 0
    validation["checks"]["json_parse_clean"] = len(corrupt_rows) == 0

    strong_suspicious = [s for s in validation["suspicious"] if s["label"] in {"GOOD_STRONG", "VALIDATED_BAD"}]
    ready = (
        len(samples) > 0
        and not incomplete_chunks
        and not corrupt_rows
        and validation["checks"]["no_duplicate_sample_ids"]
        and validation["checks"]["allowed_labels_only"]
        and validation["checks"]["label_evidence_present"]
        and validation["checks"]["same_state_comparison_present"]
        and validation["checks"]["same_state_groups_complete"]
        and validation["checks"]["h40_trace_complete_or_terminal_before_h"]
        and validation["checks"]["no_unknown_validated_bad"]
        and validation["checks"]["no_eef_away_only_validated_bad"]
        and not strong_suspicious
        and validation["label_counts"].get("GOOD_STRONG", 0) > 0
        and validation["label_counts"].get("VALIDATED_BAD", 0) > 0
    )

    write_json(freeze_dir / "chunk_manifest.json", {"data_root": str(data_root), "chunks": chunk_reports})
    write_json(freeze_dir / "corrupt_rows.json", corrupt_rows)
    write_json(freeze_dir / "duplicate_sample_ids.json", validation["duplicate_details"])
    write_json(freeze_dir / "same_state_group_issues.json", validation["same_state_group_issues"])
    write_json(freeze_dir / "suspicious_samples.json", validation["suspicious"])
    write_jsonl(freeze_dir / "corrected_label_suggestions.jsonl", validation["corrected_suggestions"])
    write_jsonl(freeze_dir / "random_review_samples.jsonl", validation["random_review"])
    summary_for_json = {k: v for k, v in validation.items() if k != "samples"}
    summary_for_json["num_samples"] = len(samples)
    summary_for_json["num_same_state_groups"] = len(validation["same_state_group_summary"])
    summary_for_json["dataset_ready_for_training"] = ready
    write_json(freeze_dir / "validation_summary.json", summary_for_json)

    splits = create_splits(samples, freeze_dir) if ready else None
    proc_checks = {
        "bob": proc_status("pcrobot", "stage9_20h_watchdog|collect_outcome_advantage_dataset|analyze_outcome_pilot|train_stage9"),
        "sam": proc_status("sam", "stage9_20h_watchdog|collect_outcome_advantage_dataset|analyze_outcome_pilot|train_stage9|rsync"),
    }
    report = render_report(data_root, freeze_dir, chunk_reports, corrupt_rows, validation, splits, ready, proc_checks)
    report_path = Path(args.report_path)
    duplicate_report_path = Path(args.duplicate_report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    duplicate_report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    duplicate_report_path.write_text(report)
    print(
        json.dumps(
            {
                "dataset_ready_for_training": ready,
                "freeze_dir": str(freeze_dir),
                "num_samples": len(samples),
                "label_counts": validation["label_counts"],
                "bad_subtype_counts": validation["bad_subtype_counts"],
                "suspicious_count": len(validation["suspicious"]),
                "strong_suspicious_count": len(strong_suspicious),
                "incomplete_chunks": len(incomplete_chunks),
                "corrupt_rows": len(corrupt_rows),
                "splits_created": bool(splits),
                "report_path": str(report_path),
                "duplicate_report_path": str(duplicate_report_path),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
