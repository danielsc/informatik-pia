# Teacher component tests

These small programs test one workshop component at a time before it is used
in a combined project. Stop the program and disconnect USB before changing
the circuit. Build physical circuits from the linked course diagram and its
exact connection table, not from the Wokwi layout.

| Test | Component and expected result | Physical circuit |
|---|---|---|
| [`01_onboard_led.py`](01_onboard_led.py) | onboard LED blinks | Pico only |
| [`02_external_led.py`](02_external_led.py) | ordinary LED on GP15 blinks | [ordinary LED](../../diagrams/ordinary-led.html) |
| [`03_button.py`](03_button.py) | GP13 reports each press and release | [button](../../diagrams/button-and-led.html) |
| [`04_potentiometer.py`](04_potentiometer.py) | GP26 reports raw and percentage values | [potentiometer](../../diagrams/potentiometer-and-led.html) |
| [`05_rgb_pixels.py`](05_rgb_pixels.py) | one GP16 pixel moves and changes colour | [8-RGB module](../../diagrams/rgb8-module.html) |
| [`06_passive_buzzer.py`](06_passive_buzzer.py) | GP15 plays three repeating pitches | [passive buzzer and transistor](../../diagrams/passive-buzzer.html) |
| [`07_distance_sensor.py`](07_distance_sensor.py) | GP19/GP18 report distance or `No echo` | [HC-SR04 with Echo divider](../../diagrams/distance-sensor.html) |

The buzzer test deliberately keeps each sound short and uses a low duty value.
The physical buzzer must use the 1 kΩ base resistor and S8050 transistor driver
shown in the diagram. Do not connect the physical buzzer directly to GP15 and
do not hold it near an ear.

The HC-SR04 physical circuit must use the 1 kΩ/2 kΩ Echo divider. Wokwi does
not model that protection circuit accurately, so its behavioural simulation
uses a 3.3 V virtual sensor and connects Echo directly; this is not physical
wiring guidance.

Resistors and the S8050 transistor do not receive software commands of their
own. They are tested as part of the external-LED, button, buzzer, and sensor
circuits where they limit current, establish a known input level, switch the
buzzer supply, or protect the Echo input.

## Run in Wokwi

1. Run **Wokwi: Select Config File** and choose the component's `.toml` file
   from the repository's `wokwi/` folder.
2. Run **Wokwi: Start Simulator** and keep the simulator visible.
3. Run **Tasks: Run Task → Wokwi: Run component test** and choose the matching
   Python file.
4. Interact with the component and watch the Wokwi Terminal.

The combined potentiometer/pixel demonstration remains in
[`potentiometer_pixel_spinner.py`](potentiometer_pixel_spinner.py).
