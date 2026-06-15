#!/usr/bin/env python3
import argparse
import gzip
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


GOAL_RE = re.compile(
    r"libero_goal_object_task(?P<task>\d+)_seed(?P<seed>\d+)_(?P<trials>\d+)trials\.jsonl$"
)


def parse_int_set(text):
    return set(int(x) for x in text.replace(",", " ").split() if x.strip())


def open_text(path, mode):
    path = Path(path)
    if str(path).endswith(".gz"):
        return gzip.open(path, mode + "t", encoding="utf-8")
    return open(path, mode, encoding="utf-8")


def find_clean_file(clean_dir, stem):
    candidates = [
        clean_dir / f"{stem}.jsonl.gz",
        clean_dir / f"{stem}.jsonl",
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"Could not find {stem}.jsonl.gz or {stem}.jsonl in {clean_dir}")


def iter_jsonl(path):
    with open_text(path, "r") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Bad JSON in {path}:{lineno}: {e}") from e


def stable_hash(rec):
    raw = json.dumps(rec, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def iter_source(source):
    if isinstance(source, Path):
        yield from iter_jsonl(source)
    else:
        yield from source


def counter_to_dict(counter):
    return {str(k): int(v) for k, v in sorted(counter.items(), key=lambda kv: str(kv[0]))}


def write_split(out_path, sources):
    out_path.parent.mkdir(parents=True, exist_ok=True)

    n = 0
    success = 0
    failure = 0
    unknown_success = 0
    by_task = Counter()
    by_suite = Counter()
    hashes = set()

    with open_text(out_path, "w") as out:
        for source in sources:
            for rec in iter_source(source):
                n += 1

                h = stable_hash(rec)
                hashes.add(h)

                s = rec.get("success", None)
                if s is True or s == 1:
                    success += 1
                elif s is False or s == 0:
                    failure += 1
                else:
                    unknown_success += 1

                task_id = rec.get("task_id", "unknown")
                suite = (
                    rec.get("task_suite")
                    or rec.get("suite")
                    or rec.get("suite_name")
                    or rec.get("benchmark_suite")
                    or "unknown"
                )

                by_task[task_id] += 1
                by_suite[suite] += 1

                out.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

    stats = {
        "path": str(out_path),
        "episodes": n,
        "success": success,
        "failure": failure,
        "unknown_success": unknown_success,
        "by_task": counter_to_dict(by_task),
        "by_suite": counter_to_dict(by_suite),
    }

    return stats, hashes


def load_goal_object_by_seed(goal_dir, train_seeds, val_seeds, test_seeds, task_ids):
    groups = {
        "goal_object_train": [],
        "goal_object_val_ood": [],
        "goal_object_test_ood": [],
    }

    file_stats = []
    skipped_empty = []
    skipped_seed = []
    skipped_task = []

    files = sorted(goal_dir.glob("libero_goal_object_task*_seed*_*.jsonl"))

    for path in files:
        m = GOAL_RE.match(path.name)
        if not m:
            continue

        task_id = int(m.group("task"))
        seed = int(m.group("seed"))
        trials = int(m.group("trials"))

        if task_id not in task_ids:
            skipped_task.append(str(path))
            continue

        if path.stat().st_size == 0:
            skipped_empty.append(str(path))
            continue

        if seed in train_seeds:
            split = "goal_object_train"
        elif seed in val_seeds:
            split = "goal_object_val_ood"
        elif seed in test_seeds:
            split = "goal_object_test_ood"
        else:
            skipped_seed.append(str(path))
            continue

        count = 0
        succ = 0
        fail = 0

        for rec in iter_jsonl(path):
            groups[split].append(rec)
            count += 1

            if rec.get("success") is True or rec.get("success") == 1:
                succ += 1
            elif rec.get("success") is False or rec.get("success") == 0:
                fail += 1

        file_stats.append(
            {
                "file": str(path),
                "task_id": task_id,
                "seed": seed,
                "trials": trials,
                "split": split,
                "episodes": count,
                "success": succ,
                "failure": fail,
            }
        )

    return groups, file_stats, skipped_empty, skipped_seed, skipped_task


def check_no_leak(hash_sets):
    seen = {}
    leaks = []

    for split_name, hashes in hash_sets.items():
        for h in hashes:
            if h in seen:
                leaks.append(
                    {
                        "hash": h,
                        "first_split": seen[h],
                        "second_split": split_name,
                    }
                )
            else:
                seen[h] = split_name

    return leaks


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--clean_dir",
        default="/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_denoise_clean_splits_20260504",
    )
    parser.add_argument(
        "--goal_object_dir",
        default="/home/redafrix/SimVLA_modified/evaluation/libero/eval_libero_pro/phase2_tdqc_goal_object_ood_denoise_20260504_104916",
    )
    parser.add_argument("--out_dir", default=None)

    parser.add_argument("--goal_train_seeds", default="509,521,547")
    parser.add_argument("--goal_val_seeds", default="563")
    parser.add_argument("--goal_test_seeds", default="587")
    parser.add_argument("--goal_task_ids", default="0,1,2,3,4,5,6,7,8")

    args = parser.parse_args()

    clean_dir = Path(args.clean_dir)
    goal_dir = Path(args.goal_object_dir)

    if args.out_dir is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_dir = clean_dir.parent / f"phase2_tdqc_robust_splits_{stamp}"
    else:
        out_dir = Path(args.out_dir)

    out_dir.mkdir(parents=True, exist_ok=True)

    train_clean = find_clean_file(clean_dir, "train_clean")
    val_clean = find_clean_file(clean_dir, "val_clean")
    test_clean = find_clean_file(clean_dir, "test_clean")

    train_seeds = parse_int_set(args.goal_train_seeds)
    val_seeds = parse_int_set(args.goal_val_seeds)
    test_seeds = parse_int_set(args.goal_test_seeds)
    task_ids = parse_int_set(args.goal_task_ids)

    goal_groups, file_stats, skipped_empty, skipped_seed, skipped_task = load_goal_object_by_seed(
        goal_dir=goal_dir,
        train_seeds=train_seeds,
        val_seeds=val_seeds,
        test_seeds=test_seeds,
        task_ids=task_ids,
    )

    if len(goal_groups["goal_object_train"]) == 0:
        raise RuntimeError("goal_object_train is empty. Check seeds/task IDs.")
    if len(goal_groups["goal_object_val_ood"]) == 0:
        raise RuntimeError("goal_object_val_ood is empty. Check seeds/task IDs.")
    if len(goal_groups["goal_object_test_ood"]) == 0:
        raise RuntimeError("goal_object_test_ood is empty. Check seeds/task IDs.")

    outputs = {}
    atomic_hashes = {}

    # Main atomic splits: these must be disjoint.
    outputs["train_mixed_clean_plus_goal_object"], atomic_hashes["train_mixed_clean_plus_goal_object"] = write_split(
        out_dir / "train_mixed_clean_plus_goal_object.jsonl.gz",
        [train_clean, goal_groups["goal_object_train"]],
    )

    outputs["val_id_clean"], atomic_hashes["val_id_clean"] = write_split(
        out_dir / "val_id_clean.jsonl.gz",
        [val_clean],
    )

    outputs["test_id_clean"], atomic_hashes["test_id_clean"] = write_split(
        out_dir / "test_id_clean.jsonl.gz",
        [test_clean],
    )

    outputs["val_goal_object_ood"], atomic_hashes["val_goal_object_ood"] = write_split(
        out_dir / "val_goal_object_ood.jsonl.gz",
        [goal_groups["goal_object_val_ood"]],
    )

    outputs["test_goal_object_ood"], atomic_hashes["test_goal_object_ood"] = write_split(
        out_dir / "test_goal_object_ood.jsonl.gz",
        [goal_groups["goal_object_test_ood"]],
    )

    leaks = check_no_leak(atomic_hashes)

    if leaks:
        leak_path = out_dir / "LEAKS_FOUND.json"
        with open(leak_path, "w", encoding="utf-8") as f:
            json.dump(leaks, f, indent=2)
        raise RuntimeError(f"Leakage found between atomic splits. See {leak_path}")

    # Useful derived files.
    # These intentionally overlap with the atomic validation/test files.
    outputs["train_clean_only"], _ = write_split(
        out_dir / "train_clean_only.jsonl.gz",
        [train_clean],
    )

    outputs["goal_object_train_only"], _ = write_split(
        out_dir / "goal_object_train_only.jsonl.gz",
        [goal_groups["goal_object_train"]],
    )

    outputs["val_selection_mixed_id_plus_goal_object_ood"], _ = write_split(
        out_dir / "val_selection_mixed_id_plus_goal_object_ood.jsonl.gz",
        [val_clean, goal_groups["goal_object_val_ood"]],
    )

    outputs["test_mixed_id_plus_goal_object_ood"], _ = write_split(
        out_dir / "test_mixed_id_plus_goal_object_ood.jsonl.gz",
        [test_clean, goal_groups["goal_object_test_ood"]],
    )

    manifest = {
        "strategy": {
            "clean_train": "training only",
            "clean_val": "ID validation only",
            "clean_test": "ID test only",
            "goal_object_train_seeds": sorted(train_seeds),
            "goal_object_val_ood_seeds": sorted(val_seeds),
            "goal_object_test_ood_seeds": sorted(test_seeds),
            "goal_object_task_ids_used": sorted(task_ids),
            "goal_object_task9_note": "Task 9 is skipped by default because current JSONL files are empty.",
        },
        "input": {
            "clean_dir": str(clean_dir),
            "goal_object_dir": str(goal_dir),
            "train_clean": str(train_clean),
            "val_clean": str(val_clean),
            "test_clean": str(test_clean),
        },
        "outputs": outputs,
        "goal_object_file_stats": file_stats,
        "skipped_empty_files": skipped_empty,
        "skipped_seed_files": skipped_seed,
        "skipped_task_files": skipped_task,
        "leak_check": {
            "atomic_splits_checked": list(atomic_hashes.keys()),
            "leaks_found": len(leaks),
        },
    }

    manifest_path = out_dir / "manifest_robust_splits.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print("Done.")
    print(f"Output directory: {out_dir}")
    print(f"Manifest: {manifest_path}")
    print()
    for name, stats in outputs.items():
        print(
            f"{name}: {stats['episodes']} episodes, "
            f"{stats['success']} success / {stats['failure']} failure"
        )


if __name__ == "__main__":
    main()
