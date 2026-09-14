# Leitfaden für Lehrkräfte

## Ziel des Kurses

Dieser Workshop verdichtet ausgewählte Inhalte eines halbjährigen TEALS-Kurses
auf fünf Projekttage. Nachhaltiges Verständnis ist wichtiger als die
Behandlung aller Themen. EarSketch wird ausgelassen; Physical Computing bildet
den kreativen Kontext. Objektorientierte Programmierung ist eine optionale
Erweiterung und kein Kernziel.

Jede Aktivität folgt diesem Rhythmus:

1. **Vorhersagen**, was Schaltung oder Code tun werden.
2. **Aufbauen**, während die USB-Stromversorgung getrennt ist.
3. **Ausführen** des kleinstmöglichen Tests.
4. **Erklären** der Kette aus Eingabe, Verarbeitung und Ausgabe.
5. **Verändern** einer Sache und erneutes Vorhersagen.
6. **Herausfordern**, Konzepte zu verbinden, ohne eine vollständige Lösung zu
   kopieren.

Verwenden Sie die
[Reveal.js-Folien für Lehrkräfte](../../slides/README.md) für die explizite
Vermittlung und angeleitete Übung. Die tägliche Markdown-Lektion bleibt das
Arbeitsblatt der Lernenden mit Schaltbildern, Code-Links und Baukriterien.

## Vor Beginn der Woche

- Installieren Sie die aktuelle Version von Thonny und die
  MicroPython-Firmware auf jedem Pico.
- Führen Sie `code/day-1/01_hello_pico.py` an jedem Arbeitsplatz aus.
- Gleichen Sie jedes Kit mit den Bauteillisten der Tageslektionen ab.
- Identifizieren Sie den passiven Buzzer. Er hat meist keine versiegelte
  Unterseite; verlassen Sie sich bei beschrifteten Bauteilen nicht allein auf
  das Aussehen.
- Legen Sie die Freenove-Widerstände `220 Ω`, `1 kΩ`, `2 kΩ` und `10 kΩ`
  bereit.
- Drucken Sie eine Darstellung der physischen Pico-Pinbelegung aus oder zeigen
  Sie sie an.
- Bauen und testen Sie einen vollständigen Parkassistenten.
- Prüfen Sie, ob das 8-RGB-Modul mit MicroPythons integriertem `neopixel`-Modul
  funktioniert.
- Markieren Sie mit Kreppband 15 cm, 30 cm, 60 cm und 100 cm auf den Tischen.
- Entscheiden Sie, ob die Lernenden 5-V-Schaltungen selbst anschließen dürfen.
  Eine Prüfung durch die Lehrkraft vor dem Anschließen von USB wird an Tag 4
  und 5 dringend empfohlen.

## Vorgeschlagener Tagesablauf

| Zeit | Aktivität |
|---|---|
| 09:00-09:25 | Einstieg, Demonstration, Wiederholungsfragen |
| 09:25-10:20 | angeleitete Konzepteinführung und erster Aufbau |
| 10:20-10:35 | Pause |
| 10:35-11:35 | Untersuchung und Codeänderungen |
| 11:35-12:15 | kurze Lerneinheit und Debugging-Sprechstunde |
| 12:15-13:00 | Mittagspause |
| 13:00-14:30 | tägliche Bau-Challenge |
| 14:30-15:00 | Präsentationen, Codelesen, Reflexion, Kits zurücksetzen |

Halten Sie Erklärungen kurz. Ein sichtbarer Fehler mit anschließendem
systematischem Debugging ist oft wertvoller als ein makelloser Vortrag.

## Zuordnung zum Curriculum

| Workshop | Ungefähre TEALS-Zuordnung | Bewusster Schwerpunkt |
|---|---|---|
| Tag 1 | Unit 1: Introduction to Python | Interpreter, Skripte, Strings, Zahlen, Variablen, Kommentare, Fehler |
| Tag 2 | Unit 2: Data Types and Conditionals | Typumwandlung, boolesche Werte, Vergleiche, Bedingungen, Listen, `while` |
| Tag 3 | Units 3 and 4: Functions; Nested Loops and Lists | Imports, Abstraktion, Parameter, Rückgabewerte, `for`, `range`, Indizes |
| Tag 4 | Unit 6 und Vorbereitung auf Unit 8 | Dictionaries als Konfiguration, Zerlegung, Anforderungen, Testen |
| Tag 5 | Unit 8: Final Project | Integration, Umfang, schrittweise Umsetzung, Testnachweise |

## Lernvoraussetzungen

Der TEALS-Ausgangskurs verwendet mehrere Unterrichtsstunden auf jede Unit.
Dieser fünftägige Workshop verdichtet diese Abfolge. Deshalb benötigt jeder Tag
einen kurzen, ausdrücklichen Zyklus aus Vermitteln, Üben und Anwenden. Behandeln
Sie Syntax, die nur in bereitgestellten Hilfsstrukturen vorkommt, nicht als
bereits gelernt.

| Bevor die Lernenden Folgendes einsetzen sollen ... | Zuerst vermitteln und üben |
|---|---|
| Variablen im Signal von Tag 1 | Werte, Typen, Zuweisung und das Ändern eines Werts |
| Bedingungen in der Challenge von Tag 2 | boolesche Ausdrücke, anschließend `if`/`elif`/`else` |
| Listen im Reaktionsspiel | Erstellen, Index 0, `append`, `len` und `min` |
| `while` im Reaktionsspiel | eine sichtbare Bedingung, die sich von wahr zu falsch ändert |
| selbst definierte Funktionen an Tag 3 | Aufrufe, Argumente, Parameter und `return` |
| `for` und `range` an Tag 3 | 0-7 ausgeben, bevor diese Indizes für Pixel verwendet werden |
| verschachtelte Schleifen in Animationen | ein kleines Zwei-mal-zwei-Beispiel auf Papier nachvollziehen |
| Dictionaries an Tag 4 | ein flaches Dictionary erstellen, darauf zugreifen und es aktualisieren |
| integrierte Logik an Tag 5 | für jede Hardware-Schicht erneut einen bekannten funktionierenden Test ausführen |

Die TEALS-Abfolge behandelt in Unit 1 die Grundlagen, in Unit 2 boolesche
Werte/Bedingungen/Listen/`while`, in Unit 3 Funktionen, in Unit 4 `for` und
verschachtelte Schleifen, in Unit 6 Dictionaries und in Unit 8 die
Projektplanung. Dieser Workshop bewahrt diese Abhängigkeiten, obwohl mehrere
Units auf einen Workshoptag fallen.

`try`/`except`/`finally`, Hardware-Konstruktoren und Details der
Timing-Bibliothek sind bereitgestellte Sicherheitshilfen. Erklären Sie ihre
Wirkung, prüfen Sie aber nicht, ob die Lernenden sie selbst reproduzieren
können.

An Tag 1 bleiben wiederholte Blinkblöcke bewusst sichtbar. Wenn an Tag 3
Funktionen und Schleifen eingeführt werden, sollte auf diesen Code
zurückverwiesen werden: Die Lernenden sehen zuerst das Problem und lernen dann
die Abstraktion, die es löst.

## Formative Bewertung

Stellen Sie beim Herumgehen diese Fragen:

- Was ist die Eingabe? Was ist die Ausgabe?
- Welche Zeile verändert die physische Welt?
- Welchen Typ hat dieser Wert?
- Bei welchen Werten ist diese Bedingung wahr?
- Warum wird hier eine Schleife benötigt?
- Was erhält diese Funktion und was gibt sie zurück?
- Ist dies ein Code-, Verkabelungs- oder Messproblem?
- Welcher kleinste Test könnte diese Möglichkeiten unterscheiden?

Tägliche Exit-Tickets:

| Tag | Frage |
| --- | --- |
| 1 | Zeichnet Pfeile, die zeigen, wie eine Variable ein LED-Muster verändert. |
| 2 | Schreibt einen booleschen Ausdruck, der eine schnelle Reaktion beschreibt. |
| 3 | Erklärt den Unterschied zwischen einem Parameter und einem Rückgabewert. |
| 4 | Nennt einen Grund, weshalb eine Abstandsmessung ungültig sein kann. |
| 5 | Nennt einen bestandenen Produkttest und eine Verbesserung, die ihr vornehmen würdet. |

## Kontrollpunkte der Tagesprojekte

### Tag 1: Geheime Signalmaschine

Minimum: eine benannte Nachricht, mindestens zwei Zeitvariablen und ein
erkennbares LED-Muster. Gute Arbeiten ergänzen eine externe LED und Kommentare,
die die Absicht erklären. Präsentieren Sie
[`slides/day-1.html`](../../slides/de/day-1.html), bevor Sie die Laborphase
starten. Die Präsentationsnotizen enthalten Fragen, Demonstrationen, erwartete
Antworten, Sicherheitshinweise zur Schaltung und empfohlene Übergänge.

### Tag 2: Reaktionszeit-Challenge

Minimum: Die Lernenden programmieren eine zufällige Wartezeit, messen einen
Tastendruck, klassifizieren ihn mit `if`/`else`, wiederholen dies mit `while`
über drei Runden, hängen jeden Wert an und melden den schnellsten. Gute Arbeiten
ergänzen `elif`, einen Durchschnitt oder eine Fehlstarterkennung. Verlangen Sie
nicht, dass die Lernenden die bereitgestellte Hardware-Einrichtung oder die
Aufräumhülle selbst reproduzieren.

Prüfen Sie vor der Freigabe der Starterdatei, ob die Lernenden
`while len(scores) < ROUNDS` und beide Warteschleifen für den Tasterzustand
erklären können. Keine davon ist endlos: Die Punkteschleife endet bei drei
Einträgen, und jede Tasterschleife endet, wenn sich die Eingabe ändert.
`randint`, `ticks_ms` und `ticks_diff` sind bereitgestellte APIs, keine
Implementierungsziele.

Präsentieren Sie
[`slides/day-2.html`](../../slides/de/day-2.html) vor und zwischen den Aufgaben
zu Taster, Potentiometer und Reaktionsspiel.

### Tag 3: Pixel-Haustier

Minimum: drei Zustände, die über den Potentiometer-Eingang ausgewählt und durch
Funktionen auf dem RGB-Modul angezeigt werden. Gute Arbeiten geben jedem
Zustand eine kurze Animation mit indizierten Pixeln.

Präsentieren Sie
[`slides/day-3.html`](../../slides/de/day-3.html) vor dem RGB-Aufbau und
verwenden Sie die Abschnitte zu Funktionen, Schleifen und Pixel-Haustier, wenn
die jeweiligen Aufgaben beginnen.

### Tag 4: Prototyp eines Näherungsalarms

Minimum: gültige Abstandsmessung, Klassifizierung als safe/caution/stop und
unterschiedliches Buzzer-Verhalten. Gute Arbeiten behandeln ein fehlendes Echo,
ohne einzufrieren, und dokumentieren Kalibrierungsnachweise.

Präsentieren Sie
[`slides/day-4.html`](../../slides/de/day-4.html) abschnittsweise, sodass jedes
Sicherheitsdiagramm unmittelbar vor dem Sensor-, Buzzer- oder kombinierten
Aufbau erscheint.

### Tag 5: Parkassistent

Präsentieren Sie
[`slides/day-5.html`](../../slides/de/day-5.html), während die Lernenden
Anforderungen, schichtweise Hardware-Integration, funktionsweise Umsetzung,
Tests und Präsentation durchlaufen.

Mindestanforderungen:

- Die Zustände safe, caution, stop und invalid sind unterscheidbar.
- Die optische Ausgabe funktioniert immer, auch im Stummmodus.
- Die Pieprate wird dringlicher, wenn der Abstand kleiner wird.
- Ein fehlendes Echo lässt das Programm nicht einfrieren.
- Die Lernenden können jede Funktion erklären und vier Testfälle demonstrieren.
- Beim Stoppen mit `Ctrl+C` schaltet das Programm alle Ausgänge aus.

## Differenzierung

**Unterstützung**

- Stellen Sie die vollständige Verbindungstabelle bereit, halten Sie
  Lösungsdateien aber zunächst zurück.
- Lassen Sie die Lernenden eine Konstante verändern, bevor sie neue
  Ablaufsteuerung schreiben.
- Verwenden Sie Codekarten: Import, Einrichtung, Eingabe, Entscheidung, Ausgabe,
  Verzögerung.
- Lassen Sie ein Paar ein bekannt funktionierendes Bauteil mit einem unsicheren
  vergleichen.
- Erlauben Sie den Start mit den `_starter.py`-Dateien.

**Erweiterung**

- Mittelwert und Median der Reaktionszeit berechnen.
- Den Abstand mit den letzten fünf gültigen Messwerten glätten.
- Den safe-Grenzwert über das Potentiometer einstellen.
- Jedes RGB-Pixel als Teil einer Abstandsanzeige verwenden.
- Zustandskonfiguration in einem Dictionary aus Dictionaries speichern.
- Eine Klasse `ParkingAssistant` erst erstellen, wenn die funktionsbasierte
  Version funktioniert.

## Debugging-Ablauf

Die Lernenden sollten das Symptom benennen, bevor sie etwas verändern:

1. Programm stoppen.
2. USB trennen, bevor Kabel berührt werden.
3. Jeweils ein Kabel mit der Pin-Tabelle vergleichen.
4. Ausrichtung der Bauteile und Widerstandswerte prüfen.
5. USB wieder verbinden und den kleinsten Bauteiltest ausführen.
6. Rohe Eingabewerte ausgeben.
7. Die Bedingung an ihren Grenzwerten testen.
8. Bauteile erst verbinden, nachdem jedes einzeln funktioniert.

Raten Sie von zufälligem Umverdrahten und gleichzeitigen Änderungen an mehreren
Zeilen ab.

## Bewertungsraster zum Ende der Woche

| Kriterium | Anfang | In Entwicklung | Sicher | Fortgeschritten |
|---|---|---|---|---|
| Python-Verständnis | liest Code mit Hilfe | erklärt Variablen und Bedingungen | erklärt Schleifen, Funktionen und Zustand | begründet Abstraktionen und Abwägungen |
| Physisches System | ein Bauteil funktioniert | mehrere Teile funktionieren einzeln | integriertes System erfüllt die Kriterien | robuste Kalibrierung oder Erweiterung |
| Debugging | rät | prüft Code oder Schaltung | grenzt Probleme mit kleinen Tests ein | dokumentiert Nachweise und Grenzfälle |
| Kommunikation | zeigt Ausgabe | beschreibt Verhalten | erklärt Eingabe, Verarbeitung, Ausgabe und Funktionen | verbindet Designentscheidungen mit Bedürfnissen der Nutzenden |
| Teamarbeit | ungleiche Beteiligung | teilt einige Aufgaben | tauscht Driver-/Navigator-Rollen | unterstützt andere Teams, ohne zu übernehmen |

## Zurücksetzen und Aufbewahren

Am Ende jedes Tages:

- das laufende Skript stoppen;
- PWM und RGB-LEDs ausschalten;
- USB trennen;
- Potentiometer und 3.3-V-/GND-Verkabelung von Tag 2 nach Möglichkeit für Tag 3
  stehen lassen, aber die normale LED entfernen, bevor das RGB-Modul ergänzt
  wird;
- die Schaltung von Tag 3 vor dem Aufbau mit höherer Spannung an Tag 4 abbauen;
- Bauteile zählen und Widerstände nach Werten getrennt aufbewahren.
