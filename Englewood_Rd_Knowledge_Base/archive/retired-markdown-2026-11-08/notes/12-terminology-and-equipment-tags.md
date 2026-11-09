# 12 — Standard terminology and equipment tags

**Status:** Approved by homeowner, 2026-11-08. This register governs the Markdown notes, diagrams, and generated HTML. Tags are **documentation identifiers**, not verified manufacturer designations. Preserve the exact physical terminal markings (e.g., `Mix 2 Pmp`, `Var 2 Pmp`, `ES`, `TELESTAT`) when quoting labels.

| Standard component term | Documentation tag | Installed product / note |
|---|---|---|
| Radiant zone control module | ZCM-1 | ZCM-1/Uponor three-zone module, first-floor radiant; confirmed installed part **A303XX0003** |
| Radiant zone control module | ZCM-2 | ZCM-2/Uponor three-zone module, second-floor radiant; confirmed installed part **A303XX0003** |
| Hydronic mixing controller | MC-1 | Wirsbo DuoMix 201; controls two mixed-water circuits and associated injection outputs |
| HVAC zone control panel (provisional) | ZCP-1 | Trol-A-Temp **MABS EZ-4** confirmed on cover. Installed staging and output routing remain to be traced. |
| 24 VAC control transformer | XFMR-1 (provisional) | Supplies low-voltage controls; exact shared ES circuit topology not verified |
| Water-heating plant / hydronic heat source | WH-1, WH-2 | Two Polaris water heaters in series; Left tank nameplate PG10 34-150-2NV, serial 0448117372. Right tank nameplate PG10 34-150-2NV, serial 0449124485. Tags do not assert flow order |
| Main-loop circulator | — | Grundfos UPS 26-99 BFC, product 52722518. Blue tape reads “Boiler Enable From Wirsbo.” MC-1 Boiler Enable terminal 6 receives line hot and terminal 5 sends switched hot to the pump. |
| Basement radiant circulator | — | Dedicated on/off Taco 006-B4-11. Feeds the basement radiant supply manifold from TMV-1. |
| Mixed-water circulator | P-M1, P-M2 (provisional) | DuoMix outputs `Mix 1 Pmp` (12) and `Mix 2 Pmp` (8); Mix 2 is Taco 008-BC6. Mix 1 is Taco 006-B4-11 |
| Variable-speed injection circulator | P-I1, P-I2 (provisional) | DuoMix outputs `Var 1 Pmp` (14) and `Var 2 Pmp` (10); Var 1 is Taco 008-BC6. Var 2 appears to be the same model, pending nameplate confirmation |
| Thermostatic mixing valve (TMV) | TMV-1 | Caleffi 521 basement radiant mixing valve |
| Domestic hot-water tempering valve | TMV-2 (provisional) | Caleffi above the right Polaris tank in the entrance photo. Caleffi 521 MixCal, SupplyHouse SKU 521519AC, 3/4-inch sweat, with temperature gauge and check valve per homeowner receipt. |
| Hydronic air-handling unit (hydronic air handler) | AHU-1 | Basement Lennox AM30, cabinet model AM30Q2/3-70-2, serial 5898M07675. Associated C26-41-1 refrigerant evaporator, serial 6099H46722. |
| Hydronic air-handling unit (hydronic air handler) | AHU-2 | Attic Lennox AM30Q2-40-2, serial 5801K48409, with Taco 006-B4-11 circulator |
| Air-handler hydronic circulator | P-AHU1 | Basement AM30 internal Taco 006-B4-11. |
| Air-handler hydronic circulator | P-AHU2 | Attic AM30 internal Taco 006-B4-11. Suspected failure remains unverified. |
| Motorized zone valve / zone-valve actuator | TBD | Honeywell V8043E1061 confirmed for Yellow Room. Verify other nameplates. |
| Thermoelectric actuator / thermal actuator | TBD | Wirsbo `TELESTAT` is a **terminal marking**; not evidence that this actuator type is installed |
| System end-switch contacts | ES | Contact pair on each ZCM; upper pair shows demand-dependent voltage change |
| Heating demand / call for heat | — | Thermostat demand condition |
| Switched line-voltage circulator output | — | DuoMix pump output, e.g. terminal 8 or 12, nominal 120 VAC |
| Mixing demand input | — | DuoMix terminals 1–2 and 3–4 |

**Important distinctions:** Mix 2 mixed-water circulator and the AHU-2 air-handler hydronic circulator are **different suspected devices**. `OUTPUT` and `ES/ES` are **different terminal groups** on the radiant zone control modules. MABS panel role remains provisional; no claim about thermostat sequence is justified without a trace. **A3031003** is a proposed replacement candidate. Compatibility with the installed **A303XX0003** modules remains unverified.
