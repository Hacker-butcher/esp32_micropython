#code for servo motor and soil moisture sensor with esp32s3

import machine
from machine import PWM
import time


# Define the PWM pin for the servo motor
servo_pin = machine.Pin(12, machine.Pin.OUT)
servo = PWM(servo_pin, freq=50)

# Define the ADC pin for the moisture sensor
#moisture_pin = machine.ADC(machine.Pin(4))
thresold = 2000

# Track the previous moisture level
previous_moisture_level = 0

# Function to read soil moisture level
def read_soil_moisture():
    adc = machine.ADC(machine.Pin(4))  # Pin number for ADC
    value = adc.read()
    return value
    print("Moisture Level :", value)
    
# Function to control the servo based on moisture level
def control_servo():
    global previous_moisture_level
    moisture_value = read_soil_moisture()
    print("Previous Moisture Level : ",previous_moisture_level)

    if moisture_value < thresold:
        # Soil is dry, water the plant and move the servo to 90 degrees
        servo.duty(123)  # Adjust the duty cycle to set servo position (0-1023)
        print("Moisture level is low. Watering the plant.")
    elif moisture_value >= thresold:
        # Soil is okay, move the servo to 0 degrees
        servo.duty(77)
        print("Moisture level is okay. No need to water the plant.")

    previous_moisture_level = moisture_value

try:
    while True:
        control_servo()
        time.sleep(1)  # Check moisture level every 60 seconds

except KeyboardInterrupt:
    servo.duty(0)  # Stop the servo when the program is interrupted