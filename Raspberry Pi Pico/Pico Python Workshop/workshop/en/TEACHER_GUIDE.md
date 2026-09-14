# Teacher Guide

## Course intent

This workshop compresses selected ideas from a semester-long TEALS course into
five project days. It prioritises durable understanding over covering every
topic. EarSketch is omitted; physical computing provides the creative context.
Object-oriented programming is an optional extension, not a core outcome.

The rhythm for each activity is:

1. **Predict** what the circuit or code will do.
2. **Build** with USB power disconnected.
3. **Run** the smallest possible test.
4. **Explain** the input-process-output chain.
5. **Change** one thing and predict again.
6. **Challenge** students to combine ideas without copying a full solution.

Use the [teacher Reveal.js slides](../../slides/README.md) for the explicit teaching
and guided-practice portion. The daily Markdown lesson remains the student lab
sheet with wiring diagrams, code links, and build criteria.

## Before the week

- Install current Thonny and MicroPython firmware on every Pico.
- Run `code/day-1/01_hello_pico.py` on every workstation.
- Inventory each kit against the component lists in the daily lessons.
- Identify the passive buzzer. It usually has no sealed underside; do not rely
  on appearance alone if the components are labelled.
- Prepare the Freenove `220 Ω`, `1 kΩ`, `2 kΩ`, and `10 kΩ` resistors.
- Print or display a Pico physical pinout.
- Build and test one complete parking assistant.
- Confirm the 8-RGB module works with MicroPython's built-in `neopixel` module.
- Use masking tape to mark 15 cm, 30 cm, 60 cm, and 100 cm on tables.
- Decide whether students may connect 5 V circuits themselves. Instructor
  inspection before USB connection is strongly recommended on Days 4 and 5.

## Suggested daily timetable

| Time | Activity |
|---|---|
| 09:00-09:25 | hook, demo, retrieval questions |
| 09:25-10:20 | guided concept and first build |
| 10:20-10:35 | break |
| 10:35-11:35 | investigation and code changes |
| 11:35-12:15 | mini-lesson and debugging clinic |
| 12:15-13:00 | lunch |
| 13:00-14:30 | daily build challenge |
| 14:30-15:00 | demos, code reading, reflection, reset kits |

Keep teacher explanation short. A visible failure followed by systematic
debugging is often more valuable than a polished lecture.

## Curriculum map

| Workshop | Approximate TEALS alignment | Deliberate emphasis |
|---|---|---|
| Day 1 | Unit 1: Introduction to Python | interpreter, scripts, strings, numbers, variables, comments, errors |
| Day 2 | Unit 2: Data Types and Conditionals | casting, Booleans, comparisons, conditionals, lists, `while` |
| Day 3 | Units 3 and 4: Functions; Nested Loops and Lists | imports, abstraction, parameters, returns, `for`, `range`, indexes |
| Day 4 | Unit 6 and Unit 8 preparation | dictionaries as configuration, decomposition, requirements, testing |
| Day 5 | Unit 8: Final Project | integration, scope, iterative implementation, test evidence |

## Concept gates

The TEALS source course spends several class periods on each unit. This
five-day workshop compresses that sequence, so every day needs a short,
explicit teach-practise-apply cycle. Do not treat syntax found only in supplied
scaffolding as already learned.

| Before students are asked to use... | Teach and practise first |
|---|---|
| variables in the Day 1 signal | values, types, assignment, and changing one value |
| conditions in the Day 2 challenge | Boolean expressions followed by `if`/`elif`/`else` |
| lists in the reaction game | creation, index 0, `append`, `len`, and `min` |
| `while` in the reaction game | a visible condition that changes from true to false |
| user-defined functions on Day 3 | calls, arguments, parameters, and `return` |
| `for` and `range` on Day 3 | print 0-7 before using those indexes on pixels |
| nested loops in animations | trace a tiny two-by-two example on paper |
| dictionaries on Day 4 | create, access, and update one flat dictionary |
| integrated Day 5 logic | rerun one known-working test for each hardware layer |

The TEALS progression teaches Unit 1 fundamentals, Unit 2
Booleans/conditionals/lists/`while`, Unit 3 functions, Unit 4 `for` and nested
loops, Unit 6 dictionaries, and Unit 8 project planning. This workshop keeps
that dependency order even though several units share a single workshop day.

`try`/`except`/`finally`, hardware constructors, and timing-library details are
provided safety scaffolds. Point out what they accomplish, but do not assess
students on reproducing them.

Day 1 deliberately leaves repeated flash blocks visible. Day 3 should refer
back to that code when functions and loops are introduced: students first see
the problem, then learn the abstraction that solves it.

## Formative assessment

Use these prompts while circulating:

- What is the input? What is the output?
- Which line changes the physical world?
- What type of value is this?
- What values make this condition true?
- Why is a loop needed here?
- What does this function receive and return?
- Is this a code problem, wiring problem, or measurement problem?
- What is the smallest test that could distinguish those possibilities?

Daily exit tickets:

| Day | Prompt                                                                |
| --- | --------------------------------------------------------------------- |
| 1   | Draw arrows showing how one variable changes an LED pattern.          |
| 2   | Write one Boolean expression that describes a fast reaction.          |
| 3   | Explain the difference between a parameter and a return value.        |
| 4   | Give one reason a distance reading may be invalid.                    |
| 5   | Name one test your product passes and one improvement you would make. |

## Daily project checkpoints

### Day 1: Secret Signal Machine

Minimum: a named message, at least two timing variables, and a recognisable LED
pattern. Strong work adds an external LED and comments that explain intent.
Present [`slides/day-1.html`](../../slides/en/day-1.html) before launching the lab. Its
speaker notes include questions, demonstrations, expected answers, circuit
safety reminders, and suggested transition points.

### Day 2: Reaction-Time Challenge

Minimum: students write a random wait, measure one button press, classify it
with `if`/`else`, repeat for three rounds with `while`, append each score, and
report the fastest. Strong work adds `elif`, an average, or false-start
detection. Do not require students to reproduce the supplied hardware setup or
cleanup wrapper.

Before releasing the starter, check that students can explain
`while len(scores) < ROUNDS` and both button-state wait loops. None is endless:
the score loop stops at three items, and each button loop stops when the input
changes. `randint`, `ticks_ms`, and `ticks_diff` are provided APIs, not
implementation objectives.

Present [`slides/day-2.html`](../../slides/en/day-2.html) before and between the button,
potentiometer, and reaction-game tasks.

### Day 3: Pixel Pet

Minimum: three states selected by potentiometer input and displayed by
functions on the RGB module. Strong work gives each state a short animation
using indexed pixels.

Present [`slides/day-3.html`](../../slides/en/day-3.html) before the RGB build and use
its function, loop, and Pixel Pet sections as the corresponding tasks begin.

### Day 4: Proximity Alarm Prototype

Minimum: valid distance measurement, safe/caution/stop classification, and
different buzzer behaviour. Strong work handles no echo without freezing and
records calibration evidence.

Present [`slides/day-4.html`](../../slides/en/day-4.html) in sections so each safety
diagram immediately precedes the sensor, buzzer, or combined build.

### Day 5: Parking Assistant

Present [`slides/day-5.html`](../../slides/en/day-5.html) while students move through
requirements, layered hardware integration, function-by-function
implementation, testing, and demonstration.

Minimum acceptance criteria:

- safe, caution, stop, and invalid states are distinguishable;
- visual output always works, including in muted mode;
- beep rate becomes more urgent as distance decreases;
- missing echo does not freeze the program;
- students can explain each function and demonstrate four test cases;
- the program turns outputs off when stopped with `Ctrl+C`.

## Differentiation

**Support**

- Provide the complete wiring table but hide solution files until requested.
- Ask students to modify one constant before writing new control flow.
- Use code cards: import, setup, input, decision, output, delay.
- Let one pair compare a known-working component against an uncertain one.
- Allow students to start from the `_starter.py` files.

**Extension**

- Calculate mean and median reaction time.
- Smooth distance using the most recent five valid readings.
- Let the potentiometer configure the safe threshold.
- Use each RGB pixel as a distance bar.
- Store state configuration in a dictionary containing dictionaries.
- Build a `ParkingAssistant` class only after the function-based version works.

## Debugging protocol

Students should say the symptom before changing anything:

1. Stop the program.
2. Disconnect USB before touching wires.
3. Compare one wire at a time with the pin table.
4. Check component orientation and resistor values.
5. Reconnect and run the smallest component test.
6. Print raw input values.
7. Test the condition at its boundaries.
8. Combine components only after each passes alone.

Discourage random rewiring and changing several lines at once.

## End-of-week assessment rubric

| Criterion | Beginning | Developing | Secure | Advanced |
|---|---|---|---|---|
| Python reasoning | reads code with help | explains variables and conditions | explains loops, functions, and state | justifies abstractions and trade-offs |
| Physical system | one component works | several parts work separately | integrated system meets criteria | robust calibration or extension |
| Debugging | guesses | checks code or circuit | isolates problems with small tests | records evidence and boundary cases |
| Communication | shows output | describes behaviour | explains input-process-output and functions | connects design decisions to user needs |
| Teamwork | uneven participation | shares some tasks | swaps driver/navigator roles | supports other teams without taking over |

## Reset and storage

At the end of each day:

- stop the running script;
- turn off PWM and RGB LEDs;
- unplug USB;
- keep Day 2's potentiometer and its 3.3 V/GND wiring for Day 3 if space
  permits, but remove the ordinary LED before adding the RGB module;
- dismantle the Day 3 circuit before the Day 4 high-voltage build;
- count components and store resistors separately by value.
