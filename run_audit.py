import sys
import os
import argparse

ROOT = "/media/rootalkhatib/My Passport/reda_ws"
sys.path.insert(0, os.path.join(ROOT, "asynchvla_ws/src"))
sys.path.insert(0, os.path.join(ROOT, "intern_ship_ws/assets/repos/LIBERO-PRO"))

from data_collection_stage9.collect_counterfactual_dataset import main

if __name__ == "__main__":
    main()
