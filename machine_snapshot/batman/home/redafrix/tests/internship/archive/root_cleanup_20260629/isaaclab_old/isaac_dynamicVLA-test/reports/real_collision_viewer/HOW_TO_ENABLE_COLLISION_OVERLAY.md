# How to inspect collision meshes in Isaac GUI

Open stage:
`/home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/real_collision_viewer/dom_collision_viewer_stage.usd`

Goal:
Compare visible mesh and physics/collision shape.

In Isaac Sim / Omniverse GUI:

1. Open the stage.
2. Select an object under:
   `/World/Objects/...`
3. Enable physics/collision visualization.
   Look for the "Physics" menu or the eye icon in the viewport:
   - Physics > Show > All Colliders
   - Viewport Overlay (Eye icon) > Physics > Colliders
4. Use wireframe/transparent mode if available to see the collision mesh inside the visual mesh.
5. Rotate around each object.
6. Check:
   - Does the collider tightly follow the visible object?
   - Is it only a box/sphere/capsule?
   - Is it too small/too large?
   - Is it shifted from the visual mesh?
   - For bowls/cups/trays: does the open/hollow geometry collide correctly?
   - For bottles/cans: is the cylinder close enough?
   - For boxes/trays: are edges/corners correct?

Important:
Static audit labels:
- EXACT_OR_SHARED_MESH_LIKELY: collision probably same as visible mesh.
- BBOX_MATCH_BUT_SIMPLIFIED_COLLISION: collision is simplified but bbox matches.
- ROUGH_PRIMITIVE_COLLISION: risky, inspect carefully.
- BAD_BBOX_MISMATCH: likely bad, avoid or fix.

Best first objects to inspect:
- bowl/bowl04.usd
- bowl/bowl17.usd
- tray/tray05.usd
- box/box00.usd
- cup/cup05.usd
- bottle/dbottle04.usd
- can/fcan05.usd
- kiwi/kiwi05.usd
- lime/lime03.usd
- tomato/tomato02.usd
