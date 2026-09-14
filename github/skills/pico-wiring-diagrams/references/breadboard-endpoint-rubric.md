# Breadboard Electrical Endpoint Rubric

Every electrical contact made by a jumper wire, component lead, or module
connector must land pixel-exactly on the centre of a visible breadboard hole.
This applies to power rails and both terminal fields.

Every displayed hole must also be complete. A hole-field clipping rectangle
must not reveal a partial row at any edge. The lower terminal field therefore
starts above the first complete `f` row, while each power-rail field is clipped
exactly between its upper and lower colour stripes.

## One physical contact per hole

A breadboard hole accepts only one component lead, jumper end, or connector
pin. Two declared electrical contacts may not occupy the same hole, even when
they are part of the same net.

Build shared nodes by placing each contact in a different hole in the same
connected five-hole terminal strip. For a power bus, use separate holes on the
same explicitly powered rail. Do not stack a jumper on a resistor lead or
place a module pin and jumper in one hole. Decorative junction dots do not
count as contacts and must not carry endpoint metadata.

## Obscured holes are unavailable

A breadboard hole covered by a component body cannot be used for any jumper,
lead, or connector contact. Every placed component symbol must declare the
final-coordinate bounds of the body that obscures holes:

```html
<use href="#component-example"
  data-obscures-holes="x1,y1,x2,y2"/>
```

The bounds describe only the opaque component body, not its exposed leads.
They must use final rendered SVG coordinates. If a body needs more than one
rectangle, separate bounds with semicolons. The checker rejects every declared
contact whose hole centre falls inside an obstruction rectangle.

## Connector dots

Every component lead, connector pin, and jumper-cable end must visibly
terminate in a circular dot centred on its breadboard hole. The dot uses the
connector or net colour: power red, ground black, input blue, output green, or
the explicitly labelled secondary-signal colour.

Line-based component contacts declare endpoint colours:

```html
<line data-connection-kind="component" data-breadboard-ends="both"
  data-contact-start-color="#2563eb"
  data-contact-end-color="#111827"/>
<circle data-contact-marker="true" cx="..." cy="..." r="6"
  fill="#2563eb"/>
```

Jumper wires use the standard `wire-red`, `wire-black`, `wire-yellow`,
`wire-input`, `wire-output`, or `wire-violet` class so the checker can infer
their contact-dot colour. A jumper whose endpoints use different colours must
declare them explicitly with the same start/end attributes.

A connector represented directly by a circle declares
`data-contact-color`. Decorative contact markers do not use
`data-connection-kind`; otherwise they would falsely represent a second
physical contact in the hole.

## Measurement

For each declared breadboard-contacting endpoint:

```text
X error = absolute(endpoint X - nearest visible hole centre X)
Y error = absolute(endpoint Y - nearest visible hole centre Y)
endpoint error = max(X error, Y error)
```

The diagram score uses the largest error among all checked endpoints. A point
on the mathematical grid but outside the four visible hole fields does not
count as a breadboard pin.

## Required SVG contract

Put electrical geometry in `#circuit-connections`. Mark each contacting
element with:

```html
data-connection-kind="wire|component|connector"
data-breadboard-ends="start|end|both|center"
```

- `start`, `end`, and `both` apply to `<line>` and `<polyline>`.
- `center` applies to a `<circle>` representing one connector pin.
- A component with several leads marks every lead separately.
- Decorative bodies and labels do not use these attributes.
- Electrical paths must use checkable geometry; an opaque SVG `<path>` is not
  accepted for a breadboard contact.
- Do not apply SVG transforms inside `#circuit-connections`; use final rendered
  coordinates so the checker and visible geometry cannot diverge.

The checker reads the rendered SVG coordinates themselves. Endpoint metadata
alone cannot satisfy this rubric.

## Scoring

| Score | Maximum error on either axis | Result |
|---:|---:|---|
| 4 | exactly `0.00 px` within floating-point tolerance | Pixel-exact |
| 3 | over 0 through 0.50 px | Visually aligned; correction required |
| 2 | over 0.50 through 1.00 px | Revise |
| 1 | over 1.00 through 2.00 px | Major revision |
| 0 | over 2.00 px or outside a visible hole field | Not connected |

Every finished diagram requires **4/4**. A clipped partial hole row, one missing declaration, unsupported
electrical shape, off-grid endpoint, endpoint outside a visible hole field, or
hole occupied by more than one declared contact, or contact beneath a component
body, missing connector/cable dot, off-centre dot, or dot with the wrong colour
is an automatic failure.

## Template audit

The reusable template contains the required `#circuit-connections` layer but
intentionally has no lesson-specific circuit elements. Its breadboard exposes
four explicit hole fields so derived diagrams can be checked without treating
the grid as infinite.
