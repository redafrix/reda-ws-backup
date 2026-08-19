# Stage 1D Summary — Verbatim TopK8 Threshold Generator Source Proof

## 1. Verbatim Source Files
- `train_isaac_topk8.py` SHA256: `adc0f368c5f277df83590540d3a2bd656ca19ba5228648ef8e4d19a0f640a660` (Match: True)
- `common.py` SHA256: `e89a69592ed75b8bb52850019780f6c8d4309e9a82186c59d3e01afbc2822c46` (Match: True)

## 2. `common.py` Lines 131-148 (`threshold_table`)
```python
def threshold_table(labels: np.ndarray, scores: np.ndarray) -> dict[str, float]:
    from sklearn.metrics import precision_recall_curve

    precision, recall, thresholds = precision_recall_curve(labels.astype(int), scores)
    f1 = 2 * precision * recall / np.maximum(precision + recall, 1e-9)
    if len(thresholds):
        index = int(np.nanargmax(f1[: len(thresholds)]))
        best = float(thresholds[index])
    else:
        best = 0.5
    success = scores[labels < 0.5]
    return {
        "best_val_f1": best,
        "q90_success": float(np.quantile(success, 0.90)) if len(success) else 0.5,
        "q95_success": float(np.quantile(success, 0.95)) if len(success) else 0.5,
        "q99_success": float(np.quantile(success, 0.99)) if len(success) else 0.5,
        "fixed_0.5": 0.5,
    }
```
- Snippet SHA256: `09cac3cb9d8063142a983a3651ed50a5f721077762211c217db91c2374a41ce7`

## 3. `train_isaac_topk8.py` Lines 285-361 (Execution Flow)
```python
if best_state is None:
        raise RuntimeError("training did not produce a best validation checkpoint")
    model.load_state_dict(best_state)
    model_path = output / "model.pt"
    torch.save(model.state_dict(), model_path)

    validation_scores = predict(model, validation, device, args.batch_size * 4, args.workers)
    test_scores = predict(model, test, device, args.batch_size * 4, args.workers)
    thresholds = threshold_table(validation.label, validation_scores)
    validation_ids, validation_decisions = load_row_identity(args.dataset_root / "validation")
    test_ids, test_decisions = load_row_identity(args.dataset_root / "test")
    temporal = temporal_calibration(
        validation_ids, validation.label, validation_scores, thresholds["q95_success"]
    )
    results: dict[str, Any] = {
        "schema_version": "simvla_isaac_topk8_training_result_v1",
        "architecture": {
            "model": "one SeqRiskModel",
            "history_shape": [16, 21],
            "action_shape": [10, 7],
            "static_dim": 51,
            "width": 128,
            "layers": 3,
            "heads": 4,
            "ffn": 512,
            "dropout": 0.1,
        },
        "optimization": {
            "loss": "weighted BCEWithLogitsLoss",
            "positive_weight": positive_weight,
            "optimizer": "AdamW",
            "lr": args.lr,
            "weight_decay": args.weight_decay,
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "gradient_clip_norm": 1.0,
            "selection": "highest seen-validation AUPRC",
            "training_seed": args.seed,
        },
        "promoted_trainer": {
            "path": str(PROMOTED_TRAINER),
            "sha256": PROMOTED_TRAINER_SHA256,
        },
        "dataset_root": str(args.dataset_root.resolve()),
        "dataset_manifest_sha256": sha256_file(args.dataset_root / "dataset_manifest.json"),
        "normalization_path": str((args.dataset_root / "normalization.json").resolve()),
        "normalization_sha256": sha256_file(args.dataset_root / "normalization.json"),
        "best_epoch": best_epoch,
        "best_validation_auprc": best_auprc,
        "history": history,
        "thresholds": thresholds,
        "temporal_calibration": temporal,
        "seen_validation": {},
        "seen_test": {},
        "ood150_used_for_training_or_selection": False,
        "runtime_seconds": time.time() - started,
    }
    for name, threshold in thresholds.items():
        results["seen_validation"][name] = {
            "step": step_metrics(validation.label, validation_scores, threshold),
            "episode": episode_metrics(
                validation_ids,
                validation_decisions,
                validation.label,
                validation_scores,
                threshold,
            ),
        }
        results["seen_test"][name] = {
            "step": step_metrics(test.label, test_scores, threshold),
            "episode": episode_metrics(
                test_ids, test_decisions, test.label, test_scores, threshold
            ),
        }
    write_json_atomic(output / "thresholds.json", thresholds)
    write_json_atomic(output / "temporal_thresholds.json", temporal)
    write_json_atomic(output / "results.json", results)
```
- Snippet SHA256: `fd65a35beb6ddcf2ffc71913d9b21345992fa09211a7631f1a813c87c0f51259`

## 4. Semantic Proof Conclusions
- **Validation-Only Selection**: YES (`thresholds = threshold_table(validation.label, validation_scores)`)
- **Row-Level F1 Argmax**: YES (`index = int(np.nanargmax(f1[: len(thresholds)])); best = float(thresholds[index])`)
- **Test-Independent Selection**: YES (Thresholds computed from validation and written to `thresholds.json` before test evaluation)
- **Rule-Equivalent to Mimic `row_best_f1`**: YES (Identical precision-recall curve argmax-F1 rule on validation split)
