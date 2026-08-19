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
