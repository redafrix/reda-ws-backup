from __future__ import annotations
import argparse, json, time, os, sys
from pathlib import Path
from .libero_pro_env_utils import available_suites, make_env, reset_to_init, check_success, suite_perturbation_type
from .outcome_metrics import obs_signal_summary, object_body_positions, contact_summary
from .sim_state_utils import get_state

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--suites',nargs='*',default=['libero_object_with_mug','libero_spatial_with_mug','libero_goal_with_mug']); ap.add_argument('--tasks',nargs='*',type=int,default=[0]); ap.add_argument('--resolution',type=int,default=128); ap.add_argument('--out',default=None); args=ap.parse_args()
    rows=[]
    for suite in args.suites:
      for tid in args.tasks:
        try:
          env,b=make_env(suite,tid,args.resolution,seed=123); obs=reset_to_init(env,b['init_states'][0]); st=get_state(env)
          row={'suite':suite,'task_id':tid,'task_language':b['task'].language,'perturbation_type':suite_perturbation_type(suite),'obs':obs_signal_summary(obs),'success_available':check_success(env) is not None,'object_state_count':len(object_body_positions(env)),'object_state_example':list(object_body_positions(env).items())[:10],'contact':contact_summary(env),'sim_state_kind':st.get('kind'),'sim_state_len':len(st.get('flat',[]))}
          env.close()
        except Exception as e: row={'suite':suite,'task_id':tid,'error':repr(e)}
        rows.append(row)
    out=Path(args.out or Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))/'asynchvla_ws/stage9_libero_pro_risk_data/reports/stage9_observation_signal_audit.md'); out.parent.mkdir(parents=True,exist_ok=True)
    lines=['# Stage 9 Observation Signal Audit','',f'Generated: `{time.strftime("%Y-%m-%dT%H:%M:%S")}`','', '```json', json.dumps(rows,indent=2,default=str), '```']
    out.write_text('\n'.join(lines)+'\n'); print(out)
if __name__=='__main__': main()
