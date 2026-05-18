from __future__ import annotations
import argparse,json,os,time,uuid,subprocess
from pathlib import Path
from collections import Counter,defaultdict
import numpy as np
from PIL import Image
from .libero_pro_env_utils import make_env, reset_to_init, obs_images, obs_to_proprio, suite_perturbation_type
from .task_parser import parse_task_context
from .sim_state_utils import get_state,set_state,save_state_npz
from .outcome_metrics import execute_action_chunk, object_body_positions, detect_phase, eef_pos
from .label_rules import label_outcome
from .simvla_candidate_sampler import load_simvla, sample_candidate
from .history_buffer import HistoryBuffer

PHASES_OF_INTEREST = [
    "APPROACH",
    "NEAR_GRASP",
    "GRASP_OR_LIFT",
    "TRANSPORT",
    "PLACE_OR_GOAL",
    "STUCK_OR_NO_PROGRESS"
]

def git_hash():
    try: return subprocess.check_output(["git","rev-parse","--short","HEAD"],text=True).strip()
    except Exception: return "unknown"

def save_png(path, img):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); Image.fromarray(img.astype(np.uint8)).save(path); return str(path)

def collect(args):
    rng=np.random.default_rng(args.collection_seed)
    outdir=Path(args.out_dir); outdir.mkdir(parents=True,exist_ok=True); (outdir/"states").mkdir(exist_ok=True); (outdir/"images").mkdir(exist_ok=True)
    model=proc=device=None
    if not args.no_simvla:
        model,proc,device=load_simvla()
    samples=[]; label_counts=Counter(); selected=[]
    for suite in args.suites:
      for tid in args.task_ids:
        selected.append((suite,tid))

    phase_audit_results = defaultdict(Counter)
    phases_to_collect = args.preferred_phases if args.preferred_phases else PHASES_OF_INTEREST
    max_rollouts = args.max_parent_episodes if args.max_parent_episodes is not None else args.max_parent_rollouts

    for suite,tid in selected:
      env,b=make_env(suite,tid,args.resolution,seed=args.env_seed)
      init_states=b["init_states"]; task=b["task"]; lang=task.language
      
      collected_entries = []
      all_bodies = list(object_body_positions(env).keys())

      if args.parent_selection_mode == "risky_states":
          rollout_count = 0
          print(f"Starting risky-state sampling for {suite}_t{tid}...", flush=True)
          while len(collected_entries) < args.states_per_task and rollout_count < max_rollouts:
              obs=reset_to_init(env,init_states[rollout_count % len(init_states)],warmup=args.warmup)
              hist=HistoryBuffer(args.history_k)
              task_context=parse_task_context(lang, obs, all_bodies=all_bodies)
              last_eef_pos = None
              recent_motion_queue = []
              rollout_states = []
              rollout_success = False
              
              for step in range(args.parent_roll_steps):
                  curr_eef = eef_pos(obs)
                  if last_eef_pos is not None and curr_eef is not None:
                      motion = np.linalg.norm(curr_eef - last_eef_pos)
                      recent_motion_queue.append(motion)
                      if len(recent_motion_queue) > 15: recent_motion_queue.pop(0)
                  
                  stats = {"recent_motion": np.mean(recent_motion_queue) if len(recent_motion_queue) >= 15 else 1.0}
                  phase = detect_phase(obs, env, task_context, history_stats=stats)
                  
                  S=get_state(env)
                  rollout_states.append({
                      "state": S,
                      "obs": obs,
                      "history": hist.to_list(),
                      "phase": phase,
                      "step": step,
                      "rollout": rollout_count
                  })

                  img,wrist=obs_images(obs); prop=obs_to_proprio(obs)
                  if args.no_simvla: act=np.array([0,0,0,0,0,0,-1],dtype=np.float32)
                  else:
                      cand=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=device,steps=args.horizon,flowtrace=False)
                      act=cand["candidate_action_env"][0].numpy().astype(np.float32)
                  
                  last_eef_pos = curr_eef
                  obs,rew,done,info=env.step(act)
                  hist.append({"reward":float(rew),"success":bool(rew>0),"proprio":obs_to_proprio(obs).tolist(),"executed_action":act.tolist()})
                  if rew > 0: rollout_success = True
                  if done: break
              
              is_failure = not rollout_success
              if is_failure or not args.prefer_failed_rollouts:
                  risk_start = max(0, len(rollout_states) - args.risk_window)
                  risk_indices = list(range(risk_start, len(rollout_states)))
                  if risk_indices:
                      # Take up to 2 states per rollout for diversity (middle and end of window)
                      to_pick = [risk_indices[len(risk_indices)//2]]
                      if len(risk_indices) > 1: to_pick.append(risk_indices[-1])
                      
                      for s_idx in to_pick:
                          if len(collected_entries) < args.states_per_task:
                              s = rollout_states[s_idx]
                              s["parent_failed_or_timeout"] = is_failure
                              s["parent_episode_success"] = rollout_success
                              s["parent_episode_steps"] = len(rollout_states)
                              collected_entries.append(s)
              
              rollout_count += 1

      elif args.sampling_mode == "phase_balanced":
          states_by_phase = defaultdict(list)
          rollout_count = 0
          print(f"Starting phase-balanced sampling for {suite}_t{tid}...", flush=True)
          while any(len(states_by_phase[p]) < args.states_per_phase for p in phases_to_collect) and rollout_count < max_rollouts:
              obs=reset_to_init(env,init_states[rollout_count % len(init_states)],warmup=args.warmup)
              hist=HistoryBuffer(args.history_k)
              task_context=parse_task_context(lang, obs, all_bodies=all_bodies)
              last_eef_pos = None
              recent_motion_queue = []
              
              for step in range(args.parent_roll_steps):
                  curr_eef = eef_pos(obs)
                  if last_eef_pos is not None and curr_eef is not None:
                      motion = np.linalg.norm(curr_eef - last_eef_pos)
                      recent_motion_queue.append(motion)
                      if len(recent_motion_queue) > 15: recent_motion_queue.pop(0)
                  
                  stats = {"recent_motion": np.mean(recent_motion_queue) if len(recent_motion_queue) >= 15 else 1.0}
                  phase = detect_phase(obs, env, task_context, history_stats=stats)
                  phase_audit_results[f"{suite}_t{tid}"][phase] += 1
                  
                  if phase in phases_to_collect and len(states_by_phase[phase]) < args.states_per_phase:
                      S=get_state(env)
                      states_by_phase[phase].append({
                          "state": S,
                          "obs": obs,
                          "history": hist.to_list(),
                          "phase": phase,
                          "step": step,
                          "rollout": rollout_count,
                          "parent_failed_or_timeout": False,
                          "parent_episode_success": False,
                          "parent_episode_steps": step+1
                      })
                  
                  img,wrist=obs_images(obs); prop=obs_to_proprio(obs)
                  if args.no_simvla: act=np.array([0,0,0,0,0,0,-1],dtype=np.float32)
                  else:
                      cand=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=device,steps=args.horizon,flowtrace=False)
                      act=cand["candidate_action_env"][0].numpy().astype(np.float32)
                  
                  last_eef_pos = curr_eef
                  obs,rew,done,info=env.step(act)
                  hist.append({"reward":float(rew),"success":bool(rew>0),"proprio":obs_to_proprio(obs).tolist(),"executed_action":act.tolist()})
                  if done: break
              rollout_count += 1
          
          if not args.audit_phases:
            for p in phases_to_collect:
                collected_entries.extend(states_by_phase[p])
      else:
        for state_i in range(args.states_per_task):
            obs=reset_to_init(env,init_states[state_i % len(init_states)],warmup=args.warmup)
            hist=HistoryBuffer(args.history_k)
            task_context=parse_task_context(lang, obs, all_bodies=all_bodies)
            pre_steps = int(round((state_i / max(1, args.states_per_task - 1)) * args.parent_roll_steps)) if args.states_per_task > 1 else 0
            for pre in range(pre_steps):
                img,wrist=obs_images(obs); prop=obs_to_proprio(obs)
                if args.no_simvla: act=np.array([0,0,0,0,0,0,-1],dtype=np.float32)
                else:
                    cand=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=device,steps=args.horizon,flowtrace=False)
                    act=cand["candidate_action_env"][0].numpy().astype(np.float32)
                obs,rew,done,info=env.step(act)
                hist.append({"reward":float(rew),"success":bool(rew>0),"proprio":obs_to_proprio(obs).tolist(),"executed_action":act.tolist()})
                if done: break
            collected_entries.append({
                "state": get_state(env),
                "obs": obs,
                "history": hist.to_list(),
                "phase": "UNKNOWN",
                "step": pre_steps,
                "rollout": state_i,
                "parent_failed_or_timeout": False,
                "parent_episode_success": False,
                "parent_episode_steps": pre_steps
            })

      if args.audit_phases:
          print(f"Audit phases for {suite}_t{tid}: {dict(phase_audit_results[f'{suite}_t{tid}'] )}", flush=True)
          env.close()
          continue

      task_samples = []
      for i, entry in enumerate(collected_entries):
        S = entry["state"]
        obs = entry["obs"]
        hist_list = entry["history"]
        phase = entry["phase"]
        parent_rollout = entry["rollout"]
        parent_step = entry["step"]
        
        parent_episode_id=f"{suite}_t{tid}_r{parent_rollout}_p{phase}"
        state_id=f"{parent_episode_id}_s{parent_step}_state"
        state_path=save_state_npz(outdir/"states"/f"{state_id}.npz",S)
        
        before_img,before_wrist=obs_images(obs); prop=obs_to_proprio(obs); before_obj=object_body_positions(env); task_context=parse_task_context(lang, obs, all_bodies=all_bodies)
        
        seed_list=list(args.simvla_seeds)
        for seed in seed_list:
            set_state(env,S)
            if args.no_simvla:
                chunk=np.tile(np.array([0,0,0,0,0,0,-1],dtype=np.float32),(args.horizon,1)); norm=chunk; flow={}
            else:
                cand=sample_candidate(model,proc,lang,before_img,before_wrist,prop,seed=seed,device=device,steps=args.horizon,flowtrace=True)
                chunk=cand["candidate_action_env"].numpy().astype(np.float32); norm=cand["candidate_action_normalized"].numpy().astype(np.float32); flow={k:(v.tolist() if hasattr(v,"tolist") else v) for k,v in cand.get("flow_trace_summary",{}).items()}
            
            outcome, after_obs = execute_action_chunk(env,chunk,args.horizon,obs,task_context=task_context,return_after_obs=True)
            label=label_outcome(outcome, task_context=task_context)
            label["parent_phase"] = phase
            label["parent_failed_or_timeout"] = entry.get("parent_failed_or_timeout", False)
            label["parent_episode_success"] = entry.get("parent_episode_success", False)
            label["parent_episode_steps"] = entry.get("parent_episode_steps", 0)
            
            label_counts[label["label"]]+=1
            after_img,_=obs_images(after_obs)
            
            sid=f"{state_id}_seed{seed}"
            before_path=save_png(outdir/"images"/f"{sid}_before.png",before_img) if args.save_images else None
            after_path=save_png(outdir/"images"/f"{sid}_after.png",after_img) if args.save_images and after_img is not None else None
            
            sample={"schema_version":"stage9_libero_pro_counterfactual_v3","sample_id":sid,"metadata":{"task_name":f"{suite}_task{tid}","task_language":lang,"libero_pro_suite_or_task":suite,"perturbation_type":suite_perturbation_type(suite),"parent_phase":phase,"simvla_generation_seed":int(seed),"state_id":state_id,"parent_step_index":parent_step,"collection_time":time.strftime("%Y-%m-%dT%H:%M:%S"),"code_version":git_hash()},"history":hist_list,"current":{"proprio":prop.tolist(),"object_positions_before":before_obj,"sim_state_path":state_path,"before_image_path":before_path,"after_image_path":after_path,"task_context":task_context},"candidate_action":{"candidate_action_normalized":norm.tolist(),"candidate_action_env":chunk.tolist(),"simvla_seed":int(seed),"flowtrace_features":flow},"outcome":outcome,"label":label}
            task_samples.append(sample)
        if len(task_samples) % 20 == 0: print("samples",len(task_samples),"labels",dict(label_counts),flush=True)
      
      env.close()
      jsonl=outdir/"counterfactual_samples.jsonl"
      with open(jsonl, "a") as f:
          for s in task_samples:
              f.write(json.dumps(s,default=str) + "\n")
      print(f"Finished {suite}_t{tid}, saved {len(task_samples)} samples.", flush=True)

    summary={"num_samples":len(samples),"label_counts":dict(label_counts),"out_dir":str(outdir),"suites":args.suites,"task_ids":args.task_ids}
    (outdir/"summary.json").write_text(json.dumps(summary,indent=2)); return summary

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--suites",nargs="+",default=["libero_object_with_mug"]); ap.add_argument("--task-ids",nargs="+",type=int,default=[0]); ap.add_argument("--states-per-task",type=int,default=5); ap.add_argument("--simvla-seeds",nargs="+",type=int,default=[0,1,2,3,4,5,6,7]); ap.add_argument("--horizon",type=int,default=10); ap.add_argument("--history-k",type=int,default=4); ap.add_argument("--resolution",type=int,default=128); ap.add_argument("--warmup",type=int,default=10); ap.add_argument("--parent-roll-steps",type=int,default=100); ap.add_argument("--env-seed",type=int,default=7); ap.add_argument("--collection-seed",type=int,default=123); ap.add_argument("--out-dir",default=str(Path(os.environ.get("REDA_WS","/media/rootalkhatib/My Passport/reda_ws"))/"asynchvla_ws/stage9_libero_pro_risk_data/data/pilot")); ap.add_argument("--save-images",action="store_true"); ap.add_argument("--no-simvla",action="store_true"); ap.add_argument("--sampling-mode",choices=["interval","phase_balanced"],default="interval"); ap.add_argument("--parent-selection-mode",choices=["phase_balanced","risky_states"],default="phase_balanced"); ap.add_argument("--risk-window",type=int,default=5); ap.add_argument("--min-parent-rollouts",type=int,default=10); ap.add_argument("--prefer-failed-rollouts",type=lambda x: (str(x).lower()=="true"),default=True); ap.add_argument("--states-per-phase",type=int,default=2); ap.add_argument("--max-parent-rollouts",type=int,default=5); ap.add_argument("--audit-phases",action="store_true"); ap.add_argument("--preferred-phases",nargs="+",default=None); ap.add_argument("--max-parent-episodes",type=int,default=None)
 args=ap.parse_args(); summary=collect(args); print(json.dumps(summary,indent=2))
if __name__=="__main__": main()
