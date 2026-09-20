# Copilot instructions

## Repository architecture

- The main maintained project is the five-day Raspberry Pi Pico workshop under
  `Raspberry Pi Pico/Pico Python Workshop/`. Other root-level notes and source
  documents support the teaching material but are not part of the deployed site.
- The workshop is a static site. GitHub Pages deploys the workshop directory
  verbatim from `master`; there is no package-manager build step. `index.html`
  selects a language, `en/` and `de/` are language landing pages, and
  `slides/day-N.html` preserves old URLs by redirecting to the English decks.
- Each day spans several coupled surfaces:
  - `workshop/en/` and `workshop/de/`: detailed student labs and teacher guides;
  - `slides/en/` and `slides/de/`: Reveal.js teacher presentations;
  - `code/day-N/`: shared MicroPython starters, solutions, and examples;
  - `diagrams/`: canonical standalone HTML/inline-SVG circuits and sibling PNGs.
  Treat the lesson, deck, program, wiring reference, and diagram as one system.
- `code/teacher-tests/` contains hardware-preparation checks, not a host-side
  unit-test suite. Programs run on a Pico through Thonny with the
  **MicroPython (Raspberry Pi Pico)** interpreter.
- `.github/skills/pico-wiring-diagrams` is a symlink to the tracked
  `github/skills/pico-wiring-diagrams/` implementation. It contains diagram
  templates, component artwork, rubrics, render tooling, and structural/
  geometry checkers.
- `wokwi/` is an optional potentiometer/RGB-pixel experiment. It is separate
  from the physical component-test workflow.

## Run and validate

Run commands from the repository root; quote workshop paths because they
contain spaces.

Serve the static site locally:

```bash
python3 -m http.server 8000
```

Then open
`http://localhost:8000/Raspberry%20Pi%20Pico/Pico%20Python%20Workshop/`.

Render one wiring diagram and update its committed PNG:

```bash
bash .github/skills/pico-wiring-diagrams/scripts/render-preview.sh \
  "Raspberry Pi Pico/Pico Python Workshop/diagrams/ordinary-led.html" \
  "Raspberry Pi Pico/Pico Python Workshop/diagrams/ordinary-led.png"
```

Run the checks for one diagram:

```bash
diagram="Raspberry Pi Pico/Pico Python Workshop/diagrams/ordinary-led.html"
python3 .github/skills/pico-wiring-diagrams/scripts/check-diagram.py "$diagram"
python3 .github/skills/pico-wiring-diagrams/scripts/check-breadboard-endpoints.py "$diagram"
python3 .github/skills/pico-wiring-diagrams/scripts/check-routing-overlaps.py "$diagram"
python3 .github/skills/pico-wiring-diagrams/scripts/check-rail-stripes.py "$diagram"
```

When changing the reusable wiring template, run its geometry checks:

```bash
template=.github/skills/pico-wiring-diagrams/templates/wiring-diagram.html
python3 .github/skills/pico-wiring-diagrams/scripts/check-pico-centering.py "$template"
python3 .github/skills/pico-wiring-diagrams/scripts/check-pico-pin-alignment.py "$template"
python3 .github/skills/pico-wiring-diagrams/scripts/check-pico-footprint.py "$template"
python3 .github/skills/pico-wiring-diagrams/scripts/check-breadboard-endpoints.py "$template"
python3 .github/skills/pico-wiring-diagrams/scripts/check-routing-overlaps.py "$template"
python3 .github/skills/pico-wiring-diagrams/scripts/check-rail-stripes.py "$template"
```

When changing the component gallery:

```bash
python3 .github/skills/pico-wiring-diagrams/scripts/check-component-library.py \
  .github/skills/pico-wiring-diagrams/templates/components.html
bash .github/skills/pico-wiring-diagrams/scripts/render-preview.sh \
  .github/skills/pico-wiring-diagrams/templates/components.html \
  .github/skills/pico-wiring-diagrams/templates/components.png
```

For one physical hardware test, build the linked circuit from
`code/teacher-tests/README.md`, open that single `.py` file in Thonny, and run
it on the Pico. Stop and disconnect USB before changing wiring. The optional
Wokwi pixel-spinner simulation is exposed as the VS Code task
`Wokwi: Run teacher pixel spinner`.

For slide changes, serve the site, render every affected English and German
deck in Chromium at 1280 x 720, inspect every slide and presenter notes, verify
local links/assets, and finish with:

```bash
git diff --check
```

## Project conventions

- English is the source language. Change English first, then update the matching
  German lesson or deck in the same change. Preserve matching section/slide
  order, activities, safety warnings, links, code blocks, and speaker notes.
- Do not translate Python, filenames, paths, identifiers, code comments, exact
  output strings, GPIO/pin names, electrical units, part numbers, commands,
  shortcuts, or URLs. Shared code, diagrams, and technical assets must not be
  duplicated into language directories.
- Keep student-facing material age-appropriate and free of curriculum-source
  provenance such as TEALS. Preserve required source and image attribution in
  `SOURCES_AND_IMAGES.md` and teacher-facing documentation.
- Slides teach concepts and guided practice; Markdown lessons contain the
  detailed lab, wiring, code links, and extensions. Every deck uses Reveal.js
  at 1280 x 720 through shared `workshop-slides.js`, includes speaker notes on
  every slide, and uses an explicit classroom-state label such as **Try in
  Thonny** or **Build while unplugged** when student activity changes.
- Introduce a circuit immediately before students build it: name its purpose
  and code file, require USB disconnection, show the complete PNG, link the
  scalable HTML/connection table, state pins/polarity/protection, require an
  unplugged check, and only then reconnect for the smallest test.
- Use the established course pin plan and safety design in
  `workshop/en/WIRING_AND_SAFETY.md`. In particular, GPIO is 3.3 V only,
  ordinary LEDs need current-limiting resistors, the buzzer uses its transistor
  driver, and HC-SR04 Echo reaches GP18 through the 1 kΩ/2 kΩ divider. Keep
  voltages, resistor values, thresholds, and pin assignments identical across
  code, lessons, slides, diagrams, and both languages.
- MicroPython examples use English names/comments, named uppercase hardware
  constants, timeout-safe sensor reads, and `try`/`finally` cleanup for PWM,
  pixels, and outputs. Preserve starter/solution scaffolding and do not expose
  solution files as the normal student workflow.
- For diagram work, follow the `pico-wiring-diagrams` skill and its rubrics
  rather than inventing new SVG geometry or component artwork. Start from the
  canonical template/component library, keep the exact HTML connection table
  synchronized with the drawing and code, render with Chromium, inspect
  visually, and commit both the standalone `.html` and sibling `.png`.
- Existing local workshop assets stay local. Reveal.js is the intentional
  pinned external dependency. Preserve meaningful localized alt text and avoid
  links or text over circuit diagrams.
