#micropython script
#aviral

#controlling the neopixel led

import machine
import neopixel
import time

#object for neopixel
pixels=neopixel.NeoPixel(machine.Pin(48),1)


def moonlight_effect():
    for i in range(256):  # Gradually increase brightness
        for pixel in pixels:
            pixel[0] = i  # Set the red component
            pixel[1] = i  # Set the green component
            pixel[2] = i  # Set the blue component
        pixels.write()
        time.sleep(0.01)  # Adjust the speed of the effect

    for i in range(255, -1, -1):  # Gradually decrease brightness
        for pixel in pixels:
            pixel[0] = i
            pixel[1] = i
            pixel[2] = i
        pixels.write()
        time.sleep(0.01)
while True:
    try:
        moonlight_effect()

    except KeyboardInterrupt:
        print("Exit")
        break
    
        
        
        