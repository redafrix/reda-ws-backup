import argparse
from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser()
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args(["--headless"])
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

import isaaclab.sim as sim_utils

print("Has MassPropertiesCfg in sim_utils:", hasattr(sim_utils, "MassPropertiesCfg"))
if hasattr(sim_utils, "MassPropertiesCfg"):
    print("sim_utils.MassPropertiesCfg:", sim_utils.MassPropertiesCfg)

print("Has schemas in sim_utils:", hasattr(sim_utils, "schemas"))
if hasattr(sim_utils, "schemas"):
    print("Has MassPropertiesCfg in schemas:", hasattr(sim_utils.schemas, "MassPropertiesCfg"))
    if hasattr(sim_utils.schemas, "MassPropertiesCfg"):
        print("sim_utils.schemas.MassPropertiesCfg:", sim_utils.schemas.MassPropertiesCfg)
