import machine
import time
import onewire
import ds18x20

# Define the pin where the DS18B20 data line is connected
pin = machine.Pin(12)  # Replace with the appropriate GPIO pin

# Create a one-wire bus using the specified pin
ow = onewire.OneWire(pin)

# Create a DS18X20 sensor object
ds = ds18x20.DS18X20(ow)

# Scan for DS18B20 devices on the bus
roms = ds.scan()

while True:
    # Start a temperature conversion for all DS18B20 sensors
    ds.convert_temp()
    
    # Wait for the conversion to complete (750ms for DS18B20)
    time.sleep_ms(750)
    
    for rom in roms:
        # Read the temperature from the DS18B20 sensor
        temp = ds.read_temp(rom)
        
        # Print the temperature in Celsius
        print("Temperature (Celsius): {:.2f}".format(temp))
    
    time.sleep(5)  # Wait for 5 seconds before taking the next reading
