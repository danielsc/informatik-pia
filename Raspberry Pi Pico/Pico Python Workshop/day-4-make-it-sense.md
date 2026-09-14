# Day 4: Make It Sense

## Mission

Measure distance safely, handle unreliable data, and prototype an alarm.

**Python:** sensor functions, return values, `None`, dictionaries, timeouts,
requirements, test cases  
**Hardware:** HC-SR04, passive buzzer and NPN driver  
**TEALS connection:** Unit 6 Dictionaries and Unit 8 project planning

## Safety gate

The HC-SR04 is a 5 V device, but Pico GPIO is 3.3 V-only. You must add the
1 kΩ/2 kΩ Echo voltage divider described in
[Wiring and safety](WIRING_AND_SAFETY.md#hc-sr04-distance-sensor-safer-echo-connection).
The official Freenove diagram's direct Echo wire is **not** used. Build from
the course diagram below; open the
[scalable, accessible version](diagrams/distance-sensor.html) to inspect every
contact and the exact connection table.

![Safe HC-SR04 breadboard wiring with a protected Echo input](diagrams/distance-sensor.png)

For comparison and attribution, see the official Freenove
[HC-SR04 layout](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter22_06.png)
and [Ultrasonic Ranging lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/22_Ultrasonic_Ranging.html).
The local diagram is original course artwork informed by that source.

An instructor must inspect the unpowered circuit before USB is connected.
Gather the HC-SR04, one 1 kΩ resistor, one 2 kΩ resistor, and jumper wires.
Place the sensor and both divider resistors before adding 5 V. Use the diagram's
connection table to verify `Echo → 1 kΩ → GP18 junction → 2 kΩ → GND`.

## 1. Measure a round trip

Run [`code/day-4/01_distance_sensor.py`](code/day-4/01_distance_sensor.py).
The sensor sends an ultrasonic pulse and times its return:

```text
distance = speed × round-trip time ÷ 2
```

The code uses a timeout. Without one, no returning echo could trap the program
inside a loop forever.

The supplied `try`/`finally` code returns Trigger low when the program stops.
It is safety scaffolding; today's student-owned ideas are the sensor function,
`None`, decisions, and test evidence.

Measure a flat object at 10, 20, 40, 60, and 100 cm:

| Ruler distance | Reading 1 | Reading 2 | Reading 3 | Difference |
|---:|---:|---:|---:|---:|
| 10 cm | | | | |
| 20 cm | | | | |
| 40 cm | | | | |
| 60 cm | | | | |
| 100 cm | | | | |

Try a soft object and an angled object. Why do readings change?

## 2. Represent “no measurement”

`measure_distance_cm()` returns either a float or `None`.

```python
distance = measure_distance_cm()

if distance is None:
    print("No echo")
else:
    print(distance)
```

`None` is more honest than pretending an invalid reading is zero. Zero would
incorrectly mean “dangerously close.”

## 3. Test the passive buzzer

Disconnect USB. Build the transistor driver from
[Wiring and safety](WIRING_AND_SAFETY.md#passive-buzzer-with-transistor-driver).

Open the [scalable, accessible buzzer diagram](diagrams/passive-buzzer.html) for
the exact connection table, transistor orientation, and pre-power checks.

![Passive buzzer and S8050 transistor-driver breadboard wiring](diagrams/passive-buzzer.png)

For comparison and attribution, see the official Freenove
[passive-buzzer circuit](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter07_11.png)
and [Buzzer lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/7_Buzzer.html).
The local diagram is original course artwork informed by that source.

Run [`code/day-4/02_buzzer_test.py`](code/day-4/02_buzzer_test.py). Start with
brief sounds and low PWM duty. Visual-only participation is always acceptable.

## 4. A dictionary holds configuration

Start with one dictionary in the Shell:

```python
zone = {"colour": "amber", "pause_ms": 600}
print(zone["colour"])
zone["pause_ms"] = 400
print(zone)
```

A dictionary stores **key-value pairs**. The key `"pause_ms"` finds its value;
assigning through that key updates the setting. Several related dictionaries
can then be grouped by state:

```python
ZONE_CONFIG = {
    "safe": {"beep_ms": 0, "pause_ms": 300},
    "caution": {"beep_ms": 80, "pause_ms": 520},
    "stop": {"beep_ms": 80, "pause_ms": 120},
    "invalid": {"beep_ms": 0, "pause_ms": 300},
}

print(ZONE_CONFIG["caution"]["pause_ms"])
```

Changing configuration should not require rewriting measurement logic.

## Daily build: Proximity Alarm Prototype

Run [`code/day-4/03_proximity_alarm.py`](code/day-4/03_proximity_alarm.py).
Today the Shell and onboard LED provide visual information; tomorrow the RGB
module replaces them.

Build both circuits together from the
[scalable, accessible proximity-alarm diagram](diagrams/proximity-alarm.html).
It uses GP19 for Trigger, protected GP18 for Echo, GP15 for buzzer control, and
the Pico's onboard LED; no external LED is required.

![Combined HC-SR04 and passive-buzzer proximity alarm wiring](diagrams/proximity-alarm.png)

Build in layers:

1. Stop the separate tests and disconnect USB.
2. Keep the verified sensor divider and add the buzzer circuit in the positions
   shown by the combined diagram.
3. Compare every combined connection with the HTML table.
4. Ask an instructor to check 5 V, the divider, transistor `E/B/C`, and common
   ground.
5. Reconnect and rerun the separate sensor and buzzer tests before starting the
   combined program.

Choose and document thresholds:

| State | Distance rule | LED | Sound |
|---|---|---|---|
| safe | | | |
| caution | | | |
| stop | | | |
| invalid | no echo | | |

Requirements:

- `measure_distance_cm()` returns a number or `None`;
- `classify_distance()` returns a state string;
- invalid input never creates a continuous alarm;
- sound becomes more urgent as the object approaches;
- `Ctrl+C` leaves LED and buzzer off.

## Plan tomorrow's product

Write four user stories:

- “When the obstacle is far away, I want ___ so that ___.”
- “When I enter caution range, I want ___ so that ___.”
- “When I must stop, I want ___ so that ___.”
- “When the sensor cannot read, I want ___ so that ___.”

Then write test cases with exact distances, expected colours, and expected
sound. Boundary values such as exactly 25 cm are especially important.

## Exit ticket

Why is a timeout part of correct behaviour rather than merely an optional
extra?
