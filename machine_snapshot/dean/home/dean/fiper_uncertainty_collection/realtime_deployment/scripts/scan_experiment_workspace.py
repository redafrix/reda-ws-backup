#!/usr/bin/env python3
"""Build a compact, non-destructive inventory of a FIPER workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


EPISODE_JSONL_RE = re.compile(r"episode.*summar.*\.jsonl$", re.IGNORECASE)
RESULT_JSON_RE = re.compile(r"(metrics|result|summary).*\.json$", re.IGNORECASE)
SKIP_DIRS = {"__pycache__", ".git", ".cache"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_json(values: list[Any]) -> str:
    payload = json.dumps(values, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(payload).hexdigest()


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def iter_files(root: Path) -> Iterable[Path]:
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        base = Path(current)
        for name in files:
            yield base / name


def running_processes(root: Path) -> list[dict[str, Any]]:
    try:
        output = subprocess.check_output(
            ["ps", "-eo", "pid=,etime=,args="], text=True, errors="replace"
        )
    except (OSError, subprocess.SubprocessError):
        return []
    root_text = str(root)
    rows = []
    for line in output.splitlines():
        if root_text not in line:
            continue
        if "scan_experiment_workspace.py" in line:
            continue
        match = re.match(r"\s*(\d+)\s+(\S+)\s+(.*)$", line)
        if match:
            rows.append(
                {
                    "pid": int(match.group(1)),
                    "elapsed": match.group(2),
                    "command": match.group(3),
                }
            )
    return rows


def load_configs(root: Path) -> list[dict[str, Any]]:
    configs = []
    candidates: set[Path] = set()
    for base in (root / "configs", root / "realtime_deployment" / "configs"):
        if base.is_dir():
            candidates.update(base.rglob("*.json"))
    experiments = root / "experiments"
    if experiments.is_dir():
        candidates.update(experiments.rglob("config.json"))
        candidates.update(experiments.rglob("*config*.json"))
    for path in sorted(candidates):
        data = read_json(path)
        if not isinstance(data, dict):
            continue
        seeds = data.get("seeds") or data.get("reset_seeds") or []
        checkpoint = next(
            (
                data[key]
                for key in (
                    "checkpoint",
                    "checkpoint_path",
                    "simvla_checkpoint",
                    "ckpt",
                    "ckpt_path",
                )
                if key in data
            ),
            None,
        )
        configs.append(
            {
                "path": str(path.relative_to(root)),
                "output_dir": data.get("output_dir") or data.get("run_dir"),
                "suite": data.get("suite"),
                "task_id": data.get("task_id"),
                "policy": data.get("policy") or data.get("selection_policy"),
                "checkpoint": checkpoint,
                "num_episodes": data.get("num_episodes") or data.get("episodes"),
                "seed_count": len(seeds) if isinstance(seeds, list) else None,
                "seed_hash": sha256_json(seeds) if isinstance(seeds, list) and seeds else None,
            }
        )
    return configs


def summarize_episode_jsonl(path: Path) -> dict[str, Any]:
    summary = {
        "path": str(path),
        "rows": 0,
        "successes": 0,
        "failures": 0,
        "errors": 0,
        "unique_episode_indexes": 0,
        "unique_reset_seeds": 0,
        "mean_steps": None,
        "parse_errors": 0,
    }
    try:
        if path.stat().st_size > 64 * 1024 * 1024:
            summary["note"] = "not parsed because file exceeds 64 MiB"
            return summary
    except OSError:
        return summary

    indexes: set[Any] = set()
    seeds: set[Any] = set()
    steps: list[float] = []
    try:
        with path.open(errors="replace") as handle:
            for line in handle:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    summary["parse_errors"] += 1
                    continue
                if not isinstance(row, dict):
                    continue
                summary["rows"] += 1
                success = bool(row.get("success", False))
                summary["successes"] += int(success)
                summary["failures"] += int(not success)
                summary["errors"] += int(bool(row.get("error_message") or row.get("error")))
                if "episode_index" in row:
                    indexes.add(row["episode_index"])
                if "reset_seed" in row:
                    seeds.add(row["reset_seed"])
                value = row.get("num_steps", row.get("steps"))
                if isinstance(value, (int, float)):
                    steps.append(float(value))
    except OSError as exc:
        summary["note"] = f"read failed: {exc}"
    summary["unique_episode_indexes"] = len(indexes)
    summary["unique_reset_seeds"] = len(seeds)
    if steps:
        summary["mean_steps"] = sum(steps) / len(steps)
    return summary


def discover_entry_roots(root: Path) -> list[tuple[str, Path]]:
    entries: list[tuple[str, Path]] = []
    seen: set[Path] = set()
    categories = [
        ("offline_experiment", root / "experiments"),
        ("realtime_run", root / "realtime_deployment" / "runs"),
        ("collection_run", root / "runs"),
        ("archive_bundle", root / "archive"),
    ]
    for kind, parent in categories:
        if not parent.is_dir():
            continue
        for child in sorted(parent.iterdir()):
            if child.is_dir() and child.name not in SKIP_DIRS:
                entries.append((kind, child))
                seen.add(child.resolve())

    marker_groups = [
        ("offline_result", root / "experiments", ("metrics.json", "model.pt")),
        (
            "realtime_result",
            root / "realtime_deployment" / "runs",
            ("episode_summary*.jsonl", "episode_summaries*.jsonl"),
        ),
        (
            "collection_result",
            root / "runs",
            ("episode_summary*.jsonl", "episode_summaries*.jsonl"),
        ),
    ]
    for kind, parent, patterns in marker_groups:
        if not parent.is_dir():
            continue
        marker_parents: set[Path] = set()
        for pattern in patterns:
            marker_parents.update(path.parent for path in parent.rglob(pattern))
        for path in sorted(marker_parents):
            resolved = path.resolve()
            if resolved in seen:
                continue
            entries.append((kind, path))
            seen.add(resolved)
    return entries


def matching_configs(
    root: Path, entry: Path, configs: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    rel = str(entry.relative_to(root))
    matches = []
    for config in configs:
        output = config.get("output_dir")
        if output and (str(output).rstrip("/") in rel or rel in str(output).rstrip("/")):
            matches.append(config)
    return matches


def entry_inventory(
    host: str,
    root: Path,
    kind: str,
    entry: Path,
    configs: list[dict[str, Any]],
    processes: list[dict[str, Any]],
) -> dict[str, Any]:
    if kind == "archive_bundle":
        files = []
        for current, dirs, names in os.walk(entry):
            relative_depth = len(Path(current).relative_to(entry).parts)
            if relative_depth >= 2:
                dirs[:] = []
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            files.extend(Path(current) / name for name in names)
    else:
        files = list(iter_files(entry))
    total_bytes = 0
    latest_mtime = 0.0
    extensions: dict[str, int] = {}
    for path in files:
        try:
            stat = path.stat()
        except OSError:
            continue
        total_bytes += stat.st_size
        latest_mtime = max(latest_mtime, stat.st_mtime)
        suffix = path.suffix.lower() or "[none]"
        extensions[suffix] = extensions.get(suffix, 0) + 1

    episode_files = [p for p in files if EPISODE_JSONL_RE.search(p.name)]
    episode_summaries = [summarize_episode_jsonl(p) for p in episode_files]
    for summary in episode_summaries:
        summary["path"] = str(Path(summary["path"]).relative_to(root))

    key_files = []
    for path in files:
        lower = path.name.lower()
        if (
            lower.endswith(".md")
            or lower in {"model.pt", "normalization.json", "thresholds.json", "policy_thresholds.json"}
            or RESULT_JSON_RE.search(lower)
        ):
            key_files.append(str(path.relative_to(root)))

    rel = str(entry.relative_to(root))
    matched_configs = matching_configs(root, entry, configs)
    config_names = {Path(config["path"]).name for config in matched_configs}
    active = [
        process
        for process in processes
        if str(entry) in process["command"]
        or rel in process["command"]
        or any(name in process["command"] for name in config_names)
        or (len(entry.name) >= 20 and entry.name in process["command"])
    ]
    requested = [c.get("num_episodes") for c in matched_configs if c.get("num_episodes")]
    observed = max((s["rows"] for s in episode_summaries), default=0)
    if active:
        status = "active"
    elif requested and observed >= max(requested):
        status = "complete"
    elif observed:
        status = "inactive_with_results"
    elif kind == "archive_bundle":
        status = "archived"
    else:
        status = "artifacts_only_or_unknown"

    return {
        "id": f"{host}:{rel}",
        "host": host,
        "kind": kind,
        "name": entry.name,
        "relative_path": rel,
        "absolute_path": str(entry),
        "status": status,
        "active_processes": active,
        "file_count": len(files),
        "total_bytes": total_bytes,
        "latest_mtime": datetime.fromtimestamp(latest_mtime, timezone.utc).isoformat()
        if latest_mtime
        else None,
        "extensions": dict(sorted(extensions.items())),
        "configs": matched_configs,
        "episode_summaries": episode_summaries,
        "key_files": sorted(key_files)[:200],
    }


def checkpoint_inventory(root: Path) -> list[dict[str, Any]]:
    rows = []
    paths: set[Path] = set()
    for base in (
        root / "checkpoints",
        root / "experiments",
        root / "realtime_deployment" / "dean_artifacts",
    ):
        if base.is_dir():
            paths.update(iter_files(base))
    for path in sorted(paths):
        if path.name not in {"model.pt", "model.safetensors"}:
            continue
        try:
            stat = path.stat()
        except OSError:
            continue
        rows.append(
            {
                "path": str(path.relative_to(root)),
                "size_bytes": stat.st_size,
                "modified_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--host", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    processes = running_processes(root)
    configs = load_configs(root)
    entries = [
        entry_inventory(args.host, root, kind, path, configs, processes)
        for kind, path in discover_entry_roots(root)
    ]
    report_paths: set[Path] = set()
    for base in (root / "reports", root / "realtime_deployment" / "reports"):
        if base.is_dir():
            report_paths.update(iter_files(base))
    experiments = root / "experiments"
    if experiments.is_dir():
        report_paths.update(experiments.rglob("*.md"))
        report_paths.update(experiments.rglob("*.csv"))
    reports = [
        str(path.relative_to(root))
        for path in sorted(report_paths)
        if path.suffix.lower() in {".md", ".csv", ".pdf"}
    ]
    manifest = {
        "schema_version": 1,
        "generated_at": utc_now(),
        "host": args.host,
        "root": str(root),
        "active_processes": processes,
        "entries": entries,
        "configs": configs,
        "reports": reports,
        "checkpoints": checkpoint_inventory(root),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "host": args.host,
                "entries": len(entries),
                "configs": len(configs),
                "reports": len(reports),
                "checkpoints": len(manifest["checkpoints"]),
                "active_processes": len(processes),
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
