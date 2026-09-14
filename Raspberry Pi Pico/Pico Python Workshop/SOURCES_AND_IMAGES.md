# Sources, Images, and Attribution

This workshop contains original teaching text and original example code. It was
informed by the sources below. Circuit images are linked from their official
web locations rather than copied into this repository.

## Teaching sequence

- [TEALS Second Semester Introduction to Computer Science][teals-map]
- [TEALS repository and licence statement][teals-repo]

TEALS material is licensed
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
The source repository is archived and no longer maintained. This workshop
adapts the concept sequence, omits EarSketch, and replaces screen-only examples
with physical computing activities.

The [teacher Reveal.js decks](slides/README.md) were developed from the actual
TEALS slide decks and lesson documents:

- Day 1: Unit 1 lessons 1.01-1.05;
- Day 2: Unit 2 lessons 2.01-2.06;
- Day 3: Unit 3 lessons 3.01-3.04 and Unit 4 lessons 4.01-4.04;
- Day 4: Unit 3 return-value material, Unit 6 dictionary lessons, and Unit 8
  planning material;
- Day 5: Unit 8 lesson documents, final-project organizer, development plan,
  and rubric.

The workshop decks paraphrase and reorganise the teaching sequence. They do
not copy the original TEALS slides, and their Pico labs replace the TEALS labs.

[teals-map]: https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/curriculum_map.md.html
[teals-repo]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science

## Hardware source

- [Freenove FNK0063 documentation][freenove-docs]
- [Freenove FNK0063 source repository and licence][freenove-repo]
- Local reference PDF: [`../Python_Tutorial.pdf`](../Python_Tutorial.pdf)

Freenove repository materials are licensed
[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
Freenove's name and logo remain their property. Linking does not imply
endorsement.

[freenove-docs]: https://docs.freenove.com/projects/fnk0063/en/latest/
[freenove-repo]: https://github.com/Freenove/Freenove_Super_Starter_Kit_for_Raspberry_Pi_Pico

## Visual reference index

| Topic | Lesson | Schematic | Hardware image |
|---|---|---|---|
| LED | [lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/1_LED_%28Important%29.html) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter01_19.png) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter01_20.png) |
| Button & LED | [lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/2_Button_%26_LED.html) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter02_03.png) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter02_04.png) |
| Potentiometer & LED | [lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/10_Potentiometer_%26_LED.html) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter10_00.png) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter10_01.png) |
| 8-RGB module | [lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/6_NeoPixel.html) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter06_04.png) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter06_05.png) |
| Passive buzzer | [lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/7_Buzzer.html) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter07_11.png) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter07_12.png) |
| HC-SR04 | [lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/22_Ultrasonic_Ranging.html) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter22_05.png) | [image](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter22_06.png) |

## Safety-related modification

The linked Freenove HC-SR04 circuit connects Echo directly to GP18. This course
does **not** reproduce that connection. It adds a 1 kΩ/2 kΩ divider because the
HC-SR04 Echo is a 5 V signal and RP2040 GPIO is 3.3 V-only. See
[Wiring and safety](WIRING_AND_SAFETY.md).

## Reuse

If this workshop is distributed as an adaptation of TEALS or Freenove
materials, preserve the relevant attribution, non-commercial, and share-alike
terms. This note is practical attribution guidance, not legal advice.
