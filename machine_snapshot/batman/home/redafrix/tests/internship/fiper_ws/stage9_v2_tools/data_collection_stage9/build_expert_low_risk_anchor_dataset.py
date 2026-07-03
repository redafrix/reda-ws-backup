from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for row in rows:
            f.write(json.dumps(row, default=str) + "\n")


def task_language_from_file(path: Path) -> str:
    name = path.name
    name = re.sub(r"_demo\.hdf5$", "", name)
    name = re.sub(r"^[A-Z_0-9]+_", "", name)
    return name.replace("_", " ")


def save_image(path: Path, arr) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(np.asarray(arr).astype(np.uint8)).save(path)
    return str(path)


def risk_anchor_label() -> dict[str, Any]:
    return {
        "label_schema": "continuous_risk_v2_expert_anchor",
        "risk_score": 0.05,
        "risk_confidence": 0.90,
        "chunk_quality": 0.95,
        "risk_bin": "SAFE_STRONG",
        "legacy_label_suggestion": "GOOD_STRONG",
        "bad_subtype": "unknown",
        "positive_evidence": ["libero_expert_demonstration", "expert_success_trajectory_anchor"],
        "negative_evidence": [],
        "weak_negative_evidence": [],
        "ambiguous_evidence": [],
        "risk_components": {
            "expert_anchor_credit": 1.0,
            "local_damage_risk": 0.0,
            "no_progress_risk": 0.0,
            "same_state_disadvantage_risk": 0.0,
            "expert_deviation_risk": 0.0,
            "failure_onset_risk": 0.0,
            "local_progress_credit": 1.0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--glob", default="**/*demo.hdf5")
    parser.add_argument("--max-files", type=int, default=10)
    parser.add_argument("--max-demos-per-file", type=int, default=5)
    parser.add_argument("--chunk-steps", type=int, default=10)
    parser.add_argument("--stride", type=int, default=10)
    parser.add_argument("--save-images", action="store_true")
    args = parser.parse_args()

    import h5py

    root = Path(args.dataset_root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_jsonl = out_dir / "expert_low_risk_anchors.jsonl"
    if out_jsonl.exists():
        out_jsonl.unlink()

    paths = sorted(root.glob(args.glob))[: args.max_files]
    counts = Counter()
    rows_buffer: list[dict[str, Any]] = []
    for file_idx, path in enumerate(paths):
        task_language = task_language_from_file(path)
        with h5py.File(path, "r") as h5:
            demos = sorted(h5["data"].keys())[: args.max_demos_per_file]
            for demo_name in demos:
                demo = h5["data"][demo_name]
                actions = np.asarray(demo["actions"])
                rewards = np.asarray(demo["rewards"]) if "rewards" in demo else np.zeros((len(actions),), dtype=float)
                dones = np.asarray(demo["dones"]) if "dones" in demo else np.zeros((len(actions),), dtype=float)
                obs = demo.get("obs")
                n = len(actions)
                for start in range(0, max(0, n - args.chunk_steps + 1), args.stride):
                    end = min(n, start + args.chunk_steps)
                    sid = f"expert_f{file_idx:03d}_{path.stem}_{demo_name}_s{start:04d}_e{end:04d}"
                    before_agent = after_agent = before_wrist = after_wrist = None
                    if args.save_images and obs is not None:
                        if "agentview_rgb" in obs:
                            before_agent = save_image(out_dir / "images" / f"{sid}_before_agent.png", obs["agentview_rgb"][start])
                            after_agent = save_image(out_dir / "images" / f"{sid}_after_agent.png", obs["agentview_rgb"][end - 1])
                        if "eye_in_hand_rgb" in obs:
                            before_wrist = save_image(out_dir / "images" / f"{sid}_before_wrist.png", obs["eye_in_hand_rgb"][start])
                            after_wrist = save_image(out_dir / "images" / f"{sid}_after_wrist.png", obs["eye_in_hand_rgb"][end - 1])
                    row = {
                        "schema_version": "stage9_expert_low_risk_anchor_v1",
                        "sample_id": sid,
                        "metadata": {
                            "task_language": task_language,
                            "source_hdf5": str(path),
                            "demo_name": demo_name,
                            "chunk_start": int(start),
                            "chunk_end": int(end),
                            "chunk_steps": int(end - start),
                            "source": "libero_expert_demonstration",
                        },
                        "candidate_action": {
                            "candidate_action_env": actions[start:end].astype(float).tolist(),
                            "source_policy": "LIBERO_expert",
                        },
                        "outcome": {
                            "reward_sum_H": float(np.sum(rewards[start:end])),
                            "done_within_H": bool(np.any(dones[start:end])),
                            "success_after": bool(np.any(rewards[start:end] > 0)),
                            "success_within_H": bool(np.any(rewards[start:end] > 0)),
                            "H_used": int(end - start),
                            "steps_executed": int(end - start),
                        },
                        "current": {
                            "before_image_path": before_agent,
                            "before_wrist_image_path": before_wrist,
                        },
                        "visual_evidence": {
                            "after_image_path": after_agent,
                            "after_wrist_image_path": after_wrist,
                        },
                        "label": risk_anchor_label(),
                        "continuous_risk": risk_anchor_label(),
                        "labeling_policy": {
                            "label_target": "expert_action_chunk",
                            "expert_demo_used_as_low_risk_anchor": True,
                            "bad_label_source": False,
                        },
                    }
                    rows_buffer.append(row)
                    counts["samples"] += 1
                    if len(rows_buffer) >= 1000:
                        append_jsonl(out_jsonl, rows_buffer)
                        rows_buffer = []
                counts["demos"] += 1
        counts["files"] += 1
    if rows_buffer:
        append_jsonl(out_jsonl, rows_buffer)

    summary = {
        "schema_version": "stage9_expert_low_risk_anchor_summary_v1",
        "dataset_root": str(root),
        "out_dir": str(out_dir),
        "output_jsonl": str(out_jsonl),
        "counts": dict(counts),
        "risk_score": 0.05,
        "risk_confidence": 0.90,
        "note": "Expert anchors are clean low-risk positives only. They do not create BAD labels.",
    }
    write_json(out_dir / "summary.json", summary)
    report = f"""# Stage 9 Expert Low-Risk Anchor Dataset

- Source root: `{root}`
- Files processed: `{counts['files']}`
- Demos processed: `{counts['demos']}`
- Expert chunks written: `{counts['samples']}`
- Output: `{out_jsonl}`

These expert chunks are low-risk anchors with `risk_score=0.05`, `risk_confidence=0.90`.
They are not BAD labels and should not be used as proof of failure.
"""
    (out_dir / "STAGE9_EXPERT_LOW_RISK_ANCHOR_REPORT.md").write_text(report)
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
