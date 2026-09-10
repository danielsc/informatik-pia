from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

PIXEL_PIN = 16
PIXEL_COUNT = 8
OFF = (0, 0, 0)

pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)


def show_colour(colour):
    pixels.fill(colour)
    pixels.write()


def chase(colour, delay_ms):
    for index in range(PIXEL_COUNT):
        pixels.fill(OFF)
        pixels[index] = colour
        pixels.write()
        sleep_ms(delay_ms)


def level_to_colour(percent):
    if percent < 33:
        return (0, 0, 25)
    if percent < 66:
        return (0, 25, 0)
    return (25, 5, 0)


try:
    for level in [10, 50, 90]:
        colour = level_to_colour(level)
        print("Level:", level, "Colour:", colour)
        show_colour(colour)
        sleep_ms(500)
        chase(colour, 100)

    for lap in range(2):
        for colour in [(20, 0, 0), (0, 20, 0), (0, 0, 20)]:
            chase(colour, 60)
finally:
    show_colour(OFF)

