from machine import Pin, PWM, time_pulse_us
from time import sleep_ms, sleep_us

TRIGGER_PIN = 19
ECHO_PIN = 18
BUZZER_PIN = 15
SAFE_DISTANCE_CM = 60
STOP_DISTANCE_CM = 25
ECHO_TIMEOUT_US = 30000
SPEED_OF_SOUND_CM_PER_US = 0.0343
BUZZER_DUTY = 2500

trigger = Pin(TRIGGER_PIN, Pin.OUT, value=0)
echo = Pin(ECHO_PIN, Pin.IN)
led = Pin("LED", Pin.OUT)
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.freq(1800)
buzzer.duty_u16(0)

ZONE_CONFIG = {
    "safe": {"beep_ms": 0, "pause_ms": 300},
    "caution": {"beep_ms": 80, "pause_ms": 520},
    "stop": {"beep_ms": 80, "pause_ms": 120},
    "invalid": {"beep_ms": 0, "pause_ms": 300},
}


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


def classify_distance(distance_cm):
    if distance_cm is None:
        return "invalid"
    if distance_cm > SAFE_DISTANCE_CM:
        return "safe"
    if distance_cm > STOP_DISTANCE_CM:
        return "caution"
    return "stop"


def alert_once(zone):
    config = ZONE_CONFIG[zone]

    if zone == "safe":
        led.on()
    elif zone == "invalid":
        led.off()
    else:
        led.toggle()

    if config["beep_ms"] > 0:
        buzzer.duty_u16(BUZZER_DUTY)
        sleep_ms(config["beep_ms"])
        buzzer.duty_u16(0)

    sleep_ms(config["pause_ms"])


print("Proximity alarm ready. Stop with Ctrl+C.")
sleep_ms(1000)

try:
    while True:
        distance = measure_distance_cm()
        zone = classify_distance(distance)

        if distance is None:
            print("Distance: invalid | Zone:", zone)
        else:
            print("Distance:", round(distance, 1), "cm | Zone:", zone)

        alert_once(zone)
except KeyboardInterrupt:
    print("Stopped")
finally:
    trigger.off()
    led.off()
    buzzer.duty_u16(0)
    buzzer.deinit()

