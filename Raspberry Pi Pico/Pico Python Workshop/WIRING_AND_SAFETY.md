# Wiring and Safety

Original course diagrams are evaluated with the
[Wiring Diagram Quality Rubric](diagrams/DIAGRAM_RUBRIC.md). Critical
electrical, pin, component, switch, and safety categories must score 4/4.

## Rules for every build

1. Disconnect USB before adding, removing, or moving wires.
2. Ask a partner to compare the circuit with the pin table.
3. Use a resistor in series with every ordinary LED.
4. Never connect VBUS (5 V) to a GPIO or directly to GND.
5. Make all grounds common when circuits use both 3.3 V and 5 V.
6. Keep drinks away from the work area.
7. Stop immediately if anything becomes hot or smells unusual.
8. Do not hold a buzzer near an ear. Use short, low-duty sounds.

The Pico's GPIO pins use **3.3 V logic and are not 5 V tolerant**.

```text
Safe power overview

USB ──> Pico
         │
         ├── VBUS (5 V) ─────> only components that require 5 V
         ├── 3V3(OUT) ───────> 3.3 V components and pull-up resistors
         ├── GPIO ────────────> signals only; never connect to 5 V
         └── GND ─────┬──────> every component ground
                      └───────> one shared reference for the circuit
```

## Pico pins used in this course

| Signal | GPIO name | Physical pin |
|---|---:|---:|
| onboard LED | `LED` | onboard |
| external LED / buzzer control | GP15 | 20 |
| 8-RGB module data | GP16 | 21 |
| HC-SR04 Echo input | GP18 | 24 |
| HC-SR04 Trigger output | GP19 | 25 |
| potentiometer analogue input | GP26 / ADC0 | 31 |
| 3.3 V | 3V3(OUT) | 36 |
| USB 5 V | VBUS | 40 |
| diagram ground connections | GND | 13, 23, or 38 (use the pin named in the diagram) |

Check the printed labels on the Pico. **GPIO numbers are not physical pin
numbers.**

```text
Simplified course pin map -- USB connector at the top

                    ┌───────────────┐
                    │      USB      │
                    │               │
 buzzer/LED  GP15 20├               ├21 GP16  RGB data
 shared GND  GND  23├               ├24 GP18  Echo input
 trigger     GP19 25├               │
                    │               ├31 GP26  potentiometer
                    │               ├36 3V3   3.3 V power
                    │               ├40 VBUS  USB 5 V
                    └───────────────┘

The physical pin number is the number beside the board edge.
The GPIO number is the GP label used in Python.
```

## Ordinary LED

Open the
[scalable, accessible ordinary-LED diagram](diagrams/ordinary-led.html) for
the exact GP15 breadboard contacts, LED polarity, and connection table.

![Ordinary red LED on GP15 through a 220 ohm resistor](diagrams/ordinary-led.png)

Use the official Freenove
[LED hardware picture](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter01_20.png).
The local diagram is original course artwork informed by that source.

| From | Through | To |
|---|---|---|
| GP15 | 220 Ω resistor, then LED long leg | LED short leg to GND |

```text
GP15 ─── 220 Ω ─── anode |>| cathode ─── GND
                         LED
                    long leg   short leg / flat edge

Conventional current flows from the long anode leg to the short cathode leg.
```

If it does not light, disconnect USB and check LED orientation.

## Button

Open the original
[browser-rendered scalable wiring diagram](diagrams/button-and-led.html) for a
larger breadboard view, wire colours, button internals, and a pre-power
checklist.

![Button and LED breadboard wiring](diagrams/button-and-led.png)

Use the official Freenove
[Button & LED hardware picture](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter02_04.png).
The course follows the Freenove active-low circuit.

The four legs are not four separate contacts. Two legs form terminal **A** and
are permanently connected. The other two form terminal **B** and are
permanently connected. Releasing the button leaves A and B separate; pressing
it bridges A to B, at which point all four legs are electrically connected.

```text
Button viewed from above

       terminal A                          terminal B
    A1 o───────o A2                    B1 o───────o B2
       always connected                   always connected
                  \                       /
                   \____ press joins ____/

Released: A1=A2       A is not connected to B       B1=B2
Pressed:  A1=A2=B1=B2
```

The button must straddle the breadboard's centre channel. In the correct
orientation, **each permanent pair crosses the channel**: terminal A occupies
the two holes on the left, and terminal B occupies the two holes on the right.
The switch keeps the left and right pairs separate until pressed.

```text
Correct breadboard orientation -- top view

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

Do not rotate the button 90 degrees in the same four breadboard holes. That can
place A and B into connected breadboard strips and make the input appear
permanently pressed.
```

Identify the pairs before power is connected:

1. Put a multimeter in continuity mode.
2. Find two legs that beep while the button is released; they are one terminal.
3. Verify that one A leg and one B leg do not beep when released.
4. Press the button and verify that A and B now beep.

| Part | Connection |
|---|---|
| button signal | GP13 |
| pull-up | 10 kΩ from GP13 to 3.3 V |
| button other side | GND |
| external LED | GP15 through 220 Ω to LED, then GND |

```text
Active-low button and LED circuit

3.3 V ─── 10 kΩ ───┬──── GP13 input
                    │
               terminal A
                  [ button ]    open when released
               terminal B      closed when pressed
                    │
                   GND

GP15 ─── 220 Ω ─── |>| ─── GND
                    LED
```

When released, the 10 kΩ resistor weakly pulls GP13 up to 3.3 V, so the input
reads `1`. When pressed, the button provides a path to ground, so the input
reads `0`. The 10 kΩ resistor limits current; the button does not short 3.3 V
directly to ground. Code therefore uses `if not button.value():`.

## Potentiometer and PWM LED

Open the
[scalable, accessible potentiometer-and-LED diagram](diagrams/potentiometer-and-led.html)
for the exact ADC0, PWM, 3.3 V, ground, and LED contacts.

![Potentiometer on ADC0 and PWM LED on GP15](diagrams/potentiometer-and-led.png)

![Freenove potentiometer and LED circuit](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter10_01.png)

Source: [Freenove Potentiometer & LED lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/10_Potentiometer_%26_LED.html)
The local diagram is original course artwork informed by that source.

| Part | Connection |
|---|---|
| potentiometer outer pin | 3.3 V |
| potentiometer centre pin | GP26 / ADC0 |
| potentiometer other outer pin | GND |
| LED | GP15 through 220 Ω to LED, then GND |

```text
Potentiometer input                      PWM output

3.3 V ─────/\/\/\/\/\/\/───── GND
              resistor track
                    ▲
                    │ movable centre wiper
                    └──────────────> GP26 / ADC0

GP15 / PWM ─── 220 Ω ─── |>| ─── GND
                          LED

Turning the shaft moves the wiper between 0 V and 3.3 V.
```

Use only 3.3 V across the potentiometer.

## Freenove 8-RGB LED module

Open the
[scalable, accessible 8-RGB module diagram](diagrams/rgb8-module.html) for the
exact `IN` header contacts and the separate 3.3 V, ground, and GP16 routes.

![Freenove square 8-RGB module IN header wired to GP16](diagrams/rgb8-module.png)

![Freenove 8-RGB module connection](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter06_05.png)

Source: [Freenove NeoPixel lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/6_NeoPixel.html)
The local diagram is original course artwork informed by that source.

Connect the **IN** end, not OUT:

| Module pin | Pico |
|---|---|
| `S` | GP16 |
| `V` | 3.3 V |
| `G` | GND |

```text
Pico                         Freenove 8-RGB module

GP16  ─────────────────────> S   IN
3.3 V ─────────────────────> V
GND   ─────────────────────> G

                              [0][1][2][3][4][5][6][7]

Connect the end marked IN. The OUT end is only for another module.
```

The examples use deliberately low RGB values to reduce glare and current.

## Passive buzzer with transistor driver

Open the
[scalable, accessible passive-buzzer diagram](diagrams/passive-buzzer.html)
for exact breadboard contacts, the flat-face S8050 `E/B/C` orientation, and
the complete connection table.

![Passive buzzer and S8050 transistor-driver breadboard wiring](diagrams/passive-buzzer.png)

Source: [Freenove Buzzer lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/7_Buzzer.html)
and the official
[Freenove passive-buzzer circuit](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter07_11.png).
The local diagram is original course artwork informed by those sources.

Do not drive the buzzer directly from a GPIO. Follow the Freenove passive-buzzer
circuit using the NPN transistor marked `8050` and the 1 kΩ base resistor.
The control signal is GP15. The buzzer supply is VBUS (5 V).

```text
                              VBUS / 5 V
                                  │
                            passive buzzer
                                  │
                                  C
GP15 ─── 1 kΩ ─────────────── B  Q1  NPN 8050
                                  E
                                  │
                                 GND

GP15 controls a small base current.
The transistor switches the larger buzzer current; GPIO does not supply it.
```

Check the 8050 transistor's flat face and pin order against the kit
documentation before inserting it. Transistor pin order is not universal.

## HC-SR04 distance sensor: safer Echo connection

The HC-SR04 requires 5 V. Its Echo output can rise to 5 V, which is unsafe for
a Pico GPIO. The official Freenove picture shows a direct Echo connection; this
course **intentionally replaces that one wire with a voltage divider**.

Open the
[scalable, accessible safe HC-SR04 diagram](diagrams/distance-sensor.html) for
exact breadboard contacts and the complete connection table.

![Safe HC-SR04 breadboard wiring with a protected Echo input](diagrams/distance-sensor.png)

Source: [Freenove Ultrasonic Ranging lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/22_Ultrasonic_Ranging.html)
and the official
[Freenove HC-SR04 layout](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter22_06.png).
The local diagram is original course artwork informed by those sources.

| HC-SR04 pin | Connection |
|---|---|
| VCC | VBUS / 5 V, physical pin 40 |
| Trig | GP19, physical pin 25 |
| Echo | through **1 kΩ** to a junction; junction to GP18 |
| divider junction | through **2 kΩ** to GND |
| GND | Pico GND |

```text
Pico                                     HC-SR04

VBUS / 5 V ─────────────────────────────> VCC
GP19 ───────────────────────────────────> Trig
GND ────────────────────────────────────> GND

                                          Echo
                                            │  about 5 V
                                            │
                                           1 kΩ
                                            │
                         GP18 <─────────────●  divider junction
                                            │
                                           2 kΩ
                                            │
                                           GND

The 1 kΩ resistor must be between Echo and the junction.
The 2 kΩ resistor must be between the junction and GND.
```

The divider produces approximately `5 V × 2/(1+2) = 3.33 V`.

Do not substitute the 10 kΩ button wiring for this divider. An instructor
should inspect every sensor circuit before USB is connected.

## Final parking-assistant pin plan

The Day 4 prototype combines the sensor and buzzer safely before the RGB
module is added. Open the
[scalable, accessible combined diagram](diagrams/proximity-alarm.html).

![Combined HC-SR04 and passive-buzzer proximity alarm wiring](diagrams/proximity-alarm.png)

This original course diagram is informed by the official Freenove ultrasonic
and buzzer lessons. It uses the Pico's onboard LED only; no external LED is
part of the Day 4 circuit.

The complete build diagram, exact connection table, and assembly sequence are
kept together in [Day 5: Build a Parking Assistant](day-5-parking-assistant.md).

| Component | Signal | Power |
|---|---|---|
| HC-SR04 | Trig GP19; Echo via divider to GP18 | 5 V and GND |
| passive buzzer driver | GP15 through 1 kΩ to NPN base | 5 V and GND |
| 8-RGB module IN | GP16 | 3.3 V and GND |

There are no GPIO conflicts in this plan.
