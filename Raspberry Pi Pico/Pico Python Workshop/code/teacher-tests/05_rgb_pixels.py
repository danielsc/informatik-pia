from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

PIXEL_PIN = 16
PIXEL_COUNT = 8

pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)
colours = [
    (20, 0, 0),
    (0, 20, 0),
    (0, 0, 20),
]
off = (0, 0, 0)

print("One pixel should move around the eight-pixel module.")
print("Its colour changes after each lap. Stop with Ctrl+C.")

try:
    while True:
        for colour in colours:
            print("Colour:", colour)

            for index in range(PIXEL_COUNT):
                pixels.fill(off)
                pixels[index] = colour
                pixels.write()
                print("Pixel:", index)
                sleep_ms(200)
except KeyboardInterrupt:
    print("Stopped")
finally:
    pixels.fill(off)
    pixels.write()
