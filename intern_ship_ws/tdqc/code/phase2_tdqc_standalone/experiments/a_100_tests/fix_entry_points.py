import os
from pathlib import Path

base_dir = Path('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests')
for i in range(200, 250):
    train_path = base_dir / f'idea_{i}' / 'phase2_tdqc' / 'train_tdqc.py'
    if train_path.exists():
        with open(train_path, 'r') as f:
            content = f.read()
        if "if __name__ == '__main__':" not in content:
            with open(train_path, 'a') as f:
                f.write("\nif __name__ == '__main__':\n    main()\n")
            print(f'Fixed {train_path}')
