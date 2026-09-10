from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

print("Three...")
led.on()
sleep(1)

print("Two...")
led.off()
sleep(1)

print("One...")
led.on()
print("Hello, physical world!")
sleep(1)

led.off()

