#ESP32 PWM
#LED fading using PWM
#PWM can be enam=bled on all output enable pins
#the base frequency ranges from 1Hz to 40MHz
#but there is a trade off
#as the base frequency increases, the duty resolution decreases

from machine import Pin, Timer, PWM
from time import sleep_ms

#PWM object and its configuration
#PWM frequency = 1000 Hz

pwm = PWM(Pin(4),freq=1000)
pwm2 = PWM(Pin(2),freq=1000)

while True:
    #increse the LED brightness
    print("Incresing LED brightness")
    for i in range(0,1024):
        pwm.duty(1023-i)
        pwm2.duty(i)
        sleep_ms(2)
        i += 1
    print("LED is at its max brightness")
    #wait at max brightness for 2 sec
    sleep_ms(2000)
    
    #decrese the LED brightness
    print("Decreasing LED brightness")
    for i in range(0,1024):
        pwm.duty(i)
        pwm2.duty(1023-i)
        sleep_ms(2)
        i += 1
    print("LED is at its min brightness")
    #wait at min brightness for 2 sec
    sleep_ms(2000)