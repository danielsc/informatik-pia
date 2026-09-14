from machine import Pin
from neopixel import NeoPixel
from time import sleep

PIXEL_PIN = 16
PIXEL_COUNT = 8

pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)
RED = (30, 0, 0)
GREEN = (0, 30, 0)
BLUE = (0, 0, 30)
AMBER = (20, 10, 0)
OFF = (0, 0, 0)

print("Showing red, green, blue, amber, and off.")

try:
    pixels.fill(RED)
    pixels.write()
    print("Colour:", RED)
    sleep(1)

    pixels.fill(GREEN)
    pixels.write()
    print("Colour:", GREEN)
    sleep(1)

    pixels.fill(BLUE)
    pixels.write()
    print("Colour:", BLUE)
    sleep(1)

    pixels.fill(AMBER)
    pixels.write()
    print("Colour:", AMBER)
    sleep(1)

    pixels.fill(OFF)
    pixels.write()
    print("Colour:", OFF)
    sleep(1)
finally:
    pixels.fill(OFF)
    pixels.write()
