# Stage 9 Contact Check

Contact access: available through MuJoCo `sim.data.contact`.

Finding: LIBERO scenes have many persistent floor-object contacts at rest, so raw floor/table contact count falsely labeled every controlled action as BAD in rule v1.

Fix applied: rule v2/v3 treat contact count as diagnostic evidence only. It is not used as a strong BAD label until new robot/wrong-object collision contacts can be separated from static resting contacts.

Decision: contact is available but not trusted as a strong label source yet.
