from pxr import Usd, UsdGeom
import sys

stage = Usd.Stage.Open("objects/apple/apple01.usd")
print("--- USD Info ---")
for prim in stage.Traverse():
    if prim.GetTypeName() in ("Mesh", "Xform", "PhysicsCollisionGroup"):
        print("Prim:", prim.GetPath(), "Type:", prim.GetTypeName())
        xform = UsdGeom.Xformable(prim)
        if xform:
            print("  Local Transformation Ops:", xform.GetOrderedXformOps())
            for op in xform.GetOrderedXformOps():
                print(f"    Op {op.GetOpName()}: {op.Get()}")
        geom = UsdGeom.Gprim(prim)
        if geom:
            print("  Extent:", geom.GetExtentAttr().Get())
