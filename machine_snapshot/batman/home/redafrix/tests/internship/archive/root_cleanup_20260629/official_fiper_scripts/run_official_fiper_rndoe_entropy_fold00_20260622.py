import glob
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd, cwd=None, env=None, log_path=None):
    print(f"\nRunning command: {' '.join(cmd)}", flush=True)
    proc = subprocess.Popen(
        cmd,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    lines = []
    with open(log_path, "w") if log_path else open(os.devnull, "w") as log:
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="", flush=True)
            log.write(line)
            lines.append(line)
    rc = proc.wait()
    if rc != 0:
        raise subprocess.CalledProcessError(rc, cmd, output="".join(lines))
    return "".join(lines)


def clean_dir(path):
    path = Path(path)
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def link_processed_rollouts(src_task_dir, dst_task_dir):
    src = Path(src_task_dir) / "processed_rollouts"
    dst_task_dir = Path(dst_task_dir)
    dst = dst_task_dir / "processed_rollouts"
    if not (src / "obs_embeddings.pt").exists():
        raise FileNotFoundError(src / "obs_embeddings.pt")
    if dst.exists() or dst.is_symlink():
        if dst.is_symlink():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    dst_task_dir.mkdir(parents=True, exist_ok=True)
    dst.symlink_to(src, target_is_directory=True)
    print(f"Linked {dst} -> {src}", flush=True)


def copy_results(src_dir, dst_dir):
    dst_dir = Path(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    for path in glob.glob(str(Path(src_dir) / "*")):
        p = Path(path)
        target = dst_dir / p.name
        if p.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(p, target)
        else:
            shutil.copy2(p, target)
        copied += 1
    print(f"Copied {copied} result entries to {dst_dir}", flush=True)


def main():
    base_dir = Path("/home/dean/fiper_uncertainty_collection")
    fiper_dir = base_dir / "external" / "fiper"
    python_bin = "/home/redafrix/miniconda3/envs/simvla/bin/python"
    out_root = base_dir / "experiments" / "official_fiper_rndoe_entropy_fold00_20260622"
    data_src = out_root / "official_fiper_data"
    report_dir = out_root / "reports"
    log_dir = out_root / "logs"
    report_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    fiper_data_dir = fiper_dir / "data"
    fiper_results_dir = fiper_data_dir / "results"
    clean_dir(fiper_results_dir)

    link_processed_rollouts(data_src / "libero_fold00", fiper_data_dir / "libero_fold00")
    link_processed_rollouts(data_src / "libero_fold00_hygiene", fiper_data_dir / "libero_fold00_hygiene")

    option_a_out = out_root / "option_a_results"
    option_b_out = out_root / "option_b_results"
    # Skip clearing option_a_results since it's already complete!
    # clean_dir(option_a_out)
    clean_dir(option_b_out)

    env = os.environ.copy()
    env["PYOPENGL_PLATFORM"] = "egl"
    env["MUJOCO_GL"] = "egl"

    print("Option A results are already fully saved. Skipping Option A run.", flush=True)

    # Option B training checkpoints are already fully saved!
    print("Option B training checkpoints are already fully saved. Skipping Option B training.", flush=True)

    src_rnd_dir = fiper_data_dir / "libero_fold00_hygiene" / "rnd_models" / "rnd_oe"
    dst_rnd_dir = fiper_data_dir / "libero_fold00" / "rnd_models" / "rnd_oe"
    if not src_rnd_dir.exists():
        raise FileNotFoundError(src_rnd_dir)
    if dst_rnd_dir.exists():
        shutil.rmtree(dst_rnd_dir)
    dst_rnd_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src_rnd_dir, dst_rnd_dir)
    print(f"Copied hygiene-trained RND from {src_rnd_dir} to {dst_rnd_dir}", flush=True)

    clean_dir(fiper_results_dir)
    cmd_b_eval = [
        python_bin,
        str(fiper_dir / "scripts" / "run_fiper.py"),
        "tasks=['libero_fold00']",
        "rnd_models=['rnd_oe']",
        "methods=['entropy']",
        "train_rnd=False",
    ]
    run_cmd(cmd_b_eval, cwd=str(fiper_dir), env=env, log_path=log_dir / "option_b_eval_with_hygiene_rnd.log")
    copy_results(fiper_results_dir, option_b_out)
    clean_dir(fiper_results_dir)

    print("ALL_EVALUATIONS_COMPLETED", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
