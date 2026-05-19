from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch.utils.data import Dataset


LABEL_ORDER = ["GOOD_STRONG", "GOOD_WEAK", "AMBIGUOUS", "VALIDATED_BAD"]
LABEL_TO_ORDINAL = {label: idx for idx, label in enumerate(LABEL_ORDER)}
SUBTYPE_TO_ID = {"action_specific": 0, "state_context": 1}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def final_label(sample: dict[str, Any]) -> str | None:
    label = sample.get("label")
    if isinstance(label, dict):
        return label.get("final_label") or label.get("label")
    return sample.get("label") if isinstance(sample.get("label"), str) else sample.get("final_label")


def metadata(sample: dict[str, Any]) -> dict[str, Any]:
    meta = sample.get("metadata")
    return meta if isinstance(meta, dict) else {}


def label_dict(sample: dict[str, Any]) -> dict[str, Any]:
    label = sample.get("label")
    return label if isinstance(label, dict) else {}


def resolve_path(path: str, source_remaps: list[tuple[str, str]]) -> Path:
    resolved = path
    for src, dst in source_remaps:
        if resolved.startswith(src):
            resolved = dst + resolved[len(src) :]
            break
    return Path(resolved)


def parse_source_remaps(raw: list[str] | None) -> list[tuple[str, str]]:
    remaps: list[tuple[str, str]] = []
    for item in raw or []:
        if "=" not in item:
            raise ValueError(f"source remap must be OLD=NEW, got {item}")
        old, new = item.split("=", 1)
        remaps.append((old, new))
    return remaps


def pad_flat(values: Any, size: int) -> np.ndarray:
    arr = np.asarray(values if values is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(size, dtype=np.float32)
    n = min(size, arr.size)
    if n:
        out[:n] = arr[:n]
    return out


def pad_seq(values: Any, rows: int, cols: int) -> np.ndarray:
    arr = np.asarray(values if values is not None else [], dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, cols) if arr.size % cols == 0 else arr.reshape(1, -1)
    out = np.zeros((rows, cols), dtype=np.float32)
    if arr.size:
        rr = min(rows, arr.shape[0])
        cc = min(cols, arr.shape[1])
        out[:rr, :cc] = arr[:rr, :cc]
    return out


def candidate_action_seq(sample: dict[str, Any], steps: int = 10, dim: int = 7) -> np.ndarray:
    cand = sample.get("candidate_action") or {}
    values = cand.get("candidate_action_normalized") or cand.get("candidate_action_env") or []
    return pad_seq(values, steps, dim)


def history_seq(sample: dict[str, Any], steps: int = 8, dim: int = 17) -> np.ndarray:
    hist = sample.get("history") or []
    out = np.zeros((steps, dim), dtype=np.float32)
    tail = hist[-steps:]
    start = steps - len(tail)
    for i, item in enumerate(tail, start=start):
        if not isinstance(item, dict):
            continue
        row = np.concatenate(
            [
                pad_flat(item.get("proprio"), 8),
                pad_flat(item.get("executed_action"), 7),
                np.asarray([float(item.get("reward") or 0.0), float(bool(item.get("success")))], dtype=np.float32),
            ]
        )
        out[i, : min(dim, row.size)] = row[:dim]
    return out


def context_vec(sample: dict[str, Any], max_objects: int = 24) -> np.ndarray:
    current = sample.get("current") or {}
    proprio = pad_flat(current.get("proprio"), 8)
    positions = current.get("object_positions_before") or {}
    object_values: list[float] = []
    if isinstance(positions, dict):
        for key in sorted(positions)[:max_objects]:
            object_values.extend(pad_flat(positions.get(key), 3).tolist())
    object_vec = pad_flat(object_values, max_objects * 3)
    return np.concatenate([proprio, object_vec]).astype(np.float32)


def target_values(label: str, target_mode: str, bad_subtype: str) -> tuple[float, float, int, int]:
    if target_mode == "clean_binary":
        if label == "GOOD_STRONG":
            return 0.0, 1.0, LABEL_TO_ORDINAL[label], -1
        if label == "VALIDATED_BAD":
            return 1.0, 1.0, LABEL_TO_ORDINAL[label], SUBTYPE_TO_ID.get(bad_subtype, -1)
        return 0.0, 0.0, LABEL_TO_ORDINAL.get(label, -1), -1
    if target_mode == "soft_labels":
        mapping = {
            "GOOD_STRONG": (0.0, 1.0),
            "GOOD_WEAK": (0.25, 0.3),
            "AMBIGUOUS": (0.5, 0.1),
            "VALIDATED_BAD": (1.0, 1.0),
        }
        y, w = mapping[label]
        return y, w, LABEL_TO_ORDINAL[label], SUBTYPE_TO_ID.get(bad_subtype, -1)
    if target_mode == "soft_no_ambiguous":
        if label == "AMBIGUOUS":
            return 0.0, 0.0, LABEL_TO_ORDINAL[label], -1
        mapping = {"GOOD_STRONG": (0.0, 1.0), "GOOD_WEAK": (0.25, 0.3), "VALIDATED_BAD": (1.0, 1.0)}
        y, w = mapping[label]
        return y, w, LABEL_TO_ORDINAL[label], SUBTYPE_TO_ID.get(bad_subtype, -1)
    if target_mode == "ordinal":
        return float(LABEL_TO_ORDINAL[label]), 1.0, LABEL_TO_ORDINAL[label], SUBTYPE_TO_ID.get(bad_subtype, -1)
    if target_mode == "subtype_multitask":
        if label == "GOOD_STRONG":
            return 0.0, 1.0, LABEL_TO_ORDINAL[label], -1
        if label == "VALIDATED_BAD":
            return 1.0, 1.0, LABEL_TO_ORDINAL[label], SUBTYPE_TO_ID.get(bad_subtype, -1)
        return 0.0, 0.0, LABEL_TO_ORDINAL.get(label, -1), -1
    raise ValueError(f"unknown target mode {target_mode}")


class Stage9RiskDataset(Dataset):
    def __init__(
        self,
        split_jsonl: Path,
        target_mode: str,
        source_remaps: list[tuple[str, str]] | None = None,
        max_samples: int | None = None,
        balance_binary: bool = False,
    ) -> None:
        self.split_jsonl = Path(split_jsonl)
        self.target_mode = target_mode
        self.source_remaps = source_remaps or []
        split_rows = read_jsonl(self.split_jsonl)
        if max_samples:
            split_rows = split_rows[:max_samples]
        self.rows = self._load_samples(split_rows)
        self.rows = [r for r in self.rows if target_values(r["label"], target_mode, r["bad_subtype"])[1] > 0]
        if balance_binary:
            self.rows = self._balance_binary(self.rows)
        self.action_steps = 10
        self.action_dim = 7
        self.history_steps = 8
        self.history_dim = 17
        self.context_dim = 8 + 24 * 3
        self.flat_dim = self.context_dim + self.action_steps * self.action_dim + self.history_steps * self.history_dim
        self.action_flat_dim = self.action_steps * self.action_dim
        self.context_action_dim = self.context_dim + self.action_flat_dim

    def _load_samples(self, split_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        by_file: dict[Path, dict[str, dict[str, Any]]] = defaultdict(dict)
        for row in split_rows:
            source = resolve_path(str(row["source_jsonl"]), self.source_remaps)
            by_file[source][str(row["sample_id"])] = row
        samples: list[dict[str, Any]] = []
        for source, wanted in sorted(by_file.items(), key=lambda kv: str(kv[0])):
            if not source.exists():
                raise FileNotFoundError(f"missing sample source {source}")
            with source.open() as f:
                for line in f:
                    if not line.strip():
                        continue
                    sample = json.loads(line)
                    sid = str(sample.get("sample_id"))
                    if sid not in wanted:
                        continue
                    split_meta = wanted[sid]
                    label = split_meta.get("label") or final_label(sample)
                    subtype = split_meta.get("bad_subtype") or label_dict(sample).get("bad_subtype") or "unknown"
                    sample["_stage9_split_row"] = split_meta
                    sample["label"] = label
                    sample["bad_subtype"] = subtype
                    samples.append(sample)
        return samples

    @staticmethod
    def _balance_binary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        good = [r for r in rows if r["label"] == "GOOD_STRONG"]
        bad = [r for r in rows if r["label"] == "VALIDATED_BAD"]
        other = [r for r in rows if r["label"] not in {"GOOD_STRONG", "VALIDATED_BAD"}]
        if not good or not bad:
            return rows
        n = min(len(good), len(bad))
        rng = np.random.default_rng(9009)
        good_idx = rng.choice(len(good), n, replace=False)
        bad_idx = rng.choice(len(bad), n, replace=False)
        return [good[i] for i in good_idx] + [bad[i] for i in bad_idx] + other

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index: int) -> dict[str, Any]:
        sample = self.rows[index]
        label = str(sample["label"])
        subtype = str(sample.get("bad_subtype") or "unknown")
        action = candidate_action_seq(sample, self.action_steps, self.action_dim)
        history = history_seq(sample, self.history_steps, self.history_dim)
        context = context_vec(sample)
        action_flat = action.reshape(-1)
        flat = np.concatenate([context, action_flat, history.reshape(-1)]).astype(np.float32)
        context_action = np.concatenate([context, action_flat]).astype(np.float32)
        y, weight, ordinal, subtype_id = target_values(label, self.target_mode, subtype)
        split_row = sample.get("_stage9_split_row") or {}
        return {
            "flat": torch.from_numpy(flat),
            "context_action": torch.from_numpy(context_action),
            "action_flat": torch.from_numpy(action_flat.astype(np.float32)),
            "action_seq": torch.from_numpy(action.astype(np.float32)),
            "history_seq": torch.from_numpy(history.astype(np.float32)),
            "target": torch.tensor(y, dtype=torch.float32),
            "weight": torch.tensor(weight, dtype=torch.float32),
            "ordinal": torch.tensor(ordinal, dtype=torch.long),
            "subtype": torch.tensor(subtype_id, dtype=torch.long),
            "sample_id": str(sample.get("sample_id")),
            "label": label,
            "bad_subtype": subtype,
            "state_id": str(split_row.get("state_id") or metadata(sample).get("state_id") or ""),
            "task_name": str(split_row.get("task_name") or metadata(sample).get("task_name") or ""),
            "perturbation_type": str(split_row.get("perturbation_type") or metadata(sample).get("perturbation_type") or ""),
            "seed": str(split_row.get("seed") or metadata(sample).get("simvla_generation_seed") or ""),
        }


def collate_stage9(batch: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    tensor_keys = ["flat", "context_action", "action_flat", "action_seq", "history_seq", "target", "weight", "ordinal", "subtype"]
    for key in tensor_keys:
        out[key] = torch.stack([item[key] for item in batch])
    for key in ["sample_id", "label", "bad_subtype", "state_id", "task_name", "perturbation_type", "seed"]:
        out[key] = [item[key] for item in batch]
    return out


def parent_rollout_index(state_id: str) -> int | None:
    match = re.search(r"_r(\d+)_", state_id)
    return int(match.group(1)) if match else None


def split_task_id(task_name: str) -> int | None:
    match = re.search(r"_task(\d+)$", task_name)
    return int(match.group(1)) if match else None


def group_safe_split(source_split_dir: Path, out_dir: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for name in ["train", "calib", "test_seen_task", "test_unseen_task", "test_unseen_seed", "test_unseen_perturbation"]:
        path = source_split_dir / f"{name}.jsonl"
        if path.exists():
            for row in read_jsonl(path):
                row = dict(row)
                row["_original_split"] = name
                rows.append(row)
    by_sample: dict[str, dict[str, Any]] = {}
    for row in rows:
        by_sample[str(row["sample_id"])] = row
    rows = list(by_sample.values())
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get("state_id") or row.get("sample_id"))].append(row)

    split_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for state_id, group in groups.items():
        first = group[0]
        task_id = split_task_id(str(first.get("task_name") or ""))
        rollout = parent_rollout_index(state_id)
        perturb = first.get("perturbation_type")
        if perturb == "initial_position":
            split = "test_unseen_perturbation"
        elif task_id in {8, 9}:
            split = "test_unseen_task"
        elif rollout in {6, 7}:
            split = "test_unseen_seed"
        else:
            digest = int(hashlib.sha1(state_id.encode()).hexdigest()[:8], 16) % 100
            if digest < 10:
                split = "calib"
            elif digest < 20:
                split = "test_seen_task"
            else:
                split = "train"
        for row in group:
            clean = {k: v for k, v in row.items() if not k.startswith("_")}
            clean["group_safe_split"] = split
            split_rows[split].append(clean)

    out_dir.mkdir(parents=True, exist_ok=True)
    required = ["train", "calib", "test_seen_task", "test_unseen_task", "test_unseen_seed", "test_unseen_perturbation"]
    for split in required:
        write_jsonl(out_dir / f"{split}.jsonl", split_rows[split])

    leakage: dict[str, list[str]] = defaultdict(list)
    for state_id, group in groups.items():
        assigned = {row.get("group_safe_split") for split in required for row in split_rows[split] if row.get("state_id") == state_id}
        if len(assigned) > 1:
            leakage[state_id] = sorted(str(x) for x in assigned)
    manifest = {
        "source_split_dir": str(source_split_dir),
        "split_dir": str(out_dir),
        "num_samples": len(rows),
        "num_same_state_groups": len(groups),
        "same_state_group_leakage_count": len(leakage),
        "same_state_group_leakage_examples": dict(list(leakage.items())[:10]),
        "split_counts": {},
        "notes": [
            "test_unseen_seed is group-safe and uses parent rollout index parsed from state_id because candidate-generation seeds coexist within each same-state group.",
            "No task id, suite id, perturbation type, or seed is used by Stage9RiskDataset as a model feature; those fields stay in split metadata and prediction reports only.",
        ],
    }
    for split in required:
        split_data = split_rows[split]
        manifest["split_counts"][split] = {
            "num_samples": len(split_data),
            "num_groups": len({x.get("state_id") for x in split_data}),
            "label_counts": dict(Counter(x.get("label") for x in split_data)),
            "bad_subtype_counts": dict(Counter(x.get("bad_subtype") for x in split_data if x.get("label") == "VALIDATED_BAD")),
            "task_counts": dict(Counter(x.get("task_name") for x in split_data)),
            "perturbation_counts": dict(Counter(x.get("perturbation_type") for x in split_data)),
        }
    (out_dir / "split_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--make-group-safe-splits", action="store_true")
    parser.add_argument("--source-split-dir")
    parser.add_argument("--out-dir")
    args = parser.parse_args()
    if args.make_group_safe_splits:
        manifest = group_safe_split(Path(args.source_split_dir), Path(args.out_dir))
        print(json.dumps(manifest, indent=2, sort_keys=True))
    else:
        raise SystemExit("no action requested")


if __name__ == "__main__":
    main()
