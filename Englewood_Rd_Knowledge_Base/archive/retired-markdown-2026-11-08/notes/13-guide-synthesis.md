# 13 — Current guide synthesis and scope

## Deliverable approved 2026-11-08

The primary explanatory report is now **Englewood Road Hydronic Heating System**, without a street number. `report/index.html` is one self-contained HTML file with embedded photos, interactive diagrams, searchable equipment, operating sequences, and known issues. It replaces the earlier HTML presentation. Original photographs and historical records remain preserved.

The user approved conventional hydronic/electrical symbols, red/blue piping with a distinct mixed-water color, component hover previews and tap/click photo details, and a high-level-to-detail structure. The survey stops at plumbing and main electronics through both AM30 units, not downstream duct/damper mapping.

## Corrections that govern the current synthesis

- Both ZCMs are installed **A303XX0003**. A3031003 remains an unverified replacement candidate; A3030003 is an earlier guessed installed identity.
- Both upstairs isolated valve switches remained OL during powered opening; a working Living Room comparison showed continuity. This prioritizes valve travel/switch actuation, without proving ZCM-2 healthy or defective. Connected TELESTAT R1/R2 voltage alone cannot diagnose closure or board health.
- Yellow Room valve is Honeywell V8043E1061. Other valve nameplates have not all been confirmed.
- Main heating flow: common return → left Polaris → right Polaris → branches. First tee supplies basement radiant, second supplies Grundfos, following elbow supplies basement AM30.
- Grundfos loop: attic AM30 closely spaced tees → upstairs injection tees → return to basement → first-floor injection tees → common return. First-floor injection draws from this returning main loop.
- Mixed circuits: combined manifold returns → takeoff back to main loop → injection junction → supply probe/Mix inlet. Zone branches are parallel.
- Two expansion tanks connect at the common return; basement radiant joins downstream toward the left tank. Nearby return tees are not automatically a primary/secondary pair.
- Basement radiant uses one dedicated Taco and a mechanical mixer; Honeywell R8222D1014 switches its 120 V supply. No basement radiant ZCM, MC-1 demand, or basement-only Grundfos start is reported.
- Shared white transformer wiring to brown and upper black relays appears to be 24 VAC common, not a demonstrated 120 V neutral. Checked ZCM upper THERMOSTAT 2 → relay lug 2 red; THERMOSTAT 3 → relay lug 4 white; SB and 4 unused. Complete relay roles remain unresolved.
- MC-1 Boiler Enable: terminal 6 receives 120 V hot; terminal 5 supplies Grundfos hot; pump white returns to supply neutral. It is not traced to Polaris burner enable.
- Domestic water is shared with heating. Street cold feeds left Polaris Cold Inlet and TMV-2 cold inlet. Right top domestic hot outlet feeds TMV-2 hot inlet; mixed outlet feeds distribution/passive recirculation; return enters right Cold Inlet.
- Domestic mixer is receipt-confirmed Caleffi 521519AC. Basement mixer is Caleffi 521, exact suffix unverified.
- Basement AM30 model AM30Q2/3-70-2, serial 5898M07675. Attic AM30Q2-40-2, serial 5801K48409. Both internal pumps are Taco 006-B4-11; so are Mix 1 and basement radiant. Mix 2 and Var 1 are 008-BC6; Var 2 appears 008-BC6, provisional due to glare.
- MABS EZ-4 downstairs: Zone 1 Living Area, Zone 2 Master Bedroom, Zone 3 Basement. EMM-3 attic: Zone 1 Rest of Second Floor, Zone 2 Yellow Room. Equipment-to-AM30 cable identities and staging are inferred, not traced end to end.
- Stage 2 retaining stage 1 is a homeowner expectation. With failed upstairs end-switch feedback, stage 1 demand alone does not prove Grundfos operation. Independent air-only main-loop enable remains open.
- Grundfos PC 1240 is a production date code, not a proven installation date. System original installation is homeowner-reported 1999.
- Right tank reported ~170 °F and domestic mixed outlet ~105–110 °F are observations, not recommended settings. Both Polaris plates mark 160 °F outlet operation. AM30 maximum inlet is 180 °F.
- Pressure-reducing valve was not identified along the traced cold feed; absence elsewhere is not proven. Gauge ~65 psi is one uncalibrated snapshot. The 450 psi C26 rating concerns refrigerant.

## Report source and maintenance

Topic Markdown and original photos remain the evidence record. `reporting/guide/build.py` contains the curated equipment data and SVG geometry; `reporting/guide/template.html` contains the explanatory narrative and offline interaction code. Changes in findings must update the relevant Markdown and curated guide content before rebuilding. Source chapters are embedded verbatim for offline inspection, with a notice that older entries may be superseded by the synthesis.

The guide does not assert live equipment status, live supplier stock, or verified wiring where tracing stopped. External reference links require internet; embedded diagrams and photos do not.
