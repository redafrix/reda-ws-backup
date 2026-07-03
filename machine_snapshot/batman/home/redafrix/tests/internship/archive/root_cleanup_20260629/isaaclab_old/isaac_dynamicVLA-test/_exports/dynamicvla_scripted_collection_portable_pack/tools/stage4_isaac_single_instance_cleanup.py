import os, signal, subprocess, time

ROOT = "/home/redafrix/tests/internship/isaac_dynamicVLA-test"
keywords = [
    ROOT,
    "/home/redafrix/isaacsim",
    "SimulationApp",
    "isaacsim",
    "isaaclab.sh",
    "kit",
    "omni",
    "carb",
    "simulate.py",
    "translate_dataset_seq.py",
    "replay_dataset_seq.py",
    "evaluate.py",
]

# Get all ancestor PIDs of the current process to avoid killing our parent shell or scheduler processes.
ancestors = set()
curr = os.getpid()
while curr > 0:
    ancestors.add(curr)
    try:
        with open(f"/proc/{curr}/stat", "r") as f:
            parts = f.read().split()
            # The 4th item in /proc/<pid>/stat is the parent PID (PPID)
            curr = int(parts[3])
    except Exception:
        break

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
    if pid in ancestors:
        continue
    if any(k in args for k in keywords):
        targets.append((pid, args))

print("Processes selected for cleanup:")
for pid, args in targets:
    print(pid, args[:400])

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
        # Only print if it's not our ancestor to avoid clutter
        pid_s, _, _ = line.partition(" ")
        if pid_s.isdigit() and int(pid_s) not in ancestors:
            print(line)
