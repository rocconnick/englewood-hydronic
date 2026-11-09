# Master index

## Active diagnosis — 2026-11-07

**Problem:** Upstairs Mix 2 mixed-water circulator does not receive 120 V at DuoMix 201 terminal 8 during upstairs demand, while working first-floor Mix 1 terminal 12 energizes on its call.

**Wiring breakthrough:** ZCM-1 **ES** brown -> DuoMix **1 (Mix 1 Demand)**; ZCM-2 **ES** red -> DuoMix **3 (Mix 2 Demand)**. DuoMix terminals **2/4 tied**. Lower ES other terminal (white) runs to upper radiant zone control module and toward a 24 VAC transformer. **ES/ES and OUTPUT are separate terminal groups.**

**Current diagnosis:** Both upstairs valves moved open during calls, but their isolated end switches stayed OL. The working Living Room switch changed from OL to continuity. ZCM-2 ES stayed near 27 VAC during calls while working ZCM-1 dropped to about 1 VAC. Missing valve feedback explains the observed demand failure. ZCM-2 response to verified feedback remains untested.

**Next:** Inspect upstairs valve travel and end-switch actuation, then verify feedback at ZCM-2 and Mix 2 demand at MC-1. See [troubleshooting](notes/05-troubleshooting.md), [wiring](notes/04-wiring-discoveries.md), and [open questions](notes/06-open-questions.md).

**Working convention:** Markdown is the authoritative incremental knowledge base; Word document archived. Preserve evidence, uncertainty, corrections, photographs and measurements; keep this index current. Persona-specific digests will be derived later.

**Second active issue:** The attic AHU-2 circulator is Taco **006-B4-11**. Taco specifies **006-040RP**, with availability and supersession unverified. See the [cartridge crosswalk](notes/05-troubleshooting.md#ahu-2-cartridge-identification-and-availability). Pump failure remains unconfirmed.

**Interactive report:** [Open the generated HTML report](report/index.html) (new standalone field guide; rebuild via `reporting/build.py`; details in [reporting README](reporting/README.md)).

## Terminology standard

Use [approved component terms and equipment tags](notes/12-terminology-and-equipment-tags.md) throughout. **MABS EZ-4** is the confirmed basement air-zone panel. **MARS** is a separate relay manufacturer. Installed staging remains unverified.

## Navigation

1. [System architecture and equipment](notes/01-system-architecture.md)
2. [Zones, thermostats and air handlers](notes/02-zones-and-staging.md)
3. [Controls and terminal reference](notes/03-controls-terminals.md)
4. [Wiring discoveries and relays](notes/04-wiring-discoveries.md)
5. [Mix 2 fault investigation and diagnostic history](notes/05-troubleshooting.md)
6. [Questions, unknowns, next tests](notes/06-open-questions.md)
7. [Chronology of conversation and corrections](notes/07-conversation-history.md)
8. [Photo catalog with embedded originals](notes/08-photo-catalog.md)
9. [Reference files, source notes and external links](notes/09-reference-sources.md)
10. [Work handoff instructions and ongoing note templates](notes/10-work-handoff.md)
11. [Report brief / active-issue summaries](notes/11-report-brief.md)
12. [Approved terminology and equipment tags](notes/12-terminology-and-equipment-tags.md)
13. [Current guide synthesis and scope](notes/13-guide-synthesis.md)
14. [Machine-readable asset manifest](MANIFEST.tsv)

The **original proposed piping schematic** is visible in the photographs `IMG_3BA...` and `IMG_612...`; a detail crop is `cropzones.png`. It is proposed, not necessarily installed. The **black relay / ZCM-2 radiant zone control module close-up** is `IMG_28E...`.
