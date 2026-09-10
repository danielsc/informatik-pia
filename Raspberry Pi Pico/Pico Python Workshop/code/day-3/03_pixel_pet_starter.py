from machine import ADC, Pin
from neopixel import NeoPixel
from time import sleep_ms

PIXEL_PIN = 16
PIXEL_COUNT = 8
POTENTIOMETER_PIN = 26
OFF = (0, 0, 0)

pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)
knob = ADC(POTENTIOMETER_PIN)


def read_energy_percent():
    raw_value = knob.read_u16()
    # TODO: convert raw_value from 0-65535 to 0-100.
    return 0


def choose_state(energy_percent):
    # TODO: return "sleepy", "curious", or "excited".
    return "sleepy"


def show_sleepy():
    # TODO: create a slow blue animation.
    pass


def show_curious():
    # TODO: create a moving green pixel.
    pass


def show_excited():
    # TODO: create a quick colourful animation.
    pass


try:
    while True:
        energy = read_energy_percent()
        state = choose_state(energy)
        print("Energy:", energy, "State:", state)

        if state == "sleepy":
            show_sleepy()
        elif state == "curious":
            show_curious()
        else:
            show_excited()

        sleep_ms(100)
except KeyboardInterrupt:
    print("Pixel Pet is resting.")
finally:
    pixels.fill(OFF)
    pixels.write()

