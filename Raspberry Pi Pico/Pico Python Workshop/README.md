# Raspberry Pi Pico Python workshop

Workshop materials are available in English and German.

| Language | Workshop Markdown | Presentation slides |
|---|---|---|
| English (source) | [`workshop/en/`](workshop/en/) | [`slides/en/`](slides/en/) |
| Deutsch (Übersetzung) | [`workshop/de/`](workshop/de/) | [`slides/de/`](slides/de/) |

**Hosted website:** <https://danielsc.github.io/informatik-pia/>

English is the leading language. Changes are made in English first and then
translated into German. Code, identifiers, filenames, code comments, diagrams,
and technical assets are shared rather than translated or duplicated. See
[`TRANSLATION_PRINCIPLES.md`](TRANSLATION_PRINCIPLES.md) for the complete
maintenance rules.

## Shared material

| Location | Contents |
|---|---|
| [`code/`](code/) | MicroPython examples, starters, solutions, and extensions shared by both languages |
| [`diagrams/`](diagrams/) | canonical circuit diagrams and PNG previews |
| [`slides/assets/`](slides/assets/) | shared slide images |
| [`slides/workshop-slides.css`](slides/workshop-slides.css) | shared presentation design |
| [`slides/workshop-slides.js`](slides/workshop-slides.js) | shared Reveal.js configuration |
| [`SOURCES_AND_IMAGES.md`](SOURCES_AND_IMAGES.md) | sources, licences, and image attribution |
## Teacher component tests

The [`code/teacher-tests/`](code/teacher-tests/) folder contains one small
physical-hardware test for every programmable workshop component. Its
[component-test guide](code/teacher-tests/README.md) links each Python file to
an exact breadboard diagram and a PNG preview.

Stop the program and disconnect USB before moving any wire or component. The
passive buzzer test uses the transistor driver, and the HC-SR04 test uses the
Echo voltage divider shown in their diagrams.

## Optional Wokwi experiment

The original combined potentiometer/pixel simulation remains parked in
[`wokwi/`](../../wokwi/) as an optional experiment. It is not part of the
physical component-test workflow.