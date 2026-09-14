from machine import Pin
from random import randint
from time import sleep_ms, ticks_diff, ticks_ms

BUTTON_PIN = 13
LED_PIN = 15
ROUNDS = 5

button = Pin(BUTTON_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)
scores = []

print("Reaction-Time Challenge")
print("Press only after the LED turns on.")

try:
    while len(scores) < ROUNDS:
        round_number = len(scores) + 1
        print("\nRound", round_number, "of", ROUNDS)
        print("Release the button...")

        while not button.value():
            sleep_ms(10)

        wait_ms = randint(1500, 4000)
        wait_started_ms = ticks_ms()
        false_start = False
        print("Get ready...")

        while ticks_diff(ticks_ms(), wait_started_ms) < wait_ms:
            if not button.value():
                false_start = True
                break
            sleep_ms(10)

        if false_start:
            print("False start! This round does not count.")
            while not button.value():
                sleep_ms(10)
            continue

        led.on()
        start_ms = ticks_ms()

        while button.value():
            sleep_ms(1)

        reaction_ms = ticks_diff(ticks_ms(), start_ms)
        led.off()
        scores.append(reaction_ms)

        if reaction_ms < 250:
            message = "Lightning fast!"
        elif reaction_ms < 450:
            message = "Quick!"
        else:
            message = "Keep practising!"

        print("Reaction:", reaction_ms, "ms -", message)
        print("Scores:", scores)

        while not button.value():
            sleep_ms(10)

    average_ms = sum(scores) / len(scores)
    print("\nGame complete")
    print("Fastest:", min(scores), "ms")
    print("Average:", int(average_ms), "ms")
except KeyboardInterrupt:
    print("\nGame stopped")
finally:
    led.off()
