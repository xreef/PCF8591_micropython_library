#            +---------------+
#  AIN0 (1)  | * 1    U   16 |  VDD
#  AIN1 (2)  | * 2        15 |  AOUT
#  AIN2 (3)  | * 3        14 |  VREF
#  AIN3 (4)  | * 4        13 |  AGND
#    A0 (5)  | * 5        12 |  EXT
#    A1 (6)  | * 6        11 |  OSC
#    A2 (7)  | * 7        10 |  SCL
#   VSS (8)  | * 8         9 |  SDA
#            +---------------+
#
# AIN0: Analog input channel 0
# AIN1: Analog input channel 1
# AIN2: Analog input channel 2
# AIN3: Analog input channel 3
# A0: Address input 0
# A1: Address input 1
# A2: Address input 2
# VSS: Ground
# SDA: Serial data line (I2C)
# SCL: Serial clock line (I2C)
# OSC: Oscillator output
# EXT: External trigger input
# AGND: Analog ground
# VREF: Voltage reference input
# AOUT: Analog output
# VDD: Power supply


import utime
from machine import I2C, Pin

AIN0 = CHANNEL0 = 0b00000000
AIN1 = CHANNEL1 = 0b00000001
AIN2 = CHANNEL2 = 0b00000010
AIN3 = CHANNEL3 = 0b00000011


class PCF8591:
    AIN0 = CHANNEL0 = 0b00000000
    AIN1 = CHANNEL1 = 0b00000001
    AIN2 = CHANNEL2 = 0b00000010
    AIN3 = CHANNEL3 = 0b00000011

    AUTOINCREMENT_READ = 0b00000100

    SINGLE_ENDED_INPUT = 0b00000000
    TREE_DIFFERENTIAL_INPUT = 0b00010000
    TWO_SINGLE_ONE_DIFFERENTIAL_INPUT = 0b00100000
    TWO_DIFFERENTIAL_INPUT = 0b00110000

    ENABLE_OUTPUT = 0b01000000
    DISABLE_OUTPUT = 0b00000000

    OUTPUT_MASK = 0b01000000

    def __init__(self, address, i2c=None, i2c_id=0, sda=None, scl=None):
        if i2c:
            self._i2c = i2c
        elif sda and scl:
            self._i2c = I2C(i2c_id, scl=Pin(scl), sda=Pin(sda))
        else:
            raise ValueError('Either i2c or sda and scl must be provided')

        self._address = address
        self._output_status = self.DISABLE_OUTPUT  # default

    def begin(self):
        if self._i2c.scan().count(self._address) == 0:
            # raise OSError('PCF8591 not found at I2C address {:#x}'.format(self._address))
            return False
        else:
            return True

    def analog_read_all(self, read_type=SINGLE_ENDED_INPUT):
        operation = self.AUTOINCREMENT_READ | read_type | (self._output_status & self.OUTPUT_MASK)
        self._i2c.writeto(self._address, bytearray([operation]))
        utime.sleep_ms(1)
        # data = self._i2c.readfrom(self._address, 5)
        data = []
        self._i2c.readfrom(self._address, 1)
        data.append(int.from_bytes(self._i2c.readfrom(self._address, 1), 'big'))
        data.append(int.from_bytes(self._i2c.readfrom(self._address, 1), 'big'))
        data.append(int.from_bytes(self._i2c.readfrom(self._address, 1), 'big'))
        data.append(int.from_bytes(self._i2c.readfrom(self._address, 1), 'big'))

        return data[0], data[1], data[2], data[3]

    def analog_read(self, channel, read_type=SINGLE_ENDED_INPUT):
        operation = channel | read_type | (self._output_status & self.OUTPUT_MASK)
        self._i2c.writeto(self._address, bytearray([operation]))
        utime.sleep_ms(1)
        data = self._i2c.readfrom(self._address, 2)
        return data[1]

    def voltage_read(self, channel, reference_voltage=3.3):
        voltage_ref = reference_voltage
        ana = self.analog_read(channel, self.SINGLE_ENDED_INPUT)
        return ana * voltage_ref / 255

    def voltage_write(self, value, reference_voltage=3.3):
        ana = value * 255 / reference_voltage
        self.analog_write(ana)

    def analog_write(self, value):
        if value > 255 or value < 0:
            Exception('Value must be between 0 and 255')

        self._output_status = self.ENABLE_OUTPUT

        self._i2c.writeto(self._address, bytearray([self.ENABLE_OUTPUT, value]))

    def disable_output(self):
        self._output_status = self.DISABLE_OUTPUT

        self._i2c.writeto(self._address, bytearray([self.DISABLE_OUTPUT]))
