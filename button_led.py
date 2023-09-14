from machine import Pin
led=Pin(2,Pin.OUT)
button=Pin(0,Pin.IN)
while True:
    if not button.value():
        led.value(not led.value())
        print("LED turned on" if led.value() else "LED turned off")
        
        while not button.value():
            pass