from machine import I2C, Pin
from PCF8591 import PCF8591

# Initialize the I2C bus
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust the pins and frequency as needed for your board

# Initialize the PCF8591
pcf8591 = PCF8591(0x48, i2c)  # Adjust the address if needed
if pcf8591.begin():
    print("PCF8591 found")

print("AIN0 ", pcf8591.voltage_read(PCF8591.AIN0))
print("AIN1 ", pcf8591.voltage_read(PCF8591.AIN1))
print("AIN2 ", pcf8591.voltage_read(PCF8591.AIN2))
print("AIN3 ", pcf8591.voltage_read(PCF8591.AIN3))
