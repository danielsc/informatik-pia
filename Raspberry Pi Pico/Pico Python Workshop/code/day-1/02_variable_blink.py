from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

message = "Team Comet"
flash_count = 6
on_time = 0.15
off_time = 0.35

print(message)

for flash_number in range(flash_count):
    print("Flash", flash_number + 1)
    led.on()
    sleep(on_time)
    led.off()
    sleep(off_time)

print("Signal complete")

