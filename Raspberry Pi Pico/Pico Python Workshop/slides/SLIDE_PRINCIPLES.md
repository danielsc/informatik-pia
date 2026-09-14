# Workshop slide principles

These rules apply to every teacher-presented Reveal.js deck in this folder.
The slides provide the explicit teaching and guided practice. The daily
Markdown lesson provides the student lab, detailed wiring instructions, code
links, and extension work.

## 1. Write for students in the room

- Every visible heading, label, question, and instruction must make sense to a
  student seeing it for the first time.
- Do not expose planning language such as “teaching content,” “lab launch,”
  “concept gate,” “pause point,” “scaffolding,” or curriculum mapping.
- Do not use a technical term before defining it in student language.
- Prefer a concrete action or example over an abstract teaching phrase.
  For example, say “Change only `pritn` to `print`, then run it again” rather
  than “make the smallest change that tests the hypothesis.”
- Keep curriculum mapping, expected answers, pacing, and teacher checkpoints in
  speaker notes or the final teacher-reference slide.

## 2. Make the classroom state explicit

When a slide changes what students should do, show one short activity label:

- **Watch and discuss** — students do not type or build.
- **Try in Thonny** — students type or run the displayed example.
- **Try together** — the teacher leads one shared run.
- **On paper** — students predict, trace, or design before touching code.
- **Build while unplugged** — students stop the program, disconnect USB, and
  follow the diagram.
- **Test the circuit** — students reconnect only after the stated check.

Never leave students guessing whether displayed code is an explanation or an
instruction to run it.

## 3. Teach before asking students to use

- Preserve the TEALS dependency order while adapting examples to Thonny and
  MicroPython.
- Define a concept, model it, let students predict or practise it, and only then
  require it in a Pico task.
- A slide must not silently rely on vocabulary introduced only in a later day.
- Identify supplied APIs and safety wrappers explicitly. Students may call a
  supplied hardware or timing API without being expected to reproduce its
  implementation.
- Keep `try`/`except`/`finally`, hardware constructors, and specialised timing
  details as provided scaffolding unless the lesson explicitly teaches them.

## 4. Adapt TEALS teaching; replace TEALS labs

- Read the actual relevant TEALS slide decks, including speaker notes, rather
  than relying only on the curriculum map.
- Preserve useful definitions, misconceptions, prediction routines, and concept
  order.
- Paraphrase and redesign the material; do not reproduce a TEALS presentation.
- Replace TEALS console labs and projects with the workshop's Pico lab, wiring
  diagram, and coding task.
- Keep a teacher-reference slide naming the source units or lessons.

## 5. Introduce every circuit with its task

Every circuit used that day must appear in the deck immediately before students
are asked to build or test it.

For each circuit:

1. State the purpose of the circuit and the exact code file it supports.
2. Tell students to stop the program and disconnect USB.
3. Show the complete course PNG without cropping important wires, rails,
   components, endpoint dots, or pre-power checks.
4. Provide a small link to the scalable HTML diagram and exact connection table.
5. Name the important pins, component orientation, voltage, and protection
   parts in student language.
6. State the unplugged partner or instructor check.
7. Only then tell students to reconnect and run the smallest test.

Combined circuits must be introduced as layered builds. Students retest each
known-working layer before running the combined program.

The slides never replace the diagram's HTML connection table.

## 6. Use precise code demonstrations

- Code shown for tracing must match the linked workshop program or be labelled
  as a deliberately smaller example.
- Reveal every executable line in order; do not skip a state-changing line.
- Ask for a prediction that names a specific output or value.
- When debugging, give one concrete symptom and a sequence of tests. Explain
  what each result tells the student to inspect next.
- Avoid unexplained ellipses in code students are expected to run.
- Use the same variable and function names as the corresponding starter.

## 7. Launch labs with concrete steps

- State which starter file to open and what setup it already supplies.
- Name exactly what students must add, in a sensible build order.
- Replace generic instructions such as “predict, run, explain, change” with
  concrete edits and observable results.
- Keep solution files out of the main student workflow.
- Put teacher progress checks and role-swap timing in speaker notes.
- End with a short exit ticket that checks the day's central idea, not syntax
  trivia.

## 8. Presentation and accessibility

- Use a 16:9, 1280 × 720 Reveal.js canvas.
- Keep a persistent **Full screen** button; also support Reveal's `F` key.
- Include speaker notes on every slide and presenter-view instructions.
- Use large, high-contrast type suitable for projection.
- Do not rely on colour alone; pair colour with text labels.
- Give every image meaningful alternative text.
- Keep local workshop assets local. Pin any external Reveal.js dependency to a
  specific version.
- Avoid text or links over diagrams. Put diagram links beside the heading.
- Check every representative slide at 1280 × 720 in Chromium.

## 9. Required structure

Each deck should contain:

1. student-facing mission and learning goals;
2. a visible route through the day;
3. explicit concept teaching and guided practice;
4. circuit-and-task introductions at the point of use;
5. a concrete daily challenge launch;
6. an exit ticket;
7. a final teacher-reference/source slide.

The number of sections and slides may vary. Clarity is more important than
matching another day's slide count.

## 10. Completion checks

Before calling a deck complete:

- confirm every slide has speaker notes;
- resolve every local image, code, lesson, and diagram link;
- confirm every required concept appears before its first student-owned use;
- confirm every circuit diagram appears directly before its build/test task;
- compare displayed pins, thresholds, values, and filenames with lesson and
  code;
- render the title, densest code slide, every circuit slide, and challenge
  slide in Chromium at 1280 × 720;
- check that no content is clipped or hidden beneath controls;
- check that student-facing text contains no undefined terms or teacher-only
  process language;
- run `git diff --check`.
