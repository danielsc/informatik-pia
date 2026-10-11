# Workshop Code

These code files are shared by the
[English](../workshop/en/) and [German](../workshop/de/) workshop materials.
Python identifiers and comments remain in English in both versions.

For each project, filenames sort in teaching order: `1_starter`, then
`2_solution`, then an optional `3_extension`. Open the starter first; solutions
are teacher/recovery references, not the normal student workflow.

Open these files in Thonny and run them with the interpreter set to
**MicroPython (Raspberry Pi Pico)**.

| Folder | Programs |
|---|---|
| [`day-1`](day-1/) | first output, variables, Secret Signal starter and solution |
| [`day-2`](day-2/) | button decisions, potentiometer/PWM, reaction game |
| [`day-3`](day-3/) | RGB pixels, reusable functions, Pixel Pet |
| [`day-4`](day-4/) | timeout-safe distance, buzzer test, proximity alarm |
| [`day-5`](day-5/) | parking-assistant starter and complete reference |
| [`teacher-tests`](teacher-tests/) | preparation checks that are not part of the student sequence |

Before teaching Day 3, run
[`teacher-tests/potentiometer_pixel_spinner.py`](teacher-tests/potentiometer_pixel_spinner.py)
to test the potentiometer and all eight RGB pixels together. The centre
position stops the light; each side selects a direction, and turning farther
from the centre increases the rotation speed.

Stop endless loops with Thonny's red **Stop** button or `Ctrl+C`. Programs that
use PWM or RGB LEDs include cleanup code so outputs are left off.
Student programs use `try`/`finally`, introduced on Day 1. Cleanup runs on
normal completion, errors, and `Ctrl+C`; it does not suppress the interruption.

The button on GP13 is active-high (10 kΩ pull-down to GND, button to 3.3 V).
The ordinary LED uses GP15; buzzer control uses GP14 through its transistor
driver, so the two outputs can coexist.
