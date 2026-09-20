# Prompt Engineering

## Prompt Olympics

Give every group the same target, such as asking an AI system to produce a
recipe for a fictional restaurant. Reveal requirements gradually:

- exactly five ingredients;
- vegetarian;
- suitable for a 12-year-old to cook;
- under EUR 8;
- include one unusual ingredient;
- output as a table;
- do not repeat an ingredient;
- give the restaurant a ridiculous name.

In the first round, students write a one-sentence prompt. They improve it as
requirements are added. Then introduce a working structure:

> Role + task + context + constraints + output format + example

Score the output against the specification rather than judging how clever the
prompt sounds. The central idea is:

> A prompt is a specification that can be tested.

## Vibe coding example: vocabulary practice

This existing example shows prompt engineering applied to creating a small
application. A student provides a photo of French vocabulary and asks the AI
to build a flashcard app.

Example prompt:

> Build a small flashcard app that helps me learn the vocabulary in the
> attached photo. Track a statistic for each word and show words less often as
> I learn them, so that my progress is visible. The app should also be fun and
> motivating to use.

The original result was deployed as
[Wortgarten](https://wortgarten-vokabeln.danields.chatgpt.site/).

Use this example to identify what the prompt already specifies:

- the source material;
- the task;
- progress tracking;
- adaptive repetition;
- a desired user experience.

It also opens questions that belong to other topics:

- **Online Privacy:** What might be visible in an uploaded photograph?
- **Fabrications:** How will the student check that every vocabulary item was
  read and translated correctly?
- **Human judgment:** Does the generated learning strategy actually help?

### Still to develop

- a classroom-safe input image without personal information;
- criteria for evaluating the generated application;
- a second prompt round based on observed problems rather than extra features.
