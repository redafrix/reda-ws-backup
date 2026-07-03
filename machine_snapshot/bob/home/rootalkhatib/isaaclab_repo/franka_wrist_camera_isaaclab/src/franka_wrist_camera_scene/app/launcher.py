"""Isaac Sim and pxr compatibility patches and launcher setup."""

from __future__ import annotations


def patch_physx_schema() -> None:
    """Apply pxr.PhysxSchema patch for compatibility after SimulationApp is started."""
    from pxr import PhysxSchema
    if not hasattr(PhysxSchema, "PhysxDeformableBodyAPI"):
        PhysxSchema.PhysxDeformableBodyAPI = PhysxSchema.PhysxRigidBodyAPI
