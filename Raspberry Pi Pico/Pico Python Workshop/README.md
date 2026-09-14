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
## Wokwi fallback and teacher test

The repository root contains a ready-to-run Wokwi project:

- [`wokwi.toml`](../../wokwi.toml) uses the pinned Pico MicroPython firmware;
- [`diagram.json`](../../diagram.json) provides a Pico, potentiometer, and
  eight-pixel NeoPixel ring;
- the wiring matches GP26/ADC0 for the potentiometer and GP16 for pixel data.

In VS Code, run **Wokwi: Start Simulator**. Keep its tab visible, then run the
task **Wokwi: Run teacher pixel spinner** from **Tasks: Run Task**. The virtual
ring stands in for the Freenove eight-pixel module.

This simulation can also serve as a fallback if classroom hardware is
unavailable.