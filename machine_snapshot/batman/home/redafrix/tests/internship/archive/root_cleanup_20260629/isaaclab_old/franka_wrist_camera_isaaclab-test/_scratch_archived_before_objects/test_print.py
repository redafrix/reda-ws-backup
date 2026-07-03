import argparse
from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser()
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args([])
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

from isaaclab_assets import FRANKA_PANDA_HIGH_PD_CFG
import pprint
pprint.pprint(FRANKA_PANDA_HIGH_PD_CFG.actuators)
