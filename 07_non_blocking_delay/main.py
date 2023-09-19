import machine
import time


# variables
led_state=0
last_change=0
    
def led_toggle(pin, on_time,off_time):
    global led_state
    global last_change
    #object for led
    led=machine.Pin(pin,machine.Pin.OUT)
    if (time.ticks_ms()-last_change)>=off_time and led_state is 0:
        last_change=time.ticks_ms()
        led_state=1
        led.value(led_state)
        print("LED is on")
    elif (time.ticks_ms()-last_change)>=on_time and led_state is 1:
        last_change=time.ticks_ms()
        led_state=0
        led.value(led_state)
        print("LED is off")
        
while True:
    try:
        led_toggle(8,1000,2000)
    except KeyboardInterrupt:
        print("Exit")
        break
