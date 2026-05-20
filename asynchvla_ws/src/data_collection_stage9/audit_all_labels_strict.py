from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .strict_label_utils import (
    EEF_AWAY_REASON,
    INVALID_BAD,
    LABEL_AMBIGUOUS,
    LABEL_BAD,
    LABEL_GOOD_STRONG,
    LABEL_GOOD_WEAK,
    REDA_WS,
    STAGE9_ROOT,
    VALIDATED_BAD,
    anti_false_bad_checks,
    evidence,
    group_by_state,
    label_distribution,
    load_datasets,
    parent_phase,
    quality_score,
    sample_label,
    sample_uid,
    sample_reasons,
    same_state_summary,
    state_group_key,
    state_id,
    strong_bad_signals,
    strong_good_signals,
    weak_good_signals,
    write_csv,
    write_json,
)


DEFAULT_DATASETS = [
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2",
]


def strict_result_by_sample(path: str | None) -> dict[str, dict[str, Any]]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    data = json.loads(p.read_text())
    out = {}
    for v in data.get("validations", []):
        if v.get("sample_uid"):
            out[v["sample_uid"]] = v
        if v.get("sample_id") and v.get("dataset"):
            out[f"{v['dataset']}:{v['sample_id']}"] = v
    return out


def missed_bad_candidate(sample: dict[str, Any], siblings: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    e = evidence(sample)
    bad = strong_bad_signals(e)
    if not bad:
        return False, []
    if strong_good_signals(e):
        return False, []
    same = same_state_summary(sample, siblings)
    parent = parent_phase(sample).upper()
    if bad == [EEF_AWAY_REASON]:
        if parent not in {"APPROACH", "NEAR_GRASP"}:
            return False, []
        if not same.get("has_better_real_seed"):
            return False, []
    elif not same.get("has_better_real_seed") and not (set(bad) & {"target_object_dropped", "large_object_height_drop", "unstable_state", "confident_bad_contact"}):
        return False, []
    return True, bad


def audit_sample(sample: dict[str, Any], siblings: list[dict[str, Any]], strict_bad_result: dict[str, Any] | None) -> dict[str, Any]:
    label = sample_label(sample)
    e = evidence(sample)
    strong_good = strong_good_signals(e)
    weak_good = weak_good_signals(e)
    bad = strong_bad_signals(e)
    missed_bad, missed_bad_reasons = missed_bad_candidate(sample, siblings)
    same = same_state_summary(sample, siblings)
    anti = anti_false_bad_checks(sample)

    suspicious = []
    suggestion = label
    if label == LABEL_BAD:
        if strict_bad_result:
            suggestion = strict_bad_result.get("corrected_label_suggestion", label)
            if strict_bad_result.get("validation_status") != VALIDATED_BAD:
                suspicious.append("bad_failed_strict_validation")
        else:
            suspicious.append("bad_not_strict_validated")
        if anti.get("bad_reason_unknown"):
            suspicious.append("bad_reason_unknown")
        if anti.get("strong_good_evidence"):
            suspicious.append("bad_has_strong_good_evidence")
    elif label == LABEL_GOOD_STRONG:
        if not strong_good:
            suspicious.append("good_strong_without_recomputed_strong_good")
            suggestion = LABEL_AMBIGUOUS
        if bad:
            suspicious.append("good_strong_has_recomputed_bad_signal")
            suggestion = LABEL_AMBIGUOUS
    elif label == LABEL_GOOD_WEAK:
        if strong_good:
            suspicious.append("good_weak_has_strong_good_signal")
            suggestion = LABEL_GOOD_STRONG
        if missed_bad:
            suspicious.append("good_weak_missed_bad_candidate")
            suggestion = LABEL_BAD
    elif label == LABEL_AMBIGUOUS:
        if strong_good:
            suspicious.append("ambiguous_has_strong_good_signal")
            suggestion = LABEL_GOOD_STRONG
        if missed_bad:
            suspicious.append("ambiguous_missed_bad_candidate")
            suggestion = LABEL_BAD
    else:
        suspicious.append("unknown_label")
        suggestion = LABEL_AMBIGUOUS

    return {
        "dataset": sample.get("_dataset_name"),
        "sample_id": sample.get("sample_id"),
        "state_id": state_id(sample),
        "original_label": label,
        "label_reasons": sample_reasons(sample),
        "recomputed_strong_good": strong_good,
        "recomputed_weak_good": weak_good,
        "recomputed_strong_bad": bad,
        "missed_bad_candidate": missed_bad,
        "missed_bad_reasons": missed_bad_reasons,
        "quality_score": quality_score(sample),
        "same_state_has_better_seed": same.get("has_better_real_seed"),
        "same_state_has_successful_alternative": same.get("has_successful_alternative"),
        "suspicious_flags": suspicious,
        "corrected_label_suggestion": suggestion,
    }


def build_report(rows: list[dict[str, Any]], audits: list[dict[str, Any]], args: argparse.Namespace) -> str:
    before = label_distribution(rows)
    suggestions = Counter(a["corrected_label_suggestion"] for a in audits)
    suspicious_by_label = defaultdict(list)
    missed = []
    for a in audits:
        if a["suspicious_flags"]:
            suspicious_by_label[a["original_label"]].append(a)
        if a["missed_bad_candidate"] and a["original_label"] != LABEL_BAD:
            missed.append(a)

    def compact(items: list[dict[str, Any]], n: int = 20) -> list[dict[str, Any]]:
        out = []
        for a in items[:n]:
            out.append({
                "sample_id": a["sample_id"],
                "dataset": a["dataset"],
                "original_label": a["original_label"],
                "suggestion": a["corrected_label_suggestion"],
                "flags": a["suspicious_flags"],
                "strong_good": a["recomputed_strong_good"],
                "strong_bad": a["recomputed_strong_bad"],
                "same_state_has_better_seed": a["same_state_has_better_seed"],
            })
        return out

    rules_need_changes = bool(
        suspicious_by_label.get(LABEL_BAD)
        or missed
        or len(suspicious_by_label.get(LABEL_GOOD_STRONG, [])) > 0
    )

    lines = [
        "# Stage 9 All Label Audit Report",
        "",
        "Generated: `2026-05-18`",
        "",
        "## Inputs",
        "",
        *[f"- `{d}`" for d in args.data_dirs],
        "",
        "## Label Distribution Before Correction",
        "",
        "```json",
        json.dumps(before, indent=2, sort_keys=True),
        "```",
        "",
        "## Suspicious GOOD_STRONG",
        "",
        "```json",
        json.dumps(compact(suspicious_by_label.get(LABEL_GOOD_STRONG, [])), indent=2, sort_keys=True),
        "```",
        "",
        "## Suspicious GOOD_WEAK",
        "",
        "```json",
        json.dumps(compact(suspicious_by_label.get(LABEL_GOOD_WEAK, [])), indent=2, sort_keys=True),
        "```",
        "",
        "## Suspicious AMBIGUOUS",
        "",
        "```json",
        json.dumps(compact(suspicious_by_label.get(LABEL_AMBIGUOUS, [])), indent=2, sort_keys=True),
        "```",
        "",
        "## Suspicious BAD",
        "",
        "```json",
        json.dumps(compact(suspicious_by_label.get(LABEL_BAD, [])), indent=2, sort_keys=True),
        "```",
        "",
        "## Missed BAD Candidates",
        "",
        f"Count: `{len(missed)}`",
        "",
        "```json",
        json.dumps(compact(missed), indent=2, sort_keys=True),
        "```",
        "",
        "## Corrected Label Suggestion Distribution",
        "",
        "```json",
        json.dumps(dict(suggestions), indent=2, sort_keys=True),
        "```",
        "",
        "## Whether Labeler Rules Need Changes",
        "",
        f"Rules need changes: `{'YES' if rules_need_changes else 'NO'}`",
        "",
        "The most important rule change is to stop accepting EEF-away as BAD unless the saved parent phase is truly APPROACH/NEAR_GRASP, the target parse is confident, same-state real SimVLA alternatives are better, and replay reproduces the bad evidence.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dirs", nargs="+", default=DEFAULT_DATASETS)
    parser.add_argument("--strict-results", default=str(STAGE9_ROOT / "validation/strict_bad_labels/strict_bad_validation_results.json"))
    parser.add_argument("--out-dir", default=str(STAGE9_ROOT / "validation/all_label_audit"))
    parser.add_argument("--report-path", default=str(STAGE9_ROOT / "reports/STAGE9_ALL_LABEL_AUDIT_REPORT.md"))
    args = parser.parse_args()

    rows, _ = load_datasets(args.data_dirs)
    groups = group_by_state(rows)
    strict = strict_result_by_sample(args.strict_results)
    audits = [audit_sample(r, groups.get(state_group_key(r), [r]), strict.get(sample_uid(r))) for r in rows]

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "all_label_audit_results.json", {
        "input_data_dirs": args.data_dirs,
        "label_distribution_before": label_distribution(rows),
        "corrected_label_suggestion_distribution": dict(Counter(a["corrected_label_suggestion"] for a in audits)),
        "suspicious_counts": dict(Counter(flag for a in audits for flag in a["suspicious_flags"])),
        "missed_bad_count": sum(1 for a in audits if a["missed_bad_candidate"] and a["original_label"] != LABEL_BAD),
        "audits": audits,
    })
    write_csv(
        out_dir / "all_label_audit_results.csv",
        [
            {
                "dataset": a["dataset"],
                "sample_id": a["sample_id"],
                "state_id": a["state_id"],
                "original_label": a["original_label"],
                "corrected_label_suggestion": a["corrected_label_suggestion"],
                "suspicious_flags": "+".join(a["suspicious_flags"]),
                "recomputed_strong_good": "+".join(a["recomputed_strong_good"]),
                "recomputed_strong_bad": "+".join(a["recomputed_strong_bad"]),
                "missed_bad_candidate": a["missed_bad_candidate"],
                "same_state_has_better_seed": a["same_state_has_better_seed"],
            }
            for a in audits
        ],
    )

    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(rows, audits, args))
    print(json.dumps({
        "rows": len(rows),
        "suspicious_counts": dict(Counter(flag for a in audits for flag in a["suspicious_flags"])),
        "missed_bad_count": sum(1 for a in audits if a["missed_bad_candidate"] and a["original_label"] != LABEL_BAD),
        "report_path": str(report_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
