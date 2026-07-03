from __future__ import annotations

import argparse
import json
import shutil
import textwrap
from pathlib import Path
from typing import Any

import numpy as np
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:  # pragma: no cover
    Image = None
    ImageDraw = None
    ImageFont = None


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def episode_dirs(raw_root: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for steps in raw_root.rglob("steps.jsonl"):
        ep_dir = steps.parent
        meta_path = ep_dir / "episode_metadata.json"
        summary_path = ep_dir / "summary.json"
        episode_id = ep_dir.name
        for path in [meta_path, summary_path]:
            if path.exists():
                try:
                    data = json.loads(path.read_text())
                    episode_id = str(data.get("episode_id") or episode_id)
                    break
                except Exception:
                    pass
        out[episode_id] = ep_dir
    return out


def resolve_and_load_image(
    path_str: str | None,
    size: tuple[int, int],
    raw_root: Path | None,
    ep_dir: Path | None,
    alt_path_str: str | None = None,
    npz_path_str: str | None = None,
    alt_npz_path_str: str | None = None,
    npz_key: str = "agentview_image"
) -> tuple[Image.Image, str, bool]:
    bob_root = Path("/media/rootalkhatib/My Passport/reda_ws")
    
    def try_file_path(p_str: str | None) -> Path | None:
        if not p_str:
            return None
        p = Path(p_str)
        if p.exists():
            return p
        try_bob = bob_root / p_str
        if try_bob.exists():
            return try_bob
        parts = p.parts
        if 'asynchvla_ws' in parts:
            idx = parts.index('asynchvla_ws')
            rel_path = Path(*parts[idx:])
            if (bob_root / rel_path).exists():
                return bob_root / rel_path
            if rel_path.exists():
                return rel_path
        filename = p.name
        if ep_dir:
            try_ep_img = ep_dir / "images" / filename
            if try_ep_img.exists():
                return try_ep_img
            try_ep = ep_dir / filename
            if try_ep.exists():
                return try_ep
        if raw_root:
            try_raw = raw_root / filename
            if try_raw.exists():
                return try_raw
            if 'broad_mini_failure_v1_20260522_1025' in parts:
                idx = parts.index('broad_mini_failure_v1_20260522_1025')
                rel_part = Path(*parts[idx+1:])
                if (raw_root / rel_part).exists():
                    return raw_root / rel_part
        if ep_dir and 'episodes' in parts:
            idx = parts.index('episodes')
            rel_ep_path = Path(*parts[idx+1:])
            if (ep_dir / rel_ep_path).exists():
                return ep_dir / rel_ep_path
        return None

    # Step A: Try primary
    p_resolved = try_file_path(path_str)
    if p_resolved:
        try:
            return Image.open(p_resolved).convert("RGB").resize(size), str(p_resolved), False
        except Exception:
            pass
            
    # Step B: Try alt
    alt_resolved = try_file_path(alt_path_str)
    if alt_resolved:
        try:
            return Image.open(alt_resolved).convert("RGB").resize(size), f"alt:{alt_resolved}", False
        except Exception:
            pass

    # Step C: Try primary npz
    npz_resolved = try_file_path(npz_path_str)
    if npz_resolved:
        try:
            data = np.load(npz_resolved)
            if npz_key in data:
                img_arr = data[npz_key]
                img_arr = np.ascontiguousarray(img_arr[::-1, ::-1])
                return Image.fromarray(img_arr.astype(np.uint8)).resize(size), f"npz:{npz_resolved}", False
        except Exception:
            pass

    # Step D: Try alt npz
    alt_npz_resolved = try_file_path(alt_npz_path_str)
    if alt_npz_resolved:
        try:
            data = np.load(alt_npz_resolved)
            if npz_key in data:
                img_arr = data[npz_key]
                img_arr = np.ascontiguousarray(img_arr[::-1, ::-1])
                return Image.fromarray(img_arr.astype(np.uint8)).resize(size), f"alt_npz:{alt_npz_resolved}", False
        except Exception:
            pass

    # Step E: Warning panel
    warning_text = "IMAGE MISSING"
    if npz_key == "robot0_eye_in_hand_image":
        warning_text = "WRIST MISSING"
    
    img_warn = Image.new("RGB", size, (180, 40, 40))
    draw = ImageDraw.Draw(img_warn)
    try:
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "DejaVuSans-Bold.ttf"
        ]
        font = None
        for p in paths:
            if Path(p).exists():
                font = ImageFont.truetype(p, 18)
                break
        if font is None:
            font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()
        
    draw.text((10, size[1] // 2 - 10), warning_text, fill=(255, 255, 255), font=font)
    return img_warn, "MISSING_PLACEHOLDER", True


def draw_wrapped(draw: Any, xy: tuple[int, int], text: str, width: int, font: Any, fill=(235, 235, 235), step=16) -> int:
    x, y = xy
    for line in textwrap.wrap(str(text), max(12, width // 8)):
        draw.text((x, y), line, font=font, fill=fill)
        y += step
    return y


def make_sheet(row: dict[str, Any], out_path: Path, raw_root: Path | None, ep_dir: Path | None) -> bool:
    if Image is None or ImageDraw is None:
        return False
    w, h = 220, 220
    info_w = 600
    pad = 10
    canvas = Image.new("RGB", (w * 3 + info_w + pad * 5, h * 2 + pad * 3), (18, 18, 20))
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 13) if ImageFont else None
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 15) if ImageFont else font
    except Exception:
        font = ImageFont.load_default() if ImageFont else None
        title_font = font

    coords = [
        (pad, pad),
        (pad * 2 + w, pad),
        (pad * 3 + w * 2, pad),
        (pad, pad * 2 + h),
        (pad * 2 + w, pad * 2 + h),
        (pad * 3 + w * 2, pad * 2 + h),
    ]

    paths = row.get("paths") or {}
    first = paths.get("first") or {}
    peak = paths.get("peak") or {}
    last = paths.get("last") or {}

    configs = [
        ("first agent", first, "agentview_image", "before_agent_image", "after_agent_image"),
        ("peak agent", peak, "agentview_image", "before_agent_image", "after_agent_image"),
        ("last agent", last, "agentview_image", "after_agent_image", "before_agent_image"),
        ("first wrist", first, "robot0_eye_in_hand_image", "before_wrist_image", "after_wrist_image"),
        ("peak wrist", peak, "robot0_eye_in_hand_image", "before_wrist_image", "after_wrist_image"),
        ("last wrist", last, "robot0_eye_in_hand_image", "after_wrist_image", "before_wrist_image"),
    ]

    for (title, step_obj, npz_key, p_key, alt_key), (x, y) in zip(configs, coords):
        img, _, _ = resolve_and_load_image(
            path_str=step_obj.get(p_key),
            size=(w, h),
            raw_root=raw_root,
            ep_dir=ep_dir,
            alt_path_str=step_obj.get(alt_key),
            npz_path_str=step_obj.get("before_obs_npz"),
            alt_npz_path_str=step_obj.get("after_obs_npz"),
            npz_key=npz_key
        )
        canvas.paste(img, (x, y))
        draw.rectangle((x, y, x + w, y + 22), fill=(0, 0, 0))
        draw.text((x + 5, y + 3), title, font=title_font, fill=(255, 255, 255))

    x = pad * 4 + w * 3
    y = pad
    y = draw_wrapped(draw, (x, y), f"{row.get('episode_id')} chunk {row.get('chunk_index')} steps {row.get('start_step')}-{row.get('end_step')}", info_w, title_font, fill=(255, 235, 160), step=18)
    fields = {
        "risk": row.get("risk_score"),
        "confidence": row.get("confidence"),
        "bin": row.get("risk_bin"),
        "events": row.get("event_types"),
        "peak_step": row.get("peak_step"),
        "phase_counts": row.get("phase_counts"),
        "target": row.get("target_base"),
        "goal": row.get("goal_base"),
    }
    for key, value in fields.items():
        y = draw_wrapped(draw, (x, y + 4), f"{key}: {value}", info_w, font)
    compact_events = []
    for event in row.get("events") or []:
        compact_events.append({
            "type": event.get("event_type"),
            "role": event.get("role"),
            "onset": event.get("onset_step"),
            "severity": event.get("event_severity"),
            "confidence": event.get("event_confidence"),
        })
    draw_wrapped(draw, (x, y + 6), f"event refs: {compact_events}", info_w, font, fill=(220, 220, 220))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path)
    return True


def select_rows(rows: list[dict[str, Any]], top_k: int, low_k: int) -> list[tuple[str, dict[str, Any]]]:
    rows_sorted = sorted(rows, key=lambda r: float(r.get("risk_score", 0.0)), reverse=True)
    selected: list[tuple[str, dict[str, Any]]] = []
    for row in rows_sorted[:top_k]:
        selected.append(("top_risk", row))
    event_rows = [row for row in rows_sorted if row.get("event_types")]
    for row in event_rows[:top_k]:
        selected.append(("event_chunks", row))
    low_rows = list(reversed(rows_sorted[-low_k:])) if low_k > 0 else []
    for row in low_rows:
        selected.append(("low_risk_controls", row))
    seen: set[tuple[str, str, str]] = set()
    out: list[tuple[str, dict[str, Any]]] = []
    for group, row in selected:
        key = (group, str(row.get("episode_id")), str(row.get("chunk_index")))
        if key not in seen:
            seen.add(key)
            out.append((group, row))
    return out


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = load_jsonl(Path(args.chunk_labels))
    out_dir = Path(args.out_dir)
    if out_dir.exists() and not args.no_clean:
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_root = Path(args.raw_root) if args.raw_root else None
    eps = episode_dirs(raw_root) if raw_root else None

    manifest: list[dict[str, Any]] = []
    for group, row in select_rows(rows, args.top_k, args.low_k):
        filename = f"{row.get('episode_id')}_chunk{int(row.get('chunk_index', 0)):04d}.jpg"
        sheet = out_dir / group / filename
        episode_id = row.get("episode_id")
        ep_dir = eps.get(episode_id) if eps else None
        made_sheet = make_sheet(row, sheet, raw_root, ep_dir)
        manifest_row = {
            "group": group,
            "episode_id": row.get("episode_id"),
            "chunk_index": row.get("chunk_index"),
            "start_step": row.get("start_step"),
            "end_step": row.get("end_step"),
            "risk_score": row.get("risk_score"),
            "confidence": row.get("confidence"),
            "risk_bin": row.get("risk_bin"),
            "event_types": row.get("event_types"),
            "sheet": str(sheet) if made_sheet else None,
        }
        manifest.append(manifest_row)

    with (out_dir / "manifest.jsonl").open("w") as f:
        for row in manifest:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")
    summary = {
        "chunk_labels": str(args.chunk_labels),
        "out_dir": str(out_dir),
        "rows_available": len(rows),
        "review_items": len(manifest),
        "pil_available": Image is not None,
    }
    write_json(out_dir / "summary.json", summary)
    report = [
        "# Stage 9 Mini-Failure Review Pack",
        "",
        f"- Source chunk labels: `{args.chunk_labels}`",
        f"- Review items: `{len(manifest)}`",
        f"- Manifest: `{out_dir / 'manifest.jsonl'}`",
        "",
        "Sheets show first/peak/last agent and wrist views when image paths are available.",
    ]
    (out_dir / "README.md").write_text("\n".join(report) + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-labels", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--raw-root", default=None, help="Raw dataset root directory")
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--low-k", type=int, default=20)
    parser.add_argument("--no-clean", action="store_true")
    args = parser.parse_args()
    print(json.dumps(run(args), indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
