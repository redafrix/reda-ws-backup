from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from training_stage9.stage9_dataset import group_safe_split


TARGET_MODES = ["clean_binary", "soft_labels", "soft_no_ambiguous", "ordinal", "subtype_multitask"]
BOB_MODELS = [
    "small_history_transformer_k8",
    "medium_history_transformer_k8",
    "large_history_transformer_k8",
    "action_chunk_transformer",
    "history_action_cross_attention_transformer",
    "Mamba_history_k8",
    "Mamba_medium_history_k8",
]
SAM_MODELS = [
    "action_only_mlp",
    "context_action_mlp",
    "history_gru_k8",
    "history_lstm_k8",
    "TCN_history_k8",
    "residual_mlp_large",
    "gated_context_action_mlp",
]


def q(value: str | Path) -> str:
    return shlex.quote(str(value))


def train_command(
    split_dir: Path,
    out_dir: Path,
    model: str,
    target_mode: str,
    source_remap: list[str],
    epochs: int,
    max_train_samples: int | None,
    batch_size: int,
    mc_dropout: int = 0,
) -> list[str]:
    cmd = [
        "python3",
        "-u",
        "-m",
        "training_stage9.train_stage9_risk_model",
        "--split-dir",
        str(split_dir),
        "--output-dir",
        str(out_dir),
        "--model",
        model,
        "--target-mode",
        target_mode,
        "--epochs",
        str(epochs),
        "--batch-size",
        str(batch_size),
        "--num-workers",
        "2",
        "--balanced-binary-train",
    ]
    if max_train_samples:
        cmd.extend(["--max-train-samples", str(max_train_samples)])
    for remap in source_remap:
        cmd.extend(["--source-remap", remap])
    if mc_dropout:
        cmd.extend(["--mc-dropout-passes", str(mc_dropout)])
    return cmd


def queue_script(
    workspace_root: Path,
    campaign_dir: Path,
    split_dir: Path,
    machine_role: str,
    source_remap: list[str],
    quick_epochs: int,
    quick_max_train_samples: int | None,
    batch_size: int,
) -> tuple[str, list[dict[str, Any]]]:
    models = BOB_MODELS if machine_role == "bob" else SAM_MODELS
    jobs: list[dict[str, Any]] = []
    lines = [
        "#!/usr/bin/env bash",
        "set -uo pipefail",
        f"cd {q(workspace_root)}",
        f"source asynchvla_ws/scripts/activate_simvla_{machine_role}.sh >/dev/null 2>&1 || true",
        "export PYTHONPATH=\"$HOME/.local/lib/python3.10/site-packages:$PWD/asynchvla_ws/src:${PYTHONPATH:-}\"",
        "mkdir -p asynchvla_ws/stage9_libero_pro_risk_data/logs/training",
        f"mkdir -p {q(campaign_dir / machine_role / 'logs')}",
        "run_job() {",
        "  local name=\"$1\"; shift",
        "  local log=\"$1\"; shift",
        "  echo \"[$(date -Is)] START ${name}\" | tee -a \"$log\"",
        "  \"$@\" >> \"$log\" 2>&1",
        "  local code=$?",
        "  if [ $code -ne 0 ]; then",
        "    echo \"[$(date -Is)] RETRY ${name} after code ${code}\" | tee -a \"$log\"",
        "    \"$@\" >> \"$log\" 2>&1",
        "    code=$?",
        "  fi",
        "  echo \"[$(date -Is)] END ${name} code=${code}\" | tee -a \"$log\"",
        "  return 0",
        "}",
    ]
    for target in TARGET_MODES:
        for model in models:
            job_name = f"{machine_role}_quick_{target}_{model}"
            out_dir = campaign_dir / machine_role / "quick" / target / model
            log = campaign_dir / machine_role / "logs" / f"{job_name}.log"
            cmd = train_command(split_dir, out_dir, model, target, source_remap, quick_epochs, quick_max_train_samples, batch_size)
            jobs.append({"name": job_name, "machine": machine_role, "model": model, "target_mode": target, "output_dir": str(out_dir), "log": str(log), "command": cmd})
            lines.append(f"run_job {q(job_name)} {q(log)} " + " ".join(q(x) for x in cmd))
    cal_log = campaign_dir / machine_role / "logs" / f"{machine_role}_calibration.log"
    lines.append(
        f"run_job {q(machine_role + '_calibration')} {q(cal_log)} "
        + " ".join(q(x) for x in ["python3", "-u", "-m", "training_stage9.stage9_calibration", "--campaign-dir", str(campaign_dir / machine_role)])
    )
    long_log = campaign_dir / machine_role / "logs" / f"{machine_role}_long_top.log"
    run_long = [
        "python3",
        "-u",
        "-m",
        "training_stage9.launch_stage9_training_jobs",
        "--mode",
        "run_long_top",
        "--workspace-root",
        str(workspace_root),
        "--campaign-dir",
        str(campaign_dir),
        "--split-dir",
        str(split_dir),
        "--machine-role",
        machine_role,
        "--batch-size",
        str(batch_size),
    ]
    for remap in source_remap:
        run_long.extend(["--source-remap", remap])
    lines.append(f"run_job {q(machine_role + '_run_long_top')} {q(long_log)} " + " ".join(q(x) for x in run_long))
    return "\n".join(lines) + "\n", jobs


def start_detached(script_path: Path, session_name: str) -> dict[str, Any]:
    if subprocess.run(["bash", "-lc", "command -v tmux >/dev/null"], check=False).returncode == 0:
        result = subprocess.run(["tmux", "new-session", "-d", "-s", session_name, "bash", str(script_path)], text=True, capture_output=True)
        return {"method": "tmux", "session": session_name, "returncode": result.returncode, "stderr": result.stderr.strip()}
    log_path = script_path.with_suffix(".nohup.log")
    with log_path.open("ab") as log:
        proc = subprocess.Popen(
            ["nohup", "bash", str(script_path)],
            stdout=log,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
        )
    return {"method": "nohup", "pid": proc.pid, "returncode": 0, "log": str(log_path), "stderr": ""}


def run_long_top(args: argparse.Namespace) -> dict[str, Any]:
    machine_dir = Path(args.campaign_dir) / args.machine_role
    candidates: list[tuple[float, Path, dict[str, Any]]] = []
    for metrics_path in machine_dir.rglob("quick/*/*/metrics.json"):
        try:
            metrics = json.loads(metrics_path.read_text())
            score = metrics.get("splits", {}).get("test_seen_task", {}).get("clean_binary", {}).get("auroc_bad")
            if score is None:
                score = -metrics.get("splits", {}).get("test_seen_task", {}).get("clean_binary", {}).get("brier", 1.0)
            config = json.loads((metrics_path.parent / "config.json").read_text())
            candidates.append((float(score), metrics_path.parent, config))
        except Exception:
            continue
    top = sorted(candidates, key=lambda item: item[0], reverse=True)[:3]
    launched: list[dict[str, Any]] = []
    for rank, (score, old_dir, config) in enumerate(top, 1):
        model = config["model"]
        target = config["target_mode"]
        out_dir = Path(args.campaign_dir) / args.machine_role / "long_top" / f"rank{rank}_{target}_{model}"
        cmd = train_command(Path(args.split_dir), out_dir, model, target, args.source_remap or [], args.long_epochs, None, args.batch_size, mc_dropout=12 if rank == 1 else 0)
        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path.home() / ".local/lib/python3.10/site-packages") + ":" + str(Path(args.workspace_root) / "asynchvla_ws/src") + ":" + env.get("PYTHONPATH", "")
        log = out_dir / "long_train.log"
        out_dir.mkdir(parents=True, exist_ok=True)
        with log.open("w") as f:
            code = subprocess.run(cmd, cwd=args.workspace_root, env=env, stdout=f, stderr=subprocess.STDOUT).returncode
        launched.append({"rank": rank, "score": score, "source_output": str(old_dir), "output_dir": str(out_dir), "command": cmd, "returncode": code})
    subprocess.run(
        ["python3", "-u", "-m", "training_stage9.stage9_calibration", "--campaign-dir", str(machine_dir)],
        cwd=args.workspace_root,
        env={**os.environ, "PYTHONPATH": str(Path.home() / ".local/lib/python3.10/site-packages") + ":" + str(Path(args.workspace_root) / "asynchvla_ws/src") + ":" + os.environ.get("PYTHONPATH", "")},
        check=False,
    )
    summary = {"long_top_jobs": launched}
    (machine_dir / "long_top_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True, default=str))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["make_group_safe_splits", "launch", "run_long_top"])
    parser.add_argument("--workspace-root", required=True)
    parser.add_argument("--source-split-dir")
    parser.add_argument("--split-dir")
    parser.add_argument("--campaign-dir")
    parser.add_argument("--campaign-id")
    parser.add_argument("--machine-role", choices=["bob", "sam"])
    parser.add_argument("--source-remap", action="append")
    parser.add_argument("--quick-epochs", type=int, default=8)
    parser.add_argument("--quick-max-train-samples", type=int, default=16000)
    parser.add_argument("--long-epochs", type=int, default=24)
    parser.add_argument("--batch-size", type=int, default=256)
    args = parser.parse_args()

    workspace = Path(args.workspace_root)
    if args.mode == "make_group_safe_splits":
        manifest = group_safe_split(Path(args.source_split_dir), Path(args.split_dir))
        print(json.dumps(manifest, indent=2, sort_keys=True))
        return
    if args.mode == "run_long_top":
        run_long_top(args)
        return

    if not args.machine_role:
        raise SystemExit("--machine-role is required for launch")
    campaign_id = args.campaign_id or ("stage9_full_training_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
    campaign_dir = Path(args.campaign_dir) if args.campaign_dir else workspace / "asynchvla_ws/stage9_libero_pro_risk_data/training" / campaign_id
    script_dir = workspace / "asynchvla_ws/stage9_libero_pro_risk_data/scripts/training"
    script_dir.mkdir(parents=True, exist_ok=True)
    queue, jobs = queue_script(
        workspace,
        campaign_dir,
        Path(args.split_dir),
        args.machine_role,
        args.source_remap or [],
        args.quick_epochs,
        args.quick_max_train_samples,
        args.batch_size,
    )
    script_path = script_dir / f"stage9_train_queue_{args.machine_role}_{campaign_id}.sh"
    script_path.write_text(queue)
    script_path.chmod(0o755)
    manifest = {
        "campaign_id": campaign_id,
        "campaign_dir": str(campaign_dir),
        "machine_role": args.machine_role,
        "split_dir": args.split_dir,
        "jobs": jobs,
        "queue_script": str(script_path),
        "target_modes": TARGET_MODES,
        "models": BOB_MODELS if args.machine_role == "bob" else SAM_MODELS,
    }
    manifest_path = campaign_dir / args.machine_role / "job_manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True, default=str) + "\n")
    launch = start_detached(script_path, f"stage9_train_{args.machine_role}_{campaign_id[-6:]}")
    manifest["launch"] = launch
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
