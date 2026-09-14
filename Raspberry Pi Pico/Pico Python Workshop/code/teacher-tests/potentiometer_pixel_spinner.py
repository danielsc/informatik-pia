# Teacher preparation test
# Potentiometer: 3V3, GP26 / ADC0, GND
# 8-RGB module IN header: S = GP16, V = 3.3 V, G = GND

from machine import ADC, Pin
from neopixel import NeoPixel
from time import sleep_ms

pixels = NeoPixel(Pin(16), 8)
knob = ADC(26)

position = 0
off = (0, 0, 0)
colour = (0, 20, 10)

print("Turn the knob left or right.")
print("Centre = stopped; farther from centre = faster.")
print("Stop with Ctrl+C.")

try:
    while True:
        value = knob.read_u16()

        if value < 28000:
            direction = -1
            direction_name = "reverse"
        elif value > 38000:
            direction = 1
            direction_name = "forward"
        else:
            direction = 0
            direction_name = "stopped"

        distance_from_centre = abs(value - 32768)
        delay_ms = 400 - distance_from_centre // 100

        if delay_ms < 50:
            delay_ms = 50

        if direction != 0:
            position = (position + direction) % 8

        pixels.fill(off)
        pixels[position] = colour
        pixels.write()

        print(
            "Value:",
            value,
            "Direction:",
            direction_name,
            "Delay:",
            delay_ms,
            "ms",
        )

        sleep_ms(delay_ms)
except KeyboardInterrupt:
    print("Stopped")
finally:
    pixels.fill(off)
    pixels.write()
