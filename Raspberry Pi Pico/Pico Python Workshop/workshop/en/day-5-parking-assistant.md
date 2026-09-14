# Day 5: Build a Parking Assistant

## Mission

Integrate sensing, decisions, light, and sound into one testable product.

**Python:** decomposition, dictionaries, state, integration, boundary testing,
debugging, cleanup<br>
**Hardware:** HC-SR04, passive buzzer driver, 8-RGB module<br>
**TEALS connection:** Unit 8 Final Project

This is a table-top learning prototype, **not a real vehicle safety device**.

## 1. Build in layers

Use the combined pin plan in
[Wiring and safety](WIRING_AND_SAFETY.md#combined-builds).
Keep USB disconnected until an instructor has checked the HC-SR04 divider,
5 V wiring, transistor orientation, and common grounds.

Build from the
[scalable, accessible complete parking-assistant diagram](../../diagrams/parking-assistant.html).
It includes the protected HC-SR04, transistor-driven passive buzzer, and the
8-RGB module's `IN` header on its separate 3.3 V supply.

![Complete parking assistant breadboard wiring](../../diagrams/parking-assistant.png)

This original course diagram is informed by the official Freenove
ultrasonic-ranging, buzzer, and NeoPixel lessons.

| Component | Signal | Power |
|---|---|---|
| HC-SR04 | Trig GP19; Echo via divider to GP18 | 5 V and GND |
| passive buzzer driver | GP15 through 1 kΩ to NPN base | 5 V and GND |
| 8-RGB module IN | GP16 | 3.3 V and GND |

Do not wire everything and immediately run the final endless loop. Build and
test one layer at a time:

1. With USB disconnected, build the HC-SR04 and Echo-divider part of the final
   diagram. Get an instructor check, then run Day 4's distance test.
2. Stop the program, disconnect USB, and add the transistor-driven buzzer.
   Reconnect only after checking `E/B/C`, then run Day 4's buzzer test.
3. Stop, disconnect, and add the RGB module's `IN` header on 3.3 V. Run Day 3's
   RGB colour test.
4. Stop and compare the whole build with the final HTML connection table. Get
   one final instructor check of 5 V, 3.3 V, the divider, and common ground.
5. Test `classify_distance()` with fixed numbers before using live readings.
6. Combine measurement and RGB output with sound muted.
7. Add short buzzer feedback, then test invalid input by pointing the sensor
   away from useful targets.

## 2. Agree on requirements

The supplied baseline uses:

| State | Rule | RGB display | Sound |
|---|---|---|---|
| safe | over 60 cm | green | silent |
| caution | over 25 cm through 60 cm | amber | slow beep |
| stop | 25 cm or less | red | rapid beep |
| invalid | no usable echo | blue | silent |

You may adjust thresholds after calibration, but record the change.

## 3. Read the architecture

```python
distance_cm = measure_distance_cm()
zone = classify_distance(distance_cm)
show_zone(zone, distance_cm)
sound_zone(zone)
```

Each function has one main responsibility. This makes failures easier to
isolate.

Start from
[`code/day-5/parking_assistant_starter.py`](../../code/day-5/parking_assistant_starter.py).
Use [`code/day-5/parking_assistant.py`](../../code/day-5/parking_assistant.py) only
for comparison, recovery, or teacher demonstration.

The starter deliberately supplies imports, pin setup, cleanup, and function
names. Students complete logic using concepts already taught: conditions,
functions, return values, loops, and dictionary lookups.

## 4. Required behaviour

- Use named constants for pins and thresholds.
- Handle a missing echo without freezing.
- Use a dictionary for zone colours or timing.
- Show safe, caution, stop, and invalid states visually.
- Increase visual urgency as distance decreases.
- Increase beep urgency as distance decreases.
- Keep the safe and invalid states silent.
- Print distance and state for test evidence.
- Turn RGB output and PWM off after `Ctrl+C`.

## 5. Test before decorating

| Test | Input/setup | Expected | Actual | Pass? |
|---|---|---|---|---|
| T1 | flat target at 100 cm | safe, green, silent | | |
| T2 | flat target at 40 cm | caution, amber, slow beep | | |
| T3 | flat target at 15 cm | stop, red, rapid beep | | |
| T4 | no useful echo | invalid, blue, silent | | |
| T5 | exactly safe threshold | agreed boundary behaviour | | |
| T6 | exactly stop threshold | agreed boundary behaviour | | |
| T7 | stop program | all outputs off | | |

If a test fails, isolate one component. Do not rewrite the entire program.

## 6. Product challenge

After the baseline passes all tests, choose **one** meaningful improvement:

- a distance bar that fills more pixels as the obstacle approaches;
- a potentiometer that adjusts the caution threshold;
- mute mode while visual warnings remain active;
- smoothing using the latest five valid measurements;
- different tones as well as different beep rates;
- a startup self-test that checks every colour and sound;
- an enclosure or dashboard made from card, with sensor openings unobstructed.

Scope is a programming skill. One reliable improvement is better than five
unfinished ideas.

## 7. Final demonstration

Each pair has three minutes:

1. State the user problem and safety limitation.
2. Demonstrate safe, caution, stop, and invalid cases.
3. Show one boundary test.
4. Explain one function with a parameter and return value.
5. Describe one bug and the evidence used to fix it.
6. Name the next improvement.

## Reflection

- Which programming idea became clearer because you could see or hear it?
- Which bug was in code, which was in wiring, and which was an assumption?
- Where does your program store state or configuration?
- How would requirements change for a real product?
