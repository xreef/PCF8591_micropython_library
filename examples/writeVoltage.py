from machine import I2C, Pin
import utime
from PCF8591 import PCF8591  # Make sure the PCF8591 class is in your MicroPython filesystem as pcf8591.py
from PCF8591 import AIN0, AIN1, AIN2, AIN3
from PCF8591 import CHANNEL1

# Initialize the I2C bus
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust the pins and frequency as needed for your board

# Initialize the PCF8591
pcf8591 = PCF8591(0x48, i2c)  # Adjust the address if needed
if pcf8591.begin():
    print("PCF8591 found")

pcf8591.voltage_write(3.3)
utime.sleep(1)
pcf8591.voltage_write(1.65)
utime.sleep(1)
pcf8591.voltage_write(0)
