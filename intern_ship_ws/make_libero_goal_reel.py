import os
import argparse
import imageio.v2 as imageio
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--speed', type=float, default=4.0)
    parser.add_argument('--fps', type=int, default=40)
    args = parser.parse_args()

    # Get one success video per task from task_sweep_database
    # These are named by task description then epX_success.mp4
    all_files = sorted([f for f in os.listdir(args.input_dir) if f.endswith('success.mp4')])
    
    # Group by task name (prefix before _ep)
    tasks = {}
    for f in all_files:
        task_name = f.split('_ep')[0]
        if task_name not in tasks:
            tasks[task_name] = f
            
    selected_vids = sorted(tasks.values())
    print(f'Found {len(selected_vids)} unique tasks.')
    
    writer = imageio.get_writer(args.output, fps=args.fps)
    total_frames = 0
    for v in selected_vids:
        path = os.path.join(args.input_dir, v)
        print(f'Processing {v}...')
        reader = imageio.get_reader(path)
        step = max(1, int(args.speed))
        count = 0
        for frame in reader:
            if count % step == 0:
                writer.append_data(frame)
                total_frames += 1
            count += 1
        reader.close()
    
    writer.close()
    print(f'Done. Reel saved to {args.output} ({total_frames} frames)')

if __name__ == "__main__":
    main()
