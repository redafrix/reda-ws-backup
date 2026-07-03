#!/usr/bin/env python3
"""Merge host manifests into a navigable Markdown experiment catalog."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "__", value).strip("_")


def human_bytes(value: int | None) -> str:
    if value is None:
        return "unknown"
    size = float(value)
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if size < 1024 or unit == "TiB":
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TiB"


def annotation_for(entry: dict[str, Any], rules: list[dict[str, Any]]) -> dict[str, Any]:
    target = f"{entry.get('kind', '')}:{entry.get('relative_path', '')}"
    merged: dict[str, Any] = {}
    for rule in rules:
        if re.search(rule["pattern"], target, re.IGNORECASE):
            merged.update({k: v for k, v in rule.items() if k != "pattern"})
    return merged


def episode_table(summaries: list[dict[str, Any]]) -> str:
    if not summaries:
        return "No episode-summary JSONL was discovered in this entry."
    lines = [
        "| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        mean = row.get("mean_steps")
        lines.append(
            "| `{}` | {} | {} | {} | {} | {} | {} |".format(
                row.get("path", "?"),
                row.get("rows", 0),
                row.get("successes", 0),
                row.get("failures", 0),
                row.get("errors", 0),
                row.get("unique_reset_seeds", 0),
                f"{mean:.2f}" if isinstance(mean, (int, float)) else "-",
            )
        )
    return "\n".join(lines)


def config_table(configs: list[dict[str, Any]]) -> str:
    if not configs:
        return "No configuration was automatically associated with this entry."
    lines = [
        "| Config | Suite/task | Policy | Checkpoint field | Seeds |",
        "|---|---|---|---|---:|",
    ]
    for config in configs:
        suite = config.get("suite") or "?"
        task = config.get("task_id")
        suite_task = f"{suite} / {task}" if task is not None else suite
        lines.append(
            "| `{}` | {} | {} | {} | {} |".format(
                config.get("path", "?"),
                suite_task,
                config.get("policy") or "not declared",
                config.get("checkpoint") or "not declared",
                config.get("seed_count") if config.get("seed_count") is not None else "-",
            )
        )
    return "\n".join(lines)


def entry_readme(entry: dict[str, Any], annotation: dict[str, Any], generated: str) -> str:
    title = entry.get("title") or annotation.get("title") or entry.get("name") or entry["id"]
    meaning = entry.get("meaning") or annotation.get("meaning") or (
        "Purpose not yet semantically verified. Use the listed raw artifacts and reports before drawing conclusions."
    )
    checkpoint = entry.get("checkpoint") or annotation.get("checkpoint") or "not verified"
    trust = entry.get("trust") or annotation.get("trust") or "inventory only; interpretation unverified"
    warning = entry.get("warning") or annotation.get("warning")
    lines = [
        f"# {title}",
        "",
        f"- **Catalog ID:** `{entry['id']}`",
        f"- **Host:** `{entry.get('host', '?')}`",
        f"- **Kind:** `{entry.get('kind', '?')}`",
        f"- **Status:** `{entry.get('status', '?')}`",
        f"- **Original path:** `{entry.get('absolute_path', '?')}`",
        f"- **Checkpoint/model meaning:** {checkpoint}",
        f"- **Trust level:** {trust}",
        f"- **Catalog generated:** {generated}",
        "",
        "## What This Result Means",
        "",
        meaning,
    ]
    if warning:
        lines += ["", "## Important Warning", "", f"> {warning}"]
    if entry.get("active_processes"):
        lines += ["", "## Active Processes At Scan Time", ""]
        for process in entry["active_processes"]:
            lines.append(
                f"- PID `{process.get('pid')}`, elapsed `{process.get('elapsed')}`: `{process.get('command')}`"
            )
    lines += [
        "",
        "## Episode Results",
        "",
        episode_table(entry.get("episode_summaries", [])),
        "",
        "## Associated Configuration",
        "",
        config_table(entry.get("configs", [])),
        "",
        "## Artifact Summary",
        "",
        f"- Files: `{entry.get('file_count', 'unknown')}`",
        f"- Total size: `{human_bytes(entry.get('total_bytes'))}`",
        f"- Latest modification: `{entry.get('latest_mtime') or 'unknown'}`",
    ]
    key_files = entry.get("key_files", [])
    if key_files:
        lines += ["", "### Key Files", ""]
        lines.extend(f"- `{path}`" for path in key_files)
    lines += [
        "",
        "## Navigation",
        "",
        f"Connect to `{entry.get('host', '?')}` and inspect `{entry.get('absolute_path', '?')}`.",
        "Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.",
        "",
    ]
    return "\n".join(lines)


def write_host_index(host: str, entries: list[dict[str, Any]], output: Path) -> None:
    lines = [
        f"# {host.capitalize()} Experiment Index",
        "",
        "| Status | Kind | Experiment | Original path |",
        "|---|---|---|---|",
    ]
    for entry in sorted(entries, key=lambda item: (item.get("status", ""), item.get("relative_path", ""))):
        rel = Path("entries") / host / slug(entry["id"]) / "README.md"
        link = Path("..") / rel
        lines.append(
            f"| `{entry.get('status', '?')}` | `{entry.get('kind', '?')}` | [{entry.get('name', entry['id'])}]({link.as_posix()}) | `{entry.get('absolute_path', '?')}` |"
        )
    output.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifests", nargs="+", required=True, type=Path)
    parser.add_argument("--annotations", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    annotations = load_json(args.annotations)
    rules = annotations.get("rules", [])
    manifests = [load_json(path) for path in args.manifests]
    generated = datetime.now(timezone.utc).isoformat()
    output = args.output_dir

    preserved = {
        "catalog_annotations.json",
        "manifests",
        "README_SCHEMA.md",
        "KEY_RESULTS.md",
        "WORKSPACE_MAP.md",
        "SYNC_STATUS.md",
        "source_reports",
        "source_configs",
    }
    if output.exists():
        for child in output.iterdir():
            if child.name not in preserved:
                if child.is_dir():
                    shutil.rmtree(child)
                else:
                    child.unlink()
    output.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, Any]] = []
    for manifest in manifests:
        entries.extend(manifest.get("entries", []))
    entries.extend(annotations.get("external_entries", []))

    by_host: dict[str, list[dict[str, Any]]] = {}
    for entry in entries:
        host = entry.get("host", "unknown")
        by_host.setdefault(host, []).append(entry)
        entry_dir = output / "entries" / host / slug(entry["id"])
        entry_dir.mkdir(parents=True, exist_ok=True)
        (entry_dir / "README.md").write_text(
            entry_readme(entry, annotation_for(entry, rules), generated)
        )

    host_dir = output / "hosts"
    host_dir.mkdir(parents=True, exist_ok=True)
    for host, host_entries in sorted(by_host.items()):
        write_host_index(host, host_entries, host_dir / f"{host}.md")

    warnings = annotations.get("global_warnings", [])
    readme = [
        "# FIPER Experiment Catalog",
        "",
        "This is the canonical navigation layer for the distributed FIPER, SimVLA, and risk-aware experiments. Original artifacts remain in place so existing scripts and provenance paths are not broken.",
        "",
        "## Start Here",
        "",
        "- [Key results and their actual meaning](KEY_RESULTS.md)",
        "- [Workspace map](WORKSPACE_MAP.md)",
        "- [Synchronization status](SYNC_STATUS.md)",
        "- [Required README schema](README_SCHEMA.md)",
        "- [Artifact index](ARTIFACT_INDEX.md)",
        "- [Entries requiring semantic verification](UNVERIFIED_ENTRIES.md)",
    ]
    for host in sorted(by_host):
        readme.append(f"- [{host.capitalize()} index](hosts/{host}.md): {len(by_host[host])} catalog entries")
    readme += [
        "",
        "## Semantic Corrections",
        "",
    ]
    readme.extend(f"> {warning}" for warning in warnings)
    readme += [
        "",
        "## Status Vocabulary",
        "",
        "- `active`: a matching process was running when the manifest was captured.",
        "- `complete`: observed episode rows met the episode count declared in an associated config.",
        "- `inactive_with_results`: results exist, but automatic completion proof is unavailable.",
        "- `artifacts_only_or_unknown`: model/config/report artifacts exist without a recognized episode summary.",
        "- `archived`: historical material retained for provenance.",
        "- `host_offline_result_known_from_audit`: only a prior audited summary is locally available.",
        "",
        "## Operating Rule",
        "",
        "Never compare two folders based only on names such as `baseline`, `risk_base`, or `vanilla`. Verify the checkpoint, runner, seed manifest, execution horizon, and success semantics recorded in the experiment README.",
        "",
        f"Generated: `{generated}`",
        "",
    ]
    (output / "README.md").write_text("\n".join(readme))

    all_configs = []
    all_reports = []
    all_checkpoints = []
    for manifest in manifests:
        host = manifest.get("host", "unknown")
        all_configs.extend({"host": host, **row} for row in manifest.get("configs", []))
        all_reports.extend({"host": host, "path": row} for row in manifest.get("reports", []))
        all_checkpoints.extend({"host": host, **row} for row in manifest.get("checkpoints", []))
    (output / "inventory.json").write_text(
        json.dumps(
            {
                "generated_at": generated,
                "entries": entries,
                "configs": all_configs,
                "reports": all_reports,
                "checkpoints": all_checkpoints,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    artifact_lines = [
        "# Artifact Index",
        "",
        "## Checkpoints And Detector Models",
        "",
        "| Host | Path | Size |",
        "|---|---|---:|",
    ]
    for row in sorted(all_checkpoints, key=lambda item: (item["host"], item["path"])):
        artifact_lines.append(
            f"| `{row['host']}` | `{row['path']}` | {human_bytes(row.get('size_bytes'))} |"
        )
    artifact_lines += [
        "",
        "## Configurations",
        "",
        "| Host | Path | Suite/task | Policy | Checkpoint field | Seeds |",
        "|---|---|---|---|---|---:|",
    ]
    for row in sorted(all_configs, key=lambda item: (item["host"], item["path"])):
        suite = row.get("suite") or "?"
        task = row.get("task_id")
        suite_task = f"{suite}/{task}" if task is not None else suite
        artifact_lines.append(
            f"| `{row['host']}` | `{row['path']}` | `{suite_task}` | "
            f"`{row.get('policy') or 'not declared'}` | `{row.get('checkpoint') or 'not declared'}` | "
            f"{row.get('seed_count') if row.get('seed_count') is not None else '-'} |"
        )
    artifact_lines += [
        "",
        "## Reports",
        "",
        "| Host | Path |",
        "|---|---|",
    ]
    for row in sorted(all_reports, key=lambda item: (item["host"], item["path"])):
        artifact_lines.append(f"| `{row['host']}` | `{row['path']}` |")
    (output / "ARTIFACT_INDEX.md").write_text("\n".join(artifact_lines) + "\n")

    unverified = []
    for entry in entries:
        note = annotation_for(entry, rules)
        if entry.get("meaning") or note.get("meaning"):
            continue
        unverified.append(entry)
    unverified_lines = [
        "# Entries Requiring Semantic Verification",
        "",
        "These entries are inventoried and navigable, but their exact experimental purpose or checkpoint has not yet been independently reconstructed. They must not be cited as evidence until their README is upgraded with verified semantics.",
        "",
        "| Host | Kind | Status | Entry |",
        "|---|---|---|---|",
    ]
    for entry in sorted(unverified, key=lambda item: (item.get("host", ""), item.get("relative_path", ""))):
        target = Path("entries") / entry.get("host", "unknown") / slug(entry["id"]) / "README.md"
        unverified_lines.append(
            f"| `{entry.get('host', '?')}` | `{entry.get('kind', '?')}` | `{entry.get('status', '?')}` | "
            f"[{entry.get('relative_path', entry['id'])}]({target.as_posix()}) |"
        )
    unverified_lines += ["", f"Total unverified entries: **{len(unverified)}**.", ""]
    (output / "UNVERIFIED_ENTRIES.md").write_text("\n".join(unverified_lines))
    print(
        json.dumps(
            {
                "entries": len(entries),
                "hosts": {host: len(rows) for host, rows in sorted(by_host.items())},
                "configs": len(all_configs),
                "reports": len(all_reports),
                "checkpoints": len(all_checkpoints),
                "output": str(output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
