from machine import I2C, Pin
import utime
from PCF8591 import PCF8591 

# Initialize the I2C bus
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust the pins and frequency as needed for your board

# Initialize the PCF8591
pcf8591 = PCF8591(0x48, i2c)  # Adjust the address if needed
if pcf8591.begin():
    print("PCF8591 found")

# Main loop
while True:
    # Read all analog input channels
    ain0, ain1, ain2, ain3 = pcf8591.analog_read_all()

    # Print the results
    print("AIN0:", ain0, "AIN1:", ain1, "AIN2:", ain2, "AIN3:", ain3)

    # Wait for 1 second
    utime.sleep(1)
