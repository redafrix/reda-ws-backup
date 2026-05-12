import subprocess, os, time
from pathlib import Path

DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
TEST_DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_test.pt'
OOD_DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt'
LOG_DIR = Path('logs_marathon_v2')

for i in range(101, 115):
    idea = f'idea_{i:03d}'
    runs_dir = Path(idea) / 'runs'
    ckpt_path = runs_dir / 'best.pt'
    
    if not ckpt_path.exists():
        with open(LOG_DIR / f'{idea}.log', 'a') as f:
            f.write(f'\n--- Training {idea} ---\n')
            f.flush()
            subprocess.run(['python3', f'{idea}/train.py', '--dataset_path', DATA, '--output_dir', f'{idea}/runs', '--epochs', '1000', '--patience', '20'], 
                           stdout=f, stderr=subprocess.STDOUT)
    
    if ckpt_path.exists():
        with open(LOG_DIR / f'{idea}.log', 'a') as f:
            f.write('\n--- MEANINGFUL EVAL (TEST) ---\n')
            f.flush()
            subprocess.run(['python3', '-m', 'phase2_tdqc.eval_tdqc', '--dataset_path', TEST_DATA, '--ckpt', 'runs/best.pt'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=idea)
            
            f.write('\n--- MEANINGFUL EVAL (OOD) ---\n')
            f.flush()
            subprocess.run(['python3', '-m', 'phase2_tdqc.eval_tdqc', '--dataset_path', OOD_DATA, '--ckpt', 'runs/best.pt'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=idea)
