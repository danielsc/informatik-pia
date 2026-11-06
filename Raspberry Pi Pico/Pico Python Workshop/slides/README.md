# Teacher slides · Präsentationsfolien

These Reveal.js decks contain the explicit teaching and guided-practice portion
of each workshop day. The daily Markdown lessons contain the student lab,
wiring diagrams, and coding tasks.

## View online

Open the hosted workshop at:

<https://danielsc.github.io/informatik-pia/>

The site is deployed automatically from `master` by GitHub Actions whenever
the workshop materials or deployment workflow change.

## Choose a language

| Language | Slides | Workshop Markdown |
|---|---|---|
| English (source) | [`en/`](en/) | [`../workshop/en/`](../workshop/en/) |
| Deutsch (Übersetzung) | [`de/`](de/) | [`../workshop/de/`](../workshop/de/) |

English is the leading language. Follow
[`../TRANSLATION_PRINCIPLES.md`](../TRANSLATION_PRINCIPLES.md) when changing
or translating workshop content.

## Present an English deck

Choose the deck for the current day:

| Day | Teacher deck | Student lab |
|---|---|---|
| 1 | [`en/day-1.html`](en/day-1.html) | [`../workshop/en/day-1-make-it-light.md`](../workshop/en/day-1-make-it-light.md) |
| 2 | [`en/day-2.html`](en/day-2.html) | [`../workshop/en/day-2-make-it-decide.md`](../workshop/en/day-2-make-it-decide.md) |
| 3 | [`en/day-3.html`](en/day-3.html) | [`../workshop/en/day-3-make-it-reusable.md`](../workshop/en/day-3-make-it-reusable.md) |
| 4 | [`en/day-4.html`](en/day-4.html) | [`../workshop/en/day-4-make-it-sense.md`](../workshop/en/day-4-make-it-sense.md) |
| 5 | [`en/day-5.html`](en/day-5.html) | [`../workshop/en/day-5-parking-assistant.md`](../workshop/en/day-5-parking-assistant.md) |

## Deutsche Foliensätze

| Tag | Präsentation | Arbeitsblatt |
|---|---|---|
| 1 | [`de/day-1.html`](de/day-1.html) | [`../workshop/de/day-1-make-it-light.md`](../workshop/de/day-1-make-it-light.md) |
| 2 | [`de/day-2.html`](de/day-2.html) | [`../workshop/de/day-2-make-it-decide.md`](../workshop/de/day-2-make-it-decide.md) |
| 3 | [`de/day-3.html`](de/day-3.html) | [`../workshop/de/day-3-make-it-reusable.md`](../workshop/de/day-3-make-it-reusable.md) |
| 4 | [`de/day-4.html`](de/day-4.html) | [`../workshop/de/day-4-make-it-sense.md`](../workshop/de/day-4-make-it-sense.md) |
| 5 | [`de/day-5.html`](de/day-5.html) | [`../workshop/de/day-5-parking-assistant.md`](../workshop/de/day-5-parking-assistant.md) |

The decks load a pinned version of Reveal.js from jsDelivr and keep workshop
images local. The shared design and authoring rules are documented in
[`SLIDE_PRINCIPLES.md`](SLIDE_PRINCIPLES.md).

Useful controls:

| Key | Action |
|---|---|
| arrow keys or Space | move through slides and reveals |
| **Days overview** link | return directly to the five-day deck list |
| `S` | open the presenter view with speaker notes and timer |
| `F` | enter fullscreen |
| `O` or Esc | show the slide overview |
| `?` | show Reveal.js keyboard help |

To serve the whole workshop locally from its root:

```bash
python3 -m http.server 8000
```

Then open, for example:

```text
http://localhost:8000/Raspberry%20Pi%20Pico/Pico%20Python%20Workshop/en/
```

Add `?print-pdf` to the URL and use the browser's print dialog to create a PDF
handout.

## Program downloads · Programme herunterladen

Every program used in the decks has a direct filename download link at its
activity, including starters and the component tests reused on Day 5.
Click the filename, save the `.py` file to **Downloads**, then open it from
Thonny's **Files pane on the left**, under the computer's Downloads folder.
Use **Local Python 3** for Day 1's opening desktop script and **MicroPython
(Raspberry Pi Pico)** for hardware programs. Click the **green play button**
only after the matching circuit has been checked. No clone or ZIP is needed.
If you already downloaded a file, reopen that copy rather than downloading
duplicates.

Jedes in den Folien verwendete Programm hat bei seiner Aktivität einen
direkten Download-Link, auch Starter und an Tag 5 erneut verwendete Bauteiltests.
Dateinamen anklicken, die `.py`-Datei nach **Downloads** herunterladen und in
Thonny **links unter Dateien** im Downloads-Ordner des Computers öffnen.
Für das erste Computer-Skript an Tag 1 **Lokales Python 3**, für Hardware
**MicroPython (Raspberry Pi Pico)** verwenden. Den **grünen Play-Button**
erst nach der passenden Schaltungsprüfung anklicken. Kein Klonen und kein ZIP
nötig. Bereits heruntergeladene Dateien wieder öffnen, statt doppelte Kopien
herunterzuladen.

Solutions are labelled teacher/recovery references after the final classroom
slide on Days 1, 2, 3, and 5, not the normal student starting files. Day 2's
separate extension download is optional after the three-round game works.
Day 4 uses a complete alarm example rather than a separate starter/solution
pair. Workshop programs are self-contained; their imports use built-in
MicroPython modules, so there are no extra helper files to copy onto the Pico.

Lösungen stehen an Tag 1, 2, 3 und 5 nach der letzten Unterrichtsfolie als
klar markierte Referenzen für Lehrkräfte, gemeinsamen Neustart oder Vergleich,
nicht als normale Startdateien. Die eigene Erweiterungsdatei an Tag 2 ist
optional nach dem funktionierenden Spiel mit drei Runden. Tag 4 verwendet ein
vollständiges Alarmbeispiel statt eines Starter-/Lösungspaars. Die Programme
sind eigenständig und importieren eingebaute MicroPython-Module; es müssen
keine zusätzlichen Hilfsdateien auf den Pico kopiert werden.

## Teaching sources

The decks adapt the teaching progression from the actual TEALS lesson decks
and lesson documents. TEALS labs are replaced by the workshop's Pico builds and
coding tasks. Hardware imports, constructors, specialised timing calls, and
safety cleanup are presented as supplied API vocabulary rather than syntax
students must reproduce from memory.
