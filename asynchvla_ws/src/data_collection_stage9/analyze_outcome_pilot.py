from __future__ import annotations

import csv
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path


def sample_label(sample):
    label = sample.get("label")
    if isinstance(label, dict):
        return label.get("label")
    return label


def raw_label(sample):
    return (sample.get("raw_local_label") or {}).get("label")


def terminal_success(sample):
    outcome = sample.get("outcome") or {}
    return bool(outcome.get("terminal_success") or outcome.get("success_within_H") or outcome.get("success_after"))


def terminal_failure(sample):
    outcome = sample.get("outcome") or {}
    return bool(outcome.get("terminal_failure") or outcome.get("terminal_timeout"))


def trace_len(sample):
    outcome = sample.get("outcome") or {}
    trace = outcome.get("horizon_trace") or {}
    return len(trace.get("rewards") or [])


def label_reasons(sample):
    label = sample.get("label") or {}
    return label.get("validated_bad_reasons") or label.get("label_reasons") or []


def raw_reasons(sample):
    raw = sample.get("raw_local_label") or {}
    return raw.get("bad_evidence") or raw.get("label_reasons") or []


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("usage: analyze_outcome_pilot.py DATA_DIR VALIDATION_DIR WORKSPACE_ROOT")
    data = Path(sys.argv[1])
    validation = Path(sys.argv[2])
    workspace = Path(sys.argv[3])
    rows = []
    with (data / "counterfactual_samples.jsonl").open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))

    labels = Counter(sample_label(s) for s in rows)
    raws = Counter(raw_label(s) for s in rows)
    reasons = Counter()
    reasons_phase = Counter()
    reasons_task = Counter()
    phase_counts = Counter((s.get("metadata") or {}).get("parent_phase") for s in rows)
    task_counts = Counter((s.get("metadata") or {}).get("task_name") for s in rows)
    trace_lengths = Counter()
    trace_completeness = Counter()
    examples = {"validated_bad": [], "downgraded_bad": [], "good_strong": [], "ambiguous": []}
    suspicious = []
    state_groups = defaultdict(list)
    for sample in rows:
        state_groups[(sample.get("metadata") or {}).get("state_id")].append(sample)

    for sample in rows:
        lab = sample_label(sample)
        rlab = raw_label(sample)
        meta = sample.get("metadata") or {}
        outcome = sample.get("outcome") or {}
        n = trace_len(sample)
        trace_lengths[str(n)] += 1
        succ = terminal_success(sample)
        fail = terminal_failure(sample)
        done = bool(outcome.get("done_within_H"))
        if n >= 40 or succ or done:
            trace_completeness["complete_or_terminal_before_40"] += 1
        else:
            trace_completeness["short_without_terminal_success_or_done"] += 1

        if lab == "VALIDATED_BAD":
            rs = label_reasons(sample)
            if not rs:
                suspicious.append({"sample_id": sample.get("sample_id"), "issue": "validated_bad_missing_reason"})
            if set(rs) == {"eef_moved_away_from_target_during_approach"}:
                suspicious.append({"sample_id": sample.get("sample_id"), "issue": "validated_bad_eef_only"})
            if succ:
                suspicious.append({"sample_id": sample.get("sample_id"), "issue": "validated_bad_terminal_success"})
            if n < 40 and not (succ or done):
                suspicious.append({"sample_id": sample.get("sample_id"), "issue": "validated_bad_short_trace", "trace_len": n})
            for reason in rs:
                reasons[reason] += 1
                reasons_phase[(reason, meta.get("parent_phase"))] += 1
                reasons_task[(reason, meta.get("task_name"))] += 1
            if len(examples["validated_bad"]) < 8:
                examples["validated_bad"].append({
                    "sample_id": sample.get("sample_id"),
                    "state_id": meta.get("state_id"),
                    "seed": meta.get("simvla_generation_seed"),
                    "phase": meta.get("parent_phase"),
                    "reasons": rs,
                    "terminal_steps": outcome.get("terminal_steps"),
                    "terminal_timeout": outcome.get("terminal_timeout"),
                    "trace_len": n,
                    "same_state": (sample.get("label") or {}).get("same_state_comparison", {}),
                })

        if rlab == "BAD" and lab != "VALIDATED_BAD" and len(examples["downgraded_bad"]) < 8:
            examples["downgraded_bad"].append({
                "sample_id": sample.get("sample_id"),
                "final_label": lab,
                "raw_reasons": raw_reasons(sample),
                "terminal_success": succ,
                "terminal_failure": fail,
                "trace_len": n,
            })

        if lab == "GOOD_STRONG":
            gr = label_reasons(sample)
            if not succ:
                suspicious.append({"sample_id": sample.get("sample_id"), "issue": "good_strong_without_terminal_success"})
            if len(examples["good_strong"]) < 8:
                examples["good_strong"].append({
                    "sample_id": sample.get("sample_id"),
                    "state_id": meta.get("state_id"),
                    "seed": meta.get("simvla_generation_seed"),
                    "phase": meta.get("parent_phase"),
                    "reasons": gr,
                    "terminal_steps": outcome.get("terminal_steps"),
                    "trace_len": n,
                    "reward_sum_H": outcome.get("reward_sum_H"),
                })

        if lab == "AMBIGUOUS" and len(examples["ambiguous"]) < 8:
            examples["ambiguous"].append({
                "sample_id": sample.get("sample_id"),
                "raw_label": rlab,
                "phase": meta.get("parent_phase"),
                "terminal_steps": outcome.get("terminal_steps"),
                "terminal_success": succ,
                "terminal_failure": fail,
                "trace_len": n,
                "raw_reasons": raw_reasons(sample),
            })

    group_summary = []
    for gid, samples in sorted(state_groups.items()):
        lc = Counter(sample_label(x) for x in samples)
        rc = Counter(raw_label(x) for x in samples)
        group_summary.append({
            "state_id": gid,
            "label_counts": dict(lc),
            "raw_counts": dict(rc),
            "terminal_success_count": sum(terminal_success(x) for x in samples),
            "terminal_failure_count": sum(terminal_failure(x) for x in samples),
            "phase": (samples[0].get("metadata") or {}).get("parent_phase"),
            "parent_failed": (samples[0].get("metadata") or {}).get("parent_failed_or_timeout"),
            "distance": (samples[0].get("metadata") or {}).get("distance_to_failure_or_timeout"),
        })

    validated = [s for s in rows if sample_label(s) == "VALIDATED_BAD"]
    good = [s for s in rows if sample_label(s) == "GOOD_STRONG"]
    checks = {
        "no_final_bad_unknown_reason": all(label_reasons(s) for s in validated),
        "no_final_bad_from_eef_away_alone": all(set(label_reasons(s)) != {"eef_moved_away_from_target_during_approach"} for s in validated),
        "some_validated_bad_exists": bool(validated),
        "good_strong_has_terminal_success": all(terminal_success(s) for s in good),
        "ambiguous_used_when_unsure": labels.get("AMBIGUOUS", 0) > 0,
        "same_state_comparison_exists": all(bool((s.get("label") or {}).get("same_state_comparison")) for s in rows),
        "full_h40_trace_or_terminal_before_40": trace_completeness.get("short_without_terminal_success_or_done", 0) == 0,
        "no_zero_step_samples": all(trace_len(s) > 0 for s in rows),
    }

    summary = {
        "dataset_path": str(data),
        "num_samples": len(rows),
        "num_states": len(state_groups),
        "label_counts": dict(labels),
        "raw_label_counts": dict(raws),
        "phase_counts": dict(phase_counts),
        "task_counts": dict(task_counts),
        "validated_bad_reason_counts": dict(reasons),
        "validated_bad_reason_by_phase": {" | ".join(map(str, k)): v for k, v in reasons_phase.items()},
        "validated_bad_reason_by_task": {" | ".join(map(str, k)): v for k, v in reasons_task.items()},
        "trace_length_counts": dict(trace_lengths),
        "trace_completeness": dict(trace_completeness),
        "raw_bad_count": raws.get("BAD", 0),
        "raw_bad_downgraded_count": sum(1 for s in rows if raw_label(s) == "BAD" and sample_label(s) != "VALIDATED_BAD"),
        "suspicious_count": len(suspicious),
        "suspicious_labels": suspicious[:50],
        "same_state_groups": group_summary,
        "examples": examples,
        "checks": checks,
    }

    validation.mkdir(parents=True, exist_ok=True)
    analysis_stem = data.name
    (validation / f"{analysis_stem}_analysis.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    review = validation / f"{analysis_stem}_review"
    review.mkdir(parents=True, exist_ok=True)
    (review / "metrics.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    review_rows = []

    def add_review(sample, bucket):
        meta = sample.get("metadata") or {}
        outcome = sample.get("outcome") or {}
        current = sample.get("current") or {}
        sid = sample.get("sample_id")
        row = {
            "bucket": bucket,
            "sample_id": sid,
            "label": sample_label(sample),
            "raw_label": raw_label(sample),
            "phase": meta.get("parent_phase"),
            "seed": meta.get("simvla_generation_seed"),
            "terminal_steps": outcome.get("terminal_steps"),
            "terminal_success": outcome.get("terminal_success"),
            "terminal_failure": outcome.get("terminal_failure"),
            "terminal_timeout": outcome.get("terminal_timeout"),
            "trace_len": trace_len(sample),
            "reasons": ";".join(label_reasons(sample)),
        }
        for key in ["before_image_path", "after_image_path"]:
            raw_path = current.get(key)
            if raw_path:
                src = Path(raw_path)
                if not src.is_absolute():
                    src = workspace / raw_path
                if src.exists():
                    dest = review / bucket / f"{sid}_{key.replace('_image_path', '')}.png"
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest)
                    row[key] = str(dest)
        review_rows.append(row)

    for sample in validated[:50]:
        add_review(sample, "validated_bad")
    for sample in [s for s in rows if raw_label(s) == "BAD" and sample_label(s) != "VALIDATED_BAD"][:50]:
        add_review(sample, "downgraded_raw_bad")
    for sample in good[:20]:
        add_review(sample, "good_strong")
    for sample in [s for s in rows if sample_label(s) == "AMBIGUOUS"][:20]:
        add_review(sample, "ambiguous")

    if review_rows:
        fieldnames = sorted({k for row in review_rows for k in row})
        with (review / "review_table.csv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(review_rows)
    md = [
        "# Outcome Advantage v2 Review Pack",
        "",
        f"Dataset: `{data}`",
        "",
        "| bucket | sample_id | label | raw_label | phase | seed | terminal_steps | trace_len | reasons |",
        "|---|---|---|---|---|---:|---:|---:|---|",
    ]
    for row in review_rows:
        md.append(
            f"| {row.get('bucket')} | `{row.get('sample_id')}` | {row.get('label')} | {row.get('raw_label')} | "
            f"{row.get('phase')} | {row.get('seed')} | {row.get('terminal_steps')} | {row.get('trace_len')} | {row.get('reasons')} |"
        )
    (review / "review_table.md").write_text("\n".join(md) + "\n")

    print(json.dumps({
        "num_samples": summary["num_samples"],
        "num_states": summary["num_states"],
        "label_counts": summary["label_counts"],
        "raw_label_counts": summary["raw_label_counts"],
        "validated_bad_reason_counts": summary["validated_bad_reason_counts"],
        "trace_length_counts": summary["trace_length_counts"],
        "trace_completeness": summary["trace_completeness"],
        "raw_bad_downgraded_count": summary["raw_bad_downgraded_count"],
        "suspicious_count": summary["suspicious_count"],
        "checks": summary["checks"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
