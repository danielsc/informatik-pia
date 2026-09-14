# Workshop translation principles

## Source of truth

- English (`en`) is the leading language and the source for future content
  changes.
- German (`de`) is maintained as a translation of the English teaching
  material.
- Change English first. Then update German in the same pull request or commit
  whenever the change affects translated content.
- Keep both versions structurally parallel: matching days, slide order,
  headings, activities, safety warnings, links, and speaker notes.

## What is translated

Translate language used to teach, guide, or assess:

- slide titles, explanations, prompts, activity labels, and speaker notes;
- daily lesson instructions, questions, checklists, and rubrics;
- teacher guidance and wiring/safety explanations;
- navigation, page descriptions, alternative text, and interface labels that
  describe the workshop;
- student-visible labels around code and circuit diagrams.

Do not translate material whose exact spelling is part of the technical task:

- Python and MicroPython code;
- filenames and paths;
- variable, constant, function, class, module, and API names;
- strings whose exact value students must type or observe;
- code comments;
- GPIO names, pin names, component identifiers, electrical units, and part
  numbers;
- command-line commands, keyboard shortcuts, and URLs.

If a code string is ordinary output rather than required syntax, keep it
unchanged when the German lesson refers to that exact output. Explain its
meaning in German around the code instead of creating a different program.

## German style

- Use clear, age-appropriate standard German suitable for eighth-grade
  students.
- Address students consistently with informal plural forms such as `ihr`,
  `euch`, and direct imperatives.
- Prefer short, concrete instructions over literal translations of English
  idioms.
- Use established German classroom terms, but retain the English technical
  term where students see it in Thonny or Python. For example:
  - Editor, Shell, Files;
  - Variable, Boolean value, list, dictionary, function, loop;
  - Run, Stop, MicroPython, GPIO, PWM, RGB.
- Introduce an English technical term with a short German explanation when it
  first appears. Do not invent German replacements that make the software or
  code harder to recognise.
- Preserve the distinction between instructions to watch, discuss, type,
  build while unplugged, test, and answer on paper.

## Code and identifiers

- Variable and function names remain English in every language.
- Code comments remain English.
- Code files are shared by all languages and are never duplicated solely for
  translation.
- Keep code blocks byte-for-byte equivalent between matching English and
  German materials unless the English source itself changes.
- Never translate Python keywords such as `if`, `else`, `while`, `for`,
  `return`, `True`, `False`, or `None`.

## Shared technical material

- `code/`, `diagrams/`, and `slides/assets/` are shared across languages.
- Diagram HTML and connection tables remain shared while they contain the
  canonical electrical design. Language-specific teaching text explains the
  diagram around the image.
- `SOURCES_AND_IMAGES.md`, diagram rubrics, and repository-maintenance files
  remain shared unless a translated version provides clear classroom value.
- Safety facts, voltages, resistor values, pin assignments, and test criteria
  must be identical in every language.

## Paths and public website

- English slides live in `slides/en/`; German slides live in `slides/de/`.
- English workshop Markdown lives in `workshop/en/`; German Markdown lives in
  `workshop/de/`.
- Shared assets are referenced with relative paths; do not duplicate them in
  language folders.
- The GitHub Pages root offers a language choice.
- Public language landing pages live at `/en/` and `/de/`.
- Existing `/slides/day-N.html` URLs redirect to the corresponding English
  deck for backward compatibility.

## Translation review

For each matching English/German pair:

1. Confirm the same number and order of slides or lesson sections.
2. Confirm code blocks, identifiers, filenames, pin names, and values have not
   been translated.
3. Confirm all local links resolve from the language subfolder.
4. Confirm every image retains meaningful alternative text in that language.
5. Render representative slides at 1280 × 720 and check that longer German
   text does not clip or cover diagrams.
6. Confirm speaker notes exist for every slide in both languages.
7. Recheck safety wording and electrical values independently of prose quality.
