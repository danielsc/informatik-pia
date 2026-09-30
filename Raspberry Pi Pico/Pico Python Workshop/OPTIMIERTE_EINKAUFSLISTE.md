# Optimierte Einkaufsliste für 40 Pico-Workshop-Kits

**Stand:** 30. September 2026  
**Umfang:** 40 vollständige Zweierteam-Kits  
**Preisangaben:** brutto, ohne noch zu bestätigende Versandkosten und
Mengenrabatte

Diese Liste bündelt die passenden Teile bei möglichst wenigen Versendern:

- **BerryBase** liefert die günstigen, workshop-spezifischen Module.
- **Reichelt** liefert Pico, Breadboards, Standardbauteile und USB-Kabel.
- **Conrad** wird in der aktuellen Preisrechnung nicht benötigt, bleibt aber
  als Ausweichlieferant dokumentiert.

Die Preise sind Momentaufnahmen aus den verlinkten Shops. Vor der Bestellung
sollte für 40 Kits jeweils ein schriftliches Schul- oder Mengenangebot
eingeholt werden.

## Gesamtkosten

| Reichelt | BerryBase | Warenwert gesamt | Pro Kit |
|---:|---:|---:|---:|
| 480,95 € | 283,20 € | **764,15 €** | **19,10 €** |

Versandkosten sind nicht eingerechnet. Bei BerryBase liegt der Warenwert über
der üblichen Schwelle für kostenlosen Versand; dies muss im B2B-Angebot
bestätigt werden. Bei Reichelt Versandkosten oder kostenlose Lieferung im
Angebot gesondert ausweisen lassen.

Die 40 USB-A-auf-Micro-B-Datenkabel sind in der Bestellkalkulation enthalten.

## Bestellung 1: Reichelt

| Pos. | Artikel | Bestellmenge | Einzel-/Packpreis | Summe |
|---:|---|---:|---:|---:|
| 1 | [Raspberry Pi Pico 2 H mit verlöteten Headern](https://www.reichelt.de/de/de/shop/produkt/raspberry_pi_pico_2_h_rp235x_cortex-m33_microusb-398577) | 40 | 5,90 € | 236,00 € |
| 2 | [Experimentier-Steckboard, 830 Kontakte](https://www.reichelt.de/de/de/shop/produkt/experimentier-steckboard_830_kontakte-282600) | 40 | 3,85 € | 154,00 € |
| 3 | [Rote 5-mm-LEDs, 100 Stück](https://www.reichelt.de/de/de/shop/produkt/led_5_mm_-_farbe_rot_100_stueck-280134) | 1 Pack | 5,55 € | 5,55 € |
| 4 | [Kurzhubtaster 6×6 mm, vier Pins](https://www.reichelt.de/de/de/shop/produkt/kurzhubtaster_6x6mm_hoehe_4_3mm_12v_vertikal-27892) | 50 | 0,20 € | 10,00 € |
| 5 | [BC337-25, NPN, TO-92](https://www.reichelt.de/de/de/shop/produkt/bipolartransistor_npn_45v_0_8a_0_625w_to-92-4986) | 50 | 0,06 € | 3,00 € |
| 6 | [Passiver Piezo-Signalgeber ohne Oszillator, 5 Vpp](https://www.reichelt.de/de/de/shop/produkt/piezo-signalgeber_piezoelektrisch_85_4000_hz_5_0_vpp_14_mm-428983) | 40 | 0,31 € | 12,40 € |
| 7 | [220-Ω-Widerstand, 0,25 W](https://www.reichelt.de/de/de/shop/produkt/widerstand_kohleschicht_220_ohm_0207_250_mw_5_-1382) | 100 | ca. 0,021 € | 2,10 € |
| 8 | [1-kΩ-Widerstand, 0,25 W](https://www.reichelt.de/de/de/shop/produkt/widerstand_kohleschicht_1_0_kohm_0207_250_mw_5_-1315) | 100 | ca. 0,021 € | 2,10 € |
| 9 | [2-kΩ-Widerstand, 0,25 W](https://www.reichelt.de/de/de/shop/produkt/widerstand_kohleschicht_2_0_kohm_0207_250_mw_5_-1366) | 100 | ca. 0,021 € | 2,10 € |
| 10 | [10-kΩ-Widerstand, 0,25 W](https://www.reichelt.de/de/de/shop/produkt/widerstand_kohleschicht_10_kohm_0207_250_mw_5_-1338) | 100 | ca. 0,021 € | 2,10 € |
| 11 | [USB-A auf Micro-B, 1 m, Datenkabel](https://www.reichelt.de/de/de/shop/produkt/sync-_ladekabel_usb-a_-_micro-b_nylon_schwarz_grau_1_0_m-315218) | 40 | 1,29 € | 51,60 € |
|  | **Zwischensumme Reichelt** |  |  | **480,95 €** |

Reine Ladekabel sind ungeeignet, weil Thonny eine Datenverbindung zum Pico
benötigt.

Der zweite 1-kΩ-Widerstand pro Kit ist beabsichtigt: Einer gehört an die Basis
des Summer-Transistors, einer in den HC-SR04-Echo-Spannungsteiler.

## Bestellung 2: BerryBase

| Pos. | Artikel | Bestellmenge | Einzelpreis | Summe |
|---:|---|---:|---:|---:|
| 1 | [40-poliges Jumperkabel-Band Male–Male, trennbar, 20 cm](https://www.berrybase.de/40pin-jumper-dupont-kabel-male-male-trennbar/laenge-0-20-m) | 40 | 1,80 € | 72,00 € |
| 2 | [Breadboard-Potentiometer, 10 kΩ linear](https://www.berrybase.de/breadboard-potentiometer-10k-ohm) | 40 | 1,19 € | 47,60 € |
| 3 | [HC-SR04-Ultraschallsensor](https://www.berrybase.de/hc-sr04-ultraschall-sensor) | 40 | 1,49 € | 59,60 € |
| 4 | [NeoPixel-Stick mit 8 WS2812-LEDs, SKU NEOPS8](https://www.berrybase.de/neopixel-stick-mit-8-ws2812-5050-rgb-leds) | 40 | 2,60 € | 104,00 € |
|  | **Zwischensumme BerryBase** |  |  | **283,20 €** |

Der BerryBase-Pico kostet derzeit 6,50 € und ist deshalb nicht eingeplant; der
Pico 2 H bei Reichelt spart bei 40 Stück 24,00 €. Das günstige
[BerryBase-Breadboard](https://www.berrybase.de/breadboard-mit-830-kontakten)
für 1,90 € war bei der Prüfung ausverkauft. Falls es vor der Bestellung wieder
in ausreichender Menge verfügbar ist, sinkt die Gesamtsumme durch einen Wechsel
von Reichelt zu BerryBase um **78,00 €**.

## Bestellung 3: Conrad nur als Ausweichoption

Conrad ist für die optimierte Bestellung derzeit nicht erforderlich. Folgende
Artikel bleiben sinnvolle Ersatzquellen:

| Artikel | Conrad-Link | Einsatz |
|---|---|---|
| Pico 2 H | [Bestell-Nr. 3415095](https://www.conrad.de/de/p/raspberry-pi-pico-2-h-mikrocontroller-pico-2-h-3415095.html) | falls Reichelt nicht 40 Stück liefern kann |
| passiver 5-V-Piezo-Signalgeber | [Bestell-Nr. 2300515](https://www.conrad.de/de/p/tru-components-tc-9202060-piezo-signalgeber-geraeusch-entwicklung-85-db-spannung-5-v-dc-dauerton-1-st-2300515.html) | nur nach erfolgreichem Mustertest |
| BC337-25 | [Bestell-Nr. 155900](https://www.conrad.de/de/p/diotec-transistor-bjt-diskret-bc337-25-to-92-anzahl-kanaele-1-npn-155900.html) | falls Reichelt nicht liefern kann |

Eine zusätzliche Conrad-Bestellung lohnt sich nur bei Lieferproblemen oder
einem besseren Mengenangebot, weil sonst ein dritter Versandvorgang entsteht.

## Freigaben vor der Großbestellung

1. Je ein Muster von Breadboard, Taster, Potentiometer, Piezo-Signalgeber und
   NeoPixel-Stick bestellen.
2. Prüfen, ob der Taster über den Mittelkanal passt und welche Pins intern
   verbunden sind.
3. Den passiven Piezo-Signalgeber mit
   `code/teacher-tests/05_passive_buzzer.py` und der Transistorschaltung testen.
4. Die Pinreihenfolge des tatsächlich gelieferten BC337-25 im Hersteller-
   Datenblatt prüfen.
5. Vor Einsatz des BC337-25 die noch auf S8050 ausgelegten Summer-Schaltpläne,
   PNGs, Anschlusslisten sowie englischen und deutschen Texte ändern.
6. Am HC-SR04 weiterhin zwingend den dokumentierten
   1-kΩ/2-kΩ-Echo-Spannungsteiler verwenden; nicht 2,2 kΩ liefern lassen.
7. Bei Position 11 kontrollieren, dass tatsächlich Datenkabel und keine reinen
   Ladekabel geliefert werden.

## Anfrage für das Mengenangebot

Beiden Versendern sollte dieselbe kurze Anfrage geschickt werden:

> Bitte bestätigen Sie für die aufgeführten Artikel den Bruttopreis, die
> sofort lieferbare Menge, die Versandkosten, einen möglichen Schul- oder
> Mengenrabatt sowie eine Lieferung auf Rechnung. Mechanisch oder elektrisch
> abweichende Ersatzartikel bitte nicht ohne vorherige Freigabe einsetzen.
