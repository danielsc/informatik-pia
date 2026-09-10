from machine import ADC, Pin, PWM
from time import sleep_ms

POTENTIOMETER_PIN = 26
LED_PIN = 15

knob = ADC(POTENTIOMETER_PIN)
led = PWM(Pin(LED_PIN))
led.freq(1000)

print("Turn the knob. Stop with Ctrl+C.")

try:
    while True:
        raw_value = knob.read_u16()
        percent = int(raw_value / 65535 * 100)

        led.duty_u16(raw_value)
        print("Raw:", raw_value, "Brightness:", percent, "%")
        sleep_ms(100)
except KeyboardInterrupt:
    led.duty_u16(0)
    led.deinit()
    print("Stopped")

