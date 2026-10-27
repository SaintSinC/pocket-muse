# Pocket Muse

**Pocket Muse is a pocket-sized voice companion that brings Muse Spark
off the screen and into your hand — talk to it, and it answers out
loud and shows pictures and cards on its round display.**

A submission to the **Meta Global AI Developer Hackathon** (Indie
Developer track, theme: **Build for Your World**), built solo by
Saint, an indie developer in San Diego.

---

## What Pocket Muse does

You carry a small round-screen gadget in your pocket. Press its button and talk:

- *"What's the weather at my house in Texas?"* — it answers out loud
and shows a weather card.
- *"Show me a tiger."* — a picture is drawn and appears on the round display.
- *"How much is gold today?"* — it checks and tells you.

No phone screen, no typing. Voice in, voice + picture out.

## What was built during the hackathon (Oct 27 – Nov 4, 2026) — the new work

This repository contains the work created **during the event**:

- **The Pocket Muse Brain** — a service that gives the gadget real
skills, powered by the **Meta Model API**:
  - Muse Spark reasons over what you asked and picks a skill.
  - Skills include live weather cards, picture generation via **Muse
Image** rendered to the gadget's round display, and quick fact/price
lookups.
- **An open-weights lane** — the same brain can run on **Muse Spark
Open** (`meta-models/muse-spark-open-1026`), served by Baseten, so the
gadget's intelligence is not tied to a single endpoint.
- The request/response plumbing between the gadget and the Brain, and
the card/picture rendering pipeline for the 466×466 round display.

## What pre-exists (the stage, not the submission)

The physical gadget and its firmware platform were built **before**
the hackathon and are **not** claimed as hackathon work:

- ESP32-S3 handhelds (a Waveshare 1.75″ AMOLED board and an AIPI Lite)
running Meta's Muse gadget SDK firmware, paired to the Muse app.
- A text-to-speech patch so the gadget speaks Muse's replies aloud
instead of only showing text.

The hackathon project is the **Brain and its skills** — the new
intelligence the gadget calls — built on top of that pre-existing
platform.

## Status

- [x] Public repo created (Oct 27) — github.com/SaintSinC/pocket-muse
- [x] First Meta Model API call (Muse Spark) from the Brain
- [x] First Muse Spark Open call via Baseten
- [ ] Skill 1 end-to-end: ask by voice → answer spoken → card/picture
on the round screen
- [ ] Demo video
- [ ] Submission via Cerebral Valley (due Nov 4, 6:00 PM PT)

## Credits

- Meta Model API credits provided for the hackathon.
- Baseten credits provided for the hackathon (Muse Spark Open serving).

---

*Built with Muse — fittingly, Pocket Muse is both the project and the
story: a non-traditional builder using AI to give AI a body.*
