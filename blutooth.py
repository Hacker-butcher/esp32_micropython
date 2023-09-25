import uos
import ubluetooth as bluetooth
import utime

# Check if Bluetooth is available and enable it
if uos.uname().sysname == "esp32s3":
    bluetooth.enable()
    print("Bluetooth enabled.")
else:
    print("Bluetooth is not available on this device.")

# Initialize Bluetooth stack
ble = bluetooth.BLE()

# Define the UUIDs for the service and characteristic
service_uuid = bluetooth.UUID(0x180F)  # Battery Service UUID
char_uuid = bluetooth.UUID(0x2A19)     # Battery Level Characteristic UUID

# Define a custom service
battery_service = (
    bluetooth.UUID(0x180F),
    [
        (bluetooth.UUID(0x2A19), bluetooth.FLAG_READ | bluetooth.FLAG_WRITE),
    ],
)

# Function to handle read requests on the characteristic
def on_read(connection_handle, char_uuid):
    if char_uuid == char_uuid:
        return bytes([battery_level])

# Function to handle write requests on the characteristic
def on_write(connection_handle, char_uuid, data):
    global battery_level
    if char_uuid == char_uuid:
        battery_level = data[0]
        print("Battery level set to:", battery_level)

# Set the read and write handlers
ble.irq(bluetooth.BLE_IRQ_CENTRAL_CONNECT, lambda _: print("Connected"))
ble.irq(bluetooth.BLE_IRQ_CENTRAL_DISCONNECT, lambda _: print("Disconnected"))
ble.irq(bluetooth.BLE_IRQ_GATTS_WRITE, on_write)
ble.irq(bluetooth.BLE_IRQ_GATTS_READ_REQUEST, on_read)

# Initialize the battery level
battery_level = 50

# Start advertising as a BLE peripheral
ble.active(True)
ble.gatts_register_services((battery_service,))
ble.gap_advertise(100, bytearray("\x02\x01\x06\x03\x03\x0F\x18"))

# Main loop
while True:
    utime.sleep(1)
