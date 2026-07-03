from __future__ import annotations

import argparse
import json
import shutil
import textwrap
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def image_or_blank(path: str | None, size=(240, 240)) -> Image.Image:
    if path and Path(path).exists():
        return Image.open(path).convert("RGB").resize(size)
    return Image.new("RGB", size, (28, 28, 30))


def text_wrap(draw, xy, text, width, font, fill=(240, 240, 240), step=16):
    x, y = xy
    for line in textwrap.wrap(str(text), max(10, width // 8)):
        draw.text((x, y), line, font=font, fill=fill)
        y += step
    return y


def make_sheet(row: dict[str, Any], out_path: Path) -> None:
    current = row.get("current") or {}
    visual = row.get("visual_evidence") or {}
    label = row.get("label") or {}
    meta = row.get("metadata") or {}
    panels = [
        ("before agent", current.get("before_image_path")),
        ("after agent", visual.get("after_image_path") or current.get("after_image_path")),
        ("before wrist", current.get("before_wrist_image_path")),
        ("after wrist", visual.get("after_wrist_image_path")),
    ]
    w, h = 240, 240
    info_w = 500
    pad = 10
    canvas = Image.new("RGB", (w * 2 + info_w + pad * 4, h * 2 + pad * 3), (18, 18, 20))
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 13)
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 15)
    except Exception:
        font = ImageFont.load_default()
        title_font = font
    coords = [(pad, pad), (pad * 2 + w, pad), (pad, pad * 2 + h), (pad * 2 + w, pad * 2 + h)]
    for (title, path), (x, y) in zip(panels, coords):
        img = image_or_blank(path, (w, h))
        canvas.paste(img, (x, y))
        draw.rectangle((x, y, x + w, y + 22), fill=(0, 0, 0))
        draw.text((x + 5, y + 3), title, font=title_font, fill=(255, 255, 255))
    x = pad * 3 + w * 2
    y = pad
    y = text_wrap(draw, (x, y), f"sample: {row.get('sample_id')}", info_w, title_font, fill=(255, 235, 160), step=18)
    fields = {
        "task": meta.get("task_language"),
        "phase": meta.get("parent_phase"),
        "risk": label.get("risk_score"),
        "confidence": label.get("risk_confidence"),
        "bin": label.get("risk_bin"),
        "subtype": label.get("bad_subtype"),
        "positive": label.get("positive_evidence"),
        "negative": label.get("negative_evidence"),
        "weak_negative": label.get("weak_negative_evidence"),
        "same_state": label.get("same_state_comparison_v2"),
    }
    for key, value in fields.items():
        y = text_wrap(draw, (x, y + 4), f"{key}: {value}", info_w, font)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jsonl", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--top-k", type=int, default=40)
    args = parser.parse_args()
    rows = load_jsonl(Path(args.jsonl))
    rows.sort(key=lambda r: float((r.get("label") or {}).get("risk_score", 0.5)), reverse=True)
    high = rows[: args.top_k]
    low = list(reversed(rows[-args.top_k:]))
    out = Path(args.out_dir)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    manifest = []
    for group, selected in [("high_risk", high), ("low_risk", low)]:
        for row in selected:
            sheet = out / group / f"{row.get('sample_id')}.jpg"
            make_sheet(row, sheet)
            manifest.append({
                "group": group,
                "sample_id": row.get("sample_id"),
                "risk_score": (row.get("label") or {}).get("risk_score"),
                "risk_bin": (row.get("label") or {}).get("risk_bin"),
                "sheet": str(sheet),
            })
    with (out / "manifest.jsonl").open("w") as f:
        for row in manifest:
            f.write(json.dumps(row, sort_keys=True) + "\n")
    report = f"""# Stage 9 Continuous Risk Review Pack

- Source: `{args.jsonl}`
- High-risk sheets: `{len(high)}`
- Low-risk sheets: `{len(low)}`
- Manifest: `{out / 'manifest.jsonl'}`

Sheets show agent and wrist before/after views plus continuous risk evidence.
"""
    (out / "README.md").write_text(report)
    print(json.dumps({"status": "ok", "out_dir": str(out), "items": len(manifest)}, indent=2))


if __name__ == "__main__":
    main()
