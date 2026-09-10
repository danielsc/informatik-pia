from machine import Pin
from neopixel import NeoPixel
from time import sleep

PIXEL_PIN = 16
PIXEL_COUNT = 8

pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)
colours = [
    (30, 0, 0),
    (0, 30, 0),
    (0, 0, 30),
    (20, 10, 0),
    (0, 0, 0),
]

print("Showing red, green, blue, amber, and off.")

try:
    for colour in colours:
        pixels.fill(colour)
        pixels.write()
        print("Colour:", colour)
        sleep(1)
finally:
    pixels.fill((0, 0, 0))
    pixels.write()

