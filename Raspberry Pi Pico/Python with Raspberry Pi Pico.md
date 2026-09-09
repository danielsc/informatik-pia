## **Physical Computing Curriculum for Secondary School**

**Target group:** Grade 8 / Sekundarstufe I  
**Programming language:** MicroPython  
**Hardware:** Raspberry Pi Pico 2 H  
**Class size:** approximately 70 students  
**Working arrangement:** pairs  
**Required workstations:** 35 student workstations + 3 spare sets = **38 hardware kits**

---
# **1. Curriculum Overview**

This curriculum adapts the programming-language content of the TEALS Introduction to Computer Science curriculum to physical computing with the Raspberry Pi Pico.

The emphasis remains on learning Python. The Pico provides physical inputs and outputs that make programming concepts visible and interactive.

|**Unit**|**Python concepts**|**Physical computing concepts**|**Main project**|
|---|---|---|---|
|1. Make Things Happen|variables, data types, `print()`, input/output, errors|GPIO, LEDs, buttons|Interactive signal device|
|2. Make Things Decide|casting, Boolean expressions, conditionals, lists, `while`|buttons, LEDs, buzzer|Reaction game|
|3. Make Things Reusable|functions, arguments, return values, imports, scope|reusable hardware functions|Security/alarm system|
|4. Make Things Repeat|`for`, `range()`, lists, indexes, nested loops|NeoPixel RGB LEDs|Light animations / game|
|5. Make Things Sense and Move|integration of previous Python concepts|sensors, PWM and actuators|Physical-computing design project|
|6. Make Things Remember|dictionaries, lists in dictionaries, iteration|game state and configuration|Physical quiz/game console|

Unit 5 replaces the optional EarSketch unit in the original TEALS curriculum.

---

# **Unit 1 — Make Things Happen**

## **Goal**

Introduce Python programming and demonstrate that code can control objects in the physical world.

## **Python concepts**

- Python / MicroPython
- IDE
- interpreter
- console
- script
- expressions
- strings
- integers
- floats
- variables
- assignment
- `print()`
- comments
- input/output
- syntax errors
- debugging

## **Pico concepts**

- Connecting the Pico via USB
- Running MicroPython from Thonny
- GPIO pins
- Digital output
- LEDs
- Pushbuttons
- Digital input

## **Suggested progression**

### **1.1 Hello Python**

```python
print("Hello!")
```

Students learn the IDE, console and interpreter.

### **1.2 Hello Pico**

```python
from machine import Pin

led = Pin("LED", Pin.OUT)
led.on()
```

The first program changes something in the physical world.

### **1.3 Variables and types**

```python
delay = 0.5
number_of_flashes = 5
message = "Starting"
```

Discuss:

- `float`
- `int`
- `str`
- variables
- assignment

### **1.4 Physical output**

Students create LED sequences and use the buzzer.

Possible exercise:

Create your own visual SOS or secret signalling pattern.

### **1.5 Physical input**

Connect a pushbutton.

```python
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

print(button.value())
```

Discuss the general computer-science concept:

**Input → Processing → Output**

Keyboard input and a physical button are both forms of input.

### **1.6 Debugging**

Students receive deliberately broken programs and/or circuits.

They identify:

- syntax errors
- missing imports
- incorrect pin numbers
- missing parentheses
- incorrect wiring
- software vs hardware errors

## **Unit project**

### **Interactive Signal Device**

Using:

- Pico
- pushbuttons
- LEDs
- buzzer

Possible projects:

- pedestrian crossing
- doorbell
- secret signalling device
- traffic light
- warning system

---

# **Unit 2 — Make Things Decide**

## **Goal**

Introduce program logic and state by creating an interactive game.

## **Python concepts**

- data types
- casting
- Boolean values
- `True`
- `False`
- comparison operators
- `and`
- `or`
- `not`
- `if`
- `elif`
- `else`
- lists
- indexes
- `len()`
- `append()`
- `pop()`
- `remove()`
- `while`

## **2.1 Data types and casting**

Example:

```python
score = 10

print("Score: " + str(score))
```

Students discover why this does not work:

```python
print("Score: " + score)
```

This provides a practical reason for learning type conversion.

## **2.2 Booleans**

A physical button provides a natural Boolean input.

```python
pressed = button.value()

if pressed:
    led.on()
```

Experiments can introduce:

```python
if button1.value() and button2.value():
```

and:

```python
if button1.value() or button2.value():
```

## **2.3 Conditionals**

Students classify reaction times:

```python
if reaction_time < 300:
    print("Amazing!")
elif reaction_time < 500:
    print("Good!")
else:
    print("Too slow!")
```

## **2.4 Lists**

Store successive reaction times:

```python
reaction_times = [421, 389, 512, 301]
```

Students use:

```python
reaction_times[0]
len(reaction_times)
reaction_times.append(new_time)
reaction_times.pop()
```

## **2.5 Game loop**

```python
while score < 10:
    play_round()
```

Introduce the concept of a game loop.

## **Unit project**

### **Reaction Game**

Basic sequence:

1. Player presses Start.
2. Pico waits for a random interval.
3. LED/NeoPixel lights up.
4. Player presses the reaction button.
5. Pico measures reaction time.
6. Result appears on the laptop.
7. Score is stored.

Possible extensions:

- two players
- best of five
- false-start detection
- difficulty levels
- high-score list
- buzzer feedback
- different NeoPixel colors

---

# **Unit 3 — Make Things Reusable**

## **Goal**

Teach students to structure increasingly complex programs using functions.

## **Python concepts**

- functions
- calling functions
- arguments
- parameters
- imports
- return values
- `None`
- abstraction
- user-defined functions
- local variables
- global variables
- scope
- mutable lists
- stack traces

## **3.1 Libraries and imports**

Examples:

```python
from random import randint
from machine import Pin
from time import sleep
```

Discuss the idea of using code written by other programmers through an API.

## **3.2 User-defined functions**

Instead of repeating:

```python
led.on()
sleep(0.2)
led.off()
```

students create:

```python
def flash_led():
    led.on()
    sleep(0.2)
    led.off()
```

Then introduce parameters:

```python
def flash_led(times, delay):
    ...
```

## **3.3 Return versus print**

```python
def get_reaction_time():
    ...
    return elapsed
```

Compare with:

```python
def get_reaction_time():
    ...
    print(elapsed)
```

Question:

Which version allows another part of the program to use the result?

## **3.4 Scope**

Example:

```python
score = 0

def play_round():
    score = 1
```

Why does the global score not change?

Discuss:

- local scope
- global scope
- mutable data
- program state

## **Unit project**

### **Security / Alarm System**

Possible functions:

```python
arm()
disarm()
read_sensor()
sound_alarm()
check_code()
```

Possible hardware:

- buttons
- LEDs
- buzzer
- NeoPixel stick

---

# **Unit 4 — Make Things Repeat**

## **Goal**

Introduce iteration and more complex data structures through programmable RGB LEDs.

## **Python concepts**

- `for`
- iteration
- `range()`
- indexes
- lists
- traversal
- nested loops
- nested lists
- debugging loops

## **Hardware focus**

**8-pixel WS2812 / NeoPixel RGB stick**

Each of the eight LEDs can be controlled independently.

## **4.1 Basic iteration**

```python
for i in range(8):
    print(i)
```

Then apply the same concept to physical LEDs.

## **4.2 Moving light**

Conceptually:

```python
for i in range(8):
    pixels[i] = (255, 0, 0)
    pixels.write()
    sleep(0.1)
    pixels[i] = (0, 0, 0)
```

This makes indexes and `range()` visually understandable.

## **4.3 Lists and colors**

```python
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]
```

Students iterate over colors and pixels.

## **4.4 Nested loops**

Example concept:

```python
for repetition in range(5):
    for pixel in range(8):
        ...
```

Students can see the relationship between outer and inner loops directly in the resulting animation.

## **Unit project**

### **NeoPixel Game or Animation**

Possible projects:

- moving light
- racing lights
- Simon-style memory game
- reaction game
- countdown
- random color game
- traffic simulation
- animated status indicator

---

# **Unit 5 — Make Things Sense and Move**

## **Replacement for TEALS EarSketch unit**

This unit deliberately introduces relatively little new Python syntax.

Instead, students use the programming concepts they already know to interact with additional hardware.

## **Concepts**

Possible topics include:

- analogue input
- sensors
- PWM
- servo motors
- sound
- physical state
- event-driven behaviour

Example:

```python
distance = get_distance()

if distance < 10:
    sound_alarm()
else:
    show_safe()
```

## **Possible projects**

### **Parking assistant**

Distance determines:

- NeoPixel color
- flashing rate
- buzzer frequency

### **Electronic safe**

Correct button sequence unlocks the device.

### **Miniature traffic system**

Buttons represent pedestrians and vehicles.

### **Environmental indicator**

Sensor measurements are converted into NeoPixel colors.

### **Electronic instrument**

Input values determine sound frequency or rhythm.

## **Unit project**

### **Smart Device Challenge**

Students design a physical device that must include:

- at least one input
- at least one output
- a conditional
- a loop
- a function
- a variable representing state

---

# **Unit 6 — Make Things Remember**

## **Goal**

Introduce dictionaries and structured data through games and device configuration.

## **Python concepts**

- dictionaries
- keys
- values
- dictionary access
- updating dictionaries
- `pop()`
- default values
- dictionaries containing lists
- iteration over dictionaries

## **6.1 Basic dictionaries**

```python
player = {
    "name": "Anna",
    "score": 12,
    "level": 3
}
```

Or device configuration:

```python
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}
```

## **6.2 Dictionaries containing lists**

```python
players = {
    "Anna": [320, 301, 289],
    "Leo": [410, 355, 330]
}
```

Students can calculate:

- fastest result
- average result
- number of attempts
- leaderboard position

## **6.3 Looping through dictionaries**

```python
for player, scores in players.items():
    print(player, scores)
```

## **Unit project**

### **Physical Quiz / Game Console**

Questions remain displayed on the laptop rather than requiring an expensive OLED display.

Example data:

```python
questions = [
    {
        "question": "What is 7 * 8?",
        "answers": [42, 48, 56, 64],
        "correct": 2
    }
]
```

The laptop displays:

```text
What is 7 * 8?

A: 42
B: 48
C: 56
D: 64
```

The student answers using four physical buttons.

The Pico can respond with:

- green/red LEDs
- NeoPixel animation
- buzzer
- score update

This integrates:

- variables
- lists
- dictionaries
- nested data structures
- loops
- conditionals
- functions
- physical input
- physical output

---

# **Mapping to the Original TEALS Curriculum**

|**TEALS concept**|**Pico curriculum**|
|---|---|
|Interpreter|✓|
|Strings|✓|
|Integers|✓|
|Floats|✓|
|Variables|✓|
|Expressions|✓|
|Input/output|✓|
|Debugging|✓|
|Casting|✓|
|Booleans|✓|
|`if / elif / else`|✓|
|Lists|✓|
|List methods|✓|
|`while` loops|✓|
|Imports|✓|
|Built-in functions|✓|
|User-defined functions|✓|
|Arguments / parameters|✓|
|Return values|✓|
|Scope|✓|
|`for` loops|✓|
|`range()`|✓|
|Nested loops|✓|
|Nested lists|✓|
|Dictionaries|✓|
|Dictionary methods|✓|
|Dictionaries containing lists|✓|
|Dictionary iteration|✓|
|EarSketch|Replaced by physical computing|

---

# **Five-Day Workshop Version**

The complete curriculum above is suitable for a longer Informatik course.

For a single project week, use a vertical slice through the curriculum.

|**Day**|**Programming**|**Physical project**|
|---|---|---|
|**1 — Make it light**|IDE, scripts, variables, types, `print()`, errors|LEDs and simple signals|
|**2 — Make it react**|input, Booleans, `if/elif/else`|Buttons + reaction tester|
|**3 — Make it a game**|`while`, lists, random numbers|Reaction game + scores|
|**4 — Make it reusable**|functions, arguments, `for`, `range()`|NeoPixel game/animations|
|**5 — Build your own**|integration + debugging|Team design challenge|

The objective should not be to cover every Python feature in five days.

The project week should establish a strong understanding of:

1. variables
2. data types
3. input and output
4. Boolean logic
5. conditionals
6. loops
7. lists
8. functions
9. debugging

---

# **Hardware Bill of Materials**

## **Class assumptions**

- Students: **70**
- Students per team: **2**
- Active teams: **35**
- Complete spare sets: **3**
- Total hardware sets: **38**

All hardware below is sourced from **BerryBase Germany**.

Prices are retail prices including German VAT as checked on **8 September 2026** and may change.

---

# **Standard Hardware Set per Pair**

Each pair receives:

- 1 × Raspberry Pi Pico 2 H
- 1 × 400-contact breadboard
- 1 × 8-pixel WS2812 NeoPixel stick
- 4 × pushbuttons with caps
- 15 × ordinary LEDs
- 30 × 330 Ω resistors
- 1 × active buzzer
- 10 × male-to-male jumper wires
- 10 × male-to-female jumper wires
- 10 × female-to-female jumper wires
- 1 × USB data cable
- 1 × storage hardcase

---

# **BerryBase Purchasing List**

## **1. Raspberry Pi Pico 2 with Headers**

**Product:** Raspberry Pi Pico 2, RP2350 Mikrocontroller-Board, mit Headern**BerryBase product number:** `RPI-PICO2-H`  
**Quantity:** 38**Price:** €6.50 each**Total:** **€247.00**

Product:

https://www.berrybase.de/raspberry-pi-pico-2-rp2350-mikrocontroller-board-mit-headern

The **H/header version is strongly recommended** for school use because the GPIO headers are already fitted. Students do not need to solder headers onto the boards.

At the time of checking, BerryBase showed **100+ units immediately available**.

---

## **2. Electronics Project Kit**

**Product:** Elektronik Projekt-Kit mit Breadboard, Jumperkabeln, LEDs, Tastern, Buzzer, Widerständen & Tasche**BerryBase product number:** `RPI-PKIT1`  
**Quantity:** 38**Price:** €5.90 each**Total:** **€224.20**

Product:

https://www.berrybase.de/elektronik-projekt-kit-mit-breadboard-jumperkabeln-leds-tastern-buzzer-widerstaenden-tasche

### **Contents of each kit**

- 15 × 5 mm LEDs
    - 5 yellow
    - 5 red
    - 5 green
- 4 × pushbuttons with caps
- 30 × 330 Ω resistors
- 1 × active 5 V buzzer
- 10 × female-female jumper wires, 20 cm
- 10 × female-male jumper wires, 20 cm
- 10 × male-male jumper wires, 20 cm
- 1 × 400-contact breadboard
- 1 × hard storage case

### **Availability warning**

As of **8 September 2026**, BerryBase lists this item as:

**“Artikel aktuell nicht lieferbar.”**

Because the kit is unusually well matched to this curriculum and inexpensive, the recommended course of action is to contact BerryBase and request:

- expected restock date
- availability of 38 units
- educational/B2B pricing
- a quotation for the complete school order

BerryBase also lists the product in its B2B shop:

https://b2b.berrybase.de/Raspberry-Pi/Boards/Kits/Projekt-Kit-fuer-Get-Started-with-Raspberry-Pi/

---

## **3. 8-Pixel NeoPixel Stick**

**Product:** NeoPixel Stick mit 8 WS2812 5050 RGB LEDs**BerryBase product number:** `NEOPS8`  
**Quantity:** 38**Price:** €2.60 each**Total:** **€98.80**

Product:

https://www.berrybase.de/neopixel-stick-mit-8-ws2812-5050-rgb-leds

At the time of checking, BerryBase showed **100+ units immediately available**.

Each stick contains eight individually addressable WS2812 RGB LEDs.

This component is particularly useful for teaching:

- lists
- indexes
- `for` loops
- `range()`
- nested loops
- functions
- RGB tuples
- state
- animation

---

## **4. USB Data Cables**

The Pico 2 uses a **Micro-USB connector**.

For laptops with USB-A ports:

**Product:** USB 2.0 Hi-Speed Kabel A-Stecker – Micro-B-Stecker**BerryBase product number:** `MicroUSBblk` / appropriate length**Quantity:** 38**Price:** from approximately €0.90 each**Estimated total:** **€34.20**

BerryBase Micro-USB category:

https://www.berrybase.de/multimedia-office/kabel-adapter/computer/usb-kabel-adapter/micro-usb/

Example 0.5 m cable:

https://www.berrybase.de/usb-2.0-hi-speed-kabel-a-stecker-micro-b-stecker-0-50m-schwarz

The cable must support **data**, not merely charging.

### **Important before ordering**

Check the student laptops.

If the laptops primarily have USB-C ports, order **USB-C → Micro-B data cables** instead.

Do not purchase 38 USB-A cables until the laptop interfaces have been confirmed.

---

# **Cost Summary**

|**Product**|**Quantity**|**Unit price**|**Total**|
|---|---|---|---|
|Raspberry Pi Pico 2 H|38|€6.50|€247.00|
|Electronics Project Kit|38|€5.90|€224.20|
|8-pixel NeoPixel stick|38|€2.60|€98.80|
|USB data cable|38|~€0.90|~€34.20|
|**Total**|||**~€604.20**|

Shipping is not included.

## **Cost per workstation**

Approximately:

**€604.20 / 38 = €15.90 per complete workstation**

## **Cost per student**

For 70 students:

**€604.20 / 70 = €8.63 per student**

The hardware is reusable in subsequent school years.

---

# **Recommended Budget Request**

Although the calculated hardware cost is approximately **€604**, a school budget request of approximately **€700** is recommended.

This provides room for:

- shipping
- price changes
- replacement components
- additional USB cables/adapters
- damaged Pico boards
- damaged NeoPixel sticks
- consumable components

The 38-set calculation already includes three complete spare workstations.

---

# **How to Order**

## **Preferred route**

Contact BerryBase before placing the order because the electronics project kit is currently unavailable.

Request a quotation for:

|**BerryBase SKU**|**Product**|**Quantity**|
|---|---|---|
|`RPI-PICO2-H`|Raspberry Pi Pico 2 with headers|**38**|
|`RPI-PKIT1`|Electronics Project Kit|**38**|
|`NEOPS8`|8 × WS2812 NeoPixel Stick|**38**|
|`MicroUSBblk` or equivalent|USB data cable|**38**|

BerryBase:

https://www.berrybase.de/

BerryBase B2B:

https://b2b.berrybase.de/

In the request, explain that this is a **school purchase for approximately 70 students** and ask for:

1. availability/restock date of `RPI-PKIT1`
2. quotation for 38 units of each item
3. educational or volume discount
4. shipping cost
5. delivery time
6. whether the complete quantity can be supplied in one shipment

---

# **Recommended Classroom Organization**

Number the hardware cases:

```text
PICO-01
PICO-02
PICO-03
...
PICO-38
```

Students work in permanent pairs.

Sets **01–35** are active student kits.

Sets **36–38** remain spare.

At the end of every session, each pair checks that its case contains:

- Pico
- breadboard
- NeoPixel stick
- USB cable
- four buttons
- buzzer
- jumper wires
- LEDs
- resistors

This makes the equipment manageable across multiple classes and school years.

---

# **Software Requirements**

No paid software is required.

Student laptops require:

- Python/MicroPython-compatible IDE
- recommended: **Thonny**
- Raspberry Pi Pico MicroPython firmware

The Pico itself does **not** run Linux.

Commands such as:

```bash
sudo apt update
sudo apt upgrade
```

do not run on a Pico.

Programs are written on the student’s laptop and transferred to/run on the Pico through USB.

---

# **Overall Recommendation**

For a first implementation, keep the hardware deliberately simple.

The combination of:

- Raspberry Pi Pico 2 H
- breadboard
- four buttons
- ordinary LEDs
- buzzer
- eight programmable RGB LEDs

is sufficient to teach almost all of the core Python concepts in the adapted TEALS curriculum.

Avoid adding OLED displays, complex sensors or robotics hardware initially. They introduce additional libraries, wiring and hardware debugging that can distract from the primary objective:

**Learning programming through physical computing.**

Once the core course is established, sensors and actuators can be added as optional advanced projects in Unit 5.