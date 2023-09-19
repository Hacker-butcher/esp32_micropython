import machine
import time

# Variables
led_state_1 = 0
led_state_2 = 0
last_change_1 = 0
last_change_2 = 0

def led_toggle(pin_1, pin_2, on_time, off_time):
    global led_state_1, led_state_2, last_change_1, last_change_2

    # Object for LED 1
    led_1 = machine.Pin(pin_1, machine.Pin.OUT)

    # Object for LED 2
    led_2 = machine.Pin(pin_2, machine.Pin.OUT)

    current_time = time.ticks_ms()

    # Check LED 1 state and time
    if (current_time - last_change_1) >= off_time and led_state_1 == 0:
        last_change_1 = current_time
        led_state_1 = 1
        led_1.value(led_state_1)
        print("LED 1 is on")

    if (current_time - last_change_1) >= on_time and led_state_1 == 1:
        last_change_1 = current_time
        led_state_1 = 0
        led_1.value(led_state_1)
        print("LED 1 is off")

    # Check LED 2 state and time
    if (current_time - last_change_2) >= off_time and led_state_2 == 0:
        last_change_2 = current_time
        led_state_2 = 1
        led_2.value(led_state_2)
        print("LED 2 is on")

    if (current_time - last_change_2) >= on_time and led_state_2 == 1:
        last_change_2 = current_time
        led_state_2 = 0
        led_2.value(led_state_2)
        print("LED 2 is off")

while True:
    try:
        led_toggle(8, 9, 100, 200)  # Use pins 8 and 9 for two LEDs, with on_time and off_time intervals
    except KeyboardInterrupt:
        print("Exit")
        break
