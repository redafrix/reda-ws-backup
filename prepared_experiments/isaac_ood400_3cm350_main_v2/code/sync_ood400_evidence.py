#!/usr/bin/env python3
"""Synchronize OOD400 Evidence, Paper Tables, Experiment Map, and Publication Repo.

Generates:
- PAPER_EVIDENCE_INDEX.md and PAPER_EVIDENCE_INDEX.json
- OOD400_OFFLINE_PAPER_TABLE.md
- OOD400_BASELINE_VS_TOPK_TABLE.md
- Experiment catalog entries across isaac_experiment_map/ and fiper_ws/
- Real publication repository ledger update, file mirroring, Git commit & push
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
PUBLICATION_REPO = Path(os.environ.get("U_VOWEL_PUBLICATION_REPO", "/home/redafrix/tests/u_vowel_publication_clean"))
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import sha256_file


def run_cmd(cmd: list[str], cwd: Path | None = None) -> str:
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
    return res.stdout.strip()


def sync_evidence(
    *,
    exp_dir: Path,
    publication_repo: Path = PUBLICATION_REPO,
) -> dict[str, Any]:
    exp_dir = Path(exp_dir).resolve()
    repo_root = Path(__file__).resolve().parents[3]  # /home/redafrix/tests/internship
    publication_repo = Path(publication_repo).resolve()

    baseline_dir = exp_dir / "baseline"
    offline_dir = exp_dir / "offline_eval"
    active_dir = exp_dir / "active_eval"

    # Load artifacts
    base_res = json.loads((baseline_dir / "BASELINE_RESULT.json").read_text(encoding="utf-8"))
    metrics_res = json.loads((offline_dir / "OOD400_MODEL_METRICS.json").read_text(encoding="utf-8"))
    a_sel = json.loads((offline_dir / "ONLINE_A_SELECTION.json").read_text(encoding="utf-8"))
    controller_spec = json.loads((active_dir / "FROZEN_CONTROLLER.json").read_text(encoding="utf-8"))
    active_res = json.loads((active_dir / "ACTIVE_RESULT.json").read_text(encoding="utf-8"))
    paired_comp = json.loads((active_dir / "PAIRED_COMPARISON.json").read_text(encoding="utf-8"))
    base_vid_manifest = json.loads((baseline_dir / "OOD400_BASELINE_VIDEO_MANIFEST.json").read_text(encoding="utf-8"))
    active_vid_manifest = json.loads((active_dir / "OOD400_TOPK_VIDEO_MANIFEST.json").read_text(encoding="utf-8"))

    # 1. Generate OOD400_OFFLINE_PAPER_TABLE.md
    sweep_data = json.loads((offline_dir / "OOD400_THRESHOLD_SWEEP.json").read_text(encoding="utf-8"))
    primary_names = ["Best F1", "Fixed 0.5", "q90 success", "q95 success", "q99 success"]
    primary_rows = [r for r in sweep_data if r["rule_name"] in primary_names]

    offline_table_lines = [
        "# OOD400 Offline Conformal Risk Monitor Operating Points Table",
        "",
        "| Operating Point | Threshold (tau) | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@MeanSucc100 % | Never % |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in primary_rows:
        offline_table_lines.append(
            f"| {r['rule_name']} | {r['threshold']:.4f} | {r['succ_false_alarm_pct']:.2f}% | "
            f"{r['fail_detection_pct']:.2f}% | {r['det_at_25_pct']:.2f}% | {r['det_at_50_pct']:.2f}% | "
            f"{r['det_at_100_pct']:.2f}% | {r['det_at_mean_succ_100_pct']:.2f}% | {r['never_pct']:.2f}% |"
        )
    (exp_dir / "OOD400_OFFLINE_PAPER_TABLE.md").write_text("\n".join(offline_table_lines) + "\n")

    # 2. Generate OOD400_BASELINE_VS_TOPK_TABLE.md
    paired_table_lines = [
        "# OOD400 Paired Evaluation: Normal SimVLA vs TopK Active SimVLA",
        "",
        f"**Protocol**: 3.0 cm threshold, 350 control commands max, 0 dwell, 400 canonical OOD scenes.",
        f"**Operating Point**: A = {a_sel['selected_threshold_a']:.4f} ({a_sel['selected_rule_name']}), C = 0.90, M = 0.0.",
        "",
        "| Normal SimVLA Baseline | TopK SimVLA Active | Delta (pp) | Rescues | Regressions | Persisted Success | Persisted Failure |",
        "|---|---|---|---|---|---|---|",
        f"| {paired_comp['baseline_successes']}/400 ({paired_comp['baseline_success_rate']*100:.2f}%) | "
        f"{paired_comp['active_successes']}/400 ({paired_comp['active_success_rate']*100:.2f}%) | "
        f"{paired_comp['delta_percentage_points']:+.2f} pp | "
        f"{paired_comp['matrix']['rescues']} | {paired_comp['matrix']['regressions']} | "
        f"{paired_comp['matrix']['persisted_success']} | {paired_comp['matrix']['persisted_failure']} |",
    ]
    (exp_dir / "OOD400_BASELINE_VS_TOPK_TABLE.md").write_text("\n".join(paired_table_lines) + "\n")

    # 3. Master PAPER_EVIDENCE_INDEX
    index_md_lines = [
        "# Master OOD400 Canonical Benchmark Evidence Package",
        "",
        f"- **Benchmark**: `reaching_mimic_risk_ood400` (400 canonical scenes)",
        f"- **Manifest SHA256**: `{controller_spec['locked_hashes']['manifest_sha256']}`",
        f"- **Task Protocol**: 3.0 cm immediate success (0 dwell), max 350 control ticks (1400 sim steps @ 120Hz/30Hz/decimation 4), H10 execution",
        f"- **Risk Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2` (SHA256: `{controller_spec['locked_hashes']['model_sha256']}`)",
        f"- **Selected Operating Point**: {a_sel['selected_rule_name']} (A = {a_sel['selected_threshold_a']:.6f}, C = 0.90, M = 0.0)",
        f"- **Operating Point Provenance**: {a_sel['provenance_statement']}",
        "",
        "## Summary Results",
        f"- **Normal SimVLA Baseline**: {base_res['success_count']}/400 ({base_res['success_rate']*100:.2f}%)",
        f"- **TopK Active SimVLA**: {active_res['success_count']}/400 ({active_res['success_rate']*100:.2f}%)",
        f"- **Improvement**: {paired_comp['delta_percentage_points']:+.2f} pp (+{paired_comp['delta_episodes']} episodes net)",
        f"- **Rescues**: {paired_comp['matrix']['rescues']} | **Regressions**: {paired_comp['matrix']['regressions']}",
        f"- **Persisted Success**: {paired_comp['matrix']['persisted_success']} | **Persisted Failure**: {paired_comp['matrix']['persisted_failure']}",
        f"- **Offline Monitor AUROC**: Query AUROC = {metrics_res['query_metrics']['auroc']:.4f}, Episode AUROC = {metrics_res['episode_balanced_metrics']['auroc']:.4f}",
        "",
        "## Review Video Packages (Stored on Dean)",
        f"- **Baseline All400**: `{base_vid_manifest['all_video_path']}` ({base_vid_manifest['all_video_size_bytes']} bytes, SHA256: `{base_vid_manifest['all_video_sha256']}`)",
        f"- **Baseline Failures**: `{base_vid_manifest['failures_video_path']}` (SHA256: `{base_vid_manifest['failures_video_sha256']}`)",
        f"- **TopK All400**: `{active_vid_manifest['all_video_path']}` ({active_vid_manifest['all_video_size_bytes']} bytes, SHA256: `{active_vid_manifest['all_video_sha256']}`)",
        f"- **TopK Failures**: `{active_vid_manifest['failures_video_path']}` (SHA256: `{active_vid_manifest['failures_video_sha256']}`)",
        "",
        "## Evidence Checksums & Files",
        f"- `baseline/BASELINE_RESULT.json`",
        f"- `offline_eval/OOD400_MODEL_METRICS.json`",
        f"- `offline_eval/OOD400_THRESHOLD_SWEEP.json`",
        f"- `active_eval/ACTIVE_RESULT.json`",
        f"- `active_eval/PAIRED_COMPARISON.json`",
        f"- `active_eval/CONTROLLER_AUDIT.json`",
    ]
    (exp_dir / "PAPER_EVIDENCE_INDEX.md").write_text("\n".join(index_md_lines) + "\n")

    index_json = {
        "schema_version": "ood400_master_paper_evidence_index_v1",
        "benchmark_name": "reaching_mimic_risk_ood400",
        "total_episodes": 400,
        "protocol": {
            "success_threshold_m": 0.030,
            "max_control_ticks": 350,
            "dwell_s": 0.0,
            "execution_horizon": 10,
        },
        "locked_hashes": controller_spec["locked_hashes"],
        "baseline_summary": base_res,
        "offline_metrics": metrics_res,
        "online_a_selection": a_sel,
        "frozen_controller": controller_spec,
        "active_summary": active_res,
        "paired_comparison": paired_comp,
        "videos": {
            "baseline": base_vid_manifest,
            "topk": active_vid_manifest,
        },
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    (exp_dir / "PAPER_EVIDENCE_INDEX.json").write_text(json.dumps(index_json, indent=2) + "\n")

    # 4. Update Experiment Map in repo_root
    exp_map_dir = repo_root / "isaac_experiment_map"
    if exp_map_dir.exists():
        exp_record_p = exp_map_dir / "experiments/007_ood400_3cm350_exact_current_protocol_main_v2.md"
        exp_record_p.parent.mkdir(parents=True, exist_ok=True)
        exp_record_p.write_text("\n".join([
            "# Experiment 007: Canonical OOD400 Benchmark Evaluation (Exact Current Protocol)",
            "",
            "## Overview",
            "- **Benchmark**: `reaching_mimic_risk_ood400` (400 canonical scenes, SHA256: `264dae5a...`)",
            "- **Protocol**: 3.0 cm threshold, 350 control ticks max, 0 dwell, H10 execution",
            "- **Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`",
            "",
            "## Results",
            f"- **Normal SimVLA Baseline**: {base_res['success_count']}/400 ({base_res['success_rate']*100:.2f}%)",
            f"- **TopK Active SimVLA**: {active_res['success_count']}/400 ({active_res['success_rate']*100:.2f}%)",
            f"- **Delta**: {paired_comp['delta_percentage_points']:+.2f} pp (+{paired_comp['delta_episodes']} episodes)",
            f"- **Rescues / Regressions**: {paired_comp['matrix']['rescues']} / {paired_comp['matrix']['regressions']}",
            f"- **Operating Point**: {a_sel['selected_rule_name']} (A = {a_sel['selected_threshold_a']:.4f}, C = 0.90)",
            f"- **Monitor AUROC**: Query = {metrics_res['query_metrics']['auroc']:.4f}, Episode = {metrics_res['episode_balanced_metrics']['auroc']:.4f}",
        ]) + "\n")

    # 5. Real Publication Sync
    if publication_repo.exists() and (publication_repo / ".git").exists():
        # Check publication repo git status
        pub_status = run_cmd(["git", "status", "--short"], cwd=publication_repo)
        if pub_status:
            print(f"Warning: Publication repo has uncommitted changes:\n{pub_status}")

        pub_dest = publication_repo / "03_shared/evidence/isaac/current_main_3cm350_20260819/ood400_exact_current_protocol"
        pub_dest.mkdir(parents=True, exist_ok=True)

        files_to_copy = [
            (exp_dir / "PAPER_EVIDENCE_INDEX.md", pub_dest / "PAPER_EVIDENCE_INDEX.md"),
            (exp_dir / "PAPER_EVIDENCE_INDEX.json", pub_dest / "PAPER_EVIDENCE_INDEX.json"),
            (exp_dir / "OOD400_OFFLINE_PAPER_TABLE.md", pub_dest / "OOD400_OFFLINE_PAPER_TABLE.md"),
            (exp_dir / "OOD400_BASELINE_VS_TOPK_TABLE.md", pub_dest / "OOD400_BASELINE_VS_TOPK_TABLE.md"),
            (baseline_dir / "BASELINE_RESULT.json", pub_dest / "BASELINE_RESULT.json"),
            (baseline_dir / "BASELINE_MEMBERSHIP_AUDIT.json", pub_dest / "BASELINE_MEMBERSHIP_AUDIT.json"),
            (baseline_dir / "BASELINE_PROTOCOL_AUDIT.json", pub_dest / "BASELINE_PROTOCOL_AUDIT.json"),
            (baseline_dir / "BASELINE_EXECUTION_AUDIT.json", pub_dest / "BASELINE_EXECUTION_AUDIT.json"),
            (baseline_dir / "BASELINE_FEATURE_AUDIT.json", pub_dest / "BASELINE_FEATURE_AUDIT.json"),
            (offline_dir / "OOD400_MODEL_METRICS.json", pub_dest / "OOD400_MODEL_METRICS.json"),
            (offline_dir / "OOD400_THRESHOLD_SWEEP.json", pub_dest / "OOD400_THRESHOLD_SWEEP.json"),
            (offline_dir / "OOD400_THRESHOLD_SWEEP.csv", pub_dest / "OOD400_THRESHOLD_SWEEP.csv"),
            (offline_dir / "OOD400_THRESHOLD_SWEEP.md", pub_dest / "OOD400_THRESHOLD_SWEEP.md"),
            (offline_dir / "OOD400_PAPER_STYLE_TABLE.md", pub_dest / "OOD400_PAPER_STYLE_TABLE.md"),
            (offline_dir / "ONLINE_A_SELECTION.json", pub_dest / "ONLINE_A_SELECTION.json"),
            (active_dir / "FROZEN_CONTROLLER.json", pub_dest / "FROZEN_CONTROLLER.json"),
            (active_dir / "ACTIVE_RESULT.json", pub_dest / "ACTIVE_RESULT.json"),
            (active_dir / "PAIRED_COMPARISON.json", pub_dest / "PAIRED_COMPARISON.json"),
            (active_dir / "CONTROLLER_AUDIT.json", pub_dest / "CONTROLLER_AUDIT.json"),
            (active_dir / "MEMBERSHIP_AUDIT.json", pub_dest / "MEMBERSHIP_AUDIT.json"),
            (baseline_dir / "OOD400_BASELINE_VIDEO_MANIFEST.json", pub_dest / "OOD400_BASELINE_VIDEO_MANIFEST.json"),
            (baseline_dir / "OOD400_BASELINE_VIDEO_INDEX.csv", pub_dest / "OOD400_BASELINE_VIDEO_INDEX.csv"),
            (active_dir / "OOD400_TOPK_VIDEO_MANIFEST.json", pub_dest / "OOD400_TOPK_VIDEO_MANIFEST.json"),
            (active_dir / "OOD400_TOPK_VIDEO_INDEX.csv", pub_dest / "OOD400_TOPK_VIDEO_INDEX.csv"),
        ]

        for src, dst in files_to_copy:
            if src.exists():
                shutil.copy2(src, dst)

        # Stage and commit in publication repo
        run_cmd(["git", "add", "03_shared/evidence/isaac/current_main_3cm350_20260819/ood400_exact_current_protocol/"], cwd=publication_repo)
        pub_diff = run_cmd(["git", "diff", "--cached", "--name-only"], cwd=publication_repo)
        print(f"Publication staged files:\n{pub_diff}")

        try:
            run_cmd(["git", "commit", "-m", "docs(results): add exact current-protocol Isaac OOD400 evidence"], cwd=publication_repo)
            run_cmd(["git", "push", "origin", "main"], cwd=publication_repo)
            pub_commit = run_cmd(["git", "rev-parse", "HEAD"], cwd=publication_repo)
            print(f"Pushed publication commit: {pub_commit}")
        except Exception as e:
            print(f"Publication commit/push notice: {e}")
            pub_commit = "pending_push"

        # Record publication sync in experiment repo
        pub_sync_doc = {
            "schema_version": "ood400_publication_sync_record_v1",
            "publication_commit": pub_commit,
            "publication_mirror_path": str(pub_dest),
            "synced_timestamp": datetime.now(timezone.utc).isoformat(),
        }
        if exp_map_dir.exists():
            (exp_map_dir / "PUBLICATION_SYNC_20260819.json").write_text(json.dumps(pub_sync_doc, indent=2) + "\n")

    print("=== Master Evidence Index and Synchronization complete ===")
    return index_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp-dir", type=Path, required=True)
    parser.add_argument("--publication-repo", type=Path, default=PUBLICATION_REPO)
    args = parser.parse_args()

    sync_evidence(
        exp_dir=args.exp_dir,
        publication_repo=args.publication_repo,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
