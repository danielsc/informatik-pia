# Pico-to-Breadboard Pin Alignment Rubric

This rubric applies to all 40 Pico header-pad centres in
`templates/wiring-diagram.html`.

## Measurement

The breadboard hole grid is:

```text
hole X = origin X + column × horizontal pitch
hole Y = origin Y + row × vertical pitch
```

For every Pico pin, calculate the shortest horizontal and vertical distance to
a breadboard-hole centre after applying the Pico group's translation.

```text
pin error = max(horizontal distance, vertical distance)
```

The template score uses the **largest error among all 40 pins**. One misaligned
pin therefore fails the whole template.

## Scoring

| Score | Maximum error on either axis | Result |
|---:|---:|---|
| 4 | exactly `0.00 px` within floating-point tolerance | Perfect pixel alignment |
| 3 | over 0 through 0.50 px | Visually aligned, but template must be corrected |
| 2 | over 0.50 through 1.00 px | Revise |
| 1 | over 1.00 through 2.00 px | Major revision |
| 0 | over 2.00 px | Misaligned |

The reusable template requires **4/4**. Finished diagrams derived from the
template must preserve the same pitch and alignment.

## Placement gates

The alignment check also fails if:

- there are not exactly 20 pins in each header row;
- horizontal Pico pin pitch differs from breadboard hole pitch;
- either header row sits outside a five-hole terminal field;
- the pin positions are represented only by metadata and disagree with the
  rendered SVG geometry.
- any silkscreen label reads in a direction other than bottom-to-top;
- a silkscreen label is more than `0.50 px` from its header-pad centre;
- the labels in either row do not share a uniform pin-side anchor line;
- the upper label row is not exactly `1 px` from its header edge;
- the lower label row is not exactly `3 px` from its header edge.

## Current template audit

| Measurement | Value |
|---|---:|
| Breadboard hole origin | `(13, 13.5)` |
| Breadboard pitch | `26 × 27 px` |
| First Pico pin X | `91 px` |
| Pico pin pitch | `26 px` |
| Rendered top-header Y | `256.5 px` |
| Rendered bottom-header Y | `418.5 px` |
| Maximum X error | `0.00 px` |
| Maximum Y error | `0.00 px` |
| Silkscreen writing direction | Bottom-to-top on both rows |
| Maximum label-to-pad X error | `0.48 px` |
| Top label-to-header gap | `1.00 px` |
| Bottom label-to-header gap | `3.00 px` |
| Pins checked | `40` |
| Score | **4/4 — PASS** |
