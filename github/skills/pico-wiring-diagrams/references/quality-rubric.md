# Wiring Diagram Quality Rubric

Use this rubric for every diagram created by this skill.

## Scale

| Score | Meaning |
|---:|---|
| 4 | Excellent: accurate, immediately usable, no correction needed |
| 3 | Pass: correct and usable, with minor presentational limitations |
| 2 | Revise: ambiguity or visual weakness could cause mistakes |
| 1 | Major revision: incomplete, misleading, or difficult to follow |
| 0 | Unsafe or unusable |

## Required categories

| # | Category | Passing evidence | Threshold |
|---:|---|---|---:|
| 1 | Physical-reference resemblance | Landscape breadboard, physically represented Pico/components, realistic proportions, coloured jumper routing, and a composition recognisably serving the same purpose as the source reference | 3 |
| 2 | Electrical net correctness | Every power, ground, input, and output path matches the intended circuit; no shorts, floating required connections, or ambiguous junctions | **4** |
| 3 | Pico pin accuracy | GPIO names, physical pin numbers, visual board positions, voltage rails, and code constants agree | **4** |
| 4 | Breadboard buildability | Paths are traceable, legs and placement are physically plausible, endpoints land on holes, avoidable overlaps are absent, and shared power rails are used where they improve clarity | 3 |
| 5 | Component accuracy | Type, value, polarity, terminal names, resistor bands, and transistor orientation are correct | **4** |
| 6 | Interaction/orientation clarity | Buttons, potentiometers, sensors, and directional modules clearly show orientation and state changes relevant to the activity | **4** |
| 7 | Readability | No collisions, clipping, or avoidable conductor overlaps; labels are legible at normal size; crossings and junctions are unambiguous; colour has text support | 3 |
| 8 | Safety and failure prevention | Voltage limits, power-off instruction, protection parts, polarity, common ground, and pre-power checks are visible or adjacent | **4** |
| 9 | Accessibility and portability | Responsive vector output, semantic title/description, printable styling, text alternative, and no image-model or remote-image dependency | 3 |
| 10 | Source independence and attribution | Original vector artwork, source acknowledged, and no copied pixels, traced artwork, protected logo, or endorsement implication | **4** |

## Automatic failures

The diagram fails regardless of score if it:

- routes 5 V into a Pico GPIO;
- omits a required resistor, divider, transistor, or common ground;
- conflicts with the matching program's GPIO constants;
- shows a tactile switch orientation that permanently closes the intended path;
- reverses a polarised component;
- contains an ambiguous crossing that could reasonably create a short;
- overlaps wires, leads, or connector points in a way that obscures an
  endpoint or could be mistaken for an electrical junction;
- places two component leads, jumper ends, or connector pins in the same
  breadboard hole instead of using separate holes in one connected strip;
- uses any breadboard hole obscured by a component body as a connection point;
- scales a component away from the canonical dimensions defined by the
  component library;
- omits a hole-centred, colour-matched connector dot from any component lead,
  connector pin, or jumper-cable endpoint;
- uses a wrong resistor value or colour code;
- claims illustrative holes are an exact placement plan;
- was not rendered and visually inspected.

## Audit template

```markdown
| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 |  | PASS/REVISE | |
| 2 |  | PASS/REVISE | |
| 3 |  | PASS/REVISE | |
| 4 |  | PASS/REVISE | |
| 5 |  | PASS/REVISE | |
| 6 |  | PASS/REVISE | |
| 7 |  | PASS/REVISE | |
| 8 |  | PASS/REVISE | |
| 9 |  | PASS/REVISE | |
| 10 |  | PASS/REVISE | |
```

The outcome is PASS only if every row meets its threshold and no automatic
failure is present.
