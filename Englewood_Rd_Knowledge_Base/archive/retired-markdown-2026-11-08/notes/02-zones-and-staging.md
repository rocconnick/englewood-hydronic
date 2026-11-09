# 02 — Zones, thermostats, air handlers

| Radiant zone | Controller | Mixed group | Air support / notes |
|---|---|---|---|
| Basement | Dedicated on/off Taco circulator + Caleffi 521 | Not DuoMix | Basement Lennox AM30 |
| Living Area | ZCM-1, left / zone 1 | Mix 1 | Basement AM30 |
| Master Bedroom | ZCM-1, center / zone 2 | Mix 1 | Basement AM30 |
| Master Bath | ZCM-1, right / zone 3 | Mix 1 | Floor sensor; separate stage relationship unverified |
| Rest of Second Floor | ZCM-2, left / zone 1 | Mix 2 | Attic AM30; valve opens on call, isolated end switch stays OL |
| Bedroom Above Garage / Yellow Room | ZCM-2, middle / zone 2 | Mix 2 | Attic AM30; Honeywell V8043E1061 opens on call, isolated end switch stays OL; SUP 2 sensor conductors in shared cable |
| Spare | ZCM-2, right / zone 3 | None | Labeled SPARE; unused |

- [USER] **Five air thermostats** operate first-stage radiant and second-stage supplemental forced air. Exact mapping of five air thermostats to six radiant zones and Master Bath floor sensor is **open**.
- [USER] Basement air handler covers basement, main living floor and master suite; attic air handler covers upstairs rooms.
- [OPEN] Whether stage 2 retains stage 1, how the MABS component mediates stages, and which contacts drive the air handlers.
- [CORRECTION] A previously hypothesized sequence placing MABS ahead of all Wirsbo thermostat terminals is **not verified**; could instead be direct thermostat to Wirsbo and a separate stage relay.

The attic Honeywell MiniZone enclosure labels map Zone 1 (“Bedroom 1 & 2”) to Rest of Second Floor and Zone 2 (“Bedroom Above Garage”) to Yellow Room. See the [MiniZone controls notes](03-controls-terminals.md#attic-honeywell-minizone) for terminal assignments and remaining cable traces.

The basement MABS EZ-4 (ZCP-1) maps Zone 1 to Main (Living Area), Zone 2 to Master Bedroom, and Zone 3 to Basement. Zone 4 has no visible terminal wiring. Whether Zone 3 provides forced-air heating or cooling remains unverified. See the [MABS controls notes](03-controls-terminals.md#basement-trol-a-temp-mabs-ez-4).

[USER INFERENCE] On an upstairs heating call, stage 2 (AHU-2 forced air) is expected to keep stage 1 (radiant demand) active. With valid radiant feedback, that demand would start the Grundfos through MC-1 Boiler Enable. Stage overlap and any independent AHU-2 heat call remain unverified.
