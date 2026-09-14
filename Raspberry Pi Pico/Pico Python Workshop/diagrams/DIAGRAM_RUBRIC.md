# Wiring Diagram Quality Rubric

Use this rubric for every original course wiring diagram. A diagram passes only
when every category reaches its threshold and no automatic-fail condition is
present.

## Scoring scale

| Score | Meaning |
|---:|---|
| 4 | Excellent: accurate, immediately usable, and needs no correction |
| 3 | Pass: correct and usable, with only minor presentational limitations |
| 2 | Revise: understandable, but ambiguity or visual weakness could cause mistakes |
| 1 | Major revision: incomplete, misleading, or difficult to follow |
| 0 | Unsafe or unusable |

## Categories and thresholds

| # | Category | Passing evidence | Threshold |
|---:|---|---|---:|
| 1 | Freenove-style physical resemblance | Landscape breadboard, Pico and components shown physically, realistic proportions, coloured jumper routing, and a layout recognisably related to the official kit illustration without copying its artwork | 3 |
| 2 | Electrical net correctness | Every power, ground, input, and output path matches the intended circuit; no unintended shorts or floating required connections | **4** |
| 3 | Pico pin accuracy | GPIO names, physical pin numbers, board positions, power rails, and code constants agree | **4** |
| 4 | Breadboard buildability | Connections are visually traceable; component legs and switch placement make physical sense; an exact connection list resolves any hole-placement ambiguity | 3 |
| 5 | Component accuracy | Component type, polarity, terminal names, resistor values, resistor colour bands, and transistor orientation where applicable are correct | **4** |
| 6 | Switch orientation and operation | Permanent terminal pairs, centre-channel placement, released state, pressed state, and active-low result are explicit | **4** |
| 7 | Readability | No overlapping labels, important text is legible at normal size, wire crossings are understandable, and colour is supplemented by labels | 3 |
| 8 | Safety and failure prevention | Power-off instruction, current-limiting resistor, voltage limits, polarity, and a pre-power check are visible or immediately adjacent | **4** |
| 9 | Accessibility and portability | Scalable vector output, semantic title/description, printable styling, text alternatives, and no dependence on an image-generation service | 3 |
| 10 | Source independence and attribution | Original artwork, source relationship acknowledged, and no implication that the new graphic is an official Freenove image | **4** |

## Automatic failures

A diagram fails regardless of its numerical scores if it:

- routes 5 V into a Pico GPIO;
- omits a required current-limiting or protection component;
- disagrees with the corresponding MicroPython pin constants;
- shows a button orientation that makes the intended switch permanently closed;
- reverses a polarised component without explicitly teaching reverse-bias testing;
- uses an ambiguous crossing where a student could reasonably create a short;
- puts two component leads or jumper ends into one breadboard hole;
- uses a hole hidden beneath a component body;
- scales a component away from its canonical component-library dimensions;
- omits a hole-centred dot from any component lead, connector pin, or jumper
  end, or gives a dot a colour that does not match its declared net;
- claims that illustrative breadboard holes are an exact placement plan.

## Shared breadboard-template geometry audit

This audit applies to every diagram below after the shared template correction.

| Category | Score | Evidence |
|---|---:|---|
| Lower terminal-field visibility | **4/4** | Rows `f` through `j` render as five complete rows. The first row below the centre channel is no longer clipped; the Pico-covered `h` row remains hidden beneath the top-view board and pads. |
| Power-rail row count | **4/4** | Each power bank renders exactly two complete hole rows. Its hole field begins at the upper stripe and ends at the lower stripe, so no partial third row is visible. |
| Pico alignment and footprint | **4/4** | All 40 Pico pads retain `0.00 px` hole-alignment error, the Pico remains vertically centred, and the complete footprint retains `0.00 px` overflow. |

**Outcome:** PASS. The shared breadboard geometry has no clipped partial rows,
and all existing electrical endpoints remain on complete, visible holes. The
automated endpoint and rail checks enforce this row-visibility contract for
future diagrams.

## Audit: `button-and-led.html`

Reviewed against the rendered HTML/SVG, the Day 2 program, and the wiring guide.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | Full landscape breadboard; canonical horizontal Pico; realistic LED, resistors, tactile switch, rails, holes, and right-angle coloured wires match the kit reference's physical-computing visual language. |
| 2 | 4 | PASS | 3.3 V → labelled top rail → 10 kΩ → terminal A/GP13; terminal B → labelled top GND rail; GP15 → 220 Ω → LED anode; cathode → labelled bottom GND rail. |
| 3 | 4 | PASS | Canonical Pico geometry places 3V3 pin 36, top-rail GND pin 38, GP13 pin 17, bottom-rail GND pin 13, and GP15 pin 20 in official order; code constants agree. |
| 4 | 4 | PASS | All 28 declared wire, component-lead, and connector endpoints use distinct, unobscured hole centres with 0.00 px error and matching foreground contact dots. |
| 5 | 4 | PASS | The button, LED, 10 kΩ resistor, and 220 Ω resistor use unscaled canonical symbols with obstruction bounds; polarity and both resistor band codes are correct. |
| 6 | 4 | PASS | The canonical button body spans the trench; its left A pair and right B pair each cross it, and the inset explains released and pressed states. |
| 7 | 4 | PASS | Canonical 12 px Pico labels, legend, component values, polarity, non-overlapping orthogonal routes, and foreground button contacts are legible at normal size. |
| 8 | 4 | PASS | The diagram says to disconnect USB, shows both required resistors, labels every energized rail, marks the unused rail, and checks switch placement, polarity, and grounds. |
| 9 | 4 | PASS | Inline SVG scales without loss, includes `title`, `desc`, ARIA labelling, print CSS, a text caption, and an HTML connection table. |
| 10 | 4 | PASS | Caption identifies it as original course artwork informed by the FNK0063 circuit; no Freenove artwork is embedded or traced. |

**Outcome:** all ten categories pass, all four critical electrical/safety
categories score 4, and no automatic-fail condition is present.

## Audit: teacher-test diagrams

The isolated teacher-test diagrams were reviewed against their numbered
programs, the wiring guide, the rendered PNGs, and the same automatic geometry
checks as the lesson diagrams.

| Diagram | Physical reference | Electrical | Pico pins | Buildability | Components | Orientation | Readability | Safety | Accessibility | Independence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `onboard-led.html` | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| `button-only.html` | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| `potentiometer-only.html` | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 4 |

The onboard test intentionally has no external electrical contacts. The
button-only circuit preserves the 10 kΩ active-low pull-up and centre-channel
switch orientation. The potentiometer-only circuit preserves 3.3 V, common
ground, and the GP26/ADC0 wiper; its long separated ADC route accounts for the
honest 3/4 buildability and readability scores. All three have **4/4**
electrical, pin, component, orientation, and safety scores.

### Routing and rail audit: teacher-test diagrams

| Diagram | Conductor separation | Power-rail use | Rail geometry | Endpoint error |
|---|---:|---:|---:|---:|
| `onboard-led.html` | 4/4 | 4/4 | 4/4 | no external endpoints |
| `button-only.html` | 4/4 | 4/4 | 4/4 | 0.00 px |
| `potentiometer-only.html` | 4/4 | 4/4 | 4/4 | 0.00 px |

**Outcome:** PASS. No automatic-fail condition is present.

## Routing and rail audit

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | The automated audit checks 17 routes and 22 segments with no overlaps or ambiguous crossings; GP13 and GP15 use distinct rows. |
| Power-rail use | **4/4** | Pico pin 36 explicitly powers the labelled top 3.3 V rail; pins 38 and 13 explicitly ground the labelled top and bottom GND rails; the unused positive rail is marked unused. |
| Rail-stripe geometry | **4/4** | All four colour stripes frame their two pin rows from the outside at an identical `13.50 px` distance; maximum geometry error is `0.00 px`. |

## Audit: `distance-sensor.html`

Reviewed against `code/day-4/01_distance_sensor.py`, the Day 4 lesson, the
wiring guide, and the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | Full landscape breadboard, canonical Pico, physical HC-SR04, resistor bodies, coloured jumpers, and rail distribution use the kit lesson's physical-computing visual language without copying its image. |
| 2 | 4 | PASS | VBUS powers VCC; GP19 reaches Trig; Echo reaches GP18 only through the 1 kΩ divider leg; the 2 kΩ leg and sensor GND return to common ground. |
| 3 | 4 | PASS | GP19 physical pin 25, GP18 physical pin 24, VBUS physical pin 40, and Pico GND physical pin 13 match the program and official pin order. |
| 4 | 4 | PASS | All 24 checked contacts use distinct, exact, unobscured holes; every component, connector, and jumper endpoint has a hole-centred, net-coloured dot, with zero marker errors. |
| 5 | 4 | PASS | Canonical unscaled HC-SR04 artwork is preserved; both resistors use the native 104 × 24 px component with a two-pitch body and one-pitch metal lead on each side. |
| 6 | 4 | PASS | The sensor faces outward and its VCC/Trig/Echo/GND order is visible; the divider junction is marked. |
| 7 | 4 | PASS | The sensor body, four pin leads, signal routes, divider resistors, junction label, and ground return occupy separate readable bands. |
| 8 | 4 | PASS | The inset requires USB disconnection, identifies 5 V VCC, forbids direct Echo-to-GPIO wiring, and requires common ground and a partner check. |
| 9 | 4 | PASS | Standalone responsive inline SVG includes title, description, ARIA labelling, print CSS, caption, and exact HTML connection table. |
| 10 | 4 | PASS | Original vector artwork is identified as informed by the official Freenove lesson; no remote image, traced pixels, logo, canvas, or base64 content is used. |

**Outcome:** PASS. Every category is **4/4**, and no automatic-fail condition
is present.

### Routing and rail audit: `distance-sensor.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | The automated routing audit reports zero overlaps or ambiguous crossings; Trigger and Echo use separated orthogonal lanes. |
| Power-rail use | **4/4** | Pico VBUS visibly powers the top 5 V rail, a right-edge jumper powers the labelled bottom 5 V rail, and Pico GND powers the labelled bottom GND rail. |
| Rail-stripe geometry | **4/4** | All four stripe distances are exactly `13.50 px`; maximum error is `0.00 px`. |

## Audit: `passive-buzzer.html`

Reviewed against `code/day-4/02_buzzer_test.py`, the Day 4 lesson, the wiring
guide, and the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | Full breadboard, canonical Pico, realistic passive buzzer, resistor, and TO-92 transistor create an original physical kit-style view. |
| 2 | 4 | PASS | GP15 drives the base through 1 kΩ; VBUS feeds buzzer `+`; buzzer `−` reaches collector; emitter returns to Pico GND. |
| 3 | 4 | PASS | GP15 physical pin 20, VBUS physical pin 40, and GND physical pin 13 match the program and Pico pin order. |
| 4 | 4 | PASS | All 19 checked contacts use distinct, exact, unobscured holes; every component, connector, and jumper endpoint has a colour-matched centre dot, with zero marker errors. |
| 5 | 4 | PASS | The unscaled canonical buzzer and S8050 show polarity and `E/B/C`; the 1 kΩ resistor uses its native 104 × 24 px four-pitch lead-to-lead artwork. |
| 6 | 4 | PASS | Buzzer polarity and the transistor's flat-face viewing orientation are explicit at the parts and in the safety inset. |
| 7 | 4 | PASS | Labels remain legible, routes are orthogonal, and no conductor, terminal, or component connection is ambiguously crossed. |
| 8 | 4 | PASS | The inset prohibits direct GPIO drive, identifies the 5 V path, requires common ground, and says to disconnect USB and verify orientation. |
| 9 | 4 | PASS | Responsive inline SVG, semantic title/description, ARIA groups, print CSS, caption, and exact table are present. |
| 10 | 4 | PASS | The caption attributes the factual Freenove source while identifying the vector drawing as original course artwork. |

**Outcome:** PASS. All categories score **4/4**, and no automatic-fail
condition is present.

### Routing and rail audit: `passive-buzzer.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | The routing checker reports zero conflicts; base, switched collector, supply, and emitter routes occupy separate lanes. |
| Power-rail use | **4/4** | VBUS visibly energizes the labelled top 5 V rail used by the buzzer; Pico GND visibly energizes the used bottom GND rail; unused rails are labelled. |
| Rail-stripe geometry | **4/4** | All stripe-to-pin distances are exactly `13.50 px`, with `0.00 px` maximum error. |

## Audit: `proximity-alarm.html`

Reviewed against `code/day-4/03_proximity_alarm.py`, the Day 4 lesson, the
wiring guide, and the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | The widened landscape breadboard keeps the canonical left-aligned Pico and presents the sensor, buzzer, transistor, divider, rails, and jumpers at realistic relative scale. |
| 2 | 4 | PASS | The complete sensor and buzzer nets coexist: GP19 Trigger, protected GP18 Echo, GP15 base drive, VBUS loads, and one common Pico ground. |
| 3 | 4 | PASS | GP19/pin 25, GP18/pin 24, GP15/pin 20, VBUS/pin 40, GND/pin 13, and the onboard `LED` constant all agree with the program. |
| 4 | 3 | PASS | All 39 checked contacts use distinct, exact, unobscured holes; every component, connector, and jumper endpoint has a colour-matched centre dot with zero marker errors, and the GP15 jumper uses the clear lower perimeter. |
| 5 | 4 | PASS | All components use canonical dimensions; every resistor has a two-pitch body plus one-pitch metal leads on both sides, with correct bands, polarity, pin order, and `E/B/C` labels. |
| 6 | 4 | PASS | Sensor direction, module pin order, buzzer polarity, transistor orientation, and onboard-LED-only behavior are explicit. |
| 7 | 3 | PASS | The widened board prevents component crowding and all routes are unambiguous; the necessary perimeter GP15 route is longer than in the single-circuit view. |
| 8 | 4 | PASS | The inset explicitly forbids direct 5 V Echo, requires the divider and common ground, confirms all GPIO roles, and requires USB disconnection and polarity checks. |
| 9 | 4 | PASS | The standalone responsive SVG has semantic text alternatives, ARIA groups, print CSS, a caption, and an exact connection table. |
| 10 | 4 | PASS | The combined artwork is original, attributes both official Freenove lessons, and contains no copied pixels or external rendering dependency. |

**Outcome:** PASS. Categories 4 and 7 are honestly recorded at **3/4**; all
critical categories are **4/4**, and no automatic-fail condition is present.

### Routing and rail audit: `proximity-alarm.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | The widened board and lower-perimeter GP15 route produce zero automated routing conflicts and no visual crossings or shared spans. |
| Power-rail use | **4/4** | VBUS visibly powers the top and bottom 5 V rails; the used bottom GND rail is visibly sourced from Pico GND; the unused top negative rail is labelled unused. |
| Rail-stripe geometry | **4/4** | The widened rails retain exact symmetric `13.50 px` stripe spacing with `0.00 px` error. |

## Audit: `ordinary-led.html`

Reviewed against the Day 1 external-LED activity, the `Pin(15, Pin.OUT)`
instruction, the wiring guide, and the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | Landscape breadboard, canonical horizontal Pico, native-size resistor and LED, coloured jumpers, and physical polarity details match the kit lesson's visual language. |
| 2 | 4 | PASS | GP15 reaches the LED anode only through 220 Ω; the cathode returns through the labelled bottom GND rail to Pico GND. |
| 3 | 4 | PASS | GP15 physical pin 20 and GND physical pin 13 use the canonical Pico order and match the Day 1 `Pin(15, Pin.OUT)` modification. |
| 4 | 4 | PASS | All 10 declared contacts use distinct, exact, visible holes; the signal, resistor, LED legs, and ground return are directly traceable. |
| 5 | 4 | PASS | The canonical 220 Ω resistor has red-red-brown-gold bands; the canonical LED shows its long anode, short cathode, and flat cathode edge. |
| 6 | 4 | PASS | LED direction and the required GP15-to-anode, cathode-to-ground orientation are visible and repeated in the safety inset. |
| 7 | 4 | PASS | Short orthogonal routes, foreground contact dots, leg labels, legend, and component value remain clear at normal size. |
| 8 | 4 | PASS | The diagram requires USB disconnection, a partner check, the current-limiting resistor, correct polarity, and a visibly sourced ground rail. |
| 9 | 4 | PASS | Standalone responsive inline SVG includes semantic title/description, ARIA groups, print CSS, caption, and exact HTML connection table. |
| 10 | 4 | PASS | Original vector artwork is identified as informed by the official Freenove LED lesson; no copied pixels or remote dependency is used. |

**Outcome:** PASS. Every category is **4/4**, and no automatic-fail
condition is present.

### Routing and rail audit: `ordinary-led.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | The routing checker reports zero conflicts; signal, resistor, bent LED leads, and ground occupy separate lanes. |
| Power-rail use | **4/4** | The only shared supply needed is GND, and the used bottom GND rail is visibly sourced from Pico GND; unused rails are labelled. |
| Rail-stripe geometry | **4/4** | All stripe-to-pin distances are exactly `13.50 px`, with `0.00 px` maximum error. |

## Audit: `potentiometer-and-led.html`

Reviewed against `code/day-2/02_potentiometer_led.py`, the Day 2 lesson, the
wiring guide, and the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | Full breadboard, canonical Pico, native potentiometer, LED, resistor, rails, and coloured wiring create a recognisable physical kit layout. |
| 2 | 4 | PASS | The potentiometer track spans 3.3 V and GND, its wiper reaches GP26/ADC0, and GP15 drives the LED only through 220 Ω. |
| 3 | 4 | PASS | GP26 physical pin 31, GP15 physical pin 20, 3V3 physical pin 36, and GND physical pin 13 agree with the program. |
| 4 | 3 | PASS | All 23 contacts are exact, distinct, and unobscured; the compact internal 3.3 V rail bridge is clear, while the separated ADC route remains necessarily long. |
| 5 | 4 | PASS | All components use canonical native dimensions; potentiometer terminals, LED polarity, and red-red-brown-gold 220 Ω bands are correct. |
| 6 | 4 | PASS | The rotary control and movable centre wiper are visible, with the two outer supply pins clearly distinguished from ADC0. |
| 7 | 3 | PASS | Labels and contacts are legible with no crossings, though the necessary separated perimeter routes make the drawing visually busier. |
| 8 | 4 | PASS | The inset limits the potentiometer to 3.3 V, requires the LED resistor and polarity check, labels every used rail, and requires USB disconnection. |
| 9 | 4 | PASS | Responsive inline SVG, semantic alternatives, ARIA groups, print CSS, caption, and exact connection table are present. |
| 10 | 4 | PASS | The original vector drawing attributes the factual Freenove lesson and contains no copied artwork or external rendering dependency. |

**Outcome:** PASS. Categories 4 and 7 are honestly recorded at **3/4**; all
critical categories are **4/4**, and no automatic-fail condition is present.

### Routing and rail audit: `potentiometer-and-led.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | Automated checking finds no overlaps or ambiguous crossings across the ADC, PWM, power, ground, and component leads. |
| Power-rail use | **4/4** | Pico 3V3 visibly sources the top rail and a clear right-side internal bridge links the labelled bottom 3.3 V rail; Pico GND sources the bottom GND rail. |
| Rail-stripe geometry | **4/4** | All four stripe distances are exactly `13.50 px`; maximum error is `0.00 px`. |

## Audit: `rgb8-module.html`

Reviewed against the Day 3 programs, the Day 3 lesson, the wiring guide, and
the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | The full breadboard, canonical Pico, and native square eight-pixel module with mounting holes and coloured jumpers match the intended physical module setup. |
| 2 | 4 | PASS | Module `IN S` reaches GP16, `IN V` reaches 3.3 V, and `IN G` reaches the common Pico ground; the OUT header remains unused. |
| 3 | 4 | PASS | GP16 physical pin 21, 3V3 physical pin 36, and GND physical pin 13 match `PIXEL_PIN = 16` in the Day 3 code. |
| 4 | 4 | PASS | All 13 declared contacts are exact, distinct, unobscured, and joined through visible terminal strips or labelled rails. |
| 5 | 4 | PASS | The canonical unscaled module preserves its square PCB, eight radial pixels, four mounting holes, and separate labelled IN/OUT S/V/G headers. |
| 6 | 4 | PASS | The connected IN end is visually oriented toward the three cable contacts, and both the inset and table explicitly reject the OUT header. |
| 7 | 4 | PASS | Three separated routes, foreground contact dots, module labels, and a text-supported legend remain clear at normal size. |
| 8 | 4 | PASS | The inset requires USB disconnection, specifies 3.3 V rather than VBUS, identifies every IN pin, and requires a partner check. |
| 9 | 4 | PASS | Standalone responsive inline SVG includes semantic title/description, ARIA groups, print CSS, caption, and exact HTML table. |
| 10 | 4 | PASS | Original vector artwork attributes the official Freenove NeoPixel lesson without embedding or tracing its image. |

**Outcome:** PASS. Every category is **4/4**, and no automatic-fail
condition is present.

### Routing and rail audit: `rgb8-module.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | Automated checking reports zero conflicts; S, V, and G use separate terminal strips and routes. |
| Power-rail use | **4/4** | Pico 3V3 explicitly sources the labelled top rail and Pico GND explicitly sources the labelled bottom rail used by the module. |
| Rail-stripe geometry | **4/4** | All four stripe distances are exactly `13.50 px`, with no alignment error. |

## Audit: `parking-assistant.html`

Reviewed against `code/day-5/parking_assistant.py`,
`code/day-5/parking_assistant_starter.py`, the Day 5 lesson, the wiring guide,
and the rendered PNG.

| # | Score | Result | Evidence |
|---:|---:|---|---|
| 1 | 4 | PASS | The widened physical breadboard contains the canonical Pico, HC-SR04, buzzer, S8050, three resistors, and square 8-RGB module at realistic native proportions. |
| 2 | 4 | PASS | GP19 Trigger, divided GP18 Echo, GP15 transistor base drive, VBUS sensor/buzzer power, GP16 RGB data, separate 3.3 V RGB power, and common ground are complete. |
| 3 | 4 | PASS | GP19/pin 25, GP18/pin 24, GP15/pin 20, GP16/pin 21, 3V3/pin 36, VBUS/pin 40, and GND/pin 13 match both Day 5 files. |
| 4 | 3 | PASS | All 48 contacts are exact, distinct, and unobscured; the dense integrated build requires long separated perimeter routes for GP15, GP16, and RGB power. |
| 5 | 4 | PASS | All components use canonical dimensions; divider and base resistor bands, sensor order, buzzer polarity, transistor E/B/C, and RGB IN header are correct. |
| 6 | 4 | PASS | Sensor direction, buzzer/transistor orientation, and RGB IN-versus-OUT direction are explicit in the artwork, labels, inset, and table. |
| 7 | 3 | PASS | The enlarged board prevents ambiguous crossings and all labels remain readable, but the complete three-subsystem circuit is necessarily denser than the Day 4 prototype. |
| 8 | 4 | PASS | The inset separates 5 V and 3.3 V, requires the Echo divider and transistor, confirms common ground and pin roles, and requires USB disconnection. |
| 9 | 4 | PASS | Standalone responsive inline SVG has semantic alternatives, ARIA groups, print CSS, a caption, and an exact connection table. |
| 10 | 4 | PASS | The original combined vector artwork attributes all three relevant Freenove lessons and contains no copied pixels or remote assets. |

**Outcome:** PASS. Categories 4 and 7 are honestly recorded at **3/4**; all
critical categories are **4/4**, and no automatic-fail condition is present.

### Routing and rail audit: `parking-assistant.html`

| Category | Score | Evidence |
|---|---:|---|
| Conductor separation | **4/4** | The checker reports zero overlaps or ambiguous crossings across all 25 declared routes and 54 segments. |
| Power-rail use | **4/4** | VBUS visibly powers both labelled 5 V rails, Pico GND powers the common GND rail, and RGB V receives a separate labelled direct 3.3 V route. |
| Rail-stripe geometry | **4/4** | The widened breadboard preserves exact `13.50 px` stripe spacing with `0.00 px` maximum error. |
