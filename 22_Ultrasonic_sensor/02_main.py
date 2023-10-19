import machine
import time

# Define the pins for the trigger and echo on your board
trigger_pin = machine.Pin(3, machine.Pin.OUT)
echo_pin = machine.Pin(9, machine.Pin.IN)

# Function to measure the distance using the ultrasonic sensor
def measure_distance():
    # Ensure the trigger pin is low for a short time to reset
    trigger_pin.off()
    time.sleep_us(2)

    # Generate a 10us pulse on the trigger pin to trigger the sensor
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()

    # Measure the pulse duration on the echo pin
    pulse_duration = machine.time_pulse_us(echo_pin, 1, 30000)

    # Calculate the distance in centimeters
    if pulse_duration > 0:
        distance = pulse_duration / 58
        return distance
    else:
        return None

try:
    while True:
        distance = measure_distance()
        if distance is not None:
            print("Distance: {:.2f} cm".format(distance))
        else:
            print("Sensor timeout")

        # Delay before taking the next measurement
        time.sleep(1)

except KeyboardInterrupt:
    pass
