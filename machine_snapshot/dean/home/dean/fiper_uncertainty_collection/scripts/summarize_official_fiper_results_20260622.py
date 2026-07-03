import os
from pathlib import Path

import pandas as pd

BASE = Path("/home/dean/fiper_uncertainty_collection")
EXP = BASE / "experiments" / "official_fiper_rndoe_entropy_fold00_20260622"
REPORT_DIR = EXP / "reports"
REPORT = REPORT_DIR / "OFFICIAL_FIPER_RNDOE_ENTROPY_FOLD00_RESULTS_20260622.md"


def read_tail(path: Path, n: int = 80) -> str:
    if not path.exists():
        return "_missing_"
    lines = path.read_text(errors="replace").splitlines()
    return "\n".join(lines[-n:])


def csv_sections(root: Path):
    sections = []
    for csv_path in sorted(root.rglob("*.csv")):
        rel = csv_path.relative_to(EXP)
        try:
            df = pd.read_csv(csv_path)
        except Exception as exc:
            sections.append(f"### `{rel}`\n\nCould not parse CSV: `{exc}`\n")
            continue
        sections.append(
            f"### `{rel}`\n\n"
            f"Rows: `{len(df)}` Columns: `{list(df.columns)}`\n\n"
            + df.head(40).to_markdown(index=False)
            + "\n"
        )
    return sections


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    materialize_validate = BASE / "logs/official_fiper_repair_20260622/validate.log"
    if not materialize_validate.exists():
        materialize_validate = BASE / "logs/official_fiper_sharded_20260622/validate.log"
    option_a_log = EXP / "logs/option_a_run.log"
    option_b_train_log = EXP / "logs/option_b_train_hygiene.log"
    option_b_eval_log = EXP / "logs/option_b_eval_with_hygiene_rnd.log"

    option_a_csvs = csv_sections(EXP / "option_a_results")
    option_b_csvs = csv_sections(EXP / "option_b_results")

    md = [
        "# Official FIPER RND-OE + Entropy Fold00 Results (2026-06-22)",
        "",
        "This report summarizes the closest official-FIPER offline ablation run on the materialized fold00 LIBERO data.",
        "",
        "## Paths",
        "",
        f"- Experiment root: `{EXP}`",
        f"- Materialized data: `{EXP / 'official_fiper_data'}`",
        f"- Option A results: `{EXP / 'option_a_results'}`",
        f"- Option B results: `{EXP / 'option_b_results'}`",
        "",
        "## Validation Tail",
        "",
        "```text",
        read_tail(materialize_validate, 120),
        "```",
        "",
        "## Option A: Official Semantics",
        "",
        "Option A uses `libero_fold00`: official-style calibration on `success_calib_seen` and testing on seen/OOD success/failure test splits.",
        "",
    ]
    md.extend(option_a_csvs or ["No Option A CSV result files found.\n"])
    md.extend(
        [
            "",
            "### Option A Log Tail",
            "",
            "```text",
            read_tail(option_a_log, 120),
            "```",
            "",
            "## Option B: Hygiene Training",
            "",
            "Option B trains RND on `success_train_seen` through `libero_fold00_hygiene`, copies the trained RND checkpoints, then evaluates on `libero_fold00` with calibration/test semantics.",
            "",
        ]
    )
    md.extend(option_b_csvs or ["No Option B CSV result files found.\n"])
    md.extend(
        [
            "",
            "### Option B Train Log Tail",
            "",
            "```text",
            read_tail(option_b_train_log, 80),
            "```",
            "",
            "### Option B Eval Log Tail",
            "",
            "```text",
            read_tail(option_b_eval_log, 120),
            "```",
            "",
            "## Final Flags",
            "",
            "- MATERIALIZATION_COMPLETE = YES if validation tail contains `VALIDATION_PASS`",
            "- DATASET_VALIDATION_PASS = YES if validation tail contains `VALIDATION_PASS`",
            "- OPTION_A_PASS = YES if Option A CSVs/logs exist and no error appears in log tail",
            "- OPTION_B_PASS = YES if Option B CSVs/logs exist and no error appears in log tail",
            "- SAFE_TO_COMPARE_WITH_NEXTGEN = check the tables above before marking trusted",
            "",
        ]
    )
    REPORT.write_text("\n".join(md))
    print(f"Wrote {REPORT}")


if __name__ == "__main__":
    main()
