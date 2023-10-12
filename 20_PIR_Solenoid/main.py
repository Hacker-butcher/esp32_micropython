import machine
import time

# Define GPIO pin numbers for PIR sensor and relay
pir_pin = 17  # Replace with the actual GPIO pin number connected to the PIR sensor
relay_pin = 18  # Replace with the actual GPIO pin number connected to the relay

# Initialize the PIR sensor pin as an input
pir = machine.Pin(pir_pin, machine.Pin.IN)

# Initialize the relay pin as an output
relay = machine.Pin(relay_pin, machine.Pin.OUT)

# Configure settings
motion_detected = False
motion_timer = 0
motion_timeout = 5  # Time in seconds for consistent motion detection

try:
    while True:
        # Read the PIR sensor state
        pir_state = pir.value()

        if pir_state == 1:
            # PIR sensor detected motion
            if not motion_detected:
                motion_detected = True
                motion_timer = time.time()
            elif time.time() - motion_timer >= motion_timeout:
                # Consistent motion detected for the specified duration
                print("Motion detected! Unlocking the door...")
                
                # Turn on the relay (unlock the door)
                relay.on()
                
                # Wait for some time (e.g., 5 seconds)
                time.sleep(5)
                
                # Turn off the relay (lock the door)
                relay.off()
        else:
            # No motion detected
            motion_detected = False
        
        # Add a delay to avoid rapid sensor reading
        time.sleep(0.5)

except KeyboardInterrupt:
    # Terminate the program when Ctrl+C is pressed
    print("Program terminated by user")
