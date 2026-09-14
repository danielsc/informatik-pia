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
    while len(scores) < ROUNDS:
        print("\nRelease the button...")
        while not button.value():
            sleep_ms(10)

        wait_ms = randint(1000, 3000)
        print("Get ready...")
        sleep_ms(wait_ms)

        led.on()
        start_ms = ticks_ms()

        while button.value():
            sleep_ms(1)

        reaction_ms = ticks_diff(ticks_ms(), start_ms)
        led.off()
        scores.append(reaction_ms)

        if reaction_ms < 350:
            message = "Quick!"
        else:
            message = "Keep practising!"

        print("Reaction:", reaction_ms, "ms -", message)

        while not button.value():
            sleep_ms(10)

    print("\nScores:", scores)
    print("Fastest:", min(scores), "ms")
except KeyboardInterrupt:
    print("\nGame stopped")
finally:
    led.off()
