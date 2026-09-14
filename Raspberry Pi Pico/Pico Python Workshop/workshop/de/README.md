# Python in der physischen Welt

## Ein fünftägiger Raspberry-Pi-Pico-Workshop

In diesem Kurs gebt ihr nicht nur Wörter auf einem Bildschirm aus. Ihr erzeugt
Licht, Farbe, Ton und Spiele und baut einen Parkassistenten, der auf die reale
Welt reagiert.

**Zielgruppe:** Schülerinnen und Schüler von etwa 12 bis 15 Jahren, Arbeit in Paaren<br>
**Dauer:** fünf ganze Workshoptage<br>
**Sprache:** MicroPython<br>
**Hardware:** Raspberry Pi Pico und Freenove FNK0063 Super Starter Kit<br>
**Editor:** Thonny

**Präsentationen für Lehrkräfte:** [öffnet die veröffentlichte
Folien-Website][slides-site] — das Repository muss nicht geklont werden.

Die Lernabfolge ist an die
[Curriculum Map von TEALS Introduction to Computer Science][teals] angelehnt.
Die EarSketch-Einheit wird bewusst ausgelassen. Die Hardware-Aktivitäten
verwenden die [Python-Dokumentation zum Freenove FNK0063][freenove].

[teals]: https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/curriculum_map.md.html
[freenove]: https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python.html
[slides-site]: https://danielsc.github.io/informatik-pia/

## Die Woche im Überblick

| Tag | Leitfrage | Python-Konzepte | Hardware | Tagesprojekt |
|---|---|---|---|---|
| [1](day-1-make-it-light.md) | Wie bewirkt Code, dass etwas geschieht? | Skripte, `print`, Werte, Variablen, Fehler | interne und externe LEDs | Geheime Signalmaschine |
| [2](day-2-make-it-decide.md) | Wie reagiert ein Computer? | Eingaben, boolesche Werte, Vergleiche, Bedingungen, `while`, Listen | Taster, Potentiometer, LED, PWM | Reaktionszeit-Challenge |
| [3](day-3-make-it-reusable.md) | Wie vermeiden wir Wiederholungen? | Funktionen, Parameter, Rückgabewerte, `for`, `range`, Indizes | 8-RGB-LED-Modul, Potentiometer | Pixel-Haustier |
| [4](day-4-make-it-sense.md) | Wie kann Code die Welt messen? | Sensorwerte, Dictionaries, Timeouts, Zerlegung, Testen | HC-SR04 und passiver Buzzer | Prototyp eines Näherungsalarms |
| [5](day-5-parking-assistant.md) | Wie werden einzelne Teile zu einem Produkt? | Integration, Zustand, Debugging, Anforderungen, Testfälle | Abstand, Ton, RGB-Anzeige | Parkassistent |

## Hier beginnen

1. Lest die [gemeinsame Referenz zu Verkabelung und
   Sicherheit](WIRING_AND_SAFETY.md) und baut ausschließlich nach dem
   gerenderten Diagramm in der Lektion des jeweiligen Tages.
2. Öffnet Thonny und wählt unten rechts **MicroPython (Raspberry Pi Pico)**.
3. Arbeitet zu zweit: Eine Person als **Driver** tippt, die andere als
   **Navigator** prüft die Schaltung und erklärt den Code. Tauscht die Rollen
   alle 20 Minuten.
4. Kopiert das passende Programm aus [`code/`](../../code/) in euren eigenen
   Ordner.
5. Startet ein Programm mit Thonnys grüner Schaltfläche **Run**.
6. Stoppt eine Endlosschleife mit der roten Schaltfläche **Stop** oder `Ctrl+C`.
7. Trennt die USB-Stromversorgung, bevor ihr eine Schaltung verändert.

Die Beispiele sind bewusst klein. Tippt sie ab, führt sie aus, verändert sie
und sagt voraus, was passieren wird. Beginnt erst danach mit der Challenge.

Einige bereitgestellte Programme enthalten eine
`try`/`except`/`finally`-Sicherheitshülle, damit `Ctrl+C` die Ausgänge
ausschaltet. Ihr müsst diese Hülle nicht auswendig schreiben können.
Konzentriert euch auf den neuen Code, auf den die Lektion hinweist; die Hülle
ist eine bereitgestellte Hilfestellung.

## Lernfortschritt in Python

Jedes Konzept wird vermittelt, bevor es in einer Challenge eingesetzt werden
muss:

| Tag | Neue, von den Lernenden selbst eingesetzte Konzepte | Erneut geübte frühere Konzepte |
|---|---|---|
| 1 | Werte, Typen, Variablen, Zuweisung, Skripte, Fehler | keine |
| 2 | Typumwandlung, boolesche Werte, Vergleiche, `if`/`elif`/`else`, Listen, `while` | Variablen und Debugging |
| 3 | Funktionsaufrufe, Parameter, `return`, `for`, `range`, Indizes, verschachtelte Schleifen | Bedingungen und Listen |
| 4 | `None`, Dictionaries, Sensorfunktionen, Timeouts | Funktionen, Schleifen und Bedingungen |
| 5 | Anforderungen, Integration, Grenzwerttests, Zustandskonfiguration | alle bisherigen Konzepte |

Bibliotheksspezifische Einrichtung wie `Pin`, `PWM`, `NeoPixel` und
`time_pulse_us` wird bereitgestellt und als Hardware-Vokabular erklärt. Ihr
verändert die Python-Logik erst, nachdem das entsprechende Konzept eingeführt
wurde.

## Woran ihr Erfolg erkennt

Bis Freitag solltet ihr:

- Eingabe, Verarbeitung und Ausgabe erklären können;
- sinnvolle Variablen und Datentypen wählen können;
- boolesche Ausdrücke und `if`/`elif`/`else` verwenden können;
- `while`- und `for`-Schleifen verwenden können;
- zusammengehörige Werte in Listen und Dictionaries speichern können;
- Funktionen mit Parametern und Rückgabewerten schreiben können;
- digitale und analoge Eingaben lesen können;
- digitale, PWM- und RGB-Ausgaben steuern können;
- herausfinden können, ob ein Problem im Code, in der Verkabelung oder in
  Annahmen liegt;
- einen Parkassistenten anhand schriftlicher Testfälle demonstrieren können.

## Übersicht der Kursdateien

| Ort | Zweck |
|---|---|
| [Veröffentlichte Folien][slides-site] | jeden Foliensatz direkt im Browser öffnen und präsentieren |
| [Leitfaden für Lehrkräfte](TEACHER_GUIDE.md) | Vorbereitung, Zeitplanung, Bewertung, Differenzierung und Antworten |
| [`slides/`](../../slides/de/) | Reveal.js-Foliensätze, Präsentationsnotizen, gemeinsame Stile und Gestaltungsprinzipien |
| [`diagrams/`](../../diagrams/) | genaue HTML-/SVG-Schaltbilder und ihre PNG-Vorschauen |
| [`code/day-1/`](../../code/day-1/) | erste Skripte, variables Blinken und Starter/Lösung für das Geheime Signal |
| [`code/day-2/`](../../code/day-2/) | Taster- und Potentiometerbeispiele sowie Starter/Lösung/Erweiterung für das Reaktionsspiel |
| [`code/day-3/`](../../code/day-3/) | RGB- und Funktionsbeispiele sowie Starter/Lösung für das Pixel-Haustier |
| [`code/day-4/`](../../code/day-4/) | Abstandssensor, Buzzer-Test und Näherungsalarm |
| [`code/day-5/`](../../code/day-5/) | Starter und vollständige Referenzimplementierung des Parkassistenten |
| [Verkabelung und Sicherheit](WIRING_AND_SAFETY.md) | gemeinsame Sicherheitsregeln, Vorgehen beim Lesen von Diagrammen und wiederverwendbare Pin-Referenz |
| [Quellen und Bilder](../../SOURCES_AND_IMAGES.md) | offizielle Referenzen, Zuordnung der Lehrquellen und Bildnachweise |

## Wichtige Einschränkung

Dies ist ein Lernprototyp, **kein Sicherheitssystem**. Verwendet den
Parkassistenten niemals, um ein echtes Fahrzeug zu führen oder Menschen oder
Eigentum zu schützen.
