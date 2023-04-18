import utime
from PCF8591 import PCF8591

# Initialize the PCF8591
pcf8591 = PCF8591(0x48, scl=22, sda=21)  # Adjust the address if needed
if pcf8591.begin():
    print("PCF8591 found")

pcf8591.analog_write(255)
utime.sleep(1)
pcf8591.analog_write(128)
utime.sleep(1)
pcf8591.analog_write(0)
