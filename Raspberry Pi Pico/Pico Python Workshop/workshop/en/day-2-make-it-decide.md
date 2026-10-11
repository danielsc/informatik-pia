# Day 2: Make It Decide

## Mission

Turn physical input into decisions, then build a reaction-time challenge.

**Python:** Boolean values, comparisons, casting, `if`/`elif`/`else`, `while`,
lists, indexes, `append`, `len`<br>
**Hardware:** button, ADC, potentiometer, PWM LED<br>
## 1. A button is a Boolean question

Disconnect USB. Gather the tactile button, one 10 kΩ resistor, one 220 Ω
resistor, one red LED, and jumper wires.

[Open the course's scalable HTML wiring diagram](../../diagrams/button-and-led.html).
It shows the Pico connections, breadboard orientation, internal button
contacts, and pre-power checks.

![Button and LED breadboard wiring](../../diagrams/button-and-led.png)

Build in this order:

1. Match the Pico's USB-left orientation.
2. Place the button across the centre channel exactly as shown.
3. Add the 10 kΩ pull-down and 220 Ω LED resistor.
4. Add power, ground, GP13, and GP15 wires.
5. Read the HTML connection table aloud while a partner points to each hole.

A four-leg tactile button contains only two electrical terminals. The two blue
legs marked A in the diagram are always connected, and the two red legs marked
B are always connected. Pressing joins A to B.

Before connecting USB, use a multimeter in continuity mode if available:

1. Two legs in the same terminal should beep even when released.
2. One A leg and one B leg should not beep while released.
3. The A-to-B test should beep only while the button is pressed.

Rotating the button 90 degrees in the same holes can make the input appear
permanently pressed. If the program always prints `Pressed: 1`, disconnect
USB and check orientation before changing the code.

Run [`code/day-2/01_button_decisions.py`](../../code/day-2/01_button_decisions.py).
The course circuit is active-high:

```python
pressed = button.value()

if pressed:
    led.on()
else:
    led.off()
```

`if` chooses one path when its Boolean condition is `True`; `else` chooses the
other path. The supplied `while True` keeps asking the button question until
you press Stop or `Ctrl+C`.

The 10 kΩ pull-down resistor connects GP13 to GND and makes it read `0` while
the button is released. Pressing connects GP13 to 3.3 V, making it read `1`.
Python treats `0` as false and `1` as true in a condition, so `if pressed:`
directly means “if the button is pressed”. The pin detects voltage, not current.

`not` reverses a truth value: `not True` is `False`, and `not False` is `True`.
Thus `not pressed` means “the button is not pressed”. `and` requires both
conditions to be true; `or` requires at least one. For the examples below,
first set `score = 1` and `time_is_up = False`.

Predict these expressions before trying them:

```python
pressed == True
not pressed
pressed and score > 0
pressed or time_is_up
```

## 2. From analogue world to numbers

A digital input has two states. A potentiometer can produce many values.
Disconnect USB, **leave the button and LED circuit in place**, and add only the
potentiometer's three connections shown below.

Open the
[scalable, accessible potentiometer-and-LED diagram](../../diagrams/potentiometer-and-led.html)
for exact breadboard contacts and the connection table.

![Incremental Day 2 circuit with the button retained and a potentiometer added on ADC0](../../diagrams/potentiometer-and-led.png)

The next program does not use GP13, so the connected button does not affect
the potentiometer test.

Run [`code/day-2/02_potentiometer_led.py`](../../code/day-2/02_potentiometer_led.py).

The Pico reads a number from 0 to 65535:

```python
raw_value = knob.read_u16()
percent = int(raw_value / 65535 * 100)
```

### ADC and PWM quick reference

**ADC = Analog-to-Digital Converter.** It turns an input voltage into a
number. The potentiometer changes the voltage at GP26; `knob.read_u16()`
represents roughly 0–3.3 V as a number from `0` to `65535`.

**PWM = Pulse-Width Modulation.** It rapidly switches an output off and on.
The **duty cycle** is the proportion of time it stays on: 10% gives a dim LED,
90% a bright one. `led.duty_u16(...)` sets that proportion using `0` to `65535`.
The pin switches between about 0 V and 3.3 V; it does not produce a steady
intermediate voltage. **ADC reads the knob; PWM controls the brightness.**

Reading GP26 with `Pin(..., Pin.IN).value()` instead would give only `0` or
`1`, not the knob position. Its threshold is not guaranteed to be halfway.
Use `knob.read_u16() >= 32768` if you want an explicit upper-half test.

Here `int(...)` casts a float to an integer. Record values near 0%, 25%, 50%,
75%, and 100%. Real measurements will not be exact.

PWM brightness uses a value from 0 to 65535:

```python
led.duty_u16(0)      # off
led.duty_u16(20000)  # dim
led.duty_u16(65535)  # full brightness
```

An `elif` adds another possible path. Python runs only the first branch whose
condition is true:

```python
if points >= 10:
    print("gold")
elif points >= 5:
    print("silver")
else:
    print("bronze")
```

### Threshold challenge

Change the program so the LED is:

- off below 20%;
- dim from 20% to 70%;
- bright above 70%.

Use `if`, `elif`, and `else`.

## 3. Lists remember several results

Try this in the Shell:

```python
times = [410, 375, 522]
print(times[0])
times.append(330)
print(len(times))
print(min(times))
```

Indexes start at zero. Predict what `times[-1]` returns.

## 4. A `while` loop repeats while a condition is true

A game must keep checking the button while it waits:

```python
while not button.value():
    sleep_ms(1)
```

Read this as: “while the button is released, wait 1 ms and check again.” The
loop stops when `button.value()` becomes `1`. Unlike `while True`, this loop
has a condition that can become false.

The opposite wait checks the pressed state directly:

```python
while button.value():
    sleep_ms(10)
```

Read this as: “while the button is pressed, wait until it is released.” Test
both loops with print statements before putting them inside the game.

Predict which loop is suitable for each job:

- keep the whole game running;
- wait until the button is pressed;
- repeat until five scores have been stored.

The reaction-game file also uses supplied timing tools such as `randint()` and
`ticks_ms()`. You may call those tools without knowing how they are built.

### Ready check before the game

Everything students must write in the baseline has now been practised:

| Game code | Where it was introduced |
|---|---|
| variables and assignment | Day 1 |
| active-high `button.value()`, `not`, and `and` | Day 2, section 1 |
| `if`/`else` and comparisons | Day 2, sections 1 and 2 |
| `scores = []`, `append`, `len`, and `min` | Day 2, section 3 |
| `while` with a condition | Day 2, section 4 |
| calling supplied tools such as `sleep_ms()` | examples since Day 1 |

The baseline does **not** require `for`, `range`, `def`, dictionaries, or an
endless `while True` loop. Those ideas are either taught later or remain inside
provided scaffolding. `randint()`, `ticks_ms()`, and `ticks_diff()` are supplied
timing tools; students only use the call patterns listed below.

## Daily build: Reaction-Time Challenge

Keep the complete circuit connected. The reaction-game program uses the button
on GP13 and LED on GP15; it simply ignores the potentiometer on GP26. Start from
[`code/day-2/03_reaction_game_1_starter.py`](../../code/day-2/03_reaction_game_1_starter.py).
The starter supplies imports, pin setup, an empty `scores` list, and safe LED
cleanup. **You write the game.**

### How the game works

Release the button and wait. When the LED lights, press as quickly as you can.
Holding the button down when the random wait ends is a **false start**: that
attempt earns no score and you try again. Complete three valid rounds and compare your reaction times.
The first version uses two result categories.

### Step 1: write the plan as comments

Put these ideas in the correct order before writing Python:

- repeat until the score list contains three results;
- wait until the button is released;
- wait a random amount of time;
- then check the button; if still pressed, report a false start without a score;
- turn on the LED and remember the start time;
- wait while the button is released;
- calculate the elapsed time and turn off the LED;
- add the result to the list;
- classify and print the result.

### Step 2: build one working round

Use the supplied tools:

- `randint(1000, 3000)` chooses the wait in milliseconds;
- `sleep_ms(wait_ms)` performs that wait;
- `sleep_ms(1)` pauses briefly between checks;
- `ticks_ms()` records a clock reading;
- `ticks_diff(end, start)` calculates elapsed milliseconds.

Write and test one round before adding the outer game loop. The LED must turn
off after the press, and the Shell must print a believable reaction time.
Remember that this active-high button reads `0` when released and `1` when
pressed; use one `while` loop to wait for release and another to wait for the
press.

Keep the random wait simple, then check the button before lighting the LED:

```python
sleep_ms(wait_ms)
```

After the wait, check `if button.value():` to report a false start. Put the LED,
reaction timing, and score code in the `else` branch. This baseline detects a
button held at the start; a press released during the wait is not detected.

### Step 3: add a decision

Write your own `if`/`else`:

- below 350 ms prints `Quick!`;
- 350 ms or more prints `Keep practising!`.

Change the boundary after the first successful test and predict which results
will be classified differently.

### Step 4: turn one round into three

Wrap the working round in:

```python
while len(scores) < ROUNDS:
    # your tested one-round code goes here
```

This is a bounded loop, not an endless loop. It stops as soon as the list
contains three scores. The button-wait loops stop when the button changes
state.

Append each `reaction_ms` to `scores`. When the loop finishes, print the whole
list and the fastest result with `min(scores)`.

The supplied `try`/`finally` wrapper uses the cleanup pattern introduced on
Day 1. Leave it in place. Use
[`code/day-2/03_reaction_game_2_solution.py`](../../code/day-2/03_reaction_game_2_solution.py)
only for recovery or comparison after your three-round version works.

### Extensions

Choose one only after the baseline works:

- calculate the average with `sum(scores) / len(scores)`;
- add a third result category with `elif`;
- celebrate a personal best;
- increase the game to five rounds;
- create a two-player version.

The optional
[`code/day-2/03_reaction_game_3_extension.py`](../../code/day-2/03_reaction_game_3_extension.py)
adds five rounds, a third result category, and an average after the baseline
works. It also monitors the random wait to detect presses released before the
wait ends; this extra logic is optional.

### Demo checklist

- Show one complete timed round.
- Show all three stored scores.
- Demonstrate a false start and show that it does not add a score.
- Explain why the main program needs a `while` loop.
- Point to the Boolean expression that ends a wait.
- Explain why each score is an integer.

## Exit ticket

Write a condition that is true when `reaction_ms` is at least 200 and below
500. Then describe what values lie exactly on each boundary.
