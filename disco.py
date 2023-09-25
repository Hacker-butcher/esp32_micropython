from machine import Pin, PWM
from time import sleep_ms
import random

class LEDController:
    def __init__(self, pins, freq=1000):
        self.leds = [PWM(Pin(pin), freq=freq) for pin in pins]

    def disco_light(self, num_iterations, min_flicker_delay_ms, max_flicker_delay_ms):
        for _ in range(num_iterations):
            # Randomly turn on and off LEDs
            for idx in range(len(self.leds)):
                if random.randint(0, 1) == 0:
                    self.turn_off(idx)
                else:
                    self.turn_on(idx)
            sleep_ms(random.randint(min_flicker_delay_ms, max_flicker_delay_ms))

    def turn_on(self, led_idx):
        self.leds[led_idx].duty(1023)

    def turn_off(self, led_idx):
        self.leds[led_idx].duty(0)

# Define the GPIO pins for your 5 LEDs (replace these with your specific pin numbers)
led_pins = [4, 6, 15, 17, 3]

# Create an instance of the LEDController class with the specified pins
led_controller = LEDController(led_pins)

# Run the disco light pattern with 10 iterations, minimum flicker delay of 50ms, and maximum flicker delay of 200ms
led_controller.disco_light(num_iterations=1000, min_flicker_delay_ms=10, max_flicker_delay_ms=100)

