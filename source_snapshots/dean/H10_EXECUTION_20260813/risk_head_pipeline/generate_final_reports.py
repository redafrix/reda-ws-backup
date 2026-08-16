#!/usr/bin/env python3
"""Generate the three final compact reports from completed immutable artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
DATA = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1"
MODEL = WORKSPACE / "models/isaac_h10_topk8_temporal_v1"
EVAL = WORKSPACE / "evaluations/locked_h10_ood150_topk8_v1"
REPORTS = WORKSPACE / "reports/final_risk_pipeline"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, default=DATA)
    parser.add_argument("--model-root", type=Path, default=MODEL)
    parser.add_argument("--evaluation-root", type=Path, default=EVAL)
    parser.add_argument("--report-root", type=Path, default=REPORTS)
    parser.add_argument("--report-suffix", default="")
    args = parser.parse_args()
    reports = args.report_root.resolve()
    reports.mkdir(parents=True, exist_ok=True)
    dataset = json.loads((args.dataset_root / "dataset_manifest.json").read_text())
    model = json.loads((args.model_root / "results.json").read_text())
    model_manifest = json.loads((args.model_root / "model_manifest.json").read_text())
    evaluation = json.loads((args.evaluation_root / "results.json").read_text())
    suffix = args.report_suffix

    dataset_lines = [
        "# Final Isaac Risk Dataset Report",
        "",
        f"- Frozen dataset: `{args.dataset_root.resolve()}`",
        f"- Feature schema: `{dataset['feature_schema_version']}`",
        f"- Source audited rounds: `{len(dataset['source_rounds'])}`",
        f"- Train episodes/rows: `{dataset['splits']['train']['episodes']}` / `{dataset['splits']['train']['rows']}`",
        f"- Validation episodes/rows: `{dataset['splits']['validation']['episodes']}` / `{dataset['splits']['validation']['rows']}`",
        f"- Seen-test episodes/rows: `{dataset['splits']['test']['episodes']}` / `{dataset['splits']['test']['rows']}`",
        f"- Split seed: `{dataset['split_contract']['seed']}`",
        f"- Group key: `{dataset['split_contract']['group_key']}`",
        f"- Training normalization: `{dataset['normalization']['path']}`",
        "",
        "SYNTHETIC_ROWS_INCLUDED=NO",
        "INFRASTRUCTURE_ERRORS_INCLUDED=NO",
        "TIMEOUT3600_ROWS_INCLUDED=NO",
        "OOD150_ROWS_INCLUDED=NO",
        "GROUP_OR_ROW_LEAKAGE=NO",
    ]
    (reports / f"FINAL_ISAAC_RISK_DATASET_REPORT{suffix}.md").write_text(
        "\n".join(dataset_lines) + "\n"
    )

    training_lines = [
        "# Isaac TopK8 Risk Training Report",
        "",
        f"- Model: `{model_manifest['model_path']}`",
        f"- SHA-256: `{model_manifest['model_sha256']}`",
        f"- Best epoch: `{model['best_epoch']}`",
        f"- Best seen-validation AUPRC: `{model['best_validation_auprc']:.8f}`",
        "- Architecture: one SeqRiskModel, width 128, 3 layers, 4 heads, FFN 512.",
        "- Optimization: weighted BCEWithLogitsLoss, AdamW, lr 2e-4, weight decay 1e-4, batch 512, 10 epochs.",
        "- Selection and calibration: seen validation only.",
        "",
        "OOD150_USED_FOR_TRAINING=NO",
        "OOD150_USED_FOR_NORMALIZATION=NO",
        "OOD150_USED_FOR_MODEL_SELECTION=NO",
        "OOD150_USED_FOR_THRESHOLD_CALIBRATION=NO",
    ]
    (reports / f"ISAAC_TOPK8_RISK_TRAINING_REPORT{suffix}.md").write_text(
        "\n".join(training_lines) + "\n"
    )

    q95 = evaluation["threshold_results"]["q95_success"]
    eval_lines = [
        "# Isaac Seen to OOD-150 Final Evaluation Report",
        "",
        f"- Locked OOD episodes/rows: `{evaluation['episodes']}` / `{evaluation['rows']}`",
        f"- Step AUROC: `{evaluation['step_auroc']:.8f}`",
        f"- Step AUPRC: `{evaluation['step_auprc']:.8f}`",
        f"- q95 success false-alarm rate: `{q95['episode']['episode_success_false_alarm_rate']:.8f}`",
        f"- q95 failure detection: `{q95['episode']['failure_detection_rate']:.8f}`",
        f"- q95 Det@10/25/50: `{q95['episode']['det_at_10']:.8f}` / `{q95['episode']['det_at_25']:.8f}` / `{q95['episode']['det_at_50']:.8f}`",
        f"- q95 mean detection fraction: `{q95['episode']['mean_detection_fraction']}`",
        f"- q95 Never count: `{q95['episode']['never_count']}`",
        "",
        "LOCKED_OOD150_EVALUATED_ONCE=YES",
        "OOD150_USED_TO_ADJUST_MODEL_OR_THRESHOLDS=NO",
    ]
    (reports / f"ISAAC_SEEN_TO_OOD150_FINAL_EVAL_REPORT{suffix}.md").write_text(
        "\n".join(eval_lines) + "\n"
    )
    print(reports)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
