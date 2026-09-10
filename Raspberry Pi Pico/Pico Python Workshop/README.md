# Python in the Physical World

## A five-day Raspberry Pi Pico workshop

In this course, you will not just print words on a screen. You will make light,
colour, sound, games, and a parking assistant that reacts to the real world.

**Audience:** students aged about 12-15, working in pairs  
**Length:** five full workshop days  
**Language:** MicroPython  
**Hardware:** Raspberry Pi Pico and Freenove FNK0063 Super Starter Kit  
**Editor:** Thonny

The learning sequence is adapted from the
[TEALS Introduction to Computer Science curriculum map][teals]. The EarSketch
unit is intentionally omitted. Hardware activities use the
[Freenove FNK0063 Python documentation][freenove].

[teals]: https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/curriculum_map.md.html
[freenove]: https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python.html

## The week at a glance

| Day | Big question | Python ideas | Hardware | Daily build |
|---|---|---|---|---|
| [1](day-1-make-it-light.md) | How does code make something happen? | scripts, `print`, values, variables, errors | onboard and external LEDs | Secret Signal Machine |
| [2](day-2-make-it-decide.md) | How does a computer react? | input, Booleans, comparisons, conditionals, `while`, lists | button, potentiometer, LED, PWM | Reaction-Time Challenge |
| [3](day-3-make-it-reusable.md) | How do we avoid repeating ourselves? | imports, functions, parameters, returns, `for`, `range`, indexes | 8-RGB LED module, potentiometer | Pixel Pet |
| [4](day-4-make-it-sense.md) | How can code measure the world? | sensor values, dictionaries, timeouts, decomposition, testing | HC-SR04 and passive buzzer | Proximity Alarm Prototype |
| [5](day-5-parking-assistant.md) | How do separate parts become a product? | integration, state, debugging, requirements, test cases | distance, sound, RGB display | Parking Assistant |

## Start here

1. Read [Wiring and safety](WIRING_AND_SAFETY.md) before connecting components.
2. Open Thonny and select **MicroPython (Raspberry Pi Pico)** at the lower right.
3. Work in pairs: one **driver** types and one **navigator** checks the circuit
   and explains the code. Swap roles every 20 minutes.
4. Copy the matching program from [`code/`](code/) to your own folder.
5. Run a program with Thonny's green **Run** button.
6. Stop an endless loop with the red **Stop** button or `Ctrl+C`.
7. Disconnect USB power before changing a circuit.

The examples are deliberately small. Type them, run them, change them, predict
what will happen, and only then move to the challenge.

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

## Course files

| File | Purpose |
|---|---|
| [Teacher guide](TEACHER_GUIDE.md) | preparation, pacing, assessment, differentiation, and answers |
| [Wiring and safety](WIRING_AND_SAFETY.md) | reusable pin tables and safe final circuit |
| [Sources and images](SOURCES_AND_IMAGES.md) | official visual references and attribution |
| [`code/`](code/) | runnable examples, challenge starters, and solutions |

## Important limitation

This is a learning prototype, **not a safety device**. Never use the parking
assistant to guide a real vehicle or protect people or property.

