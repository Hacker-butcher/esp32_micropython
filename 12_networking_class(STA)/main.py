import network
import time
import sys

wlan=network.WLAN(network.STA_IF)

wlan.active(False)
time.sleep(1)
wlan.active(True)

#ssid="Semaphore"
#psk="Mrinal@16"

try:
    networks=wlan.scan()
    print(networks)
except Exception as e:
    print(f"Error>{e}")
    
sys.exit()
    #wlan.connect(ssid,psk)
   # if wlan.isconnected()==True:
        #print(wlan.ifconfig())