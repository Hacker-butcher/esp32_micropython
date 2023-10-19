import machine
import time

# Define the GPIO pins for TRIG and ECHO
TRIG_PIN = 3
ECHO_PIN = 9

# Initialize the GPIO pins
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# Function to measure distance
def measure_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    while echo.value() == 0:
        pass
    pulse_start = time.ticks_us()
    while echo.value() == 1:
        pass
    pulse_end = time.ticks_us()
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration / 2) / 29.1  # Convert to centimeters
    return distance

while True:
    distance = measure_distance()
    print("Distance: {:.2f} cm".format(distance))
    time.sleep(1)  # Wait for a second before the next measurement
