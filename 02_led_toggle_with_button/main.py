#micropython script
#aviral

#led blinking script

import machine
import time

#object for LED pin
led=machine.Pin(8,machine.Pin.OUT)
#object for button
button=machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)

while True:
    try:
        if button.value()==0:
            led.value(not led.value())
            print("led is ON" if led.value() else "led is off")
            while button.value() ==0:
                time.sleep_ms(20)
    except KeyboardInterrupt:
        print("Exit")
        break
    
        