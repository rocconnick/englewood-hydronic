# 05 — Active fault: second-floor radiant circulator

**Diagnostic rule:** Voltage across connected TELESTAT R1/R2 is a clue about the feedback circuit. It cannot establish end-switch closure or determine whether the ZCM is faulty. Both upstairs inputs dropped to 0 VAC on a call even though their isolated valve end switches read OL. Verify closure independently, then assess the module by its ES output and the corresponding DuoMix demand response with verified feedback applied.

**Current diagnosis:** Both upstairs valves moved on a call but their isolated end switches stayed OL. The working Living Room switch showed continuity during demand. Inspect valve travel and switch actuation first. ZCM-2 replacement is deferred until its response to valid feedback can be checked.

## Symptom
[USER] Rest of Second Floor thermostat calls for heat; the corresponding ZCM-2 radiant zone control module yellow indicator illuminates, but DuoMix LCD shows no visible response and **Mix 2 mixed-water circulator does not receive 120 V at DuoMix terminal 8** under test conditions. By contrast, a first-floor call produces **120 V at Mix 1 mixed-water circulator terminal 12**. Do not extrapolate voltage readings to other conditions; the meter reference, time since call, and settings were not logged.

## What is actually established
1. Thermostat call correlates with lower radiant zone control module zone-1 yellow indicator.
2. At least some electrical path reaches or affects the radiant zone control module; LED meaning not independently verified.
3. Mix 2 mixed-water circulator switched-hot output was not active when checked; this does not by itself prove DuoMix fault.
4. Mix 1 output is capable of energizing during a different zone call.
5. No visible LCD change was reported; display interpretation remains unverified.
6. The Yellow Room's 17/20 conductors are supply sensor, **not Mix 2 demand**.

## Fault tree (unverified branches)
- Missing demand at DuoMix 3–4: board OUTPUT issue, upstream external relay/contact, Honeywell valve end switch (if used), loose wire, staging control.
- Demand reaches DuoMix but output inhibited: control logic, sensor/outdoor conditions, settings, pump protection, internal relay failure.
- Apparent failure due to test conditions: time delay, sensor state, incomplete thermostat call, wrong meter reference, wrong assumed output.

## Test plan (visual/non-invasive first)
1. Photograph DuoMix **3–4** and follow each conductor physically to source. Record cable IDs and terminal labels.
2. Photograph external relay part numbers and all terminals; trace contacts versus coils with power safely isolated and qualified assistance.
3. Identify Honeywell valve model and observe mechanical position during sustained call; trace any end-switch wires.
4. Document the right-side OUTPUT labels and wires on ZCM-2 (installed part **A303XX0003**). Locate manufacturer's instructions before electrical testing.
5. Record all indicators and DuoMix display during controlled, sustained upstairs demand; note elapsed minutes and room/pipe temperatures.
6. If professionally tested, compare actual state of DuoMix 3–4 with active call to determine upstream versus controller-side fault; never short terminals or inject voltage without confirmed manufacturer instructions.

## Prior service clue
[USER] Replacement Wirsbo zone-controller box contained handwritten note **“no output on zone 3.”** Board/date/author and meaning of output unknown. Current problem is **lower radiant zone control module zone 1**, so the note is context, not diagnosis. Whether a removed board is in box was asked but not answered.

## 2026-11-07: simultaneous upstairs zone demand (new photographs)
[USER] Both upstairs zones (Rest of Second Floor and Bedroom Above Garage) calling at once. [OBSERVED PHOTO] ZCM-2 radiant zone control module has two illuminated amber LEDs adjacent to printed TELESTAT legends, one for each active zone; green 24V LED illuminated. [OBSERVED PHOTO] DuoMix 201 LCD reads `OPEN` with upper item text not confidently transcribed. User reports neither upstairs call appears as a Mix 2 demand on DuoMix. This **does not prove** whether terminals 3–4 are open, or what `OPEN` refers to; it may be a selected diagnostic/menu value rather than a global demand status. Do not assume amber LEDs prove valve position or contact closure. Photos: `../photos/IMG_81CD45AE-2742-4ED7-989A-802AA7705E40.jpeg` (DuoMix) and `../photos/IMG_3FA9E00D-211B-43EB-838B-A3E298D1D1E3.jpeg` (Wirsbo). Next discriminator: identify wires and verified electrical state of DuoMix Mix 2 Demand 3–4 under simultaneous call; separately determine what display item shows OPEN.

## 2026-11-07 — Major diagnostic breakthrough: comparative ES voltage
Using a **multimeter set to V~ (AC)**, the homeowner measured **directly across the two ES terminals** on each radiant zone control module:

| Controller | Condition | Across ES/ES |
|---|---|---:|
| Upper (working Mix 1) | No first-floor call | **27.2 VAC** |
| Upper (working Mix 1) | One first-floor zone calling | **~1 VAC** |
| Lower (suspect Mix 2) | Both upstairs zones calling | **27.2 VAC** |
| Lower (suspect Mix 2) | Both upstairs zones satisfied | **27.2 VAC** |

**Voltage interpretation:** These are AC voltage readings across the two ES terminals with the circuit connected. ZCM-1 dropping from 27.2 VAC to about 1 VAC is consistent with its contact closing. ZCM-2 retaining 27.2 VAC during the call shows the terminals did not come to nearly the same potential. In the traced demand circuit, that is consistent with an open or high-resistance ES path. The reading alone cannot distinguish a relay that was never commanded from a failed contact or a wiring fault, or establish what MC-1 sees across terminals 3 and 4.

**Unverified causes:** Missing actuator travel or end-switch feedback, an external interlock or wiring fault, or a fault in the ZCM-2 ES relay or associated circuitry. The installed A303XX0003 activation sequence remains unverified.

**Traced wiring:** Upper ES brown -> DuoMix 1; lower ES upper red -> DuoMix 3; lower ES lower white -> upper radiant zone control module -> apparent 24 VAC transformer; DuoMix 2 and 4 tied together. ES terminals are **not** the separate OUTPUT terminals.

**[USER] Yellow Room call:** The initial closed-valve observation was made after the call had stopped. On a renewed call, the homeowner heard the valve operate and saw it move toward open. This supports actuator drive reaching the valve. On recheck during the same call, yellow remained lit, lower red stayed off, and the valve still felt open. Photo confirms Honeywell V8043E1061, normally closed, with two yellow motor leads and two red end-switch leads. Full travel, red-lead switch closure, feedback routing, and concurrent ES voltage remain unverified.

**[USER] Yellow Room feedback wiring:** At the Honeywell V8043E1061, the two red end-switch leads splice to green and yellow conductors in one brown-jacketed thermostat cable. A matching green/yellow pair lands on the Yellow Room lower TELESTAT R1/R2 terminals at ZCM-2. End-to-end cable identity, individual color-to-terminal assignment, and contact closure remain unverified. The valve motor has its own separate pair of yellow leads.

**[USER] Yellow Room R1/R2 measurement:** 11 VAC (meter on V~) across the lower TELESTAT R1/R2 screws on ZCM-2 with the green and yellow feedback wires connected. During the reading, yellow remained lit, red remained off, and the valve had finished moving. Full mechanical travel and end-switch closure remain unverified.

**[USER] Working ZCM-1 comparison:** Across a main-floor zone’s lower TELESTAT R1/R2, the homeowner repeatedly measured about 7.5 VAC while satisfied. At call onset with yellow lighting, voltage briefly rose, then fell to approximately 0 VAC as the red LED lit. This is consistent with the end-switch path closing and bringing R1/R2 to nearly the same potential. The observation does not distinguish contact closure from any coincident change in the board’s sensing voltage.

**[USER] All thermostats satisfied:** ZCM-1 lower TELESTAT R1/R2 measured 7.68 VAC on all three zones. ZCM-2 measured 0 VAC on Yellow Room and Rest of Second Floor and 11 VAC on the spare zone, which has no thermostat connected. Yellow Room therefore measured 0 VAC idle and 11 VAC on a sustained call with red off. The spare reading is from a different channel and does not establish continuity to the Yellow Room valve. The reason for the differing idle voltages remains unverified.

**[USER] Rest of Second Floor call:** Across ZCM-2 lower TELESTAT R1/R2 screws read 0 VAC while satisfied, then rose to 8.8 VAC when yellow lit. The reading held at the 15-second check and remained unchanged before the homeowner went upstairs. Red LED state and valve travel during this call remain to be confirmed.

**[USER] Rest of Second Floor follow-up:** Valve observed open upstairs. About 8 VAC persisted across the ZCM-2 lower TELESTAT R1/R2 screws after returning downstairs, while probing the exposed copper of the two conductors entering those terminals gave 0 VAC. The homeowner found neither conductor loose and saw bare copper entering both ports. Verify probe contact and terminal clamping before interpreting the discrepancy as a wiring or board fault.

**[USER] Rest of Second Floor later reading:** With the meter back on V~, R1/R2 initially read 8.8 VAC across the screws, then fell to 0 VAC across both the screws and the exposed conductors. Yellow remained lit through the drop and red remained off. Valve position at the instant of the drop was not confirmed.

**[USER] ES output comparison:** During the Rest of Second Floor test sequence, ZCM-2 ES measured about 27 VAC across both the screws and their corresponding conductors (corrected reading). While Master Bath called on ZCM-1, its yellow and red indicators were on and its ES measured about 1 VAC. MC-1 indicated Mix 1 demand and no Mix 2 demand. ZCM-2 R1/R2 had previously fallen to 0 VAC with yellow on and red off. These observations support a missing ZCM-2 ES transition. An isolated end-switch test is still needed to verify the feedback presented to ZCM-2.

**[USER] Repeat R1/R2 cycle:** About 9 VAC during the call, about 9 VAC immediately after satisfying it, then 9.8 VAC. On renewed demand, the reading held near 9 VAC before falling to 0 VAC. The red LED never lit. This repeats the voltage drop during demand. Contact closure and the exact cause of the drop remain unverified.

**[USER] Yellow Room repeat cycle:** With the zone satisfied, lower TELESTAT R1/R2 measured 10.69 VAC. During the renewed call, yellow lit and voltage held near 10.3 VAC before dropping to 0 VAC, confirmed at both the exposed conductors and the screws. Red stayed off. This matches the delayed drop and dark red LED seen on Rest of Second Floor. The satisfied reading differs from the earlier 0 VAC observation. During this call, ZCM-2 ES measured about 27 VAC. End-switch closure has not been independently verified.

**[USER] Yellow Room isolated valve end-switch test:** Honeywell V8043E1061 red leads disconnected from the green/yellow feedback cable at the valve. On a renewed call, the valve visibly reopened, with 0.11 VAC and OL across the isolated red leads. After satisfying the call, the pair read 0 VAC and OL. No end-switch closure was observed directly at the valve. Full travel and switch actuation remain unverified. See the separate Rest of Second Floor isolated test below.

**[USER] Rest of Second Floor isolated valve end-switch test:** At the valve, the isolated end-switch pair measured 0 VAC and OL while satisfied. On a renewed call the valve appeared fully open, but the pair still measured 0 VAC and OL. After satisfying the call, the homeowner felt the valve close and reported 0 VAC throughout. Neither upstairs valve produced a measured end-switch closure at the valve. Check end-switch actuation or travel before ordering ZCM-2.

**[USER] Working Living Room isolated end-switch comparison:** The valve end-switch pair read about 0 VAC in both states. Resistance was OL while satisfied and showed continuity on a call. This verifies that the test setup detects closure on a working zone. Both upstairs valves remained OL after opening, making valve-side end-switch actuation or travel the priority. ZCM-2 operation with valid feedback remains unverified. Defer board replacement pending valve-side diagnosis.

**[USER] Additional ZCM-1 comparison:** Master Bath calling with valve open and about 0 VAC at TELESTAT R1/R2. Master Bedroom was satisfied while its switch also appeared closed. The exact contact referred to as the M switch and the method used to establish closure remain unverified. Yellow Room was satisfied and its valve was closed.

**Next observation:** During a sustained upstairs call, record whether the red indicator stays off, flashes, or goes solid and whether the corresponding actuator opens. Compare with ZCM-1. Identify the actuator model and trace any feedback wiring. Verify the installed board’s indicator meanings before using them to distinguish missing feedback from a fault in the ES switching path.

**Replacement:** Uponor A3031003 remains an unverified candidate. Before ordering, confirm compatibility with the installed thermostats, actuators, ES demand circuit, ZCM-1 interconnection and mounting.

**Meter correction:** Earlier assistant misread multimeter photograph as DC; homeowner confirmed the original 27.2 V readings were taken with the **AC squiggle** selected.

## Active issue B — Upstairs/attic Lennox AM30 air-handler pump
- [USER, 2026-11-07] Homeowner reports a **bad pump on the upstairs (attic) Lennox AM30 hydronic air handler**. This is a separate active issue from the Mix 2 mixed-water circulator fault.
- [UNKNOWN] Symptoms, failure mode, whether seized/failed electrically, supply voltage, control demand, isolation valves, and whether it is hydronic coil circulation or another function.
- [DO NOT CONFLATE] The upstairs AM30 air-handler hydronic circulator is **not assumed to be** DuoMix Mix 2 Pmp (terminal 8), Var 2 Pmp (terminal 10), or Taco 008-BC6 until physically traced.
- [NEXT] Record the full AM30 cabinet model and serial number, document precise symptoms, determine which thermostat stage calls it, trace its supply/control, and identify safe service/replacement options.

### AHU-2 cartridge identification and availability

- [PHOTO] Homeowner photo `55573.jpg` identifies the upstairs AM30 circulator as Taco **006-B4-11**, rated 115 V, 60 Hz, 1/40 hp. Pump failure and its cause remain unverified.
- [TACO] The exact **006-B4-11** row specifies cartridge assembly **006-040RP** and casing O-ring **007-003RP**. Current stock and an approved supersession were not verified. SupplyHouse explicitly excludes the **006-B4-11** from its **005-020RP** fitment list. [Taco parts list](https://www.tacocomfort.com/documents/FileLibrary/104-110.pdf) · [SupplyHouse listing](https://www.supplyhouse.com/Taco-005-020RP-Taco-Pump-Replacement-Cartridge-TAC005-020RP-for-005-006-Bronze-and-Stainless)
- [LENNOX] Table 6 lists the original-equipment cartridge kits by air-handler model. **AM30-40 and AM30-70** use **99K70 (99K7001)**. **AM30-90, AM30-105 and AM30-120** use **73J77 (73J7701)**. The photographed attic cabinet AM30Q2-40-2 falls in the AM30-40 group, making 99K70 the Lennox catalog match. A direct manufacturer cross-reference from **006-040RP** to either kit has not been verified. [Lennox service manual](https://www.hvacpartsshop.com/content/lennox-furnace-manuals/HM30-AM30%20Series.pdf) · [LennoxPros catalog](https://www.lennoxpros.com/parts-and-supplies/installation-supplies/pumps/pump-parts/c/p201)
- [SOURCING] Parts Town lists **99K70**, with live stock unconfirmed. Use the confirmed attic cabinet model AM30Q2-40-2 and serial 5801K48409 plus the pump nameplate to check kit fit, stock and any supersession with a Lennox dealer. [Parts Town listing](https://www.partstown.com/p/lennox/len99k70)
