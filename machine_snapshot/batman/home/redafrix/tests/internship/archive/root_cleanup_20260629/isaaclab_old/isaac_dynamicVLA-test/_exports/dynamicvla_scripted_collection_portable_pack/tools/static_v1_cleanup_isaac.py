import os, signal, subprocess, time

ROOT = "/home/redafrix/tests/internship/isaac_dynamicVLA-test"
DEV = ROOT + "/_dev/data_collection_mods"

keywords = [
    ROOT + "/isaacsim",
    ROOT + "/IsaacLab",
    DEV,
    "SimulationApp",
    "isaacsim",
    "isaaclab.sh",
    "kit",
    "omni",
    "carb",
    "simulate.py",
    "translate_dataset_seq.py",
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
    if pid == os.getpid():
        continue
    if any(k in args for k in keywords):
        targets.append((pid, args))

print("Processes selected for cleanup:")
for pid, args in targets:
    print(pid, args[:300])

for pid, args in targets:
    try:
        os.kill(pid, signal.SIGTERM)
        print("SIGTERM", pid)
    except ProcessLookupError:
        pass
    except Exception as e:
        print("SIGTERM failed", pid, repr(e))

time.sleep(10)

for pid, args in targets:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        continue
    try:
        os.kill(pid, signal.SIGKILL)
        print("SIGKILL", pid)
    except Exception as e:
        print("SIGKILL failed", pid, repr(e))

print("After cleanup:")
out2 = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")
for line in out2.splitlines():
    if any(k in line for k in keywords):
        print(line)
