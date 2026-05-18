#!/usr/bin/env python3
from __future__ import annotations
import json, random
from collections import Counter, defaultdict
from pathlib import Path

REDA_WS=Path('/media/rootalkhatib/My Passport/reda_ws')
INV=REDA_WS/'asynchvla_ws/data/libero_inventory.json'
OUTDIR=REDA_WS/'asynchvla_ws/data/splits'
REPORT=REDA_WS/'asynchvla_ws/outputs/reports/split_manifest_report.md'

def split_list(files, ratios=(.7,.15,.15), seed=13):
    fs=list(files); random.Random(seed).shuffle(fs)
    n=len(fs); ntr=max(1,int(n*ratios[0])); ncal=max(1,int(n*ratios[1]));
    return fs[:ntr], fs[ntr:ntr+ncal], fs[ntr+ncal:]

def write_manifest(name, typ, train, calib, test_id=None, test_ood=None, **kw):
    m={'split_name':name,'split_type':typ,'train_files':train,'calib_files':calib,'test_id_files':test_id or [],'test_ood_files':test_ood or [], **kw}
    m['counts']={k:len(m[k]) for k in ['train_files','calib_files','test_id_files','test_ood_files']}
    p=OUTDIR/f'{name}.json'; p.write_text(json.dumps(m,indent=2)); return p,m

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    rows=json.loads(INV.read_text())['files']; usable=[r for r in rows if r['loadable_hdf5'] and r['loadable_simvla_loader']]
    paths=[r['path'] for r in usable]
    manifests=[]
    tr,cal,te=split_list(paths, seed=1); manifests.append(write_manifest('id_task_split','ID_TASK_SPLIT',tr,cal,test_id=te,reason='Random task/file split; split unit is HDF5 file.'))
    suites=defaultdict(list)
    for r in usable: suites[r['suite']].append(r['path'])
    for suite, held in sorted(suites.items()):
        if len(held)<2: continue
        non=[r['path'] for r in usable if r['suite']!=suite]
        tr,cal,tid=split_list(non, ratios=(.7,.15,.15), seed=2)
        manifests.append(write_manifest(f'holdout_{suite}','OOD_SUITE_LEAVE_ONE_OUT',tr,cal,test_id=tid,test_ood=held,heldout_suite=suite,reason=f'Train/calib/test_id exclude suite {suite}; test_ood is heldout suite.'))
    obj_counts=Counter()
    for r in usable:
        for o in r['object_words']: obj_counts[o]+=1
    selected=[o for o,c in obj_counts.most_common() if 5 <= c <= len(usable)-5][:6]
    for obj in selected:
        held=[r['path'] for r in usable if obj in r['object_words']]
        non=[r['path'] for r in usable if obj not in r['object_words']]
        tr,cal,tid=split_list(non, ratios=(.7,.15,.15), seed=3)
        manifests.append(write_manifest(f'holdout_object_{obj}','OOD_OBJECT_HELDOUT',tr,cal,test_id=tid,test_ood=held,excluded_object=obj,reason=f'Train/calib/test_id exclude object token {obj}; test_ood contains token.'))
    scenes=defaultdict(list)
    for r in usable:
        if r['scene_id']: scenes[r['scene_id']].append(r['path'])
    for sc,held in sorted(scenes.items()):
        if len(held)<3: continue
        non=[r['path'] for r in usable if r['scene_id']!=sc]
        tr,cal,tid=split_list(non, ratios=(.7,.15,.15), seed=4)
        manifests.append(write_manifest(f'holdout_scene_{sc.lower()}','OOD_SCENE_HELDOUT',tr,cal,test_id=tid,test_ood=held,heldout_scene=sc,reason=f'Train/calib/test_id exclude scene {sc}; test_ood is scene.'))
    # Pilot choices: ID, prefer object suite, then spatial; object top count.
    suite_choice='libero_object' if 'libero_object' in suites else ('libero_spatial' if 'libero_spatial' in suites else sorted(suites)[0])
    obj_choice=selected[0] if selected else None
    pilot={'id':'id_task_split','suite':f'holdout_{suite_choice}','object':f'holdout_object_{obj_choice}' if obj_choice else None}
    lines=['# Split Manifest Report','',f'- Inventory: `{INV}`',f'- Manifest dir: `{OUTDIR}`',f'- Usable files: `{len(usable)}`',f'- Manifests created: `{len(manifests)}`',f'- Pilot selection: `{pilot}`','','## Manifest Counts','','| Split | Type | Train | Calib | Test ID | Test OOD | Heldout |','|---|---|---:|---:|---:|---:|---|']
    for p,m in manifests:
        held=m.get('heldout_suite') or m.get('excluded_object') or m.get('heldout_scene') or ''
        c=m['counts']; lines.append(f'| `{m["split_name"]}` | `{m["split_type"]}` | {c["train_files"]} | {c["calib_files"]} | {c["test_id_files"]} | {c["test_ood_files"]} | `{held}` |')
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines)+'\n')
    (OUTDIR/'pilot_selection.json').write_text(json.dumps(pilot,indent=2))
    print('manifests_ok', len(manifests), 'pilot', pilot, 'report', REPORT)
if __name__=='__main__': main()
