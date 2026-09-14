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
## Wokwi fallback and teacher tests

The repository's [`wokwi/`](../../wokwi/) folder contains:

- seven individual component simulations for the onboard LED, ordinary LED,
  button, potentiometer, RGB pixels, passive buzzer, and distance sensor;
- one combined potentiometer/pixel spinner demonstration;
- the matching pinned Pico MicroPython firmware configuration.

Choose a circuit with **Wokwi: Select Config File**, start it with
**Wokwi: Start Simulator**, and then run **Wokwi: Run component test** from
**Tasks: Run Task**. See the
[Wokwi test-bench instructions](../../wokwi/README.md) and the
[teacher component tests](code/teacher-tests/README.md).

These simulations can also serve as a fallback if classroom hardware is
unavailable. The virtual RGB ring stands in for the Freenove eight-pixel
module.