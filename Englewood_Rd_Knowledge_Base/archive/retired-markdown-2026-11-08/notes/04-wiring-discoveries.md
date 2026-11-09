# 04 — Wiring discoveries, cable sharing, valve logic

## Brown-sheathed multiconductor cables
- [USER] Several 6- or 8-conductor thermostat-style cables leave the top of cabinet. Within a single sheath, conductors are split across multiple purposes; cable co-location **does not** prove electrical association.
- [USER] **Bedroom Above Garage / Yellow Room:** brown and blue conductors go to DuoMix **17 COM / 20 SUP 2**. A small temperature sensor contacts the supply pipe at the far end. The installer apparently reused spare thermostat-cable conductors for this sensor; whether it is physically part of the thermostat cable and exact route should be documented.
- [USER] **Rest of Second Floor:** brown conductors from its cable go to the black external relays; user noted wires appearing to reach **two different relays**. Which terminal and which relay is not yet established.
- [PHOTO] Relay wiring connects to upper THERMOSTAT terminals of ZCM-2 radiant zone control module. This suggests a possible input/isolation role, but direction of electrical signal remains unknown.
- [PHOTO] ZCM-2 right-edge OUTPUT strip has visible red conductors; exact number/terminal locations and destination not traced.

## Competing topology hypotheses
A. Thermostat → external relay coil → relay contact → Wirsbo THERMOSTAT input → board OUTPUT → DuoMix Mix 2 Demand.
B. Thermostat → Wirsbo THERMOSTAT input; TELESTAT or OUTPUT energizes relay/zone valve; Honeywell end switch triggers DuoMix demand.
C. Thermostat staging relay independently distributes stage-1 and stage-2 calls to Wirsbo and Lennox controls.
**None is proven.** Avoid diagramming any as verified.

## Honeywell zone valves
- [PHOTO] Yellow Room valve is a Honeywell **V8043E1061**, normally closed. The two yellow leads power its 24 VAC motor. The two red leads are the separate auxiliary end switch. Confirm nameplates individually on the other valves.
- [DOC] A motor-driven call should close the auxiliary switch at the end of the opening stroke. The manual-open lever does not operate it. The isolated pair should read OL closed-valve, near 0 ohms fully open on a call, then OL after closing. [Honeywell instructions](https://customer.resideo.com/resources/Techlit/TechLitDocuments/95-0000s/95-6983EF.pdf)
- [USER] Yellow Room red leads splice to green and yellow in a brown thermostat cable. A matching pair lands at its ZCM-2 lower TELESTAT R1/R2. End-to-end cable identity and exact color-to-terminal assignment remain unverified. Motor routing and other zone wiring remain open. Both upstairs switches stayed OL when tested at the valves during motor-driven calls. See [test log](05-troubleshooting.md).

## Proposed wiring capture table
| Cable ID | Jacket / location | Conductor | From terminal | To terminal | Voltage/contact type | Evidence |
|---|---|---|---|---|---|---|
| TBD | Yellow Room brown sheath | Brown | TBD | DuoMix 17 COM | Sensor circuit, verify | User report |
| TBD | Yellow Room brown sheath | Blue | TBD | DuoMix 20 SUP 2 | Sensor circuit, verify | User report |
| TBD | Rest of Second Floor brown sheath | Brown / other | TBD | External relay(s) TBD | Unknown | User report |
| TBD | Lower radiant zone control module OUTPUT | Red conductors | OUTPUT TBD | TBD | Unknown | Photo |
| TBD | DuoMix 3–4 | TBD | TBD | TBD | Demand input, type verify | Labels |

## 2026-11-07 — ES demand wiring (updated as-built traces)
| Origin | Wire | Destination | Confidence |
|---|---|---|---|
| ZCM-1 ES | Brown | DuoMix 1, Mix 1 Demand | Homeowner physically traced |
| ZCM-2 upper ES | Red | DuoMix 3, Mix 2 Demand | Homeowner physically traced |
| ZCM-2 lower ES | White | ZCM-1 radiant zone control module, then apparently 24 VAC transformer | Traced path; exact terminal unknown |
| DuoMix 2 | Shared wire | DuoMix 4 | Homeowner observed connection |

**Correction:** These demand wires land at **ES/ES**, not the distinct **OUTPUT** terminals above them. Upper-board transformer-side ES wire and the full DuoMix demand return need further tracing.

**Functional comparison:** Upper ES voltage drops 27.2 -> ~1 VAC on a first-floor call. Lower ES remains 27.2 VAC during upstairs calls and when satisfied. This localizes the suspected demand interruption to ES closure or its prerequisites, without proving a defective board.

The [cabinet photo](08-photo-catalog.md#zcm-boards-relays-and-zone-tags) shows two black relay assemblies above ZCM-1 and three above ZCM-2. The photo establishes the visible layout. Relay model, pinout and individual circuit assignments remain open.

[PHOTO/DOC] The upper right relay is MARS 90293 and the upper left is White-Rodgers 90-293Q. MARS cross-references these as 24 VAC coil SPDT switching relays. The three lower relay models and all installed coil/contact assignments remain to be traced. [Relay photos](08-photo-catalog.md#upper-zcm-relay-nameplates) · [MARS catalog](https://www.rogerssupply.com/Attachment/Mars_90290_Catalog.pdf)

[PHOTO] The lower-right relay above ZCM-2 is marked White-Rodgers with a 24 V 50/60 Hz coil. Its model number and circuit assignment remain unverified. See the [side-label photo](08-photo-catalog.md#lower-right-relay-above-zcm-2).

### Upper relays to Honeywell switching relay

[USER TRACE] A shared white conductor from the 24 VAC transformer bridges the brown Honeywell R8222D1014 and both upper black relays. It appears to be the shared coil common. Each upper relay has a red lead traced to ZCM-1. A second white lead from the upper-right relay enters a brown-jacketed cable that disappears into the bundle. A separate white lead at the Honeywell appears to connect to an incoming thermostat cable from the cabinet top. Its far end remains unverified. The Honeywell relay switches 120 VAC to the dedicated basement radiant Taco through its outgoing black conductor.

[USER TRACE] The homeowner confirms the same pattern across the black relay circuits checked on ZCM-1 and ZCM-2. Upper ZCM THERMOSTAT terminal 2 connects to relay lug 2 by a coiled red lead. Upper THERMOSTAT terminal 3 connects to relay lug 4 by a white lead. SB and 4 are unused on the thermostat strips checked. The numbered landing of the separate shared transformer conductor remains unverified.

[USER] Living Area, Living Room, and Rest of First Floor refer to the same main-floor zone. The wall thermostat conductor landing at the black relay remains unverified. The verified ZCM-1 THERMOSTAT terminal 3 to relay lug 4 trace is recorded above.
