from machine import Pin
from time import sleep_ms

BUTTON_PIN = 13

button = Pin(BUTTON_PIN, Pin.IN)
was_pressed = None

print("Press and release the button on GP13.")
print("Stop with Ctrl+C.")

try:
    while True:
        pressed = not button.value()

        if pressed != was_pressed:
            print("Pressed:", pressed)
            was_pressed = pressed

        sleep_ms(20)
except KeyboardInterrupt:
    print("Stopped")
