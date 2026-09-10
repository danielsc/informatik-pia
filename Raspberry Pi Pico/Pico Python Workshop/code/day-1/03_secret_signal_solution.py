from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

team_name = "Lunar Lighthouse"
short_flash = 0.15
long_flash = 0.55
inside_symbol_pause = 0.15
symbol_pause = 0.5

print("Sending SOS from", team_name)

# S: three short flashes
for flash in range(3):
    led.on()
    sleep(short_flash)
    led.off()
    sleep(inside_symbol_pause)

sleep(symbol_pause)

# O: three long flashes
for flash in range(3):
    led.on()
    sleep(long_flash)
    led.off()
    sleep(inside_symbol_pause)

sleep(symbol_pause)

# S: three short flashes
for flash in range(3):
    led.on()
    sleep(short_flash)
    led.off()
    sleep(inside_symbol_pause)

led.off()
print("Signal complete")

