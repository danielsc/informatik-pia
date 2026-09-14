from machine import Pin
from time import sleep_ms

led = Pin("LED", Pin.OUT)

print("The onboard LED should blink once per second.")
print("Stop with Ctrl+C.")

try:
    while True:
        led.on()
        print("LED on")
        sleep_ms(500)

        led.off()
        print("LED off")
        sleep_ms(500)
except KeyboardInterrupt:
    print("Stopped")
finally:
    led.off()
