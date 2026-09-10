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
MAX_DISPLAY_DISTANCE_CM = 100
MIN_DISPLAY_DISTANCE_CM = 10
ECHO_TIMEOUT_US = 30000
SPEED_OF_SOUND_CM_PER_US = 0.0343
BUZZER_FREQUENCY_HZ = 1800
BUZZER_DUTY = 2500

OFF = (0, 0, 0)
ZONE_CONFIG = {
    "safe": {
        "colour": (0, 20, 0),
        "beep_ms": 0,
        "pause_ms": 250,
    },
    "caution": {
        "colour": (25, 8, 0),
        "beep_ms": 80,
        "pause_ms": 520,
    },
    "stop": {
        "colour": (25, 0, 0),
        "beep_ms": 80,
        "pause_ms": 120,
    },
    "invalid": {
        "colour": (0, 0, 20),
        "beep_ms": 0,
        "pause_ms": 300,
    },
}

trigger = Pin(TRIGGER_PIN, Pin.OUT, value=0)
echo = Pin(ECHO_PIN, Pin.IN)
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.freq(BUZZER_FREQUENCY_HZ)
buzzer.duty_u16(0)
pixels = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)


def measure_distance_cm():
    trigger.off()
    sleep_us(2)
    trigger.on()
    sleep_us(10)
    trigger.off()

    pulse_us = time_pulse_us(echo, 1, ECHO_TIMEOUT_US)
    if pulse_us < 0:
        return None

    distance_cm = pulse_us * SPEED_OF_SOUND_CM_PER_US / 2
    if distance_cm < 2 or distance_cm > 200:
        return None
    return distance_cm


def classify_distance(distance_cm):
    if distance_cm is None:
        return "invalid"
    if distance_cm > SAFE_DISTANCE_CM:
        return "safe"
    if distance_cm > STOP_DISTANCE_CM:
        return "caution"
    return "stop"


def distance_to_pixel_count(distance_cm):
    if distance_cm is None:
        return 1

    clamped = min(
        max(distance_cm, MIN_DISPLAY_DISTANCE_CM),
        MAX_DISPLAY_DISTANCE_CM,
    )
    approach = MAX_DISPLAY_DISTANCE_CM - clamped
    display_range = MAX_DISPLAY_DISTANCE_CM - MIN_DISPLAY_DISTANCE_CM
    return 1 + int(approach * (PIXEL_COUNT - 1) / display_range)


def show_zone(zone, distance_cm):
    colour = ZONE_CONFIG[zone]["colour"]
    lit_pixels = distance_to_pixel_count(distance_cm)

    pixels.fill(OFF)
    for index in range(lit_pixels):
        pixels[index] = colour
    pixels.write()


def sound_zone(zone):
    config = ZONE_CONFIG[zone]
    beep_ms = config["beep_ms"]

    if beep_ms > 0:
        buzzer.duty_u16(BUZZER_DUTY)
        sleep_ms(beep_ms)
        buzzer.duty_u16(0)

    sleep_ms(config["pause_ms"])


def print_status(distance_cm, zone):
    if distance_cm is None:
        print("Distance: invalid | Zone:", zone)
    else:
        print("Distance:", round(distance_cm, 1), "cm | Zone:", zone)


print("Parking assistant ready. Stop with Ctrl+C.")
sleep_ms(1000)

try:
    while True:
        distance = measure_distance_cm()
        zone = classify_distance(distance)
        print_status(distance, zone)
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

