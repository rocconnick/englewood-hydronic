# 06 — Prioritized open questions

## P0: directly relevant to no Mix 2 circulation
1. **DuoMix Mix 2 terminal 3 is now traced to ZCM-2 ES (red).** Trace remaining shared return (DuoMix 2/4) and transformer-side ES wiring.
2. **What are the six black relay modules?** Read maker/model, pin labels, coil voltage and contacts; which zone controls each?
3. Verify the Yellow Room feedback cable end to end and trace motor wiring. Read the other valve nameplates and map their feedback leads.
4. **What do the separate right-hand OUTPUT terminals mean?** They are distinct from ES/ES. Identify their function, wiring and relationship to ES switching.
5. Determine why the two upstairs valve switches remain open after apparent opening. Then check ZCM-2 ES and Mix 2 demand with verified feedback.

## P1: clarify operating logic
6. Verify full mechanical travel and switch actuation on both upstairs valves. Both moved on a call, but both isolated switches stayed OL.
7. Where does thermostat wiring go first: external relay, Wirsbo, MABS or other staging hardware?
8. What are the exact radiant zone control module and relay model numbers, and their manufacturer diagrams?
9. Where is the **DuoMix 201** installation/service manual? What are LCD `OPEN`, pump icons, Mix2 demand indicators, and lockouts?
10. Mix 2 is the Taco 008-BC6 and flows right to left in the attic plumbing-wall photo. Var 2 flows upward. Confirm the apparent Taco 008-BC6 model on the glare-obscured nameplate.
11. Does the Yellow Room heat normally? Does its call light zone 2, open valve, and start Mix2?
12. Does the spare channel have any connected relay/valve? Was zone 3 historically reassigned?

## P2: complete system as-built
13. Map five air thermostats plus Master Bath floor thermostat to six radiant zones.
14. Does stage 2 forced air retain stage 1 radiant? Identify MABS board role and air-handler interlocks.
15. Locate manifolds, loops, zone valves, isolation valves, purge points, expansion tank, gauges and checks.
16. Capture both Polaris and both Lennox nameplates, serials, ages, temperatures and service records.
17. Confirm the likely SUP 1 connection from the Mix 1 inlet probe and verify the likely BRet connection to the common return probe behind the Grundfos. The outdoor sensor is out back by the air conditioners. Verify its likely connection to terminal 26 (Out), and verify calibration. SUP 2 is under the insulation immediately upstream of the Mix 2 inlet.
18. Compare photographed **proposed** piping diagram against actual installation, especially Garage Entry omitted.
19. Identify which board was replaced historically and inspect box, handwritten note and any removed board.
20. Document how a basement radiant call affects the Polaris heat source.
21. The basement is a single radiant zone controlled by turning its dedicated Taco on and off. A basement-only call does not start MC-1 or the Grundfos.
22. Verify pump cartridge compatibility and replacement plan from nameplate and Taco reference.

## Capture discipline
Every new finding should include **photo filename, visible terminal markings, cable ID, date, thermostat setpoint, elapsed time, voltage meter points (if professionally measured), and evidence status**. Record alternative interpretations instead of silently replacing them.

- **New simultaneous-call observation:** determine what DuoMix LCD item is showing `OPEN`, and whether Mix 2 Demand input 3–4 is actually asserted while both upstairs zones are calling.

## Priority following comparative ES test
- Inspect the upstairs powerheads and verify full travel. Yellow Room is confirmed V8043E1061. Read the Rest of Second Floor nameplate separately.
- Determine whether ZCM ES closure depends on valve end switch, board output, delay, or other interlock.
- Trace upper radiant zone control module's transformer-side ES wire and DuoMix 2/4 common path.

## P0 — Separate attic AM30 air-handler hydronic circulator issue
- The pump nameplate identifies Taco **006-B4-11**. The cabinet nameplate identifies AM30Q2-40-2, serial 5801K48409. Verify 99K70 kit fit and availability. See the [cartridge crosswalk](05-troubleshooting.md#ahu-2-cartridge-identification-and-availability).
- What evidence identifies it as bad (noise, no flow, temperature difference, electrical test, prior technician diagnosis)?
- What starts it and where is its relay/control located?
- How is this pump isolated and serviced? Are replacement parts available?
