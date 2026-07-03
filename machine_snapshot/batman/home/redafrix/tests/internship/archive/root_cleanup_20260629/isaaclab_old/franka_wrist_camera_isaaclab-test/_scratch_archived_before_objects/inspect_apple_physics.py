import argparse
from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser()
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args(["--headless"])
args_cli.enable_cameras = True
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

import isaaclab.sim as sim_utils
from isaaclab.scene import InteractiveScene
from franka_wrist_camera_scene.scene.tabletop import make_tabletop_scene_cfg
from franka_wrist_camera_scene.scene.object_context import load_catalog_object_context
from pxr import PhysxSchema, UsdPhysics, UsdGeom

sim_cfg = sim_utils.SimulationCfg(dt=0.00833)
sim = sim_utils.SimulationContext(sim_cfg)

object_context = load_catalog_object_context(
    catalog_config="object_catalog.yaml",
    category_id="apple",
    variant_id="apple01",
)
scene_cfg = make_tabletop_scene_cfg(object_context=object_context)
scene = InteractiveScene(scene_cfg)

sim.reset()

# Get the prim path of the TargetCube
prim_path = "/World/envs/env_0/TargetCube"
stage = sim.stage
prim = stage.GetPrimAtPath(prim_path)

print("--- Prim Info ---")
print("Prim Path:", prim_path)
print("Is valid:", prim.IsValid())
print("Prim Type:", prim.GetTypeName())

# Check physics schemas
has_rigid = prim.HasAPI(UsdPhysics.RigidBodyAPI)
has_collision = prim.HasAPI(UsdPhysics.CollisionAPI)
print("Has UsdPhysics.RigidBodyAPI:", has_rigid)
print("Has UsdPhysics.CollisionAPI:", has_collision)

# Check custom properties
rb_api = UsdPhysics.RigidBodyAPI(prim)
if has_rigid:
    for attr in rb_api.GetSchemaAttributeNames():
        print(f"UsdPhysics.RigidBodyAPI Attribute {attr}: {prim.GetAttribute(attr).Get()}")
    physx_rb = PhysxSchema.PhysxRigidBodyAPI(prim)
    if physx_rb:
        for attr in physx_rb.GetSchemaAttributeNames():
            print(f"PhysxSchema.PhysxRigidBodyAPI Attribute {attr}: {prim.GetAttribute(attr).Get()}")

# Print initial velocities and properties from UsdPhysics
for prop in prim.GetProperties():
    name = prop.GetName()
    if "velocity" in name.lower() or "gravity" in name.lower():
        print(f"Property {name}: {prop.Get()}")

# Let's run a few simulation steps and print the pose and velocity of the object from its RigidObject data
obj = scene["target_cube"]
for i in range(5):
    sim.step()
    scene.update(0.00833)
    pos = obj.data.root_pos_w[0].cpu().numpy()
    vel = obj.data.root_vel_w[0].cpu().numpy()
    print(f"Step {i}: pos={pos}, vel={vel}")
