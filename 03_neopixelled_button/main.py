#micropython script
#aviral

#controlling the neopixel led

import machine
import neopixel
import time

#object for neopixel
np=neopixel.NeoPixel(machine.Pin(48),1)


while True:
    try:
        np[0]=[255,0,0]
        np.write()
        time.sleep(0.1)
        np[0]=[0,255,0]
        np.write()
        time.sleep(0.1)
        np[0]=[0,0,255]
        np.write()
        time.sleep(0.1)
        np[0]=[255,255,0]
        np.write()
        time.sleep(0.1)
        np[0]=[128,0,128]
        np.write()
        time.sleep(0.1)
        np[0]=[255,0,255]
        np.write()
        time.sleep(0.1)
        np[0]=[255,192,203]
        np.write()
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exit")
        break
    
        