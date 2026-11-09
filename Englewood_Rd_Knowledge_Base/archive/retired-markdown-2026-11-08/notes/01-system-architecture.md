# 01 — System architecture and equipment


The homeowner reports that the system was first installed when the house was built in **1999**. The current Grundfos main-loop circulator carries production code **PC 1240** (week 40 of 2012), identifying it as a later replacement. Its installation date is unknown.
## Heat source and hydraulics
- [USER] Two Polaris gas water heaters in **series** provide hot water for hydronic radiant heat and hydronic air-handler heating. Domestic hot water and space heating share the same water, per the homeowner. The right Polaris tank in the entrance photo supplies domestic hot water through a separate Caleffi thermostatic mixing valve above the tank. The homeowner reports a tank setting around 170 °F and a mixed domestic outlet around 105–110 °F. The homeowner confirmed from the SupplyHouse receipt that TMV-2 is a Caleffi 521 MixCal, SKU 521519AC, a 3/4-inch sweat three-way thermostatic mixing valve with temperature gauge and check valve. See the [overhead mixer photo](08-photo-catalog.md#domestic-caleffi-mixer-from-above).
- [USER TRACE] The street cold-water branch feeds both the cold inlet of the domestic Caleffi mixer (TMV-2) and the left Polaris tank, at its lower side port labeled Cold Inlet. Left and right refer to the entrance view.
- [USER TRACE] Domestic hot water has a passive gravity recirculation loop. Both its supply and return connect to the right Polaris tank as seen from the entrance. The homeowner reports that it keeps hot water available in much of the house. The return descends between the tanks in the entrance photo, wraps around the right tank to its far side, and enters its lower side port labeled Cold Inlet. Copper from the top hot outlet of the right tank feeds the TMV-2 hot inlet. Street cold water enters the opposite port. The mixed outlet opposite the adjustment handle starts the domestic recirculation loop.
- [DOC] Homeowner water-heater note identifies model **PG10 34-150-2NV**, confirmed on both tank nameplates. Notes include condensate trap **186642-000**, O-ring **AS568-327, 1.725-inch ID**, stainless washer **2.187-inch diameter × .030-inch**. These are parts research notes, not confirmed installed parts.
- [USER] Basement radiant is independent of DuoMix, with a dedicated on/off Taco **006-B4-11** circulator switched by a Honeywell R8222D1014 relay and **Caleffi 521** thermostatic mixing valve.
- [USER/PHOTO] Two radiant mixed-temperature groups are controlled by a **Wirsbo DuoMix 201** with separate Mix 1 and Mix 2 circulation outputs and Var 1/Var 2 injection pump outputs.
- [USER] Upstairs circulator **Taco 008-BC6**; researched replacement cartridge **008-045RP** (compatibility still verify against nameplate). The homeowner identifies this pump as the Mix 2 mixed-water circulator.
- [USER] Two **Lennox AM30** hydronic air handlers, one basement and one attic, provide supplemental forced air. The internal circulator nameplates for both AHU-1 and AHU-2 read Taco **006-B4-11**. Product-family PDF bundled; the basement AHU-1 cabinet is AM30Q2/3-70-2, serial 5898M07675. The attic AHU-2 cabinet is AM30Q2-40-2, serial 5801K48409. Detailed field wiring remains unverified.

## Controls cabinet
- [PHOTO] Two three-zone Wirsbo circuit boards on right side, one above the other; six external black relay-like components in two groups of three, mounted above respective boards; Wirsbo DuoMix 201 and other control board on left; dense multiconductor wiring.
- [USER] Trol-A-Temp MABS EZ-4 four-zone panel confirmed on cover. Zone assignments are mapped. Installed staging remains unverified.
- [PHOTO] Original proposed radiant piping drawing photographed; **Garage Entry** was proposed but [USER] **not installed**.

## Known versus inferred relationships
- [USER] Mix 1 corresponds to first-floor radiant; Mix 2 corresponds to upstairs radiant.
- [INFERENCE] A zone call must ultimately be converted to DuoMix demand and a switched circulator output; exact intervening components unknown.
- [OPEN] All valve locations, hydronic manifold layout, piping check valves, pump positions, sensor placement, boiler enable wiring, and safety interlocks.

## Equipment behind the Polaris tanks

- [USER/PHOTO] Basement radiant uses the lower-left Taco circulator and adjacent mechanical Caleffi mixing valve.
- [USER/PHOTO] The red Grundfos UPS 26-99 BFC (product 52722518) runs the main circulation loop upstairs and back. It corresponds to the pump shown above the tanks on the proposed drawing. Flow is left to right in the behind-tank photo. The homeowner reports that the loop rises to the attic AM30 (AHU-2) first, then continues to the Var 2 injection and Mix 2 radiant assembly, where the piping branches. MC-1 Boiler Enable switches pump hot from terminal 6 to terminal 5. A basement-only radiant call runs its own Taco. The basement-only call does not send a demand to MC-1, so that call does not start the Grundfos.
- [USER/PHOTO] The two higher light-brown Taco pumps are MC-1 Mix 1 on the left and Var 1 on the right, viewed from behind the tanks.
- [USER/PHOTO] The first-floor Honeywell valves run front to back in this view in the order Master Bath, Master Bedroom, then Main (Living Area). Two expansion tanks are visible below and to the right. Their circuit connections remain to be traced.
- [USER TRACE] At the right edge of the behind-tank basement photo, the near riser is the attic supply from the red Grundfos. The return riser is partly obscured directly behind it. It drops vertically, crosses the basement plumbing at the two expansion-tank connections, then continues to the Polaris return. The second-floor heating return enters the left Polaris tank at the port labeled “Heating System Inlet.” The heating circuit passes through the left tank first and then the right tank.

See the [behind-tank photo](08-photo-catalog.md#behind-the-polaris-tanks).

## Attic hydronic piping

- [USER/PHOTO] In the right-hand plumbing-wall view, the lowest horizontal run is the incoming main-loop supply from the basement. The AM30 coil branch comes off first and projects toward the camera. The main loop continues toward the Var 2 injection and Mix 2 radiant assembly, then returns downstairs.
- [USER/PHOTO] The brown Taco on the radiant supply is Mix 2. The Taco above the red and green valve handles on the right is Var 2. Mix 2 is a Taco **008-BC6** and flows right to left in this view. Var 2 flows upward. Its Taco nameplate appears to read **008-BC6**, pending confirmation because of glare.
- [USER/PHOTO] In the attic plumbing-wall photo, the Rest of Second Floor supply continues left through the left valve. The Yellow Room supply turns back to the right before passing through the right valve. The uppermost cross-frame pipe is the Rest of Second Floor manifold return, which tees into the Yellow Room return. The closely spaced supply and return elbows are separate pipes.
- [USER TRACE] Along the attic mixed-loop return toward the Mix 2 inlet, the Yellow Room and Rest of Second Floor manifold returns combine first. The connection back to the main branch is next, followed by the Var 2 discharge tee, then the Mix 2 inlet. Var 2 draws from the main supply from the basement downstream of the AHU-2 branch and injects upward into the pipe feeding Mix 2.
- [USER TRACE] Along the attic main loop from the basement, the AHU-2 coil supply tee comes first and the coil outlet rejoins the main a few inches downstream. Farther along the main loop, the Var 2 inlet and the Mix 2 circuit return connect through a second pair of closely spaced tees.
- [USER TRACE] In the attic plumbing-wall photo with the Honeywell MiniZone panel, the main-loop return is on the left and the supply is on the right. Both pass vertically through the framed wall’s bottom plate below the visible area.
- [USER/PHOTO] SUP 2 is located under the insulation immediately upstream of the Mix 2 inlet. The visible blue leads carry a tekmar 071 tag. See the [sensor close-up](08-photo-catalog.md#sup-2-sensor-at-mix-2).
- [USER/PHOTO] The high-point air eliminator beside the visible Honeywell valve is in service. The switch labeled “Furnace” powers AHU-2, a Lennox AM30 hydronic air handler.

See the [right-hand attic photo](08-photo-catalog.md#attic-plumbing-wall-right-hand-view).

The [Yellow Room radiant manifold](08-photo-catalog.md#yellow-room-radiant-manifold) is at the far end of the attic mechanical room beside Var 2. In the manifold photo, the right header with the small valves supplies the floor loops and the left header collects their return.

The [Rest of Second Floor radiant manifold](08-photo-catalog.md#rest-of-second-floor-radiant-manifold) has its supply on the lower, farther header with the small valves. The upper, nearer header collects the return.

## Polaris heating supply branches

[USER TRACE] The upper side port labeled **Heating System Outlet** on the right Polaris tank (entrance view) feeds the heating supply header. In order from the tank, the first tee feeds the basement radiant loop, the second tee feeds the red Grundfos, and the elbow beyond both tees feeds the basement Lennox AM30 (AHU-1). The basement radiant branch has its own Taco circulator and Caleffi mixer. See the [outlet branch photo](08-photo-catalog.md#polaris-heating-outlet-branches).

[USER TRACE] The basement radiant manifold return comes around the corner toward the expansion tanks, rises, and tees into the common heating return just beyond the expansion-tank connections, toward the left Polaris Heating System Inlet. The nearby tees serve separate connections. Their spacing does not indicate a paired supply and return connection for the basement radiant circuit.

[USER/PHOTO] A temperature probe is mounted on the common heating return downstream of the basement radiant return tee, left of the expansion tanks. Its blue leads are visible behind the Grundfos. See the [return probe photo](08-photo-catalog.md#common-heating-return-temperature-probe).

[USER TRACE] The basement AM30 (AHU-1) coil return joins the same common heating return near the left Polaris Heating System Inlet. The green-handled valve in the heating outlet branch photo identifies the AM30 return line.

[USER TRACE] The insulated intertank pipe runs from the left Polaris upper **Heating System Outlet** to the right Polaris lower **Heating System Inlet**. Left and right refer to the entrance view. The second-floor heating return enters the left tank, passes through both tanks in series, and leaves the right tank through its Heating System Outlet. See the [intertank pipe photo](08-photo-catalog.md#polaris-intertank-heating-pipe).

## First-floor radiant injection piping

[USER TRACE] Var 1 (right pump, Taco **008-BC6**) draws from the main loop as it returns from upstairs. That branch feeds the Mix 1 circuit, which rejoins the same main return through the other of two closely spaced tees at the right of the photo. Mix 1 is the left pump, a Taco **006-B4-11**. Both pumps flow right to left in this view. The blue sensor lead is visible immediately upstream of Mix 1. The blue sensor leads splice to red and white conductors in a brown-jacketed thermostat cable. A red conductor lands on MC-1 SUP 1, making this the likely SUP 1 sensor. The cable disappears into a bundle before the controller, so end-to-end identity and the white conductor termination remain unverified.

See the [Mix 1 and Var 1 close-up](08-photo-catalog.md#mix-1-and-var-1-piping).

[USER TRACE] Mix 1 discharge splits into three branches for Master Bath, Master Bedroom, and Main (Living Area). Each branch passes through its Honeywell zone valve before reaching its supply manifold. Elbows turn the flow left to right through the valves toward the manifolds in the overhead view. See the [overhead photo](08-photo-catalog.md#mix-1-zone-valves-and-manifolds).

[USER TRACE] The Master Bath, Master Bedroom, and Main (Living Area) returns collect in one common first-floor return manifold visible just below Mix 1 in the Mix 1 and Var 1 close-up. From that manifold toward Mix 1, the lower pipe below Var 1 connects back to the main return first. Farther along, Var 1 discharges into the pipe feeding the Mix 1 inlet. Var 1 draws from the main loop returning from upstairs.

## Basement radiant mixer and manifold

[USER/PHOTO] The hot supply from the right Polaris heating header enters the Caleffi mixer from above. The basement Taco circulator is in the foreground and the manifold is behind it. At the right behind the wiring, the front and rear pipes visually overlap and remain separate at that point. The Caleffi mixed outlet runs left through the branch with the red-handled valve to the Taco inlet. The bottom port runs down and across to the basement radiant return manifold. The manifold return continues downstream to its tee into the common heating return by the expansion tanks. The Taco discharge feeds the basement radiant supply manifold directly.

See the [basement radiant close-up](08-photo-catalog.md#basement-radiant-mixer-and-circulator).

## Basement pressure instrumentation

The combination temperature and pressure gauge is mounted on the Mix 1 discharge, between the circulator and the three main-floor Honeywell zone valves. The October 1, 1999 Lennox CompleteHeat dealer letter describes an external pressure-reducing valve and expansion tank requirement. The homeowner traced the street cold-water feed to the Polaris and domestic mixer branch and saw no identifiable pressure-reducing valve along the route. Presence elsewhere remains unverified. See the [letter and gauge photos](08-photo-catalog.md#basement-lennox-cooling-coil-and-pressure-documentation).
