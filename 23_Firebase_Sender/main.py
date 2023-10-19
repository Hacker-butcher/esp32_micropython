#fire base real time data management
#LED control using ultrasonic distance sensor
#sender for firebase

import machine
import network
import time
import sys
import urequests
import ujson

#create object for led pin
led = machine.Pin(2,machine.Pin.OUT)

# Define the GPIO pins for TRIG and ECHO
TRIG_PIN = 3
ECHO_PIN = 9

# Initialize the GPIO pins
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# Function to measure distance
def measure_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    while echo.value() == 0:
        pass
    pulse_start = time.ticks_us()
    while echo.value() == 1:
        pass
    pulse_end = time.ticks_us()
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration / 2) / 29.1  # Convert to centimeters
    return distance


# method to connect the esp32 with wi-fi and configure it as station device
def connect_wifi(ssid,psk,timeout):
    # object for wlan
    wlan = network.WLAN(network.STA_IF)
    # restart the wlan driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    # connect with wi-fi
    wlan.connect(ssid,psk)
    t = 0
    print("Connecting",end="")
    while (wlan.isconnected()==False) and (timeout-t>0):
        t += 1
        print(".",end="")
        time.sleep(1)
    if wlan.isconnected() == True:
        print("\nConnection established")
        print("The IP of ESP device is: ",wlan.ifconfig()[0])
        print(wlan)
        return wlan 
    else:
        print("\nCould not connect, try again")
        sys.exit()
        
connect_wifi("Tifac-Core","Tifac@akg321#",10)



# Firebase configuration
FIREBASE_URL = "https://esp32-f4164-default-rtdb.firebaseio.com/"  # Replace with your Firebase URL
FIREBASE_API_KEY = "AAIzaSyCYG_1U5z9HAQqf51ZkqxeBJPdYKD4CJnY"  # Replace with your Firebase API Key
NODE_PATH = "2"  # Node path to store button state

# Helper function to update the Firebase database
def update_firebase(value):
    data = {NODE_PATH: value}
    headers = {'Content-Type': 'application/json'}
    auth_url = f"{FIREBASE_URL}{NODE_PATH}.json?auth={FIREBASE_API_KEY}"
    response = urequests.put(auth_url, data=ujson.dumps(data), headers=headers)
    response.close()
    
while True:
    distance = measure_distance()
    print("DIstance :",distance)
    if distance <= 20:
        led.value(1)
        print("LED is turned on")
        update_firebase(1)
    else:
        led.value(0)
        print("LED is turned off")
        update_firebase(0)
    