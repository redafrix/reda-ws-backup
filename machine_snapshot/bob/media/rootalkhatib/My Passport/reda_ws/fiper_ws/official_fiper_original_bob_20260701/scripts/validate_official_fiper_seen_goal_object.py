import json
import pickle
from pathlib import Path
import numpy as np
import torch

ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701")
DATA_DIR = ROOT / "official_fiper_data" / "libero_goal_object_official" / "processed_rollouts"
OUT_JSON = ROOT / "VALIDATION_SUMMARY.json"
OUT_MD = ROOT / "MATERIALIZATION_REPORT.md"

def fail(msg):
    raise SystemExit("VALIDATION_FAILED: " + msg)

def main():
    obs_path = DATA_DIR / "obs_embeddings.pt"
    act_path = DATA_DIR / "action_preds.pt"
    meta_path = DATA_DIR / "metadata.pkl"
    for p in [obs_path, act_path, meta_path]:
        if not p.exists():
            fail(f"missing {p}")
    obs = torch.load(obs_path, map_location="cpu")
    actions = torch.load(act_path, map_location="cpu")
    with meta_path.open("rb") as f:
        meta = pickle.load(f)
    if tuple(obs.shape[1:]) != (960,): fail(f"bad obs shape {tuple(obs.shape)}")
    if tuple(actions.shape[1:]) != (9, 10, 7): fail(f"bad action shape {tuple(actions.shape)}")
    if obs.shape[0] != actions.shape[0]: fail("obs/action step mismatch")
    if int(meta["num_steps"]) != int(obs.shape[0]): fail("metadata num_steps mismatch")
    if int(meta["num_rollouts"]) != 900: fail(f"expected 900 rollouts got {meta['num_rollouts']}")
    if not torch.isfinite(obs).all(): fail("obs has NaN/Inf")
    if not torch.isfinite(actions).all(): fail("actions has NaN/Inf")
    calib = np.asarray(meta["calibration_rollout_labels"], dtype=bool)
    test = np.asarray(meta["test_rollout_labels"], dtype=bool)
    success = np.asarray(meta["successful_rollout_labels"], dtype=bool)
    failed = np.asarray(meta["failed_rollout_labels"], dtype=bool)
    idl = np.asarray(meta["id_rollout_labels"], dtype=bool)
    ood = np.asarray(meta["ood_rollout_labels"], dtype=bool)
    keys = list(meta["episode_keys"])
    n = int(meta["num_rollouts"])
    for name, arr in [("calib",calib),("test",test),("success",success),("failed",failed),("id",idl),("ood",ood)]:
        if len(arr) != n: fail(f"{name} len {len(arr)} != {n}")
    checks = {
        "validation": "PASS",
        "obs_shape": list(obs.shape),
        "action_shape": list(actions.shape),
        "num_rollouts": n,
        "num_steps": int(meta["num_steps"]),
        "train_success": int((~calib & ~test & success & idl & ~ood).sum()),
        "calib_success": int((calib & success & idl & ~ood).sum()),
        "seen_test_success": int((test & success & idl & ~ood).sum()),
        "seen_test_failure": int((test & failed & idl & ~ood).sum()),
        "calib_test_overlap": int((calib & test).sum()),
        "success_failed_overlap": int((success & failed).sum()),
        "ood_true": int(ood.sum()),
        "unique_episode_keys": len(set(keys)),
    }
    if checks["train_success"] != 500: fail(str(checks))
    if checks["calib_success"] != 150: fail(str(checks))
    if checks["seen_test_success"] != 150: fail(str(checks))
    if checks["seen_test_failure"] != 100: fail(str(checks))
    if checks["calib_test_overlap"] != 0: fail(str(checks))
    if checks["success_failed_overlap"] != 0: fail(str(checks))
    if checks["ood_true"] != 0: fail(str(checks))
    if checks["unique_episode_keys"] != 900: fail(str(checks))
    OUT_JSON.write_text(json.dumps(checks, indent=2))
    lines = [
        "# Official FIPER Seen Goal Object Materialization Report",
        "",
        "Validation: PASS",
        "",
        f"- obs_embeddings.pt: `{tuple(obs.shape)}`",
        f"- action_preds.pt: `{tuple(actions.shape)}`",
        f"- num_rollouts: `{n}`",
        f"- num_steps: `{int(meta['num_steps'])}`",
        "",
        "| Split | Count |",
        "|---|---:|",
        f"| train_success | {checks['train_success']} |",
        f"| calib_success | {checks['calib_success']} |",
        f"| seen_test_success | {checks['seen_test_success']} |",
        f"| seen_test_failure | {checks['seen_test_failure']} |",
        "",
        "Flags:",
        "- DATASET_MATERIALIZED = YES",
        "- DATASET_VALIDATION_PASS = YES",
        "- CALIBRATION_SEEN_SUCCESS_ONLY = YES",
        "- OOD_USED = NO",
    ]
    OUT_MD.write_text("\n".join(lines)+"\n")
    print(json.dumps(checks, indent=2))

if __name__ == "__main__":
    main()
