from machine import ADC
from time import sleep_ms

POTENTIOMETER_PIN = 26

knob = ADC(POTENTIOMETER_PIN)

print("Turn the potentiometer connected to GP26 / ADC0.")
print("Stop with Ctrl+C.")

try:
    while True:
        value = knob.read_u16()
        percent = value * 100 // 65535
        print("Raw:", value, "Position:", percent, "%")
        sleep_ms(150)
except KeyboardInterrupt:
    print("Stopped")
