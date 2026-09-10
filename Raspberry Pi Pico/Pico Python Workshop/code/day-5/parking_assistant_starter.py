from machine import Pin, PWM, time_pulse_us
from neopixel import NeoPixel
from time import sleep_ms, sleep_us

TRIGGER_PIN = 19
ECHO_PIN = 18
BUZZER_PIN = 15
PIXEL_PIN = 16
PIXEL_COUNT = 8

SAFE_DISTANCE_CM = 60
STOP_DISTANCE_CM = 25
ECHO_TIMEOUT_US = 30000

OFF = (0, 0, 0)
ZONE_COLOURS = {
    "safe": (0, 20, 0),
    "caution": (25, 8, 0),
    "stop": (25, 0, 0),
    "invalid": (0, 0, 20),
}

trigger = Pin(TRIGGER_PIN, Pin.OUT, value=0)
echo = Pin(ECHO_PIN, Pin.IN)
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0)
pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)


def measure_distance_cm():
    # TODO: send a 10 microsecond trigger pulse.
    # TODO: call time_pulse_us with a timeout.
    # TODO: return None for a negative pulse result.
    # TODO: convert round-trip microseconds to centimetres.
    return None


def classify_distance(distance_cm):
    # TODO: return "invalid", "safe", "caution", or "stop".
    return "invalid"


def show_zone(zone, distance_cm):
    # TODO: get the colour from ZONE_COLOURS.
    # TODO: set RGB pixels and call pixels.write().
    pass


def sound_zone(zone):
    # TODO: safe and invalid must be silent.
    # TODO: caution should beep slowly and stop should beep quickly.
    sleep_ms(200)


try:
    while True:
        distance = measure_distance_cm()
        zone = classify_distance(distance)
        print("Distance:", distance, "Zone:", zone)
        show_zone(zone, distance)
        sound_zone(zone)
except KeyboardInterrupt:
    print("Parking assistant stopped.")
finally:
    trigger.off()
    buzzer.duty_u16(0)
    buzzer.deinit()
    pixels.fill(OFF)
    pixels.write()

