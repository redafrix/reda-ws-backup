from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from .strict_label_utils import (
    LABEL_AMBIGUOUS,
    LABEL_BAD,
    LABEL_GOOD_STRONG,
    STAGE9_ROOT,
    VALIDATED_BAD,
    copy_if_exists,
    evidence,
    load_datasets,
    quality_score,
    resolve_workspace_path,
    sample_label,
    sample_uid,
    sample_reasons,
    state_id,
    write_csv,
    write_json,
)


DEFAULT_DATASETS = [
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2",
]


def load_strict(path: str | None) -> dict[str, dict[str, Any]]:
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


def choose_samples(rows: list[dict[str, Any]], strict: dict[str, dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    bad_rows = [r for r in rows if sample_label(r) == LABEL_BAD]
    invalid_bad = [
        r for r in bad_rows
        if strict.get(sample_uid(r), {}).get("validation_status") not in {None, VALIDATED_BAD}
    ]
    top_bad = sorted(bad_rows, key=quality_score)[: args.top_bad]
    good = [r for r in rows if sample_label(r) == LABEL_GOOD_STRONG][: args.good_strong]
    amb = [r for r in rows if sample_label(r) == LABEL_AMBIGUOUS][: args.ambiguous]

    selected = []
    seen = set()
    for group_name, group in [
        ("invalid_or_suspicious_bad", invalid_bad),
        ("top_bad", top_bad),
        ("good_strong", good),
        ("ambiguous", amb),
    ]:
        for sample in group:
            sid = sample.get("sample_id")
            key = (group_name, sid)
            if key in seen:
                continue
            seen.add(key)
            item = dict(sample)
            item["_review_group"] = group_name
            selected.append(item)
    return selected


def video_candidates(sample_id: str) -> list[Path]:
    return [
        STAGE9_ROOT / "visual_debug/bad_videos_v1" / f"{sample_id}.mp4",
        STAGE9_ROOT / "visual_debug" / f"{sample_id}.mp4",
    ]


def copy_sample_artifacts(sample: dict[str, Any], strict: dict[str, dict[str, Any]], out_dir: Path) -> dict[str, Any]:
    sid = sample.get("sample_id")
    uid = sample_uid(sample)
    group = sample.get("_review_group") or "samples"
    sample_dir = out_dir / group / str(sid)
    current = sample.get("current") or {}
    dataset_dir = sample.get("_dataset_dir")
    before_src = resolve_workspace_path(current.get("before_image_path"), dataset_dir)
    after_src = resolve_workspace_path(current.get("after_image_path"), dataset_dir)
    before_dst = copy_if_exists(before_src, sample_dir / "before.png")
    after_dst = copy_if_exists(after_src, sample_dir / "after.png")
    video_dst = None
    for candidate in video_candidates(str(sid)):
        video_dst = copy_if_exists(candidate, sample_dir / "replay.mp4")
        if video_dst:
            break

    metric = {
        "review_group": group,
        "dataset": sample.get("_dataset_name"),
        "sample_id": sid,
        "state_id": state_id(sample),
        "label": sample_label(sample),
        "label_reasons": sample_reasons(sample),
        "quality_score": quality_score(sample),
        "strict_validation_status": strict.get(uid, {}).get("validation_status"),
        "strict_failure_reasons": strict.get(uid, {}).get("failure_reasons"),
        "evidence": evidence(sample),
        "before_image": before_dst,
        "after_image": after_dst,
        "replay_video": video_dst,
    }
    write_json(sample_dir / "metrics.json", metric)
    return metric


def write_markdown_table(out_path: Path, metrics: list[dict[str, Any]]) -> None:
    lines = [
        "# Stage 9 Validation Review Pack",
        "",
        "| Group | Dataset | Sample | Label | Strict Status | Reasons | Failures | Before | After | Video |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for m in metrics:
        lines.append(
            "| {group} | {dataset} | `{sid}` | `{label}` | `{status}` | {reasons} | {failures} | {before} | {after} | {video} |".format(
                group=m["review_group"],
                dataset=m["dataset"],
                sid=m["sample_id"],
                label=m["label"],
                status=m.get("strict_validation_status"),
                reasons=", ".join(m.get("label_reasons") or []),
                failures=", ".join(m.get("strict_failure_reasons") or []),
                before=Path(m["before_image"]).name if m.get("before_image") else "",
                after=Path(m["after_image"]).name if m.get("after_image") else "",
                video=Path(m["replay_video"]).name if m.get("replay_video") else "",
            )
        )
    out_path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dirs", nargs="+", default=DEFAULT_DATASETS)
    parser.add_argument("--strict-results", default=str(STAGE9_ROOT / "validation/strict_bad_labels/strict_bad_validation_results.json"))
    parser.add_argument("--out-dir", default=str(STAGE9_ROOT / "validation/review_pack"))
    parser.add_argument("--top-bad", type=int, default=50)
    parser.add_argument("--good-strong", type=int, default=20)
    parser.add_argument("--ambiguous", type=int, default=20)
    args = parser.parse_args()

    rows, _ = load_datasets(args.data_dirs)
    strict = load_strict(args.strict_results)
    selected = choose_samples(rows, strict, args)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    metrics = [copy_sample_artifacts(sample, strict, out_dir) for sample in selected]
    write_json(out_dir / "metrics.json", {
        "input_data_dirs": args.data_dirs,
        "num_selected": len(metrics),
        "selection_counts": dict(Counter(m["review_group"] for m in metrics)),
        "label_counts": dict(Counter(m["label"] for m in metrics)),
        "samples": metrics,
    })
    write_csv(
        out_dir / "review_table.csv",
        [
            {
                "review_group": m["review_group"],
                "dataset": m["dataset"],
                "sample_id": m["sample_id"],
                "state_id": m["state_id"],
                "label": m["label"],
                "label_reasons": "+".join(m.get("label_reasons") or []),
                "strict_validation_status": m.get("strict_validation_status"),
                "strict_failure_reasons": "+".join(m.get("strict_failure_reasons") or []),
                "before_image": m.get("before_image"),
                "after_image": m.get("after_image"),
                "replay_video": m.get("replay_video"),
            }
            for m in metrics
        ],
    )
    write_markdown_table(out_dir / "review_table.md", metrics)
    print(json.dumps({
        "out_dir": str(out_dir),
        "num_selected": len(metrics),
        "selection_counts": dict(Counter(m["review_group"] for m in metrics)),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
