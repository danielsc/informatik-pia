# BerryBase-Einkaufsliste für den Pico-Python-Workshop

**Stand:** 30. September 2026  
**Kursgröße:** ca. 70 Schülerinnen und Schüler  
**Organisation:** 35 Zweierteams + 3 vollständige Reserve-Sets = **38 Sets**

Diese Liste ist aus den tatsächlich verwendeten Schaltungen des aktuellen
Fünf-Tage-Workshops abgeleitet. Maßgeblich sind
[`workshop/en/WIRING_AND_SAFETY.md`](workshop/en/WIRING_AND_SAFETY.md) und die
zugehörigen Schaltpläne.

Für eine Schulbestellung dieser Größe sollte ein Angebot über den
[BerryBase-B2B-Shop](https://b2b.berrybase.de/) eingeholt werden. Preise und
Lagerbestände ändern sich. Mechanisch kritische Teile sollten zunächst als
Muster bestellt werden.

## Kurzfassung

| Teil | Bedarf | Bestellvorschlag | Status |
|---|---:|---:|---|
| Raspberry Pi Pico 2 H | 38 | 38 | direkt passend |
| Breadboard, 830 Kontakte | 38 | 38 | direkt passend |
| Jumperkabel Stecker–Stecker, 40er-Band | 38 Bänder | 38 | direkt passend |
| rote 5-mm-LED | 38 + Reserve | 50 | direkt passend |
| 6×6-mm-Taster, 4 Pins | 38 + Reserve | 50 | Muster prüfen |
| Breadboard-Potentiometer, 10 kΩ linear | 38 + Reserve | 40 | direkt passend |
| HC-SR04-Ultraschallsensor | 38 + Reserve | 40 | direkt passend |
| 8×WS2812-NeoPixel-Stick | 38 + Reserve | 40 | direkt passend |
| 220-Ω-Widerstand | 38 + Reserve | 100 | über B2B-Angebot |
| 1-kΩ-Widerstand | 76 + Reserve | 100 | über B2B-Angebot |
| 2-kΩ-Widerstand | 38 + Reserve | 100 | über B2B-Angebot |
| 10-kΩ-Widerstand | 38 + Reserve | 100 | über B2B-Angebot |
| USB-Datenkabel | 38 | 38 | Anschluss der Schulgeräte prüfen |
| passiver 5-V-Summer, unmoduliert | 38 + Reserve | 40 | nicht passend bestätigt |
| BC337-25-NPN-Transistor | 38 + Reserve | 50 | separat nach Kursumstellung |

Der höhere Bedarf bei **1 kΩ** ist beabsichtigt: Jedes vollständige Set braucht
einen 1-kΩ-Widerstand für den Summer-Treiber und einen zweiten für den
HC-SR04-Echo-Spannungsteiler.

## Direkt bei BerryBase bestellbare Teile

### 1. Raspberry Pi Pico 2 H

- **Menge:** 38
- **BerryBase:** [Raspberry Pi Pico 2 mit Headern, SKU RPI-PICO2-H](https://www.berrybase.de/raspberry-pi-pico-2-rp2350-mikrocontroller-board-mit-headern)
- **Warum diese Variante:** Die 2×20 Stiftleisten sind bereits verlötet. Im
  Unterricht ist kein Löten nötig.
- **Wichtig:** Der Pico 2 H verwendet Micro-USB.

### 2. Breadboard

- **Menge:** 38
- **BerryBase:** [Breadboard mit 830 Kontakten](https://www.berrybase.de/breadboard-mit-830-kontakten)
- **Warum 830 Kontakte:** Es bietet genug Platz für Pico, Sensor,
  Spannungsteiler, Summer-Treiber und RGB-Modul im Abschlussprojekt.

### 3. Jumperkabel

- **Menge:** 38 Bänder mit je 40 Kabeln
- **BerryBase:** [40pin Jumper-/Dupont-Kabel Male–Male, trennbar, 20 cm](https://www.berrybase.de/40pin-jumper-dupont-kabel-male-male-trennbar-laenge-0-20-m)
- **SKU:** `DUPK-40-MM-20`
- **Hinweis:** Die Kabel lassen sich einzeln vom Flachband trennen.

### 4. Rote 5-mm-LEDs

- **Menge:** mindestens 50; bei günstigem Mengenpreis 100
- **BerryBase:** [Kingbright Low-Current-LED, 5 mm, rot](https://www.berrybase.de/kingbright-low-current-led-5mm-rot)
- **Hinweis:** Pro Set wird eine LED verwendet. Reserve ist sinnvoll, weil
  Beinchen im Schulbetrieb verbogen oder gekürzt werden.
- **Sicherheitsregel:** Jede LED wird nur mit dem 220-Ω-Vorwiderstand aus
  Abschnitt 9 betrieben.

### 5. Breadboard-Potentiometer

- **Menge:** 40
- **BerryBase:** [Breadboard-Potentiometer, 10 kΩ](https://www.berrybase.de/breadboard-potentiometer-10k-ohm)
- **Warum passend:** Das kompakte Potentiometer ist ausdrücklich für das
  Breadboard ausgelegt und entspricht damit dem Aufbau im Kurs wesentlich
  besser als ein Potentiometer mit Lötösen.
- **Wareneingangsprüfung:** Vor dem Verteilen die drei Pins als `3V3`, `WIPER`
  und `GND` identifizieren.

### 6. Ultraschallsensor

- **Menge:** 40
- **BerryBase:** [HC-SR04-Ultraschallsensor](https://www.berrybase.de/hc-sr04-ultraschall-sensor)
- **Schaltung:** Betrieb mit 5 V. Echo darf nur über den vorgeschriebenen
  1-kΩ/2-kΩ-Spannungsteiler an GP18 gelangen.

### 7. 8er-NeoPixel-Stick

- **Menge:** 40
- **BerryBase:** [NeoPixel-Stick mit 8 WS2812 5050 RGB-LEDs](https://www.berrybase.de/neopixel-stick-mit-8-ws2812-5050-rgb-leds)
- **SKU:** `NEOPS8`
- **Wareneingangsprüfung:** Vor dem Austeilen `IN`, Datenrichtung und
  Pinbeschriftung prüfen. Das Kursdiagramm verwendet den Eingang des Moduls,
  nicht `OUT`.
- **Betrieb im Kurs:** Der Stick wird mit niedrigen Helligkeitswerten an 3,3 V
  betrieben, wie in Code und Schaltplan dokumentiert.

### 8. USB-Datenkabel

Zuerst die Anschlüsse der Schulgeräte prüfen. Jedes Kabel muss
**Datenübertragung** unterstützen; reine Ladekabel funktionieren mit Thonny
nicht.

| Computeranschluss | Menge | BerryBase |
|---|---:|---|
| USB-A | 38 | [Offizielles Raspberry-Pi-Micro-USB-Kabel, 1 m](https://www.berrybase.de/offizielles-raspberry-pi-micro-usb-kabel-rot-1-0m) |
| USB-C | 38 | [Micro-USB-Kabel und Datenkabel](https://www.berrybase.de/multimedia-office/kabel-adapter/computer/usb-kabel-adapter/micro-usb/) – dort USB-C auf Micro-B auswählen |

Nur eine der beiden Varianten bestellen oder die 38 Kabel passend zum
tatsächlichen Gerätebestand aufteilen.

## Über das B2B-Angebot konkret anfragen

### 9. Widerstände

BerryBase führt
[Widerstände und Widerstandssortimente](https://www.berrybase.de/bauelemente/passive-bauelemente/widerstaende/).
Für 38 Sets sollten im Angebot ausdrücklich die folgenden axial bedrahteten
THT-Widerstände stehen:

| Wert | Verwendung | Bestellmenge |
|---:|---|---:|
| 220 Ω | Vorwiderstand der gewöhnlichen LED | 100 |
| 1 kΩ | Transistor-Basis und oberer HC-SR04-Teilerwiderstand | 100 |
| 2 kΩ | unterer HC-SR04-Teilerwiderstand | 100 |
| 10 kΩ | Pull-up des Tasters | 100 |

0,25 W oder mehr ist für die Kursschaltungen ausreichend. **Nicht 2,2 kΩ
anstelle von 2 kΩ liefern lassen.** Die Kursunterlagen und die Berechnung des
Echo-Spannungsteilers verwenden ausdrücklich 1 kΩ und 2 kΩ.

### 10. Taster

- **Zielmenge:** 50
- **Kandidat:** [Kurzhubtaster, vertikale Printmontage, 6×6 mm, Höhe 5,0 mm](https://b2b.berrybase.de/index.php?ID=175&warenkorb_produktid=4072&warenkorb_merkliste_hinzu=4072)
- **Musterprüfung:** Ein Exemplar muss mechanisch über den Mittelkanal des
  ausgewählten Breadboards passen. Mit einem Multimeter prüfen, welche beiden
  Pins intern dauerhaft verbunden sind.

Erst nach erfolgreicher Prüfung die Restmenge bestellen.

## Nicht passend bestätigt

### 11. Passiver 5-V-Summer

BerryBase bietet unter anderem das
[KY-006 Passive-Buzzer-Modul](https://www.berrybase.de/ky-006-passives-buzzer-modul)
und einen Grove-Buzzer an. Diese Module entsprechen mechanisch und elektrisch
nicht automatisch dem **unmodulierten, zweipoligen passiven Summer** im
Kursdiagramm.

- **Benötigte Menge:** 40
- **Empfehlung:** Im B2B-Angebot ausdrücklich nach einem zweipoligen passiven
  5-V-Summer ohne eigene Tonerzeugung und ohne Modulplatine fragen.
- **Vor Bestellung:** Ein Muster mit der vorhandenen
  S8050-Treiberschaltung und `05_passive_buzzer.py` testen.
- **Keine stillschweigende Modulsubstitution:** Bei einem KY-006- oder
  Grove-Modul müssten Schaltplan, Anschlussliste und möglicherweise die
  Treiberschaltung geändert werden.

### 12. NPN-Transistor: geplante Umstellung auf BC337-25

BerryBase führt weder den S8050 noch einen belastbar dokumentierten BC337-25
als Einzelartikel. Für die nächste Fassung des Workshops ist deshalb eine
Umstellung auf den bei Conrad verfügbaren
[Diotec BC337-25](https://www.conrad.de/de/p/diotec-transistor-bjt-diskret-bc337-25-to-92-anzahl-kanaele-1-npn-155900.html)
vorgesehen.

- **Zielmenge:** 50
- **Beschaffung:** separat bei Conrad
- **Wichtig:** Der derzeitige S8050 wird im Kurs bei Blick auf die flache Seite
  als E–B–C gezeigt; der vorgesehene BC337-25 hat typischerweise C–B–E.
- **Noch nicht für den Unterricht bestellen:** Vor der Großbestellung werden
  alle Summer-Schaltpläne, PNGs, Anschlusslisten und Sicherheitstexte auf den
  BC337-25 umgestellt und mit dem Datenblatt des tatsächlich gelieferten
  Herstellers geprüft.

## Warum das Elektronik-Projekt-Kit nicht genügt

Das günstige
[Elektronik-Projekt-Kit `RPI-PKIT1`](https://www.berrybase.de/elektronik-projekt-kit-mit-breadboard-jumperkabeln-leds-tastern-buzzer-widerstaenden-tasche)
ist für allgemeine Einstiegsversuche attraktiv, ersetzt die obige Liste aber
nicht:

- es enthält ein kleineres 400-Kontakt-Breadboard;
- die enthaltenen Widerstände haben 330 Ω statt der im Kurs verwendeten
  220 Ω, 1 kΩ, 2 kΩ und 10 kΩ;
- der enthaltene Summer ist aktiv und kann nicht die programmierten Tonhöhen
  des Workshops erzeugen;
- Potentiometer, HC-SR04, 8er-NeoPixel-Stick und S8050 fehlen.

Das Kit wäre daher nur eine zusätzliche Materialsammlung und kein vollständiger
Klassensatz für diesen Workshop.

## Empfohlene Bestellreihenfolge

1. Je ein Muster von Breadboard, Taster, Potentiometer, Summer und
   NeoPixel-Stick bestellen.
2. Mit den Kurs-Schaltplänen alle Teile mechanisch und elektrisch prüfen.
3. USB-Anschlüsse der Schulgeräte zählen.
4. Bei BerryBase B2B ein Mengenangebot für 38 Sets und die genannten
   Reserve-Stückzahlen anfragen.
5. Nach der geplanten Schaltplanänderung BC337-25 und gegebenenfalls den
   passiven Summer separat beschaffen.
6. Nach Lieferung 38 nummerierte Sets zusammenstellen; Sets 36–38 als Reserve
   zurückhalten.
