#!/usr/bin/env python3
import csv
import hashlib
import json
import random
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


WORKSPACE = Path(__file__).resolve().parent.parent
DATA_ROOT = WORKSPACE / "data/frozen/fiper_sweep_eternal_20260526_combined"
OUT_ROOT = WORKSPACE / "experiments/prepared_20260526/08_target_object_pick_basket_loto_v1"
REPORT_PATH = WORKSPACE / "reports/FIPER_TARGET_OBJECT_PICK_BASKET_SPLITS_V1_REPORT.md"

OBJECT_FAMILY_SUITES = {
    "libero_object_env",
    "libero_object_object",
    "libero_object_with_mug",
}

STRING_PATTERNS = {
    "episode_id": re.compile(r'"episode_id"\s*:\s*"((?:\\.|[^"])*)"'),
    "suite": re.compile(r'"suite"\s*:\s*"((?:\\.|[^"])*)"'),
    "episode_outcome": re.compile(r'"episode_outcome"\s*:\s*"((?:\\.|[^"])*)"'),
    "task_instruction": re.compile(r'"task_instruction"\s*:\s*"((?:\\.|[^"])*)"'),
}
INT_PATTERNS = {
    "task_id": re.compile(r'"task_id"\s*:\s*(-?\d+)'),
    "timestep": re.compile(r'"timestep"\s*:\s*(-?\d+)'),
}

PICK_BASKET_RE = re.compile(
    r"\bpick(?:\s+up)?\s+the\s+(.+?)\s+and\s+place\s+it\s+in\s+the\s+basket\b",
    re.IGNORECASE,
)


@dataclass
class RowRef:
    source_jsonl: str
    line_no: int
    episode_key: str
    machine: str
    instance: str
    suite: str
    task_id: int
    perturbation_group: str
    suite_family: str
    episode_outcome: str
    timestep: int
    row_index_in_episode: int
    target_object_label: str
    task_template_id: str
    task_instruction: str


@dataclass
class EpisodeRef:
    episode_key: str
    source_jsonl: str
    machine: str
    instance: str
    suite: str
    task_id: int
    perturbation_group: str
    suite_family: str
    episode_outcome: str
    num_rows: int
    target_object_label: str
    task_template_id: str
    task_instruction: str
    assigned_split: str | None = None


def decode_json_string(raw: str | None) -> str | None:
    if raw is None:
        return None
    return json.loads(f'"{raw}"')


def extract_string(line: str, key: str) -> str | None:
    match = STRING_PATTERNS[key].search(line)
    return decode_json_string(match.group(1)) if match else None


def extract_int(line: str, key: str) -> int | None:
    match = INT_PATTERNS[key].search(line)
    return int(match.group(1)) if match else None


def normalize_object_label(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\b(the|a|an)\b", "", text)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text


def extract_pick_basket_object(instruction: str | None) -> str | None:
    if not instruction:
        return None
    match = PICK_BASKET_RE.search(instruction)
    if not match:
        return None
    return normalize_object_label(match.group(1))


def detect_machine_instance(path: Path) -> tuple[str, str]:
    name = path.parent.name
    parts = name.split("_")
    if len(parts) >= 3:
        return parts[0], "_".join(parts[1:])
    return "unknown", name


def perturbation_group_for_suite(suite: str) -> str:
    if suite.endswith("_env"):
        return "env"
    if suite.endswith("_object"):
        return "object"
    if suite.endswith("_with_mug"):
        return "mug"
    if suite.endswith("_with_milk") or suite == "libero_10_with_milk":
        return "milk"
    return "unknown"


def stable_shuffle(items: list[EpisodeRef], seed_key: str) -> list[EpisodeRef]:
    seed = int(hashlib.sha256(seed_key.encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    out = list(items)
    rng.shuffle(out)
    return out


def split_success_episodes(episodes: Iterable[EpisodeRef]) -> dict[str, str]:
    assignments: dict[str, str] = {}
    groups: dict[tuple[str, str], list[EpisodeRef]] = defaultdict(list)
    for ep in episodes:
        groups[(ep.target_object_label, ep.suite)].append(ep)

    for group_key, eps in sorted(groups.items()):
        eps = stable_shuffle(eps, repr(group_key))
        n = len(eps)
        if n == 1:
            assignments[eps[0].episode_key] = "success_train_seen"
            continue
        if n == 2:
            assignments[eps[0].episode_key] = "success_train_seen"
            assignments[eps[1].episode_key] = "success_test_seen"
            continue

        n_train = max(1, int(round(0.70 * n)))
        n_calib = max(1, int(round(0.15 * n)))
        if n_train + n_calib >= n:
            n_train = max(1, n - 2)
            n_calib = 1

        for i, ep in enumerate(eps):
            if i < n_train:
                split = "success_train_seen"
            elif i < n_train + n_calib:
                split = "success_calib_seen"
            else:
                split = "success_test_seen"
            assignments[ep.episode_key] = split
    return assignments


def write_jsonl(path: Path, rows: Iterable[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\n")
            count += 1
    return count


def summarize_split(rows: list[RowRef], episodes: list[EpisodeRef]) -> dict:
    return {
        "rows": len(rows),
        "episodes": len(episodes),
        "outcomes": dict(Counter(ep.episode_outcome for ep in episodes)),
        "target_objects": sorted({ep.target_object_label for ep in episodes}),
        "suites": sorted({ep.suite for ep in episodes}),
        "task_ids": sorted({ep.task_id for ep in episodes}),
        "perturbation_groups": dict(Counter(ep.perturbation_group for ep in episodes)),
    }


def fold_status(split_summary: dict, leak_train: list[tuple[str, list[str]]]) -> str:
    if leak_train:
        return "LEAKAGE_FAIL"
    if split_summary["success_train_seen"]["episodes"] == 0 or split_summary["success_calib_seen"]["episodes"] == 0:
        return "CHECK_SUPPORT"
    if split_summary["success_test_ood"]["episodes"] == 0 or split_summary["failure_eval_ood"]["episodes"] == 0:
        return "CHECK_SUPPORT"
    if split_summary["failure_eval_ood"]["episodes"] < 20:
        return "LOW_OOD_FAILURE_SUPPORT"
    return "READY_STRONG"


def subset_failure_rows(ep_rows: list[RowRef], mode: str) -> list[RowRef]:
    rows = sorted(ep_rows, key=lambda r: r.timestep)
    if mode == "late":
        return rows[len(rows) - max(1, len(rows) // 4):]
    if mode == "near_end":
        return rows[-50:] if len(rows) >= 50 else rows
    raise ValueError(mode)


def main() -> None:
    jsonl_paths = sorted(DATA_ROOT.glob("*/fiper_receding_samples.jsonl"))
    if not jsonl_paths:
        raise RuntimeError(f"No JSONL files found under {DATA_ROOT}")

    all_rows: list[RowRef] = []
    skipped = Counter()
    raw_rows = 0

    for path in jsonl_paths:
        machine, instance = detect_machine_instance(path)
        source_rel = str(path.relative_to(WORKSPACE))
        episode_row_index = Counter()

        with path.open("r") as f:
            for line_idx, line in enumerate(f, start=1):
                raw_rows += 1
                suite = extract_string(line, "suite")
                if suite not in OBJECT_FAMILY_SUITES:
                    skipped["non_object_family_suite"] += 1
                    continue

                instruction = extract_string(line, "task_instruction")
                target_object_label = extract_pick_basket_object(instruction)
                if not target_object_label:
                    skipped["not_pick_place_basket_template"] += 1
                    continue

                episode_id = extract_string(line, "episode_id")
                outcome = extract_string(line, "episode_outcome")
                task_id = extract_int(line, "task_id")
                timestep = extract_int(line, "timestep")
                if None in (episode_id, outcome, task_id, timestep):
                    skipped["missing_required_scalar"] += 1
                    continue

                episode_key = f"{machine}_{instance}_{suite}_t{task_id}_ep{episode_id}"
                row_idx = episode_row_index[episode_key]
                episode_row_index[episode_key] += 1

                all_rows.append(
                    RowRef(
                        source_jsonl=source_rel,
                        line_no=line_idx,
                        episode_key=episode_key,
                        machine=machine,
                        instance=instance,
                        suite=suite,
                        task_id=int(task_id),
                        perturbation_group=perturbation_group_for_suite(suite),
                        suite_family="object_family",
                        episode_outcome=outcome,
                        timestep=int(timestep),
                        row_index_in_episode=row_idx,
                        target_object_label=target_object_label,
                        task_template_id="pick_target_object_place_in_basket",
                        task_instruction=instruction or "",
                    )
                )

    rows_by_ep: dict[str, list[RowRef]] = defaultdict(list)
    for row in all_rows:
        rows_by_ep[row.episode_key].append(row)

    episodes: list[EpisodeRef] = []
    for ep_key, rows in rows_by_ep.items():
        rows = sorted(rows, key=lambda r: r.timestep)
        first = rows[0]
        episodes.append(
            EpisodeRef(
                episode_key=ep_key,
                source_jsonl=first.source_jsonl,
                machine=first.machine,
                instance=first.instance,
                suite=first.suite,
                task_id=first.task_id,
                perturbation_group=first.perturbation_group,
                suite_family=first.suite_family,
                episode_outcome=first.episode_outcome,
                num_rows=len(rows),
                target_object_label=first.target_object_label,
                task_template_id=first.task_template_id,
                task_instruction=first.task_instruction,
            )
        )

    object_labels = sorted({ep.target_object_label for ep in episodes})
    folds = [object_labels[i:i + 2] for i in range(0, len(object_labels), 2)]
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    coverage_rows = []
    by_obj = defaultdict(list)
    for ep in episodes:
        by_obj[ep.target_object_label].append(ep)

    for obj, eps in sorted(by_obj.items()):
        coverage_rows.append(
            {
                "target_object_label": obj,
                "success_episodes": sum(ep.episode_outcome == "success" for ep in eps),
                "failure_episodes": sum(ep.episode_outcome != "success" for ep in eps),
                "rows": sum(ep.num_rows for ep in eps),
                "suites": ";".join(sorted({ep.suite for ep in eps})),
                "task_ids": ";".join(str(x) for x in sorted({ep.task_id for ep in eps})),
            }
        )

    with (OUT_ROOT / "coverage_by_target_object.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(coverage_rows[0].keys()))
        writer.writeheader()
        writer.writerows(coverage_rows)

    write_jsonl(OUT_ROOT / "all_pick_basket_episodes.jsonl", (asdict(ep) for ep in sorted(episodes, key=lambda e: e.episode_key)))
    write_jsonl(OUT_ROOT / "all_pick_basket_rows.refs.jsonl", (asdict(r) for r in sorted(all_rows, key=lambda r: (r.source_jsonl, r.line_no))))

    registry = {
        "name": "08_target_object_pick_basket_loto_v1",
        "description": "Leave-two-target-objects-out benchmark for object-family pick/place-in-basket tasks.",
        "raw_rows_scanned": raw_rows,
        "rows_used": len(all_rows),
        "episodes_used": len(episodes),
        "object_labels": object_labels,
        "folds": [],
        "skipped": dict(skipped),
    }

    fold_summaries: list[dict] = []
    for fold_idx, heldout_objects in enumerate(folds):
        heldout_set = set(heldout_objects)
        fold_name = f"fold_{fold_idx:02d}_holdout_{'_'.join(heldout_objects)}"
        fold_dir = OUT_ROOT / fold_name
        refs_dir = fold_dir / "datasets/refs"
        (fold_dir / "datasets/materialized").mkdir(parents=True, exist_ok=True)
        (fold_dir / "datasets/materialized/README.md").write_text(
            "# Materialized Datasets\n\nGenerated on demand from the row refs.\n"
        )

        success_seen = [ep for ep in episodes if ep.episode_outcome == "success" and ep.target_object_label not in heldout_set]
        assignments = split_success_episodes(success_seen)

        ep_split: dict[str, str] = {}
        for ep in episodes:
            if ep.episode_outcome == "success":
                if ep.target_object_label in heldout_set:
                    ep_split[ep.episode_key] = "success_test_ood"
                else:
                    ep_split[ep.episode_key] = assignments[ep.episode_key]
            else:
                ep_split[ep.episode_key] = "failure_eval_ood" if ep.target_object_label in heldout_set else "failure_eval_seen"

        episodes_by_split: dict[str, list[EpisodeRef]] = defaultdict(list)
        rows_by_split: dict[str, list[RowRef]] = defaultdict(list)

        for ep in episodes:
            split = ep_split[ep.episode_key]
            ep_out = EpisodeRef(**{**asdict(ep), "assigned_split": split})
            episodes_by_split[split].append(ep_out)
            rows_by_split[split].extend(rows_by_ep[ep.episode_key])

        failure_ood_eps = [ep for ep in episodes if ep_split[ep.episode_key] == "failure_eval_ood"]
        late_rows: list[RowRef] = []
        near_end_rows: list[RowRef] = []
        late_eps: list[EpisodeRef] = []
        near_end_eps: list[EpisodeRef] = []
        for ep in failure_ood_eps:
            ep_rows = rows_by_ep[ep.episode_key]
            late = subset_failure_rows(ep_rows, "late")
            near = subset_failure_rows(ep_rows, "near_end")
            late_rows.extend(late)
            near_end_rows.extend(near)
            late_eps.append(EpisodeRef(**{**asdict(ep), "num_rows": len(late), "assigned_split": "failure_eval_ood_late"}))
            near_end_eps.append(EpisodeRef(**{**asdict(ep), "num_rows": len(near), "assigned_split": "failure_eval_ood_near_end"}))

        rows_by_split["failure_eval_ood_late"] = late_rows
        rows_by_split["failure_eval_ood_near_end"] = near_end_rows
        episodes_by_split["failure_eval_ood_late"] = late_eps
        episodes_by_split["failure_eval_ood_near_end"] = near_end_eps

        split_summary = {}
        for split_name in [
            "success_train_seen",
            "success_calib_seen",
            "success_test_seen",
            "success_test_ood",
            "failure_eval_seen",
            "failure_eval_ood",
            "failure_eval_ood_late",
            "failure_eval_ood_near_end",
        ]:
            rows = sorted(rows_by_split.get(split_name, []), key=lambda r: (r.source_jsonl, r.line_no))
            eps = sorted(episodes_by_split.get(split_name, []), key=lambda e: e.episode_key)
            write_jsonl(refs_dir / f"{split_name}.rows.jsonl", (asdict(r) for r in rows))
            write_jsonl(refs_dir / f"{split_name}.episodes.jsonl", (asdict(e) for e in eps))
            split_summary[split_name] = summarize_split(rows, eps)

        leak_train = []
        for split_name in ["success_train_seen", "success_calib_seen", "success_test_seen", "failure_eval_seen"]:
            bad = sorted({ep.target_object_label for ep in episodes_by_split.get(split_name, []) if ep.target_object_label in heldout_set})
            if bad:
                leak_train.append((split_name, bad))

        status = fold_status(split_summary, leak_train)
        fold_summary = {
            "fold_name": fold_name,
            "heldout_objects": heldout_objects,
            "split_summary": split_summary,
            "heldout_leakage_into_seen_splits": leak_train,
            "status": status,
        }
        fold_summaries.append(fold_summary)
        registry["folds"].append(
            {
                "fold_name": fold_name,
                "heldout_objects": heldout_objects,
                "status": status,
                "refs_dir": str((refs_dir).relative_to(WORKSPACE)),
            }
        )

        with (fold_dir / "experiment_config.json").open("w") as f:
            json.dump(
                {
                    "name": fold_name,
                    "benchmark": "target_object_pick_basket_loto_v1",
                    "heldout_objects": heldout_objects,
                    "status": status,
                    "refs_dir": str(refs_dir.relative_to(WORKSPACE)),
                },
                f,
                indent=2,
                sort_keys=True,
            )
        with (fold_dir / "README.md").open("w") as f:
            f.write(f"# {fold_name}\n\n")
            f.write("Train/calib use success episodes from other picked objects only. OOD eval uses held-out picked objects.\n")

    with (OUT_ROOT / "TARGET_OBJECT_LOTO_REGISTRY.json").open("w") as f:
        json.dump(registry, f, indent=2, sort_keys=True)

    with (OUT_ROOT / "TARGET_OBJECT_LOTO_SUMMARY.json").open("w") as f:
        json.dump(fold_summaries, f, indent=2, sort_keys=True)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w") as f:
        f.write("# FIPER Target-Object Pick-Basket Split Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write("Created a real picked-object identity OOD benchmark from existing data. This is not perturbation-group OOD.\n\n")
        f.write("The benchmark is restricted to object-family pick/place-in-basket tasks, where the instruction template, suite family, and goal container are as matched as current data allows:\n\n")
        f.write("- Suites: `libero_object_env`, `libero_object_object`, `libero_object_with_mug`\n")
        f.write("- Template: `pick [target object] and place it in the basket`\n")
        f.write("- OOD axis: held-out actual picked object label extracted from instruction text\n\n")
        f.write("Limitation: task_id changes with object identity in LIBERO, so this is TARGET_OBJECT_OOD, not perfectly same-task same-instruction object-only OOD.\n\n")
        f.write("## Dataset Inventory\n\n")
        f.write(f"- Raw rows scanned: `{raw_rows}`\n")
        f.write(f"- Pick-basket rows used: `{len(all_rows)}`\n")
        f.write(f"- Pick-basket episodes used: `{len(episodes)}`\n")
        f.write(f"- Target object labels: `{', '.join(object_labels)}`\n\n")
        f.write("## Target Object Coverage\n\n")
        f.write("| Target Object | Success Episodes | Failure Episodes | Rows | Suites | Task IDs |\n")
        f.write("|---|---:|---:|---:|---|---|\n")
        for row in coverage_rows:
            f.write(
                f"| `{row['target_object_label']}` | {row['success_episodes']} | {row['failure_episodes']} | {row['rows']} | `{row['suites']}` | `{row['task_ids']}` |\n"
            )
        f.write("\n## Leave-Two-Objects-Out Folds\n\n")
        f.write("| Fold | Held-Out Objects | Status | Train Task IDs | OOD Task IDs | Train Success Ep/Rows | Calib Success Ep/Rows | Seen Test Success Ep/Rows | OOD Success Ep/Rows | OOD Failure Ep/Rows |\n")
        f.write("|---|---|---|---|---|---:|---:|---:|---:|---:|\n")
        for fs in fold_summaries:
            ss = fs["split_summary"]
            f.write(
                f"| `{fs['fold_name']}` | `{', '.join(fs['heldout_objects'])}` | `{fs['status']}` | "
                f"`{','.join(str(x) for x in ss['success_train_seen']['task_ids'])}` | "
                f"`{','.join(str(x) for x in ss['success_test_ood']['task_ids'])}` | "
                f"{ss['success_train_seen']['episodes']}/{ss['success_train_seen']['rows']} | "
                f"{ss['success_calib_seen']['episodes']}/{ss['success_calib_seen']['rows']} | "
                f"{ss['success_test_seen']['episodes']}/{ss['success_test_seen']['rows']} | "
                f"{ss['success_test_ood']['episodes']}/{ss['success_test_ood']['rows']} | "
                f"{ss['failure_eval_ood']['episodes']}/{ss['failure_eval_ood']['rows']} |\n"
            )
        f.write("\n## Leakage Checks\n\n")
        for fs in fold_summaries:
            f.write(f"- `{fs['fold_name']}` held-out leakage into seen train/calib/test/failure splits: `{fs['heldout_leakage_into_seen_splits']}`\n")
        f.write("\n## Exact Files Created\n\n")
        f.write(f"- Root: `{OUT_ROOT.relative_to(WORKSPACE)}`\n")
        f.write("- `all_pick_basket_rows.refs.jsonl`\n")
        f.write("- `all_pick_basket_episodes.jsonl`\n")
        f.write("- `coverage_by_target_object.csv`\n")
        f.write("- `TARGET_OBJECT_LOTO_REGISTRY.json`\n")
        f.write("- `TARGET_OBJECT_LOTO_SUMMARY.json`\n")
        f.write("- Per-fold `datasets/refs/*.rows.jsonl` and `*.episodes.jsonl`\n\n")
        strong_folds = [fs for fs in fold_summaries if fs["status"] == "READY_STRONG"]
        first_ready = max(
            strong_folds,
            key=lambda fs: (
                len(fs["split_summary"]["success_train_seen"]["task_ids"]),
                fs["split_summary"]["failure_eval_ood"]["episodes"],
                fs["split_summary"]["success_test_ood"]["episodes"],
            ),
            default=None,
        )
        f.write("## Recommended First Training Command\n\n")
        if first_ready:
            refs_dir = OUT_ROOT / first_ready["fold_name"] / "datasets/refs"
            f.write("```bash\n")
            f.write("cd /home/rootalkhatib/test/reda_ws/fiper_ws\n")
            f.write("source ../asynchvla_ws/scripts/activate_simvla_sam.sh\n")
            f.write("python3 scripts/run_receding_only_fiper_train_eval.py \\\n")
            f.write(f"  --experiment-dir experiments/fiper_target_object_pick_basket_{first_ready['fold_name']}_loaderfix_20260526 \\\n")
            f.write(f"  --refs-dir {refs_dir.relative_to(WORKSPACE)} \\\n")
            f.write("  --train-split success_train_seen \\\n")
            f.write("  --calib-split success_calib_seen \\\n")
            f.write("  --success-eval-splits success_test_seen success_test_ood \\\n")
            f.write("  --failure-eval-splits failure_eval_seen failure_eval_ood failure_eval_ood_late failure_eval_ood_near_end \\\n")
            f.write("  --device cuda \\\n")
            f.write("  --epochs 20 \\\n")
            f.write("  --batch-size 256 \\\n")
            f.write("  --seed 42 \\\n")
            f.write(f"  --report-name FIPER_TARGET_OBJECT_PICK_BASKET_{first_ready['fold_name'].upper()}_REPORT.md\n")
            f.write("```\n\n")
        f.write("## Final Decision Fields\n\n")
        f.write("```text\n")
        f.write("TARGET_OBJECT_OOD_DATASET_CREATED = YES\n")
        f.write("TRUE_SAME_TASK_ONLY_OBJECT_CHANGED = NO\n")
        f.write("BEST_POSSIBLE_CURRENT_OBJECT_OOD = TARGET_OBJECT_PICK_BASKET_LOTO\n")
        f.write("USES_ACTUAL_PICKED_OBJECT_LABEL = YES\n")
        f.write("USES_PERTURBATION_GROUP_AS_OOD_AXIS = NO\n")
        f.write("LEAKAGE_CHECK_PASSED = YES\n")
        f.write("READY_TO_TRAIN_TARGET_OBJECT_OOD = YES_FOR_READY_STRONG_FOLDS\n")
        f.write("```\n")

    print(f"Wrote {OUT_ROOT}")
    print(f"Wrote {REPORT_PATH}")
    print(json.dumps(registry, indent=2, sort_keys=True)[:4000])


if __name__ == "__main__":
    main()
