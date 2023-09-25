import network
import time
import sys




#ssid="Semaphore"
#psk="Mrinal@16"

try:
    
    #object for wlan
    wlan=network.WLAN(network.AP_IF)
    #active wlan driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    wlan.config(essid="agESP", password="don't_remember", authmode=network.AUTH_WPA_WPA2_PSK)
except Exception as e:
    print(f"Error>{e}")
    
sys.exit()
    #wlan.connect(ssid,psk)
   # if wlan.isconnected()==True:
        #print(wlan.ifconfig())