from __future__ import annotations

import argparse
import json
import random
import textwrap
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


LABEL_VALIDATED_BAD = "VALIDATED_BAD"
LABEL_GOOD_STRONG = "GOOD_STRONG"
LABEL_AMBIGUOUS = "AMBIGUOUS"


def load_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def sample_label(sample: dict[str, Any]) -> str:
    label = sample.get("label") or {}
    if isinstance(label, dict):
        return label.get("final_label") or label.get("label") or ""
    return str(label)


def sample_reasons(sample: dict[str, Any]) -> list[str]:
    label = sample.get("label") or {}
    if not isinstance(label, dict):
        return []
    return list(label.get("validated_bad_reasons") or label.get("label_reasons") or [])


def raw_local(sample: dict[str, Any]) -> dict[str, Any]:
    label = sample.get("label") or {}
    return sample.get("raw_local_label") or (label.get("raw_local_label") if isinstance(label, dict) else {}) or {}


def split_index(split_dir: Path) -> tuple[dict[str, dict[str, Any]], set[str]]:
    rows: dict[str, dict[str, Any]] = {}
    sources: set[str] = set()
    for path in sorted(split_dir.glob("*.jsonl")):
        for row in load_jsonl(path):
            sid = row.get("sample_id")
            if not sid:
                continue
            row["_split"] = path.stem
            rows[sid] = row
            if row.get("source_jsonl"):
                sources.add(row["source_jsonl"])
    return rows, sources


def load_full_samples(split_rows: dict[str, dict[str, Any]], sources: set[str]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    needed = set(split_rows)
    for src in sorted(sources):
        path = Path(src)
        if not path.exists():
            continue
        for sample in load_jsonl(path):
            sid = sample.get("sample_id")
            if sid in needed:
                sample["_split"] = split_rows[sid].get("_split")
                sample["_source_jsonl"] = src
                out[sid] = sample
    return out


def categorize(sample: dict[str, Any]) -> list[str]:
    cats: list[str] = []
    label = sample_label(sample)
    reasons = set(sample_reasons(sample))
    raw = raw_local(sample)
    raw_bad = set(raw.get("bad_evidence") or [])
    raw_good = set(raw.get("strong_good_evidence") or []) | set(raw.get("weak_good_evidence") or [])
    outcome = sample.get("outcome") or {}
    if label == LABEL_VALIDATED_BAD:
        cats.append("validated_bad_random")
        if reasons == {"terminal_failure_with_successful_same_state_alternative"}:
            cats.append("bad_terminal_alt_only")
        if not raw_bad:
            cats.append("bad_no_raw_local_bad")
        if raw_good:
            cats.append("bad_with_local_good_progress")
        if outcome.get("terminal_timeout"):
            cats.append("bad_terminal_timeout")
    elif label == LABEL_GOOD_STRONG:
        cats.append("good_strong_random")
    elif label == LABEL_AMBIGUOUS:
        cats.append("ambiguous_random")
    return cats


def best_sibling_id(sample: dict[str, Any]) -> str | None:
    same = ((sample.get("label") or {}).get("same_state_comparison") or {})
    top = same.get("top_siblings") or []
    if not top:
        return None
    sid = sample.get("sample_id")
    for row in top:
        if row.get("sample_id") != sid:
            return row.get("sample_id")
    return top[0].get("sample_id")


def get_image(path: str | None, size: tuple[int, int] = (320, 320)) -> Image.Image:
    if path and Path(path).exists():
        img = Image.open(path).convert("RGB")
    else:
        img = Image.new("RGB", size, (32, 32, 32))
    return img.resize(size)


def safe_text(value: Any, max_len: int = 500) -> str:
    text = str(value) if value is not None else ""
    text = text.replace("\n", " ")
    return text[:max_len]


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, width: int, font, fill=(255, 255, 255), line_px=18) -> int:
    x, y = xy
    for para in str(text).split("\n"):
        lines = textwrap.wrap(para, width=max(10, width // 8)) or [""]
        for line in lines:
            draw.text((x, y), line, font=font, fill=fill)
            y += line_px
    return y


def metrics_summary(sample: dict[str, Any]) -> dict[str, Any]:
    out = sample.get("outcome") or {}
    raw = raw_local(sample)
    ev = raw.get("numeric_evidence") or {}
    return {
        "reward_sum_H": out.get("reward_sum_H"),
        "terminal_success": out.get("terminal_success"),
        "terminal_failure": out.get("terminal_failure"),
        "terminal_timeout": out.get("terminal_timeout"),
        "terminal_steps": out.get("terminal_steps"),
        "target_to_goal_delta": ev.get("target_to_goal_delta"),
        "target_motion": ev.get("target_motion"),
        "target_height_delta": ev.get("target_height_delta"),
        "target_to_eef_delta": ev.get("target_to_eef_delta"),
    }


def make_contact_sheet(sample: dict[str, Any], sibling: dict[str, Any] | None, out_path: Path, category: str, blind: bool = False) -> str:
    cur = sample.get("current") or {}
    sib_cur = sibling.get("current") if sibling else {}
    w, h = 320, 320
    pad = 12
    info_w = 520
    canvas = Image.new("RGB", (w * 2 + info_w + pad * 4, h * 2 + pad * 3), (18, 18, 20))
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 14)
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
    except Exception:
        font = ImageFont.load_default()
        title_font = font

    panels = [
        ("candidate before", cur.get("before_image_path"), pad, pad),
        ("candidate after", cur.get("after_image_path"), pad + w + pad, pad),
        ("best sibling before", sib_cur.get("before_image_path") if sib_cur else None, pad, pad * 2 + h),
        ("best sibling after", sib_cur.get("after_image_path") if sib_cur else None, pad + w + pad, pad * 2 + h),
    ]
    for title, path, x, y in panels:
        img = get_image(path, (w, h))
        canvas.paste(img, (x, y))
        draw.rectangle((x, y, x + w, y + 24), fill=(0, 0, 0))
        draw.text((x + 6, y + 4), title, font=title_font, fill=(255, 255, 255))

    label = sample.get("label") or {}
    raw = raw_local(sample)
    meta = sample.get("metadata") or {}
    x = pad * 3 + w * 2
    y = pad
    y = draw_wrapped(draw, (x, y), "blind visual audit" if blind else f"category: {category}", info_w, title_font, fill=(255, 235, 160), line_px=20)
    y = draw_wrapped(draw, (x, y + 4), f"sample_id: {sample.get('sample_id')}", info_w, font)
    y = draw_wrapped(draw, (x, y + 4), f"task: {meta.get('task_language')}", info_w, font)
    if blind:
        y = draw_wrapped(draw, (x, y + 4), "No dataset label or simulator evidence is shown in this sheet.", info_w, font)
        if sibling:
            draw_wrapped(draw, (x, y + 4), "The bottom row is a same-state alternative candidate.", info_w, font)
    else:
        y = draw_wrapped(draw, (x, y + 4), f"our_label: {sample_label(sample)} subtype: {label.get('bad_subtype')}", info_w, font)
        y = draw_wrapped(draw, (x, y + 4), f"reasons: {sample_reasons(sample)}", info_w, font)
        y = draw_wrapped(draw, (x, y + 4), f"raw_bad: {raw.get('bad_evidence') or []}", info_w, font)
        y = draw_wrapped(draw, (x, y + 4), f"raw_good: {(raw.get('strong_good_evidence') or []) + (raw.get('weak_good_evidence') or [])}", info_w, font)
        y = draw_wrapped(draw, (x, y + 4), f"metrics: {json.dumps(metrics_summary(sample), sort_keys=True)}", info_w, font)
        if sibling:
            y = draw_wrapped(draw, (x, y + 4), f"sibling_label: {sample_label(sibling)}", info_w, font)
            draw_wrapped(draw, (x, y + 4), f"sibling_metrics: {json.dumps(metrics_summary(sibling), sort_keys=True)}", info_w, font)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path)
    return str(out_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split-dir", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--limit-per-category", type=int, default=80)
    parser.add_argument("--seed", type=int, default=9)
    parser.add_argument("--blind", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    split_rows, sources = split_index(Path(args.split_dir))
    samples = load_full_samples(split_rows, sources)
    by_state: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in samples.values():
        sid = (sample.get("metadata") or {}).get("state_id")
        if sid:
            by_state[sid].append(sample)

    categories: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in samples.values():
        for cat in categorize(sample):
            categories[cat].append(sample)

    rng = random.Random(args.seed)
    manifest_rows = []
    seen = set()
    for cat, rows in sorted(categories.items()):
        rows = list(rows)
        rng.shuffle(rows)
        rows.sort(key=lambda s: 0 if cat.startswith("bad_") else 1)
        take = rows[: args.limit_per_category]
        for sample in take:
            key = (sample.get("sample_id"), cat)
            if key in seen:
                continue
            seen.add(key)
            sibling = None
            bsid = best_sibling_id(sample)
            if bsid and bsid in samples:
                sibling = samples[bsid]
            sheet_path = out_dir / "sheets" / cat / f"{sample.get('sample_id')}.jpg"
            make_contact_sheet(sample, sibling, sheet_path, cat, blind=args.blind)
            label = sample.get("label") or {}
            raw = raw_local(sample)
            meta = sample.get("metadata") or {}
            manifest_rows.append({
                "audit_id": f"{cat}:{sample.get('sample_id')}",
                "category": cat,
                "sample_id": sample.get("sample_id"),
                "state_id": meta.get("state_id"),
                "task_instruction": meta.get("task_language"),
                "task_name": meta.get("task_name"),
                "perturbation_type": meta.get("perturbation_type"),
                "phase": meta.get("parent_phase"),
                "our_label": sample_label(sample),
                "bad_subtype": label.get("bad_subtype"),
                "label_reasons": sample_reasons(sample),
                "raw_bad_evidence": raw.get("bad_evidence") or [],
                "raw_good_evidence": (raw.get("strong_good_evidence") or []) + (raw.get("weak_good_evidence") or []),
                "metrics": metrics_summary(sample),
                "contact_sheet_path": str(sheet_path),
                "source_jsonl": sample.get("_source_jsonl"),
                "blind": bool(args.blind),
            })

    manifest = out_dir / "vlm_audit_manifest.jsonl"
    with manifest.open("w") as f:
        for row in manifest_rows:
            f.write(json.dumps(row, default=str) + "\n")

    summary = {
        "split_dir": args.split_dir,
        "out_dir": str(out_dir),
        "num_split_rows": len(split_rows),
        "num_full_samples": len(samples),
        "source_jsonl_count": len(sources),
        "category_pool_counts": {k: len(v) for k, v in sorted(categories.items())},
        "manifest_count": len(manifest_rows),
        "manifest_category_counts": dict(Counter(r["category"] for r in manifest_rows)),
        "manifest_path": str(manifest),
    }
    (out_dir / "prepare_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
