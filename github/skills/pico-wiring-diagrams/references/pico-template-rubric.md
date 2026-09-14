# Pico Template Placement Rubric

This rubric applies to the reusable Pico footprint in
`templates/wiring-diagram.html`.

## Vertical-centering score

Measure the outer breadboard rectangle and the green Pico board rectangle after
applying the Pico group's translation:

```text
breadboard centre Y = breadboard Y + breadboard height / 2
Pico centre Y       = Pico Y + translation Y + Pico height / 2
offset              = absolute difference between the two centres
```

| Score | Vertical centre offset | Result |
|---:|---:|---|
| 4 | 0-4 px | Excellent; visually centred |
| 3 | over 4 px through 13.5 px | Pass; within half one breadboard row pitch |
| 2 | over 13.5 px through 27 px | Revise; visibly displaced by up to one row |
| 1 | over 27 px through 54 px | Major revision |
| 0 | over 54 px | Unusable placement |

The template requires **4/4**, even though 3/4 is acceptable for a finished
diagram whose components force a small layout adjustment.

## Placement gates

The template also fails if:

- USB is not on the left;
- either terminal field exposes a clipped partial row of holes;
- either two-row power bank exposes a third clipped row;
- the Pico does not begin at the leftmost usable terminal-field hole;
- the Pico is not horizontal;
- the upper and lower header rows do not occupy opposite breadboard terminal
  fields;
- the Pico does not cross the centre channel;
- any signal, power, ground, or control label is missing or out of order.

## Current template audit

| Measurement | Value |
|---|---:|
| Breadboard bounds | `y=96`, `height=500` |
| Breadboard centre | `346 px` |
| Lower terminal rows | Five complete rows; no clipped row below the channel |
| Power-rail rows | Exactly two complete rows per bank |
| Pico local bounds | `x=78`, `y=195`, `width=520`, `height=192` |
| Green PCB bounds | `x=78`, `y=195`, `width=520`, `height=175` |
| Pico translation | `55 px` |
| First header-pin X | `91 px` (leftmost terminal-field hole) |
| Pico silkscreen font | `700 12 px Arial/Helvetica` |
| Pico silkscreen labels | Reference style: `0`-`28`, `GND`, and power/control names |
| Rendered Pico centre | `346 px` |
| Absolute offset | `0 px` |
| Vertical-centering score | **4/4 — PASS** |

The USB connector and PCB begin at the left edge of the terminal fields, the
board is horizontal, the header rows land in opposite terminal fields, the
board crosses the centre channel, and all 40 reference-style silkscreen labels
are present in official pin order without a redundant physical-number layer.
