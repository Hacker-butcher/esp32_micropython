







#timer 2 has dedicated hardware PWM controller
#Timer 0, timer 1 and timer 3 can be used for various timing tasks

import machine


#object for led
led=machine.Pin(8,machine.Pin.OUT)
#object for timer
timer0=machine.Timer(0)

#method for handling ISR of timer
def timer0_isr(t):
    led.value(not led.value())
    print("LED is on" if led.value() else"LED is off")
    
#set the timer mode (intialize timer)
#timer can be start using timer0.start() and
#it can be stopped using timer0.stop() methods
#timer automatically starts with the initialization
    
timer0.init(mode=machine.Timer.PERIODIC, period=100, callback=timer0_isr)

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("EXIT")
        break