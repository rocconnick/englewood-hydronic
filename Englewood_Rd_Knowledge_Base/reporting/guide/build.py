#!/usr/bin/env python3
"""Build the offline field guide. Python 3 + Pillow; no remote assets or JS dependencies."""
from pathlib import Path
from PIL import Image, ImageOps
import base64, io, json, re, html, hashlib
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
E=html.escape
C={}
def comp(id,name,model,location,text,photos,status='Confirmed',extra=''):
 C[id]=dict(id=id,name=name,model=model,location=location,text=text,photos=photos.split('|') if photos else [],status=status,extra=extra)
comp('wh1','Left Polaris · first tank in heating flow','PG10 34-150-2NV','Basement · left tank from entrance','Receives the common heating return at Heating System Inlet. Its Heating System Outlet feeds the right tank’s Heating System Inlet. Street water enters its separate Cold Inlet. These are gas water heaters providing the heating plant as well as potable hot water; there is no separate boiler water circuit reported.','mechanical-room-overview.jpg|left-polaris-nameplate.jpg|polaris-intertank-heating-pipe.jpg',extra='Serial 0448117372 · product 0320092 · 34 US gal · natural gas · 150,000 BTU/h input. Plate marks 160 °F outlet operation. System originally installed in 1999; individual installation dates are not established.')
comp('wh2','Right Polaris · final heating supply tank','PG10 34-150-2NV','Basement · right tank from entrance','Receives water from the left tank. Its upper side Heating System Outlet supplies basement radiant, the Grundfos main loop, and the basement AM30. Its top domestic hot outlet feeds the separate domestic Caleffi mixer. The passive domestic recirculation return enters this tank’s lower Cold Inlet.','mechanical-room-overview.jpg|right-polaris-nameplate.jpg|polaris-heating-outlet-branches.jpg',extra='Serial 0449124485 · product 0320092. Owner reports approximately 170 °F setting; plate marks 160 °F outlet operation. This guide records that discrepancy and does not establish a recommended setting.')
comp('g','Main-loop circulator','Grundfos UPS 26-99 BFC · P/N 52722518','Behind Polaris tanks · red pump','Moves water up to the attic and back. The attic AM30 branch comes first, then the upstairs injection circuit. The returning main loop supplies the first-floor injection circuit before returning to the tanks. MC-1 Boiler Enable switches its 120 V hot; it is not the dedicated basement radiant pump.','grundfos-main-loop-installed.jpg|grundfos-main-loop-nameplate.jpg|mechanical-room-behind-polaris.jpg',extra='115 V · 60 Hz · single phase · three speeds · check-valve marking. PC 1240 indicates production week 40 of 2012; installation/replacement date is unknown. Field label: “Boiler Enable From Wirsbo.”')
comp('m1','Mix 1 · first-floor distribution circulator','Taco 006-B4-11','Behind tanks · left pump above Grundfos','Circulates blended water through the three first-floor radiant zones. Var 1 adds hot water to its inlet circuit. Flow is right to left in the pump-wall photo; elbows turn the flow left to right at the valve/manifold assembly.','mix-1-var-1-piping.jpg|mix-1-circulator-nameplate.jpg',extra='MC-1 output 12; neutral 11. 115 V · 0.52 A · 1/40 hp. Nameplate faces the wall and is obscured by a manifold hose from the normal service position.')
comp('v1','Var 1 · first-floor injection circulator','Taco 008-BC6','Behind tanks · right pump above Grundfos','Draws from the main loop returning from upstairs and injects into the Mix 1 inlet. This controls added heat, while Mix 1 provides radiant-loop circulation. The mixed circuit also sends water back to the main return through the other closely spaced tee.','mix-1-var-1-piping.jpg|var-1-circulator-nameplate.jpg',extra='MC-1 output 14; neutral 13. Flow right to left in wall photo. 115 V · 0.84 A · 1/25 hp.')
comp('m2','Mix 2 · upstairs distribution circulator','Taco 008-BC6','Attic plumbing wall · left of Var 2','Circulates blended water to Yellow Room and Rest of Second Floor. It is separate from the pump inside the attic AM30. During the investigation, its MC-1 output did not activate with upstairs radiant calls.','attic-plumbing-wall-right.jpg|mix-2-taco-008-bc6-nameplate.jpg',extra='MC-1 output 8; neutral 7. Flow right to left in the plumbing-wall view. 115 V · 0.84 A · 1/25 hp.')
comp('v2','Var 2 · upstairs injection circulator','Taco 008-BC6 — provisional reading','Attic plumbing wall · right-hand vertical pump','Draws from the main supply downstream of the attic AM30 branch. Pumps upward into the Mix 2 inlet circuit, after the combined manifold returns and their connection back to the main loop.','var-2-installed.jpg|var-2-nameplate.jpg|attic-plumbing-wall-right.jpg','Routing confirmed; model provisional','MC-1 output 10; neutral 9. Flash glare prevents a fully confident model reading.')
comp('b','Basement radiant circulator','Taco 006-B4-11','Behind tanks · low pump beside Caleffi mixer','A dedicated on/off pump feeds the basement radiant supply manifold directly. There is one basement radiant zone and no basement ZCM or motorized zoning valve in the reported arrangement. Its brown Honeywell switching relay is independent of DuoMix.','basement-radiant-mixer-and-circulator.jpg|basement-radiant-circulator-nameplate.jpg',extra='115 V · 0.52 A · 1/40 hp. Basement-only radiant demand does not start MC-1 or the Grundfos.')
comp('tm1','Basement radiant mixing valve','Caleffi 521 · exact suffix unverified','Behind tanks · above basement Taco','Mechanically blends hot heating supply with basement radiant return. Hot enters from above; mixed outlet runs left through the red-handled valve to the Taco. Bottom port connects to the basement manifold return, which also continues to the common return by the expansion tanks.','basement-radiant-mixer-and-circulator.jpg',extra='This valve uses radiant return for its cooler inlet. Do not confuse it with the domestic mixer, whose cold inlet receives street water.')
comp('tm2','Domestic hot-water tempering valve','Caleffi 521 MixCal · SKU 521519AC','Above right Polaris','Blends the right tank’s hot outlet with street cold water. The outlet opposite the adjustment handle supplies household hot water and begins the passive domestic recirculation loop.','domestic-caleffi-mixer-top.jpg|mechanical-room-overview.jpg',extra='Receipt-confirmed 3/4-inch sweat, three-way valve with temperature gauge and check valve. Owner reports approximately 105–110 °F mixed water; not independently measured in this survey.')
comp('dhw','Domestic distribution & gravity recirculation','No recirculation pump reported','House distribution → right Polaris Cold Inlet','The tempered domestic supply leaves TMV-2. A passive gravity return descends between the tanks and wraps around the right tank to its lower Cold Inlet. Domestic and space-heating circuits share potable water. No separating heat exchanger is reported.','domestic-caleffi-mixer-top.jpg|mechanical-room-overview.jpg','Homeowner traced','The drawing simplifies domestic fixtures and branch piping; flow rate and detailed balancing/check-valve arrangement were not surveyed.')
comp('a1','AHU-1 · basement hydronic air handler','Lennox AM30Q2/3-70-2','Basement · left of Polaris tanks','Receives its own heating branch from the elbow beyond the two supply tees. An internal Taco pumps water through the heating coil; the blower transfers heat to air. The coil returns to the common heating return near the left Polaris. The MABS equipment connection is inferred, not traced end to end.','basement-am30-nameplate.jpg|basement-am30-controls-overview.jpg|basement-am30-wiring-diagram.jpg',extra='Serial 5898M07675 · 120 V · water inlet maximum 180 °F. Internal pump Taco 006-B4-11. Separate cooling coil C26-41-1, serial 6099H46722, HCFC-22; its 450 psi rating is refrigerant-side, not water pressure. Duct distribution is outside this guide’s scope.')
comp('a2','AHU-2 · attic hydronic air handler','Lennox AM30Q2-40-2','Attic mechanical room','First branch on the upstairs main loop, connected by closely spaced supply and return tees. Its internal Taco serves the water coil; the blower provides supplemental forced-air heat. Its suspected pump problem is separate from Mix 2’s missing demand.','attic-mechanical-room-overview.jpg|attic-am30-nameplate.jpg|attic-am30-circulator-nameplate.jpg',extra='Serial 5801K48409 · maximum water inlet 180 °F. Internal Taco 006-B4-11. Nearby disconnect is labeled “Furnace.” Stage 2 retaining stage 1 is homeowner expectation, not a verified interlock.')
comp('pa1','AHU-1 internal water pump','Taco 006-B4-11','Inside basement AM30','Circulates heating water through the basement air-handler coil. Factory AM30 schematic shows the pump/control and freeze-stat circuits; installed optional wiring requires verification.','basement-am30-circulator-nameplate.jpg|basement-am30-wiring-diagram.jpg')
comp('pa2','AHU-2 internal water pump','Taco 006-B4-11','Inside attic AM30','Suspected pump fault has not been independently established. This is a different device from Mix 2 and Var 2. Exact-model cartridge research points to 006-040RP; availability and supersession are unresolved.','attic-am30-circulator-nameplate.jpg|attic-mechanical-room-overview.jpg','Identity confirmed; fault unconfirmed','Lennox AM30-40 catalog kit: 99K70 / 99K7001. Direct manufacturer cross-reference to 006-040RP remains unverified. Generic 005-020RP listing excludes 006-B4-11.')
for id,name,photo,desc in [('living','Living Area / Main','mix-1-zone-valves-and-manifolds.jpg','ZCM-1 left channel. Also called Living Room or Rest of First Floor. Working isolated end switch changed from OL satisfied to continuity on a call.'),('bed','Master Bedroom','mix-1-zone-valves-and-manifolds.jpg','ZCM-1 center channel. Shares Mix 1 circulation with the other first-floor zones.'),('bath','Master Bath','mix-1-zone-valves-and-manifolds.jpg','ZCM-1 right channel. Floor-sensor thermostat relationship and staging remain unresolved.'),('rest','Rest of Second Floor','rest-of-second-floor-manifold.jpg','ZCM-2 left channel. Attic air panel Zone 1 is labeled Bedroom 1 & 2. Isolated end switch stayed OL after apparent motor-driven opening.'),('yellow','Yellow Room / Bedroom Above Garage','yellow-room-manifold.jpg','ZCM-2 middle channel. Attic air panel Zone 2. Valve is Honeywell V8043E1061; isolated red end-switch leads stayed OL after apparent motor-driven opening.')]:
 comp(id,name,'Honeywell zone valve · V8043E1061 confirmed only for Yellow Room','Attic' if id in ('rest','yellow') else 'Behind Polaris tanks',desc+' Each valve feeds a radiant manifold; the floor-loop returns combine in its mixed circuit.',photo+'|'+('attic-plumbing-wall.jpg' if id in ('rest','yellow') else 'mix-1-var-1-piping.jpg'),extra='Manifold loop counts and room-by-room loop routing were not verified. Do not infer other valve models from the Yellow Room nameplate.')
comp('bm','Basement radiant manifold','Model not recorded','Behind basement mixer and circulator','Receives the dedicated Taco discharge. Return feeds the cool port of TMV-1 and continues to the common heating return by the expansion tanks.','basement-radiant-mixer-and-circulator.jpg')
comp('exp','Two expansion tanks','Models and precharge unrecorded','Behind Polaris · lower right','Connected at the common heating return from upstairs. Expansion capacity and condition were not assessed. The basement radiant return joins just downstream toward the left Polaris.','mechanical-room-behind-polaris.jpg','Location and connection homeowner traced')
comp('gauge','Mix 1 temperature / pressure gauge','Combination instrument · model unread','Between Mix 1 and three first-floor zone valves','Photo shows approximately 90 °F and 65 psi. The lower dial has both psi and feet of water scales. This is a measuring instrument, not a pressure-reducing valve.','basement-temperature-pressure-gauge.jpg',extra='One snapshot with operating conditions and accuracy unknown. A pressure-reducing valve was not identified along the traced cold feed; absence elsewhere is not proven.')
for id,name,model,loc,desc,photo,status in [('s1','SUP 1 · mixed supply sensor','Model unverified','Immediately upstream of Mix 1','Blue leads splice to red/white in thermostat cable. Red is seen at MC-1 terminal 23 Sup1; full cable identity and white termination unverified.','mix-1-var-1-piping.jpg','Likely assignment'),('s2','SUP 2 · mixed supply sensor','tekmar 071','Immediately upstream of Mix 2','Blue sensor leads enter insulation. Field conductors are reported at MC-1 17 Com and 20 Sup2. These are sensor conductors, not Mix 2 demand.','sup-2-sensor-at-mix-2.jpg','Homeowner traced'),('ret','Common heating return probe','Model unverified · likely BRet','Behind Grundfos, left of expansion tanks','On common return downstream of basement radiant return tee. Likely MC-1 terminal 25 BRet; cable termination unverified.','common-heating-return-probe.jpg','Likely assignment'),('out','Outdoor sensor','Model unrecorded','Outside by air conditioners','Homeowner confirms an outdoor sensor. Likely connection to MC-1 terminal 26 Out; end-to-end trace not completed.','duomix-201-terminal-strip.jpg','Likely assignment')]:
 comp(id,name,model,loc,desc,photo,status)
comp('air','High-point air eliminator','Model unrecorded','Attic · beside Honeywell zone valve','Homeowner identifies this vent at the high point and reports it in service.','attic-plumbing-wall-right.jpg')
comp('mc','MC-1 · hydronic mixing controller','Wirsbo DuoMix 201 · A3030005','Gray basement controls cabinet · upper left','Receives Mix 1 and Mix 2 demands, switches their distribution pumps, and controls the Var injection outputs. Its Boiler Enable contacts switch the Grundfos main-loop pump in this installation. The Polaris heaters regulate themselves; Boiler Enable is not traced to their burners.','duomix-201-terminal-strip.jpg',extra='Made by tekmar · faceplate March 1999. Do not substitute proMix documentation or assume equivalence to tekmar 374. Exact installed settings, LCD OPEN meaning, delays and interlocks remain unverified.')
for id,n in [('z1',1),('z2',2)]:
 comp(id,f'ZCM-{n} · radiant zone control module','Wirsbo A303XX0003','Gray cabinet · '+('upper' if n==1 else 'lower')+' right board','Interfaces the radiant zones and their feedback with a shared ES demand circuit. ZCM-1 ES brown conductor reaches MC-1 terminal 1; ZCM-2 upper ES red reaches MC-1 terminal 3. The distinct right-edge OUTPUT strip is not the ES pair.','zcm-relay-and-zone-tags.jpg|IMG_649A2520-DDED-4B0A-90D1-2B3277D7D58F.jpeg',extra='Connected lower TELESTAT R1/R2 voltage cannot establish end-switch closure or board health. Upper THERMOSTAT terminals 2/3 are a different group. A3031003 is only an unverified replacement candidate.')
comp('relays','External black interface relays','MARS 90293 / White-Rodgers 90-293Q on upper pair','Above radiant ZCM boards','Two black relays are visible above ZCM-1; three above ZCM-2. Traced pattern: ZCM upper THERMOSTAT 2 → relay lug 2 (red), THERMOSTAT 3 → relay lug 4 (white). SB and 4 are unused on checked strips. Coil/contact roles and thermostat staging topology are not fully established.','zcm-relay-and-zone-tags.jpg|zcm1-mars-relay.jpg|zcm1-white-rodgers-relay.jpg|zcm2-right-relay.jpg','Partial trace','White transformer conductor bridges upper relays and the brown Honeywell relay, apparently as coil common. A 24 V common is not a 120 V neutral. Cable tags label cables, not necessarily the nearest relay.')
comp('br','Basement radiant switching relay','Honeywell R8222D1014','Gray controls cabinet · brown relay beside MC-1','24 VAC coil operates contacts switching 120 VAC to the basement radiant Taco. Its control lead appears to enter a thermostat cable; the far endpoint is not traced. Shared white transformer conductor also reaches the upper black relays.','cabinet-honeywell-switching-relay.jpg|cabinet-honeywell-relay-nameplate.jpg','Pump output traced; control source inferred')
comp('xf','Control transformer','24 VAC · exact model unrecorded','Gray controls cabinet','Provides low-voltage control power. Shared white wiring to brown relay and upper black relays appears to be coil common. Exact ES return and transformer-side terminal mapping remains incomplete.','IMG_7022FFF1-C3BA-44C6-AFE5-CBCE2010FDEF.jpeg','Partial trace')
comp('panel1','ZCP-1 · basement air-zone panel','Trol-A-Temp MABS EZ-4','Gray cabinet · below MC-1','Zone 1 Living Area, Zone 2 Master Bedroom, Zone 3 Basement; Zone 4 visibly unwired. Equipment cable likely runs to basement AM30. TL/TL is the supply-air sensor interface, with a likely probe near the air-handler discharge. Both routes are unverified end to end.','mabs-ez4-board.jpg|mabs-ez4-wiring-diagram.jpg',extra='Do not confuse MABS panel with MARS relay brand. Basement forced-air heat/cooling use and stage count are not confirmed. Downstream dampers are outside the present survey.')
comp('panel2','Attic air-zone panel','Honeywell / Trol-A-Temp MiniZone EMM-3','Attic wall below zone valves','Zone 1 Bedroom 1 & 2 = Rest of Second Floor. Zone 2 Bedroom Above Garage = Yellow Room. Zone 3 visibly unwired. Equipment connection to attic AM30 is inferred.','attic-minizone-board.jpg|attic-minizone-cover.jpg',extra='Cover defines M1 common, M4 power open, M6 power closed. Those are air-damper terminals, not the hydronic valve end switch. Zone 1 M6 white/M1 red; Zone 2 M6 green/M1 blue observed.')
comp('stats','Room thermostats & staging','Models not recorded','Living Area, Master Bedroom, upstairs rooms, basement; separate Master Bath control','Owner describes radiant as first-stage heat and forced air as supplemental stage 2. The exact relay/staging wiring has not been fully traced. The homeowner expects stage 1 to stay on with stage 2; that remains an operating hypothesis.','zcm-relay-and-zone-tags.jpg|mabs-ez4-board.jpg','Staging unverified','With failed upstairs valve feedback, a thermostat call alone has not produced MC-1 Mix 2 demand. Therefore stage overlap alone does not prove the main loop will run during an upstairs forced-air call.')
# All diagram geometry is editable source. Dots indicate junctions; crossings without dots do not.
COL={'hot':'#c94540','mix':'#d18420','ret':'#2675b8','cold':'#2675b8','lv':'#267f72','line':'#343e50','inf':'#8b6db1'}
def start(w,h,title):
 return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(title)}" xmlns="http://www.w3.org/2000/svg"><defs>'+''.join(f'<marker id="arrow-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="{v}"/></marker>' for k,v in COL.items())+'</defs>'
def label(x,y,t,size=16,anchor='start',cls=''):
 return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" class="{cls}">{E(t)}</text>'
def pipe(points,kind='hot',dash=False,arrow=True):
 p=' '.join(f'{x},{y}' for x,y in points)
 return f'<polyline points="{p}" fill="none" stroke="{COL[kind]}" stroke-width="{3 if kind in ("lv","line","inf") else 5}" stroke-linejoin="round" {"stroke-dasharray=\"8 6\"" if dash else ""} '+(f'marker-end="url(#arrow-{kind})"' if arrow else '')+'/>'
def dot(x,y,kind='hot'):
 return f'<circle cx="{x}" cy="{y}" r="6" fill="{COL[kind]}"/>'
def node(id,x,y,kind='box',title=None,sub=None,w=190):
 c=C[id];title=title or c['name'].split(' · ')[0]
 s=f'<g class="component" data-id="{id}" tabindex="0" role="button" aria-label="{E(c["name"])}"><title>{E(c["name"]+" — "+c["model"])}</title>'
 if kind=='pump':
  s+=f'<circle cx="{x}" cy="{y}" r="24" fill="white" stroke="#25384a" stroke-width="2.5"/><path d="M{x-10} {y-14}L{x+15} {y}L{x-10} {y+14}Z" fill="#25384a"/>'+label(x,y+48,title,16,'middle')
 elif kind=='up':
  s+=f'<circle cx="{x}" cy="{y}" r="24" fill="white" stroke="#25384a" stroke-width="2.5"/><path d="M{x-14} {y+10}L{x} {y-15}L{x+14} {y+10}Z" fill="#25384a"/>'+label(x-40,y+5,title,16,'end')
 elif kind in ('valve','tmv'):
  s+=f'<path d="M{x-23} {y-17}L{x+23} {y+17}V{y-17}L{x-23} {y+17}Z" fill="white" stroke="#25384a" stroke-width="2"/>'
  if kind=='tmv':s+=f'<path d="M{x-17} {y+25}L{x} {y}L{x+17} {y+25}Z" fill="white" stroke="#25384a" stroke-width="2"/>'
  else:s+=f'<path d="M{x} {y-17}V{y-30}" stroke="#25384a"/><rect x="{x-12}" y="{y-48}" width="24" height="18" rx="2" fill="white" stroke="#25384a"/>'+label(x,y-34,'M',12,'middle')
  s+=label(x,y-37 if kind=='tmv' else y+49,title,16,'middle')
 elif kind=='tank':
  s+=f'<rect x="{x-65}" y="{y-65}" width="130" height="130" rx="25" fill="#fff" stroke="#25384a" stroke-width="2.5"/>'+label(x,y-7,title,18,'middle')+label(x,y+18,'Polaris',14,'middle')
 elif kind=='sensor':
  s+=f'<circle cx="{x}" cy="{y}" r="16" fill="white" stroke="#25384a" stroke-width="2"/>'+label(x,y+5,'T',14,'middle')+label(x,y-27,title,14,'middle')
 elif kind=='exp':
  s+=f'<ellipse cx="{x}" cy="{y}" rx="32" ry="25" fill="white" stroke="#25384a" stroke-width="2"/><path d="M{x-30} {y}H{x+30}" stroke="#25384a"/>'+label(x,y+48,title,14,'middle')
 else:
  s+=f'<rect x="{x-w/2}" y="{y-34}" width="{w}" height="68" rx="8" fill="white" stroke="#64768a" stroke-width="1.6"/>'+label(x,y-3,title,16,'middle')+label(x,y+18,sub or c['model'].split(' · ')[0],12,'middle')
 s+='</g>';return s

def plant():
 s=start(1400,700,'Heating plant and independent basement branches')
 s+=label(40,38,'01 / HEATING PLANT & BASEMENT BRANCHES',20)
 s+=label(40,67,'Tank positions follow the entrance photo. Pipe geometry is schematic; arrows show intended flow.',15)
 # Return and tanks, hot header
 s+=pipe([(1350,570),(140,570),(140,465)],'ret')+pipe([(205,400),(330,400)])+pipe([(460,400),(1250,400)])
 s+=node('wh1',140,400,'tank','Left tank')+node('wh2',395,400,'tank','Right tank')
 s+=label(242,385,'Series',14,'middle')+label(570,382,'Heating supply header',16)
 # pump main branch A
 s+=pipe([(900,400),(900,140),(1260,140)])+dot(900,400)+label(1265,146,'A → MAIN LOOP',16)
 s+=label(925,180,'Second tee → Grundfos',14)
 # basement hot/mixed circuit
 s+=pipe([(570,400),(570,280),(627,280)])+dot(570,400)
 s+=pipe([(650,280),(810,280)],'mix')+node('tm1',650,280,'tmv','TMV-1')+node('b',810,280,'pump','Basement Taco')
 s+=pipe([(835,280),(1030,280)],'mix')+node('bm',1140,280,title='Basement floors',w=210)
 s+=pipe([(1245,280),(1300,280),(1300,550),(1100,550),(1100,570)],'ret')+dot(1100,570,'ret')
 # feedback cool return line shows branch under supply circuit not connected on crossing
 s+=pipe([(1300,340),(1120,340),(1120,350),(650,350),(650,305)],'ret')+dot(1300,340,'ret')
 s+=label(750,345,'Radiant return → TMV-1 cool port',13)
 # ahu branch descends from end header
 s+=pipe([(1250,400),(1250,465),(1080,465)])+node('a1',980,465,title='AHU-1',sub='Basement AM30',w=180)
 s+=pipe([(890,465),(850,465),(850,570)],'ret')+dot(850,570,'ret')
 s+=label(1100,435,'Elbow → AHU-1',13)
 s+=label(640,445,'First tee → basement radiant',13)
 # Main return enters upstream of the expansion connections and basement return tee.
 s+=pipe([(1370,500),(1370,570),(1350,570)],'ret')+label(1370,482,'B / main return',14,'end')
 s+=node('exp',1220,620,'exp','Expansion tanks ×2')+pipe([(1220,570),(1220,595)],'ret',arrow=False)+dot(1220,570,'ret')
 s+=node('ret',340,570,'sensor','Likely BRet')
 s+=label(650,610,'Common heating return → left tank Heating System Inlet',16,'middle')
 s+=label(40,662,'Domestic connections use separate tank ports; see the Domestic water view. Main-loop A/B ports continue in the next view.',15)
 return s+'</svg>'
def mainloop():
 s=start(1400,680,'Grundfos main loop with attic and first-floor branches')
 s+=label(40,38,'02 / GRUNDFOS MAIN LOOP',20)+label(40,66,'One continuous main loop. The first-floor injection circuit draws from the returning leg after the attic.',15)
 s+=pipe([(45,220),(1350,220),(1350,520),(45,520)],'hot')
 # replace return part blue visually
 s+=pipe([(1350,330),(1350,520),(45,520)],'ret')
 s+=label(45,200,'A',19)+label(45,550,'B → common return',15)
 s+=node('g',210,220,'pump','Grundfos')
 # AHU closely spaced tees
 s+=pipe([(450,220),(450,125),(700,125),(700,180),(510,180),(510,220)],'hot')
 s+=dot(450,220)+dot(510,220)+node('a2',575,125,title='AHU-2',sub='Attic coil + internal pump',w=220)
 s+=label(480,263,'Closely spaced tees',13,'middle')
 # mix2 branch functional box
 s+=pipe([(940,220),(940,125),(1100,125)],'hot')+pipe([(1100,125),(1190,125),(1190,180),(1000,180),(1000,220)],'ret')
 s+=dot(940,220)+dot(1000,220)+node('m2',1080,125,title='Upstairs radiant',sub='Var 2 → Mix 2 → two zones',w=235)
 s+=label(970,263,'Closely spaced tees',13,'middle')
 s+=label(1308,350,'↓',26)+label(1260,390,'Return',16,'end')
 # mix1 draws right hand supply takeoff on return and returns next left tee
 s+=pipe([(940,520),(940,405),(690,405)],'hot')+pipe([(690,405),(620,405),(620,470),(880,470),(880,520)],'ret')
 s+=dot(940,520,'ret')+dot(880,520,'ret')+node('m1',780,405,title='First-floor radiant',sub='Var 1 → Mix 1 → three zones',w=250)
 s+=label(915,556,'Closely spaced tees',13,'middle')
 s+=label(220,430,'BASEMENT',16)+label(220,460,'First-floor equipment is behind the tanks.',14)
 s+=label(45,615,'Blue means relative return, not street cold water. This returning water remains the heat source for Var 1.',15)
 s+=label(45,642,'The blocks simplify branch internals. Open the injection views for the actual mixing junction order.',15)
 return s+'</svg>'
def injection(n):
 s=start(1400,760,f'Mix {n} and Var {n} injection piping')
 s+=label(40,38,f'0{2+n} / '+('FIRST-FLOOR' if n==1 else 'UPSTAIRS')+' INJECTION CIRCUIT',20)
 s+=label(40,68,'Var adds heat; Mix circulates the floor loops. Zone branches are parallel, each with a valve and manifold.',15)
 s+=pipe([(60,640),(1300,640)],'hot')+label(60,677,'Main loop '+('returning from attic' if n==1 else 'supply after AHU-2 branch'),15)
 s+=pipe([(230,640),(230,240),(350,240)],arrow=False)+dot(230,640)
 s+=node('v'+str(n),230,420,'up','Var '+str(n))
 s+=pipe([(1260,540),(350,540),(350,240)],'ret',arrow=False)
 s+=pipe([(350,540),(350,640)],'ret')+dot(350,540,'ret')+dot(350,640)+dot(350,240)
 s+=pipe([(350,240),(810,240)],'mix')+pipe([(810,150),(810,410)],'mix',arrow=False)+dot(810,240,'mix')
 s+=node('s'+str(n),510,240,'sensor','SUP '+str(n))+node('m'+str(n),650,240,'pump','Mix '+str(n))
 branches=[('bath','Master Bath',150),('bed','Master Bedroom',280),('living','Living Area',410)] if n==1 else [('rest','Rest of 2nd floor',150),('yellow','Yellow Room',410)]
 s+=pipe([(1260,150),(1260,540)],'ret')
 for id,name,y in branches:
  s+=pipe([(810,y),(1000,y)],'mix')+dot(810,y,'mix')+node(id,910,y,'valve',name)
  s+=pipe([(1190,y),(1260,y)],'ret')+dot(1260,y,'ret')+node(id,1095,y,title='Floor manifold',sub=name,w=190)
 s+=label(630,185,'Blended supply',16,'middle')+label(780,573,'Combined manifold returns',16,'middle')
 s+=label(270,710,'Closely spaced main-loop tees',15,'middle')
 s+=label(40,742,'Return sequence: manifolds → takeoff back to main loop → injection junction → sensor / Mix inlet.',15)
 if n==1:s+=node('gauge',750,240,'sensor','T / P')
 return s+'</svg>'
def domestic():
 s=start(1300,600,'Shared domestic hot water and passive recirculation')
 s+=label(40,38,'05 / DOMESTIC HOT WATER',20)+label(40,68,'Shared potable water with space heating. No separating heat exchanger is reported.',15)
 s+=pipe([(50,470),(260,470),(260,340)],'cold')+label(50,500,'Street cold',17)
 s+=node('wh1',260,275,'tank','Left Polaris')+node('wh2',530,275,'tank','Right Polaris')
 s+=pipe([(325,275),(465,275)])+label(395,252,'Intertank',14,'middle')
 s+=pipe([(530,210),(530,145),(780,145)])+node('tm2',800,145,'tmv','TMV-2')
 s+=pipe([(260,470),(800,470),(800,170)],'cold')+dot(260,470,'cold')+label(820,415,'Cold inlet',15)
 s+=pipe([(825,145),(1100,145)],'mix')+node('dhw',1100,145,title='Household hot water',sub='Tempered distribution',w=250)
 s+=pipe([(1100,180),(1100,370),(530,370),(530,340)],'ret')+label(1010,348,'Passive gravity recirculation return',15,'end')
 s+=label(540,395,'Right tank lower Cold Inlet',14)+label(50,540,'Owner-reported temperatures: right tank ~170 °F; domestic mixed outlet ~105–110 °F. Not setpoint recommendations.',15)
 s+=label(50,568,'Heating supply/return ports are omitted here for clarity; they remain connected as shown in the plant view.',15)
 return s+'</svg>'
def controls():
 s=start(1400,850,'Functional controls map with verified and inferred paths')
 s+=label(40,38,'06 / CONTROL RELATIONSHIPS',20)+label(40,67,'Solid = traced / documented relationship. Dashed purple = inferred route or incomplete circuit. Blocks are functional devices.',15)
 s+=node('stats',210,140,title='Thermostats / staging',sub='Exact routing unresolved',w=280)
 s+=node('relays',210,290,title='Black interface relays',sub='2 ↔ 2 red · 3 ↔ 4 white',w=280)
 s+=pipe([(210,174),(210,256)],'inf',True)
 for y,id in [(220,'z1'),(385,'z2')]:
  s+=node(id,590,y,title=id.upper().replace('Z','ZCM-'),sub='A303XX0003',w=210)
  s+=pipe([(350,290),(405,290),(405,y),(485,y)],'lv',arrow=False)
  s+=pipe([(695,y),(790,y),(790,285 if id=='z1' else 315),(855,285 if id=='z1' else 315)],'lv')
 s+=label(735,200,'ES → 1',14)+label(735,413,'ES → 3',14)
 s+=node('mc',970,300,title='MC-1 · DuoMix 201',sub='A3030005',w=230)
 s+=node('living',580,110,title='Main-floor valves',sub='Travel + end-switch feedback',w=240)
 s+=pipe([(580,144),(580,186)],'inf',True)
 s+=node('yellow',580,500,title='Upstairs valves',sub='Both isolated switches stayed OL',w=265)
 s+=pipe([(580,466),(580,419)],'inf',True)
 # outputs
 for y,id,txt in [(110,'g','5–6 Boiler Enable'),(220,'m1','12 Mix1 / N11'),(330,'v1','14 Var1 / N13'),(440,'m2','8 Mix2 / N7'),(550,'v2','10 Var2 / N9')]:
  s+=pipe([(1085,300),(1120,300),(1120,y),(1180,y)],'line')+node(id,1280,y,title=C[id]['name'].split(' · ')[0],sub=txt,w=200)
 s+=node('s2',970,475,title='Pipe / outdoor sensors',sub='SUP1 · SUP2 · BRet · Out',w=230)+pipe([(970,441),(970,334)],'inf',True)
 s+=node('panel1',250,645,title='MABS EZ-4',sub='Living / Master bed / Basement',w=270)+node('a1',630,645,title='AHU-1',sub='Basement AM30',w=190)+pipe([(385,645),(535,645)],'inf',True)
 s+=node('panel2',250,760,title='MiniZone EMM-3',sub='Rest 2nd / Yellow Room',w=270)+node('a2',630,760,title='AHU-2',sub='Attic AM30',w=190)+pipe([(385,760),(535,760)],'inf',True)
 s+=node('br',980,700,title='Honeywell R8222D1014',sub='Independent basement relay',w=255)+node('b',1280,700,title='Basement Taco',sub='Switched 120 V',w=200)+pipe([(1107,700),(1180,700)],'line')
 s+=label(852,760,'Control source not traced end to end.',14)+label(852,786,'No basement radiant demand to MC-1.',14)
 return s+'</svg>'
def electrical():
 s=start(1400,700,'Partial electrical schematic and terminal evidence')
 s+=label(40,38,'07 / VERIFIED LINE-VOLTAGE PATH + PARTIAL DEMAND CIRCUITS',20)
 s+=label(40,70,'Conventional contact and motor symbols. This is a partial circuit record, not a complete installation wiring diagram.',15)
 # top ladder rung
 s+=label(70,130,'120 V L',17)+label(1260,130,'N',17)
 s+=pipe([(95,150),(95,280)],'line',arrow=False)+pipe([(1280,150),(1280,280)],'line',arrow=False)
 s+=pipe([(95,215),(430,215)],'line',arrow=False)+label(410,195,'6',16)
 s+='<circle cx="430" cy="215" r="4" fill="#343e50"/><path d="M430 215L480 185" stroke="#343e50" stroke-width="3"/><circle cx="490" cy="215" r="4" fill="#343e50"/>'
 s+=pipe([(490,215),(925,215)],'line',arrow=False)+label(490,195,'5',16)+f'<g class="component" data-id="g" tabindex="0" role="button" aria-label="Grundfos motor"><circle cx="950" cy="215" r="25" fill="white" stroke="#343e50" stroke-width="2"/>'+label(950,222,'M',20,'middle')+label(950,265,'Grundfos motor',16,'middle')+'</g>'+pipe([(975,215),(1280,215)],'line',arrow=False)
 s+=label(460,260,'MC-1 Boiler Enable · shown open',16,'middle')+label(1160,255,'White return',14,'middle')
 s+=node('mc',460,330,title='MC-1 contact control',sub='Functional control link',w=240)
 s+=pipe([(460,296),(460,240)],'lv',True,False)
 s+=label(70,405,'DEMAND CONDUCTORS — PARTIAL TRACE',18)
 s+=node('z1',220,480,title='ZCM-1 ES',sub='Brown switched lead',w=230)+node('z2',220,600,title='ZCM-2 upper ES',sub='Red switched lead',w=230)
 s+=pipe([(335,480),(740,480)],'lv')+pipe([(335,600),(740,600)],'lv')
 s+=label(755,486,'MC-1 1 / Mix 1 Demand',17)+label(755,606,'MC-1 3 / Mix 2 Demand',17)
 s+=label(70,668,'MC-1 2 ↔ 4 tie observed. ES transformer-side return incompletely traced; no invented neutral or terminal assignments.',15)
 s+=label(1050,465,'24 VAC controls',16)+label(1050,495,'≠ 120 V neutral',16)
 return s+'</svg>'
DIAGRAMS={'plant':plant(),'main':mainloop(),'mix1':injection(1),'mix2':injection(2),'domestic':domestic(),'controls':controls(),'electrical':electrical()}
# Sensor gauge placement above is corrected to the actual distribution outlet; SUP sensors remain inlet-side.
# Embed a single optimized photo copy per original. Originals are never modified.
P={}
for p in sorted((ROOT/'photos').iterdir()):
 if p.suffix.lower() not in ('.jpg','.jpeg','.png') or p.name in ('contact_sheet.jpg',):continue
 with Image.open(p) as im:
  im=ImageOps.exif_transpose(im).convert('RGB'); im.thumbnail((1920,1920)); buf=io.BytesIO(); im.save(buf,format='JPEG',quality=86,optimize=True)
 P[p.name]='data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
# Include the valve nameplate attachment when available, preserving a local evidence copy.
valve=Path('/tmp/codex-remote-attachments/01a1bbc6-4c60-7ed2-b853-e97046ab0171/9CA27878-65E3-4CB4-8180-7D38CFFB790B/1-Photo-1.jpg')
if valve.exists():
 dest=ROOT/'photos/yellow-room-honeywell-valve-nameplate.jpg'
 if not dest.exists():dest.write_bytes(valve.read_bytes())
 with Image.open(dest) as im:
  im=ImageOps.exif_transpose(im).convert('RGB');im.thumbnail((1920,1920));buf=io.BytesIO();im.save(buf,format='JPEG',quality=86,optimize=True)
 P[dest.name]='data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode();C['yellow']['photos'].append(dest.name)
# Source chapters remain available offline as plain, searchable, downloadable Markdown.
NOTES=[dict(file=p.name,title=p.read_text().splitlines()[0].lstrip('# '),text=p.read_text()) for p in sorted((ROOT/'notes').glob('*.md'))]
# Captions extracted from catalog headings and image labels.
CAT={}
raw=(ROOT/'notes/08-photo-catalog.md').read_text()
for part in re.split(r'^## ',raw,flags=re.M)[1:]:
 title=part.splitlines()[0]
 for alt,file in re.findall(r'!\[([^]]*)\]\(\.\./photos/([^)]*)\)',part):CAT[file]=dict(title=title,caption=alt)
for k in P:CAT.setdefault(k,dict(title=k.replace('-',' ').rsplit('.',1)[0],caption='Field photograph; see component details for interpretation.'))
DATA=dict(components=C,photos=P,catalog=CAT,notes=NOTES)
template=(HERE/'template.html').read_text()
for key,svg in DIAGRAMS.items():
 svg=svg.replace('arrow-',key+'-arrow-')
 template=template.replace('{{'+key+'}}',svg)
template=template.replace('{{DATA}}',json.dumps(DATA,ensure_ascii=False).replace('</','<\\/'))
out=ROOT/'report/index.html';out.parent.mkdir(exist_ok=True);out.write_text(template)
print(f'Built {out}: {out.stat().st_size/1048576:.1f} MiB; {len(C)} components, {len(P)} embedded photographs, {len(DIAGRAMS)} diagrams.')
