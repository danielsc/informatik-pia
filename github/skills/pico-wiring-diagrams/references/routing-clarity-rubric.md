# Routing and Rail Clarity Rubric

Use this rubric for every breadboard wiring diagram.

## 1. Conductor separation

Inspect every jumper, component lead, connector contact, and electrical
endpoint at normal rendering size.

| Score | Evidence |
|---:|---|
| 4 | No avoidable overlaps or crossings; parallel routes have visible separation; every endpoint remains unobscured |
| 3 | One unavoidable crossing is clearly bridged away from holes and terminals |
| 2 | A crossing or short overlap is understandable only after close inspection |
| 1 | Several overlaps obscure routes or connection points |
| 0 | A route can reasonably be mistaken for a short, junction, or different endpoint |

The required score is **4/4** unless an unavoidable crossing is documented in
the diagram audit, in which case a clearly rendered bridge may score 3/4.
Collinear overlap between different conductors is never acceptable.

## 2. Power-rail use

Use rails when they reduce long routes, repeated supply wires, or crossings.
Do not energize unused rails merely to satisfy this rubric.

| Score | Evidence |
|---:|---|
| 4 | Every used rail is explicitly connected and voltage-labelled; top and/or bottom rails are used wherever they materially simplify the circuit |
| 3 | Rail use is safe and labelled, but one direct supply route would be clearer through a rail |
| 2 | Rails are underused or create unnecessary long wires |
| 1 | Rail state is difficult to infer or colour is the only voltage indication |
| 0 | A rail is mislabelled, assumed powered without a source connection, or distributes an unsafe voltage |

The required score is **4/4**.

## 3. Rail-stripe geometry

Each top or bottom power-rail bank contains two hole rows. The colour lines
frame those pins rather than running through them:

```text
upper stripe
    13.5 px
first hole row
    27 px
second hole row
    13.5 px
lower stripe
```

With the canonical 27 px vertical hole pitch, both stripe-to-pin distances
must be exactly `13.5 px`. The top and bottom banks must use identical
geometry. This category requires **4/4** and fails for any non-zero alignment
error.

## Automatic failures

The diagram fails if:

- one conductor covers another for any non-zero length;
- a conductor crosses a component pin, connector pad, or breadboard endpoint
  without electrically joining it;
- a crossing can be mistaken for a junction;
- a used rail lacks a visible source connection or voltage/ground label;
- a red or blue rail stripe is treated as an electrical source by itself.

Run `scripts/check-routing-overlaps.py` to reject collinear overlap and
non-endpoint intersections among declared wires, component leads, and
connector lines. Visual review is still required for component bodies, labels,
and rail usage.

Run `scripts/check-rail-stripes.py` to verify that all four colour stripes
frame their rail pins symmetrically.
