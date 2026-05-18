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
from .strict_label_utils import (
    LABEL_BAD,
    LABEL_AMBIGUOUS,
    LABEL_VALIDATED_BAD,
    VALIDATED_BAD,
    same_state_summary,
    sample_uid,
    validate_bad_sample,
)

PHASES_OF_INTEREST = [
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

def _replay_raw_bad(env, state, sample, before_obs, action_chunk, horizon: int, task_context: dict, attempts: int) -> dict:
    replay_attempts = []
    for attempt in range(attempts):
        set_state(env, state)
        outcome = execute_action_chunk(env, action_chunk, horizon, before_obs, task_context=task_context, return_after_obs=False)
        label = label_outcome(outcome, task_context=task_context)
        replay_attempts.append({
            "attempt": attempt,
            "requested_horizon": int(horizon),
            "status": "ok",
            "outcome": outcome,
            "label": label,
        })
    return {
        "sample_uid": sample_uid(sample),
        "sample_id": sample.get("sample_id"),
        "status": "ok",
        "attempts": replay_attempts,
        "original_bad_reasons": sample.get("label", {}).get("bad_evidence") or sample.get("label", {}).get("label_reasons") or [],
    }

def _finalize_state_samples(env, state, samples, before_obs, task_context, args, validation_counts):
    finalized = []
    for sample in samples:
        raw_label = sample["label"]
        sample["raw_label"] = raw_label
        sample["label"] = dict(raw_label)
        sample["label"]["initial_label"] = raw_label.get("label")
        sample["label"]["initial_label_output"] = raw_label
        sample["label"]["same_state_comparison"] = same_state_summary(sample, samples)
        if raw_label.get("label") == LABEL_BAD:
            action_chunk = np.asarray(sample["candidate_action"]["candidate_action_env"], dtype=np.float32)
            replay = _replay_raw_bad(env, state, sample, before_obs, action_chunk, args.horizon, task_context, args.replay_raw_bad_attempts)
            validation = validate_bad_sample(sample, samples, replay=replay, require_replay=True)
            sample["label"]["strict_validation"] = validation
            validation_counts[validation["validation_status"]] += 1
            if validation["validation_status"] == VALIDATED_BAD:
                sample["label"]["label"] = LABEL_VALIDATED_BAD
                sample["label"]["final_label"] = LABEL_VALIDATED_BAD
                sample["label"]["label_confidence"] = "HIGH"
                sample["label"]["label_reasons"] = raw_label.get("label_reasons", [])
                sample["label"]["validated_bad_reasons"] = raw_label.get("bad_evidence", [])
            else:
                sample["label"]["label"] = LABEL_AMBIGUOUS
                sample["label"]["final_label"] = LABEL_AMBIGUOUS
                sample["label"]["label_confidence"] = "LOW"
                sample["label"]["label_reasons"] = ["raw_bad_failed_strict_validation"]
                sample["label"]["downgraded_from_raw_bad"] = True
                sample["label"]["downgrade_reasons"] = validation.get("failure_reasons", [])
                sample["label"]["bad_evidence"] = []
        else:
            sample["label"]["final_label"] = raw_label.get("label")
        finalized.append(sample)
    return finalized

def collect(args):
    rng=np.random.default_rng(args.collection_seed)
    outdir=Path(args.out_dir); outdir.mkdir(parents=True,exist_ok=True); (outdir/"states").mkdir(exist_ok=True); (outdir/"images").mkdir(exist_ok=True)
    model=proc=device=None
    if not args.no_simvla:
        model,proc,device=load_simvla()
    samples=[]; label_counts=Counter(); raw_label_counts=Counter(); validation_counts=Counter(); selected=[]; total_selected_states=0
    for suite in args.suites:
      for tid in args.task_ids:
        selected.append((suite,tid))

    phase_audit_results = defaultdict(Counter)
    phases_to_collect = args.preferred_phases if args.preferred_phases else PHASES_OF_INTEREST
    max_rollouts = args.max_parent_episodes if args.max_parent_episodes is not None else args.max_parent_rollouts

    for suite,tid in selected:
      if args.max_total_states is not None and total_selected_states >= args.max_total_states:
          break
      try:
          env,b=make_env(suite,tid,args.resolution,seed=args.env_seed)
      except Exception as exc:
          print(f"Skipping invalid/unavailable task {suite}_t{tid}: {exc}", flush=True)
          continue
      init_states=b["init_states"]; task=b["task"]; lang=task.language
      
      collected_entries = []
      all_bodies = list(object_body_positions(env).keys())

      if args.parent_selection_mode == "risky_states":
          rollout_count = 0
          print(f"Starting risky-state sampling for {suite}_t{tid}...", flush=True)
          while len(collected_entries) < args.states_per_task and rollout_count < max_rollouts and (args.max_total_states is None or total_selected_states + len(collected_entries) < args.max_total_states):
              obs=reset_to_init(env,init_states[rollout_count % len(init_states)],warmup=args.warmup)
              hist=HistoryBuffer(args.history_k)
              task_context=parse_task_context(lang, obs, all_bodies=all_bodies)
              last_eef_pos = None
              recent_motion_queue = []
              rollout_states = []
              rollout_success = False
              rollout_rewards = []
              rollout_done = False
              
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
                      "rollout": rollout_count,
                      "phase_score": 1 if phase in phases_to_collect else 0,
                  })

                  img,wrist=obs_images(obs); prop=obs_to_proprio(obs)
                  if args.no_simvla: act=np.array([0,0,0,0,0,0,-1],dtype=np.float32)
                  else:
                      cand=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=device,steps=1,flowtrace=False)
                      act=cand["candidate_action_env"][0].numpy().astype(np.float32)
                  
                  last_eef_pos = curr_eef
                  obs,rew,done,info=env.step(act)
                  rollout_rewards.append(float(rew))
                  hist.append({"reward":float(rew),"success":bool(rew>0),"proprio":obs_to_proprio(obs).tolist(),"executed_action":act.tolist()})
                  if rew > 0: rollout_success = True
                  if done:
                      rollout_done = True
                      break
              
              is_failure = not rollout_success
              if is_failure or not args.prefer_failed_rollouts:
                  risk_start = max(0, len(rollout_states) - args.risk_window)
                  risk_indices = list(range(risk_start, len(rollout_states)))
                  if risk_indices:
                      phase_indices = [idx for idx in risk_indices if rollout_states[idx]["phase"] in phases_to_collect]
                      source_indices = phase_indices if phase_indices else risk_indices
                      to_pick = [source_indices[len(source_indices)//2]]
                      if len(source_indices) > 1: to_pick.append(source_indices[-1])
                      
                      for s_idx in to_pick:
                          if len(collected_entries) < args.states_per_task and (args.max_total_states is None or total_selected_states + len(collected_entries) < args.max_total_states):
                              s = rollout_states[s_idx]
                              s["parent_failed_or_timeout"] = is_failure
                              s["parent_episode_success"] = rollout_success
                              s["parent_episode_steps"] = len(rollout_states)
                              s["parent_timeout"] = bool(is_failure and not rollout_done)
                              s["distance_to_failure_or_timeout"] = max(0, len(rollout_states) - s["step"])
                              lo = max(0, s["step"] - 4); hi = min(len(rollout_rewards), s["step"] + 5)
                              s["parent_rewards_around_state"] = rollout_rewards[lo:hi]
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
                          "parent_episode_steps": step+1,
                          "parent_timeout": False,
                          "distance_to_failure_or_timeout": None,
                          "parent_rewards_around_state": []
                      })
                  
                  img,wrist=obs_images(obs); prop=obs_to_proprio(obs)
                  if args.no_simvla: act=np.array([0,0,0,0,0,0,-1],dtype=np.float32)
                  else:
                      cand=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=device,steps=1,flowtrace=False)
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
                    cand=sample_candidate(model,proc,lang,img,wrist,prop,seed=0,device=device,steps=1,flowtrace=False)
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
                "parent_episode_steps": pre_steps,
                "parent_timeout": False,
                "distance_to_failure_or_timeout": None,
                "parent_rewards_around_state": []
            })

      if args.audit_phases:
          print(f"Audit phases for {suite}_t{tid}: {dict(phase_audit_results[f'{suite}_t{tid}'] )}", flush=True)
          env.close()
          continue

      task_samples = []
      for i, entry in enumerate(collected_entries):
        if args.max_total_states is not None and total_selected_states >= args.max_total_states:
            break
        total_selected_states += 1
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
        state_samples = []
        for seed in seed_list:
            set_state(env,S)
            if args.no_simvla:
                chunk=np.tile(np.array([0,0,0,0,0,0,-1],dtype=np.float32),(args.horizon,1)); norm=chunk; flow={}
            else:
                cand=sample_candidate(model,proc,lang,before_img,before_wrist,prop,seed=seed,device=device,steps=args.horizon,flowtrace=True)
                chunk=cand["candidate_action_env"].numpy().astype(np.float32); norm=cand["candidate_action_normalized"].numpy().astype(np.float32); flow={k:(v.tolist() if hasattr(v,"tolist") else v) for k,v in cand.get("flow_trace_summary",{}).items()}
            
            sid=f"{state_id}_seed{seed}"
            trace_frame_dir = outdir/"trace_frames"/sid if args.save_trace_frames else None
            outcome, after_obs = execute_action_chunk(env,chunk,args.horizon,obs,task_context=task_context,return_after_obs=True,save_full_trace=args.save_full_trace,trace_frame_dir=trace_frame_dir,trace_frame_stride=args.trace_frame_stride)
            label=label_outcome(outcome, task_context=task_context)
            label["parent_phase"] = phase
            label["parent_failed_or_timeout"] = entry.get("parent_failed_or_timeout", False)
            label["parent_episode_success"] = entry.get("parent_episode_success", False)
            label["parent_episode_steps"] = entry.get("parent_episode_steps", 0)
            label["parent_timeout"] = entry.get("parent_timeout", False)
            label["distance_to_failure_or_timeout"] = entry.get("distance_to_failure_or_timeout")
            raw_label_counts[label["label"]]+=1
            after_img,_=obs_images(after_obs)
            
            before_path=save_png(outdir/"images"/f"{sid}_before.png",before_img) if args.save_images else None
            after_path=save_png(outdir/"images"/f"{sid}_after.png",after_img) if args.save_images and after_img is not None else None
            
            sample={"schema_version":"stage9_libero_pro_counterfactual_v4_validated","sample_id":sid,"_dataset_name":Path(args.out_dir).name,"metadata":{"task_name":f"{suite}_task{tid}","task_language":lang,"libero_pro_suite_or_task":suite,"perturbation_type":suite_perturbation_type(suite),"parent_phase":phase,"simvla_generation_seed":int(seed),"state_id":state_id,"parent_step_index":parent_step,"collection_time":time.strftime("%Y-%m-%dT%H:%M:%S"),"code_version":git_hash(),"parent_timeout":entry.get("parent_timeout",False),"distance_to_failure_or_timeout":entry.get("distance_to_failure_or_timeout"),"parent_rewards_around_state":entry.get("parent_rewards_around_state",[])},"history":hist_list,"current":{"proprio":prop.tolist(),"object_positions_before":before_obj,"sim_state_path":state_path,"before_image_path":before_path,"after_image_path":after_path,"task_context":task_context},"candidate_action":{"candidate_action_normalized":norm.tolist(),"candidate_action_env":chunk.tolist(),"simvla_seed":int(seed),"flowtrace_features":flow},"outcome":outcome,"label":label}
            state_samples.append(sample)
        finalized_state_samples = _finalize_state_samples(env, S, state_samples, obs, task_context, args, validation_counts)
        for sample in finalized_state_samples:
            label_counts[sample["label"]["label"]]+=1
        task_samples.extend(finalized_state_samples)
        if len(task_samples) % 20 == 0: print("samples",len(task_samples),"labels",dict(label_counts),flush=True)
      
      env.close()
      jsonl=outdir/"counterfactual_samples.jsonl"
      with open(jsonl, "a") as f:
          for s in task_samples:
              f.write(json.dumps(s,default=str) + "\n")
      print(f"Finished {suite}_t{tid}, saved {len(task_samples)} samples.", flush=True)

    summary={"num_samples":sum(label_counts.values()),"selected_states":total_selected_states,"label_counts":dict(label_counts),"raw_label_counts":dict(raw_label_counts),"validation_counts":dict(validation_counts),"out_dir":str(outdir),"suites":args.suites,"task_ids":args.task_ids,"horizon":args.horizon,"history_k":args.history_k,"simvla_seeds":args.simvla_seeds}
    (outdir/"summary.json").write_text(json.dumps(summary,indent=2)); return summary

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--suites",nargs="+",default=["libero_object_with_mug"]); ap.add_argument("--task-ids",nargs="+",type=int,default=[0]); ap.add_argument("--states-per-task",type=int,default=5); ap.add_argument("--max-total-states",type=int,default=None); ap.add_argument("--simvla-seeds",nargs="+",type=int,default=[0,1,2,3,4,5,6,7]); ap.add_argument("--horizon",type=int,default=40); ap.add_argument("--history-k",type=int,default=8); ap.add_argument("--resolution",type=int,default=128); ap.add_argument("--warmup",type=int,default=10); ap.add_argument("--parent-roll-steps",type=int,default=100); ap.add_argument("--env-seed",type=int,default=7); ap.add_argument("--collection-seed",type=int,default=123); ap.add_argument("--out-dir",default=str(Path(os.environ.get("REDA_WS","/media/rootalkhatib/My Passport/reda_ws"))/"asynchvla_ws/stage9_libero_pro_risk_data/data/pilot")); ap.add_argument("--save-images",action="store_true"); ap.add_argument("--save-full-trace",action=argparse.BooleanOptionalAction,default=True); ap.add_argument("--save-trace-frames",action="store_true"); ap.add_argument("--trace-frame-stride",type=int,default=10); ap.add_argument("--replay-raw-bad-attempts",type=int,default=2); ap.add_argument("--no-simvla",action="store_true"); ap.add_argument("--sampling-mode",choices=["interval","phase_balanced"],default="interval"); ap.add_argument("--parent-selection-mode",choices=["phase_balanced","risky_states"],default="phase_balanced"); ap.add_argument("--risk-window",type=int,default=8); ap.add_argument("--min-parent-rollouts",type=int,default=10); ap.add_argument("--prefer-failed-rollouts",type=lambda x: (str(x).lower()=="true"),default=True); ap.add_argument("--states-per-phase",type=int,default=2); ap.add_argument("--max-parent-rollouts",type=int,default=20); ap.add_argument("--audit-phases",action="store_true"); ap.add_argument("--preferred-phases",nargs="+",default=None); ap.add_argument("--max-parent-episodes",type=int,default=None)
 args=ap.parse_args(); summary=collect(args); print(json.dumps(summary,indent=2))
if __name__=="__main__": main()
