import subprocess, os
from pathlib import Path

DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
TEST_DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_test.pt'
OOD_DATA = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt'
LOG_DIR = Path('logs_marathon_v5')
LOG_DIR.mkdir(exist_ok=True)

for i in range(125, 135):
    idea = f'idea_{i}'
    runs_dir = Path(idea) / 'runs'
    ckpt_path = runs_dir / 'best.pt'
    log_file = LOG_DIR / f'{idea}.log'
    
    if log_file.exists():
        log_file.unlink()
        
    with open(log_file, 'w') as f:
        f.write(f'=== STARTING {idea} ===\n')
        f.flush()
        
        if not ckpt_path.exists():
            f.write(f'--- Training ---\n')
            f.flush()
            res = subprocess.run(['python3', '-u', 'train.py', '--dataset_path', DATA, '--output_dir', 'runs', '--epochs', '1000', '--patience', '20'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=idea)
            f.write(f'Training exited with code {res.returncode}\n')
            f.flush()
    
        if ckpt_path.exists():
            f.write('\n--- MEANINGFUL EVAL (TEST) ---\n')
            f.flush()
            subprocess.run(['python3', '-u', '-m', 'phase2_tdqc.eval_tdqc', '--dataset_path', TEST_DATA, '--ckpt', 'runs/best.pt'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=idea)
            
            f.write('\n--- MEANINGFUL EVAL (OOD) ---\n')
            f.flush()
            subprocess.run(['python3', '-u', '-m', 'phase2_tdqc.eval_tdqc', '--dataset_path', OOD_DATA, '--ckpt', 'runs/best.pt'], 
                           stdout=f, stderr=subprocess.STDOUT, cwd=idea)
