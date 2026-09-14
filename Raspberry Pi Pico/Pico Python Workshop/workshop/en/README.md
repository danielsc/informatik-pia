# Python in the Physical World

## A five-day Raspberry Pi Pico workshop

In this course, you will not just print words on a screen. You will make light,
colour, sound, games, and a parking assistant that reacts to the real world.

**Audience:** students aged about 12-15, working in pairs<br>
**Length:** five full workshop days<br>
**Language:** MicroPython<br>
**Hardware:** Raspberry Pi Pico and Freenove FNK0063 Super Starter Kit<br>
**Editor:** Thonny

**Teacher presentations:** [open the hosted slide website][slides-site] — no
repository clone is required.

Hardware activities use the
[Freenove FNK0063 Python documentation][freenove].

[freenove]: https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python.html
[slides-site]: https://danielsc.github.io/informatik-pia/

## The week at a glance

| Day | Big question | Python ideas | Hardware | Daily build |
|---|---|---|---|---|
| [1](day-1-make-it-light.md) | How does code make something happen? | scripts, `print`, values, variables, errors | onboard and external LEDs | Secret Signal Machine |
| [2](day-2-make-it-decide.md) | How does a computer react? | input, Booleans, comparisons, conditionals, `while`, lists | button, potentiometer, LED, PWM | Reaction-Time Challenge |
| [3](day-3-make-it-reusable.md) | How do we avoid repeating ourselves? | functions, parameters, returns, `for`, `range`, indexes | 8-RGB LED module, potentiometer | Pixel Pet |
| [4](day-4-make-it-sense.md) | How can code measure the world? | sensor values, dictionaries, timeouts, decomposition, testing | HC-SR04 and passive buzzer | Proximity Alarm Prototype |
| [5](day-5-parking-assistant.md) | How do separate parts become a product? | integration, state, debugging, requirements, test cases | distance, sound, RGB display | Parking Assistant |

## Start here

1. Read the [shared wiring and safety reference](WIRING_AND_SAFETY.md), then
   build only from the rendered diagram in the current day's lesson.
2. Open Thonny and select **MicroPython (Raspberry Pi Pico)** at the lower right.
3. Work in pairs: one **driver** types and one **navigator** checks the circuit
   and explains the code. Swap roles every 20 minutes.
4. Copy the matching program from [`code/`](../../code/) to your own folder.
5. Run a program with Thonny's green **Run** button.
6. Stop an endless loop with the red **Stop** button or `Ctrl+C`.
7. Disconnect USB power before changing a circuit.

The examples are deliberately small. Type them, run them, change them, predict
what will happen, and only then move to the challenge.

Some supplied programs contain a `try`/`except`/`finally` safety wrapper so
`Ctrl+C` turns outputs off. You are not expected to write that wrapper from
memory. Focus on the new code identified in the lesson; the wrapper is provided
scaffolding.

## Python learning progression

Each idea is taught before a challenge requires students to use it:

| Day | New student-owned ideas | Earlier ideas practised again |
|---|---|---|
| 1 | values, types, variables, assignment, scripts, errors | none |
| 2 | casting, Booleans, comparisons, `if`/`elif`/`else`, lists, `while` | variables and debugging |
| 3 | function calls, parameters, `return`, `for`, `range`, indexes, nested loops | conditionals and lists |
| 4 | `None`, dictionaries, sensor functions, timeouts | functions, loops, and conditionals |
| 5 | requirements, integration, boundary tests, state configuration | all earlier ideas |

Library-specific setup such as `Pin`, `PWM`, `NeoPixel`, and
`time_pulse_us` is supplied and explained as hardware vocabulary. Students are
expected to modify the Python logic only after the corresponding concept has
been introduced.

## What success looks like

By Friday, you should be able to:

- explain input, processing, and output;
- choose useful variables and data types;
- use Boolean expressions and `if`/`elif`/`else`;
- use `while` and `for` loops;
- store related values in lists and dictionaries;
- write functions with parameters and return values;
- read digital and analogue inputs;
- control digital, PWM, and RGB outputs;
- diagnose whether a problem is in code, wiring, or assumptions;
- demonstrate a parking assistant against written test cases.

## Course file inventory

| Location | Purpose |
|---|---|
| [Hosted slides][slides-site] | open and present any daily deck directly in a browser |
| [Teacher guide](TEACHER_GUIDE.md) | preparation, pacing, assessment, differentiation, and answers |
| [`slides/`](../../slides/en/) | Reveal.js source decks, presenter notes, shared styles, and authoring principles |
| [`diagrams/`](../../diagrams/) | exact HTML/SVG wiring diagrams and their PNG previews |
| [`code/day-1/`](../../code/day-1/) | first scripts, variable blink, and Secret Signal starter/solution |
| [`code/day-2/`](../../code/day-2/) | button and potentiometer examples plus Reaction Game starter/solution/extension |
| [`code/day-3/`](../../code/day-3/) | RGB and function examples plus Pixel Pet starter/solution |
| [`code/day-4/`](../../code/day-4/) | distance sensor, buzzer test, and Proximity Alarm |
| [`code/day-5/`](../../code/day-5/) | Parking Assistant starter and completed reference implementation |
| [Wiring and safety](WIRING_AND_SAFETY.md) | shared safety rules, diagram-reading routine, and reusable pin reference |
| [Sources and images](../../SOURCES_AND_IMAGES.md) | official references, teaching-source mapping, and attribution |

## Important limitation

This is a learning prototype, **not a safety device**. Never use the parking
assistant to guide a real vehicle or protect people or property.
