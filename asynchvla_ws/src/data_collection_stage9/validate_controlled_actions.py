from __future__ import annotations
import argparse,json,os,time
from pathlib import Path
import numpy as np
from .libero_pro_env_utils import make_env, reset_to_init
from .sim_state_utils import get_state,set_state
from .outcome_metrics import execute_action_chunk
from .label_rules import label_outcome

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--suite',default='libero_object_with_mug'); ap.add_argument('--task-id',type=int,default=0); ap.add_argument('--horizon',type=int,default=10); args=ap.parse_args()
 env,b=make_env(args.suite,args.task_id,128,seed=88); obs=reset_to_init(env,b['init_states'][0]); S=get_state(env)
 actions={'noop':np.tile(np.array([0,0,0,0,0,0,-1],dtype=np.float32),(10,1)), 'large_random':np.random.default_rng(0).uniform(-1,1,size=(10,7)).astype(np.float32), 'gripper_open':np.tile(np.array([0,0,0,0,0,0,-1],dtype=np.float32),(10,1)), 'gripper_close':np.tile(np.array([0,0,0,0,0,0,1],dtype=np.float32),(10,1))}
 rows=[]
 for name,chunk in actions.items():
   set_state(env,S); outcome=execute_action_chunk(env,chunk,args.horizon,obs); lab=label_outcome(outcome); rows.append({'controlled_action':name,'outcome':outcome,'label':lab})
 env.close(); out=Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))/'asynchvla_ws/stage9_libero_pro_risk_data/reports/stage9_controlled_action_labeler_sanity.md'; out.write_text('# Stage 9 Controlled Action Labeler Sanity\n\n```json\n'+json.dumps(rows,indent=2,default=str)+'\n```\n'); print(out)
if __name__=='__main__': main()
