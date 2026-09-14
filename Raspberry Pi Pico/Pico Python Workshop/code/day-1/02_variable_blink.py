from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

message = "Team Comet"
on_time = 0.15
off_time = 0.35

print(message)

print("Flash 1")
led.on()
sleep(on_time)
led.off()
sleep(off_time)

print("Flash 2")
led.on()
sleep(on_time)
led.off()
sleep(off_time)

print("Flash 3")
led.on()
sleep(on_time)
led.off()
sleep(off_time)

print("Signal complete")
