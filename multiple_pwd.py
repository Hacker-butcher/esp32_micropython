from machine import Pin, PWM
from time import sleep_ms

class LEDController:
    def __init__(self, pins, freq=1000):
        self.leds = [PWM(Pin(pin), freq=freq) for pin in pins]

    def pulse_pattern(self, num_pulses, pulse_duration_ms):
        for _ in range(num_pulses):
            # Increase brightness for all LEDs
            for idx in range(len(self.leds)):
                self.increase_brightness(idx)
            sleep_ms(pulse_duration_ms)

            # Decrease brightness for all LEDs
            for idx in range(len(self.leds)):
                self.decrease_brightness(idx)
            sleep_ms(pulse_duration_ms)

    def increase_brightness(self, led_idx):
        for i in range(0, 1024):
            self.leds[led_idx].duty(1023 - i)
            sleep_ms(2)
            i += 1

    def decrease_brightness(self, led_idx):
        for i in range(0, 1024):
            self.leds[led_idx].duty(i)
            sleep_ms(6)
            i += 1

    def run_fade(self):
        while True:
            for idx in range(len(self.leds)):
                self.increase_brightness(idx)
            sleep_ms(2)

            for idx in range(len(self.leds)):
                self.decrease_brightness(idx)
            sleep_ms(1)

# Define the GPIO pins for your 5 LEDs (replace these with your specific pin numbers)
led_pins = [4, 6, 15, 17, 3]

# Create an instance of the LEDController class with the specified pins
led_controller = LEDController(led_pins)

# Run the pulse pattern with 5 pulses and a pulse duration of 1000ms (1 second)
led_controller.pulse_pattern(num_pulses=5, pulse_duration_ms=100)
