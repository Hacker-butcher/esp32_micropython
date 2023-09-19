#micropython script
#aviral

#led blinking script

import machine
import time

#object for LED pin
led_pin=machine.Pin(8,machine.Pin.OUT)

while True:
    try:
        led_pin.on()
        #led_pin.value(1)
        print("LED is on")
        time.sleep(1)
        #led_pin.value(0)
        led_pin.off()
        print("LED is off")
        time.sleep(1)
        
    except KeyboardInterrupt:
        print("Exit")
        break
    
        