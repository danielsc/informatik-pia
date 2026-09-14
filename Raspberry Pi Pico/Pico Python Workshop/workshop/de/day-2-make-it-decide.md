# Tag 2: Lasst es entscheiden

## Mission

Verwandelt physische Eingaben in Entscheidungen und baut anschließend eine
Reaktionszeit-Challenge.

**Python:** Boolean-Werte, Vergleiche, Casting, `if`/`elif`/`else`, `while`,
Listen, Indizes, `append`, `len`<br>
**Hardware:** Taster, ADC, Potentiometer, PWM-LED<br>
**TEALS-Bezug:** Unit 2, Datentypen und Bedingungen

## 1. Ein Taster stellt eine Boolean-Frage

Trennt die USB-Verbindung. Holt den Taster, einen 10-kΩ-Widerstand, einen
220-Ω-Widerstand, eine rote LED und Jumperkabel.

[Öffnet das skalierbare HTML-Schaltbild des Kurses](../../diagrams/button-and-led.html).
Es zeigt die Pico-Anschlüsse, die Ausrichtung des Breadboards, die internen
Kontakte des Tasters und die Kontrollen vor dem Einschalten.

![Breadboard-Schaltung mit Taster und LED](../../diagrams/button-and-led.png)

Baut in dieser Reihenfolge:

1. Richtet den Pico wie gezeigt mit dem USB-Anschluss nach links aus.
2. Setzt den Taster genau wie gezeigt über die mittlere Rinne.
3. Fügt den 10-kΩ-Pull-up-Widerstand und den 220-Ω-LED-Widerstand hinzu.
4. Verbindet Stromversorgung, GND, GP13 und GP15.
5. Eine Person liest die HTML-Verbindungstabelle laut vor, während die andere
   auf jedes Loch zeigt.

Ein Taster mit vier Beinen besitzt nur zwei elektrische Anschlüsse. Die beiden
blauen, im Diagramm mit A markierten Beine sind immer verbunden. Dasselbe gilt
für die beiden roten, mit B markierten Beine. Beim Drücken werden A und B
verbunden.

Prüft vor dem Anschließen von USB nach Möglichkeit mit einem Multimeter im
Durchgangsprüfmodus:

1. Zwei Beine desselben Anschlusses sollten auch bei losgelassenem Taster
   piepen.
2. Ein A-Bein und ein B-Bein sollten bei losgelassenem Taster nicht piepen.
3. Der A-zu-B-Test sollte nur bei gedrücktem Taster piepen.

Wenn ihr den Taster in denselben Löchern um 90 Grad dreht, kann die Eingabe
dauerhaft gedrückt wirken. Falls das Programm immer `Pressed: True` ausgibt,
trennt USB und prüft die Ausrichtung, bevor ihr den Code ändert.

Führt
[`code/day-2/01_button_decisions.py`](../../code/day-2/01_button_decisions.py)
aus. Die Freenove-Schaltung ist active-low:

```python
pressed = not button.value()

if pressed:
    led.on()
else:
    led.off()
```

`if` wählt einen Pfad, wenn seine Boolean-Bedingung `True` ist; `else` wählt
den anderen Pfad. Das vorgegebene `while True` fragt den Taster immer wieder
ab, bis ihr Stop oder `Ctrl+C` drückt.

Der 10-kΩ-Pull-up-Widerstand sorgt dafür, dass GP13 bei losgelassenem Taster
`1` liest. Durch Drücken wird GP13 mit GND verbunden und liest `0`. `not`
wandelt dieses active-low-Signal in einen verständlichen Python-Wert um:
`pressed` ist `True`, wenn jemand den Taster drückt.

Sagt diese Ausdrücke voraus, bevor ihr sie ausprobiert:

```python
pressed == True
not pressed
pressed and score > 0
pressed or time_is_up
```

## 2. Von der analogen Welt zu Zahlen

Ein digitaler Eingang hat zwei Zustände. Ein Potentiometer kann viele Werte
liefern. Trennt USB und baut die folgende Schaltung auf.

Öffnet das
[skalierbare, barrierearme Diagramm für Potentiometer und LED](../../diagrams/potentiometer-and-led.html),
um die genauen Breadboard-Kontakte und die Verbindungstabelle zu sehen.

![Potentiometer an ADC0 und PWM-LED an GP15](../../diagrams/potentiometer-and-led.png)

Führt
[`code/day-2/02_potentiometer_led.py`](../../code/day-2/02_potentiometer_led.py)
aus.

Der Pico liest eine Zahl von 0 bis 65535:

```python
raw_value = knob.read_u16()
percent = int(raw_value / 65535 * 100)
```

Hier wandelt `int(...)` durch Casting einen Float in einen Integer um. Notiert
Werte nahe 0 %, 25 %, 50 %, 75 % und 100 %. Echte Messwerte sind nicht exakt.

Die PWM-Helligkeit verwendet einen Wert von 0 bis 65535:

```python
led.duty_u16(0)      # off
led.duty_u16(20000)  # dim
led.duty_u16(65535)  # full brightness
```

Ein `elif` fügt einen weiteren möglichen Pfad hinzu. Python führt nur den
ersten Zweig aus, dessen Bedingung wahr ist:

```python
if points >= 10:
    print("gold")
elif points >= 5:
    print("silver")
else:
    print("bronze")
```

### Schwellenwert-Challenge

Ändert das Programm so, dass die LED:

- unter 20 % aus ist;
- von 20 % bis 70 % schwach leuchtet;
- über 70 % hell leuchtet.

Verwendet `if`, `elif` und `else`.

## 3. Listen merken sich mehrere Ergebnisse

Probiert dies in der Shell aus:

```python
times = [410, 375, 522]
print(times[0])
times.append(330)
print(len(times))
print(min(times))
```

Indizes beginnen bei null. Sagt voraus, was `times[-1]` zurückgibt.

## 4. Eine `while`-Schleife wiederholt, solange eine Bedingung wahr ist

Ein Spiel muss den Taster beim Warten ständig prüfen:

```python
while button.value():
    sleep_ms(1)
```

Lest dies so: „Solange der Taster losgelassen ist, wartet 1 ms und prüft
erneut.“ Die Schleife endet, wenn `button.value()` zu `0` wird. Anders als
`while True` hat diese Schleife eine Bedingung, die falsch werden kann.

Für das entgegengesetzte Warten wird `not` verwendet:

```python
while not button.value():
    sleep_ms(10)
```

Lest dies so: „Solange der Taster gedrückt ist, wartet, bis er losgelassen
wird.“ Testet beide Schleifen mit print-Ausgaben, bevor ihr sie in das Spiel
einbaut.

Sagt voraus, welche Schleife sich für welche Aufgabe eignet:

- das gesamte Spiel weiterlaufen lassen;
- warten, bis der Taster gedrückt wird;
- wiederholen, bis fünf Ergebnisse gespeichert sind.

Die Datei für das Reaktionsspiel verwendet außerdem vorgegebene Timing-Werkzeuge
wie `randint()` und `ticks_ms()`. Ihr dürft diese Werkzeuge aufrufen, ohne zu
wissen, wie sie aufgebaut sind.

### Bereitschaftscheck vor dem Spiel

Alles, was ihr für die Grundversion schreiben müsst, wurde jetzt geübt:

| Spielcode | Wo er eingeführt wurde |
|---|---|
| Variablen und Zuweisung | Tag 1 |
| active-low `button.value()` | Tag 2, Abschnitt 1 |
| `if`/`else` und Vergleiche | Tag 2, Abschnitte 1 und 2 |
| `scores = []`, `append`, `len` und `min` | Tag 2, Abschnitt 3 |
| `while` mit einer Bedingung | Tag 2, Abschnitt 4 |
| Aufruf vorgegebener Werkzeuge wie `sleep_ms()` | Beispiele seit Tag 1 |

Für die Grundversion braucht ihr **kein** `for`, `range`, `def`, keine
Dictionaries und keine endlose `while True`-Schleife. Diese Ideen lernt ihr
entweder später oder sie bleiben Teil des vorgegebenen Gerüsts. `randint()`,
`ticks_ms()` und `ticks_diff()` sind vorgegebene Timing-Werkzeuge; ihr
verwendet nur die unten aufgeführten Aufrufmuster.

## Tagesprojekt: Reaktionszeit-Challenge

Baut die Taster-und-LED-Schaltung erneut auf. Beginnt mit
[`code/day-2/03_reaction_game_starter.py`](../../code/day-2/03_reaction_game_starter.py).
Der Starter enthält Importe, Pin-Einrichtung, eine leere `scores`-Liste und das
sichere Ausschalten der LED. **Ihr schreibt das Spiel.**

Die erste Version ist bewusst kleiner als ein kommerzielles Reaktionsspiel:
drei Runden, keine Fehlstart-Erkennung und zwei Ergebniskategorien.

### Schritt 1: Schreibt den Plan als Kommentare

Bringt diese Ideen in die richtige Reihenfolge, bevor ihr Python schreibt:

- wiederholen, bis die Ergebnisliste drei Werte enthält;
- warten, bis der Taster losgelassen ist;
- eine zufällige Zeit lang warten;
- die LED einschalten und die Startzeit speichern;
- warten, solange der Taster losgelassen ist;
- die vergangene Zeit berechnen und die LED ausschalten;
- das Ergebnis zur Liste hinzufügen;
- das Ergebnis einordnen und ausgeben.

### Schritt 2: Baut eine funktionierende Runde

Verwendet die vorgegebenen Werkzeuge:

- `randint(1000, 3000)` wählt die Wartezeit in Millisekunden;
- `sleep_ms(wait_ms)` wartet diese Zeit;
- `ticks_ms()` speichert einen Zeitstempel;
- `ticks_diff(end, start)` berechnet die vergangenen Millisekunden.

Schreibt und testet eine Runde, bevor ihr die äußere Spielschleife hinzufügt.
Nach dem Tastendruck muss die LED ausgehen und die Shell eine glaubwürdige
Reaktionszeit ausgeben. Denkt daran: Dieser active-low-Taster liest `1`, wenn
er losgelassen ist, und `0`, wenn er gedrückt ist. Verwendet eine
`while`-Schleife, um auf das Loslassen zu warten, und eine weitere, um auf den
Tastendruck zu warten.

### Schritt 3: Fügt eine Entscheidung hinzu

Schreibt eure eigene `if`/`else`-Anweisung:

- unter 350 ms wird `Quick!` ausgegeben;
- ab 350 ms wird `Keep practising!` ausgegeben.

Ändert nach dem ersten erfolgreichen Test den Grenzwert und sagt voraus, welche
Ergebnisse danach anders eingeordnet werden.

### Schritt 4: Macht aus einer Runde drei

Umschließt die funktionierende Runde mit:

```python
while len(scores) < ROUNDS:
    # your tested one-round code goes here
```

Dies ist eine begrenzte, keine endlose Schleife. Sie endet, sobald die Liste
drei Ergebnisse enthält. Die Warteschleifen für den Taster enden, wenn sich
sein Zustand ändert.

Fügt jeden Wert `reaction_ms` mit `append` zu `scores` hinzu. Gebt nach dem
Ende der Schleife die gesamte Liste und mit `min(scores)` das schnellste
Ergebnis aus.

Das vorgegebene `try`/`except`/`finally`-Gerüst dient der Sicherheit. Ihr müsst
diese Syntax heute nicht selbst schreiben. Verwendet
[`code/day-2/03_reaction_game_solution.py`](../../code/day-2/03_reaction_game_solution.py)
nur zur Wiederherstellung oder zum Vergleich, nachdem eure Version mit drei
Runden funktioniert.

### Erweiterungen

Wählt erst eine Erweiterung, wenn die Grundversion funktioniert:

- erkennt einen Tastendruck vor dem Aufleuchten der LED und meldet einen
  Fehlstart;
- berechnet den Durchschnitt mit `sum(scores) / len(scores)`;
- fügt mit `elif` eine dritte Ergebniskategorie hinzu;
- feiert eine persönliche Bestzeit;
- erweitert das Spiel auf fünf Runden;
- erstellt eine Version für zwei Personen.

Die optionale Datei
[`code/day-2/03_reaction_game_extension.py`](../../code/day-2/03_reaction_game_extension.py)
zeigt eine mögliche Fehlstart-Erkennung, nachdem ihr eure eigene entworfen
habt.

### Checkliste für die Vorführung

- Zeigt eine vollständige Runde mit Zeitmessung.
- Zeigt alle drei gespeicherten Ergebnisse.
- Erklärt, warum das Hauptprogramm eine `while`-Schleife braucht.
- Zeigt auf den Boolean-Ausdruck, der einen Wartevorgang beendet.
- Erklärt, warum jedes Ergebnis ein Integer ist.

## Abschlussticket

Schreibt eine Bedingung, die wahr ist, wenn `reaction_ms` mindestens 200 und
kleiner als 500 ist. Beschreibt anschließend, welche Werte genau auf den beiden
Grenzen liegen.
