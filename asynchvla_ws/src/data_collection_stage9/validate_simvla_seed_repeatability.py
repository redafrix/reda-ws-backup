from __future__ import annotations
import argparse,json,os
from pathlib import Path
import numpy as np
from .libero_pro_env_utils import make_env, reset_to_init, obs_images, obs_to_proprio
from .simvla_candidate_sampler import load_simvla, sample_candidate

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--suite',default='libero_object_with_mug'); ap.add_argument('--task-id',type=int,default=0); args=ap.parse_args(); model,proc,dev=load_simvla(); env,b=make_env(args.suite,args.task_id,128,seed=1); obs=reset_to_init(env,b['init_states'][0]); img,wrist=obs_images(obs); prop=obs_to_proprio(obs); lang=b['task'].language
 a0=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=dev,steps=10,flowtrace=False)['candidate_action_env'].numpy(); a0b=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=dev,steps=10,flowtrace=False)['candidate_action_env'].numpy(); a1=sample_candidate(model,proc,lang,img,wrist,prop,seed=1,device=dev,steps=10,flowtrace=False)['candidate_action_env'].numpy(); env.close(); rep={'same_seed_max_abs_diff':float(np.max(np.abs(a0-a0b))),'different_seed_l2':float(np.linalg.norm(a0-a1)),'pass':bool(np.max(np.abs(a0-a0b))<1e-6 and np.linalg.norm(a0-a1)>1e-4)}
 out=Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))/'asynchvla_ws/stage9_libero_pro_risk_data/reports/stage9_simvla_seed_repeatability.md'; out.write_text('# Stage 9 SimVLA Seed Repeatability\n\n```json\n'+json.dumps(rep,indent=2)+'\n```\n'); print(out)
if __name__=='__main__': main()
