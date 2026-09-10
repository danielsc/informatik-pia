# Day 2: Make It Decide

## Mission

Turn physical input into decisions, then build a reaction-time challenge.

**Python:** Boolean values, comparisons, casting, `if`/`elif`/`else`, `while`,
lists, indexes, `append`, `len`  
**Hardware:** button, ADC, potentiometer, PWM LED  
**TEALS connection:** Unit 2, Data Types and Conditionals

## 1. A button is a Boolean question

Disconnect USB and build the
[button circuit](WIRING_AND_SAFETY.md#button).

[Open the course's scalable HTML wiring diagram](diagrams/button-and-led.html).
It shows the Pico connections, breadboard orientation, internal button
contacts, and pre-power checks.

![Button and LED breadboard wiring](diagrams/button-and-led.png)

![Freenove Button & LED connection](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter02_04.png)

The picture does not make the button's orientation obvious. A four-leg tactile
button contains only two electrical terminals. The two legs in terminal A are
always connected to each other, and the two legs in terminal B are always
connected to each other. Pressing the button joins A to B.

```text
Released                              Pressed

A1 o────o A2       B1 o────o B2       A1 o────o A2
   one terminal       one terminal        │
                                          │
                                      B1 o────o B2

A and B are separate.                 A and B are connected.
```

Place the button across the breadboard's centre channel so each permanent pair
crosses the channel. Terminal A is the left pair and terminal B is the right
pair:

```text
      terminal A       terminal B
          │                │
 top     A1 o            o B1
             ╔════════╗
 channel     ║ button ║
             ╚════════╝
 bottom  A2 o            o B2
          │                │
          └ always joined  └ always joined

Pressing joins terminal A to terminal B.
```

Before connecting USB, use a multimeter in continuity mode if available:

1. Two legs in the same terminal should beep even when released.
2. One A leg and one B leg should not beep while released.
3. The A-to-B test should beep only while the button is pressed.

Rotating the button 90 degrees in the same holes can make the input appear
permanently pressed. If the program always prints `Pressed: True`, disconnect
USB and check orientation before changing the code.

Run [`code/day-2/01_button_decisions.py`](code/day-2/01_button_decisions.py).
The Freenove circuit is active-low:

```python
pressed = not button.value()

if pressed:
    led.on()
else:
    led.off()
```

The 10 kΩ pull-up resistor makes GP13 read `1` while the button is released.
Pressing connects GP13 to ground, making it read `0`. `not` converts that
active-low electrical signal into a natural Python value: `pressed` is `True`
when a person is pressing the button.

Predict these expressions before trying them:

```python
pressed == True
not pressed
pressed and score > 0
pressed or time_is_up
```

## 2. From analogue world to numbers

A digital input has two states. A potentiometer can produce many values.
Disconnect USB and build the circuit below.

![Freenove potentiometer and LED connection](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter10_01.png)

Follow the
[Freenove Potentiometer & LED page](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/10_Potentiometer_%26_LED.html)
and [course wiring instructions](WIRING_AND_SAFETY.md#potentiometer-and-pwm-led).

Open the
[scalable, accessible potentiometer-and-LED diagram](diagrams/potentiometer-and-led.html)
for exact breadboard contacts and the connection table.

![Potentiometer on ADC0 and PWM LED on GP15](diagrams/potentiometer-and-led.png)

Run [`code/day-2/02_potentiometer_led.py`](code/day-2/02_potentiometer_led.py).

The Pico reads a number from 0 to 65535:

```python
raw_value = knob.read_u16()
percent = int(raw_value / 65535 * 100)
```

Here `int(...)` casts a float to an integer. Record values near 0%, 25%, 50%,
75%, and 100%. Real measurements will not be exact.

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

## Daily build: Reaction-Time Challenge

Rebuild the button and LED circuit. Run
[`code/day-2/03_reaction_game.py`](code/day-2/03_reaction_game.py).

Game flow:

1. Release the button.
2. Pico waits for a random interval.
3. Pressing too early is a false start.
4. The LED turns on.
5. Pico measures milliseconds until the press.
6. An `if` statement classifies the result.
7. Five scores are stored in a list.

### Your modifications

Complete at least two:

- choose your own result categories;
- make the onboard LED celebrate a personal best;
- calculate the average with `sum(scores) / len(scores)`;
- add a sixth “championship” round;
- make false starts add a penalty;
- create a two-player version.

### Demo checklist

- Show one false start.
- Explain why the main program needs a `while` loop.
- Point to the Boolean expression that ends a wait.
- Explain why each score is an integer.

## Exit ticket

Write a condition that is true when `reaction_ms` is at least 200 and below
500. Then describe what values lie exactly on each boundary.
