# 03 — Controls and terminal reference

## First-floor Living Area thermostat terminal colors

[PHOTO, 2026-11-08] Google-branded thermostat base connections: **Y: yellow; C: blue; W: white; G: green; R: red; */OB: brown**.

[USER CONFIRMED, 2026-11-08] This is the first-floor Living Room / Living Area thermostat serving the main part of the first floor. The earlier reference to second floor was corrected by the homeowner. This zone is mapped to basement MABS EZ-4 Zone 1 and the ZCM-1 Living Area channel; individual conductor routes remain unverified.

[APP SCREENSHOT, 2026-11-08] Google Home identifies Nest Thermostat, 1st generation, and assigns Y Cool, C 24v common, W Heat, G Fan, R Power, and */OB Heat 2. Thus white is configured for first-stage heat and brown for second-stage heat at the thermostat. This supersedes the earlier uncertainty about */OB configuration.

[INFERENCE] A split-stage arrangement is consistent with the existing system: white W could operate the external relay/ZCM-1 radiant path, while brown Heat 2 could land on MABS Zone 1 W to request forced-air heat. The MABS zone input strip is L/G/Y/R/W, not separate W1/W2 inputs; its equipment W1/W2 terminals are a different interface. The board photo supports green/yellow/red at Zone 1 G/Y/R, but wire congestion prevents confirming the heating conductor and complete cable identity. C/common routing also remains unverified. Do not describe all six conductors as a confirmed direct thermostat-to-MABS connection.

[LIMIT] Color matching aids tracing but does not prove remote endpoints or staging. Thermostat configuration confirms the requested functions, not the installed destination of either heating-stage conductor.

See [photo](08-photo-catalog.md#first-floor-living-area-thermostat-terminal-colors).

## Wirsbo DuoMix 201
[PHOTO] Faceplate identifies **Wirsbo DuoMix 201**, part **A3030005**, made by tekmar, March 1999. **Do not conflate with Wirsbo proMix 201, proMix 212, or tekmar 374.** Homeowner's older research note speculated a tekmar 374 relationship, but that is unresolved and may apply to a different product. A bundled tekmar cross-reference covers proMix models and is not proof for DuoMix 201.

| Terminal(s) | Printed label | Evidence / note |
|---|---|---|
| 1–2 | Mix 1 Demand | Input; source not traced |
| 3–4 | Mix 2 Demand | Input; **highest-priority wiring trace** |
| 5–6 | Boiler Enable | [USER TRACE] Cabinet 120 VAC supply black hot lands on 6. Terminal 5 sends switched hot to the Grundfos main-loop circulator. The white conductor in the pump conduit returns directly to the incoming supply neutral splice. |
| 7 N, 8 Mix2 Pmp | Mix 2 mixed-water circulator | [MEASURED] no 120 V at terminal 8 on upstairs call; measurement reference undocumented |
| 9 N, 10 Var2 Pmp | Mix 2 variable injection pump | Activity unknown |
| 11 N, 12 Mix1 Pmp | Mix 1 circulation pump | [MEASURED] 120 V at terminal 12 on first-floor call |
| 13 N, 14 Var1 Pmp | Mix 1 variable injection pump | Activity unknown |
| 15 N, 16 L | 120 V supply | [PHOTO] labels |
| 23 Sup1 | Supply 1 pipe temperature sensor | Likely the probe just upstream of Mix 1. Blue sensor leads splice to red and white in a brown thermostat cable. Red is visible at SUP 1. End-to-end cable identity and white termination remain unverified. |
| 17 COM, 20 SUP 2 | Supply 2 pipe temperature sensor | [USER] brown + blue conductors from Yellow Room brown-sheathed cable; attic sensor leads carry a tekmar 071 tag and enter the insulation just upstream of Mix 2 |
| 18, 19 | Zo2, Ret2 | Printed labels. |
| 21, 22 | Com, Zo1 | Printed labels. |
| 24, 27 | Com, tN2 | Printed labels. Field endpoints remain to be traced. |
| 25 BRet | Return temperature input | Likely the common heating return probe behind the Grundfos, downstream of the basement radiant return tee. Cable termination unverified. |
| 26 Out | Outdoor temperature input | Outdoor sensor is out back by the air conditioners. Likely connection to terminal 26, pending an end-to-end trace. |

**Important:** Supply 2 sensor influences Var 2 modulation/temperature regulation; it is not the same as Mix 2 Demand. Calling it a thermocouple is colloquial; exact sensor technology and resistance curve unknown.

**LCD:** [PHOTO] Printed status legends Mix 1 Demand, Mix 2 Demand, Minimum, Maximum, Melting, Idling, CWCO. [PHOTO/USER] display once showed `OPEN` and ambiguous small pump/1/2 symbols. Meaning **not confirmed** against DuoMix manual. No LCD change observed on Rest of Second Floor call.

## radiant zone control modules
- [FIELD-VERIFIED DIAGNOSTIC LIMIT] Voltage across a connected lower TELESTAT R1/R2 pair cannot establish valve end-switch closure or diagnose the ZCM. Both ZCM-2 channels reached 0 VAC during a call while their isolated valve end switches tested open. Verify feedback closure independently, then assess the ZCM by its ES output and the corresponding MC-1 demand response with verified feedback. See [isolated switch tests](05-troubleshooting.md#2026-11-07--major-diagnostic-breakthrough-comparative-es-voltage).
- [USER] The confirmed installed part number for both three-channel radiant zone control modules (ZCM-1 and ZCM-2) is **A303XX0003**.
- [PHOTO] Top four-way THERMOSTAT terminals for each zone marked **R1 R2 Y1 Y2**. Lower four-way TELESTAT terminals. Right-edge **OUTPUT** terminals distinct from both.
- [PHOTO/USER] Yellow/orange indicator at lower radiant zone control module zone 1 lights when Rest of Second Floor calls; green near `24VAC` board power. **Exact LED logic unverified.**
- [CORRECTION] TELESTAT is Wirsbo's name for thermal actuator outputs, but homeowner has **Honeywell motorized zone valves**, not the pictured Wirsbo thermal actuator style. Yellow Room uses a Honeywell V8043E1061 with separate motor and switch circuits. Its likely feedback path terminates at lower TELESTAT R1/R2. See [valve wiring](04-wiring-discoveries.md#honeywell-zone-valves).
- [OPEN] Right-edge OUTPUT electrical type (dry contact vs powered, common vs individual outputs), zone logic, demand aggregation and connected destination.

## Black external components
- [PHOTO] Three per board, relay-like black modules, with numbered screw/spade terminals and wire connections to Wirsbo THERMOSTAT positions. [INFERENCE] Likely relays/interface devices, but model, coil pins, contacts, voltage and purpose unknown. Do not assume they directly drive Honeywell valves.

## 2026-11-07 — Confirmed ES demand connections and behavior
- [TRACED] ZCM-1 **ES switched terminal**, brown conductor -> DuoMix **terminal 1 (Mix 1 Demand)**.
- [TRACED] ZCM-2 **upper ES terminal**, red conductor -> DuoMix **terminal 3 (Mix 2 Demand)**.
- [TRACED] ZCM-2 **lower ES terminal**, white conductor -> ZCM-1 radiant zone control module -> wiring apparently connected to a nominal 24 VAC transformer. Exact intermediate termination and polarity unknown.
- [OBSERVED] DuoMix demand terminals **2 and 4 tied together**; do not assume they are line-voltage neutrals.
- [PHOTO] The board has separate **OUTPUT** terminals above a distinct pair **ES / ES**. Earlier description of demand conductors as OUTPUT was imprecise; homeowner has now traced them specifically to ES.
- [MEASURED, multimeter V~] Upper radiant zone control module ES/ES: **27.2 VAC** with no first-floor demand, **~1 VAC** with a first-floor zone calling.
- [MEASURED, multimeter V~] Lower ZCM-2 ES/ES: **27.2 VAC** with both upstairs zones calling and **27.2 VAC** with both satisfied.
- [INFERENCE] Working upper ES pair behaves like contacts that close on demand; lower ES pair does not transition in the same way. Manufacturer switching conditions remain unverified.

## Attic Honeywell MiniZone

- [PHOTO] Honeywell/Trol-A-Temp board marked **EMM-3**. Cover wiring diagram **32003618-005 Rev. E** shows three zones. The handwritten enclosure labels read Zone 1 “Bedroom 1 & 2” (Rest of Second Floor) and Zone 2 “Bedroom Above Garage” (Yellow Room), as confirmed by the homeowner.
- [PHOTO/DOC] Each bottom strip includes thermostat **R, Y, W, G, C** and damper motor **M6, M4, M1**. The cover defines **M1** as common, **M4** as power open and **M6** as power closed. Zone 3 has no visible wires on its terminal strip.
- [USER] Zone 1 has white at **M6** and red at **M1**. Zone 2 has green at **M6** and blue at **M1**. The homeowner observed an additional brown-jacketed cable serving both strips. The full conductor grouping and remote endpoints still need to be traced.
- [USER/PHOTO] The separate cable on the upper-left **EQUIPMENT** block is on the equipment interface identified in the cover diagram. Its remote endpoint remains unverified. Keep this attic panel distinct from the basement MABS panel and ZCM-2.

See the [board and cover photos](08-photo-catalog.md#attic-minizone-panel-interior).

## Basement Lennox AM30 factory wiring

The AHU-1 cabinet door provides the AM30-2 Series factory schematic, including thermostat inputs, pump and freeze-stat circuits, and blower relay logic. Use it as a reference when tracing the installed staging and pump wiring. See the [cabinet diagram photos](08-photo-catalog.md#basement-am30-wiring-diagram).

[PHOTO/DOC] The field photos show the populated five-screw **TB1** block. The cabinet schematic lists **Y, G, W, R, C** for TB1. Multiple field conductors converge at the block, so wire colors alone cannot establish which cable comes from MABS EQUIP. Confirm the cable jacket route or individual conductors before assigning endpoints. See the [TB1 close-up and overview](08-photo-catalog.md#basement-am30-low-voltage-wiring).

## Basement Trol-A-Temp MABS EZ-4

[PHOTO] ZCP-1 below MC-1 is a Trol-A-Temp **MABS EZ-4** four-zone control panel. The cover diagram identifies thermostat and damper-motor terminals for each zone and a separate equipment block with W1, W2, Y1 and Y2. Those are factory terminal functions. Installed staging and equipment wiring still need to be traced.

[USER/PHOTO] Zone 1 serves Main (Living Area), with the thermostat near the living room. Zone 2 serves Master Bedroom. Zone 3 serves Basement and has fewer connected conductors. Zone 4 has no visible terminal wiring. Basement single-stage heat and actual cooling operation remain unverified. The thermostat offers Cool mode and basement ducts are present, per homeowner.

[USER TRACE] The EQUIP cable exits through the top of the gray cabinet. The homeowner suspects it continues to the basement AM30 (AHU-1). The cable disappears into a bundle after leaving the gray cabinet. At AHU-1, the low-voltage wiring enters through a side opening near TB1. The MABS EQUIP-to-AHU-1 link is inferred from the interfaces and equipment layout. Cable identity and individual terminal assignments remain unverified. A separate brown-jacketed cable also exits the cabinet top. Its red and white conductors land on the two TL terminals, labeled ZoneMAX supply-air temperature sensor on the cover diagram. The homeowner sees a likely probe near the top of AHU-1 where the supply duct branches to the zones. The cable has not been traced end to end.

See the [MABS cover, diagram and board](08-photo-catalog.md#basement-mabs-ez-4-panel).
