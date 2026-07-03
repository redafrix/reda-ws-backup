from __future__ import annotations
import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

def get_continuous_risk(sample: dict) -> dict:
    # Look in sample["continuous_risk"], then sample["label"] (if it's a dict), then sample itself
    for key in ["continuous_risk", "label"]:
        val = sample.get(key)
        if isinstance(val, dict) and "risk_score" in val:
            return val
    # Fallback to top-level
    if "risk_score" in sample:
        return sample
    return {}

def resolve_risk_fields(sample: dict, default_score: float = 0.0) -> tuple[float, float, str, str, str]:
    cr = get_continuous_risk(sample)
    risk_score = cr.get("risk_score")
    if risk_score is None:
        risk_score = default_score
    else:
        risk_score = float(risk_score)
        
    risk_confidence = cr.get("risk_confidence")
    if risk_confidence is None:
        risk_confidence = 1.0
    else:
        risk_confidence = float(risk_confidence)
        
    risk_bin = cr.get("risk_bin") or "SAFE_STRONG"
    legacy_label = cr.get("legacy_label_suggestion")
    bad_subtype = cr.get("bad_subtype") or sample.get("bad_subtype") or "unknown"
    
    # Map to standard legacy label based on risk_bin
    # "SAFE_STRONG" -> "GOOD_STRONG"
    # "SAFE_WEAK" -> "GOOD_WEAK"
    # "UNCERTAIN" -> "AMBIGUOUS"
    # "RISKY_STRONG" -> "VALIDATED_BAD"
    bin_map = {
        "SAFE_STRONG": "GOOD_STRONG",
        "SAFE_WEAK": "GOOD_WEAK",
        "UNCERTAIN": "AMBIGUOUS",
        "RISKY_STRONG": "VALIDATED_BAD"
    }
    mapped_label = bin_map.get(risk_bin)
    if not mapped_label:
        mapped_label = legacy_label or "GOOD_STRONG"
        
    return risk_score, risk_confidence, risk_bin, mapped_label, bad_subtype

def main():
    parser = argparse.ArgumentParser(description="Compile and split Stage 9 V2 datasets with continuous risk labels.")
    parser.add_argument("--expert-anchors", required=True, help="Path to expert low-risk anchors jsonl")
    parser.add_argument("--failure-replays", required=True, help="Path to failure replays jsonl")
    parser.add_argument("--out-dir", required=True, help="Output directory to write splits")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for splitting")
    args = parser.parse_args()

    expert_path = Path(args.expert_anchors)
    failure_path = Path(args.failure_replays)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not expert_path.exists():
        raise FileNotFoundError(f"Expert anchors path not found: {expert_path}")
    if not failure_path.exists():
        raise FileNotFoundError(f"Failure replays path not found: {failure_path}")

    print(f"Reading expert anchors from: {expert_path}")
    expert_rows = []
    with expert_path.open() as f:
        for line in f:
            if line.strip():
                expert_rows.append(json.loads(line))
    print(f"Loaded {len(expert_rows)} expert anchor samples.")

    print(f"Reading failure replays from: {failure_path}")
    failure_rows = []
    with failure_path.open() as f:
        for line in f:
            if line.strip():
                failure_rows.append(json.loads(line))
    print(f"Loaded {len(failure_rows)} failure replay samples.")

    # Mapped metadata rows
    mapped_rows = []

    for row in expert_rows:
        sid = row["sample_id"]
        # Expert anchors are clean low-risk positives (default risk score 0.05, confidence 0.90)
        risk_score, risk_confidence, risk_bin, mapped_label, bad_subtype = resolve_risk_fields(row, default_score=0.05)
        mapped_rows.append({
            "sample_id": sid,
            "label": mapped_label,
            "bad_subtype": bad_subtype,
            "source_jsonl": str(expert_path.resolve()),
            "risk_score": risk_score,
            "risk_confidence": risk_confidence,
            "risk_bin": risk_bin
        })

    for row in failure_rows:
        sid = row["sample_id"]
        # Failure replays have active mined risk labels
        risk_score, risk_confidence, risk_bin, mapped_label, bad_subtype = resolve_risk_fields(row, default_score=0.5)
        mapped_rows.append({
            "sample_id": sid,
            "label": mapped_label,
            "bad_subtype": bad_subtype,
            "source_jsonl": str(failure_path.resolve()),
            "risk_score": risk_score,
            "risk_confidence": risk_confidence,
            "risk_bin": risk_bin
        })

    print(f"Total compiled samples: {len(mapped_rows)}")

    # Group by mapped legacy label for stratification
    groups = defaultdict(list)
    for row in mapped_rows:
        groups[row["label"]].append(row)

    train_rows = []
    calib_rows = []
    test_rows = []

    rng = random.Random(args.seed)

    print("\nStratified split stats:")
    for label, group in sorted(groups.items()):
        rng.shuffle(group)
        n = len(group)
        n_train = int(round(0.8 * n))
        n_calib = int(round(0.1 * n))
        
        g_train = group[:n_train]
        g_calib = group[n_train:n_train + n_calib]
        g_test = group[n_train + n_calib:]
        
        train_rows.extend(g_train)
        calib_rows.extend(g_calib)
        test_rows.extend(g_test)
        print(f"  Label '{label}': total={n}, train={len(g_train)}, calib={len(g_calib)}, test={len(g_test)}")

    # Shuffle the final split lists to interleave labels
    rng.shuffle(train_rows)
    rng.shuffle(calib_rows)
    rng.shuffle(test_rows)

    # Write split manifest JSONL files
    (out_dir / "train.jsonl").write_text("\n".join(json.dumps(r) for r in train_rows) + "\n")
    (out_dir / "calib.jsonl").write_text("\n".join(json.dumps(r) for r in calib_rows) + "\n")
    (out_dir / "test.jsonl").write_text("\n".join(json.dumps(r) for r in test_rows) + "\n")

    print(f"\nWritten splits to: {out_dir}")
    print(f"  train.jsonl: {len(train_rows)} samples")
    print(f"  calib.jsonl: {len(calib_rows)} samples")
    print(f"  test.jsonl:  {len(test_rows)} samples")

if __name__ == "__main__":
    main()
