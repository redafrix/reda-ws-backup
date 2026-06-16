import os
import argparse
import imageio.v2 as imageio
import numpy as np
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--speed', type=float, default=4.0)
    parser.add_argument('--fps', type=int, default=40)
    parser.add_argument('--limit', type=int, default=None)
    args = parser.parse_args()

    vids = sorted([f for f in os.listdir(args.input_dir) if f.endswith('success.mp4')])
    if args.limit:
        vids = vids[:args.limit]
    
    print(f'Found {len(vids)} success videos.')
    
    writer = imageio.get_writer(args.output, fps=args.fps)
    
    total_frames = 0
    for v in vids:
        path = os.path.join(args.input_dir, v)
        print(f'Processing {v}...')
        reader = imageio.get_reader(path)
        
        # Speed up by sampling
        step = max(1, int(args.speed))
        count = 0
        for frame in reader:
            if count % step == 0:
                writer.append_data(frame)
                total_frames += 1
            count += 1
        reader.close()
        
    writer.close()
    print(f'Done. Wrote {total_frames} frames.')

if __name__ == "__main__":
    main()
