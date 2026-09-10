# Day 3: Make It Reusable

## Mission

Organise repeated code into functions and bring eight RGB pixels to life.

**Python:** imports, functions, parameters, return values, lists, tuples,
`for`, `range`, indexes, nested loops, local variables  
**Hardware:** Freenove 8-RGB LED module, potentiometer  
**TEALS connection:** Unit 3 Functions and Unit 4 Nested Loops and Lists

## 1. Meet the RGB module

Disconnect USB and follow the
[8-RGB wiring table](WIRING_AND_SAFETY.md#freenove-8-rgb-led-module).

Open the
[scalable, accessible 8-RGB module diagram](diagrams/rgb8-module.html) and use
the module header marked `IN`.

![Freenove square 8-RGB module IN header wired to GP16](diagrams/rgb8-module.png)

![Freenove 8-RGB module connection](https://docs.freenove.com/projects/fnk0063/en/latest/_images/Chapter06_05.png)

The official
[Freenove NeoPixel lesson](https://docs.freenove.com/projects/fnk0063/en/latest/fnk0063/codes/Python/6_NeoPixel.html)
uses a custom library. Our code uses MicroPython's built-in `neopixel` module,
so no extra file is required.

Run [`code/day-3/01_neopixel_colours.py`](code/day-3/01_neopixel_colours.py).

An RGB colour is a tuple of red, green, and blue values:

```python
RED = (30, 0, 0)
GREEN = (0, 30, 0)
BLUE = (0, 0, 30)
```

Keep values low; `255, 255, 255` is unnecessarily bright.

## 2. A `for` loop visits each index

```python
for index in range(8):
    pixels[index] = (0, 0, 20)
    pixels.write()
```

`range(8)` produces 0 through 7, exactly the valid pixel indexes. What error do
you predict for `pixels[8]`?

Run [`code/day-3/02_pixel_functions.py`](code/day-3/02_pixel_functions.py).
Find:

- a function with no parameter;
- a function with two parameters;
- a local variable;
- a `return` value;
- nested loops.

Explain why returning a colour is more reusable than printing a colour.

## 3. Write functions before animations

Implement and test these one at a time:

```python
def show_colour(colour):
    ...

def chase(colour, delay_ms):
    ...

def level_to_colour(percent):
    ...
```

A function is a promise: given suitable inputs, it performs one named job.

## Daily build: Pixel Pet

Keep the RGB module on GP16. Add the potentiometer on GP26 using 3.3 V and GND.
There is no ordinary LED in this build.

Start from [`code/day-3/03_pixel_pet_starter.py`](code/day-3/03_pixel_pet_starter.py).
The knob controls the pet's “energy”:

- 0-32%: sleepy, slow blue pulse;
- 33-65%: curious, green moving pixel;
- 66-100%: excited, quick colourful sparkle.

Requirements:

- a function reads and returns energy percent;
- a function decides and returns the state;
- a function displays each state;
- at least one `for` loop visits all pixels;
- at least one animation uses a pixel index;
- the loop prints energy and state for debugging.

### Stretch ideas

- Define colours in a list and traverse it.
- Add a “hungry” warning if energy remains low for ten readings.
- Store the most recent five readings and display their average.
- Use nested loops for a two-lap chase.

### Demo checklist

- Show all three boundary regions.
- Explain one parameter and one return value.
- Explain why your functions are easier to test than one long loop.

## Exit ticket

What is the difference between:

```python
print(energy)
return energy
```

Which one lets another function make a decision using the value?
