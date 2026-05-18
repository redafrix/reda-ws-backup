#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path
import h5py

REDA_WS=Path('/media/rootalkhatib/My Passport/reda_ws')
ROOT=REDA_WS/'intern_ship_ws/assets/data/libero_datasets'
SIM=REDA_WS/'intern_ship_ws/simvla/code/SimVLA_modified'
OUT=REDA_WS/'asynchvla_ws/data/libero_inventory.json'
REPORT=REDA_WS/'asynchvla_ws/outputs/reports/libero_inventory_report.md'
sys.path.insert(0,str(SIM))
STOP=set('the a an and or to of in on at from into with for by it them this that demo hdf5 pick up put place turn open close move left right top bottom middle front back next near object scene kitchen living room study wooden black white red blue green yellow'.split())
KEEP={'bowl','plate','mug','drawer','stove','pudding','cabinet','book','box','basket','microwave','oven','sink','table','counter','pot','pan','tray','cup','door','shelf','cream','tomato','butter'}

def task_name(p:Path):
    s=p.stem
    if s.endswith('_demo'): s=s[:-5]
    m=re.search(r'(KITCHEN|LIVING_ROOM|STUDY|LIBERO)_SCENE\d+_',s)
    if m: s=s[m.end():]
    return s.replace('_',' ')

def scene_id(p:Path):
    m=re.search(r'((?:KITCHEN|LIVING_ROOM|STUDY|LIBERO)_SCENE\d+)',p.stem)
    return m.group(1) if m else None

def object_words(text):
    toks=[t for t in re.split(r'[^a-z0-9]+', text.lower()) if t]
    return sorted({t for t in toks if (not re.fullmatch(r'scene\d+', t) and (t in KEEP or (len(t)>3 and t not in STOP and not t.isdigit())))})

def h5_info(p:Path):
    info={'loadable_hdf5':False,'demo_count':0,'total_timesteps':0,'action_shape':None,'error':None}
    try:
        with h5py.File(p,'r') as f:
            info['loadable_hdf5']=True
            if 'data' not in f: return info
            demos=list(f['data'].keys()); info['demo_count']=len(demos)
            shapes=[]; total=0
            for d in demos:
                demo=f['data'][d]
                if 'actions' in demo:
                    sh=list(demo['actions'].shape); shapes.append(sh); total+=sh[0]
            info['total_timesteps']=total
            info['action_shape']=shapes[0] if shapes else None
    except Exception as e:
        info['error']=repr(e)
    return info

def loader_ok(p:Path):
    try:
        import tempfile
        from datasets.dataset_smolvlm import SmolVLMDataReader
        meta={'dataset_name':'libero_hdf5','data_dir':str(ROOT),'datalist':[{'path':str(p),'task':task_name(p),'subset':p.parent.name}], 'num_episodes':1,'state_dim':8,'action_dim':7}
        tmp=OUT.parent/'_inventory_loader_probe.json'; tmp.write_text(json.dumps(meta))
        ds=SmolVLMDataReader(str(tmp),num_actions=10,num_views=3,training=False,action_mode='libero_joint',image_size=384)
        next(iter(ds))
        return True,None
    except Exception as e:
        return False,repr(e)

def main():
    rows=[]
    for p in sorted(ROOT.glob('*/*.hdf5')):
        suite=p.parent.name; t=task_name(p); sc=scene_id(p); h=h5_info(p); ok,err=loader_ok(p) if h['loadable_hdf5'] else (False,h['error'])
        rows.append({'suite':suite,'path':str(p),'file_name':p.name,'task_name':t,'scene_id':sc,'language_instruction':t,'demo_count':h['demo_count'],'total_timesteps':h['total_timesteps'],'action_shape':h['action_shape'],'object_words':object_words(t+' '+p.name),'loadable_hdf5':h['loadable_hdf5'],'loadable_simvla_loader':ok,'error':h['error'] or err})
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps({'root':str(ROOT),'files':rows},indent=2))
    by_suite=defaultdict(list); obj=Counter(); scenes=Counter(); broken=[]
    for r in rows:
        by_suite[r['suite']].append(r)
        obj.update(r['object_words'])
        if r['scene_id']: scenes[r['scene_id']]+=1
        if not r['loadable_hdf5'] or not r['loadable_simvla_loader']: broken.append(r)
    lines=['# LIBERO Inventory Report','',f'- Inventory: `{OUT}`',f'- Root: `{ROOT}`',f'- Total files: `{len(rows)}`','','## Suite Summary','','| Suite | Files | Demos | Timesteps | Tasks |','|---|---:|---:|---:|---:|']
    for s,rs in sorted(by_suite.items()): lines.append(f'| `{s}` | {len(rs)} | {sum(r["demo_count"] for r in rs)} | {sum(r["total_timesteps"] for r in rs)} | {len(set(r["task_name"] for r in rs))} |')
    lines += ['','## Top Object Words','']+[f'- `{k}`: `{v}`' for k,v in obj.most_common(40)]
    lines += ['','## Scene IDs','']+[f'- `{k}`: `{v}`' for k,v in sorted(scenes.items())]
    lines += ['','## Broken Files','']+([f'- `{r["path"]}` hdf5={r["loadable_hdf5"]} loader={r["loadable_simvla_loader"]} error=`{r["error"]}`' for r in broken] or ['None'])
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines)+'\n')
    print('inventory_ok', len(rows), 'broken', len(broken), 'report', REPORT)
if __name__=='__main__': main()
