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

### Day 2: Reaction-Time Challenge

Minimum: random wait, early-press detection, measured reaction time, and a
classification using `if`/`elif`/`else`. Strong work stores five scores in a
list and reports the fastest.

### Day 3: Pixel Pet

Minimum: three states selected by potentiometer input and displayed by
functions on the RGB module. Strong work gives each state a short animation
using indexed pixels.

### Day 4: Proximity Alarm Prototype

Minimum: valid distance measurement, safe/caution/stop classification, and
different buzzer behaviour. Strong work handles no echo without freezing and
records calibration evidence.

### Day 5: Parking Assistant

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
- keep Day 2's potentiometer circuit for Day 3 if space permits;
- dismantle the Day 3 circuit before the Day 4 high-voltage build;
- count components and store resistors separately by value.

