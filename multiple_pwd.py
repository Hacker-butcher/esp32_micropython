from machine import Pin, PWM
from time import sleep_ms

class LEDController:
    def __init__(self, pins, freq=1000):
        self.leds = [PWM(Pin(pin), freq=freq) for pin in pins]

    def increase_brightness(self, led_idx):
        for i in range(0, 1024):
            self.leds[led_idx].duty(1023 - i)
            sleep_ms(2)
            i += 1

    def decrease_brightness(self, led_idx):
        for i in range(0, 1024):
            self.leds[led_idx].duty(i)
            sleep_ms(2)
            i += 1

    def run_pattern(self):
        while True:
            # Increase brightness
            for idx in range(len(self.leds)):
                self.increase_brightness(idx)
            # Wait at max brightness for 2 seconds
            sleep_ms(2000)

            # Decrease brightness
            for idx in range(len(self.leds)):
                self.decrease_brightness(idx)
            # Wait at min brightness for 2 seconds
            sleep_ms(2000)

# Define the GPIO pins for your 5 LEDs
led_pins = [4, 2, 15, 17, 6]  # Replace with the GPIO pins you're using

# Create an instance of the LEDController
led_controller = LEDController(led_pins)

# Run the LED pattern
led_controller.run_pattern()
