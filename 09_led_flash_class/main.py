import machine
import time

class Flasher:
    def __init__(self,pin,on_time,off_time):
        self.pin=pin
        self.on_time=on_time
        self.off_time=off_time
        self.led_state=0
        self.last_change=0
        self.led=machine.Pin(self.pin,machine.Pin.OUT)
    def update(self):
        if (time.ticks_ms()-self.last_change)>=self.off_time and self.led_state == 0:
            self.last_change=time.ticks_ms()
            self.led_state=1
            self.led.value(self.led_state)
            print(f"LED at Pin {self.pin} is On")
        elif (time.ticks_ms()-self.last_change)>=self.off_time and self.led_state == 1:
            self.last_change=time.ticks_ms()
            self.led_state=0
            self.led.value(self.led_state)
            print(f"LED at Pin {self.pin} is Off")
        
# object for led 1
led1=Flasher(8,400,600)
# object for led 2
led2=Flasher(47,1500,500)
#object for led 3
led3=Flasher(8,700,300)
# object for led 4
led4=Flasher(47,1300,700)

while True:
    try:
        led1.update()
        led2.update()
        led3.update()
        led4.update()
    except KeyboardInterrupt:
        print("Exit")
        break