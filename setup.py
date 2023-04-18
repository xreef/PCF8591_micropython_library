import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="pcf8591-library",
    package_dir={'': 'src'},
    py_modules=["PCF8591"],
    version="0.0.1",
    description="PCF8591, library for Arduino, Raspberry Pi Pico and rp2040 boards, esp32, SMT32 and ESP8266",
    long_description="Library to use pcf8591 i2c analog IC with Arduino, Raspberry Pi Pico and rp2040 boards, esp32, SMT32 and ESP8266. Can read analog value and write analog value with only 2 wire. ",
    keywords="micropython, digital, i2c, expander, pcf8591, pcf8591a, esp32, esp8266, stm32, SAMD, Arduino, wire, rp2040, Raspberry",
    url="https://github.com/xreef/PCF8591_micropython_library",
    author="Renzo Mischianti",
    author_email="renzo.mischianti@gmail.com",
    maintainer="Renzo Mischianti",
    maintainer_email="renzo.mischianti@gmail.com",
    license="MIT",
    install_requires=[],
    project_urls={
        'Documentation': 'https://www.mischianti.org/2019/01/03/pcf8591-i2c-analog-i-o-expander/',
        'Documentazione': 'https://www.mischianti.org/it/2019/01/03/pcf8591-un-expander-i2c-i-o-analogico/'
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)