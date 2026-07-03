import os
import signal
import subprocess
import time

repo = "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test"
home = os.path.expanduser("~")
keywords = [
    repo,
    home + "/IsaacLab",
    home + "/isaacsim",
    "isaacsim",
    "isaaclab.sh",
    "SimulationApp",
    "omni.kit",
    "kit",
    "carb",
    "run_scene.py",
    "debug_scene.py",
    "collect.py",
]

user = os.environ.get("USER", "")
out = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")

targets = []
for line in out.splitlines():
    line = line.strip()
    if not line:
        continue
    pid_s, _, args = line.partition(" ")
    if not pid_s.isdigit():
        continue
    pid = int(pid_s)
    if pid == os.getpid() or pid == os.getppid():
        continue
    if any(k in args for k in keywords):
        targets.append((pid, args))

print("Selected stale Isaac/Kit processes:")
for pid, args in targets:
    print(pid, args[:300])

for pid, _ in targets:
    try:
        os.kill(pid, signal.SIGTERM)
        print("SIGTERM", pid)
    except ProcessLookupError:
        pass
    except Exception as e:
        print("SIGTERM failed", pid, repr(e))

time.sleep(8)

for pid, _ in targets:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        continue
    try:
        os.kill(pid, signal.SIGKILL)
        print("SIGKILL", pid)
    except Exception as e:
        print("SIGKILL failed", pid, repr(e))
