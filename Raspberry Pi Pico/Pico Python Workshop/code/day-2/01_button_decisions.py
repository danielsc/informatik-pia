from machine import Pin
from time import sleep_ms

BUTTON_PIN = 13
LED_PIN = 15

button = Pin(BUTTON_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)

print("Press the button. Stop with Ctrl+C.")

try:
    while True:
        pressed = not button.value()

        if pressed:
            led.on()
            print("Pressed: ", pressed)
        else:
            led.off()

        sleep_ms(50)
except KeyboardInterrupt:
    led.off()
    print("Stopped")

