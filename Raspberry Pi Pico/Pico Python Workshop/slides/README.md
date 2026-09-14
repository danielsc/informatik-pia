# Teacher slides

These Reveal.js decks contain the explicit teaching and guided-practice portion
of each workshop day. The daily Markdown lessons contain the student lab,
wiring diagrams, and coding tasks.

## View online

Open the hosted workshop at:

<https://danielsc.github.io/informatik-pia/>

The site is deployed automatically from `master` by GitHub Actions whenever
the workshop materials or deployment workflow change.

## Present a deck

Choose the deck for the current day:

| Day | Teacher deck | Student lab |
|---|---|---|
| 1 | [`day-1.html`](day-1.html) | [`../day-1-make-it-light.md`](../day-1-make-it-light.md) |
| 2 | [`day-2.html`](day-2.html) | [`../day-2-make-it-decide.md`](../day-2-make-it-decide.md) |
| 3 | [`day-3.html`](day-3.html) | [`../day-3-make-it-reusable.md`](../day-3-make-it-reusable.md) |
| 4 | [`day-4.html`](day-4.html) | [`../day-4-make-it-sense.md`](../day-4-make-it-sense.md) |
| 5 | [`day-5.html`](day-5.html) | [`../day-5-parking-assistant.md`](../day-5-parking-assistant.md) |

The decks load a pinned version of Reveal.js from jsDelivr and keep workshop
images local. The shared design and authoring rules are documented in
[`SLIDE_PRINCIPLES.md`](SLIDE_PRINCIPLES.md).

Useful controls:

| Key | Action |
|---|---|
| arrow keys or Space | move through slides and reveals |
| `S` | open the presenter view with speaker notes and timer |
| `F` | enter fullscreen |
| `O` or Esc | show the slide overview |
| `?` | show Reveal.js keyboard help |

To serve the whole workshop locally from its root:

```bash
python3 -m http.server 8000
```

Then open, for example:

```text
http://localhost:8000/Raspberry%20Pi%20Pico/Pico%20Python%20Workshop/slides/day-1.html
```

Add `?print-pdf` to the URL and use the browser's print dialog to create a PDF
handout.

## Teaching sources

The decks adapt the teaching progression from the actual TEALS lesson decks
and lesson documents. TEALS labs are replaced by the workshop's Pico builds and
coding tasks. Hardware imports, constructors, specialised timing calls, and
safety cleanup are presented as supplied API vocabulary rather than syntax
students must reproduce from memory.
