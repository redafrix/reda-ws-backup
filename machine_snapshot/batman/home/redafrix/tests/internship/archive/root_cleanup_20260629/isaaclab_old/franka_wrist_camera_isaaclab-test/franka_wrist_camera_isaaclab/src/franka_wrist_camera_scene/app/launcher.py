"""Isaac Sim and pxr compatibility patches and launcher setup."""

from __future__ import annotations

import sys
import types

# Compatibility layer for Isaac Sim 6.0 (redirects omni.physics.tensors.impl.api -> omni.physics.tensors.api)
class LazyApiModule(types.ModuleType):
    def __getattr__(self, name):
        import sys
        try:
            import omni.physics.tensors.api as api
            return getattr(api, "DeformableBodyView" if name == "SoftBodyView" else name)
        except ImportError:
            self_name = self.__name__
            self_module = sys.modules.pop(self_name, None)
            try:
                import omni.physics.tensors.impl.api as impl_api
                return getattr(impl_api, name)
            finally:
                if self_module is not None:
                    sys.modules[self_name] = self_module

    def __dir__(self):
        import sys
        try:
            import omni.physics.tensors.api as api
            return dir(api)
        except ImportError:
            self_name = self.__name__
            self_module = sys.modules.pop(self_name, None)
            try:
                import omni.physics.tensors.impl.api as impl_api
                return dir(impl_api)
            finally:
                if self_module is not None:
                    sys.modules[self_name] = self_module


# Apply sys.modules patches immediately when this module is imported, only if we are not on Isaac Sim 4.5 (where impl.api already exists)
is_isaac_sim_4_5 = False
try:
    import isaacsim
    import os
    version_path = os.path.abspath(os.path.join(os.path.dirname(isaacsim.__file__), "../../VERSION"))
    if os.path.isfile(version_path):
        with open(version_path) as f:
            ver = f.readline().strip()
            if ver.startswith("4.5"):
                is_isaac_sim_4_5 = True
except Exception:
    pass

if not is_isaac_sim_4_5:
    if "omni.physics.tensors.impl.api" not in sys.modules:
        sys.modules["omni.physics.tensors.impl.api"] = LazyApiModule("omni.physics.tensors.impl.api")
    if "omni.physics.tensors.impl" not in sys.modules:
        sys.modules["omni.physics.tensors.impl"] = types.ModuleType("omni.physics.tensors.impl")





def patch_physx_schema() -> None:
    """Apply pxr.PhysxSchema patch for compatibility after SimulationApp is started."""
    from pxr import PhysxSchema
    if not hasattr(PhysxSchema, "PhysxDeformableBodyAPI"):
        PhysxSchema.PhysxDeformableBodyAPI = PhysxSchema.PhysxRigidBodyAPI

    # Patch PhysxCfg to filter out unsupported arguments on older Isaac Lab versions
    try:
        from isaaclab.sim import PhysxCfg
        import dataclasses

        orig_init = PhysxCfg.__init__

        def new_init(self, *args, **kwargs):
            valid_fields = {f.name for f in dataclasses.fields(PhysxCfg)}
            filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_fields}
            orig_init(self, *args, **filtered_kwargs)

        PhysxCfg.__init__ = new_init
    except Exception as e:
        print(f"Failed to patch PhysxCfg: {e}")

