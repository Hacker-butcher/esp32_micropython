import time
from machine import Pin

# Define the pin numbers for the LEDs
led1_pin = 2  # GPIO2
led2_pin = 4  # GPIO4

# Initialize the LED pins as outputs
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

# Function to toggle between the LEDs
def toggle_leds():
    led1.value(not led1.value())
    led2.value(not led2.value())

# Initialize the first LED ON and the second LED OFF
led1.value(1)
led2.value(0)

# Blink the LEDs alternately in a loop
while True:
    toggle_leds()
    time.sleep(0.3)  # Wait for 1 second between each toggle
