import machine
import time

# Define GPIO pin numbers for PIR sensor and relay

pir_pin = 17  # Replace with the actual GPIO pin number connected to the PIR sensor
relay_pin = 18  # Replace with the actual GPIO pin number connected to the relay

# Initialize the PIR sensor pin as an input
pir = machine.Pin(pir_pin, machine.Pin.IN)

# Initialize the relay pin as an output
relay = machine.Pin(relay_pin, machine.Pin.OUT)

try:
    while True:
        # Read the PIR sensor state
        pir_state = pir.value()

        if pir_state == 1:
            # PIR sensor detected motion
            print("Motion detected! Activating the solenoid...")
            
            # Turn on the relay (activate the solenoid)
            relay.on()
            
            # Wait for some time (e.g., 5 seconds)
            time.sleep(5)
            
            # Turn off the relay (deactivate the solenoid)
            relay.off()
        else:
            # No motion detected
            print("No motion detected.")
        
        # Add a delay to avoid rapid sensor reading
        time.sleep(1)

except KeyboardInterrupt:
    # Terminate the program when Ctrl+C is pressed
    print("Program terminated by user")
