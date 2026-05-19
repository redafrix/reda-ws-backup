from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from training_stage9.stage9_eval import accepted_risk_table, binary_metrics, read_predictions, summarize_predictions, write_predictions


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -50.0, 50.0)))


def logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def fit_temperature(y: np.ndarray, p: np.ndarray) -> dict[str, Any]:
    logits = logit(p)
    best = {"temperature": 1.0, "nll": float("inf")}
    for temp in np.linspace(0.25, 5.0, 96):
        pp = sigmoid(logits / temp)
        nll = -np.mean(y * np.log(np.clip(pp, 1e-6, 1)) + (1 - y) * np.log(np.clip(1 - pp, 1e-6, 1)))
        if nll < best["nll"]:
            best = {"temperature": float(temp), "nll": float(nll)}
    return best


def apply_temperature(p: np.ndarray, params: dict[str, Any]) -> np.ndarray:
    return sigmoid(logit(p) / float(params["temperature"]))


def fit_platt(y: np.ndarray, p: np.ndarray) -> Any:
    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression(solver="lbfgs")
    model.fit(logit(p).reshape(-1, 1), y.astype(int))
    return model


def apply_platt(p: np.ndarray, model: Any) -> np.ndarray:
    return model.predict_proba(logit(p).reshape(-1, 1))[:, 1]


def fit_isotonic(y: np.ndarray, p: np.ndarray) -> Any:
    from sklearn.isotonic import IsotonicRegression

    model = IsotonicRegression(out_of_bounds="clip")
    model.fit(p, y.astype(float))
    return model


def apply_isotonic(p: np.ndarray, model: Any) -> np.ndarray:
    return model.predict(p)


def fit_beta(y: np.ndarray, p: np.ndarray) -> Any:
    from sklearn.linear_model import LogisticRegression

    features = np.stack([np.log(np.clip(p, 1e-6, 1.0)), np.log(np.clip(1.0 - p, 1e-6, 1.0))], axis=1)
    model = LogisticRegression(solver="lbfgs")
    model.fit(features, y.astype(int))
    return model


def apply_beta(p: np.ndarray, model: Any) -> np.ndarray:
    features = np.stack([np.log(np.clip(p, 1e-6, 1.0)), np.log(np.clip(1.0 - p, 1e-6, 1.0))], axis=1)
    return model.predict_proba(features)[:, 1]


def split_arrays(rows: list[dict[str, Any]], split: str) -> tuple[list[dict[str, Any]], np.ndarray, np.ndarray]:
    selected = [r for r in rows if r.get("split") == split and r.get("label") in {"GOOD_STRONG", "VALIDATED_BAD"}]
    y = np.asarray([1 if r["label"] == "VALIDATED_BAD" else 0 for r in selected], dtype=np.int64)
    p = np.asarray([float(r["risk_prob"]) for r in selected], dtype=np.float64)
    return selected, y, p


def calibrate_predictions(prediction_path: Path, out_dir: Path) -> dict[str, Any]:
    rows = read_predictions(prediction_path)
    calib_rows, y_calib, p_calib = split_arrays(rows, "calib")
    if len(y_calib) < 20 or y_calib.sum() == 0 or y_calib.sum() == len(y_calib):
        raise RuntimeError(f"not enough calibration labels in {prediction_path}")
    methods: dict[str, Any] = {}
    methods["raw"] = None
    methods["temperature"] = fit_temperature(y_calib, p_calib)
    methods["platt"] = fit_platt(y_calib, p_calib)
    methods["isotonic"] = fit_isotonic(y_calib, p_calib)
    methods["beta"] = fit_beta(y_calib, p_calib)

    def apply(name: str, p: np.ndarray) -> np.ndarray:
        if name == "raw":
            return p
        if name == "temperature":
            return apply_temperature(p, methods[name])
        if name == "platt":
            return apply_platt(p, methods[name])
        if name == "isotonic":
            return apply_isotonic(p, methods[name])
        if name == "beta":
            return apply_beta(p, methods[name])
        raise KeyError(name)

    out_dir.mkdir(parents=True, exist_ok=True)
    method_metrics: dict[str, Any] = {}
    for method in methods:
        calibrated_rows: list[dict[str, Any]] = []
        for row in rows:
            new = dict(row)
            new["risk_prob_raw"] = float(row["risk_prob"])
            new["risk_prob"] = float(apply(method, np.asarray([float(row["risk_prob"])]))[0])
            new["calibration_method"] = method
            calibrated_rows.append(new)
        write_predictions(out_dir / f"predictions_{method}.jsonl", calibrated_rows)
        method_metrics[method] = summarize_predictions(calibrated_rows)

    # Conformal-style thresholds are selected on calibration predictions.
    conformal: dict[str, Any] = {}
    for method in methods:
        p = apply(method, p_calib)
        order = np.argsort(p)
        for accept in [0.90, 0.75, 0.50, 0.25]:
            k = max(1, int(round(len(p) * accept)))
            threshold = float(p[order[:k]].max())
            accepted = p <= threshold
            conformal[f"{method}_accept_{int(accept * 100)}pct"] = {
                "method": method,
                "target_accept_fraction": accept,
                "threshold": threshold,
                "calib_accepted_bad_leakage": float(y_calib[accepted].sum() / max(1, accepted.sum())),
                "calib_accept_count": int(accepted.sum()),
            }

    summary = {
        "prediction_path": str(prediction_path),
        "calibration_count": int(len(y_calib)),
        "calibration_bad_count": int(y_calib.sum()),
        "methods": {k: (v if isinstance(v, dict) else str(v)) for k, v in methods.items()},
        "metrics": method_metrics,
        "conformal_thresholds": conformal,
    }
    (out_dir / "calibration_metrics.json").write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + "\n")
    report_lines = ["# Stage 9 Calibration Report", "", f"Predictions: `{prediction_path}`", ""]
    for method, values in method_metrics.items():
        clean = values.get("test_seen_task", {}).get("clean_binary", {})
        all_non_bad = values.get("test_seen_task", {}).get("bad_vs_all_non_bad", {})
        report_lines.extend(
            [
                f"## {method}",
                "",
                f"- test_seen_task AUROC BAD: `{clean.get('auroc_bad')}`",
                f"- test_seen_task AUPRC BAD: `{clean.get('auprc_bad')}`",
                f"- test_seen_task Brier: `{clean.get('brier')}`",
                f"- accepted BAD leakage @ accept 90%: `{(all_non_bad.get('accepted_risk') or {}).get('accept_90pct', {}).get('accepted_bad_leakage')}`",
                "",
            ]
        )
    (out_dir / "calibration_report.md").write_text("\n".join(report_lines) + "\n")
    return summary


def calibrate_campaign(campaign_dir: Path) -> dict[str, Any]:
    results: dict[str, Any] = {}
    for pred in sorted(campaign_dir.rglob("predictions.jsonl")):
        if "calibration" in pred.parts:
            continue
        out_dir = pred.parent / "calibration"
        try:
            results[str(pred.parent)] = calibrate_predictions(pred, out_dir)
        except Exception as exc:  # noqa: BLE001
            results[str(pred.parent)] = {"error": str(exc)}
    ensemble_dir = campaign_dir / "ensembles" / "ensemble_top3"
    try:
        results[str(ensemble_dir)] = make_top3_ensemble(campaign_dir, ensemble_dir)
    except Exception as exc:  # noqa: BLE001
        results[str(ensemble_dir)] = {"error": str(exc)}
    (campaign_dir / "calibration_campaign_summary.json").write_text(json.dumps(results, indent=2, sort_keys=True, default=str) + "\n")
    return results


def model_score(metrics_path: Path) -> float:
    try:
        metrics = json.loads(metrics_path.read_text())
        split = metrics.get("splits", {}).get("test_seen_task", {}).get("clean_binary", {})
        score = split.get("auroc_bad")
        if score is not None:
            return float(score)
        brier = split.get("brier")
        if brier is not None:
            return -float(brier)
    except Exception:
        return -1e9
    return -1e9


def make_top3_ensemble(campaign_dir: Path, out_dir: Path) -> dict[str, Any]:
    candidates: list[tuple[float, Path]] = []
    for metrics_path in campaign_dir.rglob("metrics.json"):
        pred = metrics_path.parent / "predictions.jsonl"
        if pred.exists():
            candidates.append((model_score(metrics_path), pred))
    candidates = sorted(candidates, key=lambda x: x[0], reverse=True)[:3]
    if len(candidates) < 2:
        raise RuntimeError("need at least two completed prediction files for ensemble_top3")
    keyed: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for score, pred in candidates:
        for row in read_predictions(pred):
            keyed.setdefault((str(row.get("split")), str(row.get("sample_id"))), []).append(row)
    ensemble_rows: list[dict[str, Any]] = []
    for (_split, _sid), rows in keyed.items():
        if len(rows) != len(candidates):
            continue
        base = dict(rows[0])
        probs = np.asarray([float(r["risk_prob"]) for r in rows], dtype=np.float64)
        base["risk_prob"] = float(probs.mean())
        base["risk_prob_std"] = float(probs.std())
        base["ensemble_members"] = [str(path.parent) for _, path in candidates]
        base["ensemble_scores"] = [float(score) for score, _ in candidates]
        ensemble_rows.append(base)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_predictions(out_dir / "predictions.jsonl", ensemble_rows)
    metrics = {
        "members": [{"score": float(score), "prediction_path": str(path)} for score, path in candidates],
        "splits": summarize_predictions(ensemble_rows),
    }
    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True, default=str) + "\n")
    return calibrate_predictions(out_dir / "predictions.jsonl", out_dir / "calibration")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions")
    parser.add_argument("--out-dir")
    parser.add_argument("--campaign-dir")
    args = parser.parse_args()
    if args.campaign_dir:
        print(json.dumps(calibrate_campaign(Path(args.campaign_dir)), indent=2, sort_keys=True, default=str))
    elif args.predictions and args.out_dir:
        print(json.dumps(calibrate_predictions(Path(args.predictions), Path(args.out_dir)), indent=2, sort_keys=True, default=str))
    else:
        raise SystemExit("use --predictions/--out-dir or --campaign-dir")


if __name__ == "__main__":
    main()
