# 10 — Work session handoff and update workflow

## Suggested initial instruction for ChatGPT Work
> Unpack this ZIP, read README.md, INDEX.md and all Markdown notes, inspect every photo in photos/, and treat this as the current Englewood Rd. heating system knowledge base. Distinguish observed facts from hypotheses. Do not assume an as-built circuit unless traced. Help identify the ZCM-2 OUTPUT circuit, the external black relay models, Honeywell valve wiring and DuoMix Mix 2 Demand 3–4 path. Maintain the Markdown files and image catalog as discoveries are made, and package a new version for export when requested.

## Work priorities
1. Resolve Mix 2 demand wiring with original photographs and new close-ups.
2. Identify external relay pinout and Honeywell valve/end-switch wiring.
3. Find **correct DuoMix 201 A3030005** manual and zone-board documentation, not similarly named proMix.
4. Develop verified as-built schematic and cable schedule.
5. Update the master reference with confidence tags and test log.

## Template for each field observation
```markdown
### YYYY-MM-DD HH:MM — observation title
- Zone / thermostat / setpoint:
- Equipment, terminal IDs and wire colors:
- What was directly seen:
- Meter reading (if any): meter points, AC/DC, value, elapsed time:
- Photo filename:
- Interpretation [INFERENCE]:
- Alternative explanation:
- Follow-up:
```

## Files and portability
Keep relative links stable. Never overwrite original photos; add annotated derivatives separately. Update `MANIFEST.tsv` when assets change. This bundle is portable but does not automatically migrate the original ChatGPT conversation's exact messages or private Project state into Work.

## As-built capture plan

Survey scope covers plumbing and main system controls through the Lennox AM30 units. Downstream ductwork and damper tracing are deferred.

1. Start with two overlapping wide photos of the mechanical room from opposite angles. Include the Polaris tanks and nearby pipe branches.
2. Trace supply and return by branch. Cover basement radiant, Mix 1, Mix 2, and both AM30s. Photograph pump nameplates, flow arrows, mixing valves, and points where pipes disappear.
3. Map pump and valve cables to their boards and terminals. Distinguish the Mix 2 circulator, Var 2 injection pump, Taco 008-BC6, and attic AM30 Taco 006-B4-11.
4. Observe a working radiant call and a forced-air call. Record thermostat, valve, ZCM, DuoMix, relay and pump changes. Keep unresolved MABS and staging links visible.

Use the same equipment labels on the plumbing map, controls map and zone table. Mark each link observed, traced or unresolved. Use the proposed piping drawing for orientation and field observations for the as-built map.
