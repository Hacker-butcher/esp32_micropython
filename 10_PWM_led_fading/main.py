from machine import Pin, Timer, PWM
from time import sleep_ms

# pwm object and its configuration
#pwm frequency = 1000Hz
pwm2=PWM(Pin(2),freq=1000)

while True:
    #increase the LED brightness
    print("Increasing LED brightness...")
    for i in range (0,1024):
        pwm2.duty(i)
        sleep_ms(1)
        i += 1
    print(" LED is at its max brightness")
    
    # wait at max brightness for 2 sec
    sleep_ms(100)
    # decrese the LED brightness
    print("Decreasing LED brightness")
    for i in range(0,1024):
        pwm2.duty(1023-i)
        sleep_ms(1)
        i += 1
    print("LED is at its min brightness")
    #wait at min brightness for 2 sec
    sleep_ms(100)