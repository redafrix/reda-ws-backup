import json
import pickle
from pathlib import Path

import numpy as np
import torch


EXP_DIR = Path("/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625")
DATA_DIR = EXP_DIR / "official_fiper_data" / "libero_fold00" / "processed_rollouts"
OOD_SUMMARIES = Path(
    "/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/"
    "simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622/episode_summaries.jsonl"
)
SPLIT_MANIFEST = Path(
    "/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/"
    "worker_0/stratified_query_samples_50train_15calib_per_task_manifest.json"
)


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


def main() -> None:
    obs_path = DATA_DIR / "obs_embeddings.pt"
    act_path = DATA_DIR / "action_preds.pt"
    meta_path = DATA_DIR / "metadata.pkl"
    for path in [obs_path, act_path, meta_path, OOD_SUMMARIES, SPLIT_MANIFEST]:
        if not path.exists():
            fail(f"missing {path}")

    obs = torch.load(obs_path, map_location="cpu")
    actions = torch.load(act_path, map_location="cpu")
    with meta_path.open("rb") as f:
        meta = pickle.load(f)

    if tuple(obs.shape[1:]) != (960,):
        fail(f"bad obs shape {tuple(obs.shape)}")
    if tuple(actions.shape[1:]) != (9, 10, 7):
        fail(f"bad action shape {tuple(actions.shape)}")
    if obs.shape[0] != actions.shape[0]:
        fail(f"step mismatch obs={obs.shape[0]} actions={actions.shape[0]}")
    if not torch.isfinite(obs).all():
        fail("obs contains NaN/Inf")
    if not torch.isfinite(actions).all():
        fail("actions contains NaN/Inf")

    n_rollouts = int(meta["num_rollouts"])
    n_steps = int(meta["num_steps"])
    if n_steps != int(obs.shape[0]):
        fail(f"metadata num_steps={n_steps} tensor steps={obs.shape[0]}")
    if n_rollouts != 830:
        fail(f"expected 830 rollouts, got {n_rollouts}")

    calib = np.asarray(meta["calibration_rollout_labels"], dtype=bool)
    test = np.asarray(meta["test_rollout_labels"], dtype=bool)
    success = np.asarray(meta["successful_rollout_labels"], dtype=bool)
    failed = np.asarray(meta["failed_rollout_labels"], dtype=bool)
    id_labels = np.asarray(meta["id_rollout_labels"], dtype=bool)
    ood = np.asarray(meta["ood_rollout_labels"], dtype=bool)
    keys = list(meta["episode_keys"])

    for name, arr in [
        ("calibration", calib),
        ("test", test),
        ("success", success),
        ("failed", failed),
        ("id", id_labels),
        ("ood", ood),
    ]:
        if len(arr) != n_rollouts:
            fail(f"{name} label length {len(arr)} != {n_rollouts}")

    if int(calib.sum()) != 150:
        fail(f"expected 150 calibration rollouts, got {int(calib.sum())}")
    if int(test.sum()) != 180:
        fail(f"expected 180 test/OOD rollouts, got {int(test.sum())}")
    if int(ood.sum()) != 180:
        fail(f"expected 180 OOD rollouts, got {int(ood.sum())}")
    if int((calib & test).sum()) != 0:
        fail("calibration/test overlap")
    if int((id_labels & ood).sum()) != 0:
        fail("ID/OOD overlap")
    if int((success & failed).sum()) != 0:
        fail("success/failure overlap")

    ood_outcomes = {}
    ood_tasks = {}
    for line in OOD_SUMMARIES.open():
        if not line.strip():
            continue
        row = json.loads(line)
        ood_outcomes[row["episode_id"]] = bool(row["success"])
        ood_tasks[row["episode_id"]] = int(row["task_id"])
    if len(ood_outcomes) != 180:
        fail(f"expected 180 OOD summaries, got {len(ood_outcomes)}")

    test_keys = [k for k, is_test in zip(keys, test) if is_test]
    if set(test_keys) != set(ood_outcomes):
        fail("test keys do not match OOD summary episode IDs")
    test_success = sum(ood_outcomes[k] for k in test_keys)
    test_failure = len(test_keys) - test_success
    if (test_success, test_failure) != (149, 31):
        fail(f"expected OOD 149/31 success/failure, got {test_success}/{test_failure}")
    task_counts = {t: sum(ood_tasks[k] == t for k in test_keys) for t in range(18)}
    if any(v != 10 for v in task_counts.values()):
        fail(f"bad OOD per-task counts {task_counts}")

    manifest = json.loads(SPLIT_MANIFEST.read_text())
    if manifest["train_count"] != 500 or manifest["calib_count"] != 150:
        fail("bad split manifest train/calib counts")
    expected_50 = {str(t): 50 for t in range(10)}
    expected_15 = {str(t): 15 for t in range(10)}
    if manifest["train_counts_by_task"] != expected_50:
        fail(f"bad train counts {manifest['train_counts_by_task']}")
    if manifest["calib_counts_by_task"] != expected_15:
        fail(f"bad calib counts {manifest['calib_counts_by_task']}")

    summary = {
        "validation": "PASS",
        "obs_shape": list(obs.shape),
        "action_shape": list(actions.shape),
        "num_rollouts": n_rollouts,
        "num_steps": n_steps,
        "train_rollouts": 500,
        "calibration_rollouts": int(calib.sum()),
        "ood_test_rollouts": int(test.sum()),
        "ood_success": test_success,
        "ood_failure": test_failure,
        "ood_task_counts": task_counts,
    }
    out = EXP_DIR / "VALIDATION_SUMMARY.json"
    out.write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
