import json
import subprocess
import shlex
from pathlib import Path

NEW_ROOT = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2d_commit_gate_20260610")
SMOKE_TASKS = [0, 17]
MODELS = ["topk8_v2d_commit_gate"]

def run():
    for task_id in SMOKE_TASKS:
        for label in MODELS:
            config_path = NEW_ROOT / f"configs/task{task_id}_{label}.json"
            cfg = json.loads(config_path.read_text())
            
            cfg["reset_seeds"] = [0]
            cfg["output_dir"] = str(NEW_ROOT / f"runs_smoke/task{task_id}/{label}")
            
            smoke_config_path = NEW_ROOT / f"configs/smoke_task{task_id}_{label}.json"
            smoke_config_path.write_text(json.dumps(cfg, indent=2))
            
            policy = "topk8_v2d_commit_gate"
            
            activate_script = "/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh"
            runner_script = str(NEW_ROOT / "src/run_policy_matrix_adaptive_horizon_v2d.py")
            
            inner_script = (
                f"source {shlex.quote(activate_script)} >/dev/null; "
                f"export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8; "
                f"python3 {shlex.quote(runner_script)} --config {shlex.quote(str(smoke_config_path))} --policy {shlex.quote(policy)} --smoke"
            )
            
            print(f"--- SMOKE TEST: Task {task_id} Label {label} ---", flush=True)
            res = subprocess.run(["bash", "-lc", inner_script], capture_output=True, text=True)
            log_path = NEW_ROOT / f"smoke_logs_task{task_id}_{label}.txt"
            log_path.write_text(res.stdout + "\n" + res.stderr)
            if res.returncode != 0:
                print(f"FAILED (code {res.returncode})! Check {log_path}", flush=True)
                print(res.stderr, flush=True)
            else:
                print("PASSED", flush=True)

if __name__ == "__main__":
    run()
