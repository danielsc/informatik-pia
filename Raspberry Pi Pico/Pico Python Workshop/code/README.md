# Workshop Code

These code files are shared by the
[English](../workshop/en/) and [German](../workshop/de/) workshop materials.
Python identifiers and comments remain in English in both versions.

For each project, filenames sort in teaching order: `1_starter`, then
`2_solution`, then an optional `3_extension`. Open the starter first; solutions
are teacher/recovery references, not the normal student workflow.

Start Day 1 with the download link for
[`00_first_script.py`](day-1/00_first_script.py) in the first script activity and save it to
**Downloads**. In Thonny's **Files pane on the left**, open the **Downloads**
folder on your computer and double-click **`00_first_script.py`**.
If the pane is hidden, choose **View → Files**. Select **Local Python 3**
and click the **green play button (Run)**. This first script needs no Pico.

For the hardware programs, switch the interpreter to
**MicroPython (Raspberry Pi Pico)** after connecting the Pico by USB.

All day-program files have direct downloads in the matching English and German
slides; no clone or ZIP is needed. Examples and starters are linked at their
activities, including component tests reused on Day 5. Solutions are clearly
labelled teacher/recovery references at the end of Days 1, 2, 3, and 5; Day 2's
extension is optional after the baseline works. Day 4 uses the complete alarm
example. These files are self-contained and use built-in MicroPython modules;
there are no extra helper files to download. Day 1 also links the known-good
[`GP15 LED test`](teacher-tests/02_external_led.py) in its troubleshooting activity.

| Folder | Programs |
|---|---|
| [`day-1`](day-1/) | first desktop script, Pico output, variables, Secret Signal starter and solution |
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
