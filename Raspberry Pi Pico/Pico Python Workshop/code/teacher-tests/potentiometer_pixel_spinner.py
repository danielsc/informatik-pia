# Teacher preparation test
# Potentiometer: 3V3, GP26 / ADC0, GND
# 8-RGB module IN header: S = GP16, V = 3.3 V, G = GND

from machine import ADC, Pin
from neopixel import NeoPixel
from time import sleep_ms, ticks_diff, ticks_ms

PIXEL_PIN = 16
PIXEL_COUNT = 8
POTENTIOMETER_PIN = 26

CENTRE = 32768
DEAD_ZONE = 5000
SLOWEST_DELAY_MS = 400
FASTEST_DELAY_MS = 40
STOPPED_DELAY_MS = 60
REPORT_INTERVAL_MS = 500

FORWARD_COLOUR = (0, 25, 8)
REVERSE_COLOUR = (0, 8, 25)
STOPPED_COLOUR = (12, 0, 12)
OFF = (0, 0, 0)

pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)
knob = ADC(POTENTIOMETER_PIN)


def read_knob():
    total = 0
    for sample in range(4):
        total += knob.read_u16()
    return total // 4


def control_from(raw_value):
    offset = raw_value - CENTRE
    distance = abs(offset)

    if distance <= DEAD_ZONE:
        return 0, STOPPED_DELAY_MS

    usable_distance = distance - DEAD_ZONE
    maximum_distance = CENTRE - DEAD_ZONE
    speed = usable_distance / maximum_distance
    speed = min(speed, 1)

    delay_range = SLOWEST_DELAY_MS - FASTEST_DELAY_MS
    delay_ms = SLOWEST_DELAY_MS - int(speed * delay_range)
    direction = 1 if offset > 0 else -1
    return direction, delay_ms


def show_one_pixel(index, colour):
    pixels.fill(OFF)
    pixels[index] = colour
    pixels.write()


print("Teacher test: potentiometer-controlled rotating pixel")
print("Turn the knob left or right.")
print("Centre = stopped; farther from centre = faster.")
print("Stop with Ctrl+C.")

position = 0
last_report = ticks_ms()

try:
    while True:
        raw = read_knob()
        direction, delay_ms = control_from(raw)

        if direction == 0:
            direction_name = "stopped"
            colour = STOPPED_COLOUR
        elif direction > 0:
            direction_name = "forward"
            colour = FORWARD_COLOUR
            position = (position + 1) % PIXEL_COUNT
        else:
            direction_name = "reverse"
            colour = REVERSE_COLOUR
            position = (position - 1) % PIXEL_COUNT

        show_one_pixel(position, colour)

        now = ticks_ms()
        if ticks_diff(now, last_report) >= REPORT_INTERVAL_MS:
            print(
                "Raw:",
                raw,
                "Direction:",
                direction_name,
                "Delay:",
                delay_ms,
                "ms",
            )
            last_report = now

        sleep_ms(delay_ms)
except KeyboardInterrupt:
    print("Stopped")
finally:
    pixels.fill(OFF)
    pixels.write()
