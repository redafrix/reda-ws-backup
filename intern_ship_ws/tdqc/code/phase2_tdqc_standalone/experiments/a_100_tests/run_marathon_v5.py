import subprocess, os
from pathlib import Path

BASE_DIR = Path('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/')
DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
TEST_DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_test.pt'
OOD_DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt'
LOG_DIR = BASE_DIR / 'logs_marathon_v5'
LOG_DIR.mkdir(exist_ok=True)

for i in range(133, 135):
    idea_name = f'idea_{i}'
    idea_path = BASE_DIR / idea_name
    runs_dir = idea_path / 'runs'
    ckpt_path = runs_dir / 'best.pt'
    log_file = LOG_DIR / f'{idea_name}.log'
    
    with open(log_file, 'w') as f:
        f.write(f'=== STARTING {idea_name} ===\n')
        f.write(f'Path: {idea_path}\n')
        f.write(f'Files: {os.listdir(idea_path)}\n')
        f.flush()
        
        if not ckpt_path.exists():
            f.write(f'--- Training ---\n')
            f.flush()
            # Use absolute path to the script
            script_path = idea_path / 'train.py'
            res = subprocess.run(['python3', '-u', str(script_path), '--dataset_path', DATA, '--output_dir', str(runs_dir), '--epochs', '1000', '--patience', '20'], 
                           stdout=f, stderr=subprocess.STDOUT)
            f.write(f'Training exited with code {res.returncode}\n')
            f.flush()
    
        if ckpt_path.exists():
            f.write('\n--- MEANINGFUL EVAL (TEST) ---\n')
            f.flush()
            subprocess.run(['python3', '-u', '-m', 'phase2_tdqc.eval_tdqc', '--dataset_path', TEST_DATA, '--ckpt', 'runs/best.pt'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=str(idea_path))
            
            f.write('\n--- MEANINGFUL EVAL (OOD) ---\n')
            f.flush()
            subprocess.run(['python3', '-u', '-m', 'phase2_tdqc.eval_tdqc', '--dataset_path', OOD_DATA, '--ckpt', 'runs/best.pt'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=str(idea_path))
