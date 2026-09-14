from machine import ADC, Pin
from neopixel import NeoPixel

potentiometer = ADC(26)
pixels = NeoPixel(Pin(16), 8)

def read_poti():
    value = potentiometer.read_u16()
    return value

def show_pixel(index, colour):
    pixels.fill((0, 0, 0))
    pixels[index] = colour
    pixels.write()