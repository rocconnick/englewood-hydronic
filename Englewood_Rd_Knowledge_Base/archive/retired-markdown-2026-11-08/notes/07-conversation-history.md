# 07 — Reconstructed conversation history, corrections and reasoning

**This is a detailed topical reconstruction, not a word-for-word transcript.** Exact full previous-chat text was not provided as an export. Some earlier photos may have been discussed before the currently mounted set; all locally mounted original images are included.

1. **System discovery.** User established two Polaris heaters in series, six installed radiant zones, five air thermostats, two AM30 hydronic air handlers, separate basement Caleffi mixing, and DuoMix dual mixed circuits. Original piping diagram is proposed and includes uninstalled Garage Entry.
2. **Control identification.** DuoMix 201 part A3030005 / March 1999; earlier research about proMix 201 and tekmar 374 was recognized as potentially conflated. Board terminal functions and LCD labels were photographed.
3. **Symptom isolated.** First-floor call produces 120 V at DuoMix terminal 12, while upstairs call does not energize terminal 8. DuoMix LCD appears unchanged on upstairs call.
4. **Wirsbo lower radiant zone control module inspection.** Zone 1 yellow indicator responds to Rest of Second Floor thermostat. Top terminal strips labeled THERMOSTAT; bottom TELESTAT; right side OUTPUT. LED semantics were initially over-interpreted; currently **unverified**.
5. **Historic replacement box.** Handwritten note 'no output on zone 3' found inside a replacement radiant zone control module box. Which board, date, channel and type of output unclear. User did not yet confirm whether an old board is in the box.
6. **Distinct OUTPUT strip.** User recognized the right-side OUTPUT is separate from THERMOSTAT and TELESTAT. This suggests a possible demand interface to DuoMix, but **no physical trace established**.
7. **MABS question.** User asked whether MABS or Wirsbo receives thermostat signal first. Assistant hypothesized MABS first, explicitly **not verified**; alternative direct-to-Wirsbo exists.
8. **Telestat definition.** Assistant explained Wirsbo thermal actuator mechanism, but user corrected: actual installed zone valves are **Honeywell motorized valves**. Thus generic Wirsbo thermal actuator photos and opening delays must not be assumed to describe installed valves.
9. **Black relay photo.** User showed three black modules above ZCM-2 radiant zone control module, another three above upper. Wires lead to Wirsbo THERMOSTAT terminals. Hypotheses: isolation/staging relays, valve control, contact logic; not yet identified.
10. **Multiconductor cable tracing.** User found brown-sheathed cables leaving cabinet. Yellow Room's brown/blue conductors connect to DuoMix 17 COM and 20 SUP 2; a pipe-mounted sensor is present, so these are supply-temperature sensing, not zone demand. Rest of Second Floor cable's brown wires route to external black relays (possibly two different relays). Other conductors in sheath serve thermostat functions. Cable co-location is not evidence of common purpose.
11. **Supply sensor versus VAR2.** Sensor informs variable injection pump modulation/temperature regulation; Mix 2 Demand at 3–4 is distinct and remains key unknown.
12. **Master document.** A v0.1 DOCX and PDF were generated with 11 sections, zone table, terminal map, hypotheses, 18 initial open questions. Both archived in this ZIP. The present Markdown knowledge base expands that transfer with source files and all available photos.
13. **Current request.** User wants all available photos and comprehensive Markdown reference/index in a ZIP to bring into ChatGPT Work. This bundle is that portable handoff.

## Claims explicitly withdrawn or downgraded
- 'MABS definitely comes before Wirsbo' → unproven.
- 'Yellow LED proves thermostat demand output' → LED may instead indicate TELESTAT/output; manual needed.
- 'Telestat actuators are installed' → false; Honeywell valves installed.
- 'Black relays open zone valves' → plausible, not proven.
- 'Right-side OUTPUT directly feeds DuoMix 3–4' → plausible, not traced.
- 'DuoMix 201 is tekmar 374' → unverified model cross-reference.
- 'Supply 2 temperature sensor initiates Mix 2 mixed-water circulator' → incomplete; sensor modulates temperature control, distinct from heat demand.
- 'Historic zone 3 fault explains present zone 1 problem' → no evidence of direct causal link.

## 2026-11-07 — ES wiring, multimeter and comparative diagnostic readings
Homeowner confirmed demand wiring: ZCM-1 ES brown -> DuoMix 1; lower ES red -> DuoMix 3; lower ES white -> upper radiant zone control module -> apparent transformer; DuoMix 2/4 tied. The distinct OUTPUT terminals were differentiated from ES. The multimeter was correctly in V~ AC mode; an earlier assistant misreading was corrected. Upper ES read 27.2 VAC with no first-floor call, ~1 VAC with call; lower ES read 27.2 VAC with both upstairs zones calling and both satisfied. Leading fault hypothesis: lower ES contacts not closing or a required condition for closure not being met. Root cause unconfirmed.

## Upstairs valve feedback and working comparison

The Yellow Room valve nameplate confirmed Honeywell V8043E1061. Its red switch leads splice to a green/yellow pair with matching colors at ZCM-2 TELESTAT R1/R2. Both upstairs valves opened on a call, but their isolated end switches stayed OL. The working Living Room switch changed from OL to continuity. Connected R1/R2 voltage fell to 0 VAC on both upstairs calls despite the open switches. Defer ZCM-2 replacement until valve feedback is restored and its ES response can be tested. The separate attic AM30 circulator was identified as Taco 006-B4-11. See the [field tests and cartridge research](05-troubleshooting.md).
