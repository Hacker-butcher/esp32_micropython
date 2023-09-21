import machine
import neopixel
import time

# Initialize the NeoPixel LED
np = neopixel.NeoPixel(machine.Pin(48), 1)

# Function to simulate the moonlight effect
def moonlight_effect():
    for i in range(256):  # Gradually increase brightness
        np[0] = (150, 0, i)  # Set the color to blue with increasing intensity (R, G, B)
        np.write()
        time.sleep_ms(10)  # Adjust the speed of the effect

    for i in range(255, -1, -1):  # Gradually decrease brightness
        np[0] = (150, 0, i)
        np.write()
        time.sleep_ms(10)

# Main loop
while True:
    try:
        moonlight_effect()
    except KeyboardInterrupt:
        print("Exit")
        break
