from machine import Pin
from random import randint
from time import sleep_ms, ticks_diff, ticks_ms

BUTTON_PIN = 13
LED_PIN = 15
ROUNDS = 3

button = Pin(BUTTON_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)
scores = []

print("Reaction-Time Challenge")
print("Press only after the LED turns on.")

try:
    # Build the game here.
    #
    # 1. Repeat until scores contains ROUNDS results.
    # 2. Wait until the button is released.
    # 3. Wait a random time.
    # 4. Turn on the LED and remember the start time.
    # 5. Wait until the button is pressed.
    # 6. Calculate reaction_ms and turn off the LED.
    # 7. Append reaction_ms and classify the result.
    pass
except KeyboardInterrupt:
    print("\nGame stopped")
finally:
    led.off()
