from machine import Pin
from time import sleep_ms

LED_PIN = 15

led = Pin(LED_PIN, Pin.OUT)

print("The external LED on GP15 should blink once per second.")
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
