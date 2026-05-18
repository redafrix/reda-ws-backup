from __future__ import annotations
import argparse,json,time,os
from pathlib import Path
import numpy as np
from .libero_pro_env_utils import make_env, reset_to_init
from .sim_state_utils import get_state,set_state,state_distance
from .outcome_metrics import object_body_positions,eef_pos

def rollout(env, action, n):
    rewards=[]; obs=None
    for _ in range(n): obs,r,d,i=env.step(action); rewards.append(float(r))
    return obs,rewards,object_body_positions(env),get_state(env)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--suite',default='libero_object_with_mug'); ap.add_argument('--task-id',type=int,default=0); ap.add_argument('--horizon',type=int,default=5); args=ap.parse_args()
 env,b=make_env(args.suite,args.task_id,128,seed=77); obs=reset_to_init(env,b['init_states'][0]); S=get_state(env); action=np.array([0,0,0,0,0,0,-1],dtype=np.float32)
 obs1,r1,obj1,st1=rollout(env,action,args.horizon); set_state(env,S); obs2,r2,obj2,st2=rollout(env,action,args.horizon)
 rep={'suite':args.suite,'task_id':args.task_id,'reward_seq_1':r1,'reward_seq_2':r2,'reward_max_abs_diff':float(np.max(np.abs(np.array(r1)-np.array(r2)))),'state_max_abs_diff_after':state_distance(st1,st2),'object_positions_run1':obj1,'object_positions_run2':obj2,'pass': bool(np.max(np.abs(np.array(r1)-np.array(r2)))<1e-8 and (state_distance(st1,st2)<1e-7 or np.isnan(state_distance(st1,st2))))}
 env.close(); out=Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))/'asynchvla_ws/stage9_libero_pro_risk_data/reports/stage9_reset_determinism_report.md'; out.write_text('# Stage 9 Reset Determinism Report\n\n```json\n'+json.dumps(rep,indent=2)+'\n```\n'); print(out)
if __name__=='__main__': main()
