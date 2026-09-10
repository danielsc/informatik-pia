from machine import Pin, PWM
from time import sleep_ms

BUZZER_PIN = 15
QUIET_DUTY = 2500

buzzer = PWM(Pin(BUZZER_PIN))
buzzer.freq(1800)
buzzer.duty_u16(0)


def beep(frequency_hz, duration_ms):
    buzzer.freq(frequency_hz)
    buzzer.duty_u16(QUIET_DUTY)
    sleep_ms(duration_ms)
    buzzer.duty_u16(0)


print("Three brief tones. Stop with Ctrl+C.")

try:
    for frequency in [1200, 1600, 2000]:
        print(frequency, "Hz")
        beep(frequency, 120)
        sleep_ms(350)
except KeyboardInterrupt:
    print("Stopped")
finally:
    buzzer.duty_u16(0)
    buzzer.deinit()

