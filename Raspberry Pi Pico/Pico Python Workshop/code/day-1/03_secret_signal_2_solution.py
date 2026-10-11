from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

team_name = "Lunar Lighthouse"
short_flash = 0.15
long_flash = 0.55
between_flash_pause = 0.15
group_pause = 0.5

print("Sending SOS from", team_name)

# S: three short flashes
led.on()
sleep(short_flash)
led.off()
sleep(between_flash_pause)
led.on()
sleep(short_flash)
led.off()
sleep(between_flash_pause)
led.on()
sleep(short_flash)
led.off()
sleep(between_flash_pause)

sleep(group_pause)

# O: three long flashes
led.on()
sleep(long_flash)
led.off()
sleep(between_flash_pause)
led.on()
sleep(long_flash)
led.off()
sleep(between_flash_pause)
led.on()
sleep(long_flash)
led.off()
sleep(between_flash_pause)

sleep(group_pause)

# S: three short flashes
led.on()
sleep(short_flash)
led.off()
sleep(between_flash_pause)
led.on()
sleep(short_flash)
led.off()
sleep(between_flash_pause)
led.on()
sleep(short_flash)
led.off()
sleep(between_flash_pause)

led.off()
print("Signal complete")
