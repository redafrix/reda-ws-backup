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
