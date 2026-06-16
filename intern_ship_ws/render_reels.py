import os
import argparse
import json
import numpy as np
import torch
import imageio.v2 as imageio
from pathlib import Path
from tqdm import tqdm
import sys

# Add LIBERO to path
sys.path.insert(0, '/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO')
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv

LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
NUM_STEPS_WAIT = 10

def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
    if quat[3] > 1.0: quat[3] = 1.0
    elif quat[3] < -1.0: quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if np.isclose(den, 0.0): return np.zeros(3)
    return (quat[:3] * 2.0 * np.arccos(quat[3])) / den

def render_episode(env, init_state, step_scores_path, speed, writer):
    # Load step actions
    actions = []
    if os.path.exists(step_scores_path):
        with open(step_scores_path, 'r') as f:
            for line in f:
                data = json.loads(line)
                # Receding horizon check10 usually executes 10 steps
                # The step_scores has the executed_action for each step
                if 'executed_action' in data:
                    actions.append(data['executed_action'])

    obs = env.set_init_state(init_state)
    t = 0
    frames_written = 0
    
    # Wait steps
    for _ in range(NUM_STEPS_WAIT):
        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
        
    for act in actions:
        img = np.ascontiguousarray(obs['agentview_image'][::-1, ::-1])
        if t % int(speed) == 0:
            writer.append_data(img)
            frames_written += 1
        
        obs, rew, done, info = env.step(act)
        t += 1
        if done:
            break
            
    # Final frame
    img = np.ascontiguousarray(obs['agentview_image'][::-1, ::-1])
    writer.append_data(img)
    frames_written += 1
    return frames_written

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--runs_dir', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--suite', default='libero_goal_object_ood')
    parser.add_argument('--speed', type=float, default=4.0)
    parser.add_argument('--fps', type=int, default=40)
    args = parser.parse_args()

    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict[args.suite]()
    
    writer = imageio.get_writer(args.output, fps=args.fps)
    
    for tid in range(task_suite.n_tasks):
        task_dir = os.path.join(args.runs_dir, f'task{tid}', 'risk_topk8_selected_cap', 'risk_topk8')
        summary_path = os.path.join(task_dir, 'episode_summaries.jsonl')
        scores_path = os.path.join(task_dir, 'step_scores_risk_topk8.jsonl')
        
        if not os.path.exists(summary_path):
            continue
            
        success_idx = None
        with open(summary_path, 'r') as f:
            for line in f:
                data = json.loads(line)
                if data.get('success'):
                    success_idx = data.get('episode_index')
                    break
        
        if success_idx is None:
            with open(summary_path, 'r') as f:
                line = f.readline()
                if line:
                    success_idx = json.loads(line).get('episode_index')
        
        if success_idx is not None:
            print(f'Rendering Task {tid} Episode {success_idx}...')
            task = task_suite.get_task(tid)
            init_states = task_suite.get_task_init_states(tid)
            bddl = Path(get_libero_path('bddl_files')) / task.problem_folder / task.bddl_file
            env = OffScreenRenderEnv(bddl_file_name=str(bddl), camera_heights=256, camera_widths=256)
            
            # Filter scores for this episode
            ep_scores_tmp = '/tmp/ep_scores.jsonl'
            with open(ep_scores_tmp, 'w') as outf:
                with open(scores_path, 'r') as inf:
                    for line in inf:
                        d = json.loads(line)
                        if d.get('episode_index') == success_idx:
                            outf.write(line)
            
            render_episode(env, init_states[success_idx % len(init_states)], ep_scores_tmp, args.speed, writer)
            env.close()
            
    writer.close()
    print(f'Done. Reel saved to {args.output}')

if __name__ == "__main__":
    main()
