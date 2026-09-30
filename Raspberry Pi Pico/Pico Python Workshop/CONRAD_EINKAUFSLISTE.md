# Conrad-Einkaufsliste für den Pico-Python-Workshop

**Stand:** 30. September 2026  
**Kursgröße:** ca. 70 Schülerinnen und Schüler  
**Organisation:** 35 Zweierteams + 3 vollständige Reserve-Sets = **38 Sets**

Diese Liste ist aus den tatsächlich verwendeten Schaltungen des aktuellen
Fünf-Tage-Workshops abgeleitet. Maßgeblich sind
[`workshop/en/WIRING_AND_SAFETY.md`](workshop/en/WIRING_AND_SAFETY.md) und die
zugehörigen Schaltpläne.

Preise und Lagerbestände bei Conrad ändern sich. Vor einer Bestellung über 38
Stück sollte Conrad ein Schul- oder Mengenangebot erstellen. Bei mechanisch
kritischen Bauteilen ist zunächst ein Muster zu bestellen.

## Kurzfassung

| Teil | Bedarf | Bestellvorschlag | Status |
|---|---:|---:|---|
| Raspberry Pi Pico 2 H | 38 | 38 | direkt passend |
| Breadboard, 830 Kontakte | 38 | 38 | direkt passend |
| Jumperkabel Stecker–Stecker, 40er-Band | 38 Bänder | 38 | direkt passend |
| rote 5-mm-LED | 38 + Reserve | 100 | direkt passend |
| 6×6-mm-Taster, 4 Pins | 38 + Reserve | 50 | Muster prüfen |
| lineares 10-kΩ-Potentiometer | 38 + Reserve | 40 | Muster prüfen |
| passiver 5-V-Summer | 38 + Reserve | 40 | direkt passend |
| HC-SR04-kompatibler Ultraschallsensor | 38 + Reserve | 40 | direkt passend |
| 220-Ω-Widerstand | 38 + Reserve | 100 | direkt passend |
| 1-kΩ-Widerstand | 76 + Reserve | 100 | direkt passend |
| 2-kΩ-Widerstand | 38 + Reserve | 100 | direkt passend |
| 10-kΩ-Widerstand | 38 + Reserve | 100 | direkt passend |
| USB-Datenkabel | 38 | 38 | Anschluss der Schulgeräte prüfen |
| BC337-25-NPN-Transistor | 38 + Reserve | 50 | für geplante Kursumstellung |
| 8×WS2812-RGB-Modul | 38 + Reserve | 40 | nicht passend bei Conrad gefunden |

Der höhere Bedarf bei **1 kΩ** ist beabsichtigt: Jedes vollständige Set braucht
einen 1-kΩ-Widerstand für den Summer-Treiber und einen zweiten für den
HC-SR04-Echo-Spannungsteiler.

## Direkt bei Conrad bestellbare Teile

### 1. Raspberry Pi Pico 2 H

- **Menge:** 38
- **Conrad:** [Raspberry Pi Pico 2 H, Bestell-Nr. 3415095](https://www.conrad.de/de/p/raspberry-pi-pico-2-h-mikrocontroller-pico-2-h-3415095.html)
- **Warum diese Variante:** Die Stiftleisten sind bereits verlötet. Im
  Unterricht ist kein Löten nötig.
- **Wichtig:** Der Pico 2 H verwendet Micro-USB.

### 2. Breadboard

- **Menge:** 38
- **Conrad:** [TRU COMPONENTS Steckplatine, 830 Kontakte, Bestell-Nr. 2885953](https://www.conrad.de/de/p/tru-components-steckplatine-selbstklebend-polzahl-gesamt-830-l-x-b-16-51-cm-x-5-46-cm-1-st-2885953.html)
- **Alternative:** [Joy-it Breadboard, 830 Kontakte, Bestell-Nr. 2253827](https://www.conrad.de/de/p/joy-it-breadboard-830-steckplatine-polzahl-gesamt-830-l-x-b-16-5-cm-x-5-5-cm-1-st-2253827.html)
- **Warum 830 Kontakte:** Es bietet genug Platz für Pico, Sensor,
  Spannungsteiler, Summer-Treiber und RGB-Modul im Abschlussprojekt. Ein
  400-Kontakt-Board ist für die kombinierten Aufbauten unnötig eng.

### 3. Jumperkabel

- **Menge:** 38 Bänder mit je 40 Kabeln
- **Conrad:** [Renkforce JKMM403, 40× Stecker–Stecker, 30 cm, Bestell-Nr. 2299846](https://www.conrad.de/de/p/renkforce-jkmm403-jumper-kabel-arduino-banana-pi-raspberry-pi-40x-drahtbruecken-stecker-40x-drahtbruecken-stecker-3-2299846.html)
- **Hinweis:** Die Kabel lassen sich einzeln vom Flachband trennen. Für die
  Schaltungen auf dem Breadboard werden überwiegend Stecker–Stecker-Kabel
  benötigt.

### 4. Rote 5-mm-LEDs

- **Menge:** 100
- **Conrad:** [TRU COMPONENTS, 5 mm, rot, Bestell-Nr. 2377620](https://www.conrad.de/de/p/tru-components-led-bedrahtet-5-mm-rot-rund-5-mm-100-mcd-60-20-ma-2377620.html)
- **Hinweis:** Pro Set wird eine LED verwendet. Die größere Menge schafft
  Reserve für verbogene oder gekürzte Beine.
- **Sicherheitsregel:** Jede LED wird nur mit dem 220-Ω-Vorwiderstand aus
  Abschnitt 9 betrieben.

### 5. Passiver Summer

- **Menge:** 40
- **Conrad:** [TRU COMPONENTS TC-9202060, passiver 5-V-Piezo-Signalgeber, Bestell-Nr. 2300515](https://www.conrad.de/de/p/tru-components-tc-9202060-piezo-signalgeber-geraeusch-entwicklung-85-db-spannung-5-v-dc-dauerton-1-st-2300515.html)
- **Nicht verwechseln:** Es muss ein **passiver** Summer ohne eingebaute
  Tonerzeugung sein. Nur damit kann das Programm unterschiedliche Tonhöhen
  erzeugen.
- **Schaltung:** Der Summer wird über den S8050-Treiber geschaltet und niemals
  direkt an einem GPIO betrieben.

### 6. Ultraschallsensor

- **Menge:** 40
- **Conrad:** [Iduino ST1099 / HC-SR04, Bestell-Nr. 1616245](https://www.conrad.de/de/p/iduino-st1099-ultraschallsensor-1-st-1616245.html)
- **Schaltung:** Betrieb mit 5 V. Echo darf nur über den vorgeschriebenen
  1-kΩ/2-kΩ-Spannungsteiler an GP18 gelangen.

### 7. Widerstände

Alle Widerstände sind axial bedrahtete THT-Bauteile. 0,25 W oder mehr ist für
die Kursschaltungen ausreichend.

| Wert | Verwendung | Menge | Conrad |
|---:|---|---:|---|
| 220 Ω | Vorwiderstand der gewöhnlichen LED | 100 | [TRU COMPONENTS, 100 Stück, Bestell-Nr. 1584857](https://www.conrad.de/de/p/tru-components-1584857-tc-cfr0w4j0221kit203-kohleschicht-widerstand-220-axial-bedrahtet-0207-0-25-w-5-100-st-bag-1584857.html) |
| 1 kΩ | Transistor-Basis und oberer HC-SR04-Teilerwiderstand | 100 | [TRU COMPONENTS, Bestell-Nr. 1583972; 100 Stück bestellen](https://www.conrad.de/de/p/tru-components-1583972-tc-mf0w4ff1001a50203-metallschicht-widerstand-1-k-axial-bedrahtet-0207-0-25-w-1-1-st-1583972.html) |
| 2 kΩ | unterer HC-SR04-Teilerwiderstand | 100 | [Yageo MF0207F2KH, Bestell-Nr. 1417622; 100 Stück bestellen](https://www.conrad.de/de/p/yageo-mf0207f2kh-mf0207fte52-2k-metallschicht-widerstand-2-k-axial-bedrahtet-0207-0-6-w-1-1-st-1417622.html) |
| 10 kΩ | Pull-up des Tasters | 100 | [TRU COMPONENTS, 100 Stück, Bestell-Nr. 1583903](https://www.conrad.de/de/p/tru-components-1583903-tc-mf0w4ff1002kit203-metallschicht-widerstand-10-k-axial-bedrahtet-0207-0-25-w-1-100-st-1583903.html) |

**Nicht 2,2 kΩ statt 2 kΩ bestellen.** Die Kursunterlagen und die Berechnung
des Echo-Spannungsteilers verwenden ausdrücklich 1 kΩ und 2 kΩ.

### 8. USB-Datenkabel

Zuerst die Anschlüsse der Schulgeräte prüfen. Jedes Kabel muss
**Datenübertragung** unterstützen; reine Ladekabel funktionieren mit Thonny
nicht.

| Computeranschluss | Menge | Conrad |
|---|---:|---|
| USB-A | 38 | [Raspberry Pi SC0557, USB-A auf Micro-B, 1 m, Bestell-Nr. 3366525](https://www.conrad.de/de/p/raspberry-pi-sc0557-daten-strom-kabel-raspberry-pi-1x-usb-2-0-stecker-a-1x-usb-2-0-stecker-micro-b-1-00-m-rot-3366525.html) |
| USB-C | 38 | [LogiLink CU0242, USB-C auf Micro-B, 1 m, Bestell-Nr. 3770869](https://www.conrad.de/de/p/logilink-usb-c-kabel-usb-2-0-usb-c-stecker-usb-micro-b-stecker-1-0-m-weiss-cu0242-3770869.html) |

Nur eine der beiden Varianten bestellen oder die 38 Kabel passend zum
tatsächlichen Gerätebestand aufteilen.

## Vor der Großbestellung als Muster prüfen

### 9. Taster

- **Zielmenge:** 50
- **Kandidat:** [Weltron T602, 6×6 mm, 4 Pins, Bestell-Nr. 701274](https://www.conrad.de/de/p/weltron-t602-t602-drucktaster-24-v-dc-0-05-a-1-x-aus-ein-tastend-l-x-b-x-h-6-x-6-x-5-0-mm-1-st-701274.html)
- **Musterprüfung:** Ein Exemplar muss mechanisch über den Mittelkanal des
  ausgewählten Breadboards passen. Mit einem Multimeter prüfen, welche beiden
  Pins intern dauerhaft verbunden sind.

Erst nach erfolgreicher Prüfung die Restmenge bestellen.

### 10. Potentiometer

- **Zielmenge:** 40
- **Kandidat:** [Bourns 3310C-001-103L, 10 kΩ linear, Bestell-Nr. 2996246](https://www.conrad.de/de/p/bourns-3310c-001-103l-leitplastik-potentiometer-0-25-w-10-k-1-st-piece-2996246.html)
- **Musterprüfung:** Pinabstand, Breadboard-Halt und Drehrichtung prüfen. Die
  drei Anschlüsse müssen als `3V3`, `WIPER` und `GND` eindeutig identifizierbar
  sein.

Dieses Bauteil ist deutlich teurer als übliche Maker-Potentiometer. Vor einer
Bestellung von 40 Stück sollte Conrad nach einem günstigeren, breadboardfähigen
10-kΩ-Linear-Potentiometer gefragt werden.

## Nicht passend bei Conrad gefunden

### 11. NPN-Transistor: geplante Umstellung auf BC337-25

- **Zielmenge:** 50
- **Conrad:** [Diotec BC337-25, TO-92, Bestell-Nr. 155900](https://www.conrad.de/de/p/diotec-transistor-bjt-diskret-bc337-25-to-92-anzahl-kanaele-1-npn-155900.html)
- **Verwendung:** Schalter für den passiven 5-V-Summer

Der BC337-25 kann die Schaltfunktion übernehmen und ist bei Conrad erhältlich.
Er ist jedoch **kein mechanisch identischer Ersatz** für den S8050. Bei
typischen TO-92-Ausführungen ist die Anschlussreihenfolge bei Blick auf die
flache Seite:

| Transistor | Anschlussfolge bei Blick auf die flache Seite |
|---|---|
| derzeitiger S8050 im Kurs | E–B–C |
| vorgesehener BC337-25 | C–B–E |

**Noch nicht für den Unterricht bestellen:** Die veröffentlichten
Kurs-Schaltpläne zeigen weiterhin den S8050. Vor der Großbestellung werden
Summer-Schaltpläne, PNGs, Anschlusslisten und Sicherheitstexte gemeinsam auf
den BC337-25 umgestellt und mit dem Datenblatt des tatsächlich gelieferten
Herstellers geprüft.

### 12. 8×WS2812-RGB-Modul

Der Kurs verwendet ein lineares Modul mit acht einzeln adressierbaren WS2812
und einem klar markierten Eingang `IN S/V/G`. Bei Conrad wurde kein
entsprechendes 8er-Modul gefunden.

- **Benötigte Menge:** 40
- **Empfehlung:** Das bestehende
  [8er-NeoPixel-Modul bei BerryBase](https://www.berrybase.de/neopixel-stick-mit-8-ws2812-5050-rgb-leds)
  oder das zum Freenove-Kit gehörende Modul verwenden.
- **Keinen beliebigen LED-Streifen bestellen:** Eine andere Bauform oder
  Anschlussbelegung erfordert neue Schaltpläne und möglicherweise eine
  geänderte Stromversorgung.

## Optional: Aufbewahrung

Für langfristig nummerierte Klassensätze kann pro Team eine flache
Kleinteilebox verwendet werden:

- [TRU COMPONENTS PP15-01, 15 Fächer, Bestell-Nr. 1570099](https://www.conrad.de/de/p/tru-components-pp15-01-sortimentskasten-l-x-b-x-h-200-x-175-x-26-mm-anzahl-faecher-15-feste-unterteilung-inhalt-1-st-1570099.html)

Vor einer Bestellung von 38 Boxen ein Muster bestellen und prüfen, ob
Breadboard, Pico, Kabel und Module gemeinsam hineinpassen.

## Empfohlene Bestellreihenfolge

1. Je ein Muster von Breadboard, Taster, Potentiometer, Summer und Box
   bestellen.
2. Mit den Kurs-Schaltplänen alle Bauteile mechanisch und elektrisch prüfen.
3. USB-Anschlüsse der Schulgeräte zählen.
4. Bei Conrad ein Mengenangebot für die bestätigten Stückzahlen anfragen.
5. Nach der geplanten Schaltplanänderung BC337-25 bei Conrad und
   8er-WS2812-Module separat bei BerryBase beschaffen.
6. Nach Lieferung 38 nummerierte Sets zusammenstellen; Sets 36–38 als Reserve
   zurückhalten.
