# Teacher component tests

These small programs test one workshop component at a time before it is used
in a combined project. Stop the program and disconnect USB before changing
the circuit. Build each physical circuit from the linked scalable diagram and
its exact connection table.

| Test | Component and expected result | Build diagram |
|---|---|---|
| [`01_onboard_led.py`](01_onboard_led.py) | onboard LED blinks | [Pico only; no external wiring](../../diagrams/onboard-led.html) |
| [`02_external_led.py`](02_external_led.py) | ordinary LED on GP15 blinks | [ordinary LED](../../diagrams/ordinary-led.html) |
| [`03_button.py`](03_button.py) | GP13 reports each press and release | [button only](../../diagrams/button-only.html) |
| [`04_potentiometer.py`](04_potentiometer.py) | GP26 reports raw and percentage values | [potentiometer only](../../diagrams/potentiometer-only.html) |
| [`05_rgb_pixels.py`](05_rgb_pixels.py) | one GP16 pixel moves and changes colour | [8-RGB module](../../diagrams/rgb8-module.html) |
| [`06_passive_buzzer.py`](06_passive_buzzer.py) | GP15 plays three repeating pitches | [passive buzzer and transistor](../../diagrams/passive-buzzer.html) |
| [`07_distance_sensor.py`](07_distance_sensor.py) | GP19/GP18 report distance or `No echo` | [HC-SR04 with Echo divider](../../diagrams/distance-sensor.html) |

### 01 · Onboard LED

[![Pico with the onboard LED highlighted](../../diagrams/onboard-led.png)](../../diagrams/onboard-led.html)

### 02 · External LED

[![Ordinary LED connected safely to GP15](../../diagrams/ordinary-led.png)](../../diagrams/ordinary-led.html)

### 03 · Button

[![Active-low button connected to GP13](../../diagrams/button-only.png)](../../diagrams/button-only.html)

### 04 · Potentiometer

[![Potentiometer connected to GP26 ADC0](../../diagrams/potentiometer-only.png)](../../diagrams/potentiometer-only.html)

### 05 · RGB pixels

[![Eight-pixel RGB module connected to GP16](../../diagrams/rgb8-module.png)](../../diagrams/rgb8-module.html)

### 06 · Passive buzzer

[![Passive buzzer connected through an S8050 transistor driver](../../diagrams/passive-buzzer.png)](../../diagrams/passive-buzzer.html)

The buzzer test deliberately keeps each sound short and uses a low duty value.
The physical buzzer must use the 1 kΩ base resistor and S8050 transistor driver
shown in the diagram. Do not connect the physical buzzer directly to GP15 and
do not hold it near an ear.

### 07 · Distance sensor

[![HC-SR04 connected with a safe Echo voltage divider](../../diagrams/distance-sensor.png)](../../diagrams/distance-sensor.html)

The HC-SR04 physical circuit must use the 1 kΩ/2 kΩ Echo divider so its
5 V Echo signal never reaches GP18 directly.

Resistors and the S8050 transistor do not receive software commands of their
own. They are tested as part of the external-LED, button, buzzer, and sensor
circuits where they limit current, establish a known input level, switch the
buzzer supply, or protect the Echo input.

The separate combined potentiometer/pixel demonstration remains in
[`potentiometer_pixel_spinner.py`](potentiometer_pixel_spinner.py); build it
by combining the [potentiometer-only](../../diagrams/potentiometer-only.html)
and [RGB-module](../../diagrams/rgb8-module.html) connection tables. GP26 and
GP16 do not conflict.
