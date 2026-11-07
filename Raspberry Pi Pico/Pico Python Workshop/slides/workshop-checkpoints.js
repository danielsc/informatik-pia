const checkpointText = (en, de) => ({ en, de });

const workshopQuizDays = [
  {
    password: "COMET",
    questions: [
      {
        prompt: checkpointText("What appears in the Shell?", "Was erscheint in der Shell?"),
        code: 'message = "Team Comet"\nprint(message)',
        answers: [
          checkpointText("message", "message"),
          checkpointText("Team Comet", "Team Comet"),
          checkpointText("Nothing: a variable cannot be printed.", "Nichts: Eine Variable kann nicht ausgegeben werden."),
          checkpointText("The LED turns on instead.", "Stattdessen geht die LED an.")
        ],
        correct: 1,
        hint: checkpointText("Without quotation marks, Python uses the value of the variable.", "Ohne Anführungszeichen verwendet Python den Wert der Variable.")
      },
      {
        prompt: checkpointText("Three flashes use sleep(on_time). You change only on_time from 0.15 to 1.5. What changes?", "Drei Lichtsignale nutzen sleep(on_time). Ihr ändert nur on_time von 0.15 auf 1.5. Was ändert sich?"),
        answers: [
          checkpointText("Only the first flash lasts longer.", "Nur das erste Lichtsignal dauert länger."),
          checkpointText("The OFF pauses also become 1.5 seconds.", "Die AUS-Pausen dauern ebenfalls 1.5 Sekunden."),
          checkpointText("All three ON pauses become 1.5 seconds; off_time stays unchanged.", "Alle drei EIN-Pausen dauern 1.5 Sekunden; off_time bleibt unverändert."),
          checkpointText("Nothing until all three sleep calls are edited.", "Nichts, solange nicht alle drei sleep-Aufrufe geändert werden.")
        ],
        correct: 2,
        hint: checkpointText("Each sleep(on_time) reads the same variable. The OFF pauses use a different variable.", "Jeder Aufruf von sleep(on_time) liest dieselbe Variable. Die AUS-Pausen verwenden eine andere Variable.")
      },
      {
        prompt: checkpointText("What does Python do with the line beginning with #?", "Was macht Python mit der Zeile, die mit # beginnt?"),
        code: "# A short flash starts our signal\nled.on()",
        answers: [
          checkpointText("It prints that line in the Shell.", "Es gibt diese Zeile in der Shell aus."),
          checkpointText("It ignores the whole program.", "Es ignoriert das ganze Programm."),
          checkpointText("It treats # as a variable name.", "Es verwendet # als Variablennamen."),
          checkpointText("It ignores the comment, then runs led.on().", "Es ignoriert den Kommentar und führt danach led.on() aus.")
        ],
        correct: 3,
        hint: checkpointText("A comment ends at the end of its line. It is not a print instruction.", "Ein Kommentar endet am Zeilenende. Er ist keine print-Anweisung.")
      },
      {
        prompt: checkpointText("How do you safely move the blinking signal to the external LED on GP15?", "Wie übertragt ihr das Blinksignal sicher auf die externe LED an GP15?"),
        answers: [
          checkpointText('Unplug USB, check the LED circuit with its 220 Ω resistor, and use Pin(15, Pin.OUT) in a copy.', 'USB trennen, die LED-Schaltung mit 220-Ω-Widerstand prüfen und in einer Kopie Pin(15, Pin.OUT) verwenden.'),
          checkpointText('Leave Pin("LED", Pin.OUT) unchanged; it also controls GP15.', 'Pin("LED", Pin.OUT) unverändert lassen; damit wird auch GP15 gesteuert.'),
          checkpointText("Change only the printed team name.", "Nur den ausgegebenen Teamnamen ändern."),
          checkpointText("Rewire while the program runs so the result is visible immediately.", "Bei laufendem Programm umstecken, damit das Ergebnis sofort sichtbar ist.")
        ],
        correct: 0,
        hint: checkpointText("The onboard LED and GP15 are different outputs. Change wiring only while unplugged, and keep the protection resistor.", "Die eingebaute LED und GP15 sind verschiedene Ausgänge. Nur ohne USB umstecken und den Schutzwiderstand beibehalten.")
      },
      {
        prompt: checkpointText("You are about to run 01_hello_pico.py on the Pico. Which Thonny setup is correct?", "Ihr wollt 01_hello_pico.py auf dem Pico ausführen. Welche Thonny-Einstellung passt?"),
        answers: [
          checkpointText("Local Python 3; no USB connection is needed.", "Lokales Python 3; USB ist nicht nötig."),
          checkpointText("MicroPython (Raspberry Pi Pico), Pico connected by USB, automatic port detection.", "MicroPython (Raspberry Pi Pico), Pico per USB verbunden, automatische Port-Erkennung."),
          checkpointText("Any interpreter, as long as the file is in Downloads.", "Ein beliebiger Interpreter, solange die Datei in Downloads liegt."),
          checkpointText("Only the Shell can run programs on the Pico.", "Nur die Shell kann Programme auf dem Pico ausführen.")
        ],
        correct: 1,
        hint: checkpointText("The desktop interpreter runs on the computer. Hardware programs need the Pico interpreter and a connection.", "Der lokale Interpreter läuft auf dem Computer. Hardwareprogramme brauchen den Pico-Interpreter und eine Verbindung.")
      }
    ]
  },
  {
    password: "BUTTON",
    questions: [
      {
        prompt: checkpointText("Which two answers does Python print, in order?", "Welche beiden Antworten gibt Python nacheinander aus?"),
        code: "score = 350\nprint(score < 350)\nprint(score == 350)",
        answers: [
          checkpointText("True, then True", "True, dann True"),
          checkpointText("True, then False", "True, dann False"),
          checkpointText("False, then True", "False, dann True"),
          checkpointText("False, then False", "False, dann False")
        ],
        correct: 2,
        hint: checkpointText("< means strictly smaller. == asks whether the values are equal.", "< bedeutet echt kleiner. == fragt, ob die Werte gleich sind.")
      },
      {
        prompt: checkpointText("The active-high button is released. What are button.value() and not button.value()?", "Der Active-high-Taster ist losgelassen. Was ergeben button.value() und not button.value()?"),
        answers: [
          checkpointText("0 and True", "0 und True"),
          checkpointText("1 and False", "1 und False"),
          checkpointText("0 and False", "0 und False"),
          checkpointText("1 and True", "1 und True")
        ],
        correct: 0,
        hint: checkpointText("The pull-down makes a released button read 0. not reverses its truth value.", "Der Pull-down sorgt beim losgelassenen Taster für 0. not kehrt den Wahrheitswert um.")
      },
      {
        prompt: checkpointText("Which word is printed at exactly 70 percent?", "Welches Wort wird bei genau 70 Prozent ausgegeben?"),
        code: 'percent = 70\nif percent < 20:\n    print("off")\nelif percent <= 70:\n    print("dim")\nelse:\n    print("bright")',
        answers: [
          checkpointText("off", "off"),
          checkpointText("bright", "bright"),
          checkpointText("Both dim and bright", "Sowohl dim als auch bright"),
          checkpointText("dim", "dim")
        ],
        correct: 3,
        hint: checkpointText("<= includes the boundary. Python runs only the first matching branch.", "<= schließt den Grenzwert ein. Python führt nur den ersten passenden Zweig aus.")
      },
      {
        prompt: checkpointText("How many scores are there, and which is the fastest?", "Wie viele Ergebnisse sind gespeichert und welches ist das schnellste?"),
        code: "scores = [410, 375]\nscores.append(390)",
        answers: [
          checkpointText("Two scores; 375 ms", "Zwei Ergebnisse; 375 ms"),
          checkpointText("Three scores; 375 ms", "Drei Ergebnisse; 375 ms"),
          checkpointText("Three scores; 410 ms", "Drei Ergebnisse; 410 ms"),
          checkpointText("One score; 390 ms", "Ein Ergebnis; 390 ms")
        ],
        correct: 1,
        hint: checkpointText("append adds an item; it does not replace the list. A shorter reaction time is faster.", "append fügt einen Eintrag hinzu und ersetzt nicht die Liste. Eine kürzere Reaktionszeit ist schneller.")
      },
      {
        prompt: checkpointText("When does this waiting loop end?", "Wann endet diese Warteschleife?"),
        code: "while not button.value():\n    sleep_ms(1)",
        answers: [
          checkpointText("After exactly one millisecond, whatever the button does.", "Nach genau einer Millisekunde, unabhängig vom Taster."),
          checkpointText("When the active-high button is released.", "Wenn der Active-high-Taster losgelassen wird."),
          checkpointText("When the active-high button is pressed.", "Wenn der Active-high-Taster gedrückt wird."),
          checkpointText("It cannot end because it is a while loop.", "Sie kann nicht enden, weil es eine while-Schleife ist.")
        ],
        correct: 2,
        hint: checkpointText("while repeats only while its condition is true. Consider not 0 and not 1.", "while wiederholt nur, solange die Bedingung wahr ist. Überlegt, was not 0 und not 1 ergeben.")
      }
    ]
  },
  {
    password: "PIXEL",
    questions: [
      {
        prompt: checkpointText("Which line lets another function use the energy value to make a decision?", "Welche Zeile ermöglicht einer anderen Funktion, den Energiewert für eine Entscheidung zu nutzen?"),
        answers: [
          checkpointText("print(energy), because displayed text is automatically passed on.", "print(energy), weil angezeigter Text automatisch weitergegeben wird."),
          checkpointText("return energy, because it gives the value back to the calling code.", "return energy, weil der Wert an den aufrufenden Code zurückgegeben wird."),
          checkpointText("# energy, because comments store results.", "# energy, weil Kommentare Ergebnisse speichern."),
          checkpointText("sleep(energy), because waiting returns the value.", "sleep(energy), weil Warten den Wert zurückgibt.")
        ],
        correct: 1,
        hint: checkpointText("Showing a value is different from giving it back for the next calculation or decision.", "Einen Wert anzuzeigen ist etwas anderes, als ihn für die nächste Berechnung oder Entscheidung zurückzugeben.")
      },
      {
        prompt: checkpointText("What value is stored in answer?", "Welcher Wert wird in answer gespeichert?"),
        code: "def doubled(number):\n    return number * 2\n\nanswer = doubled(4)",
        answers: [
          checkpointText("8", "8"),
          checkpointText("4", "4"),
          checkpointText("2", "2"),
          checkpointText("The text number", "Der Text number")
        ],
        correct: 0,
        hint: checkpointText("The argument 4 becomes the parameter number inside this call.", "Das Argument 4 wird in diesem Aufruf zum Wert des Parameters number.")
      },
      {
        prompt: checkpointText("What colour does this RGB tuple describe?", "Welche Farbe beschreibt dieses RGB-Tupel?"),
        code: "colour = (0, 30, 0)",
        answers: [
          checkpointText("Red", "Rot"),
          checkpointText("Blue", "Blau"),
          checkpointText("All pixels off", "Alle Pixel aus"),
          checkpointText("Green", "Grün")
        ],
        correct: 3,
        hint: checkpointText("The order is red, green, blue. Look at which position has a nonzero value.", "Die Reihenfolge lautet Rot, Grün, Blau. Welche Position hat einen Wert ungleich null?")
      },
      {
        prompt: checkpointText("Which indexes does range(8) visit on the eight-pixel module?", "Welche Indizes besucht range(8) beim Modul mit acht Pixeln?"),
        answers: [
          checkpointText("1 through 8", "1 bis 8"),
          checkpointText("0 through 8", "0 bis 8"),
          checkpointText("0 through 7", "0 bis 7"),
          checkpointText("Only index 8", "Nur Index 8")
        ],
        correct: 2,
        hint: checkpointText("Counting starts at zero. The end value of range is not included.", "Die Zählung beginnt bei null. Der Endwert von range gehört nicht dazu.")
      },
      {
        prompt: checkpointText("What is printed immediately after 0 green?", "Was wird unmittelbar nach 0 green ausgegeben?"),
        code: 'for lap in range(2):\n    for colour in ["red", "green"]:\n        print(lap, colour)',
        answers: [
          checkpointText("0 red", "0 red"),
          checkpointText("1 red", "1 red"),
          checkpointText("1 green", "1 green"),
          checkpointText("Nothing: both loops are finished.", "Nichts: Beide Schleifen sind beendet.")
        ],
        correct: 1,
        hint: checkpointText("The inner loop finishes for each lap, then starts again for the next lap.", "Die innere Schleife läuft für jeden Durchgang von lap vollständig durch und beginnt danach neu.")
      }
    ]
  },
  {
    password: "ECHO",
    questions: [
      {
        prompt: checkpointText("No useful echo returns before the timeout. Why return None instead of 0?", "Bis zum Timeout kommt kein brauchbares Echo zurück. Warum wird None statt 0 zurückgegeben?"),
        answers: [
          checkpointText("0 would falsely claim that the object is at zero distance; None means no usable measurement.", "0 würde fälschlich Abstand null melden; None steht für eine fehlende brauchbare Messung."),
          checkpointText("None means the same distance as 0 cm.", "None bedeutet denselben Abstand wie 0 cm."),
          checkpointText("None automatically retries forever.", "None wiederholt die Messung automatisch endlos."),
          checkpointText("A timeout always means the object is very close.", "Ein Timeout bedeutet immer, dass das Objekt sehr nah ist.")
        ],
        correct: 0,
        hint: checkpointText("A missing measurement is not a measured distance. A timeout lets the program continue.", "Eine fehlende Messung ist kein gemessener Abstand. Ein Timeout lässt das Programm weiterlaufen.")
      },
      {
        prompt: checkpointText("Which Echo connection protects the Pico input?", "Welche Echo-Verbindung schützt den Pico-Eingang?"),
        answers: [
          checkpointText("Echo directly to GP18", "Echo direkt an GP18"),
          checkpointText("Echo to GP18 through only a wire to GND", "Echo an GP18 nur über ein Kabel zu GND"),
          checkpointText("Echo through 1 kΩ to the GP18 junction, then 2 kΩ from that junction to GND", "Echo über 1 kΩ zum GP18-Knotenpunkt, von dort 2 kΩ zu GND"),
          checkpointText("Echo to the buzzer transistor instead of GP18", "Echo statt an GP18 an den Buzzer-Transistor")
        ],
        correct: 2,
        hint: checkpointText("HC-SR04 Echo can reach about 5 V; Pico GPIO is 3.3 V only. Both divider resistors have a job.", "HC-SR04 Echo kann etwa 5 V erreichen; Pico-GPIO verträgt nur 3.3 V. Beide Widerstände des Spannungsteilers werden benötigt.")
      },
      {
        prompt: checkpointText("What value is printed?", "Welcher Wert wird ausgegeben?"),
        code: 'config = {"caution": {"pause_ms": 520}}\nconfig["caution"]["pause_ms"] = 400\nprint(config["caution"]["pause_ms"])',
        answers: [
          checkpointText("520", "520"),
          checkpointText("400", "400"),
          checkpointText("caution", "caution"),
          checkpointText("pause_ms", "pause_ms")
        ],
        correct: 1,
        hint: checkpointText("First choose the state, then its setting. Assignment replaces the old value under that key.", "Zuerst den Zustand, dann seine Einstellung wählen. Die Zuweisung ersetzt den bisherigen Wert unter diesem Schlüssel.")
      },
      {
        prompt: checkpointText("The alarm rules say: safe over 60 cm, caution over 25 through 60 cm, stop at 25 cm or less. Which state applies at exactly 25 cm?", "Die Alarmregeln lauten: safe über 60 cm, caution über 25 bis 60 cm, stop bei höchstens 25 cm. Welcher Zustand gilt bei genau 25 cm?"),
        answers: [
          checkpointText("safe", "safe"),
          checkpointText("caution", "caution"),
          checkpointText("invalid", "invalid"),
          checkpointText("stop", "stop")
        ],
        correct: 3,
        hint: checkpointText("'25 cm or less' includes exactly 25. Check the boundary, not just nearby examples.", "„Höchstens 25 cm“ schließt genau 25 ein. Prüft den Grenzwert, nicht nur benachbarte Beispiele.")
      },
      {
        prompt: checkpointText("The Day 4 proximity alarm receives None. What should happen?", "Der Näherungsalarm von Tag 4 erhält None. Was soll passieren?"),
        answers: [
          checkpointText("The stop alarm sounds continuously.", "Der Stopp-Alarm ertönt dauerhaft."),
          checkpointText("The last measured distance is always treated as current.", "Der letzte gemessene Abstand gilt immer als aktuell."),
          checkpointText("The state is invalid; the onboard LED is off and the buzzer is silent.", "Der Zustand ist invalid; die eingebaute LED ist aus und der Buzzer bleibt stumm."),
          checkpointText("The program waits forever for another echo.", "Das Programm wartet endlos auf ein weiteres Echo.")
        ],
        correct: 2,
        hint: checkpointText("Invalid input needs its own state. It must not be mistaken for an object at zero distance.", "Eine ungültige Eingabe braucht einen eigenen Zustand. Sie darf nicht mit einem Objekt bei Abstand null verwechselt werden.")
      }
    ]
  },
  {
    password: "MAKER",
    questions: [
      {
        prompt: checkpointText("Which statement is a testable requirement, rather than an implementation detail?", "Welche Aussage ist eine prüfbare Anforderung und kein Detail der Umsetzung?"),
        answers: [
          checkpointText("Use a function named show_zone.", "Eine Funktion namens show_zone verwenden."),
          checkpointText("At 100 cm, the RGB pixels are green and the buzzer is silent.", "Bei 100 cm leuchten die RGB-Pixel grün und der Buzzer bleibt stumm."),
          checkpointText("Write more lines of Python.", "Mehr Python-Zeilen schreiben."),
          checkpointText("Use a dictionary somewhere.", "Irgendwo ein Dictionary verwenden.")
        ],
        correct: 1,
        hint: checkpointText("A requirement describes an observable result for a specific situation, not the code used to produce it.", "Eine Anforderung beschreibt ein beobachtbares Ergebnis in einer bestimmten Situation, nicht den dafür verwendeten Code.")
      },
      {
        prompt: checkpointText("How should you first test classify_distance?", "Wie sollt ihr classify_distance zuerst testen?"),
        answers: [
          checkpointText("With fixed values such as 100, 40, 15, and None, before using live sensor input.", "Mit festen Werten wie 100, 40, 15 und None, bevor echte Sensormessungen verwendet werden."),
          checkpointText("Only by running the complete endless loop with every output active.", "Nur mit der vollständigen Endlosschleife und allen eingeschalteten Ausgängen."),
          checkpointText("By changing several wires and thresholds at once.", "Indem mehrere Kabel und Grenzwerte gleichzeitig geändert werden."),
          checkpointText("By checking whether the program contains enough functions.", "Indem geprüft wird, ob das Programm genügend Funktionen enthält.")
        ],
        correct: 0,
        hint: checkpointText("Isolate the decision logic from sensor and output problems. Compare known inputs with written expected states.", "Trennt die Entscheidungslogik von Sensor- und Ausgabeproblemen. Vergleicht bekannte Eingaben mit vorher notierten Sollzuständen.")
      },
      {
        prompt: checkpointText("With the baseline rules, what should happen at exactly 60 cm?", "Was soll mit den vorgegebenen Regeln bei genau 60 cm passieren?"),
        answers: [
          checkpointText("safe: green, silent", "safe: grün, stumm"),
          checkpointText("stop: red, rapid beeps", "stop: rot, schnelle Pieptöne"),
          checkpointText("invalid: blue, silent", "invalid: blau, stumm"),
          checkpointText("caution: amber, slow beeps", "caution: bernsteinfarben, langsame Pieptöne")
        ],
        correct: 3,
        hint: checkpointText("Safe means strictly over 60 cm. Caution includes the upper boundary of 60 cm.", "safe bedeutet echt mehr als 60 cm. Der obere Grenzwert 60 cm gehört noch zu caution.")
      },
      {
        prompt: checkpointText("The final parking assistant gets no usable echo. Which output matches its invalid state?", "Der fertige Parkassistent erhält kein brauchbares Echo. Welche Ausgabe gehört zu seinem Zustand invalid?"),
        answers: [
          checkpointText("Red pixels and continuous sound", "Rote Pixel und Dauerton"),
          checkpointText("Green pixels and silence", "Grüne Pixel und Stille"),
          checkpointText("Blue pixels and silence", "Blaue Pixel und Stille"),
          checkpointText("No state change: show any previous result as current.", "Kein Zustandswechsel: Einen alten Wert weiter als aktuell anzeigen.")
        ],
        correct: 2,
        hint: checkpointText("The final project's invalid colour is blue. Missing data must not produce an alarm sound.", "Die Farbe für invalid ist im Abschlussprojekt Blau. Fehlende Daten dürfen keinen Alarmton auslösen.")
      },
      {
        prompt: checkpointText("Which shutdown test must the project pass?", "Welchen Abschalttest muss das Projekt bestehen?"),
        answers: [
          checkpointText("After Stop, the last colour and tone must remain active.", "Nach Stop müssen die letzte Farbe und der letzte Ton aktiv bleiben."),
          checkpointText("After Stop, the supplied finally cleanup turns RGB and PWM outputs off.", "Nach Stop schaltet das vorgegebene finally-Aufräumen RGB- und PWM-Ausgänge aus."),
          checkpointText("The only test is whether unplugging USB removes power.", "Es wird nur geprüft, ob das Trennen von USB die Stromversorgung beendet."),
          checkpointText("Shutdown does not matter if the normal distance tests pass.", "Abschalten ist unwichtig, wenn normale Abstandstests funktionieren.")
        ],
        correct: 1,
        hint: checkpointText("Cleanup is code that runs when the activity ends or is interrupted. Removing power does not test that code.", "Aufräumcode läuft beim Ende oder bei einer Unterbrechung der Aufgabe. Das Trennen der Stromversorgung testet diesen Code nicht.")
      }
    ]
  }
];

const checkpointCopy = {
  en: {
    overview: "Days overview",
    gateTitle: day => `Unlock Day ${day}`,
    gateIntro: day => `Enter the password from Day ${day - 1}'s exit ticket.`,
    password: "Password",
    unlock: "Open presentation",
    wrongPassword: "That password does not match. Check the code from the previous exit ticket.",
    storageWarning: "This browser cannot remember the unlock. You may need to enter the password again when reopening the presentation.",
    quizTitle: day => `Day ${day} · Exit ticket`,
    progress: (current, total) => `Question ${current} of ${total}`,
    quizIntro: "Choose one answer. Get all five questions right to receive your code. Hints help you correct mistakes.",
    choose: "Choose an answer first.",
    check: "Check answer",
    correct: "Correct.",
    incorrect: "Not quite. Hint: ",
    next: "Next question",
    finish: "Show my code",
    success: "All five questions answered correctly!",
    codeTitle: day => day === 5 ? "Your workshop completion code" : `Your password for Day ${day + 1}`,
    codeHelp: day => day === 5
      ? "Write down your code and show your teacher. Your classroom prototype is complete; it is not a real vehicle safety system."
      : "Write down the password. Enter it when you open the next day's presentation.",
    nextDay: day => `Open Day ${day + 1} and enter the password`,
    review: "Review this day's presentation",
    invalid: "This exit-ticket link is not valid. Choose a day from the overview."
  },
  de: {
    overview: "Tagesübersicht",
    gateTitle: day => `Tag ${day} freischalten`,
    gateIntro: day => `Gebt das Passwort aus dem Abschlussticket von Tag ${day - 1} ein.`,
    password: "Passwort",
    unlock: "Präsentation öffnen",
    wrongPassword: "Das Passwort stimmt nicht. Prüft den Code aus dem vorigen Abschlussticket.",
    storageWarning: "Dieser Browser kann sich die Freigabe nicht merken. Beim erneuten Öffnen müsst ihr das Passwort möglicherweise noch einmal eingeben.",
    quizTitle: day => `Tag ${day} · Abschlussticket`,
    progress: (current, total) => `Frage ${current} von ${total}`,
    quizIntro: "Wählt jeweils eine Antwort. Für euren Code müsst ihr alle fünf Fragen richtig beantworten. Hinweise helfen euch, Fehler zu korrigieren.",
    choose: "Wählt zuerst eine Antwort.",
    check: "Antwort prüfen",
    correct: "Richtig.",
    incorrect: "Noch nicht richtig. Hinweis: ",
    next: "Nächste Frage",
    finish: "Meinen Code anzeigen",
    success: "Alle fünf Fragen richtig beantwortet!",
    codeTitle: day => day === 5 ? "Euer Abschlusscode für den Workshop" : `Euer Passwort für Tag ${day + 1}`,
    codeHelp: day => day === 5
      ? "Notiert den Code und zeigt ihn eurer Lehrkraft. Euer Lernprototyp ist fertig; er ist kein Sicherheitssystem für echte Fahrzeuge."
      : "Notiert das Passwort. Gebt es ein, wenn ihr die Präsentation des nächsten Tages öffnet.",
    nextDay: day => `Tag ${day + 1} öffnen und Passwort eingeben`,
    review: "Zurück zur Präsentation dieses Tages",
    invalid: "Dieser Link zum Abschlussticket ist ungültig. Wählt einen Tag in der Tagesübersicht."
  }
};

function checkpointElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

function checkpointSession(day, unlock = false) {
  try {
    const key = `pico-workshop-unlocked-day-${day}`;
    if (unlock) sessionStorage.setItem(key, "yes");
    return sessionStorage.getItem(key) === "yes";
  } catch (error) {
    if (!(error instanceof DOMException) ||
        !["SecurityError", "QuotaExceededError"].includes(error.name)) throw error;
    console.warn("Workshop unlock cannot be saved in this tab.", error);
    return false;
  }
}

function startWorkshopDay(startSlides) {
  const day = Number(document.documentElement.dataset.workshopDay);
  const language = document.documentElement.lang === "de" ? "de" : "en";
  const copy = checkpointCopy[language];
  if (!Number.isInteger(day) || day < 1 || day > 5) {
    throw new Error("Presentation must declare a workshop day from 1 to 5.");
  }
  const open = () => {
    document.documentElement.classList.add("workshop-unlocked");
    startSlides();
  };
  if (day === 1 || checkpointSession(day)) {
    open();
    return;
  }

  const shell = checkpointElement("main", "checkpoint-shell checkpoint-gate");
  const overview = checkpointElement("a", "checkpoint-overview", copy.overview);
  overview.href = `../../${language}/`;
  const heading = checkpointElement("h1", "", copy.gateTitle(day));
  const intro = checkpointElement("p", "", copy.gateIntro(day));
  const form = checkpointElement("form", "checkpoint-form");
  const label = checkpointElement("label", "", copy.password);
  label.htmlFor = "day-password";
  const input = checkpointElement("input", "checkpoint-password");
  input.id = "day-password";
  input.type = "password";
  input.autocomplete = "off";
  input.required = true;
  input.maxLength = 40;
  input.spellcheck = false;
  const feedback = checkpointElement("p", "checkpoint-feedback");
  feedback.id = "password-feedback";
  feedback.setAttribute("role", "alert");
  input.setAttribute("aria-describedby", feedback.id);
  const submit = checkpointElement("button", "checkpoint-button", copy.unlock);
  submit.type = "submit";
  form.append(label, input, feedback, submit);
  shell.append(overview, heading, intro, form);
  document.body.append(shell);
  input.focus();

  form.addEventListener("submit", event => {
    event.preventDefault();
    if (input.value.trim().toUpperCase() !== workshopQuizDays[day - 2].password) {
      feedback.textContent = copy.wrongPassword;
      input.setAttribute("aria-invalid", "true");
      input.select();
      return;
    }
    if (!checkpointSession(day, true)) {
      window.alert(copy.storageWarning);
    }
    shell.remove();
    open();
  });
}

function startWorkshopQuiz() {
  const params = new URLSearchParams(location.search);
  const language = params.get("lang");
  const validLanguage = language === "en" || language === "de";
  const copy = checkpointCopy[validLanguage ? language : "en"];
  const dayText = params.get("day") || "";
  const validDay = /^[1-5]$/.test(dayText);
  const day = Number(dayText);
  const main = document.querySelector("#checkpoint");
  document.documentElement.lang = validLanguage ? language : "en";
  main.replaceChildren();

  const overview = checkpointElement("a", "checkpoint-overview", copy.overview);
  overview.href = `../${validLanguage ? language : "en"}/`;
  if (!validDay || !validLanguage) {
    document.title = copy.invalid;
    main.append(checkpointElement("h1", "", copy.invalid), overview);
    return;
  }

  document.title = copy.quizTitle(day);
  const quiz = workshopQuizDays[day - 1];
  let questionIndex = 0;
  const heading = () => {
    const title = checkpointElement("h1", "", copy.quizTitle(day));
    title.tabIndex = -1;
    return title;
  };

  function showResult() {
    const title = heading();
    const result = checkpointElement("section", "checkpoint-result");
    const code = checkpointElement("code", "checkpoint-code", quiz.password);
    result.append(
      checkpointElement("p", "checkpoint-success", copy.success),
      checkpointElement("h2", "", copy.codeTitle(day)),
      code,
      checkpointElement("p", "", copy.codeHelp(day))
    );
    if (day < 5) {
      const next = checkpointElement("a", "checkpoint-button", copy.nextDay(day));
      next.href = `./${language}/day-${day + 1}.html`;
      result.append(next);
    }
    const review = checkpointElement("a", "checkpoint-review", copy.review);
    review.href = `./${language}/day-${day}.html`;
    main.replaceChildren(overview, title, result, review);
    title.focus();
  }

  function showQuestion() {
    const question = quiz.questions[questionIndex];
    const title = heading();
    const progress = checkpointElement("p", "checkpoint-progress",
      copy.progress(questionIndex + 1, quiz.questions.length));
    const intro = checkpointElement("p", "checkpoint-intro", copy.quizIntro);
    const form = checkpointElement("form", "checkpoint-form");
    const fieldset = checkpointElement("fieldset", "");
    const legend = checkpointElement("legend", "", question.prompt[language]);
    fieldset.append(legend);
    if (question.code) {
      const pre = checkpointElement("pre", "");
      pre.append(checkpointElement("code", "", question.code));
      fieldset.append(pre);
    }
    const answers = checkpointElement("div", "checkpoint-answers");
    question.answers.forEach((answer, index) => {
      const label = checkpointElement("label", "checkpoint-answer");
      const radio = checkpointElement("input", "");
      radio.type = "radio";
      radio.name = "answer";
      radio.value = String(index);
      label.append(radio, checkpointElement("span", "", answer[language]));
      answers.append(label);
    });
    fieldset.append(answers);
    const feedback = checkpointElement("p", "checkpoint-feedback");
    feedback.setAttribute("role", "status");
    feedback.setAttribute("aria-live", "polite");
    const submit = checkpointElement("button", "checkpoint-button", copy.check);
    submit.type = "submit";
    form.append(fieldset, feedback, submit);
    main.replaceChildren(overview, title, progress, intro, form);
    let correct = false;
    form.addEventListener("submit", event => {
      event.preventDefault();
      if (correct) {
        questionIndex += 1;
        if (questionIndex === quiz.questions.length) showResult();
        else showQuestion();
        return;
      }
      const selected = form.querySelector('input[name="answer"]:checked');
      if (!selected) {
        feedback.textContent = copy.choose;
        form.querySelector('input[name="answer"]').focus();
      } else if (Number(selected.value) !== question.correct) {
        feedback.textContent = copy.incorrect + question.hint[language];
      } else {
        correct = true;
        fieldset.disabled = true;
        feedback.textContent = copy.correct;
        feedback.classList.add("checkpoint-success");
        submit.textContent = questionIndex === quiz.questions.length - 1
          ? copy.finish : copy.next;
        submit.focus();
      }
    });
    title.focus();
  }

  showQuestion();
}

if (document.querySelector("#checkpoint")) startWorkshopQuiz();
