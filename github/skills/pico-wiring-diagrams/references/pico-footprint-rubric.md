# Pico Footprint Rubric

The reusable Pico drawing must occupy no more than:

- **20 breadboard columns horizontally**, and
- **six terminal-row pitches plus the centre channel vertically**.

This rubric applies to the entire rendered `#pico` group, not only the green
PCB. USB, pads, labels, shadows, and decorative parts must not render outside
the footprint.

## Required dimensions

Using the template breadboard geometry:

```text
maximum width  = 20 × 26 px = 520 px
maximum height = 6 × 27 px + 30 px centre channel = 192 px
```

## Scoring

| Score | Overflow beyond either maximum | Result |
|---:|---:|---|
| 4 | exactly `0.00 px` | Exact footprint |
| 3 | over 0 through 0.50 px | Visually close, but template must be corrected |
| 2 | over 0.50 through 2.00 px | Revise |
| 1 | over 2.00 through one breadboard pitch | Major revision |
| 0 | over one pitch | Unusable footprint |

The reusable template requires **4/4**.

## Containment gates

The template also fails if:

- the green PCB exceeds the declared footprint;
- any Pico subcomponent renders outside the footprint;
- the green PCB centre is shifted from the centre of its two header-pad rows;
- the Pico group does not use the declared footprint as an SVG clip path;
- the clip rectangle and declared bounds disagree;
- footprint metadata disagrees with breadboard pitch or channel height.

Annotations outside the Pico group are allowed, but pin labels belong inside
the Pico group and must therefore fit inside the same footprint.

## Current template audit

| Measurement | Value |
|---|---:|
| Horizontal pitch | `26 px` |
| Column count | `20` |
| Maximum width | `520 px` |
| Pico footprint width | `520 px` |
| Green PCB width | `520 px` |
| Vertical pitch | `27 px` |
| Row-pitch count | `6` |
| Centre-channel height | `30 px` |
| Maximum height | `192 px` |
| Pico footprint height | `192 px` |
| Green PCB height | `175 px`, centred on the two fixed header rows |
| PCB-to-header centre offset | `0.00 px` on both axes |
| Maximum overflow | `0.00 px` |
| Score | **4/4 — PASS** |
