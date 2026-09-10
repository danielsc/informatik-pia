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
    return int(knob.read_u16() / 65535 * 100)


def choose_state(energy_percent):
    if energy_percent < 33:
        return "sleepy"
    if energy_percent < 66:
        return "curious"
    return "excited"


def show_sleepy():
    for blue in range(2, 15, 3):
        pixels.fill((0, 0, blue))
        pixels.write()
        sleep_ms(80)
    pixels.fill(OFF)
    pixels.write()


def show_curious():
    for index in range(PIXEL_COUNT):
        pixels.fill(OFF)
        pixels[index] = (0, 20, 0)
        pixels.write()
        sleep_ms(50)


def show_excited():
    colours = [(25, 0, 5), (20, 10, 0), (0, 15, 15), (15, 0, 20)]
    for index in range(PIXEL_COUNT):
        pixels[index] = colours[index % len(colours)]
    pixels.write()
    sleep_ms(120)
    pixels.fill(OFF)
    pixels.write()


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

