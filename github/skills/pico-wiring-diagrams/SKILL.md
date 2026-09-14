---
name: pico-wiring-diagrams
description: Create and refine original, classroom-ready Raspberry Pi Pico breadboard wiring diagrams as standalone HTML with inline SVG. Use when asked to make, improve, audit, or embed wiring diagrams for the Pico workshop, especially diagrams inspired by Freenove's physical breadboard style.
---

# Pico Wiring Diagrams

Create wiring illustrations that are electrically correct, safe for students,
visually similar in purpose to the Freenove kit diagrams, and original in
execution. Use deterministic HTML and inline SVG. Do not use an image model.

## Repository context

The course lives in:

```text
Raspberry Pi Pico/Pico Python Workshop/
```

Put finished diagrams in:

```text
Raspberry Pi Pico/Pico Python Workshop/diagrams/
```

Before changing or creating a diagram, read:

1. `Raspberry Pi Pico/Pico Python Workshop/workshop/en/WIRING_AND_SAFETY.md`
2. The lesson that will use the diagram
3. The corresponding MicroPython program in `code/`
4. `references/quality-rubric.md` in this skill
5. The existing `diagrams/button-and-led.html` exemplar when present
6. `references/pico-template-rubric.md` when changing the reusable template
7. `references/pico-pin-alignment-rubric.md` when changing Pico or breadboard
   geometry
8. `references/pico-footprint-rubric.md` when changing board dimensions,
   component geometry, or the Pico clip boundary
9. `references/breadboard-endpoint-rubric.md` when adding any wire, component,
   module, or connector
10. `references/routing-clarity-rubric.md` when routing power, ground, signals,
    component leads, or module connectors
11. `references/component-library.md` and `templates/components.html` before
    drawing any workshop component

Treat the lesson, code, and wiring guide as one system. If they disagree, fix
the inconsistency rather than choosing one silently.

## Non-negotiable safety gates

Stop and correct the design if any gate fails:

- Never route 5 V into a Pico GPIO.
- Pico GPIO uses 3.3 V logic and is not 5 V tolerant.
- Show a current-limiting resistor for every ordinary LED.
- Show the transistor driver for a buzzer when the course circuit requires it.
- Show the HC-SR04 Echo divider: Echo → 1 kΩ → GP18 junction, with 2 kΩ
  from that junction to GND.
- Connect all circuit grounds.
- Distinguish VBUS/5 V from 3V3(OUT).
- Check polarity for LEDs, transistors, sensors, and modules.
- Show that USB power must be disconnected while wiring.
- Do not claim that an illustrative hole position is exact.

Critical electrical, pin, component, switch, and safety rubric categories must
score 4/4. A merely attractive diagram is not acceptable.

## Workflow

### 1. Establish the circuit before drawing

Read the code and source documentation. Write a netlist with one row per
electrical path:

| From | Through | To | Purpose |
|---|---|---|---|
| Pico pin | component/value | destination | signal or power role |

Record:

- GPIO name and physical pin number;
- component value and polarity;
- power voltage;
- input/output direction;
- shared nodes;
- protection components;
- software constant that uses the pin.

Do not infer the netlist from a photograph alone. Confirm it against code,
Pico documentation, and component specifications.

### 2. Inspect the visual reference

When a Freenove diagram is supplied, inspect it for:

- Pico orientation and approximate scale;
- breadboard orientation, rails, centre channel, row letters, and columns;
- component placement and relative size;
- wire colours and right-angle routing;
- which details make the circuit easy to reproduce.

Match its useful physical-computing visual language, not its exact artwork.
Do not trace, embed, or copy Freenove image pixels, logos, or proprietary
illustrations. Attribute the factual source and link to the official page.

### 3. Create a standalone HTML/SVG file

Start from `templates/wiring-diagram.html`. The output must:

- use HTML5 with one inline `<svg>`;
- define a responsive SVG `viewBox`;
- use `role="img"` and `aria-labelledby`;
- include SVG `<title>` and `<desc>`;
- use vector shapes, paths, patterns, gradients, and text;
- avoid `<canvas>`, base64 images, and remote image dependencies;
- include print CSS;
- include a visible legend;
- include a text `figcaption`;
- include an exact HTML connection table below the drawing.

The template already contains the canonical Pico footprint. Preserve its:

- USB-left horizontal orientation;
- vertical centring on the breadboard;
- position across the breadboard centre channel, with one header row in each
  terminal field;
- exact horizontal and vertical alignment between every Pico header-pad centre
  and a breadboard-hole centre;
- leftmost placement, beginning at the first usable terminal-field column;
- actual 40-pin physical ordering;
- complete GPIO, ADC, power, ground, and control labels.

All Pico silkscreen labels read bottom-to-top. Centre each label exactly on
the X coordinate of its pad. Keep the upper label row on a uniform anchor line
`1 px` below its header edge and the lower row `3 px` above its header edge.
Do not add a second layer of physical pin numbers to the board artwork.

Do not replace the labelled Pico with a generic rectangle. If the finished
circuit uses only a few pins, highlight those pads and keep the remaining
silkscreen labels available for orientation.

Reuse the canonical component artwork from `templates/components.html`.
Copy the needed symbol definitions into the finished standalone diagram; do
not link the diagram to the gallery. Preserve component proportions, polarity
marks, pin labels, and resistor bands.

Instantiate every component at its canonical, unscaled `viewBox` width and
height. Do not enlarge or shrink component symbols per diagram. Canonical
resistors are exactly `104 × 24 px`: the body is two `26 px` breadboard
pitches long, and each light-grey metal lead adds one pitch, for four pitches
lead-to-lead.

Use semantic groups with `aria-label` for the Pico, breadboard, each component,
and explanatory inset.

### 4. Draw in physical layers

Draw from back to front:

1. page background and title;
2. breadboard body;
3. power rails, terminal holes, row letters, and column numbers;
4. Pico and module bodies;
5. relevant pins and pin labels;
6. jumper wires;
7. resistors and component leads;
8. LEDs, buttons, sensors, buzzers, and transistors;
9. callouts, legends, and safety checks.

Use a landscape breadboard as the dominant object. Keep component proportions
close to real hardware. Components should not become oversized teaching icons.
The breadboard may be widened to a maximum of 80 hole columns when a combined
circuit needs more routing space. Preserve the canonical `26 px` horizontal
hole pitch, extend all hole fields and rails consistently, and never shrink
canonical components to fit. Use only as much width as improves readability;
an unnecessarily wide board makes the rendered PNG harder to read.

### 5. Use consistent visual conventions

Default wire colours:

| Meaning | Colour |
|---|---|
| positive power | red |
| ground | black |
| digital/analogue input | blue |
| controlled output | green |
| secondary signals | yellow or violet, with a label |

Colour alone is insufficient. Label every relevant GPIO and include a legend.
Route wires orthogonally where practical. Avoid ambiguous crossings; use a
visible junction dot only where conductors connect.

Do not overlap wires, component leads, connector contacts, or component
connection points unless the circuit cannot be laid out clearly without doing
so. Prefer separate parallel lanes. If a crossing is unavoidable, keep it
away from holes and component terminals and use an explicit bridge treatment
that cannot be mistaken for a junction.

Use the breadboard power rails as shared buses when that shortens routes or
makes power distribution easier to understand:

- label every energized rail `3.3 V`, `5 V`, or `GND`;
- connect a rail to the matching Pico supply or ground before using it;
- never assume a rail is powered merely because it has a red or blue stripe;
- use both top and bottom rails when doing so reduces long wires or crossings;
- do not force signals onto rails or add rail jumpers that make the diagram
  harder to follow.

Draw each power-rail bank with its colour stripes outside the two hole rows:
the upper stripe sits half a row pitch above the first row and the lower stripe
sits half a row pitch below the second. Use the same distance for the top and
bottom rail banks.

Every electrical element that contacts the breadboard must be in
`#circuit-connections` and declare:

- `data-connection-kind="wire"`, `"component"`, or `"connector"`;
- `data-breadboard-ends="start"`, `"end"`, `"both"`, or `"center"`.

Use `<line>` or `<polyline>` for leads and jumpers and `<circle>` for a single
connector pin. The declared rendered endpoint or centre must coincide exactly
with a visible breadboard-hole centre. Do not use metadata as a substitute for
matching SVG geometry.

Each visible breadboard hole may contain exactly one physical contact. Never
place two component leads, jumper ends, or connector pins in the same hole,
even when they belong to the same electrical net. Join them through separate
holes in the same connected five-hole terminal strip or through separate holes
on the same powered rail. A junction dot does not make stacked contacts
physically buildable.

A hole hidden beneath a component body is unavailable. Give each placed
component a final-coordinate `data-obscures-holes="x1,y1,x2,y2"` bounding box
covering the part of its body that sits over the breadboard. Route every lead
and jumper endpoint to a visible hole outside all such bounds; use another hole
in the same connected strip rather than drawing a connection under a part.

Every component lead, connector pin, and jumper-cable end must terminate
exactly at a hole centre, and that hole must show a circular dot in the
connector's declared colour. For line-based leads, declare
`data-contact-start-color` and/or
`data-contact-end-color`, then add a same-colour
`data-contact-marker="true"` circle at each declared electrical endpoint.
For jumper wires, use a standard `wire-*` class so the checker can derive the
marker colour, or declare the endpoint colours explicitly when the two ends
differ.
Connector circles declare `data-contact-color` directly. A contact marker is
only a visual cap: it must not carry `data-connection-kind` and does not count
as a second physical contact.

Default resistor bands:

| Value | Bands |
|---:|---|
| 220 Ω | red, red, brown, gold |
| 330 Ω | orange, orange, brown, gold |
| 1 kΩ | brown, black, red, gold |
| 2 kΩ | red, black, red, gold |
| 10 kΩ | brown, black, orange, gold |

For ordinary LEDs, label `A`/anode/long leg and `K`/cathode/short leg. For a
four-leg tactile button, explicitly show:

- the two permanently connected terminal-A legs;
- the two permanently connected terminal-B legs;
- A and B open while released;
- A and B joined while pressed;
- correct placement across the breadboard centre channel.

### 6. Make the diagram buildable

Every visible path must be traceable from source to destination. Ensure:

- wires end at pins, leads, or breadboard nodes rather than floating nearby;
- connected conductors share an endpoint or junction dot;
- disconnected crossings do not look joined;
- physical pin positions follow the actual Pico order;
- resistor bands agree with text labels;
- component legs plausibly enter breadboard holes;
- the exact connection table matches the drawing and code.

If hole placement is illustrative, state that explicitly and rely on labelled
electrical endpoints plus the exact connection table. Never invite students to
count holes in a non-exact illustration.

### 7. Render, inspect, score, and iterate

Never stop after writing SVG source. Render it:

```bash
bash .github/skills/pico-wiring-diagrams/scripts/render-preview.sh \
  "Raspberry Pi Pico/Pico Python Workshop/diagrams/example.html" \
  "Raspberry Pi Pico/Pico Python Workshop/diagrams/example.png"
```

The preview must be rendered by the same browser engine used to inspect the
HTML, preferably headless Chromium. Do not use macOS Quick Look when Chromium
is available: Quick Look can position SVG `<use>` instances differently from
the browser while leaving separately drawn contact markers unchanged. Compare
the PNG against the browser-rendered SVG at endpoint-level zoom before
accepting it.

Commit the sibling PNG and embed it in the relevant Markdown lesson. GitHub
can display committed SVG and PNG files, but it does not render an HTML page
as an image. Keep the HTML link for the scalable, accessible version and use
the PNG for the inline GitHub preview.

Open the generated PNG with an image-viewing tool. Inspect at normal size for:

- visual similarity to the physical Freenove reference;
- component scale and placement;
- wire endpoints and crossings;
- text collisions or clipped labels;
- resistor-band correctness;
- Pico pad ordering;
- polarity and terminal clarity;
- sufficient contrast without relying on colour alone.

Then run:

```bash
python3 .github/skills/pico-wiring-diagrams/scripts/check-diagram.py \
  "Raspberry Pi Pico/Pico Python Workshop/diagrams/example.html"
```

When changing the component library, also run:

```bash
python3 .github/skills/pico-wiring-diagrams/scripts/check-component-library.py \
  .github/skills/pico-wiring-diagrams/templates/components.html

bash .github/skills/pico-wiring-diagrams/scripts/render-preview.sh \
  .github/skills/pico-wiring-diagrams/templates/components.html \
  .github/skills/pico-wiring-diagrams/templates/components.png
```

When creating or changing the reusable template itself, also run:

```bash
python3 .github/skills/pico-wiring-diagrams/scripts/check-pico-centering.py \
  .github/skills/pico-wiring-diagrams/templates/wiring-diagram.html

python3 .github/skills/pico-wiring-diagrams/scripts/check-pico-pin-alignment.py \
  .github/skills/pico-wiring-diagrams/templates/wiring-diagram.html

python3 .github/skills/pico-wiring-diagrams/scripts/check-pico-footprint.py \
  .github/skills/pico-wiring-diagrams/templates/wiring-diagram.html

python3 .github/skills/pico-wiring-diagrams/scripts/check-breadboard-endpoints.py \
  .github/skills/pico-wiring-diagrams/templates/wiring-diagram.html

python3 .github/skills/pico-wiring-diagrams/scripts/check-routing-overlaps.py \
  .github/skills/pico-wiring-diagrams/templates/wiring-diagram.html

python3 .github/skills/pico-wiring-diagrams/scripts/check-rail-stripes.py \
  .github/skills/pico-wiring-diagrams/templates/wiring-diagram.html
```

Score the rendered diagram against every category in
`references/quality-rubric.md` and `references/routing-clarity-rubric.md`.
Record the audit beside the diagram or in the course's diagram rubric file.

Iterate until:

- every category meets its stated threshold;
- every critical category is 4/4;
- no automatic-fail condition is present.

Do not inflate scores to finish. A score of 2 means revise and render again.

### 8. Integrate the finished diagram

For a reusable component or intermediate circuit, link the HTML and embed the
sibling PNG in both the relevant daily lesson and the matching component
section of `WIRING_AND_SAFETY.md`.

Keep a final-project integration diagram in the final lesson rather than
duplicating it in `WIRING_AND_SAFETY.md`. The shared wiring guide may retain
the pin plan and a concise link to that lesson. Keep the official Freenove
source link for comparison and attribution, and describe each new diagram as
original course artwork informed by the source rather than as an official or
endorsed Freenove diagram.

## Completion report

Report:

- the diagram path;
- the lesson and code it matches;
- meaningful visual and electrical decisions;
- rubric scores, including any category at 3/4;
- any remaining limitation, especially illustrative hole placement.

Do not say the diagram is complete until it has been rendered and every rubric
category passes.
