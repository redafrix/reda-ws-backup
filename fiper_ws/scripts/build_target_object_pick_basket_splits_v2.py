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
DATA_ROOT = WORKSPACE / "data/frozen/fiper_sweep_eternal_20260527_combined"
OUT_ROOT = WORKSPACE / "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1"
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
    "main_seed": re.compile(r'"main_seed"\s*:\s*(-?\d+)'),
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

def make_episode_key(machine: str, instance: str, suite: str, task_id: int, episode_id: str, start_line_no: int) -> str:
    """Key one contiguous rollout segment, not one random action sample."""
    return f"{machine}_{instance}_{suite}_t{task_id}_ep{episode_id}_start{start_line_no}"

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

def split_success_episodes_loto(episodes: Iterable[EpisodeRef]) -> dict[str, str]:
    assignments: dict[str, str] = {}
    groups: dict[tuple[str, str], list[EpisodeRef]] = defaultdict(list)
    for ep in episodes:
        groups[(ep.target_object_label, ep.suite)].append(ep)

    for group_key, eps in sorted(groups.items()):
        eps = stable_shuffle(eps, repr(group_key))
        n = len(eps)
        if n == 1:
            assignments[eps[0].episode_key] = "success_train_seen"
        elif n == 2:
            assignments[eps[0].episode_key] = "success_train_seen"
            assignments[eps[1].episode_key] = "success_test_seen"
        elif n == 3:
            assignments[eps[0].episode_key] = "success_train_seen"
            assignments[eps[1].episode_key] = "success_calib_seen"
            assignments[eps[2].episode_key] = "success_test_seen"
        elif n == 4:
            assignments[eps[0].episode_key] = "success_train_seen"
            assignments[eps[1].episode_key] = "success_val_seen"
            assignments[eps[2].episode_key] = "success_calib_seen"
            assignments[eps[3].episode_key] = "success_test_seen"
        else:
            n_train = max(1, int(round(0.55 * n)))
            n_val = max(1, int(round(0.15 * n)))
            n_calib = max(1, int(round(0.15 * n)))
            n_test = n - n_train - n_val - n_calib
            if n_test <= 0:
                n_test = 1
                n_train = n - n_val - n_calib - n_test

            for i, ep in enumerate(eps):
                if i < n_train:
                    split = "success_train_seen"
                elif i < n_train + n_val:
                    split = "success_val_seen"
                elif i < n_train + n_val + n_calib:
                    split = "success_calib_seen"
                else:
                    split = "success_test_seen"
                assignments[ep.episode_key] = split
    return assignments

def split_failure_episodes_loto(episodes: Iterable[EpisodeRef]) -> dict[str, str]:
    assignments: dict[str, str] = {}
    groups: dict[tuple[str, str], list[EpisodeRef]] = defaultdict(list)
    for ep in episodes:
        groups[(ep.target_object_label, ep.suite)].append(ep)

    for group_key, eps in sorted(groups.items()):
        eps = stable_shuffle(eps, repr(group_key))
        n = len(eps)
        if n == 1:
            assignments[eps[0].episode_key] = "failure_train_seen"
        elif n == 2:
            assignments[eps[0].episode_key] = "failure_train_seen"
            assignments[eps[1].episode_key] = "failure_test_seen"
        elif n == 3:
            assignments[eps[0].episode_key] = "failure_train_seen"
            assignments[eps[1].episode_key] = "failure_val_seen"
            assignments[eps[2].episode_key] = "failure_test_seen"
        else:
            n_train = max(1, int(round(0.60 * n)))
            n_val = max(1, int(round(0.20 * n)))
            n_test = n - n_train - n_val
            if n_test <= 0:
                n_test = 1
                n_train = n - n_val - n_test

            for i, ep in enumerate(eps):
                if i < n_train:
                    split = "failure_train_seen"
                elif i < n_train + n_val:
                    split = "failure_val_seen"
                else:
                    split = "failure_test_seen"
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
        current_signature = None
        current_episode_key = None
        current_timestep = None
        current_line_no = None

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

                signature = (suite, int(task_id), str(episode_id))
                starts_new_segment = (
                    current_episode_key is None
                    or signature != current_signature
                    or current_timestep is None
                    or int(timestep) <= current_timestep
                    or current_line_no is None
                    or line_idx != current_line_no + 1
                )
                if starts_new_segment:
                    current_episode_key = make_episode_key(machine, instance, suite, int(task_id), str(episode_id), line_idx)
                current_signature = signature
                current_timestep = int(timestep)
                current_line_no = line_idx
                episode_key = current_episode_key
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
        failure_seen = [ep for ep in episodes if ep.episode_outcome != "success" and ep.target_object_label not in heldout_set]

        success_assignments = split_success_episodes_loto(success_seen)
        failure_assignments = split_failure_episodes_loto(failure_seen)

        ep_split: dict[str, str] = {}
        for ep in episodes:
            if ep.episode_outcome == "success":
                if ep.target_object_label in heldout_set:
                    ep_split[ep.episode_key] = "success_test_ood"
                else:
                    ep_split[ep.episode_key] = success_assignments[ep.episode_key]
            else:
                if ep.target_object_label in heldout_set:
                    ep_split[ep.episode_key] = "failure_eval_ood"
                else:
                    ep_split[ep.episode_key] = failure_assignments[ep.episode_key]

        episodes_by_split: dict[str, list[EpisodeRef]] = defaultdict(list)
        rows_by_split: dict[str, list[RowRef]] = defaultdict(list)

        for ep in episodes:
            split = ep_split[ep.episode_key]
            ep_out = EpisodeRef(**{**asdict(ep), "assigned_split": split})
            episodes_by_split[split].append(ep_out)
            rows_by_split[split].extend(rows_by_ep[ep.episode_key])

        CANONICAL_SPLITS = [
            "success_train_seen",
            "success_val_seen",
            "success_calib_seen",
            "success_test_seen",
            "success_test_ood",
            "failure_train_seen",
            "failure_val_seen",
            "failure_test_seen",
            "failure_eval_ood"
        ]

        split_summary = {}
        for split_name in CANONICAL_SPLITS:
            rows = sorted(rows_by_split.get(split_name, []), key=lambda r: (r.source_jsonl, r.line_no))
            eps = sorted(episodes_by_split.get(split_name, []), key=lambda e: e.episode_key)
            write_jsonl(refs_dir / f"{split_name}.rows.jsonl", (asdict(r) for r in rows))
            write_jsonl(refs_dir / f"{split_name}.episodes.jsonl", (asdict(e) for e in eps))
            split_summary[split_name] = summarize_split(rows, eps)

        leak_train = []
        for split_name in ["success_train_seen", "success_val_seen", "success_calib_seen", "success_test_seen", "failure_train_seen", "failure_val_seen", "failure_test_seen"]:
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
            f.write("Train/val/calib use success episodes from other picked objects only. OOD eval uses held-out picked objects.\n")

    with (OUT_ROOT / "TARGET_OBJECT_LOTO_REGISTRY.json").open("w") as f:
        json.dump(registry, f, indent=2, sort_keys=True)

    with (OUT_ROOT / "TARGET_OBJECT_LOTO_SUMMARY.json").open("w") as f:
        json.dump(fold_summaries, f, indent=2, sort_keys=True)

    print("Target-object folds generated successfully!")

if __name__ == "__main__":
    main()
