#
# PCF8591 Analog GPIO Port Expand
#
# AUTHOR:  Renzo Mischianti
# Website: www.mischianti.org
# VERSION: 0.0.1
#
# Description:
# This script write an analog value on OUT of pcf8591
#
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
#
# Porting of PCF8591 library for Arduino
# https://www.mischianti.org/2019/01/03/pcf8591-i2c-analog-i-o-expander/
#

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
