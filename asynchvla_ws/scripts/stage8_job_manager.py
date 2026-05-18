#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, shlex, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

BOB_ROOT = Path('/media/rootalkhatib/My Passport/reda_ws')
SAM_ROOT = Path('/home/rootalkhatib/test/reda_ws')
REL_ROOT = Path('asynchvla_ws/stage8_ultimate')
LOCAL_REPORT_DIR = Path('/home/redafrix/tests/internship/codex_reports/stage8')
STATUSES = {'PENDING', 'RUNNING', 'DONE', 'FAILED', 'SKIPPED'}


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')


def root_for(machine: str) -> Path:
    return BOB_ROOT if machine == 'bob' else SAM_ROOT


def remote_prefix(machine: str) -> List[str]:
    if machine == 'bob':
        return []
    sam_ssh = os.environ.get('STAGE8_SAM_SSH', 'ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new sam')
    return shlex.split(sam_ssh)


def run_cmd(cmd: List[str], timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)


def remote_run(machine: str, command: str, timeout: int | None = None) -> subprocess.CompletedProcess:
    if machine == 'bob':
        return run_cmd(['bash', '-lc', command], timeout=timeout)
    return run_cmd(remote_prefix(machine) + [command], timeout=timeout)


def ensure_dirs(machine: str) -> None:
    root = root_for(machine)
    cmd = f'mkdir -p {shlex.quote(str(root / REL_ROOT / "jobs"))} {shlex.quote(str(root / REL_ROOT / "logs"))} {shlex.quote(str(root / REL_ROOT / "status"))} {shlex.quote(str(root / REL_ROOT / "reports"))} {shlex.quote(str(root / REL_ROOT / "results"))} {shlex.quote(str(root / REL_ROOT / "configs"))}'
    cp = remote_run(machine, cmd, timeout=20)
    if cp.returncode != 0:
        raise RuntimeError(cp.stdout)


def read_manifest(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text())


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')


def status_path(job: Dict[str, Any]) -> Path:
    return Path(job['status_path'])


def load_status(machine: str, job: Dict[str, Any]) -> Dict[str, Any] | None:
    p = status_path(job)
    cp = remote_run(machine, f'test -f {shlex.quote(str(p))} && cat {shlex.quote(str(p))} || true', timeout=20)
    if cp.returncode != 0 or not cp.stdout.strip():
        return None
    try:
        return json.loads(cp.stdout)
    except Exception:
        return {'job_id': job['job_id'], 'state': 'FAILED', 'error': 'corrupt status json', 'raw': cp.stdout[-2000:]}


def write_remote_status(machine: str, job: Dict[str, Any], state: str, **extra: Any) -> None:
    assert state in STATUSES
    p = status_path(job)
    data = {'job_id': job['job_id'], 'machine': machine, 'state': state, 'updated_at': now(), **extra}
    payload = json.dumps(data, indent=2, sort_keys=True)
    cp = remote_run(machine, f'mkdir -p {shlex.quote(str(p.parent))} && cat > {shlex.quote(str(p))} <<\'JSON\'\n{payload}\nJSON', timeout=20)
    if cp.returncode != 0:
        raise RuntimeError(cp.stdout)


def gpu_busy(machine: str) -> bool:
    cp = remote_run(machine, "nvidia-smi --query-compute-apps=pid,process_name,used_memory --format=csv,noheader,nounits 2>/dev/null | awk 'NF {print}'", timeout=10)
    if cp.returncode != 0:
        return False
    for line in [l.strip() for l in cp.stdout.splitlines() if l.strip()]:
        # NVIDIA can leave a stale "[Not Found]" compute-app entry even when
        # the process table and normal nvidia-smi process list are clear.
        if '[Not Found]' in line:
            continue
        return True
    return False


def machine_has_running_gpu_job(manifest: Dict[str, Any], machine: str) -> bool:
    for job in manifest['jobs']:
        if job.get('machine') != machine or not job.get('gpu_required'):
            continue
        st = load_status(machine, job)
        if st and st.get('state') == 'RUNNING':
            return True
    return False


def deps_done(manifest: Dict[str, Any], job: Dict[str, Any]) -> bool:
    dep_ids = job.get('dependencies') or []
    by_id = {j['job_id']: j for j in manifest['jobs']}
    for dep in dep_ids:
        dj = by_id[dep]
        st = load_status(dj['machine'], dj)
        if not st or st.get('state') != 'DONE':
            return False
    return True


def launch_job(manifest: Dict[str, Any], job: Dict[str, Any], dry_run: bool = False) -> str:
    machine = job['machine']
    ensure_dirs(machine)
    st = load_status(machine, job)
    if st and st.get('state') == 'DONE':
        return f"{job['job_id']}: already DONE"
    attempts = int(st.get('attempt', 0)) if st else 0
    if st and st.get('state') == 'RUNNING':
        return f"{job['job_id']}: already RUNNING"
    if attempts > int(job.get('max_retries', 0)):
        write_remote_status(machine, job, 'FAILED', attempt=attempts, error='retry limit reached')
        return f"{job['job_id']}: retry limit reached"
    if not deps_done(manifest, job):
        return f"{job['job_id']}: waiting for dependencies"
    if job.get('gpu_required') and (gpu_busy(machine) or machine_has_running_gpu_job(manifest, machine)):
        return f"{job['job_id']}: GPU busy on {machine}"

    attempt = attempts + 1
    cmd_path = Path(job['command_file'])
    log_path = Path(job['log_path'])
    done_marker = Path(str(status_path(job)) + '.done_marker')
    fail_marker = Path(str(status_path(job)) + '.fail_marker')
    command = job['command']
    wrapper = f"""#!/usr/bin/env bash
set -uo pipefail
mkdir -p {shlex.quote(str(log_path.parent))} {shlex.quote(str(status_path(job).parent))} {shlex.quote(str(done_marker.parent))}
echo '[stage8] job {job['job_id']} attempt {attempt} start '$(date -Is)
bash -lc {shlex.quote(command)}
rc=$?
echo '[stage8] job {job['job_id']} exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch {shlex.quote(str(done_marker))}; else echo $rc > {shlex.quote(str(fail_marker))}; fi
exit $rc
"""
    if dry_run:
        return f"{job['job_id']}: dry-run launch {machine}"
    write_remote_status(machine, job, 'RUNNING', attempt=attempt, pid=None, log_path=str(log_path), command_file=str(cmd_path))
    script_payload = wrapper
    remote_run(machine, f"mkdir -p {shlex.quote(str(cmd_path.parent))} && cat > {shlex.quote(str(cmd_path))} <<'JOB'\n{script_payload}\nJOB\nchmod +x {shlex.quote(str(cmd_path))}", timeout=20)
    launch = f"nohup {shlex.quote(str(cmd_path))} > {shlex.quote(str(log_path))} 2>&1 & echo $!"
    cp = remote_run(machine, launch, timeout=20)
    if cp.returncode != 0:
        write_remote_status(machine, job, 'FAILED', attempt=attempt, error=cp.stdout[-2000:])
        return f"{job['job_id']}: launch failed"
    pid = cp.stdout.strip().splitlines()[-1] if cp.stdout.strip() else None
    write_remote_status(machine, job, 'RUNNING', attempt=attempt, pid=pid, log_path=str(log_path), command_file=str(cmd_path), started_at=now())
    return f"{job['job_id']}: launched pid={pid} on {machine}"


def refresh_job(job: Dict[str, Any]) -> Dict[str, Any]:
    machine = job['machine']
    st = load_status(machine, job) or {'job_id': job['job_id'], 'machine': machine, 'state': 'PENDING'}
    if st.get('state') != 'RUNNING':
        return st
    done_marker = Path(str(status_path(job)) + '.done_marker')
    fail_marker = Path(str(status_path(job)) + '.fail_marker')
    cp = remote_run(machine, f'if [ -f {shlex.quote(str(done_marker))} ]; then echo DONE; elif [ -f {shlex.quote(str(fail_marker))} ]; then echo FAILED:$(cat {shlex.quote(str(fail_marker))}); else echo RUNNING; fi', timeout=20)
    val = cp.stdout.strip()
    if val == 'DONE':
        missing = []
        for out in job.get('expected_outputs') or []:
            ocp = remote_run(machine, f'test -e {shlex.quote(out)}', timeout=10)
            if ocp.returncode != 0:
                missing.append(out)
        state = 'FAILED' if missing else 'DONE'
        write_remote_status(machine, job, state, attempt=st.get('attempt', 1), pid=st.get('pid'), completed_at=now(), missing_outputs=missing)
        return load_status(machine, job) or st
    if val.startswith('FAILED'):
        write_remote_status(machine, job, 'FAILED', attempt=st.get('attempt', 1), pid=st.get('pid'), completed_at=now(), error=val)
        return load_status(machine, job) or st
    pid = st.get('pid')
    if pid:
        alive = remote_run(machine, f'kill -0 {shlex.quote(str(pid))} 2>/dev/null', timeout=10)
        if alive.returncode != 0:
            write_remote_status(machine, job, 'FAILED', attempt=st.get('attempt', 1), pid=pid, completed_at=now(), error='process exited without marker')
            return load_status(machine, job) or st
    return st


def status(manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    for job in sorted(manifest['jobs'], key=lambda j: (j.get('priority', 999), j['job_id'])):
        rows.append(refresh_job(job))
    return rows


def launch_ready(manifest: Dict[str, Any], limit: int = 999, dry_run: bool = False) -> List[str]:
    msgs = []
    count = 0
    for job in sorted(manifest['jobs'], key=lambda j: (j.get('priority', 999), j['job_id'])):
        st = refresh_job(job)
        if st.get('state') == 'FAILED':
            attempts = int(st.get('attempt', 0))
            if attempts <= int(job.get('max_retries', 0)):
                msg = launch_job(manifest, job, dry_run=dry_run)
            else:
                msg = f"{job['job_id']}: FAILED retry limit"
        elif st.get('state') in ('PENDING', 'SKIPPED') or st.get('state') is None:
            msg = launch_job(manifest, job, dry_run=dry_run)
        else:
            msg = f"{job['job_id']}: {st.get('state')}"
        msgs.append(msg)
        if 'launched' in msg:
            count += 1
            if count >= limit:
                break
    return msgs


def default_manifest(root: Path) -> Dict[str, Any]:
    base_b = BOB_ROOT / REL_ROOT
    base_s = SAM_ROOT / REL_ROOT
    def job(job_id, machine, priority, command, gpu=False, deps=None, retries=1, expected=None, hours=1.0, smoke=None):
        base = base_b if machine == 'bob' else base_s
        return {
            'job_id': job_id,
            'machine': machine,
            'priority': priority,
            'command': command,
            'command_file': str(base / 'jobs' / f'{job_id}.sh'),
            'expected_outputs': expected or [],
            'log_path': str(base / 'logs' / f'{job_id}.log'),
            'status_path': str(base / 'status' / f'{job_id}.json'),
            'max_retries': retries,
            'dependencies': deps or [],
            'smoke_command': smoke,
            'timeout_hours': hours,
            'gpu_required': gpu,
        }
    return {
        'schema_version': 'stage8_manifest_v1',
        'created_at': now(),
        'jobs': [
            job('smoke_bob_cpu', 'bob', 1, 'cd "/media/rootalkhatib/My Passport/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/results && echo bob_ok > asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt', expected=[str(base_b/'results/smoke_bob_cpu.txt')]),
            job('smoke_sam_cpu', 'sam', 1, 'cd /home/rootalkhatib/test/reda_ws && mkdir -p asynchvla_ws/stage8_ultimate/results && echo sam_ok > asynchvla_ws/stage8_ultimate/results/smoke_sam_cpu.txt', expected=[str(base_s/'results/smoke_sam_cpu.txt')]),
            job('smoke_dependency_child', 'bob', 2, 'cd "/media/rootalkhatib/My Passport/reda_ws" && cat asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt > asynchvla_ws/stage8_ultimate/results/smoke_dependency_child.txt', deps=['smoke_bob_cpu'], expected=[str(base_b/'results/smoke_dependency_child.txt')]),
            job('smoke_retry_failure', 'bob', 2, 'cd "/media/rootalkhatib/My Passport/reda_ws"; f=asynchvla_ws/stage8_ultimate/results/smoke_retry_counter.txt; n=0; [ -f "$f" ] && n=$(cat "$f"); n=$((n+1)); echo $n > "$f"; if [ "$n" -lt 2 ]; then echo intentional_fail; exit 7; fi; echo retry_ok > asynchvla_ws/stage8_ultimate/results/smoke_retry_success.txt', retries=2, expected=[str(base_b/'results/smoke_retry_success.txt')]),
        ]
    }


def collect_reports() -> str:
    LOCAL_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    cp = remote_run('bob', f'find {shlex.quote(str(BOB_ROOT / REL_ROOT / "reports"))} -maxdepth 1 -type f \\( -name "*.md" -o -name "*.json" \\) -print', timeout=20)
    copied = []
    for line in cp.stdout.splitlines():
        p = line.strip()
        if not p:
            continue
        out = LOCAL_REPORT_DIR / Path(p).name
        data = remote_run('bob', f'cat {shlex.quote(p)}', timeout=20)
        if data.returncode == 0:
            out.write_text(data.stdout)
            copied.append(str(out))
    return '\n'.join(copied)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default=str(BOB_ROOT / REL_ROOT / 'configs/stage8_job_manifest.json'))
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('init')
    sub.add_parser('status')
    p_launch = sub.add_parser('launch-ready'); p_launch.add_argument('--limit', type=int, default=999); p_launch.add_argument('--dry-run', action='store_true')
    sub.add_parser('collect-reports')
    args = ap.parse_args()
    manifest_path = Path(args.manifest)
    if args.cmd == 'init':
        man = default_manifest(BOB_ROOT)
        write_json(manifest_path, man)
        print(manifest_path)
        return
    man = read_manifest(manifest_path)
    if args.cmd == 'status':
        rows = status(man)
        print(json.dumps(rows, indent=2, sort_keys=True))
    elif args.cmd == 'launch-ready':
        print('\n'.join(launch_ready(man, limit=args.limit, dry_run=args.dry_run)))
    elif args.cmd == 'collect-reports':
        print(collect_reports())

if __name__ == '__main__':
    main()
