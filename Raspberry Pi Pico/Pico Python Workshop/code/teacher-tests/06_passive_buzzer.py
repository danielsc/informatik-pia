from machine import Pin, PWM
from time import sleep_ms

BUZZER_PIN = 15
QUIET_DUTY = 2500

buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0)

print("The passive buzzer should play three short, quiet pitches.")
print("Frequency changes pitch. Duty switches the sound on and off.")
print("Stop with Ctrl+C.")

try:
    while True:
        for frequency_hz in [800, 1200, 1600]:
            print("Pitch:", frequency_hz, "Hz")
            buzzer.freq(frequency_hz)
            buzzer.duty_u16(QUIET_DUTY)
            sleep_ms(180)
            buzzer.duty_u16(0)
            sleep_ms(500)
except KeyboardInterrupt:
    print("Stopped")
finally:
    buzzer.duty_u16(0)
    buzzer.deinit()
