from machine import Pin, time_pulse_us
from time import sleep_ms, sleep_us

TRIGGER_PIN = 19
ECHO_PIN = 18
ECHO_TIMEOUT_US = 30000
SPEED_OF_SOUND_CM_PER_US = 0.0343

trigger = Pin(TRIGGER_PIN, Pin.OUT, value=0)
echo = Pin(ECHO_PIN, Pin.IN)


def measure_distance_cm():
    trigger.off()
    sleep_us(2)
    trigger.on()
    sleep_us(10)
    trigger.off()

    pulse_us = time_pulse_us(echo, 1, ECHO_TIMEOUT_US)

    if pulse_us < 0:
        return None

    return pulse_us * SPEED_OF_SOUND_CM_PER_US / 2


print("Move an object in front of the HC-SR04.")
print("Stop with Ctrl+C.")
sleep_ms(1000)

try:
    while True:
        distance_cm = measure_distance_cm()

        if distance_cm is None:
            print("No echo")
        else:
            print("Distance:", round(distance_cm, 1), "cm")

        sleep_ms(300)
except KeyboardInterrupt:
    print("Stopped")
finally:
    trigger.off()
