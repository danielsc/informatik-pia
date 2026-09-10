from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

team_name = "CHANGE ME"
short_flash = 0.2
long_flash = 0.6
symbol_pause = 0.4

print("Sending signal from", team_name)

# First symbol: short, short, short
led.on()
sleep(short_flash)
led.off()
sleep(short_flash)

# TODO: add two more short flashes.

sleep(symbol_pause)

# TODO: add your second and third symbols.
# Use long_flash for a long flash.

led.off()
print("Signal complete")

