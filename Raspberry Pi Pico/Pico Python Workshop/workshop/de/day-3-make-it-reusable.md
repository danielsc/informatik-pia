# Tag 3: Wiederverwendbar machen

## Mission

Ordnet wiederholten Code in Funktionen und erweckt acht RGB-Pixel zum Leben.

**Python:** Importe, Funktionen, Parameter, Rückgabewerte, Listen, Tupel,
`for`, `range`, Indizes, verschachtelte Schleifen, lokale Variablen<br>
**Hardware:** Freenove-8-RGB-LED-Modul, Potentiometer<br>
**TEALS-Bezug:** Einheit 3 „Funktionen“ und Einheit 4 „Verschachtelte Schleifen und Listen“

## 1. Lernt das RGB-Modul kennen

Trennt die USB-Verbindung und folgt der
[8-RGB-Anschlusstabelle](WIRING_AND_SAFETY.md#freenove-8-rgb-led-modul).

Öffnet den
[skalierbaren, barrierearmen Schaltplan für das 8-RGB-Modul](../../diagrams/rgb8-module.html)
und verwendet den mit `IN` beschrifteten Anschluss des Moduls.

![Quadratisches Freenove-8-RGB-Modul, dessen IN-Anschluss mit GP16 verbunden ist](../../diagrams/rgb8-module.png)

Die offizielle
[Freenove-NeoPixel-Lektion](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/6_NeoPixel.html)
verwendet eine eigene Bibliothek. Unser Code nutzt das eingebaute
MicroPython-Modul `neopixel`; ihr braucht also keine zusätzliche Datei.

Führt [`code/day-3/01_neopixel_colours.py`](../../code/day-3/01_neopixel_colours.py) aus.

Eine RGB-Farbe ist ein Tupel aus Rot-, Grün- und Blauwert:

```python
RED = (30, 0, 0)
GREEN = (0, 30, 0)
BLUE = (0, 0, 30)
```

Haltet die Werte niedrig; `255, 255, 255` ist unnötig hell.
Das erste Programm wiederholt für jede Farbe dasselbe Muster aus Füllen,
Anzeigen, Ausgeben und Warten. Lasst diese Wiederholung vorerst stehen. In den
nächsten Abschnitten verbessert ihr sie mit Funktionen und Schleifen.

## 2. Funktionen benennen wiederverwendbare Aufgaben

Ihr habt bereits eingebaute Funktionen und Hardwarefunktionen wie
`print(...)`, `sleep_ms(...)` und `pixels.fill(...)` aufgerufen. Ein
**Argument** ist ein Wert, der in den Klammern übergeben wird.

Eine selbst definierte Funktion beginnt mit `def`:

```python
def level_to_colour(percent):
    if percent < 33:
        return (0, 0, 25)
    return (0, 25, 0)

colour = level_to_colour(20)
```

`percent` ist ein Parameter: der lokale Name, der ein Argument empfängt.
`return` gibt einen Wert an den aufrufenden Code zurück. Es gibt den Wert nicht
in der Shell aus.

Probiert diese kleinere Funktion in der Shell aus, bevor ihr eine Animation
bearbeitet:

```python
def doubled(number):
    return number * 2

print(doubled(4))
```

## 3. Eine `for`-Schleife besucht jedes Element oder jeden Index

Gebt zuerst eine bekannte Folge aus:

```python
for index in range(8):
    print(index)
```

`range(8)` erzeugt die Werte 0 bis 7. Die eingerückte Zeile läuft einmal für
jeden Wert, und `index` speichert den aktuellen Wert. Genau das sind die
gültigen Pixelindizes.

Wendet die Schleife nun auf die Hardware an:

```python
for index in range(8):
    pixels[index] = (0, 0, 20)
    pixels.write()
```

Welchen Fehler erwartet ihr bei `pixels[8]`?

Führt [`code/day-3/02_pixel_functions.py`](../../code/day-3/02_pixel_functions.py)
aus. Findet:

- eine Funktion ohne Parameter;
- eine Funktion mit zwei Parametern;
- eine lokale Variable;
- einen mit `return` zurückgegebenen Wert;
- verschachtelte Schleifen.

Erklärt, warum eine zurückgegebene Farbe besser wiederverwendbar ist als eine
ausgegebene Farbe.

Die letzten beiden Schleifen in dieser Datei sind verschachtelt: Für jeden
Wert der äußeren Schleife erledigt die innere Schleife ihre gesamte Arbeit.
Verfolgt zuerst ein Beispiel mit zwei Elementen auf Papier.

## 4. Schreibt jeweils eine Funktion

Implementiert und testet diese Funktionen nacheinander:

```python
def show_colour(colour):
    ...

def chase(colour, delay_ms):
    ...

def level_to_colour(percent):
    ...
```

Eine Funktion ist ein Versprechen: Mit passenden Eingaben erledigt sie genau
eine benannte Aufgabe.

## Tagesprojekt: Pixel Pet

Lasst das RGB-Modul an GP16 angeschlossen. Ergänzt das Potentiometer an GP26
mit 3.3 V und GND. In diesem Aufbau gibt es keine gewöhnliche LED.

Behaltet die drei RGB-Verbindungen aus dem Schaltplan von Tag 3 und ergänzt:

| Potentiometer-Pin | Verbindung |
|---|---|
| äußerer Pin `3V3` | dieselbe versorgte 3.3-V-Schiene wie RGB `IN V` |
| mittlerer `WIPER` | GP26 / ADC0 |
| äußerer Pin `GND` | dieselbe gemeinsame GND-Schiene wie RGB `IN G` |

Stoppt den RGB-Test und trennt USB, bevor ihr das Potentiometer ergänzt.
Kontrolliert zu zweit die drei neuen Kontakte, verbindet USB wieder und gebt
die ADC-Rohwerte aus, bevor ihr mit dem Pixel Pet beginnt.

Beginnt mit
[`code/day-3/03_pixel_pet_starter.py`](../../code/day-3/03_pixel_pet_starter.py).
Der Drehknopf steuert die „Energie“ des Tiers:

- 0-32%: sleepy, langsames blaues Pulsieren;
- 33-65%: curious, ein wanderndes grünes Pixel;
- 66-100%: excited, schnelles buntes Funkeln.

Anforderungen:

- Eine Funktion liest den Energie-Prozentwert und gibt ihn zurück.
- Eine Funktion entscheidet den Zustand und gibt ihn zurück.
- Je eine Funktion zeigt jeden Zustand an.
- Mindestens eine `for`-Schleife besucht alle Pixel.
- Mindestens eine Animation verwendet einen Pixelindex.
- Die Schleife gibt Energie und Zustand zum Debuggen aus.

Der vorgegebene `try`/`finally`-Block schaltet beim Programmende alle Pixel
aus. Diese Sicherheitsumhüllung müsst ihr nicht selbst schreiben.

### Zusatzideen

- Definiert Farben in einer Liste und durchlauft sie.
- Fügt eine „hungry“-Warnung hinzu, wenn die Energie zehn Messungen lang
  niedrig bleibt.
- Speichert die letzten fünf Messwerte und zeigt ihren Mittelwert an.
- Verwendet verschachtelte Schleifen für einen Lauf über zwei Runden.

### Demo-Checkliste

- Zeigt alle drei Wertebereiche.
- Erklärt einen Parameter und einen Rückgabewert.
- Erklärt, warum eure Funktionen leichter zu testen sind als eine lange
  Schleife.

## Abschlussfrage

Was ist der Unterschied zwischen:

```python
print(energy)
return energy
```

Mit welcher Zeile kann eine andere Funktion anhand des Werts entscheiden?
