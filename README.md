<div>
<a href="https://www.mischianti.org/forums/forum/mischiantis-libraries/pcf8591-i2c-analog-expander/"><img
  src="https://github.com/xreef/LoRa_E32_Series_Library/raw/master/resources/buttonSupportForumEnglish.png" alt="Support forum pcf8591 English"
   align="right"></a>
</div>
<div>
<a href="https://www.mischianti.org/it/forums/forum/le-librerie-di-mischianti/pcf8591-expander-analogico-i2c/"><img
  src="https://github.com/xreef/LoRa_E32_Series_Library/raw/master/resources/buttonSupportForumItaliano.png" alt="Forum supporto pcf8591 italiano"
  align="right"></a>
</div>

#
#### www.mischianti.org

### MicroPython Library to use i2c analog IC with arduino and esp8266. Can read analog value and write analog value with only 2 wire (perfect for ESP-01).

#### Changelog
 - 07/11/2023: v0.0.3 Fix on read when write is active and running [#Forum](https://mischianti.org/forums/topic/micropython-i2c-pcf8591-round-value-problem-raspberry-pi-pico/#post-28043)
 - 16/05/2023: v0.0.2 Minor fix on read and write [#Forum](https://www.mischianti.org/forums/topic/micropython-i2c-pcf8591-round-value-problem-raspberry-pi-pico/)
 - 18/04/2023: v0.0.1 Initial commit of stable version.

I try to simplify the use of this IC, with a minimal set of operation.

#### Installation
To install the library execute the following command:

```bash
pip install pcf8591-library
```

**Constructor:**
Pass the address of I2C 
```python
from PCF8591 import PCF8591
from machine import I2C, Pin
    
# Initialize the I2C bus
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  

# Initialize the PCF8591
pcf8591 = PCF8591(0x48, i2c)
if pcf8591.begin():
    print("PCF8591 found")

```
or
```python
from PCF8591 import PCF8591

pcf8591 = PCF8591(0x48, sda=21, scl=22)
if pcf8591.begin():
    print("PCF8591 found")

```

To read all analog input in one 
```python
# Main loop
while True:
    # Read all analog input channels
    ain0, ain1, ain2, ain3 = pcf8591.analog_read_all()

    # Print the results
    print("AIN0:", ain0, "AIN1:", ain1, "AIN2:", ain2, "AIN3:", ain3)

    # Wait for 1 second
    utime.sleep(1)
```

If you want to read a single input:
```python
print("AIN0 ", pcf8591.analog_read(PCF8591.AIN0))
print("AIN1 ", pcf8591.analog_read(PCF8591.AIN1))
print("AIN2 ", pcf8591.analog_read(PCF8591.AIN2))
print("AIN3 ", pcf8591.analog_read(PCF8591.AIN3))
```

If you want to write a value:
```python
pcf8591.analog_write(255)
utime.sleep(1)
pcf8591.analog_write(128)
utime.sleep(1)
pcf8591.analog_write(0)
```

You can also read and write voltage

```python
pcf8591.voltage_write(3.3)
utime.sleep(1)
pcf8591.voltage_write(1.65)
utime.sleep(1)
pcf8591.voltage_write(0)
```
or
```python
print("AIN0 ", pcf8591.voltage_read(PCF8591.AIN0))
print("AIN1 ", pcf8591.voltage_read(PCF8591.AIN1))
print("AIN2 ", pcf8591.voltage_read(PCF8591.AIN2))
print("AIN3 ", pcf8591.voltage_read(PCF8591.AIN3))
```


For the examples I use this wire schema on breadboard:
![esp32 and pcf8591 wiring](https://www.mischianti.org/wp-content/uploads/2023/04/esp32-pcf8591-wiring_bb.jpg)