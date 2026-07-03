#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TASK_IDS = set(range(10))
EXPECTED_STATE_INDICES = set(list(range(10)) + list(range(40, 50)))
EXPECTED_RUNS = {
    'goal_object_t0to9': set(range(10)),
    'goal_object_t40to49': set(range(40, 50)),
}


def fail(message: str) -> None:
    raise SystemExit(f'VERIFICATION FAILED: {message}')


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def parse_bddl_language(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    m = re.search(r'\(:language\s*(.*?)\)', text, flags=re.S | re.I)
    if not m:
        fail(f'missing (:language ...) in {path}')
    return ' '.join(m.group(1).split()).lower()


def verify_sha256sums() -> None:
    sums = ROOT / 'SHA256SUMS'
    if not sums.is_file():
        fail('missing SHA256SUMS')
    seen = 0
    for line in sums.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        expected, rel = line.split('  ', 1)
        path = ROOT / rel
        if not path.is_file():
            fail(f'SHA256SUMS references missing file: {rel}')
        actual = sha256(path)
        if actual != expected:
            fail(f'sha256 mismatch for {rel}: expected {expected}, got {actual}')
        seen += 1
    if seen == 0:
        fail('SHA256SUMS is empty')


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f'missing CSV: {path.relative_to(ROOT)}')
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def count_init_states(path: Path) -> int:
    try:
        import torch
    except Exception as exc:
        fail(f'torch is required to count .pruned_init states but could not be imported: {exc!r}')
    try:
        return len(torch.load(path, weights_only=False))
    except TypeError:
        return len(torch.load(path))


def main() -> None:
    verify_sha256sums()

    manifest = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        rel = item['destination_relative_path']
        path = ROOT / rel
        if not path.is_file():
            fail(f'MANIFEST references missing file: {rel}')
        if sha256(path) != item['sha256']:
            fail(f'MANIFEST sha256 mismatch: {rel}')

    source_json = json.loads((ROOT / 'source_manifests/libero_goal_object_exact_trials0to9_40to49_eval_seed0_20260605.json').read_text(encoding='utf-8'))
    source_csv = load_csv(ROOT / 'source_manifests/libero_goal_object_exact_trials0to9_40to49_eval_seed0_20260605.csv')
    identity_rows = load_csv(ROOT / 'verification/episode_identity_table.csv')
    inventory = json.loads((ROOT / 'verification/task_inventory.json').read_text(encoding='utf-8'))['tasks']
    inventory_by_task = {int(row['task_id']): row for row in inventory}

    if len(identity_rows) != 200:
        fail(f'episode_identity_table must have 200 rows, got {len(identity_rows)}')
    if len(source_csv) != 200:
        fail(f'source CSV must have 200 rows, got {len(source_csv)}')
    if set(inventory_by_task) != EXPECTED_TASK_IDS:
        fail(f'task inventory ids mismatch: {sorted(inventory_by_task)}')

    identities = set()
    states_by_task = defaultdict(set)
    states_by_run_task = defaultdict(set)
    descriptions_by_task = defaultdict(set)
    for row in identity_rows:
        task_id = int(row['task_id'])
        state_idx = int(row['initial_state_index'])
        eval_seed = int(row['eval_seed'])
        trial_index = int(row['trial_index'])
        episode_seed = int(row['episode_seed'])
        run_id = row['run_id']
        if task_id not in EXPECTED_TASK_IDS:
            fail(f'unexpected task_id={task_id}')
        if state_idx not in EXPECTED_STATE_INDICES:
            fail(f'unexpected initial_state_index={state_idx}')
        if trial_index != state_idx:
            fail(f'trial_index does not equal initial_state_index in {row}')
        if episode_seed != state_idx:
            fail(f'episode_seed does not equal initial_state_index in {row}')
        if eval_seed != 0:
            fail(f'eval_seed is not 0 in {row}')
        if run_id not in EXPECTED_RUNS:
            fail(f'unexpected run_id={run_id}')
        if state_idx not in EXPECTED_RUNS[run_id]:
            fail(f'run {run_id} contains state {state_idx}, expected {sorted(EXPECTED_RUNS[run_id])}')
        identity = (row['task_suite_name'], task_id, state_idx, eval_seed)
        if identity in identities:
            fail(f'duplicate episode identity: {identity}')
        identities.add(identity)
        states_by_task[task_id].add(state_idx)
        states_by_run_task[(run_id, task_id)].add(state_idx)
        descriptions_by_task[task_id].add(row['task_description'].lower())

        bddl_path = ROOT / row['bddl_relative_path']
        init_path = ROOT / row['init_state_file_relative_path']
        if not bddl_path.is_file():
            fail(f'missing BDDL file referenced by episode row: {row["bddl_relative_path"]}')
        if not init_path.is_file():
            fail(f'missing init file referenced by episode row: {row["init_state_file_relative_path"]}')
        if sha256(bddl_path) != row['bddl_sha256']:
            fail(f'BDDL hash mismatch for {row["bddl_relative_path"]}')
        if sha256(init_path) != row['init_state_file_sha256']:
            fail(f'init hash mismatch for {row["init_state_file_relative_path"]}')

    if len(identities) != 200:
        fail(f'expected 200 unique identities, got {len(identities)}')
    for task_id in EXPECTED_TASK_IDS:
        if states_by_task[task_id] != EXPECTED_STATE_INDICES:
            fail(f'task {task_id} does not have exact state set 0-9 and 40-49')
        for run_id, expected_states in EXPECTED_RUNS.items():
            if states_by_run_task[(run_id, task_id)] != expected_states:
                fail(f'{run_id}/task {task_id} state set mismatch')

    # Verify task assets, BDDL language prompt, and init-state counts.
    for task_id, inv in inventory_by_task.items():
        bddl_path = ROOT / inv['bddl_relative_path']
        init_path = ROOT / inv['init_state_file_relative_path']
        if not bddl_path.is_file() or not init_path.is_file():
            fail(f'missing asset for task {task_id}')
        if sha256(bddl_path) != inv['bddl_sha256']:
            fail(f'task_inventory BDDL hash mismatch for task {task_id}')
        if sha256(init_path) != inv['init_state_file_sha256']:
            fail(f'task_inventory init hash mismatch for task {task_id}')
        actual_language = parse_bddl_language(bddl_path)
        if actual_language != inv['bddl_language']:
            fail(f'BDDL language mismatch in inventory for task {task_id}')
        if descriptions_by_task[task_id] != {actual_language}:
            fail(f'manifest description does not match BDDL language for task {task_id}: {descriptions_by_task[task_id]} vs {actual_language}')
        n_states = count_init_states(init_path)
        if n_states < 50:
            fail(f'init file for task {task_id} has only {n_states} states')
        if n_states != int(inv['number_of_initialization_states']):
            fail(f'init count mismatch for task {task_id}: file={n_states}, inventory={inv["number_of_initialization_states"]}')

    # Verify source JSON episode list agrees with identity table.
    source_eps = [ep for run in source_json['runs'] for ep in run['episodes']]
    if len(source_eps) != 200:
        fail(f'source JSON has {len(source_eps)} episodes')
    source_keys = {(ep['run_id'], int(ep['task_id']), int(ep['initial_state_index']), int(ep['eval_seed'])) for ep in source_eps}
    table_keys = {(row['run_id'], int(row['task_id']), int(row['initial_state_index']), int(row['eval_seed'])) for row in identity_rows}
    if source_keys != table_keys:
        fail('source JSON identities do not match episode_identity_table')

    print('VERIFIER_PASS: exact episode identity bundle is internally consistent')
    print(json.dumps({
        'episode_count': len(identity_rows),
        'task_ids': sorted(EXPECTED_TASK_IDS),
        'initial_state_indices': sorted(EXPECTED_STATE_INDICES),
        'eval_seed': 0,
        'bddl_file_count': len(list((ROOT / 'libero_pro/bddl_files/libero_goal_object').glob('*.bddl'))),
        'init_file_count': len(list((ROOT / 'libero_pro/init_files/libero_goal_object').glob('*.pruned_init'))),
    }, sort_keys=True))


if __name__ == '__main__':
    main()
