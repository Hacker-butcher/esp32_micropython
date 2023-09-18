import machine
import time

# Define RGB LED pins
red_pin = machine.Pin(15, machine.Pin.OUT)
green_pin = machine.Pin(13, machine.Pin.OUT)
blue_pin = machine.Pin(12, machine.Pin.OUT)

# Define boot button pin and set it as an input with a pull-up resistor
button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Create PWM objects for each color
red_pwm = machine.PWM(red_pin, freq=500)
green_pwm = machine.PWM(green_pin, freq=500)
blue_pwm = machine.PWM(blue_pin, freq=500)

# Define color values
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # Red, Green, Blue

# Initialize color index
color_index = 0

# Function to set RGB color
def set_color(red, green, blue):
    red_pwm.duty(int(red * 1023))     # Scale 0-1 to 0-1023
    green_pwm.duty(int(green * 1023)) # Scale 0-1 to 0-1023
    blue_pwm.duty(int(blue * 1023))   # Scale 0-1 to 0-1023

# Function to change color when the button is pressed
def change_color(pin):
    global color_index
    color_index = (color_index + 1) % len(colors)
    set_color(*colors[color_index])

# Attach the button's interrupt handler
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=change_color)

# Initial color setting
set_color(*colors[color_index])

# Main loop
while True:
    # You can add other tasks or code here as needed
    time.sleep_ms(100)  # Small delay to avoid busy-waiting
